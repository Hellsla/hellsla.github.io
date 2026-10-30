VERDICT: PASS
CONTENT-HASH: 0dc06ac7bbe7c1fa

## Blocking

## Polish
- exercises.json L1-03 (carried over) — a cyclist braking from 20,0 m/s (72 km/h) is not a realistic speed. — Use, for example, 8,00 m/s, or make the vehicle a car.
- solutions.md L2-04 Järkevyys (carried over) — "Todellinen nopeus voi olla suurempi, jos auto törmäsi johonkin" contradicts the task's given "Auto pysähtyi jäljen päähän". — Give a different caveat: the deceleration is an estimate, or braking may have started before the marks.

## Checked
- Rename: L1-04, L2-03 and L3-02 (Kysytty, Kaava, Sijoitus) and the answers.py docstring and comments now write $F_\text{ka}$. No $F_\text{k}$ is left, and the symbol matches fy4-9 and the lesson.
- I recomputed all 12 answers in one script with my own formulas: 24,0 m; 39,06 m; 4,00 s; 8750 N; 1,20 s; 79,17 m; 131,1 m ($a=\mu g$); 10 417 N; 81,46 km/h; 36,72 km/h; 11 253 N; 35,94 m. Every one agrees with exercises.json and answers.py.
- L3-03: a time-stepped simulation of both cars confirms that a gap of 35,94 m gives a minimum separation of 0. The end-position difference is therefore the right model, as the solution argues.
- L3-02: Δt = 2s/v₀ comes from constant deceleration, and that condition is stated in the task.
- Every solution is symbolic first, the conversions are right, the significant figures follow the limiting datum, and the reasonableness checks are real comparisons.
