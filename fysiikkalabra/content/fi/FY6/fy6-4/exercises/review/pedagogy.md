VERDICT: PASS
CONTENT-HASH: f3db54128b103065
SCOPE: delta caption-label,md-paragraphs,numbers,reflow,teacher-figure,typography from b76783ab2894e5cb base b5600a6

## Blocking
- none

## Polish
- solutions.md, Kaava rows with `\Sigma U = 0 \Rightarrow U = U_1 + U_2` (L1 series tasks, L3 E12 task) — Kirchhoff's laws are taught only in the next chapter, and the sign step (`U - U_1 - U_2 = 0`) is skipped, so the symbol is unexplained here. Keep the rule's basic-principle start, but write the principle in the Periaate line in words ("jännitteet summautuvat") or drop `\Sigma U = 0` from this chapter's solutions.
- L3 E12 task, Kaava — `\Sigma U = 0 \Rightarrow R_\text{sarja} = R_a + R_b` jumps over `U = RI`; add the two rows `U = (R_a + R_b) I` and `U = R I`.
- Heater task (I_rinnan / I_sarja), Kaava — the step from `I = U/R` to `R_sarja / R_rinnan` is not shown; add `I_rinnan / I_sarja = (U / R_rinnan) / (U / R_sarja)`.

## Checked
- Diff judged in context: Kaava steps now start from a basic principle and run as aligned rows (read from the files on disk), the symbolic result is reached before substitution, and every chain still ends in the earlier formula.
- Derivations (parallel `U/R = U/R_1 + U/R_2`, three equal resistors, quadratic in L3) are correct and followable.
- Split Sijoitus and Mallivastaus paragraphs read well, one idea each; numbers unchanged.
- L2-09 and the two task figures (teacher-approved) unchanged and still give the data without the answer.
- Levels, counts and L2-09 earlier acceptance stand; no numbers or answers changed.
- Captures in the packet predate the new Kaava rows (the level 1 capture shows the old form); the layout checks are green at 360 to 1280 px.
