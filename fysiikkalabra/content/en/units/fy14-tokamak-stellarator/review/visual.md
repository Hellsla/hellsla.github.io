VERDICT: PASS
CONTENT-HASH: 4d4c220db142d2dd

## Blocking
(none) The earlier blocking finding is fixed: the feedback and the "Find the error" prompt now use curly quotes. The toroidal figure's radius dots are larger and easy to find at 390.

## Polish
1. [Minor] Inline `\frac` still makes small, cramped fractions in Check 2 and in the Apply hint and reasonableness line, e.g. $B = \frac{\mu_0 N I}{2\pi R}$. Write them as $B = \mu_0 N I/(2\pi R)$.
2. [Minor] Reactors explorer, stellarator view: the coil swatch still includes the grey ring-coil colour, which this view does not use. The three green field layers differ only by dash pattern (shared component).
3. [Minor] Respelling style: "luh SHAHN mah-nyay-TEEK" here but "luh shahn mah-nyay-TEEK" in *Charged particles*.

## Checked
- New captures for this hash: contact sheets, top/intro at 390 and 1280, stage-selita-390-1 (toroidal figure), fx-1 (tokamak) at 390 and 1280, the Investigation 2 table, and the Check stage. The stellarator view with every layer on was checked earlier this session; this commit did not change that component.
- Playwright at 390 and 1280: no overflow, no `.katex-error`, no raw `$`, no backslashes, no console errors. Figure labels are 15.4 px at 390.
- The hash was the same at the end.

## Scores
illustrations 4 · typography 4 · English 4 · accessibility 4

## Shared issues
- Known: raw select keys and true/false in experiment tables; the unit repeats in the initial-state line.
- `assets/units/fy14/fx/reactors.js`: the stellarator legend swatch and the same-green layers.

## Re-check 2026-11-01: photographs
- Screenshots at 360, 768 and 1280 px (details opened, image loaded); check_layout.py OK at 360 and 1280 px; figure gaps 20 px above and 24 px below, no overflow, credit on its own line and legible.
- W7-X coil and WEST chamber fine; at 360 and 768 px the caption wraps inside 'Wendelstein 7-X' ("7-" / "X"), cosmetic only.
