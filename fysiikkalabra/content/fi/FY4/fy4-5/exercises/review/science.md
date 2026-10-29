VERDICT: PASS
CONTENT-HASH: 5ea8f43966d623bc

## Blocking

## Polish
- solutions.md L1-05 — the task now says "Piirrä köyden voima ja sen komponentit katkoviivoin", but the solution has no drawing step. — Add one Voimakuvio line before Kaava, for example "T vinosti ylös 40° kulmassa, T_x vaakasuoraan ja T_y pystysuoraan katkoviivoin".
- solutions.md L1-01 Vastaus — the answer gives 14,7 N ≈ 15 N "kaksi merkitsevää numeroa", which mixes two precisions. — Give 15 N as the final answer and mention 14,7 N only as the intermediate value.

## Checked
- L1-01: the answer is now 14.7 with tolerance 0.03, a limit of 0.441 N. Both 14,7 and 15 are accepted, and answers.py gives 14.715.
- The L1-05 rounding sentence is now right. 191,5 N → 190 N is within tolerance, and so is 192.
- The L3-01 wording change (draw before opening the solution) leaves the physics unchanged: N = m(g − 1,5) = 581,7 → 580 N, and the model figure `malli-hissi` agrees.
- All 12 answers were recomputed in one script and agree with exercises.json and answers.py (largest difference 0,8 %).
- Every fbd-tagged solution draws its diagram before its equations, with signs that follow the diagram.
- Directions: the wall's N is horizontal and the friction on the book points up; the ceiling pushes the balloon down; the curling stone has no forward force; for the downward push, N > G.
- Model figures: `malli-pulkka` has N < G and F_μ = T_x, with T_x dashed. In `malli-hissi`, N < G, and v and a are drawn as separate blue arrows.
- The `ruutu` figure and its description give the forces without giving the answer away (15 N).
- The units, the gram-to-kilogram conversion and the magnitudes are realistic.
