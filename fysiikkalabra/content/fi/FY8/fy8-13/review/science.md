VERDICT: PASS
CONTENT-HASH: e9e47c77f1bab9da

## Blocking

## Polish

## Checked
- Round-2 blocker fixed: inquiry.json tarkistus-2 Järkevyys now compares with Cs-137 in concrete ≈ 4 cm (agrees with lesson.md Puoliintumispaksuus and fy8-12) and correctly infers somewhat higher-energy radiation (d½ in concrete grows with energy in the Compton region).
- Round-2 polish fixed: lesson-answers.py section comment now cites STUK-A263 (2020).
- Tarkista 2 figure (shot fig-12) reads 80 → 40 µSv/h at 5,0 cm, 20 at 10 cm; 25 cm → 2,5 µSv/h; answer 5,0 cm and mistakes 10/40 right.
- Recomputed in one script: koe-1 40/10/4,44/2,50; koe-2 40/20/10/5,00, 30 mm 1,25; siirto 12,5 µSv and mistakes 37,5/25/50/750; esimerkki 1,67 mGy → 33 mSv → 4,0 mSv; virhe 1,2 mSv; 1 Gy → 2,4·10⁻⁴ K; ΣwT = 1. lesson-answers.py agrees.
- STUK-A263 breakdown (5,9; radon ~4; other natural 1,1; health care 0,76 → 0,8; < 0,1): table, to-scale bar figure, summary, hook and ennuste-3 feedback consistent; 86 % ≈ 85 %, 68 % ≈ two thirds, 5×.
- Exactly one correct option in kertaus, ennuste-1/2/3, virhe, tarkistus-1; distractor feedback physics correct.
- Sim (sim.js H1 = 40,0, DHALF = 6,0, (1/2)^(x/d½)) implements the stated model; limits (no air attenuation, no scatter build-up, no background) stated; koe-1/koe-2 isolate r and x.
- Inverse-square and half-value-layer conditions stated where used; w_R/w_T table per ICRP 103.
- Radon mechanism (decay products, Po-218/Po-214 alpha, winter underpressure) and tarkistus-3 model answer agree with theory; exit ticket agrees.
- Nothing else regressed since round 2.
