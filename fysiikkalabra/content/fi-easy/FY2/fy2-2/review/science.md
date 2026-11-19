VERDICT: PASS
CONTENT-HASH: 09214a4f687ff460

## Blocking

## Polish
- inquiry.json:tarkistus-3 (model) — "Tankki tyhjenee, koska energia on muuttunut muotoon, jota ei enää helposti saa kerättyä" mixes two things: the tank empties because the petrol burns, and the energy is not lost but spread out as lämpöenergia. Suggest: "Tankki tyhjenee, koska bensiini palaa. Sen energia ei katoa, mutta hajaantunutta lämpöenergiaa ei saa helposti takaisin käyttöön."
- inquiry.json:ketju-lampo (solution, Järkevyys) — "Voimalaitoksissa niin on" is a weak check. The real check is the sum $66\,\text{MJ} + 34\,\text{MJ} = 100\,\text{MJ}$, and that the largest loss ($60\,\text{MJ}$) is at the plant.

## Checked
- Round 2's blocking item is fixed. The worked example's Tulos step now uses the subtraction rule: $450\,\text{kJ}$ is known to the nearest $10\,\text{kJ}$, so the answer is $340\,\text{kJ}$. Both round 2 polish items are also fixed: the photo caption says "lämpöenergiaksi", and the johtopäätös model says "jokaisessa vaiheessa osa".
- I recomputed everything in one script, and every value agrees with lesson-answers.py: example 340 kJ; the pysähdy answers 380 kJ, 4200 J, 3 MJ and 160; the chain 66 MJ (60 + 2 + 4); the transfer task 51 GJ; check 2 is 7,3 and check 3 is 100; the exit ticket 9 kJ; the Sankey 600 kJ; the common mistake 1800 kJ.
- Prediction 2: πR²·1361 W/m²·3600 s = 6,25·10²⁰ J ≈ 620 EJ, the same as humankind's use in 2023. The "tuhat vuotta" option comes to about 41 days, so "noin 40" is right. Every choice item has exactly one correct option, and the distractors' feedback is correct.
- The tikapuut figure is to scale: 33,2 px per decade. The points for 1 kJ, 10 MJ, 1,6 GJ and 140 TJ sit at 195,5, 328,5, 401,5 and 565,5 px, and the computed positions are 195,5, 328,2, 401,3 and 565,2 px.
- The säilyminen Sankey is to scale: the 96 px band splits into 24 + 72 px, which matches 800 = 200 + 600 kJ.
- sim.js magnitudes: the apple is 0,98 J, OL3 1,6 GW × 24 h = 1,38·10¹⁴ J, the tank 50 × 32 MJ = 1,6 GJ, Finland's electricity per day 7,9·10¹⁴ J, the gas bottle 5,1·10⁸ J and TNT 4,2·10⁹ J. A green photon, the Sun's luminosity and the M 9 earthquake are all plausible.
- koe-1 and koe-2: the initial objects exist as select values, and simState gives E_MJ and E_EJ. Each experiment varies only kohde, and there are no other parameters to hold fixed.
- The model box says the values are rounded magnitudes with sources or estimates, and that the scale is logarithmic.
- Scope: there is no E_k, E_p, W = Fs, Q = cmΔT or chain efficiency. The physics stays inside FY2's energy forms, conservation and the joule.
