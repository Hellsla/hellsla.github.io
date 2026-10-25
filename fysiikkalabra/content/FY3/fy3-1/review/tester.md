VERDICT: PASS
CONTENT-HASH: 504251c86e89d23f

## Blocking
(none)

## Polish
- tests/sims/fy3-1.json (end) — simState.body and the highlighted bar are in the spec ("valittu korostettuna") but only the Maa readout is asserted, so a wrong body name for Kuu, Mars or Jupiter would pass — add:
  {"setup": "const s=document.querySelector('#sim-root select'); s.value='Mars'; document.querySelector('#sim-root input[type=range]').value=20;", "expr": "(() => { const x=document.querySelector('#sim-root .readout').textContent; return window.simState.body==='Mars' && x.includes('g = 3,71 N/kg (Mars)') && x.includes('G = m · g = 74,2 N') ? 1 : 0 })()", "expected": 1, "tol": 0, "note": "Mars: body name, g and G in the readout (20 kg · 3,71 = 74,2 N)"}
- tests/sims/fy3-1.json (chartFull test) — chartFull is asserted only at 10 kg (248); the mass dependence is covered indirectly by the "ten times the mass" test, but a direct second point is cheap — add:
  {"setup": "const r=document.querySelector('#sim-root input[type=range]'); r.value=40; r.dispatchEvent(new Event('input'));", "expr": "new Promise(f => setTimeout(() => f(window.simState.chartFull), 250))", "expected": 992, "tol": 1e-06, "note": "bar chart full scale follows the mass: 40 kg · 24,8 N/kg"}
- tests/sims/fy3-1.json:20-ff — several tests depend on the state left by the previous one (the 5 kg mass test relies on the Kuu setup before it, the Kuu/Maa bar test on Maa from earlier); reordering breaks them. Give each a full setup.
- The drawing-only floors (2 px bar, 3 px arrow, spring rest length) and the scale text above the chart are canvas pixels and cannot be read from simState; they are not asserted, which is acceptable.

## Checked
- test_sims.py: PASS preview/fy3-1  [] []  (no console or page errors, 23 assertions in the file, all pass)
- lint_lesson.py fy3-1: 0 error(s), 0 warning(s); build.py --all built fy3-1 (reviewed) without errors
- Formula in sim.js (G = m * g, g = 1,62 / 3,71 / 9,81 / 24,8 N/kg) equals lesson.md line 19 and the table in lines 23-28
- Every slider and select is driven by assertions: mass 1-100 kg (range, label unit, values 5, 10, 25, 40, 100), body Kuu, Mars, Maa, Jupiter (option list, G for each)
- G, g, m asserted by value (98,1; 8,1; 92,75; 2480) and in the DOM readout; mass independent of body asserted
- stretch and arrow: proportional to G across bodies and masses (ratio constant, so no offset), ordered Kuu < Mars < Maa < Jupiter, fit at full scale (stretch at most 190 px, arrow at most 120 px)
- New bar-chart scaling: chartFull = m · 24,8 (248 at 10 kg), Jupiter bar always 220 px, Maa bar = 220 · 9,81/24,8, Kuu/Maa bar ratio 1,62/9,81, proportions unchanged when mass x10 while G and stretch grow x10
- Canvas 600x400 asserted
- answers.py is present, matches exercises.json per the lint; tester hash unchanged at start and end (504251c86e89d23f)
