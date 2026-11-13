VERDICT: PASS
CONTENT-HASH: 70d00e3dd2da41b6
SCOPE: delta added-exercise from a52283bbb84cf337 base 611fb7d5c174
Mode: delta
Round: 2

## Blocking

## Polish
- solutions.md fy2-6-L2-08 Järkevyys: the estimate of 6,9 GW rated power and about 1400 turbines is the right order of magnitude. If you like, add the real comparison: Finland had about 8 GW and roughly 1 900 turbines at the end of 2024, and the fleet grew during the year, so the mean share was below one third. This is C.

## Checked
- Hash 70d00e3dd2da41b6 at the start and the end. I judged only the added L1-10 and L2-08.
- L1-10 (my round-1 blocking B is fixed): the text now says that burning releases energy at 2,0 MW. The Periaate uses that rate in E = Pt, so the case η = 100 % is no longer hidden.
- L1-10 recomputed: E = 2,0 MJ/s · 3600 s = 7200 MJ and m = Pt/H = 7200 MJ : 10 MJ/kg = 720 kg. This matches answers.py and exercises.json (kg, 0,04).
- L1-10 solution: m = Pt/H is solved in symbols first, MW → MJ/s is right, and the check 12 kg/min is right. The MAFY hint is in `hints`.
- L2-08 recomputed: 20,2 TWh = 20 200 GWh, and P = E/t = 20 200 : 8784 h = 2,30 GW. This matches answers.py and exercises.json (2,3 GW, 0,02). The 2024 leap year is stated in the task.
- L2-08 (my round-1 blocking A is fixed): the wrong claim "satoja voimaloita" is gone. The new check follows the chapter's model: 3 · 2,30 GW ≈ 6,9 GW rated, and 6,9 GW : 5 MW ≈ 1400 turbines ("tuhansia"). That is consistent and the right order of magnitude.
- L2-08: the back-substitution 2,30 GW · 8784 h ≈ 20 200 GWh is a real check. The three significant figures follow the 20,2 read from the bar.
