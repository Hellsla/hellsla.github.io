VERDICT: PASS
CONTENT-HASH: 67fac107b7b678a0

## Blocking

## Polish
- exercises.json:90 (L3-02) — "Mammografiassa käytetään noin 30 keV:n röntgensäteilyä": mammography tubes run at about 25–35 kV, so the mean photon energy is about 17–22 keV. Write "noin 30 kV:n jännitteellä; oletetaan fotonien energiaksi 30 keV" so that the data stay the same.
- solutions.md:49 (L1-05 Järkevyys) — "pienenee selvästi alle 50 %" reads as "falls below 50 %". Write "pienenee selvästi alle puolella: noin 15 %".
- L3-03 — the half-value thickness is a narrow-beam value. A real syringe shield needs somewhat more lead because of scatter (buildup). One clause in the Periaate is enough.
- L2-02 — Am-241 also emits alpha particles. The task is right as written (sealed source, gamma used); this is optional context only.

## Checked
- One script recomputed every answer from the task text: 25 %, 37,7→38 MBq, 5,7 mSv, 0,10 J, 31,5→32 kBq, 17 029→17 000 a, 0,303 mm, 572,5→570 d, 10 µSv, 15,6→16 Gy, 8,87→8,9, 16,9→17 mm. All are within tolerance, and answers.py agrees.
- Data against references: steel d½ 0,73 mm at 60 keV (NIST Fe, 0,730 mm); Pb 3,9 mm at 511 keV; FDG 0,019 mSv/MBq (ICRP 128, web-confirmed); Tc-99m 6,01 h; Am-241 432 a; C-14 5700 a (same as the decay-law chapter); 5,1 mSv natural (same as fy8-13); 30 µSv/h at 1 m after an FDG injection is realistic.
- L2-04 states the point-source and constant-rate assumptions, and the solution uses them.
- L3-01 entrance factor 1,3; the beams add only at the tumour, and the Järkevyys (about ¼ of 60 Gy) holds.
- L3-02 uses the d½ values of the lesson's 30 keV table, and the ratio is solved symbolically first.
- L1-04 Järkevyys ΔT ≈ 0,0005 K is correct.
- Rounding and the stated limiting data are consistent; units are converted correctly (min→h, g→kg).
