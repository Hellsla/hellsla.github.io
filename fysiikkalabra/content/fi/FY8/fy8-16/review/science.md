VERDICT: PASS
CONTENT-HASH: fc98bdf258eb85cf
Mode: full (coordinator 2026-11-14: the change adds a number, nickel-62). Hash the same at start and end.

## Blocking

## Polish
- inquiry.json ennuste-2 (correct option) — "mistä tahansa galaksista katsottuna muut loittonevat samalla tavalla" is the idealised model and now reads a little more absolute than the theory, which says "keskimäärin kaukaiset galaksit" and lets nearby galaxies approach each other. This is a C simplification, because the prompt says "Lähes kaikki" and the feedback describes uniform expansion. For an exact match the option could say "kaukaiset galaksit loittonevat keskimäärin samalla tavalla" (fi, en, fi-easy).
- lesson-answers.py:575 — the comment says the least-squares slope is 69,7 km/s/Mpc, but the script computes 69,83. The comment only; no text a student reads uses it.

## Checked
- New sentence (1), fi/en/fi-easy: true. Hubble flow on average, peculiar motion plus gravitation of neighbours (Andromeda approaches), and bound systems do not expand. It agrees with "Avaruus itse laajenee", the misconception section ("kaukaisten galaksien … keskimäärin samassa suhteessa"), the ennuste-2 feedbacks and the Kaava section's peculiar-velocity sentence.
- New sentence (2): B/A from AME2020 atomic masses (my script): Ni-62 8,7945, Fe-58 8,7922, Fe-56 8,7903, Ni-60 8,7808 MeV. So "suurimmillaan raudan ja nikkelin alueella, noin 8,8 MeV" and "suurin arvo nikkeli-62:lla" are right. Prior, criterion and Tiivistelmä ("rautaan asti") are a fair C simplification of the same region. Tarkistus-3 model answer agrees in all three languages. Figure label Fe-56 is left as the teacher decided.
- Recomputed in one script: the eight galaxies (v, z, Δλ), the LSQ fit of 69,8, galaxies 1/3/5/7 above the line, hook 669,4 / 495,8 nm = 2,0 %, the spektri figure's line positions in px against its 400–720 nm scale, 1/H0 = 4,41·10¹⁷ s ≈ 1,4·10¹⁰ a, the virhe task's 1,4·10¹³ a, the worked example (z = 0,035045, v = 10 506 km/s, H0 = 70,0), siirto 86,0 Mpc and its mistakes 84,3 / 86 000 / 6020, tarkistus-2 72, 1/72 → 13,6·10⁹ a, koe-1 mistake 0,0143.
- CMB: stretch 3000/2,725 ≈ 1100, Wien peak 1,06 mm (966 nm at release: "lähi-infrapuna" right), 13,6 eV ↔ 91 nm.
- BBN n:p = 1:7 → Y = 25 %. Planck 2018: 4,9 / 26,2 / 68,9 %. Triple-alpha 7,27 MeV. Timeline: Sun at 9,2 Gyr.
- Laajeneminen figure: distances ×1,5 to scale, displacements 1:2:3.
- Sim: v = 70d + own motion, z = v/c, λ = λ0(1+z). simState has d, dlam, z, v for koe-1, which varies galaksi only. Its limits (invented values, small z, exaggerated stretch) are stated in Mallin oletukset.
- Every prediction, check and error-spotting choice has exactly one correct option, and every distractor's feedback is right.
- Scope: within FY8 "maailmankaikkeuden kehitys" and its täsmennys.
