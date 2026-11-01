VERDICT: PASS
CONTENT-HASH: d748ffe438661103

## Blocking
- none

## Polish
- content/fi/FY3/fy3-1/inquiry.json:222,226,230,314,318,403 — written divisions in feedback still use "/" ($5{,}6 / 1{,}6 \cdot 1{,}0\,\text{N}$ etc.) unlike the lesson's colon form — use ":" or \tfrac; values right (carried over).
- lessons/FY3/fy3-1/sim-spec.md:1 — "asteikko on kirjoitettu kaavion yläpuolelle" still describes the removed caption; the full-scale value is on the top of the y axis — update the sentence (carried over).

## Checked
- Round 3 delta: sim.js diff since 4253a4a (the last PASS) is two lines in drawChart: chart title now sized to titleMax = BARS.w − 8 (292 px, over the chart only) and drawn at BARS.y − ts(14) instead of − ts(6). `git diff 4253a4a -- lessons/FY3/fy3-1 content/*/FY3/fy3-1 lang` shows nothing else but exercises/review/carry.tsv (review log, not lesson content); packet full only because sim.js changed.
- Layout only: G = m g, stretch, arrow, bars, chartFull = m · 24,8, gridline step, readout and simState { m, body, g, G, stretch, arrow, bars, chartFull } untouched; inquiry tests 65/65, lint/latex/build/sims/layout 360 px ok.
- Geometry: title (x 274–566, baseline 60 − 14k) cannot meet the axis title G (N) (right-aligned at x 264, centred at 90 − 14k) nor the Jupiter value label (baseline ≥ 84 at full scale).
- Captures sim-390 and sim-1280 (10 kg, Maa): title above G (N), no overlap; axis 50…200, 248; Maa 98,1 N, Kuu 16,2 N, Mars 37,1 N, Jupiter 248 N = m·g recomputed, Jupiter bar at the full-scale tick; readout 0–248 N agrees.
- Earlier results still hold (unchanged): pred-1 98,1/294 N, pred-2 248 N (×2,53), kalibrointi 3,5 N, virhe 4,91 N, siirto 72,7 N, check-2 8,8 m/s², check-c2 ≈ 15 N, example 1177,2/445,2 N, 70 kg ≈ 690 N, exit 7,5 cm.
- Physics guardrails (definitions, G = mg with surface g, proportionality, FY3 scope): unchanged, no issue.
- Hash d748ffe438661103 at start and end.
