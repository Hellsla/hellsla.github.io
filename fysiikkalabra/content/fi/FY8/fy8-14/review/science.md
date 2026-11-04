VERDICT: FAIL
CONTENT-HASH: 1c59e4e4a38d1723

## Blocking
- inquiry.json:85 (ennuste-2 correct option and its feedback), :190 (johtopaatos model), lesson-answers.py koe-1, sim-spec "satojen koinsidenssien jälkeen" — **A**: the conclusion "the brightest point reaches the tumour only after hundreds of coincidences" comes from one unrepresentative seed (seed 4). The same model run over 60 other seeds gives a median distance of 1.4 cm at N = 20 and 1.0 cm at N = 50, and 97 % of runs are within 1.5 cm at N = 100. Even seed 4 is non-monotonic (3.6 cm at N = 20, then 14.9 cm at N = 50). — Pick a seed whose sequence is typical and monotonic-ish (and update the model values), or reword to "kymmeniä tai satoja; pienillä N:llä tulos vaihtelee sattumalta". A third way: have koe-1 record N = 20 too, so the student sees the chance.
- lesson.md:279 ("Yksi jana ei kerro, missä kohdassa janaa lähde on"), inquiry.json:64 ("Keskipisteestä ei siis voi päätellä mitään"), :132 sim model — **B**: this is true only when the device does not measure the difference in arrival times. Current time-of-flight PET scanners measure it with a resolution of about 0.2–0.5 ns, which places the source to within a few cm along the line (Δx = cΔt/2). — Add "kun saapumisaikojen eroa ei mitata" in the theory and in the model box ("malli ei käytä saapumisaikojen eroa"), and soften the feedback to "laite ei erota näin pientä aikaeroa tarkasti".
- lesson.md:58 (and the glossary term röntgensäteily) — **B**: the text says the name tells whether the photon came from braking or from a nuclear transition. X-ray tubes also emit characteristic X-rays from transitions in the anode atoms' inner electron shells. — Write "elektronien jarrutuksessa tai atomin sisäkuoren siirtymässä vai ytimessä".

## Polish
- lesson.md:178 and exit-ticket — "kalsiumatomeissa on paljon elektroneja": the main cause is the larger atomic number (photoelectric absorption grows steeply with Z) together with the density. Say "suuri järjestysluku".
- lesson.md:285 figure and ennuste-3 — "terve kudos … noin 0,40 Gy": exercise L3-01 rightly gives the entrance dose as 1.3 times that. Say "yhden keilan annoksen" without the number, or add "keilan tulokohdassa enemmän".
- lesson.md:445 "noin 150 000-kertainen" corresponds to a 3.4 eV (UV-edge) photon. Tarkistus-2 uses 2 eV, which gives 2.6·10^5. Write "noin 200 000".
- lesson.md:189 "PET-kuvaus noin 6 mSv" is FDG only. PET-TT adds the CT dose; say so, since the hero image shows a PET-TT room.
- lesson-answers.py comments give IB 0,05434 / ratio 3,60 and siirto 772,3. The values are 0,05449 / 3,59 and 772,0, and the lesson text has them right.

## Checked
- NIST μ/ρ → d½: water 1.85/3.37/4.06 cm, cortical bone 0.271/1.15/1.95 cm, 20 cm tissue 0.055 %/1.6 %/3.3 %; Pb 0.255 mm (140 keV), 3.90 mm (511 keV), consistent with fy8-12's Cs-137 5.5 mm.
- Notation $d_{1/2}$ and $I = I_0(\tfrac12)^{d/d_{1/2}}$ match fy8-12; Tc-99m 6,01 h and C-14 5700 a match the decay-law chapter; 5,1 mSv natural matches fy8-13.
- Esimerkki 0,1957/0,05449 → 3,59 → 3,6; check 2^1,85.
- 511 keV = m_e c² (8,187·10⁻¹⁴ J); f = 1,2355·10²⁰ Hz and its mistakes 1,24e17 and 7,71e38.
- Siirto 772,0 → 770 MBq; mistakes 116,6, 600 and 304,8.
- F-18 110 min / β⁺; ICRP 128 FDG 0,019 mSv/MBq (web-confirmed); bone scan about 3 mSv; dental, chest, CT and PET doses fit typical STUK orders of magnitude.
- Am-241 37 kBq, 432 a, 1,6 % in 10 a; sterilisation 25 kGy ≈ 6,0 K; 2 Gy × 30 = 60 Gy; säteilylaki 859/2018, 20 mSv/a.
- sim.js matches lesson-answers.py and the sim-spec (seed, 25 %/20 %, σ 0,8 cm, 0,6 cm backprojection, simState keys).
- Interpret table, ratios ≈ 7 and ≈ 2; virhe 0,054; kertaus options.
- Tarkistus-3 model: 3,9 : 0,26 = 15.
