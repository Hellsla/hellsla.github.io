VERDICT: PASS
CONTENT-HASH: 9971f42a92ccaa34
SCOPE: delta: new tasks s7, s8 and the intro; older tasks untouched

## Blocking
- (none)

## Polish
- [Minor] s7 d criterion (tasks.json): "tasaista veto-laitetta" -> "tasaista vetolaitetta" (compound word, and it would break badly on a phone line).
- [Minor] s7 figure (fy4-6/mittaus) at 390 px: the plot is small (dots about 4 px, tick numbers about 9 px). It is legible and has the expand button, so it may wait; a slightly larger dot radius would help reading values to 0,1 N.
- [Minor] s8 b: alt text and the task use "$B = 12\,\text{mT}$"; fine, but the s8 figure's origin point is drawn as a dot, while c speaks of a $0{,}04\,\text{mT}$ zero reading; for science: check that the zero point is meant to be a measured point.

## Checked
- The Sovella set has no captures of its own in review/shots.md (the stage captures show the Esimerkit stage), so I made my own element captures of the task cards 1.3-7 and 1.3-8 at 390 px with every box open (scratchpad `fi-s7-390.png`, `fi-s8-390.png`, tops opened at readable size).
- s7 and s8 situation text, figure, part list and point labels: no clipping, no horizontal overflow, parts stacked in one column, units and symbols in LaTeX ($0{,}1\,\text{N}$, $\mu_0 = 4\pi \cdot 10^{-7}\,\text{Vs/(Am)}$), decimal comma throughout.
- Figure alt texts (svg aria-label) in the page HTML: s7 describes five points with the correct values; s8 six points, fitted line, grid spacing; names (tukivoima $N$, kitkavoima, $B$, $I$) match the task text.
- Rubric and model-solution presentation read in the packet: calculation chains are aligned rows (`aligned`), results rounded to the data's precision (s7 $0{,}215 \pm 0{,}005$, s8 $2{,}0 \cdot 10^3\,\text{1/m}$, $4{,}9\,\text{A}$), unit field language-neutral ("", "1/m", "A", "%").
- Task texts do not give away the solution's structure (no formula for $\mu$ in s7; s8 gives only the law of the physics, which is the model, not the method).
- Intro: "Kahdeksan tehtävää" matches the set. Finnish is natural and consistent with the glossary terms (systemaattinen virhe, satunnainen vaihtelu, kulmakerroin).
- Hash re-checked at the end: 9971f42a92ccaa34 (unchanged).

## Scores
illustrations 4 · typography 5 · Finnish 4 · accessibility 4
