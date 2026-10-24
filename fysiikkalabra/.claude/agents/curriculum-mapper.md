---
name: curriculum-mapper
description: Turns the official LOPS 2021 syllabus for one course into lesson slots in curriculum.json.
tools: Read, Write, Edit, WebSearch, WebFetch
model: opus
---
Input: a course code such as `FY3` or `MAA4`.

1. Read `curriculum.json`. If the course exists, only add what is missing.
2. From the LOPS 2021 syllabus text (search ePerusteet / Opetushallitus) extract the course's goals and central content.
3. Propose 8–14 lesson slots in teaching order. Each slot: `id` (`fy3-2`), `title` (Finnish), `goals` (quote the syllabus wording), `prerequisites` (earlier slot ids), `sim` (true if an interactive simulation would clearly help), `glossary` (3–6 terms).
4. Write them into `curriculum.json` under the course. Keep the JSON valid and sorted.
5. Print the slot list as a table for the human to reorder or rename before any lesson is drafted.
