VERDICT: FAIL
CONTENT-HASH: 8a021cf8fc8e7bb7
Mode: full, round 1 (--lang en)

## Blocking
- inquiry.json:87 and :95 (ennuste-2, feedback of the correct option and of "One is enough") — **B**: "Only about a quarter of the segments passed through the tumour" lacks its condition. Experiment 1 has the student record "through tumour (%)" at N = 10 and 20, where the sim shows 10 % and 5 % (26 % at N = 50, 25.5 % at 200; confirmed in the browser), so the feedback contradicts two of the four required rows, and line 95 joins "a quarter" with the N = 10 result — fix: state the condition as the conclusion's model answer (line 190) does: "with large N about a quarter … (at N = 10 and 20 only 10 % and 5 %)".

## Polish
- inquiry.json:203 (rontgen table) — the 20 cm column (1.6 %, 3.3 %) comes from unrounded coefficients; the table's own d½ give 1.7 % and 3.4 % — use those or say so.
- lesson.md:462 vs tarkistus-2 solution — "150 000 times a visible photon" (3.3 eV) but "2.6·10^5 times" (2 eV) — name the reference photon in the lesson.
- inquiry.json:370 (tarkistus-3 model) — "every decay of fluorine-18" (97 % are β+) and the inverse-square law beside an extended patient — "almost every", "roughly".

## Checked
- One script, own formulas: d½ of water and bone at 30/60/100 keV, ratios, 20 cm transmission; lead d½ 0.26 and 3.9 mm, ratio 15.
- Worked example: n 2.353 and 4.198, ratio 3.59; second route 0.1957 : 0.05449; symbolic first, rounding reason right.
- E = m_e c² = 8.187·10⁻¹⁴ J = 511 keV; f = 1.2355·10²⁰ Hz; both mistake values.
- Siirto 772.0 → 770 MBq; mistakes 116.6, 600, 304.8; check 386 → 300 MBq.
- Tc-99m 6.3 % after a day, Am-241 −1.6 %, 25 kGy → 6.0 K, TOF 4.5 cm, FDG 5.7 mSv, bone scan 2.9 mSv.
- Sim: own port of sim.js and simState in the preview agree (N = 10/20/50/200 → 18.4/4.0/1.4/0 cm); concentration ratio about 56; y sign consistent; limits stated.
- Experiment 1: kohde and ilmaisu locked, N varied, virhe and osuus exist in simState.
- Every choice: one correct option, distractors wrong, feedback physics right apart from Blocking.
- Kontrasti graph is to scale; the PET figure's line passes through the annihilation point.
- Scope inside FY8; exit ticket and summary agree with the theory.
