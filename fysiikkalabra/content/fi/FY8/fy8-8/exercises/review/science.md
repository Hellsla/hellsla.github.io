VERDICT: PASS
CONTENT-HASH: 36ac7c9b588458f9
## Blocking

## Polish
- exercises/exercises.json:211 and solutions.md:139 (fy8-8-L2-07) — "kanavanumero on verrannollinen fotonin energiaan" but the fit is E = kK + b with b ≈ 1,2 keV; proportional means b = 0. Write "riippuu lineaarisesti" (the answer is unaffected: a fit through the origin gives 916,2 keV).
- exercises/exercises.json fy8-8-L3-05 data — the cascade 351,2 + 468,9 + 681,3 = 1501,4 keV closes exactly, while 820,5 differs by 0,4 keV from 351,2 + 468,9 = 820,1. The solution covers it ("alle 0,5 keV"), but changing the 820,5 line to 820,1 (or 468,9/681,3 to 469,3/680,9) makes the level scheme close; the answer 1150,2 keV stays.
- exercises/exercises.json:87 (fy8-8-L1-08) — Ni-60* from Co-60 normally de-excites by two gammas in cascade (1173 and 1332 keV, cf. L2-01): "lähettämällä gammafotoneja" or "yhden tai useamman gammafotonin" avoids contradicting L2-01.
- exercises/exercises.json:77 (fy8-8-L1-07) — kind "concept" on a pure count; it is also close to L1-02/L1-05 (daughter numbers after one decay). Optional: ask for the decay equation as the plan says ("hajoamisyhtälö: alfa ja beeta").
- fy8-8-L3-04 — same method as L3-01 (n_α from ΔA, n_β from ΔZ), and its table repeats L2-02's Bi-214 → Po-214 → Pb-210; acceptable since a)/b)/d) add the table reading and reasoning the plan asks for.

## Checked
- All 20 answers recomputed independently; all agree with answers.py and the keys (L2-07 fit k = 0,5978 keV/kanava, b = 1,199 keV, 916,4 keV, residuals < 0,6 keV; L3-05 1150,2 keV → 1,078 pm).
- L2-05: each row's (Z, N) → (Z′, N′) matches the nuclide's main decay (Ra-226 α, Pb-210 β⁻, Na-22 β⁺, I-131 β⁻, Ba-137m γ, Sr-90 β⁻); 3 β⁻ correct.
- L2-06: student's equation fails charge (95 ≠ 96); correct Np-237 with Z = 93, N = 144.
- L3-04: transitions α, α, β⁻, β⁻, α; Pb-210 → Pb-206 needs 1 α + 2 β⁻ (real chain via Bi-210, Po-210); total 4 α, 4 β⁻; d) argument (Z → 78) right.
- L3-05: level scheme 351,2 / 820 / 1501,4 keV is the only one that explains all five lines; alternative ordering correctly rejected.
- L1-06: exactly one correct option; distractor feedback correct (β⁺ lowers Z, α −2/−4, γ none).
- Notation as in the brief (^A_Z X, ⁰₋₁e, ν̄, E_y − E_a); tolerances fit.
- New tasks follow docs/exercise-bank/FY8.md (nuclide-table and calibration data at level 2, error analysis, decay series and level scheme at level 3).
- Hash identical at start and end.
