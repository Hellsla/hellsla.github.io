VERDICT: FAIL
CONTENT-HASH: b8fd7d501f975b22

## Blocking
- exercises/solutions.md:33, 35, 37, 73, 75, 77, 103, 105, 107 (L1-04, L2-03, L3-02) and the answers.py docstring/comments: the mean force is written $F_\text{k}$, but the momentum chapter fy4-9 (lesson and solutions) writes it $F_\text{ka}$. The same quantity carries two symbols in consecutive chapters (A, internal consistency across chapters). Fix: write $F_\text{ka}$, matching fy4-9 and the corrected fy4-11 lesson.

## Polish
- exercises.json L1-03: a cyclist braking from 20,0 m/s (72 km/h) is an implausible speed. Use, for example, 8,00 m/s, or make the vehicle a car.
- solutions.md:89 (L2-04 Järkevyys): "Todellinen nopeus voi olla suurempi, jos auto törmäsi johonkin" contradicts the task's given "Auto pysähtyi jäljen päähän". A better caveat is that the deceleration of 8,0 m/s² is an estimate, or that braking began before the marks.

## Checked
- I recomputed all 12 answers in one script with my own formulas, and every one agrees with exercises.json and answers.py: 24,0 m; 39,06 m; 4,00 s; 8750 N; 1,20 s; 79,2 m; 131 m ($a=\mu g$); 10 417 N; 81,5 km/h; 36,7 km/h; 11 253 N; 35,9 m.
- L3-03: the leading car is slower than the following one throughout (relative speed 3t + 6 > 0), so the smallest gap occurs when the following car stops and the end-position difference is the right model. The solution states this reason.
- L3-02: Δt = 2s/v₀ comes from the constant-deceleration triangle, and the condition is stated in the task.
- Every solution is symbolic first, its conversions are right, its significant figures follow the limiting datum (L2-02 gives 1,3·10² m because of μ = 0,30), and its reasonableness checks are real comparisons (dry versus snow, weight multiples, 1,6 s time gap).
- The model's conditions (level road, constant deceleration, no air resistance, full grip) are stated in answers.py and in the solutions where they are used.
