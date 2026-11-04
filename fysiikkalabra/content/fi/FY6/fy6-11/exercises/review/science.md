VERDICT: PASS
CONTENT-HASH: 171aa8bf96452262
Round 3: delta review of commit d6007a53c (solutions.md fy6-11-L2-07 Annettu).

## Blocking

## Polish
- docs/exercise-bank/FY6.md fy6-11 Taso 2 — the plan's graph task (droplet deflection, figure) became the error-analysis task L2-06, and no new task has a graph. Update the plan line (carried over).

## Checked
- Hash 171aa8bf96452262 at start and end. Diff d6007a53c^..d6007a53c in content/fi/FY6/fy6-11/exercises read in full: the only exercise change is solutions.md:163, force at x = 8,0 cm 52,1 → 58,0 µN.
- solutions.md:163 Annettu now lists 60,2; 59,8; 59,5; 59,0; 58,0; 33,0 µN, identical to exercises.json L2-07 table rows and to answers.py `fx`; no "52,1" left in the exercise set.
- Recomputed L2-07 from the task data: E = 3,01 / 2,99 / 2,98 / 2,95 / 2,90 / 1,65 · 10⁴ V/m; deviations 0,7 / 1,2 / 2,0 / 3,7 / 45,2 %; homogeneous x = 0–6,0 cm; mean 29 812,5 V/m = 2,98 · 10⁴ V/m, 0,6 % below U : d = 3,0 · 10⁴ V/m. Sijoitus, Vastaus, Järkevyys ("0,6 %" is right: 0,625 %) and answer field agree.
- Visual round-2 Blocking (Annettu contradicting task table and Sijoitus) resolved.
- answers.py run: all 18 answers unchanged and equal to exercises.json.
- Physics, scope, levels and notation unchanged from round 2 (PASS); nothing else touched.
