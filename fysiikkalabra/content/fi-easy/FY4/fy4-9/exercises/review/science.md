VERDICT: PASS
CONTENT-HASH: fbbb9b9401d75abc
SCOPE: delta added-exercise from ce753f67cda910eb base abdc9e095e4f

## Blocking

## Polish
- exercises.json fy4-9-L2-09 — "noin $5\,\text{min}$": the source record says only that these videos are 3–5 minutes long — "muutaman minuutin" would not depend on the exact length.
- solutions.md fy4-9-L2-09 (Periaate, a) — "painovoima": the course's term for the force is paino; the meaning is clear here (gravity keeps the station in orbit).
- Earlier polish items (L2-07 rounding reason, L3-03 v_k clash) still open; not part of this change.

## Checked
- Hash the same at the start and the end (fbbb9b9401d75abc).
- Added task fy4-9-L2-09 only; the other 22 exercises are unchanged by the packet's check.
- Source (coordinator's record, read 16.11.2026): Andreas Mogensen (ESA), SLAMMD, a known force on the attached astronaut and mass from the resulting acceleration by Newton's second law: stated as recorded, with link and date in task and solution. The solution describes no scene of the video and tells the student to compare with what they saw.
- a: a scale reads the normal force; station and astronaut are in free fall with the same acceleration, so the reading is zero while the mass and the gravitational force remain. Correct.
- b: m = F/a and m = FΔt/Δv are the same law (a = Δv/Δt); the condition is stated (the push is the only significant force along the motion, body rigid and attached).
- c: example values named as examples, not measurements: 20,0 N · 0,50 s : 0,125 m/s = 80 kg (two figures from 0,50 s); second method from rest m1v1 = m2v2: 10,0 kg · 0,40 m/s : 0,050 m/s = 80 kg; unit N·s = kg·m/s. The solution says that many methods are right.
- d: Δv read 0,130 m/s (+4 %) gives 76,9 kg ≈ 77 kg (−4 %); random and systematic error kept apart; calibration with known masses.
- Every part is answerable with the source and the chapter (impulse principle, Newton II and III); nothing outside FY4.
- answers.py: the task's numbers recomputed (asserts pass); the answer is a string, no number in the gate.
