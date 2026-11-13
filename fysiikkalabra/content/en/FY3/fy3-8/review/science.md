VERDICT: PASS
CONTENT-HASH: fce3bdbb94cc86ef

## Blocking
None.

## Polish
None.

## Checked
Delta: tests/sims/fy3-8.json only; the five changed assertions swap ΔL, L_0, L for Δl, l_0, l (matching lang/*.json sims fy3-8) and keep the same quantities, numbers and tolerances (6,00 mm, 10,0060 m; −138 mm, 99,8620 m; 0,330 mm, 1,00033 m; 0,0600 %; l_0 = 42 m label), recomputed from Δl = α l_0 ΔT; build and test_sims fy3-8 pass on fi, fi-easy, en.
