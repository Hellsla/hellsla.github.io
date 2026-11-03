VERDICT: PASS
CONTENT-HASH: 311b8a552540fc24

## Blocking

## Polish
- lesson.md:326–338, 658; inquiry.json ennuste-3; lessons/FY8/fy8-13/answers.py docstring — the 5,9 mSv total is confirmed (STUK), but the breakdown and its year could not be verified here (stuk.fi not reachable from this session). Search results tie 5,9 mSv to STUK-A263 (2020, data from 2018), which gives radon "noin 4 mSv", medical use 0,76 mSv and other natural sources about 1,1 mSv; no source found for 4,1 / 0,6 / 0,5 / 0,4 / 0,3 or for "arvio vuodelta 2023" — check against STUK's current "Suomalaisten keskimääräinen säteilyannos" page and correct the year and health-care figure if they differ (0,76 would still be the second-largest source, so no option changes).
- lesson.md:382 — 94 Bq/m³ is the widely quoted STUK average (older surveys 96 Bq/m³); keep, but cite the survey year next to it as for the dose table.
- lesson.md:553 (Puoliarvokerros) — Cs-137 in lead is usually given as about 6,5 mm; "noin 6 mm" is acceptable (C), and concrete about 5 cm is right.

## Checked
- All numbers recomputed in one script: Esimerkki 1,67 mGy → 33 mSv → 4,0 mSv; Etsi virhe 1,2 mSv; siirto 12,5 µSv and mistakes 37,5 / 25 / 50 / 750; tarkistus-2 5,0 cm (figure read: 80 → 40 at 5 cm); 1 Gy → 0,00024 K; radon share 69 %, natural 90 %.
- ICRP 103 w_T list complete, sum 1,00; w_R gamma/beta 1, alpha 20, neutrons 2,5–20 correct.
- STM 1044/2018 reference levels 300/200 Bq/m³; Säteilylaki 859/2018 limits 20 mSv/a (worker) and 1 mSv/a (public, not natural or own medical exposure); background 0,05–0,30 µSv/h; ~300 lung cancers/a; Rn-222 3,82 d, Po-218/Po-214 alpha — all consistent with what I know/found.
- Bar chart lahteet to scale (63,5 px/mSv) and matches the table.
- sim.js: Hdot = 40·(1/r²)·(1/2)^(x/6); model limits (no air attenuation, no scatter build-up, no background) stated in the sim box and the theory.
- Experiments isolate r and x; ennusteet have exactly one right option, every distractor's feedback correct.
- Inverse-square law conditions (small source, little air attenuation) stated where used.
- Exit ticket and tarkistus-3 model answer agree with the theory.
