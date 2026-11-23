VERDICT: FAIL
CONTENT-HASH: 5512292a4a3afd87

## Blocking
- [Major] solutions.md Kaava lines of L1-05, L2-03, L2-04, L2-05, L2-07, L2-08, L3-02, L3-04 (every changed Kaava chain; `grep -n '^\*\*Kaava' | grep '\\frac'`) — the edited chains were written with `\frac` in inline maths, so the page sets them in text style: numerators and denominators are tiny, subscripts such as λ_0, v_A, d_B and the λ_nyt fraction shrink to near-illegibility next to the full-size fractions in the Sijoitus rows (captures open-exercises-L2-1280-4, L2-1280-5, 1280-1) — the Kaava is the formula the student should read first, and the previous version used `\dfrac` here — change `\frac` to `\dfrac` in these inline chains (NOTES §1: `\tfrac` only for short inline references, a displayed or row-split chain uses `\dfrac`). Fix by search and replace in the changed Kaava lines.

## Polish
- [Minor] exercises.json 16-13 (student's solution) — the closing quotation mark and full stop ".”" sit alone on a line after the display block (open-exercises-L2-1280-5); put the closing words inside the same paragraph or end the quote before the block.
- [Minor] solutions.md 16-14 Kaava — "z = (λ−λ_0)/λ_0" stands alone in a box above a second block; combine into one block.

## Checked
- Delta (Kaava step re-set as short aligned chains). Opened contact-6, and at full size open-exercises-L2-1280-4 (16-13: rows with small fractions), open-exercises-L2-1280-5 (16-14: tiny z fraction, then three-row block); the L1-05 and 16-11 blocks seen on the contact sheet show the same small fractions.
- Everything else (Sijoitus rows, Vastaus, Järkevyys, units) is clean and aligned.
- No 390 px capture with solutions open.

## Scores
illustrations 4 · typography 3 · Finnish 5 · accessibility 4
