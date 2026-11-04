VERDICT: FAIL
CONTENT-HASH: e1d566ce1d59da9e

## Blocking
- [Major] solutions.md fy7-4-L3-05, Sijoitus (a) — `check_layout.py fy7-4 --width 360` reports "FAIL formula 6 px [hints] inline, cannot wrap: = \sqrt{\dfrac{2\pi \cdot 0{,}010\,\text{m} \cdot 0{,}0030\,\text{kg} …" — the chain `I = \sqrt{\dfrac{…}{…}} = \sqrt{2943\,\text{A}^2} = 54{,}25\,\text{A}` overflows a 360 px phone by 6 px, because the radicand cannot wrap — shorten the first side without changing the physics, for example give the denominator separately ("$\mu_0 l = 4\pi \cdot 10^{-7}\,\tfrac{\text{Vs}}{\text{Am}} \cdot 0{,}50\,\text{m} = 6{,}28 \cdot 10^{-7}\,\text{Vs/A}$") and write `I = \sqrt{\dfrac{2\pi \cdot 0{,}010\,\text{m} \cdot 0{,}0030\,\text{kg} \cdot 9{,}81\,\text{m/s}^2}{6{,}28 \cdot 10^{-7}\,\text{Vs/A}}}`, or drop the units inside the root and put $\text{A}^2$ after it.

## Polish
- [Minor] L1-08 Periaate — "verrannollinen sini $\sin\alpha$ eikä kulmaan" is ungrammatical — "verrannollinen kulman siniin $\sin\alpha$ eikä kulmaan $\alpha$".
- [Minor] L2-06 text — the pupil's calculation is in straight quotes; use ”…”.
- [Minor] L2-07 Järkevyys — the coil radius $1{,}2\,\text{cm}$ gives about $70$ turns, "lähellä kierroslukua $60$"; the lesson uses $1{,}3\,\text{cm}$ ($65$ turns) — use the lesson's radius.
- [Minor] L2-05, L2-07, L3-04 tables — long captions with maths make the tables scroll at 360 px (layout warnings); shorten "(esimerkkiaineisto)" captions or move the current into the task text.

## Checked
- Contact sheets 7 and 8 (#73–#85): L2-05 (4-13), L2-06 (4-14), L2-07 (4-15), L3-04 (4-19), L3-05 (4-20), solutions open; at 1280 px the L3-05 chain is clean.
- Ran check_layout fy7-4 --width 360: the one FAIL above; the table lines are warnings only.
- Recomputed 0,30 N; 0,094 N; 0,085 T; 0,041 T; 5,3 m; 0,35 T; 54 A: all match the solutions; the vertical-stability argument in L3-05 is correct.
- No plain quantity, no ×.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 3
