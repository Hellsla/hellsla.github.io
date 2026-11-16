VERDICT: FAIL
CONTENT-HASH: eff3226dac5f158c

## Blocking
- [Major] inquiry.json:344 (siirto solution; captures fy5-2-les-390-1, fy5-2-les-1280-1) — two formulas end with a comma that floats away from the result: "= 1471,5 Nm        ," (Sijoitus) and "= 1079,1 N        ," (Järkevyys), about 70 px away at 390 px and 130 px at 1280 px. The last row ends with the trailing `&` and the sentence's mark (`$$,`) is set after it, in a third alignment column — a lone comma in the middle of the box, beside numbers that use a decimal comma, looks like a typesetting error — put the mark before the `&`: either write it in the source (`&= 1471{,}5\,\text{Nm}\text{,} & \end{aligned}$$ yhteensä`, no comma after `$$`) or let mathlayout.with_punct set the mark before a trailing `&` (shared change; the same defect is in fy5-2 exercises, fy5-5 and fy5-6).

## Polish
- [Minor] inquiry.json:344 — at 1280 px the F_p chain is joined correctly; nothing to do. The "· 0,50 m" continuation rows start with "·" while fy5-1 ends the row with it.

## Checked
- Delta: the re-broken chains of inquiry.json (lines 32, 327, 328, 344). The formula-name change in lesson.md (teacher-approved, already on main) was not re-judged.
- Own captures from preview/fy5-2.html?ratkaisut=1, all boxes opened, in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis2-fi-1: fy5-2-les-390-1.png, fy5-2-les-1280-1.png.
- Kertaus feedback, both hints and the remaining solution chains: aligned, rows start at a relation or a sign, one row each at 1280 px, nothing clipped (scrollWidth 390 and 1280).

## Scores
illustrations 5 · typography 3 · Finnish 5 · accessibility 4
