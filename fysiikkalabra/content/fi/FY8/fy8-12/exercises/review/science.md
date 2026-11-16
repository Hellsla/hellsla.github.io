VERDICT: FAIL
CONTENT-HASH: 6048e1bfb9aa68ef

## Blocking
- exercises/solutions.md:223, exercises/exercises.json (fy8-12-L2-08 `answer`) — A (rounding): the final answer is given as $14{,}5\,\mu\text{eV}$ "kolme merkitsevää numeroa", although the only datum, $3{,}5\,\text{GHz}$, has two, as the same paragraph admits. $14{,}48$ rounds to $14\,\mu\text{eV}$ (the brief's "15 µeV" was wrong too). Fix: `answer` 14, with Vastaus "$14\,\mu\text{eV}$, kaksi merkitsevää numeroa kuten taajuudessa". Tolerance 0,04 still accepts 14,48 and 14,5.

## Polish
- exercises/solutions.md:224 — "(10 eV tai enemmän)" overstates the claim, since some atoms ionise at about 4–5 eV. Write "suuruusluokkaa $10\,\text{eV}$", as the task does. The sentence also lacks a verb ("ei ole lähelläkään").
- exercises/solutions.md:223 — "Gammafotonit ionisoivat, koska niiden energia on yli $10^5\,\text{eV}$": use the task's "suuruusluokkaa $10^5$–$10^6\,\text{eV}$".
- exercises/solutions.md:209 — Write $\text{J}\,\text{s}$ as in the lesson and glossary, not $\text{Js}$.

## Checked
- Hash 6048e1bfb9aa68ef at the start and the end. Only fy8-12-L2-08 was judged.
- Recomputed: $E = hf = 2{,}319 \cdot 10^{-24}\,\text{J} = 1{,}448 \cdot 10^{-5}\,\text{eV} = 14{,}48\,\mu\text{eV}$. answers.py also gives 14,476. The ratios $6{,}9 \cdot 10^5$ and $6{,}9 \cdot 10^9$ are correct.
- Every ANVS fact in the text, Annettu and a) is in the verified lines: ten products, RIVM, low level, the skin limit at a year of 24 h a day, the sale ban, storing sealed in a cabinet, and not in household waste. No health claim is invented, and the claims are inferred from the names and labelled as inference.
- Principle: ionisation depends on the single-photon energy, not on intensity. This is correct at the level.
- c) is labelled a general method, not RIVM's. Background subtraction, distance, counting time and absorbers for identifying the radiation type are correct.
- d): the anti-5G claim is physically wrong and the product's ionising radiation is a real effect. The classification is correct.
