VERDICT: FAIL
CONTENT-HASH: 2c1c2a557074f30d

## Blocking
- [Major] Tutki, koe-1/3/5 "Alkutila" lines (lab-1280-1, exp-koe-1/3/5-390, stage-tutki-390) — values with Ω appear in plain sans text ("etuvastus = 330 Ω", "kuormitusvastus = 0 Ω", "= 50 Ω") beside LaTeX values ("lähteen jännite = 2 V", "1000 W/m²") — plain number+unit in student text (NOTES §1, Major in new text), mixed typefaces on one line — cause: scripts/inquiry.py UNIT regex `[A-Za-z/%]+[²³]?` excludes Ω, so fmt() falls through to the plain branch — add Ω to UNIT (template, no content change) and rebuild. Content itself is clean.

## Polish
- [Minor] fig "teho" (fig-12-390, theory-1280-4) — peak label "maksimiteho" is not the glossary term and the upper panel's axis nearly touches the lower panel's "P (W)" — use "maksimitehopiste" (or $P_\text{max}$) and add a few px between panels.
- [Minor] figs "kenno"/"teho" (fig-8, fig-12) — I-curves are blue while the circuit's current arrows are violet; blue is the electron/velocity colour in FY6 — keep, but be aware of the implication; at least keep the sim's violet operating point consistent in text.
- [Minor] fig "ominaiskayra" (fig-6-390) — legend sits close to the silicon curve at 390 px; shift legend left or shorten.
- [Minor] sim canvas (sim-390) — x-axis ticks "−1" and "0" crowd each other.
- [Minor] lesson "Yleinen virhekäsitys" (theory-1280-4) — inline "U − U_D" breaks across lines after the minus; keep together with `\,` non-breaking grouping.

## Checked
- contact-1…4,6,7; top-390, intro-1280 (hero, learning goals, Pohjatiedot); figs 4 (suunnat), 6 (ominaiskayra), 8 (kenno), 10 (etuvastus), 12 (teho), 14 (Tarkista graph) at 390; hero via fig-1/intro.
- sim-390, sim-1280, lab-1280-1, example-390-1/2, theory-1280-1/3/4, open-tarkista-1280-1, stages via contact sheets (Pohdinta, Ennusta, Tutki, Sovella, exit ticket).
- Circuit colours: current arrows violet, forces none, LED red as component colour; all figure labels LaTeX; sim canvas and readout LaTeX; arrow direction and diode orientation consistent in both panels.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
