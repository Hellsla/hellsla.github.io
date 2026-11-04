VERDICT: PASS
CONTENT-HASH: 1471eeec4778a473

## Blocking

## Polish
- lesson.md:215, exit-ticket.json:8 — "Lähteen koko teho muuttuu … sisäenergiaksi": power is a rate, not something that changes form — "lähteen antama energia muuttuu kokonaan pariston ja johtimen sisäenergiaksi" (FY6 wording: "…sisäenergiaksi, joka siirtyy lämpönä ympäristöön" if the transfer is meant).
- lesson.md:302 — "Väärin päin asetettu paristo vähentää ryhmän lähdejännitettä omansa verran" can be read as 3E − E = 2E (it is 2E + (−E) = E; 2E less than with all cells the right way) — write it as $E = E_1 + E_2 - E_3$, as solutions L3-02 does.
- inquiry.json:436 (tarkistus-1, distractor "lähdejännite on pienempi") — the feedback says the lower E "ei selitä" the dimmer glow, but it does contribute (3 Ω lamp: about 18 % less power from E alone, 52 % less in total) — "ei yksin selitä".
- inquiry.json:186 (koe-1 mistakes) — U : I is caught only for the 1,0 Ω row (1,0). The 2, 4 and 8 Ω rows give 2,0, 4,0 and 8,0 with no targeted feedback — add those values with the same feedback.
- exercises/solutions.md:119 (L3-03) — the rounding reason names the voltages, but the resistances 2,0 Ω and 6,0 Ω (2 s.f.) limit the currents. The answer 1,60 V is still right; justify it (or give 1,6 V). Also in the exercise report.

## Checked
- Recomputed in one script with my own formulas (not agreement with solutions): the sim batteries in koe-1/2/3 (new 1,60 V/0,20 Ω, used 1,45 V/1,2 Ω; R = 1, 2, 4, 8 Ω; series 2,286 V, parallel 1,455 V), koe-1 R_s 0,2006 from rounded readings, mistakes 1,0/1,2. All match.
- Worked example (0,3625 A, 0,36 Ω, 4,4 A, symbolic first, 2 s.f. from 0,13 V), Etsi virhe (0,67 A, 8,0 V, 1,0 V), siirto (10,44 V; P ratio 0,69; I_k 1050 A; relative tolerance accepts 10,4), exit ticket 5,0 A.
- ui-graph figure to scale: E 1,50 V, I_k 5,0 A, triangle (1 A; 1,2 V)–(3 A; 0,6 V) checked against the pixel coordinates. The check-graph least-squares fit gives −2,00 V/A and 9,00 V, the line ends on a grid point (1,5 A; 6,0 V).
- Potential figure, model diagram and connection diagram: signs, current directions and 2E/2R_s, E/(R_s/2) are right.
- sim.js: I = E/(R+R_s), U = E − R_s I, the voltmeter is on the battery side of the switch (U = E when open), the current moves + → − outside, the glow follows R_s I² per cell, the fit is least squares, axes fit all states, and the adapter params match the experiments' initial/locked values. Limits are stated in the "model" box.
- Each prediction has exactly one correct option, and every distractor's feedback carries the right model numbers.
- Car battery: R_s ~0,01 Ω × hundreds of A = volts; the cold-weather mechanism is right.
- Guardrails: the fit sentence ("yleensä"), slope read from the fitted line, extrapolation condition stated, model values called model values.
- FY6 notation (E, R_s, I_k) and the energy wording are consistent. No "muuttuu lämmöksi".
- Scope: inside FY6 contents (napajännite, oikosulku, sarja/rinnan).
