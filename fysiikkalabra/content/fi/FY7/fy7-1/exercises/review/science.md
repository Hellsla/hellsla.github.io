VERDICT: PASS
CONTENT-HASH: fd1880c1a9c4044c

## Blocking

## Polish
- exercises.json:318 (fy7-1-L3-02 answer) and solutions.md:94 (Mallivastaus) still say "kovassa teräksessä ... jäävät järjestykseen". Only the Periaate line was changed to "säilyy osittain myös kentän poistuttua". Fix: use the same wording in the answer and in the Mallivastaus.
- solutions.md L2-04 Järkevyys: "kuten magneetin kenttä luvun simulaatiossakin" refers to the lesson's simulation. The check would stand without it: compare with the on-axis 1/r³ value 2³ = 8.

## Checked
- Round 2 diff since round 1, i.e. hash 87bf9eac2d0b59a7 (`git diff HEAD~3`): it changes only statement 4 of fy7-1-L1-09 with its feedback, and the Periaate of fy7-1-L3-02. No number, answer, answers.py line, figure or data table changed.
- fy7-1-L1-09 statement 4 now names the bar-magnet model ("Maan sauvamagneettimallin etelänapaa"). That matches L1-07 and the lesson's misconception and summary. "Tosi" is now unambiguous, and its feedback is correct.
- fy7-1-L3-02 Periaate: partial retention of domain alignment after the field is removed is correct for the steel of a paper clip.
- All 17 numeric answers were recomputed in round 1 with my own formulas (tan θ = B_m : B_h, B_h = B cos I, B_v = B sin I, Pythagorean sums, the r₀ from the mean of B_m r³). They agree with exercises.json and answers.py. Unchanged since.
- Every tolerance accepts the rounded answer given in the solution (L1-02 2,1 % vs tol 3 %, L2-05 3,4 % vs 4 %, L3-05 1,2 % vs 5 %).
- L2-05 and L3-05 data: B_m r³ is nearly constant in both tables, so the falloff is consistent with 1/r³. r₀ = 16,2 cm. Field directions on the axis and in the equatorial position (L1-05, L3-01, L3-05) are correct.
- L1-06 and L1-07: exactly one correct option, and every distractor's feedback is right physics.
- Figures sum-grid and incl-grid: to scale, they match how the solutions read the grid, and neither gives the answer away.
- Angle notation `^\circ` is the same everywhere, and every angle answer has the unit "°". Everything is in FY7 scope and uses the lesson's notation.
