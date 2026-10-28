VERDICT: DONE

Lesson-form retrofit (lint findings only; no numbers or physics claims changed).

lesson.md
- Ydinajatus: new inline SVG after the sand/water paragraph (house style, 600×300, currentColor, 24 px, aria-label, Q/ΔT/title as .fig-tex foreignObject): equal Q into equal masses of water and sand; thermometer rises drawn in the ratio 4190/800 ≈ 5,2 (20 px vs 105 px); sand level lower because it is denser.
- Esimerkki: staged into 5 `<!-- vaihe -->` stages (Tunnetut ja kysytty · Kaava ratkaistuna · Sijoitus · Tulos · Järkevyys). Kaava stage solves c_m symbolically; Sijoitus starts with the symbolic Q_v row, then 5656,5 J, 374,6 → 3,7·10² J/(kg·K). The significant-figure, copper and heat-capacity remarks are kept verbatim in Tulos/Järkevyys.

solutions.md
- fy3-6-L3-01: Kaava now ends with m_k = c_v m_v (T − T_v) / (c_k (T_k − T)); T = 40 °C moved to Annettu; wording tightened to stay under the word limit (all numbers kept).

Checks: check_lesson.py all ok, lint 0/0, test_inquiry.py 28 passed; 390 px screenshot shows the figure without clipping or overlap.

Note: lesson.md changes were swept into commit a9ed5d2 by someone else mid-pass; I did not commit.
