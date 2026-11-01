VERDICT: FAIL
CONTENT-HASH: 78ca43a94673e3d9

## Blocking
1. [Major] `inquiry.json` lines 371 and 489 — literal backslashes in task prompts: `A student writes: \"An electron and a proton …\"` and `A younger student asks: \"Why are fusion machines shaped like a doughnut …?\"`. The JSON has `\\\"`. Fix: use `\"` or typographic quotes “ … ”.
2. [Major] `assets/sims/fy14/magnetic/sim.js` line 108 `fh = Math.round(12 * k)` — all canvas text (grid scale, slow-down, $\overline{B}$ panel, particle name, $r$, the $\overline{v}$/$\overline{F}$ tags) renders at about 11.9 CSS px at 390 (canvas 324 px) and 12 px at 1280. This is below the 14 px house rule (developer-brief, "Simulation canvas text ≥ 14 px"), and these labels carry the scale students must read in Experiment 1. Fix: `fh = Math.round(14 * k)`, as in the photoelectric sim, and check that the panels still fit.
3. [Major] Simulation readout (`strings.json` `lukemat`, `lukemat2`, `lukemat_E`, `lukemat_peili`; `sim-390-1`, my capture `simroot-along-390`) — inline `\dfrac` makes tall lines, and at 390 the equalities break in the middle: "$f =$ / $\frac{1}{T} = 15.2$ MHz", "$v =$ / $2.00 \cdot 10^6$", "$v_\perp =$ / $v\sin\theta$", "$\sin^2\theta \geq$ / $\frac{B_0}{B_{\max}}$". These are the readings students record. Fix: no `\dfrac` inline. Write $r = mv/(|q|B)$, $T = 2\pi m/(|q|B)$, $f = 1/T$, $B_0/B_{\max}$, wrap each equality in braces `{r = … = {{r}}}` so KaTeX does not break inside it, and put r, T and f on separate lines.

## Polish
4. [Minor] Sim, field-along view — the bottom-left label card ("proton, q = +e / θ = 45°") covers the first bottom coil, which shows through it (`simroot-along-1280`). Fix: lift the panel above the coil row or make the card opaque.
5. [Minor] Sim controls — the "Electric field" and "Magnetic mirror" checkboxes sit centred above their labels instead of beside them, at both widths. Fix: put the checkbox inline before the text.
6. [Minor] Figure `torus` (`stage-selita-390-3`) — the label "a ring: no ends" is overlapped by the bottom coil of the ring. Move it about 10 units down.
7. [Minor] Figure `lorentz` — the white box of the upper $\overline{v}$ label clips the arrowhead (it reads "(v"). Move the label 8 units right.
8. [Minor] Apply task solution, **Given** at 390 — "$m =$ / $6.645…$" and "$2 \cdot$ / $1.602$" break after the operator. Wrap each equality in braces.

## Checked
- Fresh captures for this hash: contact sheets; top/intro; sim-390-1/-2. My own 2× captures of the canvas (uniform field, the E field on, the field-along view with the mirror) at 390 and 1280, and the canvas width measured (324 px at 390). Colours: v blue, F red (F_E red dashed), B green, E purple, as required.
- stage-selita-390-1/-2/-3 (lorentz, mirror and torus figures); the worked example and the Apply solution (`stage-sovella-390-2`); the ordering task; the French corner; sources.
- Playwright: no overflow, no `.katex-error`, no raw `$`, no console errors. The hash was the same at the end.

## Scores
illustrations 4 · typography 3 · English 4 · accessibility 3

## Shared issues
- Known: raw keys (p/d/e/a) and true/false in experiment tables; the unit repeats in the initial-state line.
- Italic-space rendering (site font/CSS): "alongit", "whymagnetic".
