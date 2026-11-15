VERDICT: FAIL
CONTENT-HASH: 8a021cf8fc8e7bb7
Mode: full, round 1 (--lang en)

## Blocking
- inquiry.json:87 and :95 (ennuste-2, feedback of the correct option and of "One is enough") — **B**: "Only about a quarter of the segments passed through the tumour" is stated without its condition. Experiment 1 makes the student record "through tumour (%)" at N = 10 and 20, where the sim shows 10 % and 5 % (26 % at N = 50, 25.5 % at 200; confirmed in the browser). The feedback contradicts the student's own table at two of the four required rows, and line 95 joins "a quarter" with the N = 10 result — fix: state the condition as the conclusion's model answer (line 190) already does, e.g. "with large N about a quarter of the segments passed through the tumour (at N = 10 and 20 only 10 % and 5 %)".

## Polish
- inquiry.json:203 (rontgen table) — the 20 cm column (1.6 %, 3.3 %) is computed from unrounded coefficients; from the table's own d½ a student gets 1.7 % and 3.4 % — use those or say the column comes from unrounded values.
- lesson.md:462 vs inquiry.json tarkistus-2 solution — "about 150 000 times a photon of visible light" (3.3 eV photon) but "2.6·10^5 times" (2 eV photon) — name the reference photon in the lesson ("the most energetic visible photon").
- inquiry.json:370 (tarkistus-3 model) — "every decay of fluorine-18 produces two photons" (97 % are β+) and "dose rate decreases with the square of the distance" (point-source approximation; only roughly so beside a patient) — "almost every", "roughly".

## Checked
- One script, own formulas: d½ of water and bone at 30/60/100 keV, ratios, 20 cm transmission; lead d½ 0.26 mm and 3.9 mm, ratio 15.
- Worked example: n_A 2.353, n_B 4.198, ratio 3.59; second route 0.1957 : 0.05449; symbolic first, rounding reason right.
- E = m_e c² = 8.187·10⁻¹⁴ J = 511 keV; f = 1.2355·10²⁰ Hz; both mistake values.
- Siirto: 772.0 → 770 MBq; mistakes 116.6, 600, 304.8; the check 386 → 300 MBq.
- Tc-99m 6.3 % after a day, Am-241 −1.6 %, 25 kGy → 6.0 K, TOF 0.3 ns → 4.5 cm, FDG 5.7 mSv, bone scan 2.9 mSv, 60 Gy = 30 · 2 Gy.
- Sim: own port of sim.js and simState in the preview agree: N = 10/20/50/200 → 18.4 / 4.0 / 1.4 / 0 cm; tumour concentration ratio about 56 ("tens of times"); axes and y sign consistent; singles mode gives virhe −1.
- Experiment 1: kohde and ilmaisu locked, N varied, virhe and osuus exist in simState; model limits are stated.
- Every choice: exactly one correct option, distractors wrong, feedback physics right (apart from Blocking).
- Kontrasti graph is to scale (markers at 1.1, 2.2, 3.4 cm; curve ends 0.196 and 0.0065); PET figure's line passes through the annihilation point.
- Scope inside FY8 contents; X-ray/gamma naming, justification/optimisation/dose limits and exit ticket agree with the theory.
