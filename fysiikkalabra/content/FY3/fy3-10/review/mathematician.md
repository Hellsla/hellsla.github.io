VERDICT: FAIL
CONTENT-HASH: 61f1d64048b5e6d4

## Blocking
1. lesson.md:49 — "paine kilopascaleina ja tilavuus litroina … tuhat- tai miljoonakertaisesti väärä" is false: kPa · l = J, so pV/(RT) with both is correct and no kPa/l mix gives 10⁶. It contradicts solutions.md:63 (L2-03), which keeps kPa and l. — Name a mismatched pair: "sijoittaa paine kilopascaleina mutta tilavuus kuutiometreinä tai paine pascaleina mutta tilavuus litroina. Silloin tulos on tuhatkertaisesti väärä."
2. solutions.md:61 (L2-03) — the first wrong step is "= 828,3 K"; 303,15 · 138/50,5 = 828,41 K, so θ₂ = 828,4 − 273,15 = 555,3 °C (not 555,1). The final 555 °C is right (answers.py 555,26). — Write "= 828,4 K. θ₂ = 828,4 − 273,15 = 555,3 °C ≈ 555 °C".

## Polish
1. exit-ticket.json:4 — 27 °C is written as 300 K; with 273,15, as everywhere else, it is 300,15 K, which gives 0,601 mol, not 0,602 mol.
2. solutions.md:90 (L3-03) — write "V = 200 l = 0,200 m³" like the other Annettu lines.
3. solutions.md:42–93 — θ is used but never named in lesson.md; name it once at lesson.md:36.
4. lesson.md:44 — "Pyöristämätön ainemäärä on 0,207 mol" is rounded; say "Tarkempi arvo".
5. solutions.md:31 — "324 − 273" uses 273; use 273,15 for consistency (the result is still ≈ 51 °C).

## Checked
- Lint is clean; the hash was the same at start and end; `check_layout.py fy3-10` reports OK at 360 px.
- Rearrangements n = pV/(RT), p = nRT/V, V = nRT/p, T = pV/(nR), M = m/n and T₂ = T₁p₂V₂/(p₁V₁) are correct; the combined law follows from pV/T = nR.
- Conversions l → m³, 200 bar → 2,00 · 10⁷ Pa, 4,60 MPa → 4600 kPa, 3,0 bar → 3,0 · 10⁵ Pa, m³ → l and °C + 273,15 are correct.
- Every substitution was recomputed and matches answers.py, except the L2-03 intermediate.
- L2-03: 30 °C gives 303,15 K, so 3 sf are justified; 550–560 °C stays inside ±0,02.
- L3-01: 1,298 · 10²² gives a = 1,3, inside tolerance; 2,7 · 10²¹ O₂ is correct.
- L3-03: the gauge difference equals the absolute difference; the initial mass is 2,64 kg, so 27 % leaked.
- The sanity numbers in L2-01, L2-02, L2-04 and L3-02, and the worked example (0,21 mol, 0,83 g, 6,0 g), are correct.
