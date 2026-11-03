VERDICT: PASS
CONTENT-HASH: dee2764a7a7b4845

## Blocking

## Polish
- lesson.md:282 — Recomputed with WMM2025 (pygeomag WMM_2025.COF, epoch 2025.9; IGRF-14 agrees to 0.1): Helsinki F 52.6 µT, H 14.8, Z 50.4, I 73.7°, D 10.3° E; Hanko I 73.4°; Rovaniemi D 13.3°; Utsjoki I 78.9°, D 15.6°. Fix: write "noin 73°–79°" and "etelässä noin 10°, Lapissa noin 15° itään".
- lesson.md:319/325/378 — The value credited to WMM2025 is rounded down: the model gives 52.6 µT (53 µT) and B_h ≈ 15 µT. The lesson's 14 µT comes from rounding 52 µT and 74° first. Fix: write "noin 52–53 µT" and call 14 µT the rounded course value, or use 15 µT throughout (lesson text, sim BH, lesson-answers).
- lesson.md:323/325 — 45 T is no longer the record. As far as I know, Hefei reached 45.22 T in 2022 and an NHMFL test coil 45.5 T in 2019. Fix: write "noin 45 T" and describe NHMFL's magnet as its 45 T hybrid magnet, not as the record holder.
- lesson.md:446 — "joidenkin senttimetrien päässä": a school bar magnet gives millitesla a few centimetres away; the sim gives 30 µT at 10 cm. Fix: "noin kymmenen senttimetrin päässä".
- lesson.md:371 — "siihen vaikuttaa vain vaakakomponentti": the vertical component does act on the needle; it just cannot turn it in the horizontal plane. Fix: use the sim box's wording, "vain vaakakomponentti kääntää sitä".

## Checked
- I recomputed the inquiry numbers with my own pole-pair model and they agree. exp-1: B_m 30,0/15,5/9,15/2,87 µT, θ 65,0/47,9/33,2/11,6°, ratio 10,4; readout 10,3 is inside the tolerance. exp-2: θ 90°/−90°/90°.
- Worked example 18 µT (17,9); virhe 22,8 µT and 52°; siirto 37,6° with its mistakes 55,0°, 59,0° and 52,4°; B_h 14,3 and B_v 50,0.
- Figures: vector-sum is to scale (14 : 20, S pole facing the compass); inclination is drawn at 74,0°.
- Predictions and checks: each has exactly one right option and correct distractor feedback. In the two-magnets figure, the like poles cannot be told apart, as the feedback says.
- Sim: the pole model is stated in its box, the lines inside the magnet are hidden, simState gives theta and Bm, and the locked parameters isolate r and φ.
- Domains, Curie point 770 °C, no monopole, and no para- or diamagnetism, as the scope requires.
- Earth: magnetic S pole near the geographic north, dynamo, dipole tilt about 10° (IGRF about 9°).
