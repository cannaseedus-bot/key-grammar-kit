#include "fold_direction.h"
#include "../util/json.h"
#include <algorithm>
#include <chrono>
#include <ctime>
#include <optional>

namespace khanary::kuhul {

namespace {

std::string iso8601_now() {
    const auto tt = std::chrono::system_clock::to_time_t(std::chrono::system_clock::now());
    struct tm tm_buf{};
    localtime_s(&tm_buf, &tt);
    char buf[32];
    std::strftime(buf, sizeof(buf), "%Y-%m-%dT%H:%M:%S", &tm_buf);
    return std::string(buf);
}

float jaccard(const std::vector<std::string>& A, const std::vector<std::string>& B) {
    if (A.empty() && B.empty()) return 0.0f;
    std::unordered_set<std::string> set_b(B.begin(), B.end());
    size_t intersection = 0;
    for (const auto& a : A)
        if (set_b.count(a)) ++intersection;
    const size_t union_sz = A.size() + B.size() - intersection;
    return union_sz ? static_cast<float>(intersection) / static_cast<float>(union_sz) : 0.0f;
}

// Deserialise a "fold_delta" JROM payload back into a FoldDelta.
// Returns nullopt if the payload is malformed or verdict != "GOOD".
std::optional<FoldDelta> parse_fold_delta_payload(
    const std::string& json_str, uint64_t seq)
{
    const auto root = util::parse(json_str);
    if (!root || !root->is_object()) return std::nullopt;

    const auto mid     = root->get_string("micronaut_id");
    const auto verdict = root->get_string("verdict");
    const auto ext_at  = root->get_string("extracted_at");

    if (!mid || mid->empty()) return std::nullopt;
    if (!verdict || *verdict != "GOOD") return std::nullopt;

    FoldDelta delta;
    delta.micronaut_id  = *mid;
    delta.verdict       = *verdict;
    delta.extracted_at  = ext_at.value_or("");
    delta.jrom_seq      = seq;
    delta.weights.micronaut_id    = *mid;
    delta.confidence.micronaut_id = *mid;

    if (const auto dw = root->get_number("delta_W"))
        delta.weights.delta_W = static_cast<float>(*dw);
    if (const auto dc = root->get_number("delta_C"))
        delta.confidence.delta_C = static_cast<float>(*dc);

    if (const auto* caps = root->get("added_capabilities"); caps && caps->is_array()) {
        for (const auto& item : caps->as_array()) {
            if (!item || !item->is_string()) continue;
            const auto& tok = item->as_string();
            if (!tok.empty())
                delta.relations.added_capabilities.push_back({*mid, tok});
        }
    }

    if (const auto* govs = root->get("added_governs"); govs && govs->is_array()) {
        for (const auto& item : govs->as_array()) {
            if (!item || !item->is_string()) continue;
            const auto& tok = item->as_string();
            if (!tok.empty())
                delta.relations.added_governs.push_back({*mid, tok});
        }
    }

    return delta;
}

} // anonymous namespace

bool DirectionStore::ingest(const FoldDelta& delta) {
    if (delta.verdict != "GOOD") return false;
    if (delta.micronaut_id.empty()) return false;

    std::lock_guard<std::mutex> lock(mtx_);

    auto& dir = store_[delta.micronaut_id];

    // Idempotency: skip already-seen jrom_seq. jrom_seq == 0 means the delta
    // was constructed without JROM logging — allowed but the replay idempotency
    // guarantee does not apply.
    if (delta.jrom_seq != 0 && dir.source_jrom_seqs.count(delta.jrom_seq))
        return false;

    dir.id = delta.micronaut_id;

    // PrincipalDirection for discrete capability tokens = sorted union/consensus.
    // "Union" because capabilities from different GOOD episodes each verified a
    // real extension — the full set is the stable profile of this direction.
    for (const auto& e : delta.relations.added_capabilities) {
        if (e.cap_token.empty()) continue;
        if (std::find(dir.capability_key.begin(), dir.capability_key.end(), e.cap_token)
                == dir.capability_key.end())
            dir.capability_key.push_back(e.cap_token);
    }
    std::sort(dir.capability_key.begin(), dir.capability_key.end());

    for (const auto& e : delta.relations.added_governs) {
        if (e.scope_token.empty()) continue;
        if (std::find(dir.governs_key.begin(), dir.governs_key.end(), e.scope_token)
                == dir.governs_key.end())
            dir.governs_key.push_back(e.scope_token);
    }
    std::sort(dir.governs_key.begin(), dir.governs_key.end());

    // W and C remain at neutral priors (1.0, 0.5).
    // This store only ever sees GOOD verdicts — updating W or C here would
    // create a ratchet that rises but never falls. Verdict-driven reinforcement
    // (which must observe BAD verdicts too) is a separate future component.

    if (delta.jrom_seq != 0) dir.source_jrom_seqs.insert(delta.jrom_seq);
    ++dir.episode_count;
    if (!delta.extracted_at.empty()) dir.last_updated = delta.extracted_at;

    return true;
}

uint32_t DirectionStore::rebuild_from_jrom(const io::JROM& jrom) {
    uint32_t ingested = 0;
    jrom.replay(0, [&](const io::JROMEvent& ev) {
        if (ev.type != "fold_delta") return;
        const auto delta = parse_fold_delta_payload(ev.payload_json, ev.seq);
        if (!delta) return;
        if (ingest(*delta)) ++ingested;
    });
    return ingested;
}

std::vector<DirectionStore::QueryResult> DirectionStore::query(
    const std::vector<std::string>& query_caps, float min_score) const
{
    std::lock_guard<std::mutex> lock(mtx_);

    std::vector<QueryResult> results;
    results.reserve(store_.size());

    for (const auto& [id, dir] : store_) {
        if (dir.capability_key.empty()) continue;
        const float R     = jaccard(query_caps, dir.capability_key);
        const float score = dir.W * dir.C * R;
        if (score < min_score) continue;
        results.push_back({id, R, score, dir});
    }

    std::sort(results.begin(), results.end(),
        [](const QueryResult& a, const QueryResult& b) { return a.score > b.score; });

    return results;
}

const FoldDirection* DirectionStore::get(const std::string& id) const {
    std::lock_guard<std::mutex> lock(mtx_);
    const auto it = store_.find(id);
    return (it != store_.end()) ? &it->second : nullptr;
}

std::vector<std::string> DirectionStore::list() const {
    std::lock_guard<std::mutex> lock(mtx_);
    std::vector<std::string> keys;
    keys.reserve(store_.size());
    for (const auto& [id, _] : store_) keys.push_back(id);
    return keys;
}

size_t DirectionStore::size() const {
    std::lock_guard<std::mutex> lock(mtx_);
    return store_.size();
}

} // namespace khanary::kuhul
