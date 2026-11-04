VERDICT: PASS
CONTENT-HASH: 7ae87cbc6cfd7f44

## Blocking

## Polish
- solutions.md:98 (L3-01) — the task says to round intermediate angles to hundredths, but the shown products come from unrounded angles: 1.5143 · sin 22.16° = 0.57119 (α4 = 34.83°), not 0.57127 (34.84°); violet gives 0.58509 (35.81°). A student who follows the instruction gets 0.98°. The key 0.9659 with 2 % tolerance accepts 0.98, so this is not blocking. Fix: show the values from the rounded angles and say that rounding gives 0.96–0.98°. Alternatively, drop the rounding instruction.
- review/packet-science.md:57 — the exercise brief is still empty for en, a review_packet.py heading-match issue, not a content finding.

## Checked
- The \text{p} → \text{r} change is applied consistently across solutions.md (14 occurrences, no \text{p} left) and agrees with the en lesson.
- Recomputed from task text (scratchpad sci/recompute_r2.py): L1 35.107°, 196 078 km/s, 1.5161, 37.0°, 42.0°; L2 265.0 ns, 34.983°, 15.646°; L3 0.9659°, 30.703°, 1.665° (key 1.6647).
- L2-03: the reading 1.639 gives 183 038 km/s, and the key 183 072 comes from 1.6387, which is within tolerance.
- Task data are physically consistent: L1-05 implies n = 1.331 (water). L1-04's 52.0° implies n ≈ 1.50, a plausible glass.
- L2-01 states v = c : n and names group velocity as what is ignored. L2-04 uses top = θ − h. L3-02: 30.7° < 42.3°, so the point is inside the arc.
- Symbolic-first steps, rounding reasons (difference of nearly equal numbers) and units are correct in every solution.
