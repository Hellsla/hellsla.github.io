VERDICT: FAIL
CONTENT-HASH: a8a5be11ce98c4fb

## Blocking
1. [Major] Simulation, "Field along the particle" view at 390 (my capture of the sim at 390, field-along view) — with the new 14 px text, the two top label cards run into each other: "time slowed down $2 \cdot 10^7$ times" ends right where "$B_\max = 4.0\ \text{T}$ (ends)" starts. It reads "timesB_max", and the cards overlap. The ink boxes in `simState.labels` do not overlap, so the check script misses it, but the cards do. Students read the field ratio here for Experiment 2. Fix in `sim.js` `drawAlong` (the `panel` calls near line 255): when the left and right top cards would overlap, either put the right card ($B_0$, $B_\max$) under the left one, or shorten the strings to "slowed $2 \cdot 10^7$×" and "$B_\max = 4.0\ \text{T}$". Then check at 360 and 390 with the electron as well.

## Polish
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
