VERDICT: PASS
CONTENT-HASH: 4bdb4c08e06070a4

The lesson does what its goals promise and tells one story. It starts with the astronaut question, moves through interaction, force and the voimamittari with its calibration, reaches G = m g with g in m/s², and returns to the astronaut with the new kuudesosa sentence (lesson.md:63). It stays inside FY3: force never causes motion, there are no vectors, and 1 N = 1 kg·m/s² is left to FY4. All four round-3 Polish items are applied. L1-04 is now independent of the Ydinajatus spring, and exit tickets 1 and 3 test the main goal and the mass-versus-weight confusion. Each level now has at least one spring task and at least one task that uses G = m g. The length (719 words) matches fy3-2 (703) and fy3-3 (829). The gold lesson is still a placeholder, so I compared against these two.

## Blocking
(none)

## Polish
- lesson.md:47 — "Kuu on massaltaan ja kooltaan paljon pienempi kuin Maa, joten … heikompi" says that the smaller size also weakens the interaction. On its own, a smaller radius would make g larger. — Use "Kuu on paljon pienempi taivaankappale kuin Maa, ja Kuun ja astronautin välinen vuorovaikutus on heikompi …". This states the fact without giving a wrong cause.

## Checked
- Lint: 0 errors, 0 warnings. The editor hash was the same at start and end.
- meta.json goals equal curriculum.json, and all seven glossary terms are in glossary.json.
- There is no N/kg in any lesson file. The g values agree in the table, the exercises, sim.js:14 and sim-spec.
- answers.py was re-run, and all 12 answers match exercises.json. Significant figures follow the data.
- L1-04 (4,0 N ↔ 2,5 cm, 6,0 cm → 9,6 N) appears nowhere in the theory. No exercise repeats the robot example.
- Levels have 5/4/3 exercises.
- Exit tickets: 3,0 kg gives 29 N and 4,9 N, and 1,5 kg gives 15 N. Answer 1 names the interaction, and question 3 quotes the water.
- The kuudesosa sentence (1,62/9,81 ≈ 0,17) answers the opening question.
- The sim-spec readout and the m · 24,8 m/s² chart scale match sim.js:48 and sim.js:94.
