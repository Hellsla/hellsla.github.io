VERDICT: PASS
CONTENT-HASH: d60bbb553ac5682a

## Blocking

## Polish
- content/en/FY7/fy7-16/lesson.md:51 — "This is why the gap ... is only a few millimetres" now follows the sentence about how the figure is drawn, so "this" can be read as pointing at the drawing rather than at the steep fall of flux — move the figure sentence after "...is only a few millimetres" (same order in fi; not a translation error).
- content/en/FY7/fy7-16/inquiry.json:63 — "weakens steeply once the distance becomes as large as the radius of the coil": the model's half-value is at 8.8 mm, under half the 20 mm radius — "already at distances smaller than the radius of the coil" would fit the numbers (same in fi, which passed).

## Checked
- Every number in lesson.md, inquiry.json, exit-ticket.json and the figures is the same as in the passed fi version (scripted field-by-field and paragraph-by-paragraph diff); the figures differ from fi only in label text and label box widths, the graph's 16.7 km label in decimal point.
- Coupling model recomputed independently with the Neumann integral (not the elliptic form): e0 = 4.404 / 1.957 / 0.869 / 0.445 V at 3/10/20/30 mm, share 19.74 %, half-value 8.8 mm, Φ0 = 0.501 µWb; R1 scan at 20 mm 0.285/0.869/1.211/1.247/1.229 V (optimum 35.4 mm), at 3 mm optimum 20.7 mm; field-line counts 6 and 1.
- koe-1 numeric 19.74 % and mistakes 80.26 % / 506.6 %; koe-1/koe-2 lock the right parameter and simState gives phi0, e0, osuus.
- Ravenscraft data 47.3 %, mistakes 6.75 / 147.3 / 32.1 %; offset case 79.7 %.
- Fibre: halving 16.7 km, 1.58 % after 100 km, graph 35 % / 16 % at 25 km, 4.9 µs/km, worked example 0.0502 mW (2.5 %), check-2 25.1 % with mistakes 40 / 74.9 %, exit ticket 20 dB.
- siirto B0 = 0.775 mT, mistakes 9.30 / 4.87 / 7.75·10⁻⁵ mT, ≈15 × Earth's 52 µT.
- Exactly one correct option in every choice; each distractor's feedback states the right physics (DC gives constant flux, eddy currents in Al, glass not conducting, decibels multiply).
- Translated physics checked against fi: Lenz direction, ferrite, skin-layer argument for steel vs aluminium, attenuation by absorption and scattering, "model values" wording kept.
- Sim (en build, 390/1280 px captures): English labels and readouts, values match the recomputation; model box states no ferrite, no load, constant current.
