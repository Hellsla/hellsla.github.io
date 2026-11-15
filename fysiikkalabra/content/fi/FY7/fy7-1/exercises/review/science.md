VERDICT: PASS
CONTENT-HASH: 9a398310c855a2de

## Blocking

## Polish
- solutions.md L2-04 Järkevyys: "kuten magneetin kenttä luvun simulaatiossakin" refers to the lesson's simulation. The check would stand without it: compare with the on-axis 1/r³ value 2³ = 8.

## Checked
- Round 3 diff (`git diff HEAD~1`): it changes only two texts of fy7-1-L3-02, the answer in exercises.json and the Mallivastaus in solutions.md. Both now say "teräksessä moni niistä / moni alkeisalue jää järjestykseen", which matches the Periaate ("säilyy osittain"). The physics is right: remanent magnetisation after the field is removed is only partial. No number, answer, answers.py line, figure or data changed.
- fy7-1-L1-09 statement 4 (round 2) names the bar-magnet model, so "Tosi" is unambiguous. That matches L1-07 and the lesson.
- All 17 numeric answers were recomputed in round 1 with my own formulas (tan θ = B_m : B_h, B_h = B cos I, B_v = B sin I, Pythagorean sums, the r₀ from the mean of B_m r³). They agree with exercises.json and answers.py. Unchanged since.
- Every tolerance accepts the rounded answer given in the solution (L1-02 2,1 % vs 3 %, L2-05 3,4 % vs 4 %, L3-05 1,2 % vs 5 %).
- L2-05 and L3-05 data: B_m r³ is nearly constant in both tables, so the falloff is consistent with 1/r³. r₀ = 16,2 cm. Field directions on the axis and in the equatorial position (L1-05, L3-01, L3-05) are correct.
- L1-06 and L1-07: exactly one correct option, and every distractor's feedback is right physics.
- Figures sum-grid and incl-grid: to scale, they match how the solutions read the grid, and neither gives the answer away.
- Angle notation `^\circ` is the same everywhere, and every angle answer has the unit "°". Everything is in FY7 scope and uses the lesson's notation.
