VERDICT: FAIL
CONTENT-HASH: d9ad8d1ce3ec7242

## Blocking
- inquiry.json:364 (tarkistus-2 solution, Järkevyys) — B/6: "betonille tyypillinen noin $5\,\text{cm}$" contradicts lesson.md:523 ("cesium-137:n gammasäteilylle ... betonissa noin $4\,\text{cm}$") and fy8-12 ("betonia noin seitsemän kertaa paksumpi" than 5,5 mm Pb ≈ 3,9 cm). Narrow-beam Cs-137 value is ≈3,8 cm; 5–6 cm holds only for higher energies (Co-60), which the text does not say. — Fix: "samaa suuruusluokkaa kuin cesium-137:n gammasäteilyn puoliintumispaksuus betonissa, noin 4 cm" (or state the higher energy).

## Polish
- lessons/FY8/fy8-13/lesson-answers.py:36 — section comment still says "(STUK 2023)" while the docstring and lesson cite STUK-A263 (2020) — change to "(STUK-A263, 2020)".

## Checked
- Dose breakdown: STUK-A263 (Siiskonen ym., 2020, tilanne 2018) gives 5,9 mSv total, radon ~4, other natural ~1,1, health care 0,76; table, bar figure (to scale), summary, ennuste-3 feedback all agree; 5,1/5,9 = 86 % ("noin 85 %"), 4/5,9 = 68 % ("kaksi kolmasosaa"), 4/0,8 = 5×.
- Hook/hero neutral: no radon reveal before ennuste-3; exactly one correct option there, distractor feedback numbers right.
- Term puoliintumispaksuus $d_{1/2}$ consistent with fy8-12 symbol and formula; Pb 5,5 mm for Cs-137 matches fy8-12 and μ/ρ data (≈5,4 mm); model's 6,0 mm stated as rounded.
- Flight "noin 3 µSv/h" plausible for long-haul cruise; ilmakehä mechanism correct.
- Recomputed: siirto 12,5 µSv and its mistakes 37,5/25/50/750; esimerkki 4,0 mSv; virhe 1,2 mSv; 1 Gy → 2,4·10⁻⁴ K; ΣwT = 1.
- Sim/experiments: koe-1 and koe-2 isolate r and x; model values 40/10/4,44/2,50 and 40/20/10/5,00 match sim.js.
- Tarkista 2 figure reads 80 → 40 µSv/h at 5,0 cm; answer 5,0 cm correct.
- Exit ticket and summary agree with theory.
