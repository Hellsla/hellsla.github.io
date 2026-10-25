VERDICT: PASS
CONTENT-HASH: 8a415710a3012e0e

## Blocking
(none)

## Polish
- tests/sims/fy3-9.json — piston height and gauge needle angle are canvas-only and not in simState, so a regression that detaches the piston from V or the needle from p would pass — optional: expose `pistonY` and `needleKPa` in simState and assert them against V and p (e.g. `{"expr":"window.simState.needleKPa","expected":200,"tol":0.01,"setup":"..."}` after setting V = 25 ml).
- tests/sims/fy3-9.json — particle bounce behaviour (fewer hits at larger V) is only checked through speed and containment (#27-29); acceptable for an illustration, no action needed.

## Checked
- test_sims.py output: `PASS preview/fy3-9  [] []` (no console/page errors, all 53 assertions hold)
- Independent playwright probe at 360 px and 1280 px: all three modes, 3 saved rows each, no console or page errors, scrollWidth = viewport width, particles inside gas (inside = 1)
- check_layout.py fy3-9: OK at 360 px; lint_lesson.py: 0 errors, 0 warnings
- Formulas in sim.js (p = p0V0/V, V = V0T/T0, p = p0T/T0, T in kelvins) match lesson.md (p1V1 = p2V2, V1/T1 = V2/T2, p1/T1 = p2/T2)
- Spec coverage: both sliders (ranges, step, hidden/visible per mode), select options, both buttons, checkbox and its (1/V, p) axis, all three modes' p/V/T/constant, table columns and values, 10-row cap, Tyhjennä, mode-switch reset, readout text, labels, canvas size, 40 particles, speed ~ sqrt(T): each has at least one assertion
- simState fields mode, V (m3), p (Pa), T (K), constant, rows all asserted in SI units
- Hash unchanged between start and end of review
