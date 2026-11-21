VERDICT: PASS
CONTENT-HASH: 15049c66145b9c8b

## Blocking

## Polish
- content/en/FY7/fy7-16/lesson.md:297 — the answer writes the ratio both as $P_0 : P$ and as $P/P_0$ in one sentence — optionally write $P : P_0 \approx 0.13$ to match the division notation used elsewhere in the step (and the figure's axis $P : P_0$).

## Checked
- Delta (pysahdy, line 297): recomputed $A = 0.18 \cdot 50 = 9.0\,\text{dB}$, $10^{0.90} = 7.94 \approx 7.9$, $1/7.94 = 0.126 \approx 0.13$, so about 13 % left; correct.
- The added inverse step follows the lesson's definition $A = 10\,\text{dB}\cdot\lg(P_0 : P)$ (line 240) and the worked example's step $\lg(P_0/P) = A/10\,\text{dB}$ (line 324); units cancel correctly.
- Rounding: 9.0 dB and 13 % have two significant figures, as the data 0.18 dB/km.
- Consistent with the theory text (every 10 dB to a tenth; 9 dB just above a tenth) and the summary.

## Vanhan sisällön löydökset
None.
