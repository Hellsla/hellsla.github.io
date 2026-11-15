VERDICT: PASS
CONTENT-HASH: 1cb648c85bc9b6e3
Mode: full, round 1

## Blocking
- none

## Polish
- inquiry.json ennuste-2 (feedback of all three options) — "kasvaimen kautta kulki vain noin neljäsosa janoista" holds only from N = 50 on (model: 10 % at N = 10, 5 % at N = 20, 26 % at 50), and the student's own table shows the small values — say "suurilla N:n arvoilla", as the johtopaatos model answer already does.
- lesson.md Kaava, Annihilaatiofotonin energia vs inquiry.json tarkistus-2 Järkevyys — the visible photon is 3,3 eV in one (factor 150 000) and 2 eV in the other (factor 2,6·10^5); both are right, but name the photon (violet / red) or use one value.
- inquiry.json rontgen table — the 20 cm column is computed from unrounded d½ (1,6 %; 3,3 %), while the table's own rounded d½ give 1,7 % and 3,4 %; harmless, but a student who checks gets another last digit.
- inquiry.json tarkistus-3 model and criterion 2 — "annosnopeus pienenee etäisyyden neliön mukaan" is the point-source law; a patient is an extended source, so add "likimain" (close to the patient it falls more slowly).
- inquiry.json siirto solution, Vastaus — "kahden tai kolmen merkitsevän numeron tarkkuudella" is vague; state that 300 MBq and 110 min are read as two figures.

## Checked
- Own script recomputes every number: d½ from the XCOM coefficients (1,85/3,37/4,06 cm water; 0,27/1,15/1,95 cm bone), ratios 7 and 2, worked example n = 2,353 and 4,198, ratio 3,59; virhe 0,36 · 0,15 = 0,054; siirto 772,0 MBq and its three mistake values; f = 1,2355·10^20 Hz and both mistake values; m_e c² = 8,187·10^-14 J = 511 keV.
- Lesson figures: Tc-99m 6,3 % after 24 h, Am-241 −1,6 % in 10 a, 25 kGy → 6,0 K in water, lead d½ 0,26 mm and 3,9 mm (ratio 15), time-of-flight 0,3 ns → 4,5 cm, doses 300 MBq · 0,019 and 600 MBq · 0,0049 mSv/MBq.
- Simulation run in the preview: simState at N = 10, 20, 50, 200, 1000 gives virhe 18,4 / 4,0 / 1,4 / 0 / 0 cm and osuus 10 / 5 / 26 / 25,5 / 27,8 %, equal to my own reimplementation and to every feedback and model answer; singles mode gives no image (virhe −1).
- Sim model matches its Mallin oletukset box (exact back-to-back photons, no attenuation, scatter, randoms, positron range or time of flight); tumour concentration 30–44 times the body's ("monikymmenkertainen").
- koe-1 isolates N (kohde and ilmaisu locked); measured keys virhe and osuus exist in simState.
- Kontrasti graph is to scale: both curves within 0,004 of (1/2)^(d/d½); markers at 1,1, 2,2 and 3,4 cm correct.
- Each choice has exactly one correct option; distractors are wrong and their feedback gives the right reason; the single-coincidence answer states its condition (no arrival-time difference).
- E_γ = m_e c² carries its condition (annihilation nearly at rest); two photons argued from momentum.
- Radiotherapy 5 · 0,40 Gy figure: its simplifications (depth dependence, scatter, 3D) are stated right after it (C).
- Scope: inside FY8 central contents; justification, optimisation and the 20 mSv limit agree with the exit ticket and summary.
