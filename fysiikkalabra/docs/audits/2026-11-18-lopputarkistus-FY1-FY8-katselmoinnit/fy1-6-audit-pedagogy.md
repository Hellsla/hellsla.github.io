VERDICT: PASS
CONTENT-HASH: 2b496ad3e6b080b1

## Blocking
(none)

## Polish
- inquiry.json `data` (interpret, optional) — the text says measurement errors scatter the points "tasaisesti suoran molemmille puolille" and the solution says they deviate "noin 0,1 m/s". The table (1,0; 2,0; 2,9; 3,9; 4,9) lies on or just under the line (deviation at most 0,04 m/s), so the "noisy data" the task promises is not there. Fix: use values that scatter on both sides (e.g. 1,1; 1,9; 3,1; 3,8; 5,0) and redraw the figure, or drop the claim. [Major as a stated learning aim of FY1 ("luotettavuuden arviointi"), but optional]
- lesson.md "Massa ei vaikuta putoamiseen" / inquiry `hook` — the opening question rests on the Moon having no air, but no sentence says so; the lesson jumps from "Kuussa" to "tyhjiössä". Add one clause ("Kuussa ei ole ilmakehää") in the hook or the section. [Minor]
- inquiry.json `hook` question "Kasvaako putoavan kappaleen nopeus tasaisesti" — "tasaisesti" echoes "tasainen liike" (constant velocity) from fy1-5 and can be read as "stays constant". Fix: "kasvaako nopeus joka sekunti yhtä paljon". [Minor]
- inquiry.json `siirto` — answer 11.1 with the solution's final "11 m/s" (two figures); keep one value. Also lesson.md "nopeuden kasvunopeus" is clumsy; "nopeuden muutosnopeus" or "nopeuden kasvu sekunnissa". [Minor]
- No prediction for the air case (exp-3), although everyday experience (feather) is the main misconception; the student first meets it as a result. Consider one prediction in the closed "Lisää ennusteita" box. [Minor]

## Checked
- Path: retrieval (s/t) → v(t) linear → g from slope → mass → air; prerequisites match fy1-5 and the graph chapter; slot goals both met, nothing beyond FY1 (forces deferred honestly).
- Predictions are argued before evidence; each distractor's feedback repairs a named misconception (constant v, slowing growth, growing increment, heavier faster).
- Variable control good: exp-1 varies t only, exp-2 mB only, exp-3 mB with air; locked parameters stated.
- Exp-1/2 only reproduce built-in v = gt and mass independence; the conclusion model says so openly and exp-3 (air, drag emerging) carries the physics. Real-measurement evidence for the "Kokeellisesti" goal is only the strobe photo and the simulated data set. [Major, see Scores]
- Worked example: seven stages, one step each, unit conversion reasoned, sensible check from graph; does not repeat inquiry tasks.
- Checks: concept/graph, concept (g), calculation with km/h conversion, explain with observable criteria matching the prompt; hints progressive, mistakes real.
- Exit ticket tests the core idea (v = gt on another body, ratio of g).
- Finnish: case endings after number+unit correct; glossary terms used; reading level fine.
- Workload: core path about one lesson, extras optional. Captures not available ("none yet"); phone usability judged from the passed tests only.
- Exercises not judged (separate set).

## Scores
- 2 Conceptual clarity: 4, g as rate not speed treated well; Moon/no-air link missing (Minor).
- 3 Pedagogical effectiveness: 4, good sequence and gating; vacuum experiments confirm the model (Major, accepted because disclosed); no air prediction.
- 4 Exercise quality and variety (in-lesson tasks only): 4, varied, feedback repairs; noisy data task not noisy (Major, optional).
- 5 YO readiness: 3, graph slope and unit conversion present, but no real data or uncertainty handling in the required path.
- 6 Experimental reasoning: 3, variable control good; evidence is model output and the data set lacks scatter.
