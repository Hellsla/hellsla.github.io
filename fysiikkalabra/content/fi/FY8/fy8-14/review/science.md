VERDICT: PASS
CONTENT-HASH: 1cb648c85bc9b6e3
Mode: full, round 1

## Blocking
- none

## Polish
- inquiry.json ennuste-2 (all three feedbacks) — "kasvaimen kautta kulki vain noin neljäsosa janoista" holds only from N = 50 on (model: 10 % at N = 10, 5 % at 20, 26 % at 50), and the student's table shows the small values — say "suurilla N:n arvoilla", as the johtopaatos model answer does.
- lesson.md Annihilaatiofotonin energia vs inquiry.json tarkistus-2 Järkevyys — the visible photon is 3,3 eV in one (factor 150 000) and 2 eV in the other (2,6·10^5); both right, but name the photon or use one value.
- inquiry.json rontgen table — the 20 cm column comes from unrounded d½ (1,6 %; 3,3 %); the table's own d½ give 1,7 % and 3,4 %.
- inquiry.json tarkistus-3 model and criterion 2 — the inverse-square law is the point-source law; a patient is an extended source, so add "likimain".
- inquiry.json siirto, Vastaus — "kahden tai kolmen merkitsevän numeron" is vague; say that 300 MBq and 110 min are read as two figures.

## Checked
- Own script: d½ from the XCOM coefficients (water 1,85/3,37/4,06 cm; bone 0,27/1,15/1,95 cm), worked example n = 2,353 and 4,198, ratio 3,59; virhe 0,054; siirto 772,0 MBq and its mistake values; f = 1,2355·10^20 Hz and its mistake values; m_e c² = 511 keV.
- Lesson numbers: Tc-99m 6,3 % after 24 h, Am-241 −1,6 % in 10 a, 25 kGy → 6,0 K, lead d½ 0,26 and 3,9 mm, time of flight 0,3 ns → 4,5 cm, doses 5,7 and 2,9 mSv.
- Simulation run in the preview: N = 10, 20, 50, 200 give 18,4 / 4,0 / 1,4 / 0 cm and 10 / 5 / 26 / 25,5 %, equal to my reimplementation and to every feedback; singles mode gives no image.
- Sim matches its Mallin oletukset box; tumour concentration 30–44 times the body's.
- koe-1 isolates N (kohde, ilmaisu locked); virhe and osuus exist in simState.
- Kontrasti graph to scale: curves within 0,004 of (1/2)^(d/d½), markers right.
- Each choice has exactly one correct option; distractor feedback gives the right reason; the single-coincidence answer states its condition (no arrival-time difference).
- E_γ = m_e c² carries its condition (nearly at rest); two photons argued from momentum.
- Radiotherapy 5 · 0,40 Gy figure: simplifications stated after it (C); scope inside FY8; theory, summary and exit ticket agree.
