# Example Issue

Title: Reject malformed event records before scoring

Context:
The scorer accepts event records from multiple sources. Malformed records should be rejected before ranking.

Input:
- `candidates: list[dict]`
- each candidate must include `id`, `timestamp`, `description`, and `causal_claim`

Output:
- valid candidates are passed to scoring
- invalid candidates produce `invalid_event_record`

Rules:
- timestamp must be parseable
- causal_claim must be non-empty
- rejection must be deterministic

Constraints:
- do not infer missing timestamps
- return JSON-compatible error records

Acceptance:
- malformed records are rejected with stable reason
- valid records still score normally

Verification:
- red test: malformed record currently reaches scorer
- green test: malformed record rejected before scorer

Micro-plan:
1. Add failing test for missing timestamp.
2. Add validation function.
3. Re-run focused test.
4. Run full pytest.

