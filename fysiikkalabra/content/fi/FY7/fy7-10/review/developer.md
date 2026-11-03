VERDICT: DONE
Draft of fy7-10 *Valon heijastuminen ja taittuminen*; `check_lesson.py fy7-10` all ok.

- lesson.md: Ydinajatus (rays and normal, law of reflection, n = c : v and wavelength, why light refracts from wavefronts, towards/away from the normal, partial reflection, apparent depth), Kaava: Heijastuslaki ja taittumislaki (β = α₁, n = c : v, Snell, table of n with CRC 2016 source), staged example (air → water 55,0°: α₂ and v), misconceptions, summary.
- figures.py: hero (straw in a glass), interface, wavefronts, depth, graph α₂(α₁), scene; task figures fit (LOPS experiment) and protractor (L2-04).
- inquiry.json: 2 predictions, sim, koe-1 (α₁ varied, air → water), koe-2 (material varied), conclusion, LOPS interpret task (acrylic n from the slope of sin α₁ vs sin α₂, Vernier Graphical Analysis, example data), speed, transfer (aquarium wall), 3 checks, exit ticket.
- exercises 5/4/3 with solutions; answers.py, lesson-answers.py.
- New sim assets/sims/fy7/fy7-10 (laser on a protractor, two material selects, α₁ slider, Fresnel R readout), tests/sims/fy7-10.json (21 assertions), lang sims.fy7-10, glossary: taittuminen, taitekerroin, Snellin laki.
- Not fixable here: lint warns that the course's ray colour #e64980 is outside the figure palette (scripts/lint_lesson.py PALETTE).
