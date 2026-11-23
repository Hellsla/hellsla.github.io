VERDICT: PASS
CONTENT-HASH: 5b106266d8d24ded

## Blocking
None.

## Polish
- Line 104: the table headers still use a plain space, `$m\ (\text{kg})$` and similar. The unit-expression change did not cover them. This is typography only.

## Checked (gate 2026-11-23)
- Working-tree diff (`git diff HEAD`): two lines in investigation.md. `$k = (k \pm \Delta k)\ \text{N/m}$` became `\,\text{N/m}$` in "Epävarmuus ja luotettavuus" and in the report checklist. The bracketed value, the ± uncertainty and the N/m unit are unchanged and correct. No other physics, formula or number changed. investigation.json and teacher.md are unchanged.
- Committed changes since the earlier PASS (57de8ab9a6..HEAD). The vector drawing in the hero and setup figures was replaced by teacher-approved webp images (`assets/pics/fy10/`). All TeX labels and the aria-label stay. I looked at the setup image:
  - It shows the unloaded spring $l_0$ and the loaded spring $l$, with the extension $x$ measured from the dashed $l_0$ level to the bottom of the loaded spring.
  - On the body at rest, $\overline{F}$ points up from the spring's attachment point and $\overline{G}$ points down from the centre. Both arrows are about the same length (equilibrium), and there are no extra forces.
  - The label positions match the arrows and the dimension bars.
  - It agrees with the text ($F = G = mg$, Newton III for the force pulling the spring).
- I relied on the earlier full and delta reviews for everything else: $F = kx$ slope, the length-axis offset, swapped axes giving slope $1/k$, preload intercept, and the handling of the weight hanger.
