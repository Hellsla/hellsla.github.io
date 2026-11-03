VERDICT: PASS
CONTENT-HASH: 2c7036d454efdc45

## Blocking
(none)

## Polish
- [Minor] fig-9 (graph, fig-9-390, theory-1280-2) — at 390 px the tick and axis labels fall to about 7 px, and the label $e\ (\text{mV})$ sits directly under the upper plot's "0" and axis arrow, so the plots look cramped — raise the label size in the viewBox or leave a little more space between the plots. The shared time axis is labelled under the lower plot only, and that is fine.
- [Minor] lesson.md "missä …" sentences (Magneettivuo, Induktiolaki, Liikkuvan johtimen kappale) — units in parentheses are plain text: "(T)", "(m²)", "(V)", "(Wb)", "(s)", "(m/s)", "(m)". The lint accepts this, but a unit alone is still plain; if the teacher's rule covers it, write $\text{T}$, $\text{m}^2$ etc.
- [Minor] Koe 1 and Koe 2 "Alkutila" line (stage-tutki, exp-koe-1-390-1) — generated "vauhti = 0,1 m/s, magneettivuon tiheys = 0,2 T" is plain text and has fewer significant figures, while the paragraph above it is maths ($0{,}10\,\text{m/s}$) — make the generated line maths too (scripts/inquiry.py, project-wide).
- [Minor] lab-1280-1 — in the empty "Simulaation lukemat" table the fourth header "e kentän sisällä (mV)" is cut off at 1280 px and needs a sideways scroll, while at 390 it wraps — let the header wrap at 1280 as well (template, project-wide).
- [Minor] Exit ticket heading is in English ("Exit ticket") on the Finnish page (open-exit-1280) — template, project-wide.

## Checked
- Opened top-390, intro-1280, sim-390, sim-1280, lab-1280-1, exp-koe-1-390-1/2, example-390-1/2, theory-1280-1/2/3, stage-selita-390-3.
- Figures: hero (fig-2), faraday (fig-5), flux (fig-7), graph (fig-9), rod (fig-11), scene (fig-13) at 390 px. The 28–30 px captures are icons.
- Open states: open-ennusta-1280-1, open-tarkista-1280-1/2/3 and open-exit-1280.
- Maths read: induktiolaki, e = vBl, the worked example (7 steps), exit ticket and the tarkista solution.
- The graph's values (2 mWb, ±20 mV, signs) match the text, and the rod figure's E, F_s, F_m directions are consistent. The figure descriptions are full.

## Scores
illustrations 4 · typography 4 · Finnish 5 · accessibility 4
