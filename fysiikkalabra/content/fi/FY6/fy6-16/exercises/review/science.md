VERDICT: FAIL
CONTENT-HASH: 5bb0e1e6e0f0c802

## Blocking
- solutions.md:109 (fy6-16-L3-02) — A: the rounding reason "virrat on annettu kokonaislukuina, joten tulos lasketaan tarkasti" is wrong. A whole number is not an exact value: 10 A and 16 A have two significant figures. — Fix: justify the three figures by what the data are, e.g. "Vastaus: $156\,\%$; virrat $10\,\text{A}$ ja $16\,\text{A}$ ovat latausaseman tarkkoja asetusarvoja, joten suhde $1{,}6$ on tarkka". If the solution reports two significant figures (≈ 160 %) instead, raise the tolerance to at least 0,03, because 160 differs from 156 by 2,6 % and the current 0,02 would reject it.

## Polish
- exercises.json:13 (L1-02) — the cable limits the current to 10 A on an ordinary socket. The lesson says the cable "yleensä noin 8 A:iin", and as far as I recall Tukes advises keeping socket charging at about 8 A (I could not check this here). Use 8 A, or say the cable is set to 10 A.
- solutions.md:79 (L2-03) — the answer is a maximum, but 11,96 A is rounded up to 12 A, which puts the phase at 25,04 A. Write "enintään noin 12 A (11,96 A)" or round down.
- exercises.json:83 (L3-01) — η = 82 % and 92 % both fall outside the lesson's "tyypillisesti 85–90 %". Mark them as example values, or explain why: in both cases the car's own onboard charger does the conversion, and the difference comes mainly from the charging current.
- solutions.md L3-01 Järkevyys — "eroaa noin 10–12 %" is correct (397,7 : 3658,5 = 10,9 %; 397,7 : 3260,9 = 12,2 %); naming which base each percentage uses would make the check clearer.

## Checked
- All 12 answers recomputed with my own formulas in one script; they match answers.py: 41,6 kWh; 2,3 kW; 15,94 A; 6,30 €; 88 %; 27,5 kWh; 10,87 h; 11,96 A; 6,528 V; 59,65 €; 156 %; 7,157 A.
- P = UI for a single phase and P = 3UI with the same current in each phase and U = 230 V phase voltage: used as the lesson states them (L1-03, L2-03, L3-03).
- L2-04 uses 2l = 60 m (out and back): R = 0,408 Ω, drop 6,5 V ≈ 3 %, about 100 W, 3,5 W per metre of cable. Realistic.
- L2-03: the stove's phase current plus the charger's current are summed per phase conductor against the 25 A main fuse (Kirchhoff), and the result is consistent with the lesson's 12 A and 8,3 kW.
- lataus-ex figure code gives 11 kW for 0–2,0 h and 5,5 kW for 2,0–3,0 h on a 0,5 h × 1 kW grid. The description carries the same values, and no energy is written on the figure.
- In every solution the unknown is solved symbolically first; unit conversions (snt → €, mm² → m², kWh → Wh) are right; each Järkevyys is a real independent estimate.
- L3-03 needs 7,2 A, above the 6 A minimum charging current, so the scenario is realistic. L3-01's conclusion (small saving, safety the main reason) is sound.
- Units and tolerances (0,02) suit two-significant-figure data.
