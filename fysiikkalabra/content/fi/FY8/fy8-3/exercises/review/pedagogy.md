VERDICT: PASS
CONTENT-HASH: 32070231e8079b94

## Blocking

## Polish
- exercises.json:82 fy8-3-L1-08 — answer 2,55 eV equals L1-03 and the solution itself notes the same Balmer line — fix: use another pair (e.g. 3 to 5, 0,97 eV) so it is not the inverse of L1-03.
- exercises.json:74 fy8-3-L1-07 — 122 nm is still readable from the lesson's series table — fix: ask for the Lyman limit or the Paschen longest wavelength.
- exercises.json:242 fy8-3-L3-04 — the lesson table lists Paschen as 821-1876 nm, so end level n = 3 is guessable — fix: ask the student to name which argument excludes each m.

## Checked
- Delta (41862d574): answers.py now fits with hand-written _polyfit1; L2-05 gives slope -3,289e15 Hz, E_ion 13,6025 eV (same as the numpy value, answer 13,6 eV, tolerance 0,03). No numpy import remains in the path.
- check_solutions.py fy8-3 ok; answers_shown.py: all 4374 shown answers agree. All 19 numeric json answers within their 2 % tolerance of the code values (L1-07 121,57, L1-08 2,55, L2-06 3, L2-07 13,056, L3-04 365,3, L3-05 97,25).
- Nothing else in the set changed since the PASS; counts 8/7/5 unchanged.
