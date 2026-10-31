VERDICT: FAIL
CONTENT-HASH: a2d3f2f48442b01c

## Blocking
- inquiry.json:83 — **A** (assessment, consistency). The title "Ennuste 2: kymmenkertainen matka" is wrong. The task goes from 10^7 km to 10^9 km, which is a hundredfold distance. The correct option and its feedback say so ("satakertaiseksi eikä kymmenkertaiseksi"). The title instead states the premise of the distractor "Noin 330 sekuntia, koska matka kasvaa kymmenkertaiseksi", so it steers the student towards the wrong answer. — Fix: give the title a neutral name that does not give the answer away, e.g. "Ennuste 2: kaksi kymmenpotenssia pidempi matka".

## Polish
- exit-ticket.json:8 — the answers "4200 m" and "500 µm" lose the significant figures of 4,2 km and 0,50 mm. The lesson itself teaches that trailing zeros in a whole number are ambiguous. — Write 4,2·10³ m and 5,0·10² µm, or add a note on this.
- lesson.md:502 — the text calls AU "Maan ja Auringon keskimääräinen etäisyys". Two lines earlier it also says the AU "on määritelty metreinä". Both are fine as a C simplification, but saying "nykyään sovittu tarkaksi arvoksi" would remove the small tension between them.
- inquiry.json:188 — the correct option says "sen tarkkuus on lähtötietojen tarkkuus". The model's accuracy is also limited by its constant-speed assumption, which the feedback states. Consider "ja sitä rajoittavat lähtötiedot ja vakionopeusoletus".
- sim.js (the slider label) — at the view centre d = 0 km (Alusta, Aurinko), the slider label shows "d = 10^{6,00} km" because n is clamped to N_MIN. The readout below it says d = 0 km. A student could read 10^6 km as a real distance. Consider hiding the label value when d < 10^6 km, or showing "< 10^6".

## Checked
- I recomputed every number in one script: the Voyager 2 model (142,86 AU and 19,80 h on 1.1.2026; the 2018/2022/2026/2030 table to the last digit; 143,1–143,4 AU in February 2026), the 1 AU light time of 499 s = 8,32 min, Neptune (4,503·10⁹ km, 4,17 h), the transfer task 3,236 AU/a with its two mistake values, Mercury (3,22 min, mistakes 193 s and 0,0536 h), Saturn (79 min), and the area 1,702 m².
- The koe-1 values 33,4 s, 334 s and 3340 s come from simState.tLight at n = 7, 8, 9. Both experiments isolate the varied parameter: koe-2's measured keys vAU and vTh depend only on pvm.
- The sim scale: Sun 401 px, Earth 3,7 px, Neptune 1,29·10⁶ px, c = 86,3 px/s, the Moon 110,6 px from the Earth, a ruler tick every 28,8 px. Saturn's ring radii match the D/C, B and A rings.
- The sim implements d = d₀ + v(t − t₀). The texts state that the light time is measured from the Sun, with at most about 8 min difference to the Earth, and call the values model values.
- The magnitudes in the scale list are right: H atom 0,11 nm, proton 1,7 fm, red blood cell, light-year 9,46·10¹⁵ m, 63 000 AU per light-year, about 1200 AU per light-week, 7,2 AU per light-hour.
- The significant-figure rules and their examples are right (0,0250 → 3, 3,00·10⁸ → 3), and the limiting datum is justified in each solution.
- Every choice item has exactly one correct option, and every distractor's feedback is right.
- The figures: the pencil is 480 units = 12,0 cm at 40 units/cm, as its caption says. The prefix ladder is right. The conversion figure is marked as not to scale.
- The content stays in FY1 scope: s = ct is used as a given model.
