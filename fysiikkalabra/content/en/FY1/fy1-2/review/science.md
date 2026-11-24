VERDICT: FAIL
CONTENT-HASH: c60d30a7c0a9a6ea

## Blocking
- lesson.md:147 — (B) "In the tasks of this book a value given as a whole number ending in zeros, such as $10\,\text{min}$, is exact unless stated otherwise." This makes every such value exact. The house rule (P7, guardrails "Values and significant figures") says only a time span or count that the task sets is exact; a rated or measured value's trailing zeros are significant (480 kW: three, 230 V: three). Later chapters follow P7, so students would get a rule that contradicts them. The same paragraph also calls 384 400 km ambiguous. — Fix: limit the sentence to set quantities, for example "In the tasks of this book a time span or number that the task sets, such as $10\,\text{min}$, is exact; a measured or rated value's trailing zeros are significant unless stated otherwise."

## Polish
- lesson.md:14 (figure "quantity", aria-label) — the label says "horizontally 1 cm is 40 units", but in the embedded SVG the tick labels are $77.4$ units per 2 cm, so 1 cm is $38.7$ units (figures.py draws 40, and the image was rescaled when it was embedded). The figure is still to scale. Fix the stated number, or drop it.
- inquiry.json:177 (voyager-malli) and sim.js D0_AU — the model uses $119.0\,\text{AU}$ (Burlaga et al. 2019, a correct value), but the teacher's brief gives 119,7 AU and "about 143 AU for February 2026". The lesson explains the 142.5 vs 143.05 AU difference correctly (heliocentric vs geocentric, within 1 AU). Flag the departure from the brief to the teacher; this is not an error.
- lesson.md "A unit for every scale" — "defined in metres" fits the AU (exact since IAU 2012). For the light-year, "defined through $c$ and the year" would be more exact. This simplification is level C and acceptable.

## Checked
- One script recomputed every number from the task data: Voyager model table (119.0/131.9/144.9/157.8 AU; 16.5/18.3/20.1/21.9 h), 1 Jan 2026 142.2 AU / 19.7 h (ratio 142), Feb 2026 about 142.5 AU. All match.
- Light times: 1 AU 499 s = 8.32 min; $10^{7,8,9}$ km gives 33.4/334/3340 s; 1 h is about 7.2 AU, 1 week about 1212 AU, 1 ly about 63 200 AU. All match.
- Worked example (4.50e9 km, 1.502e4 s, 4.17 h): solved symbolically first, three significant figures justified, reasonableness check real.
- siirto 3.236 AU/a (4 s.f. justified); mistakes 4.84e8 and 3236 correct. Mercury 3.22 min with mistakes 193 and 0.0536 correct. Saturn 79 min with distractor 0.87 correct.
- Every choice item has exactly one correct option, and each distractor's feedback is right (kertaus, both predictions, koe-1 question, voyager-malli, virhe, merkitsevat, both checks).
- Experiments: koe-1 varies n with pvm locked, and simState gives dAU and tLight exactly at $10^n$ km. koe-2 varies pvm, and simState gives vAU and vTh.
- sim.js implements $d = d_0 + v(t - t_0)$, $t = d/c$ and the Moon = 1 px scale (Sun 401 px, Earth 3.7 px, Moon 110 px from Earth, ruler 28.8 px per $10^5$ km). The pace setting does not change the elapsed time.
- Model box: the Sun's slowing of about 0.1 km/s (computed 0.09) and the signal-time difference to Earth of at most about 8 min are both correct.
- SI table, Kibble balance and Planck constant caption, prefixes, hydrogen atom 0.11 nm, proton 1.7 fm, light-year 9.46e12 km: all correct.
- Scope: stays within FY1 (s = ct as a given model; no forces or energy).
