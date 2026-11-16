VERDICT: FAIL
CONTENT-HASH: 75da751474866688

## Blocking
- [Major] exercises/solutions.md:7 (task 5-1, Substitution; captures fy5-5-ex-step-390-0.png, fy5-5-ex-step-1280-0.png) — the calculation is torn in two: the first inline piece `F = 6.674 · 10⁻¹¹ N·m²/kg² ·` is drawn alone in a white formula box, in small type and ending with a dangling multiplication dot, and the rest (`70 kg · 55 kg / (0.80 m)² = 4.015 · 10⁻⁷ N = 0.4015 µN`) follows as loose, larger text outside the box, at 390 and at 1280 px — the first worked solution of the set looks like two separate statements, and the box reads as an unfinished formula — the solution builder turns a step that begins with `$F = …$` into an equation chain of that piece only; write the step as one display block in the house form, as the other tasks of this set do: `$$\begin{aligned} F &= 6.674 \cdot 10^{-11}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{kg}^2} \\ &\quad \cdot \dfrac{70\,\text{kg} \cdot 55\,\text{kg}}{(0.80\,\text{m})^2} \\ &= 4.015 \cdot 10^{-7}\,\text{N} \\ &= 0.4015\,\mu\text{N} \end{aligned}$$`. The same split is in the built Finnish and fi-easy pages of this task.

## Polish
(none)

## Checked
- Round 3 delta (re-broken calculations only). Own Playwright captures of preview/en/fy5-5.html?ratkaisut=1, every details box open, at 390 and 1280 px, in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis3-en-1/r3/: sheet-fy5-5-ex-390-0.png, sheet-fy5-5-ex-1280-0.png (opened as combo-fy5-5-0.png), and at double resolution /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis3-en-1/fy5-5-ex-step-390-0.png, fy5-5-ex-step-1280-0.png (opened as fy5-5-ex-step-both.png).
- Every formula the branch changed in exercises/solutions.md was located on the page and opened in the sheets; page scrollWidth equals the viewport with the boxes open, no KaTeX error, no script error.
- The other substitution blocks of the set (2.503 N, 3.799 kN, 4.27 · 10⁷ N) are whole display blocks with `· fraction` as an indented continuation row: fine, and the model for the fix.

## Scores
illustrations 5 · typography 2 · Finnish 5 · accessibility 4
