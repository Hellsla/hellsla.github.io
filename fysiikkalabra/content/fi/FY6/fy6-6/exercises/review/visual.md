VERDICT: FAIL
CONTENT-HASH: 3e04d8b6c8dc818b
ROUND: 2

## Blocking
- [Major] solutions.md fy6-6-L3-04 Vastaus (open-exercises-L3-1280-5, bottom) — the Vastaus line now starts with "$R_1 = 48{,}1\,\Omega$ ja $R_2 = 77{,}9\,\Omega$", so the solution's answer box shows "R₁ = 48,1 Ω" while the task's answer pill and answer box ask for 822 W (kohta b) — the solution contradicts the answer entered by the student — begin the line with the entry value: "$822\,\text{W}$ vastuksessa $R_2$ (pyöristettynä $8{,}2 \cdot 10^{2}\,\text{W}$). Kohdan a) resistanssit ovat $R_1 = 48{,}1\,\Omega$ ja $R_2 = 77{,}9\,\Omega$. …".

## Polish
- [Minor] fy6-6-L1-07 — now a plain P = UI with a mA conversion, close to L1-01 and L1-02 (P = UI / RI²); fine for level 1 but only the conversion is new; for science/pedagogy to judge whether it adds enough.
- [Minor] fy6-6-L3-04 Kaava/Sijoitus — the formula line "$R_1 = \dfrac{U^2}{P_1}$, $R_2 = ...$, $P' = \dfrac{U'^2}{R}$" has inline \dfrac that touches the line below (L3-1280-5); use \tfrac inline or a display block.
- [Minor] fy6-6-L3-05 Kaava (L3-1280-7) — the first two formulas are in an aligned block and $P_\text{j} = R_\text{j}I^2$ stays alone on a line below it; put all three in the block (carried over).

## Checked
- Round 1 Polish: ”…” quotation in L2-07 (fixed), 48,09 used consistently in L3-04 Sijoitus (fixed), Vastaus now shows the unrounded and the rounded value in L2-06, L3-05 (fixed; L3-05 pill 152,5 W matches).
- 1280 px captures open-exercises-1280-7, -8 (L1-07, L1-08), L2-1280-6 (L2-05, L2-06 start), L3-1280-5, -6, -7 (L3-04, L3-05) read at full size; exercises.json diff (MC L1-06 rewritten without formulas, L1-07 replaced, answers.py updated to 4,2 W) and solutions.md read; L1-07 and L2-05 numbers recomputed. No 390/360 px capture of exercise cards exists; packet layout checks are clean.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
