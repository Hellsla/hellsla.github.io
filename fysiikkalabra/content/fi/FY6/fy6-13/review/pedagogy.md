VERDICT: PASS
CONTENT-HASH: 011b4e99d4a6ac33

## Blocking

## Polish
- inquiry.json koe-2 / koe-5 — the core path holds three experiments (koe-1, 2, 3, nine table rows) while the one slot goal that has no required activity, läpilyöntilujuus, rests on the optional koe-5; swap them: make koe-5 required (a student sees the spark and reads E_max) and koe-2 optional (C = ε₀ε_rA/d is then confirmed in the exercises), which also trims the hour.
- inquiry.json ennuste-1 / ennuste-2 — options use "kapasitanssi" before the term is introduced (Ennusta comes before Teoria), and every option of ennuste-2 carries the premise "lasi kasvattaa kapasitanssia"; add one plain sentence to the prompts (e.g. "kapasitanssi kertoo, kuinka paljon varausta kondensaattoriin tulee jännitettä kohti") so the prediction can be argued from the prerequisites.
- inquiry.json siirto — the prompt hands over the key idea ("Paristo siirtää koko varauksen jännitteensä yli"), so the transfer is mostly substitution; drop that sentence and leave it to hint 1.
- inquiry.json simulaatio `howto` — "levyjen varaus jää siksi, mikä se oli irrotushetkellä" — "levyjen varaus pysyy samana kuin se oli irrotushetkellä"; tarkistus-3 "ja mitä sen energia on" — "ja kuinka suuri sen energia on".
- lesson.md "Lataus ja purkautuminen" — the charging and discharging curves (qualitative goal) are only read, not acted on beyond tarkistus-2 (charging current); one discharge item (voltage or current direction) would close the goal.

## Checked
- Path: prerequisites (E = U : d, QU energy, power) are enough; the hook question (why seconds to charge, a millisecond to flash) is answered in "Energia on sähkökentässä", in the example (6,75 J, 6,8 kW, 3,4 s) and in the reflect item; slot goals covered, kondensaattorien kytkennät correctly left out.
- Predictions can be refuted: koe-1 (Q : U constant, W grows four-fold), koe-3 (Q stays, U drops to 0,18 kV with glass); locked parameters and the source switch are the controlled variables; model values 11 µJ, 44 µJ, 88,5 nC, 0,18 kV, 7,9 µJ recomputed and correct.
- Option feedback repairs each misconception (W ∝ U, "kapasitanssi muuttuu", purged capacitor, source stays connected).
- Figures (structure, charge/discharge curves, dielectric polarisation, (Q, U) triangle) are legible at 390 px, sit beside the paragraphs they explain, and match their descriptions (4 versus 2 field lines, 9 molecules); colour always paired with sign labels.
- Worked example is staged in seven steps, principle before formula, unit step, sanity check by Q = CU; the Etsi virhe item (µF not converted) has real distractors; siirto answer 190 µJ and the three mistake values verified.
- Misconceptions named in the text: stored charge versus energy, current through the dielectric, C depends on U; safety paragraph (microwave, flash) covers the electrical-safety goal.
- Sim at 390 px (capture #2): circuit, (Q, U) graph with orange area, sliders and readout all fit; model assumptions stated (homogeneous field, instant charging, model values).
- Exit ticket tests Q = CU and the factor ½ by the triangle; explain criteria (tarkistus-3) are observable.
- Finnish and glossary terms (eriste, kapasitanssi, läpilyöntilujuus) correct; case after number+unit correct.
