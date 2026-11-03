VERDICT: FAIL
CONTENT-HASH: 44457fb54bf5215b

## Blocking
- exercises/solutions.md:49 (fy6-7-L1-05, Järkevyys) — A: "Koko vuoden valaistus yhdellä LED-lampulla käyttää vähemmän energiaa kuin yksi puolentoista tunnin saunomiskerta 6 kW:n kiukaalla" is false: 11 kWh (10,95) > 6,0 kW · 1,5 h = 9,0 kWh. — Fix: "suunnilleen saman verran (hieman enemmän) kuin yksi puolentoista tunnin saunomiskerta 6 kW:n kiukaalla (9 kWh)".

## Polish
- exercises/solutions.md:60 (L2-01) — "Lämmitys … tuottaa yli puolet energiasta": the stage uses (käyttää) the energy, it does not produce it. Write "käyttää yli puolet energiasta".
- exercises/solutions.md:29 (L1-03) — "alle 10 A:n, joten kuivaaja mahtuu tavalliseen kodin virtapiiriin" anticipates the fuse chapter; safety statements must be exact: say it fits a 10 A or 16 A fused circuit when nothing else heavy is on.
- lessons/FY6/fy6-7/answers.py:15 — comment calls the figure "fy6-7/pesukone"; its id is `fy6-7/washer`.
- exercises/solutions.md (L2-01 Järkevyys) — the "average about 0,5 kW" check is essentially the answer divided back; comparing with the 0,50 kWh heating stage alone is the real check already given.

## Checked
- All 12 answers recomputed in one script with my own formulas: agree with answers.py and exercises.json (0,18; 0,54; 7,83; 52,5; 10,95; 0,80; 480; 6,70; 75,9; 7,33; 371; 4,99).
- washer figure: values 2,0/0,2/0,4 kW and 0,25 h breaks lie on gridlines (0,2 kW, 0,25 h); description gives the same data and no energy.
- L3-03: constant resistance stated in the task; I = U : R, P = UI, E = Pt symbolic first; energy wording "sisäenergiaksi, joka siirtyy lämpönä" correct.
- L1-03 and the 230 V effective value: P = UI applied to a heating device, as the lesson states.
- L3-02: E = (K − K_perus) : a solved symbolically, check 64,15 € ≈ 64,20 €, 428 kWh mistake correct.
- Units, tolerances and significant-figure reasons fit the data; magnitudes realistic (kettle 8,7 A, standby 39 kWh/year, water heater 2,0 kW).
- Notation E, P, t, a, K, K_perus matches the brief's lesson; all inside FY6 "sähköteho ja Joulen laki".
