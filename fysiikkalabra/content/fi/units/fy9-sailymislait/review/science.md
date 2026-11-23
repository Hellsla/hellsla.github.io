VERDICT: FAIL
CONTENT-HASH: ac36248617b265a1
SCOPE: full (fi): the three new pysahdy boxes first, then unit.md, inquiry.json, teacher.md and the Sovella set (tasks, solutions, answers.py, figures.py).

## Blocking
- **A, causality and consistency (pysahdy 2, under the energy principle):** "Kitkan työ on negatiivinen, $W < 0$, koska kitka vähentää mekaanista energiaa ..." gives the consequence as the cause. In the energy principle the mechanical energy decreases *because* $W < 0$, so the answer argues in a circle. The real reason is in the paragraph just above it ($W = F_\parallel s$): friction points against the motion, so $F_\parallel < 0$. s7 b gives that reason too ("koska kitka on liikettä vastaan"). Fix: "Kitkan työ on negatiivinen, $W < 0$, koska kitkavoima on liikkeen suuntaa vastaan. Siksi se pienentää mekaanista energiaa, joka muuttuu sisäenergiaksi."
- **A, internal consistency (teacher.md "Arviointi" and the 65–75 min row):** these say "muut viisi Osa II:n tyyppisiä (15 pistettä kukin), yhteensä 95 pistettä" and "muut viisi tehtävää". The set has eight tasks: s3 is 20 points, s1, s2 and s4–s7 are 15 points each, and s8 is 14 points, so the total is 124 (`practice.py check`: 8 tasks, 124 points). Fix the counts and the total.

## Polish
- Pysahdy 3: "koska ulkoisten voimien impulssi on merkityksettömän pieni" is a condition the question does not give. Adding "lyhyen törmäyksen aikana" would match the Ydinajatus. A level-C simplification, not an error.
- s7 d conclusion: "Raskaampi kelkka kuluttaa liike-energiaa enemmän". Kitkan työ muuttaa mekaanista energiaa sisäenergiaksi; "menettää kitkaan enemmän energiaa" (as in the solution) is more exact.
- Recorded earlier and still open: s8 b "47 km/h" against the unrounded value of about 45 km/h; s7 d's closing remark on air resistance.

## Checked
- Pysahdy 1 and 3: their physics is right, and they agree with the theory and the Virheet list (energy becomes internal energy, total energy is conserved, momentum is conserved only under the stated condition).
- I recomputed every number in one script: the hook (51 200 kg·m/s, 41 → 20 kJ), aineisto (41,66 %, mistakes 58,34/1,39/65,0, spring buffer 2 %, rubber buffer 25 %), märkä tie (53/84 m), pyöräily (13,48; 20,99; 26,45), pienvesivoimala (3,302; 3,752; 4,264; 0,3366), turvavyö (6,481 kN, 9,4 G), taklaus (1,182; 2446 → 119 J), tarkistus-2 (53,56 %), the teacher's icy-road figure (≈ 270 m), and s1–s8 including the least-squares fit for s3 (k 0,0799, t_r 0,864 s, a 6,26 m/s², line points 1,66 and 2,86). All agree; `practice.py check` OK.
- Every choice item has exactly one correct option, and each distractor's feedback is right.
- Rubric points add up per part. The replaced hero and wind-turbine images (webp) match their aria-labels and labels and add no numbers.
- Hash ac36248617b265a1 at start and end.
