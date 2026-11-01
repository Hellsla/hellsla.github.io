VERDICT: FAIL
CONTENT-HASH: 449906b56c123714

## Blocking
- [Major] exercises.json L1-03, L3-02, L3-03 — numbers with units and a calculation are plain text with Unicode superscripts beside maths ("20,0 m²", "(1 GWh = 3,60 · 10¹² J)", "1 kt = 10⁶ kg", "0,950 · 0,400 = 0,380"); the sans font differs from the maths, and "10¹² / J)" breaks across a line at 390 px — house rule: number with unit in prose is maths — fix: $20{,}0\,\text{m}^2$, $1\,\text{GWh} = 3{,}60 \cdot 10^{12}\,\text{J}$, $1\,\text{kt} = 10^{6}\,\text{kg}$, $0{,}950 \cdot 0{,}400 = 0{,}380$.

## Polish
- [Minor] figure fy3-15/chain-bars — P3 bar is blue while the lesson uses navy for electricity and orange for heat flow; gridlines every 50 MW but ticks only every 100 — use the lesson's colour, label or drop the extra lines.
- [Minor] L3-02 solution Järkevyys — nested \tfrac with J/kg and powers of ten is tiny; use \dfrac.
- [Minor] L1-02/L2 tasks — dimensionless values (0,910, 0,380) plain in tasks, maths in solutions; unify.

## Checked
- open-exercises 1280 parts 1, 3, 4, 5 (L1); L2 parts 1, 3; L3 parts 1–4; stage-exercises-390; chain-bars figure in L1-04.
- Solutions' chains aligned at "=", fractions, units upright, \cdot used; no clipping.

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 4
