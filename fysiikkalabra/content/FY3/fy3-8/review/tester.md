VERDICT: PASS
CONTENT-HASH: d2bee4f9bcda79a2

## Blocking
(none)

## Polish
- tests/sims/fy3-8.json (end) — nothing asserts that `div.controls` comes before `div.readout` (NOTES.md rule, cost rounds in fy3-6/7), and the DOM order was just changed — add:
  `{"expr": "(() => { const k=[...document.querySelector('#sim-root').children].map(c=>c.className); return k.indexOf('controls') >= 0 && k.indexOf('controls') < k.indexOf('readout') && document.querySelector('#sim-root .controls button') ? 1 : 0 })()", "expected": 1, "tol": 0, "note": "controls (with the button) come before the readout"}`
- tests/sims/fy3-8.json — the exaggeration factor named in the spec ("liioittelukerroin") is only tested indirectly through `spacing`; add `{"expr": "window.simState.E", "expected": 100, "tol": 0, "note": "exaggeration factor shown on the canvas is 100"}`.
- tests/sims/fy3-8.json — spec says the vibration phase is deterministic, but no assertion covers it. Optional: with the sim paused, read `simState.t` twice (already done) and compare two page loads; low value, skip if costly.
- sim.js:77,116-140 — the chart (five lines, current point at (T, ΔL)) is canvas-only and not in `simState`; it is untestable by assertion. Optional: expose `point: {x: T, y: dL*1000}` so a test can tie the dot to the readout.

## Checked
- `python3 scripts/test_sims.py fy3-8` -> `PASS preview/fy3-8  [] []` (41 of 41 assertions, run twice, same result)
- lint_lesson.py fy3-8: 0 errors, 0 warnings; build.py --all builds fy3-8 (draft)
- Console/page errors: none at 360, 390 and 1280 px, incl. sweep of all 5 materials x (L0,T) corners (1/-40, 100/120, 100/-40, 37/20, 1/21); no horizontal overflow at 360/390 px
- Formula: sim.js `dT = T - 20`, `dL = alpha*L0*dT`, `L = L0 + dL` equals the lesson's ΔL = αL₀ΔT and L = L₀ + ΔL; the α table (12, 23, 17, 9, 3,3 · 10⁻⁶ 1/K) matches lesson.md
- Spec quantities with an assertion: material, alpha (all five), L0, T, dT, dL (5 materials, positive and negative), L, plus rel, spacing, amp, chart axis, readout text (sign, Finnish decimal comma, mm, 4+ decimals for L), labels, pause/resume button
- Slider ranges/steps (L0 1-100 step 1, T -40...120 step 1) and the five option labels are asserted
- Initial state (L0 10 m, T 20 °C, steel, dL = 0) asserted before any setup
- DOM order in #sim-root verified by hand: canvas, div.controls, div.readout, p.note
- Tolerances are tight (absolute 1e-6 m on dL, i.e. well under 1 %)
- Hash at start and at end: d2bee4f9bcda79a2 (unchanged). Note: preview/ was rebuilt by a parallel agent mid-run (fy3-8 files briefly missing); I rebuilt it and re-ran.
