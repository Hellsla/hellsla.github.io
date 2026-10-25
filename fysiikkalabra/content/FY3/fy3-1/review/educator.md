VERDICT: PASS
CONTENT-HASH: 4531ded1008f3bd6

## Blocking

## Polish
- lesson.md:12 — the calibration bodies get "paino noin 1 N" without a mass, and line 17 then uses "two identical bodies stretch twice as much" as the reason G ∝ m, which a careful student may find circular — write "joiden massa on kunkin noin 100 g eli paino noin 1 N. Kukin kappale vetää jousta yhtä voimakkaasti, joten kaksi kappaletta vetää sitä kaksinkertaisella voimalla."
- lesson.md:10 — "FY1:n lineaarisessa mallissa silloin, kun vakiotermi on nolla" is abstract for a first-timer — name the familiar cases: "kuten FY1:n suoraan verrannollisissa malleissa $s = vt$ ja $m = \rho V$".
- lesson.md:14 — the hook asks "miksi" but the text only says the Moon's interaction is weaker — append "Kuun massa on paljon pienempi kuin Maan, joten se vetää astronauttia heikommin."
- exercises.json fy3-1-L1-02, fy3-1-L1-04 — "4,0 N:n paino", "12 N:n painolla" use "paino" for the hanging object and blur the mass/weight distinction the lesson teaches; the two tasks are also the same rule-of-three — write "ripustetaan kappale, jonka paino on 4,0 N" and turn L1-04 round: "Jousi venyy 2,0 cm 5,0 N:n voimalla. Kuinka suuri voima venyttää sitä 3,0 cm?" (7,5 N, update answers.py).
- exit-ticket.json q3 — repeats lesson.md:52 almost word for word (70 kg, 690 N), so it tests recall — use a transfer item, e.g. "Pullossa on 1,5 kg vettä. Mikä on veden paino Maassa, ja miksi ’pullo painaa 1,5 kiloa’ on epätarkka?" (noin 15 N).

## Checked
- Hash same at start and end; lint clean.
- Changes since the published hash (lesson.md:21, :52) are wording only.
- Each paragraph adds at most one idea; FY1 prerequisites (linear model, 9,81 m/s²) are named where used; N/kg vs m/s² deferred to FY4 in one plain sentence.
- Motivating question is one students ask; answered at lesson.md:14, :52.
- Scope: no Newton's laws or vectors (FY4).
- Levels: L1 five one-formula tasks, L2 four (rearrangement, g→kg, difference, two steps), L3 three (changed place, same force, Moon scale) match the rubric.
- No exercise repeats the worked example (120 kg robot, Earth/Mars) with new numbers.
- Answers recomputed: worked example 1180 N / 445 N, exit ticket 29 N, 4,9 N, 7,5 cm, 690 N all correct.
- Exit ticket q1 and q2 test the core ideas (mass constant, weight changes; spring proportionality).
- Length and structure match fy3-2.
