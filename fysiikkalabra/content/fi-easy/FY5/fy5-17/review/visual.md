VERDICT: PASS
CONTENT-HASH: 7e385919934cd7f9
ROUND: 3

## Blocking
(none)

## Polish
- [Minor] inquiry.json 63 — in the display block the substitution row still uses \tfrac, so "1540 m/s·65·10⁻⁶ s" over 2 is set in script size inside a display; \dfrac would read better on a phone.
- [Minor] inquiry.json 257 — uneven spacing at the inline join ("20 s= 50 km"); known from the brief.

## Checked
- Own Playwright captures of preview/fi-easy/fy5-17.html?ratkaisut=1 (every details box opened) at 390 px (2x) and 1280 px, in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis3-easy-13/
- Opened sheet-17-390-b.png, sheet-17-1280-b.png (fy5-17-{390,1280}-n14-0, n15-1), fy5-17-390-n16-0.png, ctx-17-quote-390.png and ctx-17-quote-1280.png.
- Feedback block vt = 1540 m/s · 65 µs / ≈ 0,10 m and d = vt/2 / = … / ≈ 0,050 m.: aligned, complete, the sentence continues below the block.
- The quoted student line "joten d = (v_P − v_S) Δt / = 2,5 km/s · 20 s = 50 km.”" wraps inside the quotation at both widths, the closing quote stays with the formula, no line starts with a bare dot.
- Page-wide DOM check at both widths: no overflow, no KaTeX error.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 5
