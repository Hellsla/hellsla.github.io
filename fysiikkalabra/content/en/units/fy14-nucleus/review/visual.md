VERDICT: PASS
CONTENT-HASH: 32e35f45c81f307f

## Blocking
(none)

## Polish
1. [Minor] Worked example, step 1 *Given* (`unit.md`, 390 px). The line breaks after "mass $m =$", so the value starts the next line. Step 4 *Unit conversions*: the inline chain $r_0 = 1.2\ \text{fm} = 1.2 \cdot 10^{-15}\ \text{m}$ wraps into a two-line block that splits the sentence. Fix: wrap each inline equality in braces (`${m = 9.29 \cdot 10^{-26}\ \text{kg}}$`, `${r_0 = … = 1.2 \cdot 10^{-15}\ \text{m}}$`), as in the photoelectric unit.
2. [Minor] Isotope Builder readout at 390 (shared `fx/isotopes.js`). "Mass number $A = Z +$ / $N = 1 + 0 = 1$" breaks inside the equation. Fix: put the equation in braces, or on its own line under "Mass number".
3. [Minor] Figure `notation` (390 and 1280). The $14$ and the $6$ sit about 10 units left of the "C", so they read a little like separate numbers. Fix: move both 6–8 units right so that they hug the symbol, as in printed notation.
4. [Minor] Figure `ranges`. The white "electric force: repels" ends where the gradient becomes pale. It is readable, but the contrast is lowest on "repels". Fix: end the label about 30 units earlier, or keep the gradient darker until x ≈ 420.

## Checked
- Fresh build and captures for this hash: top/intro at 390 and 1280, every stage at 390 (contact sheets 1–2), and the 1280 stages (contact sheets 3–4).
- I captured each figure myself at 390 and 1280: the hero (no text, the magnified nucleus is clear), `hydrogen`, `notation` and `ranges` (the 0.7 and 2.5 fm bar ends and the 9.2 fm bracket are to scale). The smallest label is 15.5 px at 390.
- Worked example with all seven steps at 390. Coulomb solution and hints open.
- Isotope Builder at the start, at ⁵⁶Fe (56 balls, isotope chips wrap cleanly) and at 2p + 0n. The match and say components.
- Measured with Playwright at 390 and 1280: no `.katex-error`, no raw `$`, no horizontal overflow, no console errors. No display equation is wider than its box.
- French corner: `lang="fr"` and the respellings are consistent with the other units. The hash was the same at the end.

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 4
