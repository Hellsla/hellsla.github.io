VERDICT: FAIL
CONTENT-HASH: 8b70def838f7d770

## Blocking
- [Major] solutions.md:7, 27, 47, 57, 67, 87, 97, 117, 132, 220, 230 (Sijoitus of L1-01 … L3-03) — the comma after each γM block floats away from the result: "= 3,984 · 10¹⁴ m³/s²    ," (captures fy5-6-les-390-1, fy5-6-les-1280-1, fy5-6-ex-390-1, fy5-6-ex-1280-1: about 20 px at 390 px, about 150 px at 1280 px; L3-01 "= 3,3650 · 10²³ m³      ," about 70 px at 390 px). The last row ends with the trailing `&` and the mark after `$$` is set behind it in a third alignment column — eleven solutions show a lone comma in the box, beside decimal commas — put the mark before the `&` (`…\text{m}^3/\text{s}^2\text{,} & \end{aligned}$$ joten`, or fix mathlayout.with_punct once for all such blocks).

## Polish
- [Minor] solutions.md:97 (L3-01) — at 1280 px the block keeps its phone rows, every row flush left ("γMT² = …" / "· 6,42 · 10²³ kg · (88 620 s)²" / "= …"); known join_wide limitation.
- [Minor] solutions.md:184 (L3-04) — "Tähden massa on [formula ≈ 0,80] aurinkomassaa": the unit word is parted from its number by the display box; readable.

## Checked
- Delta: the re-broken chains of solutions.md (lines 7–232).
- Own captures from preview/fy5-6.html?ratkaisut=1, every level and solution opened, in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis2-fi-1: fy5-6-les-390-1.png, fy5-6-les-1280-1.png (γM blocks), fy5-6-ex-390-1.png, fy5-6-ex-1280-1.png (L1-07, L1-11, L3-01, L3-04).
- Apart from the comma: mantissa and power of ten never parted, "·" only between whole quantities, Järkevyys formulas whole with marks attached. Nothing clipped, scrollWidth 390 and 1280.

## Scores
illustrations 5 · typography 3 · Finnish 5 · accessibility 4
