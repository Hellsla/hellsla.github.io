VERDICT: PASS
CONTENT-HASH: 5b69d428d62913d9

## Blocking

## Polish
- lesson.md:442 — the Artemis I caption says the fuel's chemical energy becomes "raketin liike-energiaksi, lämmöksi, valoksi ja ääneksi": it leaves out the rocket's potential energy as it rises, and the largest share, which is the exhaust jet's kinetic energy. "lämmöksi" also differs from the lesson's own "lämpöenergiaksi". A fair FY2 list (C), but "raketin liike- ja potentiaalienergiaksi, pakokaasujen liike-energiaksi, lämpöenergiaksi, valoksi ja ääneksi" would match the rest of the lesson. The photo (night launch, Florida, November 2022) matches its caption.
- lesson.md:560 — the rounding reason ("110 kJ tulkitaan tarkaksi arvoksi") is not the real one. In a subtraction the last known place limits the result: 450 kJ is known to 10 kJ, so the answer is 340 kJ. The result itself is right.
- inquiry.json tarkistus-1 — the correct option says "lähes kokonaan lämpöenergiaksi", but the feedback on the first option says "lopulta kaikki". Use one wording in both.

## Checked
- One script recomputed all 12 lesson-answers.py values with my own formulas and they all agree: 340 kJ; 3,2; solar input for 1 h is 1361 W/m² · πR² · 3600 s = 6,25·10²⁰ J = 625 EJ, about the same as humankind's 620 EJ in 2023; 1000 years of use ≈ 41 days of sunlight ("noin 40"); 66 MJ = 60 + 2 + 4; 51 GJ; 100; 2500 J; 1800 kJ.
- Pysähdy answers and the exit ticket: 380 kJ, 4200 J, 3 MJ, 160, 9 kJ. check-c2: 2200 kJ : 300 kJ ≈ 7,3. Exactly one correct option in every choice item, and each distractor's feedback says correctly why it is wrong.
- The tikapuut figure is to scale at 33,2 px per power of ten: 1 kJ at 195,6, 10 MJ at 328,5, 1,6 GJ at 401,7 and 140 TJ at 565,8 match the drawn points. 140 TJ ≈ 1600 MW · 24 h; 1,6 GJ = 50 l · 32 MJ/l; lifting the apple takes 0,98 J.
- The sailyminen Sankey is to scale at 0,12 px/kJ (96 = 24 + 72 px for 800 = 200 + 600 kJ).
- The values in the sim's OBJ list are realistic: photon at 550 nm 3,6·10⁻¹⁹ J, AA cell about 13,5 kJ, 11 kg gas bottle 506 MJ, TNT 4,18 GJ, M 9 quake about 2·10¹⁸ J, Finland's electricity 80 TWh = 2,9·10¹⁷ J (7,9·10¹⁴ J per day), Tokyo flight 50 t · 43 MJ/kg. Estimates are marked with rings, and the model box states that the values are rounded.
- koe-1 and koe-2: initial objects are set, the one varied parameter is the object, and simState gives E_MJ and E_EJ.
- Scope: energy forms, conservation and joule prefixes only. No E_k or E_p expressions, W = Fs or chain products. FY2's "lämpöenergia" is used as the guardrails allow.
- The worked example goes symbolic first, then the conversion, then substitution with a sum check.
