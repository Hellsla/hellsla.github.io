VERDICT: FAIL
CONTENT-HASH: 7b152209cf589af5

## Blocking
- content/fi/FY1/fy1-8/exercises/solutions.md:192 — (A, rounding reason) The solution says "kaksi merkitsevää numeroa kuten epävarmuudessa $0{,}2\,\text{s}$", but 0,2 s has one significant figure. Line 8 of the same file says so itself ("yksi merkitsevä numero kuten epävarmuudessa $0{,}2\,\text{s}$"). The lesson's worked example gives the real reason: a minimum distance is a design estimate given to practical precision and rounded up so that the limit is met — fix: "$1{,}4\,\text{km}$, suunnitteluarvio käytännön tarkkuudella ja ylöspäin pyöristettynä, jotta $5\,\%$ raja varmasti täyttyy".

## Polish
- content/fi/FY1/fy1-8/exercises/exercises.json (fy1-8-L1-10 text) — "Mitattavan ajan suhteellisen epävarmuuden saa olla" should read "suhteellinen epävarmuus saa olla" (language).
- fy1-8-L1-10 is close to the worked example: only the speed is different (0,42 m/s becomes the speed of sound) — pedagogy's call.

## Checked
- fy1-8-L1-10 only (delta, added exercise); hash the same at start and end.
- Recomputed independently: t_min = Δt/ε_max = 0,2 s / 0,05 = 4,0 s; s = vt = 343,2 m/s · 4,0 s = 1,373 km (key 1.3736 from MAFY 343,4 m/s).
- MAFY speed of sound in air at 20 °C, 343,4 m/s, is right; the hint names the right table.
- The model is the lesson's t ≥ Δt/ε_max and s = vt. It is solved symbolically first, and the check back (0,2/4,0 = 5 %) is a real check.
- The physics is realistic: hand timing over more than 1 km is the classic way to measure the speed of sound. Neglecting the distance's own uncertainty fits the task as posed (time only).
- Tolerance 0,04: the shown 1,4 km is 1,9 % from the key.
