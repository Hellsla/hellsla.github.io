VERDICT: PASS
CONTENT-HASH: cf1d04190c313c7e

## Blocking

(none)

## Polish

- exercises.json L1-04 and L1-05 — both need a °C to K conversion before one formula, which the rubric puts at level 2 (level 1 is "one formula, values given") — optional: give the temperatures in kelvins at level 1, or accept the conversion as a light level 1.
- lesson.md:105 — one paragraph carries y = kx, the slope pV, the unit chain Pa·m³ = J and the mixed-units rule (about 90 words, four ideas) — split into two: "Kuvaaja: y = kx ... k = pV." and "Yksiköt: ... 1 kPa · 1 l = 1 J ...".
- lesson.md:90 — the paragraph states the law, its validity limits (kokonaispaine vs. mittarin ylipaine) and answers the motivating question — move the sip bag answer first and the validity sentence after it, so the answer is not buried.
- lesson.md:175 (misconception 2) and the kelvin conversion — T = θ + 273 is only taught in fy3-3; one reminder line, "T = θ + 273 K", in the Kaava text would help a student who skipped back.
- sim.js, pressure gauge — the numerals "0" and "300" crowd the needle hub at 390 px; shrink the gauge numerals or drop the "0" label.

## Checked

- Goals delivered: tilanmuutokset (iso-terms in Ydinajatus, Kaava, summary), Boylen lain todentaminen (experiment text plus simulation table), 1/V column and graph (text, figure 2, L2-03, exit ticket 2). Nothing beyond FY3 (pV = nRT is left to fy3-10).
- Prerequisites enough: kelvin conversion (fy3-3), ylipaine and p0 (fy3-4), mikromalli (fy3-8), y = kx (FY1); no unexplained leap. The motivating question (inflated crisp bag on a flight) is a natural one and is answered.
- Figures: three inline SVGs, each right after its paragraph, with informative aria-labels; legible at 390 px (about 14 px text); no horizontal scroll (scrollWidth 390).
- Example: 5 stages with `<!-- vaihe -->`, symbolic first, one step each; reveal buttons work; no exercise repeats the bag example.
- Exercises: level counts 5/4/3, contexts original; exit ticket tests the core idea (Boyle, 1/V linearisation, kelvin); solutions follow given / wanted / formula / substitution / answer / check.
- Finnish: terms match glossary.json (tilanmuutos, isoterminen, isobaarinen, isokoorinen, Boylen laki); case after number and unit correct (101 kPa:n paineessa, 280 kPa:iin, −18 °C:seen); reading level suitable.
- Simulation at 390 px: canvas, buttons and mode select fit; buttons, select and slider are 40 px high; checkbox label 40 px; colour (blue to orange) has a thermometer legend; readout is DOM text; isothermal, isobaric and isochoric modes plus the 1/V toggle all work (simState rows and plotInv updated).
- Visual richness: moving particles, flashes, weight, gauge, thermometer, theory curve with recorded points; not slider-only.
