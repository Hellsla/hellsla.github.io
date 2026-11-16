VERDICT: FAIL
CONTENT-HASH: 47cf3ab302a5fca5

## Blocking
- [Major] inquiry.json:420 (check-2 solution, Sijoitus; capture fy5-1-les-1280-1) — on a wide screen the second step renders as "= 4,75 Nm" and, about 190 px to the right in a third alignment column, "−2,85 Nm" with no binary spacing. The source rows `&= 4{,}75\,\text{Nm} & \\ &- 2{,}85\,\text{Nm}` are joined by join_wide after the trailing `&`, so the term lands in a new column — the student reads "= 4,75 Nm" as a finished step and a stray "−2,85 Nm" beside it — write the step as one row, `&= 4{,}75\,\text{Nm} - 2{,}85\,\text{Nm} & \\ &= 1{,}9\,\text{Nm}` (it fits at 390 px: shorter than the first row). At 390 px the block is correct.

## Polish
- [Minor] inquiry.json:361 (siirto solution) — at 1280 px the chain keeps its phone rows ("M = 12,0 kg · 9,81 m/s² ·" / "1,50 m · cos 40°" flush left); known join_wide limitation, readable.
- [Minor] inquiry.json:345 and 361 end a row with "·", fy5-2, fy5-5 and fy5-6 start the continuation row with "·"; choose one way for the course.

## Checked
- Delta: the re-broken chains of inquiry.json only (lines 32, 345, 361, 407, 420). The formula-name change in lesson.md (teacher-approved, already on main) was not re-judged.
- Own captures from preview/fy5-1.html?ratkaisut=1, every details box, feedback and step opened, in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis2-fi-1: fy5-1-les-390-1.png, fy5-1-les-1280-1.png.
- 390 px: all five blocks legible, rows start at a relation, a sign or a whole quantity, punctuation attached, nothing clipped (page scrollWidth 390).
- Standard captures are stale; not used.

## Scores
illustrations 5 · typography 3 · Finnish 5 · accessibility 4
