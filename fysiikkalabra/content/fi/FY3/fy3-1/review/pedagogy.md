VERDICT: PASS
CONTENT-HASH: d748ffe438661103

## Blocking
- none

## Polish
- content/fi/FY3/fy3-1/inquiry.json:222,226,230 — calibration feedback divides with "/" while the lesson writes "1{,}62 : 9{,}81"; one notation would read more consistently (carried over).

## Checked
- Round 3 delta: sim.js diff since 4253a4a (the last PASS) is two lines in drawChart: chart title now sized to titleMax = BARS.w − 8 (292 px, over the chart only) and drawn at BARS.y − ts(14) instead of − ts(6). `git diff 4253a4a -- lessons/FY3/fy3-1 content/*/FY3/fy3-1 lang` shows nothing else but exercises/review/carry.tsv (review log, not lesson content); packet full only because sim.js changed.
- sim-390: chart title "Sama massa, paino eri paikoissa" now sits on its own line above "G (N)" — the overlap the headless test found is gone; every label legible on a phone, title still readable size.
- sim-1280: same layout, title centred over the bars, axis 50…200, 248, Jupiter bar meets the full-scale tick.
- Readout "Palkkikaavion asteikko 0–248 N on tämän massan paino Jupiterissa" unchanged and still matches the axis.
- Colour meaning (red weight, grey mass, legend), learning path, staged example, gated predictions, workload, exit ticket (7,5 cm) unchanged since the PASS; inquiry tests 65/65, 360 px layout ok.
- Hash d748ffe438661103 at start and end.
