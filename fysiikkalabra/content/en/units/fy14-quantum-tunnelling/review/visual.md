VERDICT: FAIL
CONTENT-HASH: d2a9fd877ad07dac

## Blocking
1. [Major] Graph *Tunnelling and the Sun* (`figures.py` `sun_barrier()`, the `GOOD_LIGHT` strip below 2 fm; my 2× capture at 390). The green strip shows where the strong force can join the protons, but no label on the page says so: only the aria-label does. The graph exists to show the gap between the turning point at 1060 fm and that range, and colour alone carries this meaning. Fix: label the strip in the figure, for example `\text{strong force}` set vertically inside it, or "fusion range" above it at `ax.Y(3.6)`.

## Polish
2. [Minor] Worked example, **Reasonableness** (my captures at 390 and 1280). "Units: $\text{C} \cdot \text{V} = \text{J} = …$ so the square root gives …" is shown as a display box in the middle of the sentence. Fix: give the unit chain its own display line after a full sentence ("Check the units:"), then start a new sentence with "So the square root gives …".
3. [Minor] Units in the substitution: "$\text{kg}^2\text{m}^2/\text{s}^2$" has no `\cdot` between kg² and m², while the next line has "$\text{kg} \cdot \text{m/s}$". Fix: `\text{kg}^2 \cdot \text{m}^2/\text{s}^2`. The same applies in the proton task's solution.
4. [Minor] Headings: "the de Broglie wavelength" renders in lower case, because the template drops "Formula:". Fix: `## Formula: The de Broglie wavelength`.
5. [Minor] Figures:
   - In `barrier()`, the grey "$E$" label sits on the incoming wave, and the barrier height has no label. Fix: move $E$ to the right end of the dashed line (`x = 576`, "end"), and label the barrier's top edge `\text{barrier top}`.
   - In `sun_barrier()`, the top tick reads "$10^4$" while the others read 1000, 100 … Fix: write `10\,000` or use powers of ten on every tick.
6. [Minor] **Given** at 390 breaks "$e =$ / $1.602 …$" and "$h = 6.626 \cdot$ / $10^{-34}$". Fix: wrap each equality in braces.

## Checked
- Stamp current. Captures: top and intro at 390 and 1280, every stage at 390 and 1280, contact sheets 1 and 4, including the French corner at 1280.
- My 2× captures at 390 of all four figures (the hero has no text; the simulated double-slit panels are labelled "simulated"), and the worked example with all steps open at 390 and 1280.
- In Playwright: the smallest label is 14.3 px at 390 and 16.6 px at 1280. No `.katex-error`, no overflow, no console errors.
- The French respellings use *õ*/*ã* consistently and are correct. Hash unchanged at the end.

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 3

## Shared issues
- Long inline formulas are turned into display boxes in the middle of a sentence (see fy14-atom-models visual.md).
