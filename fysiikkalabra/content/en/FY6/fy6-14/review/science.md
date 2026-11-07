VERDICT: PASS
CONTENT-HASH: b979acdab1019426
Mode: light (teacher 2026-11-07, "kevyt katselmointi": the editorial-correction diff since origin/main only)

## Blocking
- none

## Polish
- The summary bullet reads "a series resistor is connected in series with the LED" (doubled 'series'); style only.

## Checked
- 'light intensity' → irradiance throughout (lesson, inquiry howto/model/calc/experiment labels, figure aria-labels, lang key sims.fy6-14.valo); defined as radiant power incident per unit area, W/m²; η = P/(GA) unchanged.
- Recomputed: 1000 W/m² · 0,0060 m² = 6,0 W; 0,92/6,0 ≈ 15 %; 5,0 V/0,184 A ≈ 27 Ω.
- LED: current must be limited; series resistor in a simple constant-voltage circuit, constant-current driver in other devices; opening question, summary, synthesis prompt, model answer and criterion consistent (= fi). (4,5 − 2,0) V / 1 Ω ≈ 2,5 A unchanged.
- Diff since origin/main compared sentence by sentence with the Finnish source change; content hash checked at start and end.
- Round 2 (git diff HEAD~1): synthesis model answer now says the LED does not limit its own current, so the circuit must (series resistor); correct and = fi. The summary-bullet polish remains.
