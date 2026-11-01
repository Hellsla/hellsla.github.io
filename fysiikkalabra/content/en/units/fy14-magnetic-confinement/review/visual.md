VERDICT: PASS
CONTENT-HASH: c5fef9077a48f7ca

## Blocking
(none) Fixed in 3735b0fa: in the "Field along the particle" view, the top-right card ($B_0$, $B_\max$) now drops under the top-left card when they would touch. I checked at 360, 390 and 1280, with and without the mirror, for the proton and the electron. No cards overlap, all text is 14 px and readable, and there are no page errors.

## Polish
1. [Minor] At 390 the dropped $B_0$/$B_\max$ card sits close to the $\overline{B}$ tag and to the particle's arrows when the particle is near the right end. Their tags stay readable. Placing the dropped card at the lower right, above the reflections card, would keep it clear of the orbit.
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
