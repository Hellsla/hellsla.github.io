VERDICT: PASS
CONTENT-HASH: f5c8999cf40efdf7

## Blocking
(none)

## Polish
- content/FY3/fy3-7/sim.js:62-65 — Q is computed as P·t from the current slider value, so moving the power slider while running rescales the whole history. Measured in headless Chromium: m = 0,5 kg, P 500 W, Q = 15,0 kJ and T = −5,7 °C, then P set to 3000 W gives Q = 107,9 kJ and T = 0 °C in the next frame. A mass change mid-run also makes T jump (here to the 0 °C plateau at 1,0 kg). Energy transferred is not conserved, which contradicts "Q = Pt" for a student who experiments. Fix: reset (t = 0, running = false) on slider input, or disable the sliders while running, or integrate Q += P·dt. The test hooks (simSetTime/simSetQ) and the 49 assertions would be unaffected by the first two options.
- tests/sims/fy3-7.json — slider ranges from the spec (m 0,10–1,00 kg, P 500–3000 W, steps 0,05 and 100) are never read back. Add: `{"expr": "(() => { const r=document.querySelectorAll('#sim-root input[type=range]'); return r[0].min==='0.1' && r[0].max==='1' && r[0].step==='0.05' && r[1].min==='500' && r[1].max==='3000' && r[1].step==='100' ? 1 : 0 })()", "expected": 1, "tol": 0, "note": "slider ranges match the spec"}`
- tests/sims/fy3-7.json — no assertion sits on a stage boundary (e.g. exactly Q = 188 000 J at m = 0,50 kg must be phase 'vesi', T = 0). Add with setup `r[0].value=0.5; r[1].value=1000; window.simSetQ(188000);` expr `window.simState.phase==='vesi' ? 1 : 0`, expected 1.
- tests/sims/fy3-7.json — the 60× acceleration is only checked as 1 < t < 60 after ~0,2 s plus the note text; a wrong SPEED (e.g. 6 or 600) would still pass the note check. Tighten to the ratio t / elapsed real seconds, or accept as is.
- sim.js:83-101 — the container content text (jää, jää ja vesi, …) and the colour are canvas-only and not in simState or the DOM, so the spec's "astian sisältö näyttää olomuodon" has no assertion beyond `phase`. Optional: expose `content` in simState and assert it.

## Checked
- `python3 scripts/test_sims.py fy3-7` -> `PASS preview/fy3-7  [] []` (49 assertions, no console or page errors)
- lint_lesson.py fy3-7: 0 errors, 0 warnings
- Formula: piecewise Q = c_jää·m·ΔT, s·m, c_vesi·m·ΔT, r·m, c_höyry·m·ΔT with s = 334 kJ/kg, r = 2260 kJ/kg, c = 2100/4190/2000 matches sim-spec, lesson (Q = sm, Q = rm, Q = cmΔT) and answers.py
- Every simState field is asserted (m, P, t, T, phase, Q, tMelt, tBoil, running, tEnd, tMax); both sliders, both buttons, end stop at 130 °C and restart from the end are covered
- Each of the five phases is asserted for both T and phase, via simSetQ and simSetTime, at several m/P combinations
- Readout text (phase, T with Finnish minus/comma, Q in kJ, t, sm/P, rm/P, axis range), labels with units and the 1 s = 60 s note are asserted
- Real run at 390 px width, m = 0,1 kg, P = 3000 W: phases sulaa, vesi, kiehuu, höyry in order, stops at T = 130, t = tEnd = 103,8 s; no page overflow (scrollWidth 390), sliders and buttons 40 px high; no console errors
- Hash before and after review: f5c8999cf40efdf7 (unchanged)
