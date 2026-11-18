VERDICT: FAIL
CONTENT-HASH: e9bf2efc3c9791b6
SCOPE: delta: new tasks s8 (car on a bend) and s9 (sign on a rod), their solutions, answers.py and the changed intro sentence (en); s1-s7 not re-judged.

## Blocking
- s9 b, `sovella/tasks.json` en, criterion "calculation": the text is Finnish ("poispäin seinästä ja ylöspäin" after $H \approx 331\,\text{N}$ ... $V \approx 14.7\,\text{N}$). It must read "away from the wall" and "upwards". Student-visible in the rubric.
- s8 (en), task text and solutions say "normal acceleration", but the alt text of fy5-4/kuvaaja-a and the rest of the unit use "centripetal acceleration" (the graph's own words); the names in task and alt text must be equal. Use "centripetal acceleration" in the s8 text, part a and the solutions (keep the symbol $a_\text{n}$).

## Polish
- s8 a uses the same figure and the same point (15 m/s, 3,0 m/s²; r = 75 m) as chapter exercise fy5-4-L2-09; a student who did that exercise recognises the answer. Consider another marked point (for example 20 m/s, 5,3) in a later round; not blocking.
- s8 a, Järkevyys: the second point (20 m/s, a_n about 5,3 m/s²) cannot be read to 0,1 from a graph whose gridlines are one unit apart; "noin 5,3" is a computed value. Say "noin 5 m/s², hieman yli viiden" or mark it as a check by calculation.
- s9 d: the task's closing "selitä, miksi muutos on tämän suuntainen" is fine, but the model answer could name the sign-reading explicitly (steeper wire, larger lever arm of its vertical part) next to the conclusion; optional.

## Checked
- Numbers recomputed: s8 r = 15²/3,0 = 75 m; F = 1200 kg · 3,0 m/s² = 3,6 kN; v_max = sqrt(0,50 · 9,81 · 75) = 19,18 m/s = 69 km/h; with 1500 kg: 4500 N needed against 7360 N available (61 %, unchanged). s9 T = 19,5 kg · 9,81 / 0,500 = 382,6 N; H = 331,3 N, V = 14,7 N, F = 331,7 N at 2,5 degrees; m_max = 29,08 kg; at 45 degrees T = 270,5 N (29 % less), H = 191 N. All agree with answers.py and the solution text; the end-of-rod moment check for V is correct.
- Rounding to the data's precision: two significant figures in every final answer, intermediate 3-4 figures marked as such; the "at most" case (s9 c, 29,08 kg) is rounded down to 29 kg, which is the safe side.
- Task texts do not reveal structure: s8 does not say "use the friction limit" or "mass cancels"; s9 d asks "how does it change" and "why in this direction" without giving the vertical-component idea. Parts rise in demand (read graph, FBD and N2, limit case with units conversion, justified word part); points 4/3/5/3 and 6/5/3/3 match the criteria counts.
- Criteria: shared keys used, each concept/math criterion states the justification, not only the number; the "centrifugal force is not drawn" and "hinge force at the hinge, direction away from the wall" points are covered. Common-mistake lists address real errors (inverted ratio, centrifugal force, lever arm without angle, steeper wire increasing force).
- Intro: "Yhdeksän / Nine / yhdeksän" now matches nine tasks; the sentence about task 7 is unchanged and still correct.
- Alt text names equal the task's names for s9 (kyltti, tanko, vaijeri, sarana) for s9; for s8 see Blocking (term mismatch).
- Solutions: calculation chains are aligned rows (`aligned` blocks), symbols first, then substitution; the units conversion step is present or stated as not needed. Language-neutral parts (answers, figure ids, links, skills) identical across languages. The sovella captures at 390 px that I opened did not contain s8/s9 and I did not judge 360 px layout here; check_layout/visual review covers it.
- Hash at start and at end identical.
