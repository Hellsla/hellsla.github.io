VERDICT: FAIL
CONTENT-HASH: ee2c8ead5cfa8ced

## Blocking
- [Major] example-390-1 (Esimerkki vaihe 3, ratkaisukaava), open-tarkista-1280-2 (check-2 Kaava and Sijoitus) — wherever the page sets an inline chain that starts `t = \dfrac{…}` as rows, the left side $t$ sits at numerator height and the first `=` drops below the fraction bar, so $t$, `=` and the fraction are on three different levels. The other rows (`= 6,0 s`) are fine — the quadratic formula and the check solution look broken, and this is the formula the worked example builds on — set the first row's left side and relation on the fraction's math axis in the row layout (`scripts/mathlayout.py` / its CSS; the source is correct, so this is a template fix, not a content fix) and recapture.

## Polish
- [Minor] fig-5-390, theory-1280-2 (figure kaava) — the $x_\text{B}$ line runs through the "lähtö" label, and $x_\text{A}$ goes past the last gridline (64 m above 60; in the esimerkki figure 100 m above 96) — move "lähtö" below the start dot and end each curve at the last gridline or add a gridline.
- [Minor] exp-exp-3-390-1 — "Käytössä:" has nothing after it (Koe 1 and Koe 2 name their case), and at this width the readout splits "$a_\text{A} =$ / $1{,}0\,\text{m/s}^2$" across lines — give the label its case name and keep each quantity together.
- [Minor] open-tarkista-1280-2, open-exit-1280 — the exit-ticket heading reads "Exit ticket" in English on a Finnish page — "Lähtölippu" (template string).
- [Minor] lesson.md Ydinajatus, 3rd paragraph — "Kohtaamishetkellä kappaleiden kuvaajat leikkaavat toisensa." repeats "Kohtaaminen on viivojen leikkauspiste" from two sentences earlier — delete it.
- [Minor] inquiry.json exp-2 question, siirto — "Vastaa yksikössä m/s." has the unit in plain text, while the solutions write "yksikössä $\text{m/s}$" — write it the same way. Also, at 390 px inline formulas wrap mid-formula (example vaihe 3 "$x_\text{B} = x_{0\text{B}} +$ / $v\,t$").

## Checked
- contact-2, contact-3 (triage); top-390, intro-1280, theory-1280-1/2/3
- fig-1…fig-6-390 (hero, ei-kohtaa, tilanne, kohtaus, kaava with a zoom on "lähtö", vt)
- example-390-1/2/3 (zoom on the ratkaisukaava row)
- sim-390, sim-1280, lab-1280-1/2
- exp-exp-1-390-1, exp-exp-3-390-1/2
- open-tarkista-1280-1/2, open-exit-1280
- Colours: force red, velocity blue and acceleration orange are kept apart in the sim legend and tilanne; the vectors are $\overline{v}$. I found no plain number+unit in prose.

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 4
