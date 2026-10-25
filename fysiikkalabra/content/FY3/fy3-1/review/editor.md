VERDICT: PASS
CONTENT-HASH: 602a68e8bcb43fde

The lesson does what its goals promise and tells one story. It opens with the astronaut question, then covers interaction, force and the voimamittari with its calibration. It reaches G = m g with g in m/s² and answers the opening question with the kuudesosa sentence (lesson.md:38, now "≈ 0,17 ≈ 1/6"). The new Moon sentence (lesson.md:22) states the fact without giving a wrong cause, and the summary (lesson.md:55) now gives 9,81 N without "noin", which matches the 1 kg data. The new Mars L3-03 closes the story well. It takes the kylpyhuonevaaka idea from the misconception section (lesson.md:50) into an unfamiliar context and does not solve it in advance, because the theory only mentions the Moon. The lesson stays inside FY3: force never causes motion, there are no vectors, and 1 N = 1 kg·m/s² is left to FY4. The length (717 words) matches fy3-2 (703) and fy3-3 (829). The gold lesson is still a placeholder.

## Blocking
(none)

## Polish
- exercises.json:98 — "näyttää kilogrammoina luvun, joka saadaan jakamalla voima arvolla 9,81 m/s²" is a little heavy. — Optionally use the lesson's wording: "Voimamittarin kilogramma-asteikko on tehty Maassa jakamalla voima arvolla 9,81 m/s²."

## Checked
- Lint: 0 errors, 0 warnings. check_latex: 8 fragments OK. The editor hash was the same at start and end.
- meta.json goals equal curriculum.json, and all seven glossary terms are in glossary.json.
- There is no N/kg in any lesson file. The g values agree in the table, the exercises, sim.js:14 and sim-spec.
- answers.py was re-run, and all 12 answers match exercises.json. L3-03: 26 · 9,81 / 3,71 = 68,75 → 69 kg, inside the 0,02 tolerance at 2 sf.
- L3-03 needs both ideas (scale reading means G/9,81, then m = G/g_Mars) and its sanity line explains why mass > reading.
- Levels have 5/4/3 exercises, and each level has a spring task and a G = m g task. No exercise repeats the robot example.
- Exit tickets: 3,0 kg gives 29 N and 4,9 N, 8,0 N → 3,0 cm gives 20 N → 7,5 cm, and 1,5 kg gives 15 N. They test the main goal and the mass-versus-weight confusion.
- The worked example's reason (lesson.md:47) and exit ticket 1 use the same interaction wording as lesson.md:22.
- The sim-spec readout and the m · 24,8 m/s² bar scale match sim.js:6 and sim.js:19–20.
