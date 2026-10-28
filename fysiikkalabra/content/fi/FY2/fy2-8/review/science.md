VERDICT: FAIL
CONTENT-HASH: f8483829c7f45bab

## Blocking
- assets/sims/fy2/fy2-8/sim.js:18 (with inquiry.json:112, :151, :140) — the 420 ppm level gives today's observed, still-rising temperature (+15 °C, from AR6's 1,1 °C for 2011–2020) as its "settled" value `Teq`. After about 20 s the readout says "asettunut", and koe-1 records it in the column "asettunut T". The 560 ppm level uses an equilibrium value (ECS 3 °C). So the sim mixes a transient value with an equilibrium one, and it tells the student that warming at today's concentration is finished. That contradicts the lag the sim exists to show. With the lesson's own ECS, 420 ppm settles at 14 + 3 · log₂(420 : 280) ≈ +15,8 → about **+16 °C**. Fix: set the 420 level's T to +16 (source: AR6 ECS 3 °C), keep "nykyisin noin +15 °C" as today's measured value in `model` and in the koe-1 feedback, and say that at today's concentration the temperature is still rising towards about +16 °C. Alternatively, label the 420 value "nykyinen (ei vielä asettunut)" and stop calling it settled.
- content/fi/FY2/fy2-8/inquiry.json:127, :140 (and :134) — the experiment's labels are not LaTeX (teacher's standing rule). `names.co2` shows on the page literally as "CO_2-pitoisuus" (shot exp-koe-1-390-1), and the measure label "asettunut T (°C)" has a plain T and °C. The table also lists the "0" level as "CO₂-pitoisuus 0 ppm → −18 °C", but that level also removes all water vapour and methane. The row therefore claims that CO₂ alone accounts for the whole 33 K. Fix: `names.co2` "$\text{CO}_2$-pitoisuus"; measure label "asettunut $T$ ($^\circ\text{C}$)" or whatever form the page renders; give `values.co2` entries for "0" ("ei kasvihuonekaasuja, ei vesihöyryä"), "280" and "560".

## Polish
- inquiry.json:140 — the measured key `Teq` is the level's constant, so a student can record a row before the thermometer has moved. Consider recording `T` with "Kirjaa mittaus" after the reading says "asettunut", or say in the intro to wait for it.
- lesson.md Ydinajatus — "kasvihuonekaasuja on hyvin vähän" (ennuste-1 feedback) cites only CO₂'s 0,42 ‰. Water vapour, the main absorber, is about 0,4 % on average. That is still small, so this is not wrong.
- packet vs disk: the packet's sim.js shows literal Finnish strings where the file on disk uses `__()` (same hash). Check review_packet.py's rendering.

## Checked
- Every lesson, inquiry and exit-ticket number recomputed in one script; all match lesson-answers.py (2,352 t → 2,4 t; 57,6 kg; 820 kg; 43,2 kg; 49 000 t; 0,049 t; 1200 t; 15,9 kg → 16 kg; 13,2 kg; 68 and 41 ratios).
- IPCC AR5 WG3 Annex III medians (820/490/230/41–48/24/12/11–12) and their rooftop/utility and onshore/offshore assignment are correct; the 69 g/MJ gasoline factor and 32 MJ/l are sound.
- m = e · E: units, conditions and scope are right. The lesson has no radiative balance and defers it to FY3.
- Sim physics: sunlight passes at every level; IR rate ∝ (T/255 K)⁴; absorbed share 0 / 0,80 / 0,84 / 0,88, exaggerated as stated; re-emission up or down at random; nothing in the sim creates energy.
- Time constant 3 s gives a half-life of 2,08 s, which matches "puolittuu noin kahdessa sekunnissa"; speed changes only the pace.
- −18 °C → +15 °C (33 K), 280 → 420 ppm (< 0,5 ‰) and pre-industrial +14 °C are consistent.
- Every correct option and every feedback in the predictions, koe-1, aineisto, alkuperä, muut perusteet, virhe (kWh²/g), kuljetus (8×) and tarkistus 1–3 is physically right.
- Figures: the greenhouse diagram is qualitative and labelled not to scale; the bar chart is to scale (361 px : 820 ≈ 0,44 px per g/kWh for every bar).
- Worked example and numeric solutions: all seven steps present, symbolic before numbers, and the rounding is justified.
