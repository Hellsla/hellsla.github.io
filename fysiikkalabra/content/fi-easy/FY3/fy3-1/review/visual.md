VERDICT: FAIL
CONTENT-HASH: 04224f76769b52e5

## Blocking
- [Major] lessons/FY3/fy3-1/sim.js bar chart (exp-exp-1-390, exp-exp-2-390) — the longer caption "kaavion asteikko 0–248 N" overlaps the Jupiter bar's value label "248 N" when the sim sits in an experiment card on a phone (canvas about 290 px), and it touches "G (N)". It fits in sim-390 and sim-1280 — labels overlap in the view where students measure, on the very value the caption explains — use `p.textWidth` to keep the caption left of the last bar's label (shorten or wrap it), or move the full-scale bar's label inside the bar. The sim is shared, so this affects every language.
- [Major] lesson.md l.214 (theory-1280-2) — "sillä $1\,\text{N}$ = $1\,\text{kg}\cdot\text{m/s}^2$": the re-set split one equation into two formulas with a plain-text "=" between them — a plain symbol in edited text — write "sillä $1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2$". The fi source has the same line.

## Polish
- [Minor] lesson.md l.214 — "(m/s²)" and "yksikössä m/s²" are plain text next to KaTeX $\text{m/s}^2$ in the same paragraph — set them as $\text{m/s}^2$.
- [Minor] inquiry.json feedback (interpret "Voimamittarin asteikko", Kuu numeric) — chains still divide with "/" ($5{,}6/1{,}6 \cdot 1{,}0\,\text{N}$, $12\,\text{N} / 1{,}62\,\text{m/s}^2$), while the lesson now uses the colon — use ":".
- [Minor] exp-1/exp-2 "Alkutila" — "taivaankappale: Maa, massa $m$ = 10 kg" (carried) — "taivaankappale Maa", with the quantity as one formula.

## Checked
- Resolved: plain quantities are now inline maths (theory-1280-1/2/3, example-390-2, stage-tutki-390-3, open-tarkista-1280-1/2/3, open-exit-1280). "$1{,}62 : 9{,}81 \approx 0{,}17 \approx 1 : 6$" and "$3{,}71 : 9{,}81$" render cleanly.
- fig-2-390, theory-1280-1: the weight arrows are red #c92a2a, and $G$ and $2G$ are clear.
- sim-390, sim-1280: the gridlines at 50–200 N and the caption resolve the 0–2500 confusion. exp-exp-1-390 and exp-exp-2-390 show the overlap.
- The collapsed optional tasks (Etsi virhe, Sovella uuteen tilanteeseen, Ennuste 1) are not shown open in the captures. I read their changed feedback in the source.
- The layout around the changes survived (fig-row-1280, the theory captures).

## Scores
illustrations 3 · typography 4 · Finnish 4 · accessibility 4
