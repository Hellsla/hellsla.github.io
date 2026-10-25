VERDICT: PASS
CONTENT-HASH: 22aa2b4fe3ce9aa9

## Blocking
(none)

## Polish
- tests/sims/fy3-6.json — canvas drawing (curves, T line, vessel colours, label collisions) has no assertion; only simState and DOM text are checked. Acceptable, canvas pixels are not part of the spec contract.
- tests/sims/fy3-6.json — the time-based checks (8 s and 2,5 s waits) make the run slow (about 13 s) but were stable in three runs.

## Checked
- `PASS preview/fy3-6  [] []` (run three times, identical; no console or page error; simState present)
- lint_lesson.py fy3-6: 0 errors, 0 warnings (not repeated). Hash before and after the review: 22aa2b4fe3ce9aa9 (unchanged during review; round 1 verdict was on cf3db0d4e8955bff)
- 45 assertions, all pass; every simState key in sim-spec.md (mW, TW0, cB, mB, TB0, Teq, CW, CB, Q, running) is asserted; all five sliders, the select (options, no ice) and the Upota button are covered
- Formula sim.js:51 Teq = (C_W·T_W0 + C_B·T_B0)/(C_W + C_B), c_W = 4190, matches lesson.md (c₁m₁(T₁ − T) = c₂m₂(T − T₂), solved for T); Q = c_B m_B (T_B0 − T) equals c_W m_W (T − T_W0) for hot and cold bodies (assertions 15, 22)
- Round-1 gap closed: assertions 43 and 44 (equal start temperatures: Q = 0, Teq = 40, readout says no heat flows)
- Assertion 45 (DOM order: Upota first control, controls before readout) passes. Independent measurement: canvas top to Upota bottom is 244 px at 360x740, 291 px at 390x740, 475 px at 1280; button height 40 px; scrollWidth - innerWidth = 0 at all three widths; no console errors at any width
- Math.min(p.deltaTime, 100) clamp present at sim.js:63 (animation step); assertions 34-36 confirm the run stops at 10 s with both bodies exactly at Teq
- Animation reset on slider change (assertions 40, 41) and no animation before Upota (2, 3) pass
- Worked example (24,6 °C model value vs 24,5 °C measured in lesson) is covered by assertions 10 and 11 with the tolerance noted
