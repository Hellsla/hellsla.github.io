VERDICT: PASS
CONTENT-HASH: 940a7eabd8a24254

Delta review over the audit's PASS (df8f923b0fdab0bc): L1-05 (0,70 · 340 W/m²) replaced by a figure task (fy3-12/earth-flows: in 341, reflected 102 W/m², thermal radiation out = ?).

## Blocking
- none
## Polish
- none
## Checked
- Figure code and screenshot: arrows labelled 341 W/m² (in), 102 W/m² (heijastuu), ? W/m² (lämpösäteily); the description gives no answer.
- Balance at constant mean temperature: P_säteily = 341 − 102 = 239 W/m²; answers.py = 239; albedo 102/341 = 0,299 ≈ 30 % right.
- Tolerance 0,02 -> 234–244 W/m²; rejects 341 (no reflection) and 102.
- Values agree with the commonly quoted global mean budget (341/102/239) and the lesson's 240 W/m² rounding.
- Steady state stated in the task ("keskilämpötila pysyy vakiona"); 3 s.f. reasoning right; units LaTeX correct.
