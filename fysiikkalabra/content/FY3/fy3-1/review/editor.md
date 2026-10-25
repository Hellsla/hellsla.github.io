VERDICT: PASS
CONTENT-HASH: 0eb40272800b66b3

The lesson delivers its goals and tells one story: interaction, then force, then the voimamittari with its calibration (the SVG now closes that paragraph), then G = m g with g in m/s², and back to the astronaut question. It stays inside FY3: no motion is explained by force, there are no vectors, and 1 N = 1 kg·m/s² is left to FY4. The round-2 Polish items are applied. The rewritten L1-02 and L1-04 now cover proportional stretch in both directions. Exit ticket 3 now adds a calculation to the mass-versus-weight question. The length (693 words) matches fy3-2 (703) and fy3-3 (829).

## Blocking
(none)

## Polish
- exercises.json:30 — L1-04 reuses the Ydinajatus spring (5,0 N ↔ 2,0 cm, lesson.md:32). Its answer, 7,5 N, is the sum of the two cases worked there. — Use new data, e.g. 4,0 N ↔ 2,5 cm, asking about 6,0 cm (9,6 N), and update answers.py and solutions.md.
- lesson.md:46 — "Kuun massa on paljon pienempi …, joten …" makes mass the only cause. The table (lines 55-60) contradicts this: Jupiter has about 300 times the Earth's mass but only 2,5 times its g. — Write "Kuu on paljon pienempi kuin Maa, ja …", or add that g depends on the body's mass and size.
- exit-ticket.json:7 — The question gives the water's mass, but the quoted sentence is about the bottle ("pullo painaa"). — Quote "vesi painaa puolitoista kiloa".
- exit-ticket.json:4 — No exit-ticket answer names the main goal, force as a measure of interaction. — End answer 1 with "koska Kuun ja kappaleen välinen vuorovaikutus on heikompi kuin Maan ja kappaleen".

## Checked
- Lint: 0 errors, 0 warnings. The hash was the same at start and end.
- meta.json goals equal curriculum.json. voimamittari is in glossary.json.
- No N/kg in the lesson, exercises, exit ticket or sim-spec. The g values agree in the table, exercises and sim.
- All 12 answers recomputed. Significant figures follow the data.
- Levels have 5/4/3 exercises. None repeats the robot example.
- The FY1 reference (lesson.md:32) is valid: fy1-5 covers s = vt and direct proportionality.
- The sim-spec readout line and the m · 24,8 m/s² full scale match sim.js:47-50.
- L3-03 matches the bathroom-scale model (lesson.md:72).
