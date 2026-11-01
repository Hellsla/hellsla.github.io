VERDICT: PASS
CONTENT-HASH: c14fd77f3c588c7d

## Blocking
(none) The earlier card overlap is fixed (3735b0fa, 4ec672e4). I rebuilt the unit and checked both views at 360, 390 and 1280: the uniform view for the proton and the electron and with the electric field on, and the field-along view with and without the mirror, for the proton and the electron. No label card overlaps another. A top-right card that would touch the top-left one drops below it, and a bottom-right card that would touch the bottom-left one rises above it. The $\overline{B}$ tag clears the cards, canvas text is 14 px, and there are no page errors.

## Polish
1. [Minor] At 360–390 the moving tags still crowd the particle in some frames. $\overline{F}$ and $\overline{v}$ sit on each other's arrows near the right mirror, $\overline{F}$ touches the $r$ tag in the uniform view, and $\overline{F}_E$/$\overline{F}_B$ bunch together with the electric field on. They stay readable. Treat the arrows themselves as obstacles for the tags.
2. [Minor] Figure `lorentz`: the upper $\overline{v}$ label now sits on a ⊗ field symbol ("⊗v"). Remove that one symbol, or move the label 10 units up.
3. [Minor] Uniform view, electron: the grid scale uses an italic μ ("5 $\mu$m"). Use an upright `\mu\text{m}` or `\text{µm}`.
4. [Minor] The "Electric field" and "Magnetic mirror" checkboxes still sit centred above their labels.
5. [Minor] The along-view bottom-left card still covers the first bottom coil.

## Checked
- Commits cf5a329b and 7561f2b5. New captures for this hash, plus my own 2× captures of the sim at 390 and 1280: uniform view (proton and electron), electric field on, and field-along view with the mirror. Canvas text is now 14 px. The readout equations are slash fractions on separate lines and no longer break at 390. Fixed: the curly quotes in both prompts, the torus label, and the mirror verdict, which is no longer given away in the readout.
- stage-selita-390-1 and -3 (lorentz, mirror and torus figures).
- Playwright: no overflow, no `.katex-error`, no raw `$`, no backslashes, no console errors. The hash was the same at the end.

## Scores
illustrations 4 · typography 4 · English 4 · accessibility 3

## Shared issues
- Known: raw select keys and true/false in experiment tables, and the unit repeats in the initial-state line.
- Italic-space rendering in the site font.
