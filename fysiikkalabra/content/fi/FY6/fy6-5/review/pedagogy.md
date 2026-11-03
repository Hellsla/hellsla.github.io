VERDICT: PASS
CONTENT-HASH: 06e3cd81e22884a5

## Blocking

(none)

## Polish

- Simulation at 390 px (fig sim-390, exp-koe-2): the source-to-meter wire is a red rectangle around the whole circuit and passes over the label "C" and the upper right of the picture. It reads, but a student may take it for part of the circuit; the "Käyttöohje" text names the wire only in prose. Consider a short "V" lead-in near the red line or a thinner line.
- Experiment 2 at 390 px: the readout block (Virrat / Jännitteet / Mittari) sits below all the controls, so the student scrolls past about a screen between moving "Mittauskohta" and seeing the reading. The graph and the circuit above do update, so the task still works; moving the "Mittauskohta" select above the sliders would shorten the scroll.
- The locked sliders show "(vakio)" under each slider; the phrase would be clearer as "(vakio kokeessa)" for a reader who has not met the locking.
- inquiry.json "kertaus", option 3: "Pariston jännite jakautuu lamppujen kesken puoliksi" is a weak distractor for two different lamps; "pariston jännite jakautuu lamppujen resistanssien suhteessa" would test the series/parallel confusion better.
- The lesson still names the junction figure "ei mittakaavassa" while the arrow widths are proportional; the alt text says so, but the visible caption could say "nuolten leveys mittakaavassa".

## Checked

- Rewritten narrow layout, simulation at 390 px: circuit, potential graph, sliders (two columns for R3 and Mittauskohta, then Nollakohta full width), readout and the collapsed Käyttöohje / Mallin oletukset / Laskennan selitys are all visible, nothing clipped, text legible.
- Sim inside Koe 2 at 390 px: locked parameters greyed and marked "(vakio)", varied parameter active, table buttons ("Aseta alkutila", "Kirjaa mittaus", "Nollaa") below, readout row labelled "Simulaation lukemat".
- Colour carries meaning with a second cue: potential is a blue number plus a shade, current is purple arrows with I labels, the meter level is a dashed red line with a ringed marker on the graph.
- Learning path unchanged from round 2: hook, retrieval, two predictions with figures, sim, experiments with min counts, conclusion, theory, reflection, example, error finding, transfer, checks, exit ticket; workload is one lesson.
- Predictions can be refuted by the experiments (R3 varied with U, R1 and R2 locked; probe varied in Koe 2 with every circuit parameter and the ground locked).
- Round 2 content (lesson.md, inquiry.json, exit ticket) is the same hash base as the PASS; I read the text again and found no new problem in Finnish or in the model's stated simplifications.
- The hash was the same at the start and the end of the review.
