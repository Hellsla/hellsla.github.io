VERDICT: PASS
CONTENT-HASH: 9785d98178775482

## Blocking

## Polish
- exercises/review/packet-science.md:56–63 — the exercise brief is empty: the packet script looks for the Finnish section names (Kaava, Esimerkki, …), which the English lesson.md headings do not carry — fix the extractor or add the `{Kaava}`-style anchors; I judged the set against the lesson as given in the lesson packet.

## Checked
- All numbers in exercises.json and solutions.md match the Finnish source exactly (scripted comparison).
- Recomputed independently: L1-01 4.783 MeV, L1-02 178.4 MeV, L1-03 348.7, L1-04 3.269 MeV, L1-05 939.57 MeV.
- L2-01 Δm = Pt/c² = 1.509 kg; L2-02 3.374·10^14 J/kg; L2-03 x = 2, 184.7 MeV; L2-04 5^(1/40) − 1 = 4.106 %.
- L3-01 4.526 kg/day; L3-02 Q = 26.73 MeV, 8.944·10^37 1/s (assumption that all energy is radiated is stated); L3-03 24 100 · log2 1000 = 2.402·10^5 a.
- answers.py uses the right physics for each task; values agree with exercises.json within tolerance.
- Electron cancellation justified by conserved ΣZ in every atomic-mass task; mass and charge numbers balanced.
- Each solution solves symbolically first; conversions (u → MeV, MeV → J, u → kg) correct; rounding reasons tied to the limiting datum.
- Reasonableness checks are real (rounded estimates, cross-check against 82 GJ/g, 2^10 ≈ 1000).
- Translation keeps the physical statements: averages for random neutron fates, Pu-239 share noted in L3-01, Sun's mass-loss 4·10^9 kg/s.
