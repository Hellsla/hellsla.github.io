VERDICT: PASS
CONTENT-HASH: facb6212c2324818

## Blocking
(none)

## Polish
- tests/sims/fy3-1.json:9-15 — the on-load assertion (Maa, 10 kg) has no `setup` by design and must run first (it does in `test_sims.py`); no change needed.
- sim.js:79-95 — canvas-only drawing (spring rest length, 2 px bar and 3 px arrow floors, the new left-aligned "asteikko 0–X N" text beside the top tick of the y axis, the chart title) is not readable from simState and not asserted; the scale value itself is asserted via `chartFull` and the DOM readout. Acceptable.

## Checked
- test_sims.py: `PASS preview/fy3-1  [] []` (no console or page error; 29 assertions in tests/sims/fy3-1.json, all pass)
- Round-5 change: sim.js changed only in drawing (scale text at BARS.x+9, y = tick − 4; title at BARS.y − 6); simState, readout text and the 29 assertions are unchanged and still pass
- Layout by arithmetic: scale text starts at x = 279 and is under 100 px wide, ending before the Maa bar (x = 432); the tallest bar (Jupiter) tops out at y = 90 and sits at the far right, so the text does not collide with a bar or its value label
- Formula sim.js:44 (G = m * g; g = 1,62 / 3,71 / 9,81 / 24,8 m/s²) equals lesson.md:27 and its table; no N/kg in sim.js or the test file
- Every spec quantity is asserted: m, body, g, G, stretch, arrow, bars, chartFull; slider 1-100 kg with unit in label; select with exactly Kuu, Mars, Maa, Jupiter; readout text (m, g, G, scale)
- Proportionality: stretch/G and arrow/G constant across bodies and masses, bar ratios equal g ratios, 10x mass gives 10x G and stretch; fit limits (stretch <= 190 px, arrow 110 px, bar <= 220 px, canvas 600x400)
- lint_lesson.py fy3-1: 0 error(s), 0 warning(s); build.py --all built without errors
- Tester hash facb6212c2324818 identical at start and end
