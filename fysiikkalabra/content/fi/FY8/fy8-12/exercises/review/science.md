VERDICT: PASS
CONTENT-HASH: 844ef976147dad75
SCOPE: delta added-exercise from edbc5d57c6709a2b base 415cbc7c6bc3

## Blocking

## Polish
- exercises/solutions.md:232 — The phrase "(10 eV tai enemmän)" overstates the threshold, since some atoms ionise at about 4–5 eV. Write "suuruusluokkaa $10\,\text{eV}$" as the task does. The clause also lacks its verb: write "ei ole lähelläkään tätä".
- exercises/solutions.md:231 — "Gammafotonit ionisoivat, koska niiden energia on yli $10^{5}\,\text{eV}$": use the task's range, "suuruusluokkaa $10^5$–$10^6\,\text{eV}$, eli paljon yli ionisaatioon tarvittavan energian".
- exercises/solutions.md:232 — "miljoonasosia elektronivoltista": the energy is $1{,}4 \cdot 10^{-5}\,\text{eV}$, so "kymmeniä miljoonasosia" (or "sadastuhannesosia") is more accurate. This is a matter of wording only.

## Checked
- Hash 844ef976147dad75 at the start and the end. Only fy8-12-L2-08 was judged.
- Round-1 blocking item fixed: `answer` 14 µeV, and the Vastaus says "$14\,\mu\text{eV}$, kaksi merkitsevää numeroa", limited by the two figures in $3{,}5\,\text{GHz}$. The spec's suggested box value (15 µeV) was wrong, and 14 is right.
- Recomputed independently: $E = hf = 6{,}626 \cdot 10^{-34} \cdot 3{,}5 \cdot 10^{9} = 2{,}319 \cdot 10^{-24}\,\text{J} = 1{,}448 \cdot 10^{-5}\,\text{eV} = 14{,}48\,\mu\text{eV}$. answers.py gives 14,476 as well.
- Tolerance 0,04 (relative) accepts 13,44–14,56, which covers 14, 14,48 and the 14,5 that the solution says the box accepts.
- The ratios now stand on their own rows outside the substitution chain: $10/1{,}448 \cdot 10^{-5} = 6{,}9 \cdot 10^{5}$ and $10^{5}/1{,}448 \cdot 10^{-5} = 6{,}9 \cdot 10^{9}$. Both are correct, and "noin miljoona kertaa" fits $6{,}9 \cdot 10^5$ as an order of magnitude.
- The Vastaus's first paragraph holds the box value with its unit.
- The ANVS facts are still limited to the verified lines: ten products, RIVM, continuous ionising emission, low level and low risk, the skin limit at a year of 24 h a day, the sale ban, and sealed storage, not household waste.
- The principle (single-photon energy decides ionisation, not intensity) and the c) and d) physics are unchanged and correct.
