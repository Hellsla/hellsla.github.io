VERDICT: FAIL
CONTENT-HASH: fc0964a3bca0df91

## Blocking
- lesson.md:569 — A (outdated fact): "Loppusijoitus voi alkaa, kun valtioneuvosto on myöntänyt luvan" — the government granted Posiva's operating licence on 22.10.2026, valid to the end of 2070 (STUK's favourable statement was 4.8.2026, which is correct). — Write e.g. "Valtioneuvosto myönsi käyttöluvan lokakuussa 2026 vuoden 2070 loppuun. Loppusijoitus voi alkaa, kun STUK on tarkastanut laitoksen." The teacher should confirm this against valtioneuvosto.fi (web search, several news sources).
- lesson.md:610 and inquiry.json:286 (keskustelu model) — A: "aseessa tarvitaan yli 90 %" / "ydinräjähdys vaatisi yli 90 %:n rikastuksen" is false as a requirement: weapons-grade uranium is about 90 %, and Little Boy averaged about 80 %. The argument only needs the contrast with 3–5 %. — Write "ydinaseissa käytetään noin 90 %:iin rikastettua uraania" (or "erittäin korkeaa rikastusta").

## Polish
- lesson.md:3 vs 549 — the hook says "noin kolme ja puoli tonnia" and the answer says "noin 3,4 tonnia" (3,42 t). Use one value.
- lesson.md:392 — "Kun sauvoja lasketaan syvemmälle": the control rods of the boiling water reactors OL1/OL2 are pushed in from below. "työnnetään syvemmälle" is neutral.
- inquiry.json:102 (ennuste-2, distractor 2200) — "noin 80" is 0,04·1987 = 79 (series value). With the model 1000·1,04^20 it is 88. Fine as it stands; it could say "lähes 90" if the model value is meant.

## Checked
- Worked example Q = 173,28 MeV, D–T 17,59 MeV, 0,08 %, 3,5 vs 0,85 MeV/nucleon, 1 g U-235 → 82 GJ → 3,42 t coal, hook 14 400 t/d (at an assumed 40 % efficiency): all recomputed.
- Binding-energy figure values (D 1,1 … U-235 7,6) and Tarkista 2 (236·0,9 ≈ 210 MeV, mistakes 0,9 / 106) are right.
- Sim: k = 1,2 − 0,008 s, absorption probabilities add up (escape fixed at 0,52), Koe 1/2 numbers 39 387 / 934 / 7 and 1437 / 1987 / 3264 are reproduced by lesson-answers.py; the model's limits are stated.
- Etsi virhe −0,8226 u → −766 MeV; ITER 1,77·10^20 1/s, mistakes 1,77·10^6 and 0,156, 1,5 mg.
- Verified on the web: STUK statement 8/2026; nuclear share 39 % in 2024 (Tilastokeskus); OL3 core about 128 t U ("noin 130 t" is fine).
- From knowledge, consistent with the lesson: Loviisa 1977/1981, OL1 1979, OL2 1982, OL3 regular production 2023; licences Loviisa to 2050 (2023) and OL1/OL2 to 2038 (2018; extension to 2048 is only at the EIA stage); net 507/890/1600 MW; ITER 500 MW, Q = 10, D–T 2039 (2024 baseline). The teacher should check these against PRIS and ITER.
- Delayed neutrons 0,65 %, decay heat 6 % → 1–2 % after 1 h, IPCC 12 g/kWh vs coal 820, Cs/Sr/Pu half-lives, Onkalo at 430 m.
- Hash fc0964a3bca0df91 at the start and at the end.
