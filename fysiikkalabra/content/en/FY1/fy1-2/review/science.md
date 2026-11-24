VERDICT: PASS
CONTENT-HASH: b31745d2f8a9936d

## Blocking

## Polish
- assets/sims/fy1/fy1-2/sim.js (readout, `tx`/`sci`/`num3`) — the English page shows the readout with decimal commas: "$v = 15{,}341\,\text{km/s}$", "$3{,}47\cdot10^{5}\,\text{km}$", "$10^{6{,}00}$". An English reader can take 15,341 km/s as fifteen thousand km/s, and inquiry.json writes $15.341\,\text{km/s}$. Fix: use the page's decimal separator in the shared number formatter. This is a localisation issue for the visual reviewer, but it changes how a magnitude reads.
- lesson.md:14 (figure "quantity", aria-label) — this carries over from round 1. The label says "1 cm is 40 units", but the embedded figure has 38.7 units per cm. The figure is still to scale. Fix the number or drop it.
- inquiry.json:177 and sim.js `D0_AU` — the model uses $119.0\,\text{AU}$ (Burlaga et al. 2019, the published value), but the teacher's brief says 119,7 AU. The lesson treats the model value of 142.5 AU and JPL's 143.05 AU from Earth correctly. Raise this with the teacher as a departure from the brief. It is not an error.
- inquiry.json:116 (sim `model`) — "15.341 km/s ... the value at the crossing": JPL's mission-status speed is a recent value, not the 2018 one. The difference is under 0.1 km/s and level C. Fix: "speed relative to the Sun (NASA/JPL)".

## Checked
- The round-1 blocking item is fixed. lesson.md:233 now follows P7: a set time span or count is exact, and the trailing zeros of a measured or rated value are significant (230 V: three).
- One script recomputed the Voyager model: the table (119.0/131.9/144.9/157.8 AU; 1.78/1.97/2.17/2.36·10^10 km; 16.5/18.3/20.1/21.9 h), 2026-01-01 (142.2 AU, 19.7 h, ratio 142) and Feb 2026 (about 142.5 AU). All match.
- Light times match: 1 AU 499 s = 8.32 min; 10^7, 10^8, 10^9 km give 33.4/334/3340 s; 1 h is 7.2 AU, 1 week 1212 AU, 1 ly 63 200 AU and 9.46·10^12 km.
- Worked example: 4.50·10^9 km, 1.502·10^4 s, 4.17 h. It is solved symbolically first, three significant figures are justified and the reasonableness check is real.
- siirto: 3.236 AU/a; mistakes 4.84·10^8 and 3236 are right. Mercury: 3.22 min; mistakes 193 s and 0.0536 h are right. Saturn: 79 min with distractor 0.87 right. Exit ticket: 500 µm. 1.85·0.92 rounds to 1.7 m².
- Every choice item has exactly one correct option, and the distractors' feedback is right (kertaus, both predictions, koe-1, voyager-malli, virhe, merkitsevat, both checks).
- Playwright on preview/en: at n = 7, 8, 9, simState gives dAU 0.0668/0.668/6.68 and tLight 33.4/334/3336 s. pvm 2026-01-01 gives vAU 142.16 and vTh 19.71. Both experiments isolate the parameter they vary.
- sim.js diff since round 1: only the layout changed (three control rows, legend line removed). The physics is unchanged: $d = d_0 + v(t-t_0)$, $t = d/c$; the Sun is 401 px, the Earth 3.7 px, the Moon 110 px from the Earth, the light pulse moves 86.3 px/s, and the pace setting does not change the elapsed time.
- Model box: the slowing of about 0.1 km/s (computed 0.095) and the difference of at most about 8 min in the signal time to Earth are correct.
- SI table, Kibble balance caption, prefixes, scale table (H atom 0.11 nm, proton 1.7 fm): all correct.
- Scope: FY1 (s = ct is a given model; no forces or energy).
