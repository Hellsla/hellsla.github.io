VERDICT: FAIL
CONTENT-HASH: 3a91930e0895b369

## Blocking
- lesson.md:6 and lesson.md:99 (also solutions.md:15, inquiry.json:235 exp-2 solution) — one symbol, two quantities: $\Delta x = x - x_\text{oikea}$ is the (signed) measurement error, then $\Delta x = (x_\text{max}-x_\text{min})/2$ is the error estimate (always positive, written as $\pm\Delta x$). The exp-2 solution calls $\bar{t}-T$ "$\Delta t$" right after the lesson defined $\Delta t$ as the half-range. This conflates error with uncertainty, the very distinction the lesson teaches. — Give the error its own symbol (e.g. $e = x - x_\text{oikea}$, or $\delta$ as the sim already does) in lesson.md:6, L1-02 and the exp-2 solution; keep $\Delta x$ for the estimate only.
- solutions.md:109 (L3-02 Järkevyys) — "pienentää suhteellisen virheen sataanosaan" is wrong: about 500 % → about 2 % is a factor of 250 (the number of sheets). — Write "250-osaan" (= 1/n).

## Polish
- solutions.md:28 (L1-03) — lesson.md:131 says an error estimate is rounded to one significant figure (two if the first is 1), so a student following it answers 0,4 s, which the 2 % tolerance rejects. — Say in the solution that 0,35 s is the exact half-range and as a stated error estimate it would be 0,4 s; or ask for "vaihteluvälin puolikas tarkasti".
- lesson.md:258 — the summary drops the "two figures if the first digit is 1" exception stated at lesson.md:131 (and used in the worked example's 0,12 s). — Add it.
- inquiry.json:115 (sim `model`) — $\delta_\text{sat}$ is the standard deviation of the fixed normal series, so the 40-reading half-range is about 1,7·δ_sat (0,26 s at 0,15 s); a student may wonder why Δt ≠ δ_sat. — Add one sentence: δ_sat is a typical single-reading deviation; the half-range of many readings is larger.
- solutions.md:19 (L1-02) — 3 mm on 20 cm (1,5 %) is not a "tavallinen suuruus mittanauhalle"; a tape is good to about 1 mm. — Say it is a large error for a tape, pointing to a systematic cause.
- sim.js:1314 — dots are binned to 0,04 s, so a dot can sit up to 0,02 s off its true reading; at n = 1 the dot (2,18 s) is visibly right of the mean line at 2,18 s. — Bin to 0,02 s or draw the dot at its exact x.

## Checked
- All 12 exercise answers and all inquiry numbers recomputed independently; match answers.py and exercises.json (tolerance relative).
- Sim series: n=1 −0,22 s; n=5/40 half-range 0,25/0,26 s; n=40 mean error −0,0005 s; exp-2 mean 2,6995 s; exp-3 0,525/0,085 = 6,18 (mistake 6 outside 3 %).
- Worked example: 19,09 s, 3,18 ± 0,12 s, 3,8 %, five of six inside — correct.
- Figure numbers: error-types means 2,41 / 2,59 s, range-half, example-plot positions all to scale.
- Thermometer data, siirto (5,44 g and its mistakes), check-2 2,1 %, exit ticket (19,9 g, 2,0 %).
- L3-01 sign reasoning (−0,06 s) and L3-03 (0,26 cm) correct.
- Experiments isolate their varied parameter; simState gives mean, puoli, vir.
- Scope: within FY1 central contents (mittaaminen, luotettavuuden arviointi).
- Hash identical at start and end.
