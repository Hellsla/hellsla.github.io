VERDICT: PASS
CONTENT-HASH: de4174ac1f57e923

## Blocking

## Polish
- content/en/FY7/fy7-13/inquiry.json (kertaus-interferenssi, correct feedback) — "Today the same condition explains…" reads oddly (fi "tänään" = in this lesson) — "In this lesson the same condition…".
- lang/en.json sims.fy7-13.r_2_none — "because 2λ > d"; the sim drops k = 2 also when 2λ = d (reachable: N = 1000, λ = 500 nm), as the lesson's kλ < d says — "2λ ≥ d" (same in fi and fi-easy; inherited).
- content/en/FY7/fy7-13/inquiry.json:hook — "evenly spaced" dots hold only at small angles (x = L tan θ) (carried over from fi).

## Checked
- Translation against the passed fi: every number of lesson.md, inquiry.json and exit-ticket.json equal to fi (script, decimal comma normalised); only change "1800-luvun alussa" → "beginning of the 19th century" (correct).
- All 8 figures: SVG geometry identical to fi; every label and aria-label (figures.json) keeps its numbers; labels translated correctly (wide/narrow slit, bright/dark, intensity, grating, screen).
- Recomputed in one script with my own formulas: koe-1 11,24°/19,9 cm, 22,95°/42,4 cm, 40,54°/85,5 cm; koe-2 15,66°, 18,61°, 22,95°; mistakes 705,9 nm and 17,70°; mittaus 532,7 nm (530–536 nm, k = 1: 531 nm, 526–536 nm), mistakes 1065, 932, 562 nm; DVD 61,45° (24,0°, 41,3°); Na 36,09° (17,13°); example 647,4 nm (tan 660 nm); Kaava 18,61°, 33,7 cm; d : λ = 2,56; white 6,89°/12,12°; exit ticket 4,0 µm. All agree.
- Physics wording: coherence and lamp phase, diffraction width vs slit, double-slit dark fringes, grating narrow maxima, kλ < d with the edge case, tan-then-sin, red deviated most vs prism, CD/DVD reflection grating with perpendicular incidence — all faithful to fi, no condition dropped.
- Sim strings (lang/en.json): model, units and readouts correct; howto/model/calc boxes state perpendicular incidence, one wavelength, to scale, dimming illustrative, model values.
- en has no Finnish visible in names, units or measure labels (ids/stage keys are internal).
