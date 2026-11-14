VERDICT: PASS
CONTENT-HASH: 9fc38bb9ac8250fa

## Blocking

## Polish
- lessons/FY8/fy8-16/lesson-answers.py:1076 — the comment says the least-squares slope is 69,7 km/s/Mpc; the code computes 69,83 and koe-1's solution and sim-spec rightly say 69,8 — make the comment 69,8 (comment only, no value changes).

## Checked
- Nickel-62 sentence (lesson.md:386, tarkistus-3 model): correct. Ni-62 has the highest binding energy per nucleon (8,795 MeV), above Fe-58 and Fe-56 (8,790 MeV), and "the region of iron and nickel" fits the figure (Fe-56 and A≈62 are both at 8,80 MeV at the figure's scale). The Fe-56 label is the teacher's decision and is not judged.
- One script recomputed every number: hook lines 669,4/495,8 nm (z = 0,020); figure spektri positions and 689,1 nm; galaxies 1–8 (d, v, z, Δλ) and their eight plotted points in figure hubble; least-squares H0 = 69,8, 1/H0 = 14,0·10⁹ a; dashed reading 200 Mpc → 14 000 km/s.
- Worked example: z = 0,035045, v = 10 506 km/s → 1,05·10⁴, H0 = 70,0 to 3 s.f. (limited by 23,0 nm and 150 Mpc); solved in symbols first; v = cz holds because z < 0,1.
- Hubble time 4,41·10¹⁷ s = 1,40·10¹⁰ a; 1 Mpc = 3,26·10⁶ light years; the virhe task's 4,4·10²⁰ s and 1,4·10¹³ a; each distractor's feedback is correct.
- Siirto: 86,0 Mpc; the mistakes 84,3, 86 000 and 6020 come from the errors they name. Tarkistus-2: 18 000/250 = 72, line drawn with slope 72 (figures.py), 1/H0 = 13,6·10⁹ a, mistake 0,0139.
- CMB: stretch 3000/2,725 ≈ 1100, Wien peak 1,06 mm, "not enough photons above 13,6 eV" (not the mean photon); BBN n:p = 1:7 → Y = 25 %; Planck 2018 split 4,9/26,2/68,9 % and bar widths to scale.
- Expansion figure (×1,5, shifts 1:2:3), timeline (9,2·10⁹ a = 13,8 − 4,6), and the dates 1927, 1929, 1965, 1998, 2017.
- Predictions, recap and checks: exactly one correct option each; distractor feedback physically right; ennuste-2 gated on the theory.
- koe-1: initial galaksi 1, H0 50; simState gives d, dlam, z, v; varying the galaxy alone isolates d; the sim's model (v = 70d + own motion, λ = λ0(1+z)) matches lesson-answers.py, and its limits (invented values, small z, exaggerated wave) are stated in the model box.
- Fusion up to the iron group, neutron capture in supernovae and mergers, and the dark-matter evidence: the causal statements are correct for this level.
