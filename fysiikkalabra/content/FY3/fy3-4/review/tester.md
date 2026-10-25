VERDICT: PASS
CONTENT-HASH: b7d4bcd794c5c8e0

## Blocking
None.

## Polish
- tests/sims/fy3-4.json (end) — no assertion guards the label layout that cost two rounds; the new `window.simDebug.boxes` makes it testable — add (sets the worst case from round 2, h = 5 m at ρ = 1000, and checks that no two boxes intersect and the reading was placed):
  `{"setup": "const r=document.querySelectorAll('#sim-root input[type=range]'), c=document.querySelector('#sim-root input[type=checkbox]'); r[0].value=5; r[1].value=1000; c.checked=false;", "expr": "(() => { const b=Object.values(window.simDebug.boxes); for (let i=0;i<b.length;i++) for (let j=i+1;j<b.length;j++) if (b[i][0]<b[j][1] && b[j][0]<b[i][1] && b[i][2]<b[j][3] && b[j][2]<b[i][3]) return 0; return window.simDebug.readingPlaced ? 1 : 0 })()", "expected": 1, "tol": 0, "note": "no two canvas label boxes intersect and the gauge reading found a free spot"}`
- tests/sims/fy3-4.json — the chart-label and kulmakerroin readout text (`ρg = 9,81 kPa/m` at ρ = 1000) have no assertion; optional.

## Checked
- `python3 scripts/test_sims.py fy3-4`: `PASS preview/fy3-4  [] []` (28 assertions, no console or page errors, 1280 px); preview/fy3-4-sim.js identical to content sim.js.
- Physics unchanged vs round 2 (4435c11): the lines for slope, pOver, pTotal, ratio, the whole readout.html block and the simState object are identical; only comments and canvas drawing differ. Formula p = p₀ + ρgh, p₀ = 101 kPa, g = 9,81 m/s² matches lesson.md (## Kaava).
- Spec coverage: h, rho, pOver, pTotal, ratio, checkbox/overOnly, chart intercept and slope, scale pMax, labels, readout text and slider ranges each have an assertion.
- Collision sweep (own script, headless Chromium, 360/390/1280 px): ρ ∈ {700, 1000, 1300} x checkbox on/off x h = 0…20 m in 0,5 m steps = 246 states per width, 738 in all. For every pair of `simDebug.boxes`: 0 intersections, minimum gap 3 canvas units (the 3-unit PAD), 0 boxes outside the 600x400 canvas, 0 hits of reading/p₀ label on a guide, the p₀ line or the dot, `readingPlaced` true in all 738 states.
- Console and page errors during the sweep: none at any width (k = 2,04 / 1,85 / 1,00).
- `lint_lesson.py fy3-4`: 0 errors, 0 warnings. `check_layout.py fy3-4`: `OK   preview/fy3-4 at 360 px`.
- Content hash `b7d4bcd794c5c8e0` identical before and after the review; sim.js and tests/sims/fy3-4.json have no uncommitted changes.
