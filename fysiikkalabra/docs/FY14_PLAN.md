# FY14 – Road to Fusion: plan

*From the Birth of Modern Physics to ITER.* Kiviruukin lukio's school-specific interdisciplinary course (physics,
English, French; CLIL), authors **Lauri Hellsten and Marjo Inkala**. Teacher's brief 2026-11-01 (the full brief is in
the project thread; this file is its durable summary). Registry entry `FY14` in `local-courses.json`
(status `building`, language `en`), page `site/FY14.html` and `site/en/FY14.html`, units in `site/en/`.

## The central question
*If scientists have understood nuclear fusion for almost a century, why is producing electricity from fusion still
so difficult?* Every chapter adds one part of the answer: physics (binding energy, the Coulomb barrier, tunnelling),
plasma (temperature, density, confinement time, instabilities), history and politics (secrecy, the Cold War,
verification, cooperation), engineering (magnets, materials, tritium, heat exhaust) and economics. Students should
experience the course as an investigation, not read an electronic textbook.

## Architecture (implemented 2026-11-01)
- **Course units** (`scripts/units.py`): one page per lesson, `content/en/units/<id>/` (`unit.json`, `unit.md`,
  `inquiry.json`, `teacher.md`, `review/`), figures in `lessons/units/<id>/figures.py`. A unit reuses the lesson
  template and the inquiry stages (docs/inquiry.md) and is published under the same three-review gate (science,
  pedagogy, visual & editorial) on its own content hash. Units are written in English and built only into
  `site/en/`; the Finnish and selkosuomi course pages link there and say the course is taught in English.
- **Components** (`assets/units/fy14/`, published as `units/fy14/`): `units.js` loads `fx/<kind>.js` for every
  `<div class="fx" data-fx="<kind>">` in a unit, with its data in a JSON script inside. Built: `match` (matching and
  sorting), `order`, `gapfill`, `say` (French phrases with the browser's French voice), `dialogue` (read → practise →
  perform), `video` (click-to-load youtube-nocookie). Planned: `timeline`, `map` (Leaflet + OpenStreetMap, data in
  `assets/units/fy14/data/facilities.json`), the explorers (isotope builder, binding energy, fusion reaction and
  energy scales, tokamak vs stellarator, ITER components). Data files live in `assets/units/fy14/data/` and are part
  of the hash of every unit that refers to them.
- **Simulations** that support guided experiments (the inquiry `experiment` activity) are ordinary p5 sims in
  `assets/sims/fy14/<name>/` with their texts in `strings.json` (`{"en": {...}}`), not in `lang/*.json`.
- The course page shows the authors, the chapters with their big questions and every unit (published ones linked).

## Chapters and units
1. **The Birth of Modern Physics** — *Why did classical physics fail to explain everything?* classical limits and
   blackbody radiation (Planck), the photoelectric effect (simulation, Einstein), Rutherford and Bohr (energy levels,
   spectra), waves, probability and tunnelling. A timeline of modern physics with short original biographies.
2. **Inside the Atom** — *How can such a small nucleus contain so much energy?* nuclei, isotopes and notation
   (Isotope Builder); mass defect, $E = mc^2$, binding energy per nucleon (Binding Energy Explorer), fission and fusion.
3. **The Energy of the Stars** — *Why hasn't the Sun burned out?* chemical and gravitational explanations,
   Eddington, the Sun's lifetime estimate; the proton–proton chain, Coulomb barrier and tunnelling, D–T fusion
   ($^2\text{H} + {}^3\text{H} \to {}^4\text{He} + \text{n} + 17.6\ \text{MeV}$, 3.5 MeV + 14.1 MeV), the first laboratory
   fusion reactions, energy scales.
4. **Plasma** — *How can we control something hotter than the centre of the Sun?* ionisation, plasma in nature;
   charged particles in magnetic fields (simulation), magnetic confinement, the triple product, instabilities.
5. **The Cold War and the Race for Fusion** — *How did the Cold War influence scientific research?* secrecy to 1958,
   Richter, pinches, stellarators, tokamaks; ZETA; T-3 and the 1969 Culham measurement (*Science Across the Iron
   Curtain*); oil crisis, PLT, TFTR, JET, JT-60; Geneva 1985 and the origins of ITER; the interactive timeline.
6. **From Early Machines to Modern Reactors** — *Which reactor design has the best chance?* pinches, inertial
   confinement, spherical tokamaks, HTS magnets, alternatives; the Tokamak vs Stellarator explorer (non-inductive
   current drive included).
7. **ITER** — *Can the world's largest fusion collaboration succeed?* why, where (Cadarache) and who; the machine and
   $Q = P_\text{fusion} / P_\text{heating}$ (Q = 1, ITER's Q = 10 aim, plasma gain vs electricity); the video CLIL
   activity; the media-literacy task *ITER: Promise, Progress and Reality* (HS 2018, Yle).
8. **Fusion, Energy and Society** — *Could fusion become part of our future energy system?* evaluation of claims,
   the structured debate, the Global Fusion Explorer map (*From Competition to Collaboration*).
9. **Fotoni Lab Visit** — before / during / after, the printable worksheet, English lab reporting.
10. **Le français de la fusion** — introductions, numbers and prices, the café role-play, at a research centre in
   Provence, reading French news by cognates. Every physics unit also ends with a short *French corner*.

## Verified facts that may change (check again before publishing a unit that uses them)
- ITER baseline (2024, iter.org / Wikipedia 2026-11-01): start of research operation 2034, deuterium–deuterium
  operation 2035, deuterium–tritium operation 2039; the earlier "first plasma 2025" plan is superseded.
- Fotoni material bank (helsinki.fi, read 2026-11-01): photoelectric effect and Planck's constant (stopping voltage,
  3 stations), electron charge-to-mass ratio $e/m$ (2 stations), double slit incl. single photons (pre-collected
  data), Millikan (qualitative), blackbody radiation of a filament, spectra of lamps and gas tubes (3 stations),
  thermal radiation and climate package.
- Video 4BkOUOK0XzM: "We Went Inside the Largest Nuclear Fusion Reactor", The B1M, 13 Apr 2022 (contains a paid
  promotion; a source-evaluation point). Its spoken content could not be read from the sandbox: video-specific
  questions are limited to what the title, description and chapters show until the teacher has watched it.

## Limitations (documented, not hidden)
- The sandbox could not reach Wikimedia Commons or hs.fi on 2026-11-01. Photographs come from a separate photo thread
  (`/mnt/project-files/fy14/photos/`, manifest with licences) and are added unit by unit; until then units use
  original SVG figures.
- Browser speech synthesis is a model voice, not a native speaker; the units say so.
