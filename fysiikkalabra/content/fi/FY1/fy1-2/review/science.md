VERDICT: PASS
CONTENT-HASH: 3b3df2a745260fbd

## Blocking

## Polish
- assets/sims/fy1/fy1-2/sim.js:997,1000 — at the start (view centre on the Sun, d = 0) the slider label reads $d = 10^{6{,}00}\,\text{km}$ and the bottom-bar marker sits at $10^6$, while the readout says $d = 0\,\text{km}$: two different d values at once. Not on any experiment's path (koe-1 starts at n = 7). Fix: when nView < N_MIN, show the label as "$d < 10^{6}\,\text{km}$" (or hide the exponent).
- inquiry.json simulaatio.model, voyager-malli.source_note, sim.js:855 — d0 = 119,0 AU (Burlaga et al. 2019) differs from the teacher's brief (119,7 AU, which "gives about 143 AU for February 2026"). The physics favours 119,0 AU: it is the published crossing distance, and the lesson explains the 0,5 AU gap to JPL's 143,05 AU as the Earth–Sun offset, which is correct. Fix: none in the physics; the coordinator should let the teacher know the brief's value was replaced.
- inquiry.json voyager-malli.source_note — the text says JPL's 143,05 AU is the distance *from Earth*. I could not check this offline. The geometry fits it: in February Voyager 2 lies roughly in the Sun's direction, so Earth is about 0,7 AU farther from the probe than the Sun is, and the model gives 142,4 AU from the Sun on 1.2.2026. Fix: confirm the label against the JPL page.
- lesson.md:116 aria-label "1 cm on 40 yksikköä" — the tick labels sit 77,4 units per 2 cm (38,7 per cm). A 3 % gap, not visible. Fix: say 38,7, or drop the number.

## Checked
- I recomputed every number in one script: worked example (4,503·10⁹ km, 1,502·10⁴ s, 4,17 h), 1 AU/c = 499 s = 8,32 min, area 1,702 m², ennuste-2 (33,4 / 3340 s, 56 min), 7,2 AU per hour, 1212 AU per week, 63 000 AU per light year.
- Voyager model values with d0 = 119,0 AU and v = 15,341 km/s: 2018/2022/2026/2030 give 119,0/131,9/144,9/157,8 AU, 1,78–2,36·10¹⁰ km and 16,5–21,9 h. 1.1.2026 gives 142,2 AU, 19,7 h and a ratio of 142. February 2026 gives 142,4–142,7 AU. All match the text.
- Solar slowing over 2018–2026: Δv ≈ 0,08 km/s from energy conservation, so "noin 0,1 km/s" holds. The Earth offset of at most 8 min is right.
- siirto: 3,236 AU/a, with the 4,842·10⁸ km and 3236 mistakes. tarkistus-2: 3,22 min, with the 193 s and 0,0536 h mistakes. check-c2: 79 min, distractor 0,87 min.
- Exactly one correct option in each choice item. Every distractor is wrong and its feedback explains why. The significant-figure rules match the glossary and NOTES §2.
- koe-1: the adapter's `n` sets the view to 10^n km, and `dAU` and `tLight` come out as 0,0668…6,68 AU and 33,4…3340 s. The date is locked and has no effect. koe-2: `vAU` and `vTh` depend only on `pvm`. Both experiments isolate their varied parameter.
- Sim scale: Sun 401 px, Earth 3,7 px, Neptune 1,29·10⁶ px, c = 86,3 px/s, Moon 110,7 px from Earth. The pace setting changes only the animation, as stated.
- Limits are stated: planets on one line, a magnified probe marker, model values rather than measurements, signal time measured from the Sun.
- Definitions are right: SI base quantities, kilogram via the Planck constant, AU as a defined length, light year as a length, prefixes. Hydrogen-atom and proton sizes are right. Scope stays inside FY1 (s = ct only).
- Exit ticket conversions (4200 m, 500 µm) and the explain model answers agree with the theory.
