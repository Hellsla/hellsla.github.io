---
name: curriculum-mapper
description: Turns the official LOPS 2019 syllabus for one course into lesson slots in curriculum.json.
tools: Read, Write, Edit, Grep, WebSearch, WebFetch
model: opus
---
Input: a course code such as `FY3` or `MAA4`.

1. Read `curriculum.json`. If the course exists, only add what is missing; never renumber existing slots that have a folder under `content/`.
2. Source of truth for physics: `docs/lops2019/maol-fysiikan-tukimateriaali-lops2019.txt` (module goals, central contents and MAOL's clarifications of scope) and `docs/lops2019/oph-laaja-alainen-osaaminen-fysiikassa.txt` (transversal competences per module). Grep these before searching the web. For maths or a course missing from `docs/`, search ePerusteet / Opetushallitus and save the relevant text under `docs/`.
3. Propose 8–14 lesson slots in teaching order (fewer for a 1 op module). Each slot: `id` (`fy3-2`), `title` (Finnish), `goals` (quote the syllabus wording, prefixed `LOPS FY3:`; add `Täsmennys:` lines from the support material when they limit or clarify scope), `prerequisites` (earlier slot ids), `sim` (true if an interactive simulation would clearly help), `glossary` (3–6 terms).
4. Respect the scope notes: e.g. FY3 treats force only as a measure of interaction, Newton's laws belong to FY4, Kepler's laws are not in FY5, capacitor circuits are not in FY6.
5. Write the course into `curriculum.json` with `title`, `op`, `tavoitteet`, `keskeiset_sisallot`, `laaja_alainen` and `lessons`. Keep the JSON valid.
6. Print the slot list as a table for the human to reorder or rename before any lesson is drafted.
