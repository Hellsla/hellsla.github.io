VERDICT: FAIL
CONTENT-HASH: 683a2b867e60ff05

## Blocking
- [Major] inquiry.json lines 204 and 265, tables of koe-1 and koe-2 (captures lab-1280-1, exp-koe-1-390) — the column header reads as plain text "Φ_0 (µWb)" with a literal underscore, because the build's tex_name does not turn a Greek-letter name into maths (e_0 does) — a plain-text symbol where the student looks is blocking under NOTES §1 — set the labels to `$\\Phi_0\\ (\\mu\\text{Wb})$` (or teach tex_name Greek letters).
- [Major] fig "charger" (lesson.md:53–128; fig-5-390, theory-1280-1) — the labels are only "laturi" twice; the phone, the transmitter coil and the receiver coil are unlabelled, though the text and the simulation name them (lähetinkäämi, vastaanotinkäämi, puhelin). The green triangles and the darker lines are explained only in the aria-label. At 390 px the two panels are small and the dark bar cannot be read as a phone — a reader cannot tell what is the phone and what is the receiver — add $\text{puhelin}$, $\text{vastaanotinkäämi}$, $\text{lähetinkäämi}$ labels as in the simulation, and one short caption phrase for the dark lines.
- [Major] fig "hob" (lesson.md:136–199) — the aria-label says the eddy-current dots and crosses are "violetteja", but in the capture they are orange-brown, like the coil's own current symbols, so the eddy currents are not distinguishable from the coil current by colour, and the alt text is wrong — redraw the pan-base symbols in the violet or correct the description; keep the label "pyörrevirta" with its leader line to the base.

## Polish
- [Minor] sim canvas (sim-390, sim-1280) — the "puhelin" label sits over a green field line and is hard to read at 390 px; give it a paper-coloured backing or move it.
- [Minor] fig hob (theory-1280-2) — "teräskattila" touches the pan wall; move the label left by about 8 px.
- [Minor] Järkevyys in the example — the sentence "2,5 % tehosta 2,0 mW on 0,050 mW" begins with a number; start with "Tehosta 2,0 mW on 2,5 % …".
- [Minor] graph — both curves are the same pink and differ only by dash and end label; fine, but a second tone for 1310 nm would help in print.

## Checked
- Opened: top-390, intro-1280 (hero), fig-5, fig-7, fig-9 at 390, theory-1280-1 to 4, sim-390, sim-1280, example-390-1/2, lab-1280-1, open-ennusta-1280-1, open-tarkista-1280-1, open-exit-1280. Figures 1 to 4 and 6, 8 and 10 are 28 px icons in the captures, not figures.
- Finnish text read in full from the packet: fluent, no stacked AI phrasing, glossary terms consistent, numbers with units in LaTeX.

## Scores
illustrations 3 · typography 4 · Finnish 5 · accessibility 4
