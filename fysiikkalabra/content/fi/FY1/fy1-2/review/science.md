VERDICT: FAIL
CONTENT-HASH: 5b5a78cac400dd78

## Blocking
- content/fi/FY1/fy1-2/lesson.md:251 + solutions.md:18, solutions.md:108 — the significant-figure rule the lesson teaches ("kaikki numerot, myös loppunollat, ovat merkitseviä") is contradicted by two solutions: L1-02 treats the trailing zeros of 384 400 km as not significant, and L3-02 says 1920 px "on annettu kolmella" merkitsevällä numerolla. By that rule 1920 has four figures (and is exact); significant figures are a lesson goal — fix: add one sentence to lesson.md saying that the trailing zeros of a whole number are ambiguous (write 3,844·10⁵ km to show the precision), then make both solutions follow it: L3-02 answer 674,4 (four figures, from 30,07 AU, 1,496·10⁸ km and 3474 km; 1920 px exact), L1-02 justification citing that rule.
- lessons/FY1/fy1-2/figures.py (lesson.md:183–333, prefixes figure) — the prefix symbols in the boxes are italic math ($n$, $\mu$, $m$, $k$, $M$, $G$, $T$); SI prefix symbols are upright, as the lesson itself says, and italic $m$ reads as mass — fix: $\text{n}$, $\mu$ upright (e.g. $\text{µ}$ or \upmu), $\text{m}$, $\text{k}$, $\text{M}$, $\text{G}$, $\text{T}$; likewise $\mu\text{m}$ in the bottom row.

## Polish
- solutions.md:57 — the intermediate 2595 s / 60 = 43,25 min is then rounded to 43,2; show 43,247 min.
- lessons/FY1/fy1-2/answers.py — the L2-04 comment says "1,325 milj. km", but the answer is 1,3255.
- inquiry.json voyager-malli — the correct option could say once that the signal time is from the Sun, not the Earth.

## Checked
- All 12 exercise answers, siirto (3,236 AU/a), tarkistus-2 (3,22 min; mistakes 193 s, 0,0536 h) and the Neptune example (4,50·10⁹ km, 4,17 h) recomputed independently: all match within 0,2 %.
- Voyager 2 model table (119,7 / 132,6 / 145,6 / 158,5 AU; 16,6 / 18,4 / 20,2 / 22,0 h) and 1.1.2026 values (142,9 AU, 19,8 h) recomputed from d0, v, t0; mid-Feb 2026 ≈ 143 AU matches JPL.
- Prediction feedback numbers: 1 h ≈ 7,2 AU, 1 week ≈ 1212 AU, 1 ly ≈ 63 000 AU, 10⁷/10⁸/10⁹ km → 33,4/334/3340 s; correct options right.
- sim.js: scale 3474 km/px (Sun 401 px, Earth 3,7 px, Moon 110 px off), Gm ruler, light pulse in simulated time, Voyager model = brief; limits (one line, mean radii, marker enlarged, Sun-distance signal time ≤ 8 min off) stated.
- koe-1/koe-2 isolate n / date; simState has the measured keys.
- Figures' numbers, SI table, FY1 scope (t = s/c as given uniform motion) correct.
