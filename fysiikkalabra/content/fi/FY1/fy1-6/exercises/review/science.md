VERDICT: PASS
CONTENT-HASH: 6f11aaaecc7f8a5d
Round: 3. Checked the round-2 Blocking fix (commit 094aa590, solutions.md L2-07 Annettu). Everything else is unchanged since round 2, so the round-2 checks still apply.

## Blocking
(none)

## Polish
- exercises.json:243 (L2-07) — "valon katkos on puolivälissä, eli kappaleen keskikohta on portin kohdalla": for an accelerating body these are not the same moment (the centre passes 0,38 ms after the mid-time at gate 1 and 0,03 ms after it at gate 2; this changes g by 0,14 %) — drop the "eli …" clause or write "suunnilleen silloin, kun keskikohta on portin kohdalla".
- exercises.json:359 (L3-05) — v = 24,5 m/s after 2,5 s means a 31 m drop, and the task does not say air resistance is negligible — add "ilmanvastus jätetään huomiotta" (or use smaller times).
- exercises.json:359 vs :197 (L3-05 vs L2-06) — both grade a clock offset found from a straight (t, v) line (t₀ = 0,20 s and 0,15 s) — consider grading g or the trend in the ratios in L3-05 instead.
- exercises.json:44 (L1-06) — carried over from round 1: the same idea as L3-01; one distractor set in air (a feather and a hammer on Earth) would separate them.

## Checked
- Hash 6f11aaaecc7f8a5d at the start and at the end.
- Round-2 Blocking (L2-07 Annettu): resolved. solutions.md:167 now says "valokatkoksen puolivälin hetki" for t₁ and t₂. This matches the task text and the Periaate (where L/Δt equals the instantaneous speed). No numbers changed, so g stays as checked in round 2.
- Round 1 and round 2 checks carried over: all 16 numeric answers were recomputed and are within tolerance, and answers.py agrees.
