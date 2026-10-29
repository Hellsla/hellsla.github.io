VERDICT: PASS
CONTENT-HASH: 8e28baefc5966084

## Blocking

## Polish
- solutions.md L1-05 — the task asks the student to draw the rope force and its dashed components, but the solution has no Voimakuvio step. — Add one line before Kaava: "T vinosti ylös 40° kulmassa, T_x ja T_y katkoviivoin".
- solutions.md L1-01 Vastaus — "14,7 N ≈ 15 N, kaksi merkitsevää numeroa" mixes two precisions. — Give 15 N as the answer and 14,7 N only as the intermediate value.
- lessons/FY4/fy4-5/figures.py:258 — the `malli_hissi_jarru` docstring says L3-02, but the figure belongs to L3-01.

## Checked
- I recomputed all twelve answers in one script with my own formulas: 14,7; 15; 4,9; 637,7; 191,5 N; 52,0; 660,6 N; 0,598 m/s²; 1,0 m/s²; 581,7; 1,9; 0,0608 N. All agree with answers.py and exercises.json within tolerance.
- No solution describes a point model. Every diagram step says "suorakulmiona" (L2-04: seen from above, with G and N from the side).
- `ruutu`: 32 px = 10 N, F1 40 N, F2 25 N, F3 = F4 = 30 N, drawn from the sides of a rectangle. The description gives the same data and not the 15 N.
- `malli-pulkka` is to scale: G 147 N, N 117 N, T 60 N at 30° from the front top corner, F_μ = T_x = 52 N from the back bottom corner, and ΣF = 0.
- `malli-hissi`: N 594 N < G 687 N, with v blue up and a orange down, both off the body, and the lift drawn as a pictorial situation picture.
- Directions: the wall's friction points up on the book (L1-03). The ceiling's N points down on the balloon, with F_noste = G + N (L3-03). The curling stone has no forward force (L3-02). A lift slowing upward has a_y < 0 (L3-01).
- Rounding follows the limiting datum. The units and the g → kg conversion in L3-03 are right.
