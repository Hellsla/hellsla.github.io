VERDICT: FAIL
CONTENT-HASH: 066c07440570c5e8

## Blocking
- [Major] solutions.md:142 (L2-07 Kaava), :177 (L3-01 Järkevyys), :205 (L3-04 Sijoitus, second formula) — the sentence's comma or full stop floats far from the last row: "= 0          ,", "= 240 kg·m        ,", "= 124,4 Nm        ." (captures fy5-2-ex-390-1, fy5-2-ex-1280-1; up to about 150 px at 1280 px). The last row ends with the trailing `&`, and the mark after `$$` is set behind it in a third alignment column — a lone mark in the box reads as a typesetting error — put the mark before the `&` (in the source: `&= 0\text{,} & \end{aligned}$$ josta`, or in mathlayout.with_punct for every such block).

## Polish
- [Minor] solutions.md:142 — at 1280 px "mg(x − 5,0 cm) − Mg(50,0 cm − x)" and "= 0" stay on two rows although one fits; known join_wide limitation.
- [Minor] solutions.md:205 — the first formula of the pair (1547 Nm) has no mark, the second has the full stop; consistent once the mark is attached.

## Checked
- Delta: the re-broken chains of solutions.md (lines 91–217). The caption-marker change in exercises.json (teacher-approved, already on main) was not re-judged.
- Own captures from preview/fy5-2.html?ratkaisut=1, every level and solution opened, in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis2-fi-1: fy5-2-ex-390-1.png, -390-2.png, fy5-2-ex-1280-1.png, -1280-2.png (21 blocks).
- The other lifted formulas (L2-02, L2-04, L2-05, L2-06, L2-08, L3-03, L3-05) are whole, aligned, marks attached, nothing clipped; scrollWidth 390 and 1280.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 4
