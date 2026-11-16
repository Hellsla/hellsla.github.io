VERDICT: FAIL
CONTENT-HASH: cbbe539866c1e960

## Blocking
- [Major] inquiry.json:210 (koe 1 solution), :406 (siirto solution), :460 (tarkistus 2 solution) — the comma after each γM / γT² block floats away from the result: "= 3,984 · 10¹⁴ m³/s²    ," and "= 5,0619 · 10⁻² m³/kg    ," (captures fy5-6-les-390-1, fy5-6-les-1280-1: about 20 px at 390 px, about 150 px at 1280 px). The last row ends with the trailing `&` and the mark after `$$` is set behind it in a third alignment column — a lone comma in the box, beside decimal commas, reads as a typesetting error and repeats in every solution — put the mark before the `&` (`…\text{m}^3/\text{s}^2\text{,} & \end{aligned}$$ joten`, or fix mathlayout.with_punct once for all such blocks). Line 210 sits in a hidden experiment answer: judged from the rendered TeX in the preview (same `&\text{,}`), not from a capture.

## Polish
- [Minor] The continuation row starts with "·" here; fy5-1 ends the row with it.

## Checked
- Delta: the re-broken chains of inquiry.json (lines 210, 406, 460).
- Own captures from preview/fy5-6.html?ratkaisut=1, all boxes opened, in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis2-fi-1: fy5-6-les-390-1.png, fy5-6-les-1280-1.png (the sheets also hold the exercise blocks with the same opening).
- Apart from the comma: constant with unit, "· 5,97 · 10²⁴ kg" whole on its row, result row aligned at "="; at 1280 px the product is joined on one row. Nothing clipped, scrollWidth 390 and 1280.

## Scores
illustrations 5 · typography 3 · Finnish 5 · accessibility 4
