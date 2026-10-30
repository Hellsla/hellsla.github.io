VERDICT: PASS
CONTENT-HASH: 23c8f56ca94e5cab

## Blocking
None.

## Polish
1. docs/coverage/FY4.md is stale: it was generated before these tasks and shows "Sovella itsenäisesti: –" for every competence. The gaps it lists are real, and the tasks close them: concept (s2 d, s3 d), math, graph and building a graph from data (s1 a, c), experiment (s1 d), communication (s3 d), transfer (s2, s3 a/b). Run `python scripts/coverage.py FY4` before merging so the table shows it.
2. s1 b model solution: the dashed components G_x and G_y in the figure are not mentioned in the text, yet the common-mistakes list warns against drawing components as extra forces. Add one sentence saying they are auxiliary and the student need not draw them.
3. s1 c: answer.value (0,030) checks only wax A, but the part asks for both. Consider stating that the answer field is A's value, or splitting the part.
4. s2: "vaijeriliu'ussa" is correct Finnish but looks like a typo to a student. Use "vaijeriradalla" or another phrasing.
5. s2 has no situation picture; a simple side profile of the cable (15 m drop, 180 m) would help. Optional.
6. s3 d draws on recall of the headrest more than on the police report. It is a fair concept item at 3 points but the least "interpret the source" part of the set.
7. Workload: s3 has 5 parts and 16 points (about 35 min), the heaviest task. Acceptable, but do not add more.

## Checked
- Independence: no heading or prompt names the model or formula. The weakest case is s2 a, which hints at an idealised calculation but does not name energy conservation. Titles are neutral. Situations are unfamiliar and authentic.
- s1 gives a data table to interpret and has four connected parts of rising demand: graph, force diagram, calculation, then reliability. It keeps FY1's linear-model skills. Its common mistakes (μ = a/g, N = mg, a forward force, components counted twice, reading the slope from adjacent points) are real. The simulated-data note is honest.
- s2 contrasts a claim with a measurement. Parts c and d force a model comparison, and the "between the two estimates" conclusion is sound.
- s3 uses source material (a police report with distractor data), a stated assumption check in b/e, and the impulse link in c/d. e is checked against the solution numbers (vB max 15,2 m/s).
- Rubrics: no points for irrelevant things. Solutions follow the Annettu/Kysytty/Periaate structure and a student can learn from them. Numbers match answers.py; practice.py check is OK.
- Variety: graph/experiment/FBD, energy, and momentum/impulse/safety. Spread across the module's goals (graphs, conservation laws, safety). Not covered: Newton 1 and 3, coupled bodies, wind and hydro power. Reasonable for 3 tasks.
- Force diagram: s1 b is a draw-alone task. The model figure is scaled and the diagram comes before the equations in c.
- Finnish checked, no errors found.
- Layout: python scripts/build.py FY4-sovella, then check_layout.py FY4-sovella --width 360: OK at 360 px.
