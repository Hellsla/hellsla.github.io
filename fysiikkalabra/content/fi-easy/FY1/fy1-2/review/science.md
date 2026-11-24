VERDICT: PASS
CONTENT-HASH: b84e90cd29627708

## Blocking

## Polish
- lesson.md:104 (quantity figure aria-label) — the raster is placed at a slightly different scale from figures.py: the tick labels 0 and 12 sit at x = 67,2 and 531,6, which is about 38,7 units per cm, not the 40 the text says. Pencil and ruler still agree (to scale) — drop the "40 yksikköä" clause or regenerate the labels from figures.py.
- exit-ticket.json:2 — the answer gives $0{,}50\,\text{mm}$ (two significant figures) as $500\,\mu\text{m}$, and the lesson says trailing zeros of an integer are ambiguous — write $5{,}0\cdot10^{2}\,\mu\text{m}$ or note that the value has two figures.
- inquiry.json voyager-malli source_note / packet scope note — the lesson uses $d_0 = 119{,}0\,\text{AU}$ (Burlaga et al. 2019, consistent everywhere, and correct for that source). The scope note still says 119,7 AU and "about 143 AU for February 2026". The model's 142,5 AU agrees with the text. Ask the teacher to update the brief so the two do not diverge.

## Checked
- One Python script recomputed every value. Voyager model (d0 119,0 AU, v 15,341 km/s): 2018/2022/2026/2030 table 119,0/131,9/144,9/157,8 AU, 1,78/1,97/2,17/2,36·10^10 km, 16,5/18,3/20,1/21,9 h. 1.1.2026: 142,2 AU, 19,7 h. Feb 2026: 142,4–142,6 AU. All match.
- Sun's pull from 119 to 143 AU slows the probe by Δv ≈ 0,08 km/s, so the sim box's "about 0,1 km/s" holds.
- Worked example: 4,503·10^9 km, 1,502·10^4 s, 4,17 h. Solved symbolically first; 3 significant figures justified by the limiting datum 30,1 AU.
- 1 AU in 499 s = 8,32 min. Koe-1 times 33,4/334/3340 s (0,0668/0,668/6,68 AU). Ennuste-2: 3340 s. Ennuste-1 feedback: about 7 AU per hour, 1212 AU per week, 63 240 AU per light-year, ratio about 142. All correct.
- Transfer task: 4,842·10^8 km, 3,236 AU/a. Four significant figures are justified; the mistakes 4,84·10^8 and 3236 are diagnosed correctly. Mercury: 5,790·10^7 km, 193,1 s, 3,22 min; mistakes 193 and 0,0536 correct. Saturn: 79 min, distractor 0,87 min.
- Exactly one correct option in each choice item, and every distractor's feedback is right (kertaus, ennuste-1/2, koe-1, voyager-malli, virhe km², merkitsevät 4,50·10^9, tarkistus-1 0,0250 m, check-c2).
- Scale table (nucleus 10^-15, atom 10^-10, red blood cell 10^-5, Earth 10^7, orbits 10^12, stars ≥10^16 m), H atom 0,11 nm, proton 1,7 fm, light-year 9,46·10^12 km, SI base quantities and symbols: all correct.
- sim.js implements the stated model: c = 299 792,458 km/s, AU exact, 1 px = 3474 km. CPX = 86,3 px/s, Sun 401 px, Earth 3,7 px, Moon 110,7 px from Earth, Neptune 1,29·10^6 px. Planet semi-major axes (JPL) and diameters (NASA) are correct; the elapsed time does not depend on the pace.
- simState has dAU, tLight, vAU and vTh. The koe-1 slider range 6–11 covers n = 7–9 and pvm is locked. Koe-2 varies only the date (capture: 142 AU, 19,7 h on 1.1.2026). Until 2100 Voyager stays inside XMAX.
- The model's limits are stated: values are model values, not measurements; signal time is from the Sun (±8 min to Earth); planets lie on one line; the probe marker is enlarged. Agreement with JPL's 143,05 AU (from Earth) is claimed only to about 1 AU.
- Theory, summary, glossary, exit ticket and model answers say the same thing (value = number × unit, km² = 10^6 m², light-year is a length).
