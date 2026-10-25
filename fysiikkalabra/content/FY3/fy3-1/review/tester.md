VERDICT: PASS
CONTENT-HASH: 07c810d7ade2cd2e

## Blocking
(none)

## Polish
- tests/sims/fy3-1.json (arrow tests) — the spec states the arrow is 110 px at full scale (100 kg on Jupiter) but the test only asserts arrow <= 120 px; a wrong ARROW_FULL such as 119 would pass. Add:
  {"setup": "const s=document.querySelector('#sim-root select'), r=document.querySelector('#sim-root input[type=range]'); s.value='Jupiter'; r.value=100; s.dispatchEvent(new Event('change')); r.dispatchEvent(new Event('input'));", "expr": "new Promise(f => setTimeout(() => f(window.simState.arrow), 250))", "expected": 110, "tol": 1e-06, "note": "spec: the arrow is 110 px at full scale (100 kg on Jupiter, 2480 N)"}
- tests/sims/fy3-1.json (readout scale) — the scale text is asserted only at 40 kg (integer form "0–992 N"); the one-decimal branch (chartFull < 100) is untested. Add:
  {"setup": "const r=document.querySelector('#sim-root input[type=range]'); r.value=2; r.dispatchEvent(new Event('input'));", "expr": "new Promise(f => setTimeout(() => f(document.querySelector('#sim-root .readout').textContent.includes('asteikko 0–49,6 N') ? 1 : 0), 250))", "expected": 1, "tol": 0, "note": "readout scale for 2 kg is 2 · 24,8 = 49,6 N (one decimal below 100 N)"}
- tests/sims/fy3-1.json:20-ff — several tests still depend on the state left by the previous one (the 5 kg mass test relies on the Kuu setup before it); reordering breaks them. Carried over from round 1, not done by the fixer; give each a full setup when convenient.
- Canvas-only drawing (spring rest length, 2 px bar and 3 px arrow floors, highlighted bar, scale line above the chart) is not readable from simState and not asserted; acceptable.

## Checked
- test_sims.py: PASS preview/fy3-1  [] []  (no console or page errors; 26 assertions in tests/sims/fy3-1.json, all pass)
- lint_lesson.py fy3-1: 0 error(s), 0 warning(s); build.py --all built fy3-1 without errors
- Formula in sim.js line 44 (G = m * g; g = 1,62 / 3,71 / 9,81 / 24,8 N/kg) equals lesson.md line 19 and its table
- Round-1 additions present and passing: Mars body/g/G readout (20 kg -> 74,2 N), chartFull at 40 kg (992), readout contains "asteikko 0–992 N"
- Slider (1-100 kg, label unit, values 5, 10, 25, 40, 100) and select (exact options, G per body) are driven by assertions; m independent of body
- G, g, m, stretch, arrow, bars, chartFull all asserted; stretch/arrow proportional to G with no offset (stretch/G constant across bodies and masses)
- Bars: Jupiter bar 220 px at any mass, Kuu/Maa = 1,62/9,81, Maa bar = 220 * 9,81/24,8; proportions unchanged when mass x10 while G and stretch grow x10
- Full-scale fit: stretch <= 190 px, arrow <= 120 px, bar <= 220 px; canvas 600x400 asserted
- Short canvas scale line in sim.js:93 and the DOM readout explanation (sim.js:50) agree with sim-spec.md
- Tester hash unchanged at start and end (07c810d7ade2cd2e)
