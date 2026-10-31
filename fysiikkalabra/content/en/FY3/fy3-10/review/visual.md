VERDICT: FAIL
CONTENT-HASH: f77ed29cd96c1d51

## Blocking
- [Major] simulation readout and canvas (sim-390, sim-1280) — the English page shows decimal commas: "1,17", "0,0 s", "0,5 s", axis ticks "1,5", "0,5" — while the lesson, tasks and experiments use decimal points ("0.207 mol"); the same quantity is written two ways within a few lines, and "mean over 0,0 s" reads oddly — switch the sim's number formatting to the point for lang=en (including the experiment tables if they copy readout values).
- [Major] exercises/exercises.json (L1-01 "0.250 m³", L1-02 "0.00710 m³", L1-04 "0.200 m³", L2-01 "1 bar = 100 kPa", L2-02/03/L3 "101 kPa", "4.60 MPa", "10.0 bar", "7.0 bar") — numbers with units sit in prose as plain text next to maths ones in the same sentence (L1-01: "0.250 m³" plain, "$278\,\text{K}$" maths); this breaks the project rule that number+unit is maths (NOTES §1) and the typeface/spacing differs visibly (open-exercises-1280-1) — wrap each as `$0.250\,\text{m}^3$` etc.

## Polish
- [Minor] lesson.md Formula, "where $p$ is the pressure (Pa), $V$ the volume (m³) … (K)" — units in plain text/Unicode ³ — write `$\text{Pa}$`, `$\text{m}^3$`, `$\text{K}$`.
- [Minor] sim 1280 (sim-1280) — the slider grid wraps "Number of particles N = / 100" onto two lines and puts Volume on a second row; align the three sliders on one grid.
- [Minor] lesson.md, "...we get the equation of state of an ideal gas" — sentence ends without a colon before the display formula; add ":".
- [Minor] `\textsf{l}` renders as "5.0 l" resembling "5.0 I" (fig/example-390) — project convention; consider a script ℓ only if the teacher agrees.
- [Minor] mole-masses figure — the "m = 4.00 g" bar is very small beside the 44.0 g bar; it is to scale, but the description should say so.

## Checked
- Contact sheet 1; figures fig-1…fig-5 at 390 px (all legible, nothing clipped, colours consistent, labels LaTeX).
- sim-390, sim-1280; example-390-1 (steps 1–4), contact sheet for rest of example; intro-1280; theory-1280-1 and -2.
- open-exercises-1280-1 (L1) and open-exercises-L2-1280-6 (graph exercise solution).
- Source of lesson, inquiry.json, exit ticket, exercises read in the packet; not opened one by one: other contact sheets, remaining exercise and tarkista captures.

## Scores
illustrations 4 · typography 4 · Finnish (English) 4 · accessibility 4
