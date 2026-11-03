VERDICT: PASS
CONTENT-HASH: 19fd05af9f6a8264

## Blocking
(none)

## Polish
(none)

## Checked
- Translation judged against content/fi/FY5/fy5-13 (three PASS reviews): lesson.md, inquiry.json, exit-ticket.json, meta.json, figures.json, lang/en.json sims.fy5-13.
- Every number in lesson.md, inquiry.json and exit-ticket.json compared by script with the Finnish (decimal comma to point): identical; check_i18n reports no formula, answer or option difference for fy5-13.
- Formulas identical: L = nλ_n/2, λ_n = 2L/n, f_n = n·v/(2L) = n f_1 (n = 1, 2, 3, …), closed tube L = nλ_n/4, f_n = n·v/(4L) (n = 1, 3, 5, …); worked example v = 2Lf_1 = 143 m/s, L' = 0.433 m; didgeridoo f_3 = 170 Hz; Tarkista 2 λ_3 = 0.80 m.
- Every prediction's correct option (200 Hz; 300 Hz), all feedback, experiment settings (L = 0.60 m, v = 120 m/s; closed and open tube 0.85 m), mistakes, hints and explain model answers keep the Finnish physics.
- Fixed by me: prediction 2 option 150 Hz feedback now says only the odd multiples of the fundamental frequency are natural frequencies (no wrong "whole-number multiples" claim).
- Node/antinode letters now N and A everywhere in English (sim labels, legend, howto, figures via figures.json S→N, K→A, figure description); no reference to Finnish letters remains.
- Terms: standing wave, node, antinode, natural frequency, fundamental frequency, overtone, resonance, end correction, displacement node/antinode: standard British textbook usage.
- Sim boxes (howto, model, calc): same steady-state model, damping, end-correction limit and node/antinode thresholds as Finnish.
