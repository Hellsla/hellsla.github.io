VERDICT: PASS
CONTENT-HASH: 9ed4393847194be0

## Blocking

## Polish
- solutions.md:272 (L2-11 Part c) — "as the STUK expert in the article also says": the expert does not say it. The article's own text calls mobile-network radiation non-ionising. The fact is on the page, the speaker is not — "as the article also states" (same remark as on the Finnish set).
- solutions.md:273 (L2-11 Part d) — "The marketing presents neither" is the solution's own conclusion — add "judging by the article".
- exercises.json (L2-11 text) — the definition of the Faraday cage sits inside "The professor says …"; in the article it is the journalist's sentence — "the article describes a Faraday cage as …".

## Checked
- Delta round 1: fy7-9-L2-10 (FY7-A2) and fy7-9-L2-11 (FY7-A3) judged, plus fy7-9-L1-09 and fy7-9-L2-09, which are also in the English diff, and five captions that lost "(example data)". Hash identical at start and end.
- English against Finnish by script: answers, units, tolerances, kinds, figure id and every number of the four solutions are the same.
- L2-10 recomputed: $f = c/\lambda$ = 6.122, 4.511 and 3.563 $\cdot 10^{14}\,\text{Hz}$ (356.3 THz); visible edges 4.0 and 7.9 $\cdot 10^{14}\,\text{Hz}$; $b/300\,\text{K} = 9.66\,\mu\text{m}$, 11.5 times 0.842 µm; $b/0.842\,\mu\text{m} = 3442\,\text{K}$. answers.py agrees.
- L2-10 source fetched 16 Nov 2026 (HTTP 200): 13 spectral bands; under "Sentinel-2 Level 3 Quarterly Mosaics" the table "Spectral Bands" gives B02 Blue 0.49, B04 Red 0.665, B08 NIR 0.842; values transformed to reflectance. All there.
- L2-11 recomputed: $\lambda = 8.57\,\text{cm}$, $E = hf = 2.319 \cdot 10^{-24}\,\text{J} = 14.48\,\mu\text{eV}$; 10 eV is $6.9 \cdot 10^5$ times larger, 1 keV $6.9 \cdot 10^7$. Shown 14 µeV is 3.3 % off, inside the 4 % tolerance.
- L2-11 source fetched (HTTP 200): protection only where the fabric covers and depending on its density; no Faraday cage when head and hands come out; continuous conducting shell; conductive paint against radio-frequency interference; STUK: no health harm by present knowledge, exposure below the limits. The English task summary and the solution match the page.
- Scope: L2-11 gives $E = hf$ and names the later course; L2-10 d) rightly judges the claim wrong (reflected sunlight).
- L1-09: $T = b/\lambda_\text{max} = 8279\,\text{K}$ (MAFY $b$), shown $8.3 \cdot 10^3\,\text{K}$. L2-09: figure curve at 2415 K peaks on the 1.2 µm grid line; shift $2.898 - 1.2 = 1.698\,\mu\text{m}$.
