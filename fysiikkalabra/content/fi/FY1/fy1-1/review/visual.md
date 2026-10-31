VERDICT: FAIL
CONTENT-HASH: ecf054010b4bf591

## Blocking
- [Major] lesson.md inline maths in prose (theory-1280-1, example-390-1/2, stage-ennusta-390) — an inline `a \cdot 10^{n}` value breaks across lines after the `\cdot` ("1,7 ·" / "10⁻¹⁵ m", "1,1 ·" / "10⁻¹⁰ m", "6,5 ·" / "10⁴"), and a comma is stranded at a line start (", kun $a$ on yli noin 3" after $10^{n+1}$) — mantissa and power are read apart, the worked example is hardest hit on a phone, and NOTES §1 says inline maths stays on one line — make inline `.katex` nowrap (the `.nobr` class exists; long chains keep their mathlayout rows) and keep punctuation attached to the maths it follows.

## Polish
- [Minor] sim-390 readout — "jalkapallo" / ", ihminen" wraps with the comma at line start (same cause as above) — fixed by the same nowrap.
- [Minor] sim-390 canvas — the five name labels and values are about 9 px and nearly touch (muurahainen faded) — acceptable, since the readout repeats the names; enlarge if the canvas allows.
- [Minor] open-tarkista-1280 — distractors/feedback "$8/3 \approx 2{,}7$", "$10^{8}/10^{3}$" use a slash for division; the house rule asks for a colon (`8 : 3`).
- [Minor] open-exit-1280 — the heading "Exit ticket" is English on a Finnish page; use a Finnish heading (e.g. "Lopputehtävä").
- [Minor] lesson.md "Kohdetyyppejä, ei portaita" — "Kaikki tähtitieteelliset kohteet eivät ole portaita" can read as "not all are"; write "Mikään tähtitieteellinen kohdetyyppi ei ole portaan paikalla samassa sisäkkäisyydessä" or "Nämä kohteet eivät ole portaita…".

## Checked
- Opened fig-1…fig-8 (390), top-390, sim-390, sim-1280, lab-1280, intro-1280, theory-1280-1…5, example-390-1/2, stage-ennusta-390-1, stage-tutki-390-1/2, exp-1 and exp-3 (390), open-ennusta-1280-1, open-tarkista-1280-1, open-exit-1280. Figures are clear, labelled in LaTeX, legible at 390, "ei mittakaavassa" stated, force red; the axes read correctly. Exercise captures are judged in the exercise report.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 4
