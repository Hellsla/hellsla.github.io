VERDICT: PASS
CONTENT-HASH: 62daa651fbd9a7eb

## Blocking
- none

## Polish
- content/fi/FY3/fy3-1/lesson.md:214 — "$1\,\text{N}$ = $1\,\text{kg}\cdot\text{m/s}^2$" puts the equals sign outside maths after the re-set — one formula: $1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2$.
- content/fi/FY3/fy3-1/inquiry.json:222,226,230,314,318,403 — written divisions in feedback still use a slash ($5{,}6 / 1{,}6 \cdot 1{,}0\,\text{N}$, $12\,\text{N} / 1{,}62\,\text{m/s}^2$, $440\,\text{N}/50\,\text{kg}$), unlike the lesson's new colon form — use ":" (or \tfrac) for consistency with the house rule; unchanged since the PASS, values right.

## Checked
- Full mode against ee6b2ec: every re-set quantity in lesson.md, inquiry.json and exit-ticket.json keeps its value and unit (1 N, 5,0 N/2,0 cm, 10 N/4,0 cm, 2,5 N/1,0 cm, 100 g/1 N, 9,81 N, 1,18 kN, 10 N, 1200 N, 445 N, 1180 N, 690 N, 20/196/200 N, 3,5/5,6/9,0 N, 1,6/5,6 cm, 5/5000 N, 12/73 N, 440 N, 3,0 cm/8,0 N/20 N/7,5 cm); no answer, option or "correct" flag changed.
- Ratios re-set with a colon: 1,62 : 9,81 = 0,165 ≈ 0,17 ≈ 1 : 6; 3,71 : 9,81 = 0,378 ≈ 0,38 — correct.
- Recomputed in one script: pred-1 98,1/294 N (+196 N), pred-2 248 N (×2,53), kalibrointi 3,5 N (distractor 8,96 ≈ 9,0), virhe 4,91 N vs 4905 N, siirto 72,7 N (mistakes 19,44, 117,72, 7,41), check-2 8,8 m/s² (0,114, 44,9), check-c2 ≈ 15 N, example 1177,2/445,2 N, 70 kg ≈ 690 N, exit 7,5 cm.
- Forcemeter figure: G and 2G arrows now red (#c92a2a), same meaning as the sim's red weight; lengths 1:2 unchanged; capture fig-2 confirms.
- sim.js: only the gridline limit changed (0,8 → 0,9 of chartFull); G = m g, stretch, arrow, bars, chartFull = m · 24,8 and simState unchanged. Checked all m = 1…100 kg: ≥ 2 gridlines, integer labels, top gridline ≥ 23 px below the full-scale line (10 kg: 50, 100, 150, 200 under 248 N).
- Caption "kaavion asteikko 0–248 N" (lang/fi.json:446) is distinct from the spring's fixed 0–2500 N ruler; readout line still explains it is this mass on Jupiter; sim-spec still matches.
- Whole lesson re-read: definitions (force as measure of interaction, mass vs weight), G = mg with surface g, proportionality stated with "kun jousta ei venytetä liikaa", within FY3 scope; no guardrail issue.
