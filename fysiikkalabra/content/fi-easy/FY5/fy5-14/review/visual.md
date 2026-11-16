VERDICT: PASS
CONTENT-HASH: f06b65d50f5467da
ROUND: 3

## Blocking
(none)

## Polish
- [Minor] inquiry.json 400 (Sijoitus of the Doppler task) — at 390 px the first row is a boxed display (v_L) and the second formula is three unboxed inline pieces ("f = 2000 Hz·" / fraction / "= 2076,8 Hz"), with the multiplication dot tight against Hz; readable and unambiguous, but an aligned display block like the row above would be more even.

## Checked
- Own Playwright captures of preview/fi-easy/fy5-14.html?ratkaisut=1 (every details box opened) at 390 px (2x) and 1280 px, in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis3-easy-13/
- Opened sheet-14-390.png, sheet-14-1280.png (fy5-14-{390,1280}-n2-0) and ctx-14-dop-390.png (the whole Sijoitus step with Vastaus below): f = 2000 Hz · 340 m/s : (340 m/s − 12,566 m/s) = 2076,8 Hz wraps between whole quantities, the dot ends the first piece, no line starts with a bare dot, fraction bar and denominator complete, nothing clipped; one line at 1280 px.
- lesson.md: figure approval marks only, no rendered change.
- Page-wide DOM check at both widths: no overflow, no KaTeX error.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 5
