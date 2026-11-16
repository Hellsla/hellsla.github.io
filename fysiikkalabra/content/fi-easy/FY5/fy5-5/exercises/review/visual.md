VERDICT: PASS
CONTENT-HASH: 436ddffb540ec372
ROUND: 3

## Blocking

## Polish
- [Minor] solutions.md, fy5-5-L1-01 Sijoitus — the inline pieces mix a small unit fraction with a full-size `\dfrac`, and the joins before `=` are tight ("F= 6,674 …", "10⁻⁷ N= 0,4015 µN" at 1280 px) — known spacing of the inline split; a display `aligned` block would read better if the line is touched again.
- [Minor] the same line and the Vastaus — the prefix in "µN" is italic (`\mu`); an SI prefix is upright (not from this diff).

## Checked
- The hash changed during the review (c915c6266e753003 at the start, 436ddffb540ec372 after the L1-01 Sijoitus was split before its first `=`), so the review was redone on the current content: the diff against main is that one Sijoitus line, now five inline formulas ($F$ | $= 6{,}674 … \cdot$ | the fraction | $= 4{,}015 \cdot 10^{-7}\,\text{N}$ | $= 0{,}4015\,\mu\text{N}$).
- preview/fi-easy/fy5-5.html?ratkaisut=1 (rebuilt after the edit) loaded at 390 px (dpr 2) and 1280 px, every details box opened, lazy maths rendered; no KaTeX error, document scrollWidth equals the viewport.
- Opened /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis3-easy-1/fy5-5-L1-01-sijoitus-390.png and fy5-5-L1-01-sijoitus-1280.png: at 390 px three lines ("F = 6,674 · 10⁻¹¹ N·m²/kg² ·" / fraction "= 4,015 · 10⁻⁷ N" / "= 0,4015 µN"), the `·` ends the first line, no line starts with a bare dot, no quantity is split, nothing leaves the solution card; at 1280 px one line. Muunnokset above and Vastaus below are intact.
- Also opened tile-fy5-5-390-0.png and tile-fy5-5-1280-0.png (same folder) for the neighbouring solution blocks: layout as passed.
- Hash run again at the end: 436ddffb540ec372.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 5
