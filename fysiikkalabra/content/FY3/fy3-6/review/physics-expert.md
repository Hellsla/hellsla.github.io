VERDICT: PASS
CONTENT-HASH: 786ee55d45e2cdff

## Blocking

None.

## Polish

1. lesson.md:87 — the 0,1 K gap between the lossless 24,6 °C and the measured 24,5 °C is put down only to losses, but 0,1 K is also the reading resolution, and the example's own premise sets losses aside. — Write "selittyy lukematarkkuudella tai sillä, että osa lämmöstä siirtyi …".
2. solutions.md:87 (L3-02) — "sopii kokemukseen" is fine, but 3,6 K is an upper limit because evaporation and night-time radiation are left out. — Optionally add "todellinen nousu on pienempi, koska osa energiasta kuluu haihtumiseen".

## Checked

- Hash before and after the review: 786ee55d45e2cdff (unchanged). lint: 0 errors, 0 warnings. check_latex: all 13 fragments OK.
- lesson.md:15–42: Q = cmΔT with ΔT = T_loppu − T_alku and the sign convention, C = cm (J/K), the balance equation with both sides positive, and the algebra to T = (c₁m₁T₁ + c₂m₂T₂)/(c₁m₁ + c₂m₂) are all correct. The weighted-mean statement is correct.
- Table c values are standard. Ratios 0,19 (sand/water) and 9,3 (water/iron) support the text.
- Example: c = 374,6 ≈ 3,7·10² J/(kg·K). A reading of 24,6 °C gives 383,4 J/(kg·K). Lossless copper gives 24,618 °C, matching the sim default.
- Misconception: the 35 °C working is correct, and so are exit-ticket 3 (65 °C) and exit-ticket 1 (419 kJ).
- answers.py: every line uses the right formula, sign and conversion. The L1-04 sign is negative and L1-05's ΔT is 18 K. L2-01 cancels c with grams. L2-03 adds ΔT to T_alku. L3-01 uses the 260 K drop for the stones. In L3-02 the area cancels.
- Hand-recomputed L2-04 = 27,11 °C (ladle −67,9 K, water +9,1 K), L3-02 = 3,58 K and L3-03 = 3,27 m³ (c ratio 5,24 > volume ratio because of density 1,6).
- solutions.md: the sanity checks are physically correct, including L1-02 ≈ ⅓ of 0,63 MJ, L1-03's 3,4 K, the 7,5× heat-capacity ratio in L2-04 and the L3-01 mass ratio of 0,60.
- sim.js:51–54 uses exactly the lesson's Teq, with C = cm and Q_body = Q_water, not an approximation. The exponential approach is labelled as illustration, and the 0–100 °C ranges cause no phase change.

```
{"fy3-6-L1-01": 0.633528, "fy3-6-L1-02": 210.6, "fy3-6-L1-03": 720.0, "fy3-6-L1-04": -35.196, "fy3-6-L1-05": 18.9, "fy3-6-L2-01": 77.6, "fy3-6-L2-02": 209.5, "fy3-6-L2-03": 53.749403, "fy3-6-L2-04": 27.113624, "fy3-6-L3-01": 12.086538, "fy3-6-L3-02": 3.579952, "fy3-6-L3-03": 3.273438}
```
