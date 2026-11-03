VERDICT: FAIL
CONTENT-HASH: 6a18b2728fb388dc

## Blocking
- exercises.json fy7-4-L1-04 and fy7-4-L3-03; solutions.md; answers.py:1073,1087 — **A**: the Earth's field data credited to "Ilmatieteen laitos, Nurmijärven geofysiikan observatorio, 2024" do not match that source. FMI's Nurmijärvi secular-variation table gives F ≈ 52,8 µT and inclination I ≈ 73,6° (predicted epoch 2025.5). IGRF (2024.5): F = 52,5 µT, I = 73,8°, H = 14,6 µT, D = +10°. L1-04 is unaffected (1,01 N → 1,0 N); L3-03 depends on cos I: with 53 µT and 74°, I = 1,81 kA → **1,8 kA**, not 2,0 kA (13 % off; tolerance 2 %). Fix: use "noin 53 µT, 74° vaakatasoon nähden" in both tasks, cite the FMI Nurmijärvi annual mean (or "IGRF-malli, 2024"), and recompute L3-03 → 1,8 kA in exercises.json, solutions.md (B_h = 53·10⁻⁶ T · cos 74° = 1,46·10⁻⁵ T) and answers.py. Verify on space.fmi.fi/MAGN/secular (unreachable here; FMI values from a search summary).
- exercises.json fy7-4-L3-03; solutions.md L3-03 Periaate — **B**: "itä–länsisuunnassa" with "kenttä osoittaa pohjoiseen". The wire is perpendicular to the horizontal component only if east–west is *magnetic*. Declination in southern Finland is ≈ +10°, so a geographic east–west wire is not perpendicular to H, and "Lanka on kohtisuorassa kumpaakin vastaan" is then false. L1-04 handles this correctly ("kompassin osoittamaan"). Fix: "kompassin mukaan itä–länsisuunnassa" (and "magneettiseen pohjoiseen").

## Polish
- solutions.md L1-04 Järkevyys — the solution says the conductor weighs "satoja newtoneja" over 100 m; a line conductor for 200 A is about 0,5–1,5 kg/m, i.e. roughly 500–1500 N. Write "satoja tai tuhansia newtoneja" or name a mass per metre.

## Checked
- Recomputed all twelve answers with my own formulas; all except L3-03 (data issue above) agree with answers.py and exercises.json: 0,24 N; 0,19 N; 0,10 T; 1,0 N; 3,0 A; 3,2 mN; 0,074 T (least-squares slope through origin of the five plotted points 0,300 g/A); 30°; 18 m/s²; 2,4 A; 270 N repulsive.
- Figure balance-points: line through (0;0) and (6 A; 1,8 g), so (5,0 A; 1,50 g) and (3,0 A; 0,90 g) lie on it as the solution reads.
- Directions: L3-01 force up with the right current, tension 2mg reversed; L3-03 east current × north H = up, vertical component gives a horizontal force; L3-02 opposite currents repel.
- L1-04 geometry: wire along the magnetic meridian lies in B's vertical plane, so the angle = inclination.
- Reasonableness masses (25 g, 0,3 g, 36 g, 27 kg, 100 g) correct.
- Conversions, symbolic-first solutions, rounding.
