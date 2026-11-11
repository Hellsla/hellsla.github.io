VERDICT: PASS
CONTENT-HASH: 09da6a2ea3b09622

## Blocking
None.

## Polish
- inquiry `menetelmat`: the list opens "No size in the simulation…" and gives "Nearest star, $4.0\cdot10^{16}\,\text{m}$: … parallax". Parallax measures a distance, so "Distance to the nearest star" would match the corrected sim label.
- sim-spec.md says objects show from about 1/2000 of the view, while the `calc` box says 1/1000. The code (fade-in about 0.25–0.7 px, visible at $a \ge 0.5$) supports about 1/1000. Only the spec is off, and students never see it.
- `tunnista` black-hole feedback: "about three solar masses or heavier" is fine at this level, because the lightest candidates are about $2.5$–$3\,M_\odot$.

## Checked
- Round 2: the round-1 blocking finding is fixed. `lang/en.json` `sims.fy1-1.o_proxima` is now "distance to Proxima Centauri", which matches the Finnish source. The fix is commit b40c5573, which touches only `lang/en.json` and `lang/fi-easy.json`. The content hash is unchanged at `09da6a2ea3b09622` (the lang texts are outside the hash), so the readout now reads "Object closest in size: distance to Proxima Centauri, size $4.0\cdot10^{16}\,\text{m}$".
- Round 1 (the lesson files are unchanged): I recomputed every number with my own script. Example $k = 6.47\cdot10^{4} \to 6.5\cdot10^{4}$; exp-1 Δn 5; exp-2 Δn 8; exp-3 midpoint −4, which matches hair (`kohdeExp` −4); siirto $d = 1.273\cdot10^{4}\,\text{km}$; check-2 $5.79\cdot10^{4}$; check-1 $10^{17}$; Sgr A* $2.54\cdot10^{10}\,\text{m}$; $F_e/F_g$ for two protons $1.2\cdot10^{36}$; 93 billion light-years; Sun/Earth 109; 42 and 62 orders of magnitude. All agree.
- Sim: at the initial L of each experiment, `mainObj` gives the object its intro names. `kohdeExp = round(log10 m)` is the same as the $\sqrt{10}$ rule, the object sizes are sound, and the model box states the limits.
- Figures: the scale-axis and object-types positions are to scale (checked from the SVG coordinates), and the cosmic-address orders are correct.
- Theory, choice items, feedback, exit ticket and model answer: no A or B findings. Each choice item has exactly one correct option, and the lesson stays within FY1 scope.
