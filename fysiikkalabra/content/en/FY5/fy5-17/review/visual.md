VERDICT: PASS
CONTENT-HASH: 5d4ffba3cf00c11c
ROUND: 3 (delta, work queue 5d: calculations re-broken; en)

## Blocking

## Polish
- [Minor] inquiry.json prediction feedback "Correct. The pulse travels…" — the lifted display block keeps `\tfrac`: fractions render at 14 px and the exponent of `10^{-6}` at 10 px on a phone (measured), small beside the 21 px rows — `\dfrac` in a display block (house rule §1).
- [Minor] error-spotting prompt — at the joins of the quoted chain the space before `=` is missing (`Δt= 2.5 km/s · 20 s= 50 km`); known join spacing.
- [Minor] feedback boxes `vt = … ≈ 0.10 m` — more empty space under the last row than above the first.

## Checked
- fy5-17-390-0/-1/-3.png, fy5-17-1280-0/-1/-3.png, zoom-17-390-1.png: both prediction feedbacks with their display blocks, equals signs in a column, full stop inside.
- ctx-17-virhe-390.png, ctx-17-virhe-1280.png: error-spotting prompt; the quoted chain wraps inside the sentence before `=`, closing quotation mark stays with `50 km.`, no line starts with a bare dot.
- Own Playwright captures of preview/en (`?ratkaisut=1`, every details box opened) at 390 and 1280 px in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis3-en-13/; page scan at both widths: no horizontal overflow, no formula past the viewport, no KaTeX error.

## Scores
illustrations 4 · typography 4 · Finnish 5 · accessibility 5
