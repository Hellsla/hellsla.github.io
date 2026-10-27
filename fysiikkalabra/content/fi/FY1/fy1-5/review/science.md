VERDICT: PASS
CONTENT-HASH: 6ddbffc5c9e6f900

## Blocking

## Polish
- lesson.md:129 — "Muunna aina ennen sijoitusta SI-yksiköihin", but the worked example then (correctly) works in AU/vrk — say "yhteensopiviin yksiköihin (yleensä SI)" so the example does not contradict the rule.
- solutions.md:104 (fy1-5-L3-02) — only the probe's motion is justified as negligible; the Earth moves about 0,03 AU (30 km/s · 1,5·10⁵ s) in the same time, still about 0,02 % — add it in one clause, or the task text could say "Maan ja luotaimen liike".
- solutions.md:19 / exercises.json fy1-5-L1-02 — 360 m in 45 s (8,0 m/s, the 400 m pace of an elite sprinter) is called "nopeaa juoksua"; say "huippujuoksijan vauhti" or pick a slower runner.
- inquiry.json:112 (koe-1) and koe-2 — the table starts at the initial state t = 0, where s/t is undefined; ask for the quotient "hetkillä t > 0".
- lesson.md Lineaarinen malli / Esimerkki — solar gravity explains only about 0,07–0,09 AU of the 0,2 AU model–JPL gap over 7–8 years (a = GM/r² ≈ 4·10⁻⁷ m/s²); the text never claims it explains all of it, so keep the hedged wording.

## Checked
- All 12 exercise answers recomputed independently from the task text; each matches answers.py and exercises.json within tolerance (3419,8 vrk; 41,58 h; 90 m; 1715 m → 1,7 km etc.).
- Worked example: 2922 days (2018-11-05 → 2026-11-05, leap days 2020, 2024), 0,0088602 AU/vrk, Δs = 25,89 AU, s = 145,6 AU = 2,18·10¹⁰ km; model at 2026-02-15 = 143,26 AU vs JPL 143,05 AU (0,15 %); 3,24 AU/yr check; 3420 d ends 2028-03-17 (maaliskuu 2028).
- Siirto 390 m and its mistakes 1092, 270; tarkistus-2 s₀ = 4,0 m and its mistakes 7, 3; exit ticket 17 m / 29 m / 12 m and 3,0 m/s, 8 m; misconception 10 m → 14 m.
- Every prediction, Etsi virhe and experiment-question correct option and feedback number (5,0 vs 3,5 m/s; 23 m vs 33 m) is right.
- Formulas s = s₀ + vt, Δs = vt, v = Δs/Δt with their conditions (straight line, one direction, v > 0) are stated and inside FY1 scope (linear model, direct proportionality); no forces or vectors beyond the sign remark.
- Figure 1: equal 115 px spacings; figure 2 to scale (68,8 px/s, 9,6 px/m): slopes 3 m/s, s₀ = 5 m, triangle Δt = 2 s, Δs = 6 m.
- sim.js implements s = s₀ + vt exactly; ranges (s₀ ≤ 10 m, v ≤ 5 m/s, t ≤ 10 s) stay within the 60 m track and graph; the slope readout Δs/4,0 s = v is right; s and ds are in simState; no ratio is shown.
- koe-1 and koe-2 lock s₀ and v and vary only t; the initial states (0; 2) and (6; 2) give the quoted values; captures confirm the locked controls and readout.
- Model assumptions (constant speed, no friction, the cart at full speed from the start) are in Mallin oletukset; values are called model values throughout.
- Solutions follow the seven steps, solve symbolically before substituting, convert units correctly, justify the rounding and check reasonableness with a genuine independent check.
