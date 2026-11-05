VERDICT: PASS
CONTENT-HASH: 55a1c542063de95f

## Blocking

## Polish
- exercises/solutions.md fy8-2-L1-07 (Model answer) — the parenthesis "(this reason is required: merely stating “the states are different” is not enough)" is a grader note inside the model answer; it mirrors the Finnish, so left as is.
- exercises/solutions.md fy8-2-L3-04 (Reasonableness) — "mirror-image level system" is mirrored from the Finnish; understandable, no change needed.

## Checked
- Structural scripted diff against content/fi: same ids, kinds, answers, units, tolerances, correct flags, choice order, table captions, columns and every table cell for all 8 new tasks (L1-06..08, L2-05..07, L3-04..05); no differences.
- Every number in the task texts, choices, feedback and solutions equals the Finnish after decimal-comma normalisation; the only token-order difference is L1-08 (wording of the same two energies), same values.
- Decimal point used in en JSON and LaTeX; no decimal comma left; no Finnish words left in en (grep of exercises.json and solutions.md).
- Recomputed new answers: L2-05 2.27 eV (mercury 435.8/546.1/577.0 match), L2-06 -0.85 eV (E_n = -13.6/16, n = 4; line E 527.1 nm unidentified), L2-07 497 nm (fit 12.01 nm/mm, 299.6 nm), L3-04 1127 nm (levels 1.10, 2.40, 3.90 eV), L3-05 22.1 % (dye B; D gives 477 nm).
- L1-06 and L1-08: exactly one correct choice, feedback names the actual misconception; L1-08 direction of transition (absorb vs emit) correct.
- check_i18n.py en: 0 errors.
