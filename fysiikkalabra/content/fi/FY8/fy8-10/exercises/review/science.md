VERDICT: FAIL
CONTENT-HASH: 0b105e1e4693fd79

## Blocking
- content/fi/FY8/fy8-10/exercises/solutions.md:8 (L1-01 Vastaus) — A: the rounding reason is wrong. "kuusi desimaalia eli neljä merkitsevää numeroa": 0,098940 has five significant figures (9, 8, 9, 4, 0), not four. — fix: give 0,098940 u ("kuusi desimaalia kuten annetuissa massoissa"), or keep 0,09894 u with a correct reason.

## Polish
- content/fi/FY8/fy8-10/exercises/solutions.md (L1-03 Vastaus) — "neljä merkitsevää numeroa; sidosenergiassa 1801,7 MeV on viisi" does not justify the rounding: five-figure data allow 7,5702. — fix: give 7,5702 MeV, or say that four figures match the 931,5 used to obtain 1801,7.
- lessons/FY8/fy8-10/answers.py (L2-03 comment) — the comment says 2,04477e-11 J, but the code computes 2,04479e-11 J, as the solution does. — fix the comment.
- The masses H-1, n, He-3, He-4, Fe-56, Ra-226, Rn-222, O-16 and C-12 agree with my AME2020 recollection to ≤ 0,5 µu. Ra-226 → Rn-222 Q = 4,871 MeV matches the literature value.

## Checked
- I recomputed all 12 answers in one script with my own formulas, and every one matches answers.py and exercises.json. Values: 0,09894 u; 127,6 MeV; 7,570 MeV; 8,99·10¹³ J; 2,388·10⁻³ u; 8,790 MeV; 4,871 MeV; 2,045·10⁻¹¹ J; 3,68·10¹⁴ kg; 20,58 MeV; 23,85 MeV; 2,80·10⁻¹² kg.
- The 931,5 MeV/c² substitution is used consistently and c² cancels correctly. The kg-and-J route in L2-03 agrees within rounding (127,7 vs 127,6 MeV).
- Atomic masses are valid: electrons balance in the alpha decays (88 = 86 + 2), in He-4 → He-3 + n, and in the H-atom defects.
- L3-01: He-3 E_B is 7,72 MeV, and 20,58 MeV is about 2,9 × 7,07, as stated. The sign handling (E = −Q) is right.
- L3-02: the binding-energy route agrees with the mass route (23,847 MeV).
- L2-04: E = Pt and Δm = E/c². The assumptions (constant power, solar wind ignored) are stated. 4,26·10⁹ kg/s is right.
- L3-03: Q = cmΔT with no change of state, as the solution states. ΔT 60,0 K.
- L1-04 check: 25 GWh, about 16 h for a 1600 MW unit, is right.
- Every solution solves the unknown symbolically before substituting. Tolerance 0,02 fits the data.
- Scope: everything is within "massan ja energian ekvivalenssi, ytimen sidosenergia".
