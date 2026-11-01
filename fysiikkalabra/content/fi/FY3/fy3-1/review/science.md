VERDICT: PASS
CONTENT-HASH: f349123e5b25e48b

## Blocking
- none

## Polish
- content/fi/FY3/fy3-1/inquiry.json:222,226,230,314,318,403 — written divisions in feedback still use a slash ($5{,}6 / 1{,}6 \cdot 1{,}0\,\text{N}$, $12\,\text{N} / 1{,}62\,\text{m/s}^2$, $440\,\text{N}/50\,\text{kg}$), unlike the lesson's colon form — use ":" (or \tfrac) for consistency; values right, unchanged since the PASS.
- lessons/FY3/fy3-1/sim-spec.md:1 — "asteikko on kirjoitettu kaavion yläpuolelle" now describes the removed caption; the full-scale value is written at the top of the y axis — update the spec sentence.

## Checked
- Delta against 7f8acef (packet full only because sim.js changed); hash f349123e5b25e48b at start and end.
- lesson.md:214 now one formula $1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2$ — my earlier Polish item is resolved; unit identity correct, deferral to FY4 unchanged.
- sim.js diff touches only drawChart labelling: G = m g, stretch, arrow, bars, chartFull = m · 24,8, gridline steps and simState { m, body, g, G, stretch, arrow, bars, chartFull } are unchanged; inquiry tests 65/65.
- New full-scale label uses the same tx(chartFull, <100 ? 1 : 0) as the readout, so axis top (248 at 10 kg; 24,8 at 1 kg) and "Palkkikaavion asteikko 0–248 N … paino Jupiterissa" always agree; 24,8 m/s² is the table's Jupiter g.
- Captures sim-390 and sim-1280 (10 kg, Maa): axis 50…200 then 248 at the full-scale tick, Jupiter bar exactly at 248 N, Maa 98,1 N, Kuu 16,2 N, Mars 37,1 N — recomputed m·g correct; axis title G (N) above the axis, no overlap with the chart title or Jupiter label.
- Earlier results still hold (nothing else changed): pred-1 98,1/294 N, pred-2 248 N (×2,53), kalibrointi 3,5 N, virhe 4,91 N, siirto 72,7 N, check-2 8,8 m/s², check-c2 ≈ 15 N, example 1177,2/445,2 N, 70 kg ≈ 690 N, exit 7,5 cm.
- Removed key sims.fy3-1.asteikko_0 has no remaining reference in lessons/ or lang/.
- Physics guardrails: definitions, G = mg with surface g, proportionality condition, scope FY3 — unchanged, no issue.
