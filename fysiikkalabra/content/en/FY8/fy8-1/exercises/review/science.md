VERDICT: PASS
CONTENT-HASH: f22ac3e71db8780e
SCOPE: delta added-exercise from b4640f1fa75ce4b0 base 5a45b28682e8

## Blocking
(none)

## Polish
- lessons/FY8/fy8-1/answers.py:263 — the comment says "387,6 nm -> 388 nm", but hc/W computes to 387.50 nm and the stored answer is 387 nm (the solution says 387.5 nm). Both are well inside the ±5 % tolerance. — Make the comment say 387.5 nm -> 387 nm (shared file; this is not a translation issue).

## Checked
- L1-10: λ0 = hc/W with W = 3.20 eV (MAFY, Ca) gives 387.50 nm; answer 387 nm, tol 5 %. Principle hf0 = W, the symbolic step, the eV→J conversion and the 1240 eV nm estimate are all right. Calling 387 nm UV, just short of the violet edge, is correct.
- L2-08: h/e = 0.41361 eV per 1e14 Hz, f0A = 5.56e14 Hz, E_k,max = 4.963 − 2.30 = 2.663 eV; answer 2.66, tol 5 % (2.53–2.79) takes the graph reading of 2.7 eV. The reading description (about 0.3 below 3 eV) matches the line.
- L2-09: f0B = 2.90/0.41361 = 7.01e14 Hz, halfway between the 6 and 8 grid lines; λ0 = c/7.0e14 = 428.3 nm; answer 428, tol 4 %. The reasonableness check (2.9 eV > W_A, so B's line lies to the right of A's) is a real check.
- The figure kuvaaja-ab (W_A = 2.30 eV, W_B = 2.90 eV, slope h/e, axes 0–16e14 Hz and 0–5 eV) gives every value the tasks need and writes no f0 or W on it; its description does not give the answers away.
- The solutions use the brief's notation and model (E_k,max = hf − W, f0, λ0). It is all inside FY8 scope.
- The English wording and numbers match the Finnish set the earlier review passed, with decimal points.
- Recomputed in one script, compared with answers.py: they agree.
- Hash f22ac3e71db8780e at start and end.
