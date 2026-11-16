VERDICT: FAIL
CONTENT-HASH: 000d0d711d21a11a
ROUND: 3

## Blocking
- [Major] inquiry.json 400 (transfer task, Sijoitus; captures fy5-14-390-doppler-ctx.png, fy5-14-390-doppler-zoom.png) — the Doppler substitution, an aligned block in round 2, is now three inline formulas, and at 390 px they wrap flush left as "f = 2000 Hz" | "· 340 m/s : (340 m/s − 12,566 m/s)" | "= 2076,8 Hz" with no box and no alignment, directly under the boxed, aligned v_L block of the same step. The multiplication dot that opens the second line touches the left end of the fraction bar and reads as part of it, so the line looks like "f = 2000 Hz" followed by a separate fraction "= 2076,8 Hz" — the main calculation of the task loses its operator on a phone, and the step is set in two different ways. — Set it as the house continuation form, as fy5-15 inquiry.json 308 is: `$$\begin{aligned} f &= 2000\,\text{Hz} \\ &\quad \cdot \dfrac{…}{…} \\ &= 2076{,}8\,\text{Hz} \end{aligned}$$`; if the three inline pieces must stay, move the dot to the end of the first piece (`$f = 2000\,\text{Hz} \cdot{}$`), so that no line begins with a bare dot against a fraction bar.

## Polish
- [Minor] same place, 390 px — the fraction's numerator sits close under "f = 2000 Hz" (inline line height); goes away with the display block.

## Checked
- Delta, round 3: inquiry.json 400 only; lesson.md not in the diff.
- Own captures from preview/fy5-14.html?ratkaisut=1, every details open, in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis3-fi-13/: fy5-14-390-dop2-0.png, fy5-14-390-doppler-ctx.png (with the steps around it), fy5-14-390-doppler-zoom.png, fy5-14-1280-dop2-0.png.
- 1280 px: the chain is on one row, "f = 2000 Hz · fraction = 2076,8 Hz", sound. The defect is at 390 px only.
- No page overflow (scrollWidth equals the viewport at both widths); nothing clipped.

## Scores
illustrations 5 · typography 3 · Finnish 5 · accessibility 4
