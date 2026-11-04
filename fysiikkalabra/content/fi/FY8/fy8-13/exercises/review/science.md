VERDICT: FAIL
CONTENT-HASH: 1f82578e25332849

## Blocking
- exercises.json:126–160 (fy8-13-L2-05, text + table) — **A**: the text says the breakdown is STUK-A263 (2020) "pyöristetty", but it is not. STUK-A263 gives radon 4,0 mSv, other natural background about 1,1 mSv and medical use 0,76 mSv (total 5,9). The table has natural non-radon sources 0,7 + 0,3 + 0,3 = 1,3 mSv and medical 0,6 mSv. It also clashes with fy8-14, where natural radiation is 5,1 mSv (so medical is about 0,8). — Fix: use STUK's split, e.g. radon 4,0, muu luonnon säteily (maaperä ja rakennusaineet, kosminen, kehon omat radioaktiiviset aineet) 1,1, lääketieteellinen käyttö 0,8 (sum 5,9). Or take the five-row split straight from the report's table and cite it. The answer stays 68 %; update solutions.md:146 ff. (Annettu, Sijoitus).
- solutions.md:186 (fy8-13-L3-04, Mallivastaus c) and task c) at exercises.json:240 — **B**, safety statement: "vuosiannosta ei saa arvioida pelkästä talvimittauksesta" and "viitearvo ei ylity" go against Finnish practice. The official radon measurement is made in the heating season (at least 2 months), and that result is used as the estimate of the annual mean (it is somewhat high, on the safe side). With this data a heating-season measurement would give about 310–380 Bq/m³, which is over 300, so in practice correction would be recommended. — Fix: rephrase c) as "why does a winter value overestimate the annual dose, and why is the measurement still done in the heating season?" The model answer should say: the stack effect makes winter the highest; in this model the dose follows the annual mean 270 Bq/m³; a heating-season result is the official, on-the-safe-side estimate and would be over 300 here, so correction is recommended. Drop "ei saa".

## Polish
- solutions.md:164 (L2-06) — "kolme merkitsevää numeroa" but r = 3,0 m has two figures; give 11 µSv/h (tolerance 0,03 already accepts it).
- solutions.md:193 + exercises.json:276 (L3-05) — the heading "Kuvaajan lukeminen" and `kind` "graph" are used, but the task has only a table; use "Taulukon lukeminen" and drop "graph" (or add a figure).
- exercises.json:82 (L1-08) — the chest X-ray is 0,10 mSv here but 0,050 mSv (keuhkokuva) in fy8-14-L2-05; use one value in both chapters (a PA chest image is about 0,02–0,1 mSv).
- L3-04 b) repeats the proportional radon scaling of L2-03 and L3-02; what is new is the seasonal mean and the inverse in d). Acceptable, but d) carries the level-3 weight.

## Checked
- All 8 new answers recomputed in one script with my own formulas: L1-07 0,20; L1-08 1,69; L2-05 67,8; L2-06 11,21 (k_ka 100,875); L2-07 7,0; L3-04 58,75 (mean 270, b 9,19); L3-05 2,357 (d½ 4,0 cm). All within tolerance, and answers.py matches.
- L1-06 MC: exactly one correct option, and each distractor's feedback is right.
- L2-06: products 102,5/98/99/104 show no trend, ±3 %; the inverse-square conditions are stated.
- L2-07 error task: the error is Gy = Sv, and w_R = 20 gives 7,0 mSv.
- L3-05: the inverse-square and half-value-layer factors combine correctly; d) names scattering (buildup) and the point-source assumption.
- Real-world values: 5,9 mSv, radon 4,0 mSv (STUK-A263, Siiskonen ed., 2020), 94 Bq/m³ and reference level 300 Bq/m³ are plausible. Concrete d½ 4 cm (Cs-137, about 4–5 cm) is acceptable as stated in the lesson.
- Counts are 8/7/5 and the set follows docs/exercise-bank/FY8.md (the concrete half-value layer moved from L2 to L3-05). There are no duplicates of existing tasks.
- The hash 1f82578e25332849 was the same at the start and at the end.
