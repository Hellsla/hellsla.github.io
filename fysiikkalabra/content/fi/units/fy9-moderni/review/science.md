VERDICT: FAIL
CONTENT-HASH: 115941f6cb5f4383
SCOPE: delta: new tasks s8 (Betoniseinä) and s9 (Galaksien etääntyminen) and the changed intro; older tasks s1-s7 untouched

## Blocking
- **A (causality), s8 d Oletukset:** "eikä lähteen aktiivisuus pysy vakiona. Siksi todellinen seinä kannattaa tehdä tulosta paksummaksi". A decaying source gives a *smaller* dose rate over time, so this reason points the other way. Scattering (build-up) is a correct reason; replace the activity clause with one that really raises the dose (a stronger or replaced source, longer time in the corridor) or drop it.
- **Assessment (7), s8 d criterion 4 (transfer, 1 p):** d asks only "kuinka paksu seinän pitää vähintään olla". The criterion scores naming an assumption and its effect, which d does not ask, and "annosnopeus on vakio" is an assumption the task text itself gives. Either ask for it in d ("Mikä mallin oletus voi tehdä tuloksesta liian pienen?") or move the point.
- **B (6, consistency), s9 c:** the Periaate "on liikkunut ... ja lähtenyt samasta paikasta kuin muut" (and the part text "jokaisen galaksin liikkuneen koko ajan samalla nopeudella", criterion 1 "kulkenut matkan d") is the explosion-from-a-point picture that s9 d's model answer, its Yleisiä virheitä ("kuin räjähdyksen sirpaleet") and fy8-16 ("ei ollut räjähdys ... jostakin pisteestä") reject. State the condition as distances: "galaksien väliset etäisyydet ovat kasvaneet nollasta koko ajan samalla nopeudella", t = d/v = 1/H0.

## Polish
- s9 a: the task text gives the grid point (250 Mpc; 18 000 km/s), so the graph_read point is earned by copying the text and a) is a single division. The alt-text already carries the point for non-visual readers; the bullet could go.
- s9 d criterion 2 requires "avaruus itse laajenee". The no-centre argument is criterion 1 (v ∝ d looks the same from every galaxy); consider accepting criterion 1's argument with any correct expansion picture.
- s8 a: (20 cm; 5,0 µSv/h) sits near the axis of a linear graph; a ±0,5 µSv/h reading gives µ = 0,134–0,144 1/cm, outside the 3 % tolerance. (10 cm; 20 µSv/h) is more robust, or widen the tolerance to about 5 %.

## Checked
- One script (scratchpad rc_moderni.py) recomputed every number from the figures' own data (fy8-13 figures.py: 80 µSv/h, half-value 5,0 cm; fy8-16: line H0 = 72, nine points, LS slope 72,4) beside answers.py: µ 0,1386 (also ln 8/15), 6,60 µSv/h, 330 h, 2,18 mSv, Ḣmax 3,03 µSv/h, d 23,61 cm, 23 cm -> 1,09 mSv, 24 cm -> 0,95 mSv, error value 31,6 cm; H0 72, 116,7 Mpc, 8640 km/s at 120 Mpc, 2,333e-18 1/s, 4,286e17 s, 1,358e10 a. All agree; roundings and the upward rounding of d are justified.
- Physics: exponential attenuation (task gives the model; fy8-13 teaches the half-value form, accepted under Hyväksytään myös), H = Ḣt, 1 mSv public limit; Hubble's law, 1/H0 as Hubble time with the non-constant rate stated. Scope FY8.
- Points: s8 3+3+3+4, s9 3+3+4+3; criteria sum to part points.
- Intro: nine tasks match the set; "Tehtävissä 8 ja 9 ... kuvaajan kanssa" true.
- practice.py check OK; hash the same at start and end.
