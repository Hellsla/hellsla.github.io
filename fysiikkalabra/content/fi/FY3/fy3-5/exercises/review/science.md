VERDICT: PASS
CONTENT-HASH: eb87ee7962362258
SCOPE: delta added-exercise from 23beb0210afaa772 base 89bcb63b7431

## Blocking

## Polish
- exercises/exercises.json (fy3-5-L2-08) — uses the same figure `fy3-5/piston-force` as L2-01, whose first step is exactly this work (60 J); physically right, but L2-08 repeats half of L2-01. Optional: place it before L2-01 as its lead-in, or use different end points.
- exercises/solutions.md (fy3-5-L1-10, Vastaus) — $8{,}37 + 3{,}0 = 11{,}4\,\text{kJ}$; by the addition rule one decimal would be kept, and 11 kJ lies 3,3 % from the stored 11,37 (inside tolerance 0,04, so not blocking). Optional: answer $11\,\text{kJ}$ with "kahden merkitsevän numeron tarkkuudella" or $11{,}4\,\text{kJ}$.

## Checked
- MAFY value verified on mafytaulukot.fi (*Yksikkömuunnoksia*): $1\,\text{cal} = 4{,}1868\,\text{J}$, as the solution uses.
- L1-10 recomputed: $Q = 2000 \cdot 4{,}1868\,\text{J} = 8{,}374\,\text{kJ}$, $\Delta U = Q + W = 11{,}37\,\text{kJ}$; answers.py agrees; with 4,184 J/cal 11,37 kJ too.
- L1-10 signs: heat into the system and work done on it, both positive, as the brief's convention; conversion kcal → cal → J shown; check (1 kcal ≈ 4,2 kJ) real.
- L2-08 recomputed from the figure code: line (0; 200 N) → (0,20 m; 400 N), on grid crossings (0,05 m, 50 N); trapezoid area $W = 60\,\text{J}$; $Q = 0$ stated in the task ("niin nopeasti, ettei lämpöä ehdi siirtyä"), so $\Delta U = W = 60\,\text{J}$; answers.py agrees.
- L2-08 sign: piston (surroundings) does work on the air, $W > 0$; solution states why; symbolic $W = \frac{F_1+F_2}{2}s$ before numbers.
- Figure description gives end points only, no area or work.
- Both within FY3 (first law, work as (s,F) area); no second law or $pV$ work needed.
- Rest of the set unchanged since PASS; hash same at start and end.
