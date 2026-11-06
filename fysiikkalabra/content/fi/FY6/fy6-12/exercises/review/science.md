VERDICT: PASS
CONTENT-HASH: 2e352fcfcb383439
Round 1, science, mode full. Scope: the new YO-skill task fy6-12-L2-08 (find the error, type 4); the rest of the set was PASS and is unchanged (commit a60d87f3e adds only L2-08, its solution and an answers.py comment). Checked from text only, no renders.

## Blocking

## Polish

## Checked
- Physics: an electron from rest at A (30 V) to B (120 V) moves toward higher potential. Rows 1, 2 and 4 are right as written (120 · 1,602e-19 J = 1,92e-17 J ≈ 1,9e-17 J). Row 3 is the only wrong row (it uses V_B for U). The right answer, 90 eV = 1,442e-17 J ≈ 1,4e-17 J, was recomputed in python.
- All numeric answers of the set were recomputed from answers.py against exercises.json in one call: no mismatch.
- Distractors target the lesson's warned mistakes: "every charge moves toward lower potential" (row 1), potential vs. potential energy and the sign of q (row 2), potential vs. potential difference (row 3, the correct choice), multiplying vs. dividing (row 4).
- Form: the choice labels are short and parallel, so none can be picked out by its length or by hedging. The correct choice's feedback explains only what is needed, and there is no reason stage.
- Notation is the lesson's: E_p = qV, U = V_B − V_A, E_k = eU, 1 eV = 1,602e-19 J. The task stays within fy6-12 and fy6-11.
- solutions.md follows Kysytty · Periaate · Mallivastaus, checks every row, rounds to two significant figures with a reason, and its check (ΔE_p = 90 eV) is a real check.
- Inline chains (text estimate): the longest, `U = V_B − V_A = 120 V − 30 V = 90 V` and `E_k = 1,442·10⁻¹⁷ J ≈ 1,4·10⁻¹⁷ J`, come to about 250 px, inside 300 px.
