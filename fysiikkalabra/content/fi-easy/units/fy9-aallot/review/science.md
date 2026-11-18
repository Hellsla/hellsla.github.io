VERDICT: PASS
CONTENT-HASH: 705a4aa32fbad8ff
SCOPE: delta: fi-easy diff since 49ba8f9 (new tasks fy9-aallot-s7 two-speaker interference and s8 standing wave on a string in sovella/tasks.json and solutions.md, intro "kahdeksan"); fidelity of s7/s8 to fi; s1-s6 not re-judged.

## Blocking
(none)

## Polish
- s7 c model answer: "Täysin hiljainen se ei ole, koska kauempana oleva kaiutin kuuluu hieman heikommin". The task tells the student to ignore this intensity difference. The criterion's "lähes hiljainen" is fine; the sentence could say "in reality". The same text is in fi.

## Checked
- Recomputed in one script from the task text and the figure data (fy5-12 speaker_grid: 12 and 5 squares of 0,50 m; fy5-13 task_string: 1,20 m, four loops): s7 a s1 = 6,0 m, s2 = sqrt(6,0² + 2,5²) = 6,5 m, Δs = 0,50 m; b λ = 343,4/343 = 1,001 m; c Δs/λ = 0,50, so destructive interference; d f = 343,4/0,50 = 686,8 Hz (690 Hz is within 2 %). s8 a λ = 2·1,20/4 = 0,600 m; b v = 30 m/s; c f3 = 3·30/2,40 = 37,5 Hz (38 is within 2 %); d f1 = 12,5 Hz and f2 = 25 Hz, so 20 Hz is not an eigenfrequency. All keys are within tolerance.
- Physics: the sources are in phase and the conditions Δs = nλ and (n + 1/2)λ are correct. Δs does not depend on f. Both string ends are nodes, L = nλ/2 and fn = nv/(2L). The wave speed depends on the tension and the mass per length, so it stays constant at a new frequency. All of this is in FY5 scope.
- Significant figures follow the data. The square counts are exact, and 1,00 m is given with three figures as the frequency has.
- Rubrics: s7 4+2+3+3 and s8 3+3+4+3. The criteria match the parts and solutions. "Hyväksytään myös" covers the phase-difference wording, the frequency ratio and the λ = v/f route in s8 d.
- Fidelity to fi: ids, figures, points, criteria, answers, tolerances and every number in tasks and solutions are identical (compared with a script).
- Intro: eight tasks, matching the set.
- The hash was the same at start and end.
