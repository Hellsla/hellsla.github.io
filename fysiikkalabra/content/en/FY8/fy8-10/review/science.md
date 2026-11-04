VERDICT: PASS
CONTENT-HASH: f9c2ece7d465ab45

## Blocking

## Polish
- assets/sims/fy8/fy8-10/sim.js:34 — `fmt` always writes a decimal comma, so the English sim shows "4,002603 u", "28,30 MeV" while the lesson text writes 4.002603 u; "28,30" can be read as a thousands separator — format by page language (decimal point in en).
- inquiry.json:354 — "The peak of the graph is exactly at the mass number 60" — the peak is at A ≈ 56–62; "near A = 60" is exact enough.
- exercises/review/packet-science.md (tooling) — the exercise brief is empty for en (the packet looks for Finnish section names); the exercise review here used the lesson text from this packet.

## Checked
- Translation faithful to the Finnish physics: definitions of u, mass defect, binding energy, Q, electron cancellation and its beta-minus remark, misconception section.
- Key idea and Formula numbers recomputed: 4.032980 u, Δm 0.030377 u (0.76 %), 931.49 MeV per u (931.9 with four-figure constants), 9.0·10¹³ J per gram, U-238 mass defect 0.81 %.
- Worked example: 28.296 MeV, 7.074 MeV per nucleon; rounding reason and estimate right.
- U-238 alpha decay: 0.004583 u, Q = 4.27 MeV; reaktio bar chart scale and 238.046204 u right.
- massat bar chart: broken axis starts at 3.990 u, bar heights to scale.
- Model values in predictions, conclusion and sim (H-2 1.112 … Ni-62 8.795, Fe-56 8.790, Ag-107 8.554, Pb-208 7.868, U-238 7.570; Fe 492.3, U 1801.7 MeV) recomputed from AME2020 masses.
- Find the error: 92.16 MeV; wrong result 8.3·10¹⁸; each distractor's feedback right.
- Transfer Po-210: 0.005806 u, Q = 5.408 MeV, alpha share 5.31 MeV ≈ measured 5.30 MeV; mistakes 3734, −5.408, 0.005806 right.
- Checks: deuterium binding energy options; curve reading (A 240 → 2×120 releases ≈ 200 MeV; others need energy); burning carbon 4.4·10⁻¹² kg ≈ 10⁻¹⁰, U-238 alpha 1.9·10⁻⁵, fission ≈ 9·10⁻⁴.
- Exit ticket Bi-209 7.85 vs Ca-40 8.55 MeV per nucleon; experiments vary only the nuclide, simState gives dm, EB, EBA.
