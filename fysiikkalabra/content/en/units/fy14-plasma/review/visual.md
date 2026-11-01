VERDICT: PASS
CONTENT-HASH: b5b52f45c65467fe

## Blocking
(none) The earlier blocking finding is fixed: the "Explain to a friend" prompt and its model answer now use curly quotes, and the page has no backslashes.

## Polish
1. [Minor] `unit.md`, worked example, **Reasonableness** — the new sentence repeats the one before it: "250 000 times more than the plasma, but the plasma is 500 000 times hotter (…)" and then "The plasma has 250 000 times fewer ions but is 500 000 times hotter…". Fix: drop the first clause and keep only "Air has about $2.5 \cdot 10^{25}$ molecules in each cubic metre at room temperature ($1.5 \cdot 10^{8}\ \text{K} : 293\ \text{K} \approx 500\ 000$)", followed by the new sentence.
2. [Minor] Figure `ionisation` — the red and blue dots are still not named as ion and electron. Add two small labels.
3. [Minor] Figure `pressure` is only 416 px wide at 1280. It could use the full column.

## Checked
- Rebuilt the unit and took new captures for this hash: contact sheets 1–5, top/intro at 390 and 1280, the Check stage, and the theory figures.
- Playwright at 390 and 1280 with all `details` open: no overflow, no `.katex-error`, no raw `$`, no backslashes in the HTML, no console errors. The smallest figure label is 13.7 px at 390.
- The hash was the same at the end.

## Scores
illustrations 4 · typography 4 · English 4 · accessibility 4

## Shared issues
- Known: raw select keys and true/false in experiment tables; the unit repeats in the initial-state line.
- Site font: an italic word followed by a space renders with no visible gap ("mustbe").

## Re-check 2026-11-01: photographs
- Screenshots at 360, 768 and 1280 px (details opened, image loaded); check_layout.py OK at 360 and 1280 px; figure gaps 20 px above and 24 px below, no overflow, credit on its own line and legible.
- Lightning and aurora are 16:9 and read well at every width (185 px tall on a phone); the aurora photo does not crowd the text before it.
