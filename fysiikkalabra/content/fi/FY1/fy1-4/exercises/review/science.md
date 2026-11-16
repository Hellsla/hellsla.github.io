VERDICT: FAIL
CONTENT-HASH: b71b8808af4ef0fd
SCOPE: delta added-exercise fy1-4-L2-09 (work queue 19), round 1

## Blocking
- content/fi/FY1/fy1-4/exercises/solutions.md:237 — This is an A error (quantitative). The model value at 16 h is wrong: T(16) = 7,2 °C + 1,517 °C/h · 10 h = 22,37 °C, which rounds to 22,4 °C. The same result comes from k = 1,52 °C/h. The solution says 22,3 °C. — Write "Klo 16 se antaa 22,4 °C".

## Polish
- content/fi/FY1/fy1-4/exercises/exercises.json:343 — The task asks for data "tunnin välein", but the fallback table and the solution's "Annettu" use 2 h steps. This is fine for a student's own download. Optionally say "tunnin tai kahden tunnin välein" so the two agree.

## Checked
- This review covers fy1-4-L2-09 only (a new exercise, judged in full). The hash was b71b8808af4ef0fd at the start and at the end.
- I recomputed the answer: k = (16,3 − 7,2) °C / (12 − 6) h = 1,5167 °C/h. answers.py gives 1.516667, which matches the key 1.517. The tolerance of 0,03 accepts 1,5 (1,1 % off).
- I recomputed the model points:
  - T(8) = 10,23 °C, measured 10,4 °C.
  - T(10) = 13,27 °C, measured 13,5 °C.
  - Inside the interval the difference is at most 0,2 °C.
  - T(0) = −1,9 °C.
  - The 2 h steps are 3,2, 3,1 and 2,8 °C, and the minimum and maximum are at 4 h and 16 h. All of this is correct.
- Two significant figures is right: ΔT = 9,1 °C has two, and the 6 h span set by the task is exact (teacher 2026-11-16 rule).
- The note °C/h = K/h is correct. The solution states the linear model with its range of validity, and it says the model fails outside that range. This is how the guardrails treat extrapolation.
- d) gives the mechanism: the Sun heats the ground and the air, the heating weakens in the afternoon and the air cools at night. Next-day weather also depends on cloud, wind and air masses. This is a fair simplification (C).
- The fallback table is labelled as invented example data, so no data is presented as measured. A diurnal range of about 12 °C fits a clear May day inland. The FMI link resolves to "Havaintojen lataus".
- The scope (graphical and linear model, rate of change) is FY1, and the notation is the brief's.
