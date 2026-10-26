VERDICT: PASS
CONTENT-HASH: 1d83eaa86fe1d6a7

## Blocking
(none)

## Polish
- inquiry.json:346 (check-3) — the prompt gives no water mass or temperature, but the model answer and criterion 4 use 0,20 kg, 20 °C (67 kJ vs 452 kJ, "noin 13 %") — state "0,20 kg 20-asteista vettä" in the prompt.
- inquiry.json pred-1 vs kayra — pred-1 has "jääpussi ja juomia", while the kayra curve is computed for 1,0 kg ice/water only (τ = c·1,0 kg/UA); plateau unaffected, after-melt rise would be slower with drinks — drop "ja juomia" from pred-1 or say the curve has no drinks.
- lesson.md Ydinajatus and Tiivistelmä — "yhtä paljon kuin … 80 kelvinillä": 334/4,19 = 79,7 K — "lähes yhtä paljon" or "noin 80 kelvinillä".

## Checked
- One Python run recomputed all 12 exercises and 6 inquiry numerics; answers.py matches (4,48 / 452 / 26,88 / 250,5 / 14,0 / 1,617 / 648,8 / 0,857 / 91,1 / 25,95 / 8,06 / 1,511; 333, 85,7, 64,9, 8,38, 56,5, 213) and every stated answer is within its tolerance.
- Formulas: Pt = ΣQ, Q = cmΔT/sm/rm, P = UAΔT, t = sm/(UAΔT) with the 0 °C condition, P = c(m/t)ΔT derived from Q = cmΔT; all within FY3 and its prerequisites.
- Worked example: 41,9 kJ, 33,6 W, t = 8,69·10³ s ≈ 2,4 h, 2,8 h without drinks, 13 %, 19 K/h initial rise; symbolic first.
- Lesson cooler-bag graph: t₀ = 2,41 h at x = 257,9; post-melt curve matches 28(1 − e^(−Δt/τ)) with τ = 6285/1,2 s at sampled points; 28 °C line at y = 70,4.
- kayra graph: t₀ = 3,68 h at x = 282,7, curve matches τ = 4190/0,90 s; answer 333 kJ with 4 % tolerance covers reading 3,6–3,8 h; mistakes 92,5 and 5,55 right.
- Table P and t rows (10,8…32,4 W; 8,59…2,86 h) and Pt ≈ 334 kJ; pred-2 2,9 h correct, 2,2 h distractor feedback right.
- Bar figure 334 / 42 / 335 kJ to scale; sauna 67 vs 452 kJ; glycol c ≈ 3500 J/(kg·K) realistic.
- Etsi virhe: 10,7 °C average, 62,9 vs 267 kJ, 0,19 kg melted, 0,61 kg left; Kelvin-option feedback right.
- Solutions' sanity checks (×5,2 for water, 0,72 kg/s, 6,3 %, 87 %) and exit ticket (175,5 kJ, 335 kJ) correct.
- Hash identical at start and end.
