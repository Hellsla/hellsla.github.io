VERDICT: PASS
CONTENT-HASH: 35d50fed670b3d0d

## Blocking
- none.
- [Major, outside this change, work item 5d] The clipped-formula rows for FY7-sovella in `docs/clipped-formulas.tsv` (lines 65–71, plus the `en/` rows 127–132) are not judged here. They are the s1 substitution chains with `v = \sqrt{\dfrac{2 \cdot 1{,}602 \cdot 10^{-19}\,\text{C} \cdot 30{,}0 …}`, `m_{10} : m_{11} = 1{,}6627 : 1{,}8281 \approx 0{,}91`, the s2 spring-constant row, the s3 power and mass rows and the s5 `0{,}780 : 1300\,\text{nm}` row. At 390 px in the solution captures `stage-fy7-s1-390-5` and `-6`, the long chains are tight against the right edge. I did not separately confirm which rows are cut off.

## Polish
- [Minor] `fy7-s2-signal` figure — the y axis runs to -16 V, but the lowest label is -12. The time labels sit on the bottom edge, so the -16 label is missing. Add the label or end the axis at -14.
- [Minor] `fy7-s5-graph` — the ringed fit point (1300; 0,780) sits almost on the measured point at 1313. The line is not named as a fit in the figure itself, only in the alt text. Add a short label "sovitettu suora" at its end.
- [Minor] `fy7-s1-implanter` — the labels $\overline{B}_\text{s}$, $U$ and $d$ are small and tight against the plates at 390 px. Moving them 6–8 px away from the plates would help.
- [Minor] Line breaks at a hyphen on a phone: "boori-/11:tä", "a-/kohdan" in s4 d). Use a non-breaking hyphen in these words.
- [Minor] The intro sentence "kokoaa moduulin: varatun hiukkasen liikkeen … ja valon interferenssin hilassa" is one long list. Split it into two sentences or turn it into a list.

## Checked
- Contact sheet 1 and `top-390`.
- Figures: `fig-1` (implanter), `fig-3` (selector forces), `fig-22` (fibre), `fig-25` (s5 graph), and the s2 and s4 task graphs in `stage-fy7-s2-390-1` and `stage-fy7-s4-390-1`/`-2`. `fig-4`–`fig-9` and the other tiny captures are only KaTeX roots.
- Stage captures: `stage-fy7-s1-390-1`, `stage-fy7-s3-390-1`, `stage-fy7-s5-390-1` and `-6`.
- Alt texts and `viewBox` values read from `solutions.md`. Force red, velocity blue and field green are consistent, vectors are `\overline{}`, labels are LaTeX, and the force diagram's forces are equal and opposite as the text says.
- Not opened: the 1280 px captures and the stage captures s2 and s4 beyond their first two parts, so desktop layout is not checked.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
