VERDICT: PASS
CONTENT-HASH: cf3db0d4e8955bff

## Blocking
(none)

## Polish
- tests/sims/fy3-6.json — no assertion for the equal-temperature branch (TB0 = TW0 gives Teq = TW0, Q = 0, text "Lämpötilat ovat samat, joten lämpöä ei siirry.") — add: {"setup":"const r=document.querySelectorAll('#sim-root input[type=range]'), s=document.querySelector('#sim-root select'); r[0].value=0.3; r[1].value=40; s.value='385'; r[2].value=0.2; r[3].value=40;","expr":"Math.abs(window.simState.Q) + Math.abs(window.simState.Teq - 40)","expected":0,"tol":1e-06,"note":"equal start temperatures: no heat flows"}
- tests/sims/fy3-6.json — the lesson example (T = 24,5 °C is a measured value, unknown metal) differs from the sim default (copper, T = 24,6 °C); the test notes mention it, but a one-line sim note or lesson remark that the sim is the model value would avoid confusion (educator's call, not a test gap).
- tests/sims/fy3-6.json — the canvas drawing (chart curves, T line, vessel colours) has no assertion; only simState and DOM text are checked. Acceptable, since canvas pixels are not part of the spec contract.
- tests/sims/fy3-6.json — the time-based checks (8 s and 2,5 s waits) make the file slow (~13 s) but they are stable across two runs.

## Checked
- `PASS preview/fy3-6  [] []` (run twice, identical; no console or page errors; simState present)
- lint_lesson.py fy3-6: 0 errors, 0 warnings (not repeated here)
- Formula in sim.js:51 T = (C_W·T_W0 + C_B·T_B0)/(C_W + C_B) with c_W = 4190 matches lesson.md "c₁m₁(T₁ − T) = c₂m₂(T − T₂)"; Q = c_B·m_B·(T_B0 − T) equals the water's c_W·m_W·(T − T_W0), asserted for both hot and cold bodies
- 42 assertions; every simState key in sim-spec.md (mW, TW0, cB, mB, TB0, Teq, CW, CB, Q, running) has at least one assertion
- Sliders: all four set through the DOM and read back (mW, TW0, mB, TB0), plus select cB (900) and its 5 options; ranges 0,10–1,00 / 5–60 / 0,05–1,00 / 0–100 asserted
- Output text: T, C_W, C_B, Q twice (given = taken), which warms, thermometer readout and chart scale asserted on DOM text with decimal comma and 1 % tolerance
- Animation: starts only after Upota, converges to Teq (hot/cold, 1 % water-water case), stops at 10 s, exact Teq at end, slider change resets it; note about the 1,5 s illustrative time constant asserted
- Materials in sim match spec and lesson table (vesi 4190, alumiini 900, hiekka 800, rauta 450, kupari 385; no ice)
- Layout at 390 px: no horizontal overflow, controls 40 px high, no console errors
- Hash before and after the review identical (cf3db0d4e8955bff)
