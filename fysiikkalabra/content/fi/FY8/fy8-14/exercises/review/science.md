VERDICT: PASS
CONTENT-HASH: 264082239c93f4c3

## Blocking

## Polish
- exercises.json L3-02 — the task now says that the mean energy is about 20 keV and then assumes 30 keV without a reason. This is honest but odd. Add "jotta voidaan käyttää luvun taulukon arvoja", or drop the 20 keV clause.
- solutions.md L1-05 Järkevyys — "pienenee selvästi alle 50 %" still reads as "below 50 %". Write "vähemmän kuin puolella: noin 15 %". Carried over from round 1.
- L3-03 — the half-value thickness is a narrow-beam value; buildup from scatter means a real shield needs somewhat more lead. One clause would cover it. Carried over from round 1.

## Checked
- One script recomputed every answer from the task text: 25 %, 37,7 → 38 MBq, 5,7 mSv, 0,10 J, 31,5 → 32 kBq, 17 029 → 17 000 a, 0,303 mm, 572,5 → 570 d, 10 µSv, 15,6 → 16 Gy, 8,87 → 8,9, 16,9 → 17 mm. All are within tolerance, and answers.py agrees.
- L3-02 keeps the 30 keV values from the lesson's table (1,8 / 0,27 cm). The answer is unchanged and is solved symbolically first.
- L2-04 states the point-source and constant-rate assumptions, and the solution uses them. L1-02 states that no tracer leaves the body.
- L3-01: the entrance factor 1,3, the single-beam path and the reasonableness check (about ¼ of 60 Gy; 78 Gy with one beam) are correct.
- Data agree with the lesson: Tc-99m 6,01 h, Am-241 432 a, C-14 5700 a, 5,1 mSv/a, FDG 0,019 mSv/MBq, Pb 3,9 mm at 511 keV, steel d½ 0,73 mm at 60 keV.
- Rounding follows the limiting data, and the unit conversions are correct (min → h, g → kg, a → d).
