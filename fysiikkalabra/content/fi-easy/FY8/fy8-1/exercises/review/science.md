VERDICT: PASS
CONTENT-HASH: 660f444084d55575
SCOPE: delta added-exercise from 5e7e04fa3110d92d base 5a45b28682e8

## Blocking
(none)

## Polish
- lessons/FY8/fy8-1/answers.py:263 — the comment says "387,6 nm -> 388 nm", but hc/W computes to 387,50 nm and the stored answer is 387 nm (the solution says 387,5 nm). Both are inside the ±5 % tolerance. — Make the comment say 387,5 nm -> 387 nm (shared file).

## Checked
- L1-10: λ0 = hc/W with W = 3,20 eV (MAFY, Ca) gives 387,50 nm; answer 387 nm, tol 5 %. The added definition of irrotustyö matches the glossary. The principle, the symbolic step, the conversion and the 1240 eV nm estimate are right.
- L2-08: h/e = 0,41361 eV per 1e14 Hz, f0A = 5,56e14 Hz, E_k,max = 4,963 − 2,30 = 2,663 eV; answer 2,66, tol 5 % takes the reading of 2,7 eV. The reading description is right.
- L2-09: f0B = 7,01e14 Hz (halfway between the 6 and 8 grid lines), λ0 = c/7,0e14 = 428,3 nm; answer 428, tol 4 %. The added definition of rajataajuus is right, and the warning not to read f0 from the vertical axis is right.
- The figure kuvaaja-ab (W_A = 2,30 eV, W_B = 2,90 eV, slope h/e) gives the needed values and no answers.
- The numbers and physics match the Finnish set the earlier review passed. The clearer Finnish drops no step of the solutions.
- Notation is the same as the brief's lesson (E_k,max, f0, λ0, hf = W + E_k,max). It is inside FY8 scope.
- Recomputed in one script, compared with answers.py: they agree.
- Hash 660f444084d55575 at start and end.
