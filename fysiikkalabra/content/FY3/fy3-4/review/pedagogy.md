VERDICT: PASS
CONTENT-HASH: 105250496aeacbbe

## Blocking
(none)

## Polish
- sim canvas labels at 390 px (sim-390, exp-exp-1-390) — axis ticks, "ilma, p₀ = 101 kPa", "p₀ = 101 kPa" and the h label render at roughly 7–8 px, and in the experiment view (canvas about 290 px wide) smaller still; legible but at the limit for a phone. The "0 m" tick sits against the tank wall and "15 m"/"20 m" touch it. Fix: keep KaTeX label size at least about 10 px rendered (scale the font up when the canvas is narrow) and add left margin for the depth ticks.
- sim readout at 390 px — "Kokonaispaine p = p₀ + ρgh = 101 kPa +" breaks after the plus and continues on the next line (exp-1 capture breaks after "=" ). Readable, but build the line as separate spans or put the sum on its own line so the equation is not split mid-expression.
- Mixed type: the canvas and readout are serif KaTeX while the sliders' captions, "Näytä vain ylipaine" and the box titles are sans. Acceptable, but "Syvyys h = 10,0 m" slider label repeats the readout's first line; drop one.
- inquiry.json pred-3 — still the only prediction with no experiment or reveal; the sim cannot test tube vs basin. A one-line reflect note would close it.
- exp-2 has no numeric question (exp-1 has); "Kuinka monta prosenttia kokonaispaine kasvoi, kun tiheys kasvoi 24 %?" would make refuting the "24 %" option explicit.

## Checked
- Hash unchanged at start and end; no lesson file edited.
- Round-1 items fixed: howto/model/calc now in three closed boxes with no duplicated "Mallin oletukset"; Alkutila line and table headers typeset as maths.
- LaTeX canvas at 1280 px (sim-1280, lab-1280): no overlaps; tank, gauge, arrows, graph labels, "199 kPa" marker and p₀ dashed line all clear and legible.
- 390 px sim: tank and graph labels do not collide with the curve or each other; readout lines wrap without clipping; sliders and checkbox usable; locked density slider shown greyed with "(vakio)" in exp-1.
- Readout values consistent with the model (98,1 + 101 = 199,1 kPa; ratio 1,97).
- Opening question answered after the derivation; slot goals covered, no more.
- pred-1/pred-2 can be refuted by exp-1/exp-2 (min 2); wrong-option feedback repairs the misconception.
- Worked example staged one step per stage; exercises at three levels; exit ticket tests the core idea.
- Finnish reads correctly.
