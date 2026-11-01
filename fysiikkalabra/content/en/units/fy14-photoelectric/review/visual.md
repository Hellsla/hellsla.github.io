VERDICT: PASS
CONTENT-HASH: 416657015f0d3d08

## Blocking
(none) All four earlier blocking findings are resolved:
- The beam now comes from above the gap and lights the cathode's inner face, where the electrons leave.
- The canvas labels are 14·k, about 13–14 CSS px at 390 and 1280, with no overlaps.
- Every experiment column has its unit.
- The reflection list renders the maths and has a space after the scenario.

## Polish
1. [Minor] Experiment set-up line (`inquiry.json` `names`, captures `stage-tutki-1280-1`, `stage-tutki-390-3`). Putting the units into the names repeats them: "wavelength λ (nm) = 650 nm", "voltage U (V) = 0 V", and "Kept constant: intensity (%)". Fix: keep the names without units and let the experiment builder add `(unit)` from `units` to the table header only.
2. [Minor] Reflection list (`back-to-predictions`, `stage-selita-390-7`). The quoted prediction prompts are long, three to five lines in small type. Acceptable, but the shared component could quote only the `.ask` part.
3. [Minor] planck-data **Reasonableness**: "$h \approx$ / $6.60 \cdot 10^{-34}…$" still breaks after ≈ at 390. Wrap it in braces like the other inline equalities.
4. [Minor] $U_\text{s}$–$f$ graph at 390: the sodium $f_0$ label sits close to the first data point. Move it 6–8 units left or down.

## Checked
Fresh build and captures for hash 32f7650573683cf9: top/intro at 390 and 1280, every stage at 390 and 1280, sim-390-1 (zoomed), sim-1280-1 (labels zoomed), fx-1/2, sources, teacher. The energy diagram ("free electron" level, 24-unit labels) and the $U_\text{s}$–$f$ graph ($f_0$ marks, line over the points, `slope = h/e`) at both widths. I recaptured the worked example with all seven steps: step 6 is now a single sentence. I also recaptured the planck-data task with hints and solution open: inline $(h/e)\,f - W/e$, and a display substitution that fits 390. The French corner tips now share one respelling convention. Hash unchanged at the end.

Re-check for b0acda37ffbeec0d (commits 4ec672e4 and ba143d0c): I rebuilt the unit and captured the sim canvas at 360, 390 (2×) and 1280. The "$I = 12.0\,\text{nA}$" label now sits fully inside the canvas at every width and clears the wire, the ammeter and "collector". No page errors and no horizontal overflow. `test_sims` passes at 360, 390 and 1280. The Fotoni sentence now says "LEDs of different colours" and reads well. Hash unchanged at the end.

## Scores
illustrations 4 · typography 4 · English 4 · accessibility 4

Re-check 2026-11-01: the "Find the error" aligned block now fits at 360/390 px with no overflow or KaTeX errors.
