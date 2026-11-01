VERDICT: PASS
CONTENT-HASH: 849e390d8423fd52

## Blocking
(none) The blocking finding is resolved. In `heating` the injector box is outside the ring, with its label above it and clear of the band. The arrow and the four fading dots end inside the plasma band, and nothing is drawn in the central hole (seen at 390 and 1280). The four polish items are also resolved:
- The Reasonableness numbers are braced.
- JT‑60 and T‑15 use non-breaking hyphens.
- The text says "million kelvin" throughout.
- The budget title says "(dollars of the time)".

## Polish
1. [Minor] `beam-speed` prompt and Given at 390: "$m =$ / $3.344 \cdot 10^{-27}\ \text{kg}$" and "$1\ \text{eV} =$ / $1.602 …$" break after "=". Fix: brace each whole equality, `{m = 3.344 \cdot 10^{-27}\ \text{kg}}`.
2. [Minor] `machines` table: "Major radius" is right-aligned, so "3.0" does not line up with "2.96". "TFTR (1982)", "JT‑60 (1985)" and "0.85–0.95" wrap at 390. Fix: write 3.0 as "3.00" if the source allows (or align on the decimal point), and put the start year in its own column or under the name with `<br>`.
3. [Minor] Same pill-shaped badge with a long note as in the other units (shared CSS).

## Checked
- Rebuilt; captures regenerated for this hash.
- Own Playwright captures of `hero`, `heating` and `budget` at 390 and 1280. Smallest label 15.5 px. I checked the beam coordinates against the band.
- `machines` table at 390 (fits, 322 of 324 px) and 1280. `beam-speed` with every hint and the solution open at 390.
- No `.katex-error`, no raw `$`, no console errors, no horizontal scroll. Hash unchanged at the end.

## Scores
illustrations 4 · typography 4 · English 4 · accessibility 4

## Re-check 2026-11-01: photographs
- Screenshots at 360, 768 and 1280 px (details opened, image loaded); check_layout.py OK at 360 and 1280 px; figure gaps 20 px above and 24 px below, no overflow, credit on its own line and legible.
- T-15 stamp (portrait) and JET photo fine; JET sits about 35 px above the 'Data: the big machines' card, which is not crowded.
