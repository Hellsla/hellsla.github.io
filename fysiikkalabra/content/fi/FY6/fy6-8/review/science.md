VERDICT: PASS
CONTENT-HASH: 9289839a457f0dc1

## Blocking

## Polish
- lesson.md:410 — "Ryhmän lähdejännite on siis kahden pariston lähdejännitteen verran pienempi" holds as written only for identical cells (the drop is twice the reversed cell's own E, it is subtracted instead of added). The flashlight context implies identical cells, so C/minor — optionally "kaksi kertaa väärin päin olevan pariston lähdejännitteen verran" or "samanlaisilla paristoilla".
- lesson-answers.py:1085 — the comment uses $0{,}010\,\Omega$ for the car battery (1260 A) while siirto uses $0{,}012\,\Omega$ (1050 A); both fit "sadasosaohmien luokkaa" and "yli tuhat ampeeria", no text change needed.

## Checked
- Reversed-battery fix (lesson.md:410): sign right (E subtracted, R_s still added in series); for identical cells the group drops by 2E from the all-correct case — correct.
- One recomputation script with my own formulas: koe-1 rows (1,333/1,333; 0,7273/1,4545; 0,3810/1,5238; 0,1951/1,5610), R_s = 0,2006 Ω from rounded rows, E = 1,60 V, mistakes 1,0 and 1,2 Ω; koe-2 1,333 / 2,286 / 1,455 V; koe-3 used-cell values.
- Worked example: I = 0,3625 A, R_s = 0,3586 Ω → 0,36 Ω, I_k = 4,406 A → 4,4 A; symbolic first, rounding from the 0,13 V difference justified, back-substitution a real check.
- Etsi virhe 0,667 A / 8,0 V / 1,0 V drop; siirto 10,44 V, (U/E)² = 0,687, I_k = 1050 A, 180 A < 1/5 of it; exit ticket 5,0 A; kertaus 6,0 V; every distractor wrong and its feedback right.
- tarkistus-2: least-squares fit of the five CHECK_PTS gives exactly −2,00 V/A and 9,00 V, the drawn line (0; 9,0)–(1,5; 6,0) ends on a grid crossing; answer 2,0 Ω, mistakes 4,0 and 6,0 Ω correct.
- ui-graph to scale: E 1,50 V at y≈103, I_k 5,0 A at x=432,5, triangle 1→3 A, 1,2→0,6 V, R_s 0,30 Ω.
- Model figure: current arrows + → load → − outside and − → + inside; the potential figure rises E, falls R_sI, U at +, falls U in R.
- Series/parallel formulas, connections figure (2E, 2R_s; E, R_s/2), parallel only for identical equally charged cells stated.
- sim.js implements I = E/(R+R_s), U = E − R_sI, group(): 2E/2R_s, E/R_s/2; Pcell uses I/2 in parallel; simState gives I and U; experiments lock paristo/kennot/kytkin (koe-2 locks R = 1,0 Ω), so each isolates its varied parameter; model box states the limits and calls numbers model values.
- Physics: energy per charge, internal energy in R_s, open-circuit E with an ideal voltmeter, used cell with near-unchanged E and larger R_s, cold battery, short-circuit hazard and extrapolation caveat — all sound and consistent with summary, glossary and exit ticket.
