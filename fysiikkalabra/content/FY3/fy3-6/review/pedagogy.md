VERDICT: PASS
CONTENT-HASH: 2241eb647ba8f7e1

## Blocking
(none)

## Polish
- sim.js, graph legend at 360 px: the "vesi/kappale" legend sits inside the plot's top-right corner. When the scale top equals a start temperature (e.g. water 60 °C, 0,05 kg iron at 0 °C), the flat water line and the "T 59,7 °C" label run straight through the "kappale" entry (my Playwright run at 360 px). At 1280 px the legend is above the plot and clear. Move the legend above the plot area (as on desktop) or add head-room to the temperature scale.
- sim.js, canvas ticks at 390 px: axis numbers and the "T / 24,6 °C" label render at about 8 px, the smallest text on the page (fy3-6-sim-390.png, fy3-6-exp-koe-1-390-1.png). Legible but tiring; raise the KaTeX font size of ticks to at least 10 px on narrow canvases.
- Controls at 390 px: the "Veden massa" label sits beside the Upota button and its slider drops below it, so label and slider look detached (fy3-6-sim-390.png). Put the button on its own row or under the first slider.
- inquiry.json "koe-2" intro: the question "Millä massalla tulos on alkulämpötilojen keskiarvo?" is answerable (0,50 kg) but is not recorded in a table column; the table (kuuman veden massa, T) already supports it, so a one-line prompt "Mitä huomaat, kun massat ovat yhtä suuret?" would link back to ennuste 2's wording.
- Readout text is serif KaTeX against the sans page text; the mixed look is acceptable but the readout's "Lämpökapasiteetit C = cm: vesi 1257 J/K, kappale (kupari) 77,0 J/K" line wraps awkwardly at 390 px.

## Checked
- Learning path: hook (hiekka/vesi), retrieval on fy3-5, two committed predictions, two experiments with locked controls (min 2), theory, reflection returning to the hook, example, error-spotting, transfer with hints and mistakes, three checks. Slot goals (lämpeneminen, kalorimetrinen mittaus, usean termin yhtälö) covered, nothing beyond FY3.
- Predictions refutable: koe-1 gives hiekka 26,8 vs vesi 44,0 °C; koe-2 gives 40,0 °C against the 55 °C average; the result emerges from the same formula, but the point (c and mass weighting) is the lesson's content.
- Worked example: 5 stages, symbolic first, units, sig figs justified; exercises not a repeat; levels 5/4/3.
- Figures 1-3 legible at 390 px, labels in LaTeX, colour not alone (arrows, brackets, labels).
- Sim at 390/360/1280: canvas labels and readout are KaTeX, no clipped controls, Käyttöohje/Mallin oletukset/Laskennan selitys boxes closed; 1280 px lab layout puts the sim beside experiments.
- Mid-run animation at 360 and 1280: no overlaps other than the legend item above.
- Finnish: terms match glossary; case after number+unit fine; chapter names, no ids.
- Exit ticket tests core idea (Q = cmΔT, c comparison, weighted mean).
- Workload fits one lesson.
- Hash unchanged start to end.
