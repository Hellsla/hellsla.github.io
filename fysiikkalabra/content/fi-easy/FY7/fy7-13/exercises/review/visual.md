VERDICT: PASS
CONTENT-HASH: 432e64faa918019f

## Blocking

## Polish
- [Minor] solutions.md:163 — the error chain still begins with a bare = after the words "ja virhe"; start it with the quantity, e.g. \text{virhe} = …, as every chain shows what it computes.
- [Minor] solutions.md:237 — on a phone the row "= 1,20 m" is followed by "· tan(…)"; readable, but \bigl( \bigr) are too low for the fraction inside: use \left( \right).

## Checked
- Packet captures have no phone-width opened solutions, so own Playwright captures of the current preview build (preview/fi-easy) at 390 px and 1280 px, every solution open; plus a scripted scan of every formula of the exercise set at 360 and 390 px: none wider than its box, none scrolling, no page overflow.
- The hash changed during the review (f845ee49d7da3de1 → current: commit 7e4ba8466f put the task's quoted formula back inline and re-broke the error chain); preview rebuilt and the review redone for the current hash.
- Delta: 15 re-broken blocks (d conversions, Tarkistus rows, d₁, d₂, x₂ : x₁, x₁ chain) at 390 and 1280 px, full size; 13-15 Sijoitus re-captured after the fix at 390 and 1280: fraction · 100 % on one row, = 5,53 % under it, equals aligned, nothing clipped.
- 13-15 task text (now inline again, as in the version passed earlier): source diff and the 360/390 px scan only, no new full capture of that paragraph. Rest not re-reviewed.

## Scores
illustrations 4 · typography 4 · Finnish 5 · accessibility 4
