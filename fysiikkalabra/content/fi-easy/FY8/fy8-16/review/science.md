VERDICT: PASS
CONTENT-HASH: bcdc97b32687d881

## Blocking

## Polish
- lessons/FY8/fy8-16/lesson-answers.py:1079 — the comment says the least-squares fit is `69,7`; the code computes 69,83, and sim-spec.md and the koe-1 solution say 69,8 — make the comment say 69,8.
- inquiry.json ennuste-2, third option's feedback — "vetää kappaleita toisiaan kohti eikä hylkii niitä" is a grammar slip — write "eikä hylji niitä".

## Checked
- New nickel-62 sentence (lesson.md "Tähdet valmistavat…", tarkistus-3 model answer). It is correct: by AME2020 masses B/A is Ni-62 8,795 MeV, Fe-58 8,792 MeV and Fe-56 8,790 MeV, so "suurimmillaan raudan ja nikkelin alueella, noin 8,8 MeV" holds. The figure's Fe-56 label is the teacher's decision and not a finding. The criterion "vapauttaa energiaa vain rautaan asti" and the summary still agree with it.
- Worked example, recomputed: z = 0,035045, v = 10 506 km/s, H0 = 70,04 km/s/Mpc. Symbols come before numbers, the three significant figures are justified and the v = cz condition is checked.
- Hubble time: 1/H0 = 4,41·10¹⁷ s = 1,40·10¹⁰ a. The virhe task's wrong value is 1,4·10¹³ a, and its four options have exactly one correct answer.
- Siirto: z = 0,020081, v = 6020 km/s, d = 86,0 Mpc. The values of the mistakes are right: 84,3 (divided by the observed λ), 86 006 (c in m/s) and 6020 (the velocity).
- The 8 galaxies of the simulation: v = 70d + v_p matches lesson-answers.py, the feedback values (1800, 2840, 7560, 19 030 km/s; z 0,0060 and 0,0635) and the fit through the origin, 69,8. simState gives d, dlam, z and v. The varied parameter is the galaxy, and H0 changes only the drawn line.
- tarkistus-2 figure data: the least-squares slope is 72,4, so reading 72 from (250 Mpc, 18 000 km/s) is consistent. Age 13,6·10⁹ a. The 1/v·d mistake values are 0,0139 and 0,0143.
- Figures at stated scale: spektri line positions (656,3 → 689,1 nm and so on, 5,0 %), Hubble points against the pixel scale, the koostumus bar (4,9 / 26,3 / 68,8 %), and the binding-energy points at A = 56 and 62 (8,80 MeV).
- CMB: 3000/2,725 ≈ 1100, the Wien peak 1,06 mm, and 3000 K radiation peaking near 970 nm (the "lähi-infrapuna" feedback). The 13,6 eV ionisation argument is stated correctly as a photon-number threshold.
- BBN: n:p = 1:7 gives Y = 25 %, at ~10⁹ K and 3–20 min. The timeline checks: 13,8 − 4,6 = 9,2·10⁹ a.
- Planck composition (5/26/69 %), dark matter evidence, peculiar velocities, and the "no centre" model (B-class conditions on "keskimäärin" and local gravity are stated). Hash checked at the start and the end.
