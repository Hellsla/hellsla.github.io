VERDICT: PASS
CONTENT-HASH: e854342069b55ac8

## Blocking

## Polish
- exercises.json:98 (fy3-1-L3-03) — I hold to this item. Asking for the number is fair, but lesson.md:50 already says "noin kuudesosan". 6,0 kg / 6 = 1,0 kg is within 1 % of 0,99, so it is inside the tolerance. The student only reads one sentence and never combines the Earth calibration with the Moon's g, so the task is level 1–2 work. — Keep the scale context and the numeric answer, but use a body whose ratio the lesson does not state, and turn the task round: "Voimamittarin asteikko on tehty Maassa niin, että se näyttää kilogrammoina voiman jaettuna arvolla 9,81 m/s². Marsissa (g = 3,71 m/s²) mittari näyttää 26 kg. Mikä on kappaleen massa?" answers.py: 26 · 9,81 / 3,71 = 68,75, answer 69 kg, tolerance 0,02.

## Checked
- The hash was the same at the start and at the end. The lint reports 0 errors and 0 warnings.
- Last round's paragraph-split item (lesson.md:8) is withdrawn because the editor asked for the merge. The paragraph still adds one idea at a time.
- lesson.md:38: the kuudesosa sentence closes the line 3 hook with the table value.
- lesson.md:22: the Moon sentence names size and mass. It is accessible and consistent with the table, and the exact wording belongs to the physics-expert.
- exercises.json:30: the new L1-04 data (4,0 N ↔ 2,5 cm, 6,0 cm gives 9,6 N) no longer reuses the lesson.md:8 spring. It is one proportion, so level 1 fits.
- exit-ticket.json: q1 now gives the interaction reason, q2 tests proportional stretch, and q3 quotes "vesi painaa" for the 1,5 kg of water. All three test core ideas.
- putoamiskiihtyvyys is in glossary.json and meta.json, and its definition matches lesson.md:29. Every meta.json term exists in glossary.json.
- I recomputed all 12 exercise answers and the 3 exit-ticket answers (29 → 4,9 N; 7,5 cm; 15 N). They match answers.py and the data's significant figures.
- Levels are 5/4/3 and follow the rubric (L3-03 aside). No exercise repeats the 120 kg robot example.
- Scope is FY3: there is no N/kg, no vectors and no force as a cause of motion. 1 N = 1 kg·m/s² is deferred to FY4.
