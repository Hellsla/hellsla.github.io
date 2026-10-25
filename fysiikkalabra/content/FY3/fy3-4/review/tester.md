VERDICT: PASS
CONTENT-HASH: 6f27a57a1ed01388

## Blocking
None.

## Polish
- content/FY3/fy3-4/sim.js:102 — at a 390 px viewport (canvas text scaled by k = 600/width) the gauge reading in the chart is drawn above-left of the point (`up = h > 4`) and, for h of about 4,5 to 7 m, its box crosses the y axis and lands on the p tick labels (seen: "31 kPa" over "50" at h = 4,5 / ρ = 700 / ylipaine; "178 kPa" over "200" at h = 6 / ρ = 1300; "145 kPa" and "160 kPa" over "150" at ρ = 1000). Not a test failure, since canvas text is not asserted; the fixer's round-1 sweep checked 1–4 m and 12, 18 m but not this gap. Fix: switch to the below-right branch while `lx - lw < CH.x0 + 4` (for example `const up = h > 4 && px - 10 - p.textWidth(txt) > CH.x0 + 4`, with textSize set first), or right-align the label at CH.x0 + 4 clamp. At 1000 px (k = 1) nothing overlaps.
- tests/sims/fy3-4.json (optional) — no assertion on the checkbox label text or on the readout line "kulmakerroin ρg = 10,79 kPa/m"; slope is asserted via simState. Thin but present.

## Checked
- `python3 scripts/test_sims.py fy3-4` -> `PASS preview/fy3-4  [] []` (no console or page errors, simState present)
- `lint_lesson.py fy3-4`: 0 errors, 0 warnings; `build.py --all` built fy3-4
- 28 assertions in tests/sims/fy3-4.json, all tolerances <= 1 %; the two round-1 additions (slider ranges 0-20 / 700-1300, "Kuolleenmeren vesi" label at 1240) are present and pass
- Formula: sim.js `pTotal = P0 + slope*h`, slope = rho*9.81/1000 equals lesson.md `p = p_0 + ρgh`, p₀ = 101 kPa, g in m/s² (no N/kg); worked example 12 m water 117,72 / 218,72 / 2,166 asserted
- Spec coverage: h slider, rho slider, checkbox (overOnly, chartBase, chartValue), simState h/rho/pOver/pTotal/ratio all asserted; readout text with decimal comma asserted
- Round-2 label placement (screenshots at 390 and 1000 px, 18 states incl. h = 0 with both checkbox states): grey p₀ label clears the reading and guide lines; reading stays above the h axis in over-only mode; "h (m)" clear of the guide line; no console errors
- Hash before and after review: 6f27a57a1ed01388 (unchanged)
