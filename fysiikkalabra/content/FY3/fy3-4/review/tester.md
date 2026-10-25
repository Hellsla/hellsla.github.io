VERDICT: PASS
CONTENT-HASH: c5607da20b3e1dea
## Blocking
None.

## Polish
- tests/sims/fy3-4.json (end of file) — the slider ranges in sim-spec.md (h 0–20 m, rho 700–1300 kg/m³) are not asserted; a changed min/max would go unnoticed — add: `{"expr": "(() => { const r=document.querySelectorAll('#sim-root input[type=range]'); return r[0].min==='0' && r[0].max==='20' && r[1].min==='700' && r[1].max==='1300' ? 1 : 0 })()", "expected": 1, "tol": 0, "note": "slider ranges h 0-20 m, rho 700-1300 kg/m3 as in sim-spec"}`
- tests/sims/fy3-4.json — only "merivesi" is asserted among the liquid names in the density label (spec: bensiini 720, vesi 1000, Kuolleenmeren vesi 1240) — add: `{"setup": "const r=document.querySelectorAll('#sim-root input[type=range]'); r[0].value=5; r[1].value=1240;", "expr": "[...document.querySelectorAll('#sim-root label')][1].textContent.includes('Kuolleenmeren vesi') ? 1 : 0", "expected": 1, "tol": 0, "note": "density label names the Dead Sea water at 1240"}`
- tests/sims/fy3-4.json — no assertion that the checkbox label text and the readout "kulmakerroin ρg = 10,79 kPa/m" line are present (slope is only checked via simState) — optional readout check at h=8, rho=1100.

## Checked
- `python3 scripts/test_sims.py fy3-4` -> `PASS preview/fy3-4  [] []` (rc 0, no console or page errors, simState present)
- `python3 scripts/build.py --all`: fy3-4 built (draft); fy3-6 skipped (expected)
- `python3 scripts/lint_lesson.py fy3-4`: 0 errors, 0 warnings
- sim.js:43 `P0 + slope*h` with slope = rho*9.81/1000 equals lesson.md `p = p_0 + ρgh`, p₀ = 101 kPa, g = 9,81 m/s² (no N/kg anywhere); lesson SVG 199 kPa at 10 m matches 101 + 98,1
- Spec coverage: h slider (assert h, label), rho slider (assert rho, label, slope), checkbox (overOnly, chartBase, chartValue, pTotal unchanged), simState h/rho/pOver/pTotal/ratio all asserted; worked example 12 m water -> 117,72 / 218,72 / 2,166 asserted
- Edge and variety: surface (h=0, any rho) pTotal = 101, ratio 1; extremes 20 m/1300 and 5,5 m/720; identity pTotal - p0 - rho*g*h/1000 = 0 at 8 m/1100
- DOM readout text with decimal comma asserted (117,7 / 218,7 / 2,17 kertaa / 356,1 / 3,53 kertaa / scale 0–400 kPa); canvas 600x400 asserted
- 26 assertions in tests/sims/fy3-4.json, all tolerances <= 1 % (1e-6 absolute)
- Hash recomputed at end of review: unchanged (c5607da20b3e1dea)
