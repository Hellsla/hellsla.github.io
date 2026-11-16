VERDICT: PASS
CONTENT-HASH: b7ae6ebc3502f36b
ROUND: 3

## Blocking

## Polish
- [Minor] inquiry.json, hint and Sijoitus of the boom task (390 px) — the row break leaves the `·` at the end of the row, tight against the exponent ("9,81 m/s²·" / "1,50 m · cos 40°"), while every other chapter starts the continuation row with the operator — write `\\ &\quad \cdot 1{,}50\,\text{m}\cdot\cos 40^\circ` as in fy5-2.

## Checked
- Method: preview/fi-easy/fy5-1.html?ratkaisut=1 loaded at 390 and 1280 px, every details box opened and the lazy maths rendered, hidden feedback and model answers revealed; every formula the diff against main changes was located by its TeX and captured in its own block (compact sheets, the rest of the page hidden). No KaTeX error, document scrollWidth equals the viewport at both widths, no changed formula outside its box.
- Opened sheet-fy5-1-390.png, tile-fy5-1-1280-0.png and zoom.png in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis3-easy-1: feedback "F sin 30° = 200 N · 0,5 = 100 N." (two rows, = aligned), the hint and Sijoitus chains for M (boom) and ΣM (steering wheel). At 390 px the continuation rows are indented under the row before; at 1280 px they are joined to one row. Sentence punctuation sits inside the last row, no third column.
- Numbers, signs and units read the same as in the diff; the text around the formulas is unchanged.
- Figures, simulation and the rest of the page not re-opened: unchanged, passed earlier.
- Hash run at the start and at the end: unchanged.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 5
