VERDICT: PASS
CONTENT-HASH: bb52b416609e298b
SCOPE: delta added-exercise from 6eb91ace4b5c1ba6 base 5b3ca4f81c77

## Blocking

## Polish
- solutions.md:370 (L3-06) — the ordinals are right on its 1-unit grid ("seitsemännen", "neljännen"), but naming the lines by their values ("vaakaviivan $7$", "vaakaviivan $4$") would match the L2-08 wording now.
- L3-06 tolerance ±4 % — a careful reading of ±0,1 per point moves the ratio by 2–4 % (6,7/4,1 → 2,91; 6,9/3,9 → 3,15), so it can just land in "Lähellä". Acceptable; ±5 % would be safer.

## Checked
- Round-1 blocking item fixed: solutions.md:336 (L2-08) now says "Piste on hieman vaakaviivan $4{,}0$ alapuolella". This matches the figure (0,5 grid, point at 3,927) and the stated 0,5 spacing, and the self-contradicting ordinal is gone.
- `git diff f19f98ccc HEAD`: in the fi exercise set the only change is that one line of solutions.md. exercises.json, answers.py and figures.py are unchanged. The en and fi-easy solutions changed one line each, as the parallel fix, and are not judged here.
- Recomputed in one script: L1-10 6,7455e15 1/s (MAFY h); L2-08 3,9e15 · hc/520 nm = 1,490 mW → 1,5; L3-06 1,70 · 1,7778 = 3,022 → 3,0; figure point 3,927e15. All agree with answers.py (6,745547e15; 1,5; 3,0).
- Physics, scope, units and rounding are as passed in round 1.
- Hash bb52b416609e298b at start and end.
