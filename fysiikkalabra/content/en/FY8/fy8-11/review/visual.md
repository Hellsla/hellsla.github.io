VERDICT: FAIL
CONTENT-HASH: 58c9cf965e5f11f7

## Blocking
- [Major] sim canvas (sim-390, lab-1280-1; assets/sims/fy8/fy8-11/sim.js:138,181) — labels "reaktorin sydän" and the axis label "sukupolvi g" are Finnish inside the English page; the same chart shows English controls — the student meets an untranslated axis title in the key investigation tool — render them via the language mechanism (reactor core; generation g).
- [Major] figures.json, fy8-11/sidosenergia-luku (task figure of check 2) — the figure description is Finnish ("Kuvaaja mittakaavassa: ytimen sidosenergia ... 20:stä 240:een ...") on an English page; screen-reader users get Finnish, and the description is part of the task's accessibility — translate it, keeping the axis-break note.

## Polish
- [Minor] exercise answer boxes (L2-02, L3-02, siirto) — unit written as plain "10³⁷ 1/s" while the answer line is typeset as $10^{37}\,\tfrac{1}{\text{s}}$; fine if project-wide, otherwise align.
- [Minor] fig-4 (binding energy graph) — the two arrows overlap the plot area and the "fusion" arrow ends near the curve peak; shorten it slightly so it does not look like a data point.
- [Minor] fig-10 (reactor) — fuel rods inside the vessel have no label while control rods do; add "fuel rods".

## Checked
- Opened: top-390/top-1280, sim-390, lab-1280-1, example-390-1, fig-1, 4, 6, 8, 10, 12, 14, 16, 18 (390), open-exercises-1280-1 and L2-1280-1 in the lesson set.
- Figures are uncluttered, labels in LaTeX, consistent palette (orange energy, green fusion, blue water), legible at 390 px; `Q` and units typeset correctly; example steps and equations aligned, no clipping.
- English is natural and consistent with the glossary terms; units use thin space and \cdot.
- Hash at start and end: 58c9cf965e5f11f7

## Scores
illustrations 5 · typography 5 · Finnish (English text) 4 · accessibility 3
