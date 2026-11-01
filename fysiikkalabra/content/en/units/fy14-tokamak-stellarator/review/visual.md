VERDICT: FAIL
CONTENT-HASH: 398b2cfa18a413c4

## Blocking
1. [Major] `inquiry.json` lines 151 and 249 — literal backslashes in student-facing text. They appear in the feedback "You divided the older duration by the newer one. \"How many times longer\" …" (Investigation 2) and in the optional "Find the error" prompt `A student writes: \"The toroidal field coils … heat the plasma.\"` (contact #16). The JSON has `\\\"`. Fix: use `\"` or typographic quotes “ … ”.

## Polish
2. [Minor] Inline `\frac` makes small, cramped fractions in running text: Check 2 "The toroidal field is $B = \frac{\mu_0 N I}{2\pi R}$", hint 2 of "Apply: the field at the inner edge", and the reasonableness line `5.29 T · \frac{6.2}{4.2}`. Fix: write them inline as $B = \mu_0 N I/(2\pi R)$ and $5.29\ \text{T} \cdot 6.2 : 4.2$, as the theory summary already does.
3. [Minor] Reactors explorer, stellarator view (my capture at 390 and 1280) — the coil legend swatch still shows the grey ring-coil colour, which the stellarator drawing does not use. The toroidal, poloidal and helical layers differ only by dash pattern in one green, so they are hard to tell apart at 390. Fix: a view-specific swatch, and a thicker stroke for the helical line.
4. [Minor] Figure `toroidal` (`stage-selita-390-1`) — the three leader lines converge on closely spaced dots. Fine at 1280; at 390 the 4.2 m dot is hard to find. Fix: give the dots 1.5× the radius.
5. [Minor] Respelling style: "luh SHAHN mah-nyay-TEEK" here but "luh shahn mah-nyay-TEEK" in *Charged particles*. Pick one.

## Checked
- Fresh build and captures for this hash: contact sheets; top/intro at 390 and 1280; fx-1-390-1/-2 (tokamak drawing, steps, comparison table); my own captures of the stellarator view with every layer on at 390 and 1280; stage-selita-390-1 (toroidal figure); Investigation 2 table and solution; Check stage; French corner.
- Playwright at 390 and 1280: no overflow, no `.katex-error`, no raw `$`, no console errors. The toroidal figure labels are 15.4 px at 390. The hero has no text. B is green throughout, and the plasma current is purple.
- The hash was the same at the end.

## Scores
illustrations 4 · typography 4 · English 4 · accessibility 4

## Shared issues
- Known: raw select keys and true/false in experiment tables; the unit repeats in the initial-state line.
- `assets/units/fy14/fx/reactors.js` (shared): the stellarator legend swatch and the same-green layers (Polish 3).
- Italic-space rendering (site font/CSS).
