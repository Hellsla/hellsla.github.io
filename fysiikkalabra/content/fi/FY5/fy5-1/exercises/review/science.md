VERDICT: PASS
CONTENT-HASH: 23f25874b515562a

## Blocking

## Polish
- exercises.json:114 (L1-09) — a unit check cannot separate $\tfrac{M}{d}$ from $\tfrac{M}{d\sin\alpha}$, so the chapter's main warned mistake (using $d$ in place of the arm $r$) cannot be a distractor here. The "long wrench increases the force" mistake is caught (in the feedback of $Md\sin\alpha$). Acceptable for type 7; no change needed.

## Checked
- Diff against HEAD~1: only L1-09 (type 7, Yksikkö ja dimensio) is new; every other task is byte-identical to the set that passed earlier.
- answers.py run once (`python3 -I`); every numeric answer recomputed and inside its tolerance (L1-09 has no number).
- L1-09 physics: $M = Fd\sin\alpha$ gives $F = \tfrac{M}{d\sin\alpha}$. The units of all four options are right in the options, the feedback and the solution: N·m², N, Nm, 1/N. Exactly one option is correct.
- Form: the four expressions are equally short, and two of them are fractions, so the correct one cannot be spotted by its form. The correct option's feedback does not go beyond the task.
- Notation $M$, $d$, $\alpha$ and $r = d\sin\alpha$ is the lesson's. The task stays inside fy5-1.
- Formula chains checked from the text only (no render): every expression is a short inline expression, under 300 px at 390 px width.
