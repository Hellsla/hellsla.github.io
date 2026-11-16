VERDICT: FAIL
CONTENT-HASH: c4409c2610f0920b

## Blocking
- [Major] inquiry.json:305 (etsi-virhe prompt; captures fy5-5-les-390-1, fy5-5-les-1280-1) — the sentence's full stop floats far to the right of the last row: "≈ 4400 m/s²          ." (about 80 px at 390 px, 180 px at 1280 px). The last row ends with the trailing `&` and the mark after `$$` is set behind it in a third alignment column — a lone dot in the box of the very formula the student must inspect for an error looks like part of the puzzle — put the mark before the `&` (`&\approx 4400\,\text{m/s}^2\text{.} & \end{aligned}$$ Mikä…`, or fix mathlayout.with_punct for every such block).

## Polish
- [Minor] inquiry.json:305 — the `\tfrac` mass-over-distance fraction is small at 390 px but legible (carried from the previous round).

## Checked
- Delta: the one re-broken chain, inquiry.json:305.
- Own captures from preview/fy5-5.html?ratkaisut=1, all boxes opened, in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis2-fi-1: fy5-5-les-390-1.png, fy5-5-les-1280-1.png.
- The chain now fits at 390 px (right edge 302 of 349 px, earlier it overflowed); rows start at a relation or at "·" before a whole quantity; at 1280 px the constant and the fraction are joined on one row. scrollWidth 390 and 1280.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 4
