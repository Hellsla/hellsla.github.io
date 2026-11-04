VERDICT: PASS
CONTENT-HASH: ebb60681fd2ae085

## Blocking

## Polish

## Checked
- One script recomputed every lesson and inquiry number from the task data: 41.7° (water→air at 30°), critical angles 48.8°/41.8°/24.4°/80.57°/42.51°/63.98°/69.98°/38.7°, sim α at θ = 0/10/14/15/30° (90/83.26/80.59/79.93/70.25°), the koe-1 limit 14.03° → 14, siirto 5.743 ms and its mistakes 3.91/2.66/0.0057 ms, virhe 40.6°, v = 2.04·10⁸ m/s, check-2 mistakes 20.02° and 0.9396. All agree.
- The translation keeps every number of the Finnish original (fi vs en multiset of numbers in lesson.md, inquiry.json and exit-ticket.json: identical apart from SVG label-box coordinates); correct flags, initial states, locked parameters and numeric answers are the same.
- Definitions: critical angle, total internal reflection, n1 = incident side, "only when n1 > n2", angles from the normal: stated correctly and the same everywhere (theory, summary, check-1, tarkistus-3, exit ticket).
- Causality: fibre guidance by TIR at the core–cladding boundary (not a mirror); steep entry and tight bends lower α; cladding protects the boundary from water/grease; small Δn limits path-length spread. Correct.
- Fibre facts: ~0.2 dB/km at 1550 nm → half power in ~15 km; amplifier spacing 50–100 km; C-Lion1 1172 km with source. Plausible and sourced.
- Simulation: sim.js implements sin θ = n1 sin θ1, α = 90° − θ1, sin α_r = n2/n1, leaking rays at β from n1 sin α = n2 sin β; en readout/labels translated correctly ("Angle of incidence on the end face θ" = angle to the axis = face normal); dimming said to be illustration only; readings called model values.
- Experiments: koe-1 locks n2 = 1.46 and varies θ; koe-2 locks θ = 30° and varies n2; simState gives alpha and alphar. Experiment capture (en) shows θ = 0°, α = 90.00°, α_r = 80.57°.
- Predictions: exactly one correct option in each; every distractor's feedback is physically right (the air-cladding item correctly says the cladding protects rather than improves reflection).
- Figures: water figure angles 30°/48.8°/65°, graph points to scale, diamond 38° vs 24.4°/41.8° consistent with the text.
- Worked example symbolic first, 3 s.f. justified, real reasonableness check.
