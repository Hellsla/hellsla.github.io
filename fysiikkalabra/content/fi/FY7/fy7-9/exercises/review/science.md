VERDICT: PASS
CONTENT-HASH: 15d1f36f8fbd294e

## Blocking

## Polish
- solutions.md:272 (L2-11 Kohta c) — "kuten artikkelissa Säteilyturvakeskuksen asiantuntijakin sanoo": the expert does not say this. The article's own text says his remit is the supervision of "ionisoimattoman säteilyn – kuten juuri matkapuhelinverkkojen radiotaajuisen säteilyn". The fact is in the source, the speaker is not — write "kuten artikkelikin toteaa".
- solutions.md:273 (L2-11 Kohta d) — "Kumpaakaan ei markkinoinnissa ole esitetty" is the solution's own conclusion; the article only reports the marketing claims and the experts' view that they are unscientific — add "artikkelin perusteella".

## Checked
- Delta round 1: only fy7-9-L2-10 (FY7-A2) and fy7-9-L2-11 (FY7-A3) judged, plus five captions that lost "(esimerkkiaineisto)" (no number changed); hash identical at start and end.
- L2-10 recomputed: $f = c/\lambda$ = 6,122, 4,511 and 3,563 $\cdot 10^{14}\,\text{Hz}$ (356,3 THz; 0,49 µm limits B02 to two figures); visible edges 4,0 and 7,9 $\cdot 10^{14}\,\text{Hz}$; $b/300\,\text{K} = 9{,}66\,\mu\text{m}$, 11,5 times 0,842 µm; $b/0{,}842\,\mu\text{m} = 3442\,\text{K}$. answers.py agrees; tolerance 2 % also covers $c = 2{,}998 \cdot 10^8\,\text{m/s}$.
- L2-10 source fetched 16 Nov 2026 (HTTP 200): 13 spectral bands; under "Sentinel-2 Level 3 Quarterly Mosaics" the table "Spectral Bands" gives B02 Blue 0.49, B04 Red 0.665, B08 NIR 0.842; the products are reflectance. All attributed values are there.
- L2-10 d): the claim is rightly judged false. At 0,842 µm a 300 K surface emits practically nothing, so the band measures reflected sunlight; a thermal camera works at 8–14 µm, as the brief says. Wien's law in kelvins, black-body approximation stated.
- L2-11 recomputed: $\lambda = c/f = 8{,}57\,\text{cm}$, $E = hf = 2{,}319 \cdot 10^{-24}\,\text{J} = 14{,}48\,\mu\text{eV}$; 10 eV is $6{,}9 \cdot 10^5$ times and 1 keV $6{,}9 \cdot 10^7$ times larger. Shown 14 µeV is 3,3 % off, inside the 4 % tolerance.
- L2-11 source fetched (HTTP 200): the Faraday cage as a continuous conducting shell, protection only where the fabric covers and depending on its density, conductive paint used against radio-frequency interference, "samaa säteilyä kuin kaikki muukin", STUK: no health harm from 5G by present knowledge, exposure under the limits. All there.
- L2-11 scope: the photon belongs to FY8, but the teacher's assignment asks for it; the task gives $E = hf$, $h$, the eV and the ionisation limit and names the later course, so nothing unstated is needed.
