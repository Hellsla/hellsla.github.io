VERDICT: PASS
CONTENT-HASH: 834a33482c603c4f

## Blocking

## Polish

## Checked
- Delta round 2: the diff since the passed version is empty (hash unchanged); a fresh scripted comparison again finds every number of exercises.json and solutions.md equal to the Finnish source.
- All numbers in exercises.json and solutions.md match the Finnish source exactly (scripted comparison).
- Recomputed independently: L1-01 4,783 MeV, L1-02 178,4 MeV, L1-03 348,7, L1-04 3,269 MeV, L1-05 939,57 MeV.
- L2-01 Δm = Pt/c² = 1,509 kg; L2-02 3,374·10^14 J/kg; L2-03 x = 2, 184,7 MeV; L2-04 4,106 %.
- L3-01 4,526 kg/vrk; L3-02 26,73 MeV, 8,944·10^37 1/s (oletus kaiken energian säteilemisestä annettu); L3-03 2,402·10^5 a.
- answers.py computes the right physics; values agree with exercises.json within tolerance.
- Split sentences keep the reasoning: ΣZ conserved → electrons cancel, mass number gives x, Pu-239 note in L3-01, all assumptions still stated in the task text.
- Symbolic solving first, conversions u → MeV → J → kg correct, rounding tied to the limiting datum.
- Reasonableness checks are real estimates and cross-checks (82 GJ/g, 2^10 ≈ 1000, 1,041^40 ≈ 4,99).
- Exercise brief (Kaava, Esimerkki, Yleinen virhekäsitys, Tiivistelmä) is consistent with the set: nothing outside it is needed.
