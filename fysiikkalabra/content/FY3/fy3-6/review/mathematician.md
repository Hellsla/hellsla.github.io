VERDICT: PASS
CONTENT-HASH: 79f641894690432a

## Blocking
(none)

## Polish
- lesson.md:38–39 — the 6 pt gap is the only thing that separates the two equations of the T derivation, and nothing says that the second one follows from the first. Optional fix: start row 39 with `\Rightarrow\;` (`&\Rightarrow\; c_1 m_1 T_1 + c_2 m_2 T_2`); line 34 already describes the steps.

## Checked
- lesson.md:15–18: the `aligned` pair `Q = cmΔT` / `ΔT = T_loppu − T_alku` is aligned at `=` and has the same content as before the split.
- lesson.md:36–42 row by row: rows 1–2 expand c₁m₁(T₁ − T) = c₂m₂(T − T₂). Rows 3–4 add c₁m₁T + c₂m₂T₂ to both sides (the right side is reordered, which is valid). Row 5 factors out T. The `\quad` indent marks continuation rows.
- lesson.md:46: dividing by c₁m₁ + c₂m₂ gives the displayed T, which agrees with row 5.
- lesson.md:87–90: the left side is alone on row 1 and `= 4190 J/(kg·K) · 0,300 kg · 4,5 K` is on row 2. 4190 · 0,300 · 4,5 = 5656,5 J, which matches line 92.
- lesson.md:94–98: 5656,5 / (0,200 · 75,5) = 5656,5 / 15,1 = 374,60 → ≈ 3,7·10² J/(kg·K), with rounding only on the last row. Every row is aligned at `=`/`≈`, and the name `c_metalli` is used consistently on lines 88 and 95.
- lesson.md:108–112 row by row: 1,0 kg·(80 °C − T) = 3,0 kg·(T − 20 °C), with the hot side on the left as in line 30. Dividing by kg and expanding gives 80 °C − T = 3T − 60 °C. Adding T + 60 °C gives 140 °C = 4T, so T = 35 °C. Units are consistent.
- lesson.md:115: "Kolmannella rivillä" correctly names the visual row 3, where the division by kg and the expansion of the brackets both happen. The weighted mean (3,0·20 + 1,0·80)/4,0 = 140/4,0 = 35 °C, with kg·°C/kg = °C, is the same as line 46 with c cancelled.
- lesson.md:102: 0,300 · 4190 = 1257 J/K, and 0,200 · 374,6 = 74,9 ≈ 75 J/K.
- solutions.md:53: ΔT = 95 °C − 15 °C = 80 K. Q = 502 800 J and t = 209,5 s ≈ 210 s. The solution is now consistent with L1-01. solutions.md:87: the added upper-limit sentence does not change the mathematics.
- `lint_lesson.py`: 0 errors and 0 warnings. `check_latex.py`: all 13 fragments OK. `check_layout.py fy3-6`: OK at 360 px. exercises.json, answers.py and exit-ticket.json are unchanged since c2ad583.
