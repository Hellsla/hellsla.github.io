VERDICT: PASS
CONTENT-HASH: 2a7e930288c2b5a4

## Blocking

## Polish
- assets/sims/fy1/fy1-1/sim.js:42-47 — orbit objects (1 AU, Saturnus, Neptunus, heliopaussi, Oort) are drawn at their diameter (`ext`) but labelled with their radius, in a picture that otherwise shows true size ratios side by side; Mallin oletukset says so, but a student comparing the Sun with 1 AU by eye gets a factor of 2 wrong — label the drawn diameter or draw the radius.
- templates/inquiry.js:22 (shared) — the experiment table shows the integer exponent n as "−10,0", "7,00", "13,0", which reads like a decimal measurement; show integers as integers.
- lessons/FY1/fy1-1/sim-spec.md:1 — says objects show from about 1/2000 of the view; the Laskennan selitys says 1/1000 and the code (a ≥ 0,5) gives about 1/1200; align on "noin 1/1000".
- lesson.md:46 — "nykyiset teoriat eivät enää toimi" is an untested expectation; "teorioiden odotetaan lakkaavan toimimasta" is safer.

## Checked
- Teacher's 2026-10-28 rules: \cdot throughout, no × or \times; divisions as operations use ':' (lesson.md:444, inquiry exp-1 solution); k as \frac; no error quantity in this lesson; every canvas label and readout value goes through LaTeX.
- Recomputed: example k = 6,47·10⁴, Δn = 5; exp-1 5; exp-3 −4; siirto 12 732 km (mistakes 40 000, 6366, 111); check-2 5,79·10⁴ (inverse 1,73·10⁻⁵); 10³⁶ e/g ratio; Sgr A* diameter 2,5·10¹⁰ m; 1 ly 9,46·10¹⁵ m.
- All 43 object sizes realistic; kohdeExp = round(log₁₀ d) matches the glossary's "a about 3" rule.
- Playwright at 360 px: every "Siirry kohteeseen" target lands on that object as nearest, all labels inside the canvas.
- Experiments run in the page: exp-1 rows −10, −10, −15, −18; exp-2 7, 9, 13, 21 (names via kohdeNimi); exp-3 (now starting at L = 27,5) 27, −35, hius −4.
- Predictions' correct options and every feedback's numbers (8 orders Neptune–Milky Way, 6 Milky Way–universe, 42/62 orders).
- Figures: scale-axis and object-types positions to scale (11,8 and 26 px per decade); ladder, matter, cosmic address numbers right.
- Physics: β-decay, residual strong force, Oort cloud, heliopause 120 AU, neutron star 20–25 km, observable universe 93 Gly with expansion.
- Hash changed twice during review (kohdeNimi as varied key, i18n strings, exp-3 start); each diff re-reviewed.
