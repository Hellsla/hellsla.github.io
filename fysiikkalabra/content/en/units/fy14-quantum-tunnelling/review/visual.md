VERDICT: FAIL
CONTENT-HASH: 52dad39318ce6af1

## Blocking
1. [Major] Worked example, **Substitution** (`unit.md` line 3552; my capture at 390 with all steps open). With the new `\cdot`, the line $p = \sqrt{2.919 \cdot 10^{-47}\ \text{kg}^2 \cdot \text{m}^2/\text{s}^2}$ is 10 px wider than the box (`scrollWidth` 347 > 337). The end of the radicand, "/s²", is cut off at the right edge, and a student on a phone sees an incomplete unit. Fix: break the line at the relation sign:
   `p &= \sqrt{2mE_\text{k}} \\ &= \sqrt{2.919 \cdot 10^{-47}\ \text{kg}^2 \cdot \text{m}^2/\text{s}^2} \\`
   That is still about 330 px wide (the proton task's solution, opened, does not overflow). Better, drop the unit inside the root and state it once: `p &= \sqrt{2.919 \cdot 10^{-47}}\ \text{kg} \cdot \text{m/s}`.

## Polish
(none) The earlier Polish items are all resolved:
- **Strong-force strip.** It is labelled "strong force" with an arrow (earlier Blocking 1).
- **Unit chain.** It is its own display line after "Check the units:", and the next sentence starts "So …".
- **Units.** They are written kg² · m²/s².
- **Heading.** It reads "The de Broglie wavelength".
- **Barrier figure.** $E$ sits at the right end of the dashed line, and "barrier top" is labelled.
- **Top tick.** It reads 10 000.
- **Given line.** Its equalities are braced.

## Checked
- Fresh captures for this hash (stamp current):
  - top and intro at 390 and 1280;
  - every stage at 390 and 1280.
- My 2× captures at 390 of all four figures, and the worked example with all steps open at 390 and 1280, the overflowing line zoomed.
- In Playwright at 390 and 1280:
  - smallest label 14.3 px;
  - no `.katex-error`, no page overflow, no console errors;
  - one display box overflows, at 390 only (above).
- The French respellings are in italics, with the convention sentence. The hash is unchanged at the end.

## Scores
illustrations 4 · typography 3 · English/French 4 · accessibility 4
