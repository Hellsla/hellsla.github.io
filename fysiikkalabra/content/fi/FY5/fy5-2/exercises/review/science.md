VERDICT: PASS
CONTENT-HASH: c75903ad5b8c78a8

## Blocking

## Polish
- exercises.json:244 (L2-08, option Rivi 4) — the misconception named for doubting row 4 ("the plank tips as soon as the can is past B") has nothing to do with $N_\text{A} = G + G_\text{p} - N_\text{B}$. Name a misconception about row 4 itself, e.g. "ajattelee, että tuki A kantaa vain lankun painon" or "unohtaa purkin painon voimien summasta".

## Checked
- Diff against HEAD~1: only L2-08 (type 4, Virheen löytäminen) is new; the rest of the set is unchanged.
- answers.py run once. Its new asserts and my own recomputation agree. The student's rows give 280 Nm, 140 N and 60 N. The correct values with $r_\text{p} = 3{,}0\,\text{m}$ are $N_\text{B} = 180\,\text{N}$ and $N_\text{A} = 20\,\text{N}$. The check about B, $+80 - 40 - 40 = 0\,\text{Nm}$, has the right signs (counterclockwise positive).
- Exactly one wrong row (row 2). Rows 1, 3 and 4 really are correct with row 2's values, and the "Laskussa ei ole virhettä" option is last.
- $N_\text{A} = 20\,\text{N} > 0$, so the plank does not tip. The model is consistent.
- Distractors catch the chapter's warned mistakes: moments taken only about the centre of gravity (row 1) and each support carrying half (row 3).
- Notation ($N_\text{A}$, $r_G$, counterclockwise positive) is the lesson's. The task stays within fy5-1 and fy5-2.
- Formula chains checked from the text only: every line of the solution is a short inline equation, under 300 px.
