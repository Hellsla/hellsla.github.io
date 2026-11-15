VERDICT: PASS
CONTENT-HASH: aeb5593ec10e643a
Mode: full, round 1

## Blocking
(none)

## Polish
- exercises/exercises.json fy8-7-L3-02 — `unit` "kpl" for a quantity asked per second; fy8-7-L1-07 uses "1/s" for the same kind of answer — use "1/s".
- exercises/solutions.md fy8-7-L2-05 — the step is headed "Kuvaajan lukeminen" though the data is a table; the content is right.
- exercises/exercises.json fy8-7-L3-01 — "vähintään" is strictly "more than half"; the solution says so ("Inversio vaatii hieman tätä enemmän"), the task could too.

## Checked
- All 15 numeric answers recomputed with own formulas from the task text (h, c, e as given): 1,959 eV; 0,800 eV; 692,7 nm; 1,607e16; 1,493 mW; 1,339e16 1/s; 75,94 %; 1,605; 527,7 nm; 5,04 MW; 0,5417 eV; 1,298; 1,806 J; 2,034e18 1/s; 92 246; 82,22 %; 0,524. All agree with exercises.json and answers.py.
- L3-05: own least-squares fit of the five points with P_p ≥ 30 mW gives slope 0,398, intercept −9,86 mW, threshold 24,8 mW; photons per extra pump photon 0,398 · 1064/808 = 0,524, below 1 and below the limit slope 808/1064 = 0,76.
- L3-04: N_p 9,826e19 1/s, N_L 8,080e19 1/s, heat 5,0 W of which the photon-energy difference 1,44 W; 0,8222 · 976/1070 = 0,750 matches the energy efficiency.
- L2-05 and L2-06 tables: 2,551 / 2,344 / 2,164 / 2,063 / 2,010 eV; rates 2,039 / 1,571 / 1,636 / 1,973 e16 1/s, order A, D, C, B.
- Rounded model answers accepted by the page: L1-07 (1,3e16 against the stored 1,34e16) passes through the half-step rule (data-step 1e15 in the built page); every other rounded answer is within 2 % or its own tolerance.
- Choice tasks L1-06, L1-08, L2-07: exactly one correct option, each distractor wrong, feedback names the right mechanism (incoming photon neither absorbed nor split; energy from the excited atom).
- L1-09: statements 2 and 5 true, 1, 3, 4 false; statement 3 limited to the two-level model as in the lesson.
- L3-01 assumptions (laser transition ends in the ground state, no decay during pumping) stated in the task and used in the solution; L3-05 d correctly separates inversion from the gain-equals-losses threshold in a four-level medium.
- Scope: photon energy, P = (N/t)hf, quantum dots qualitative with the size calculations marked Lisätietotehtävä; no de Broglie or Schrödinger.
- Notation as in the brief (E_2 − E_1, N/t, hf, λ); solutions symbolic first, rounding by the limiting datum.
