VERDICT: PASS
CONTENT-HASH: abd49d96b1b5b3bc
Mode: delta

## Blocking
(none)

## Polish
- None new. (Same optional items as the Finnish report on L1-07, L1-08, L3-04 apply to the shared task design.)

## Checked
- Delta (41862d574): answers.py now fits with hand-written _polyfit1; L2-05 gives slope -3,289e15 Hz, E_ion 13,6025 eV (same as the numpy value, answer 13,6 eV, tolerance 0,03). No numpy import remains in the path.
- check_solutions.py fy8-3 ok; answers_shown.py: all 4374 shown answers agree. All 19 numeric json answers within their 2 % tolerance of the code values (L1-07 121,57, L1-08 2,55, L2-06 3, L2-07 13,056, L3-04 365,3, L3-05 97,25).
- Nothing else in the set changed since the PASS; counts 8/7/5 unchanged.
