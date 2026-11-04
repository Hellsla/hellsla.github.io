VERDICT: DONE
Draft completed from the files an interrupted developer left behind (kept: lesson text, inquiry, exercises 5/4/3, solutions, answers.py, lesson-answers.py, figures.py, sim.js, lang and glossary keys).

- lesson.md: figures written in from figures.py; the worked example's Sijoitus starts from the symbolic formulas ($A = aL$, $P = P_0 \cdot 10^{-A/10\,\text{dB}}$).
- figures.py: empty field-line paths skipped (console error); induction-hob field lines redrawn as closed loops around each side of the coil; eddy-current label moved off the pan wall.
- sim.js: axis title and transmitter label inside the canvas at 360 px; labels get a background so field lines never cross them; "puhelin" and "laturi" moved off the axis and the coil wires.
- sim-spec.md and tests/sims/fy7-16.json (21 assertions: load state, sliders, DOM order, legend, adapter, Φ0, e0 at five distances and three radii, the share, field-line counts, readout and slider labels) written; expected values from lesson-answers.py's model.
- exercises.json, solutions.md: `{}^\circ\text{C}` (KaTeX parse error); L3-02 solution trimmed under 220 words.
- inquiry.json: siirto substitution as a colon chain (overflowed at 340 px); option lengths balanced in ennuste-kattila and check-1.

Not done here: `figcat.py build` (catalog under docs/), en/fi-easy sim strings (translation stage).
