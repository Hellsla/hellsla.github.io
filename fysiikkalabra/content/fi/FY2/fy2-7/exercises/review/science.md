VERDICT: FAIL
CONTENT-HASH: 9e1eb93be5d4c588

Round 1 (new YO-skill task L2-08 added, teacher 2026-11-05; the rest of the set was PASS in round 2 and is unchanged).

## Blocking
- exercises.json:261 (L2-08, choice "Yhtä paljon molemmissa", feedback) — A, an invalid inference: "Tässä sekä osuudet että lähtevät energiat ovat eri suuria, joten tulokset eroavat." Different shares and different input energies do not imply different losses (e.g. 3 % of 900 MWh = 9 % of 300 MWh = 27 MWh). This contradicts the very point of the task, that the product decides. — Replace the second sentence with the numbers: "Tässä häviöt ovat $0{,}040 \cdot 1000\,\text{MWh} = 40\,\text{MWh}$ ja $0{,}090 \cdot 300\,\text{MWh} = 27\,\text{MWh}$, joten ne eroavat."

## Polish
- exercises.json:281 (L2-08, reason "valon nopeudella", feedback) — "Sähkö kulkee todella nopeasti" repeats the half-truth noted in round 2 for L2-07: the electrons drift slowly, the energy (the field) travels fast, close to but below the speed of light in a cable. Write "Energia siirtyy johdoissa todella nopeasti, …".
- solutions.md L2-08 Mallivastaus — the sentence "Häviävä energia muuttuu lämmöksi ympäristöön, ei katoa" is right but not asked; keep or drop.

## Checked
- L2-08 recomputed: electricity 0,040 · 1000 MWh = 40 MWh, district heat 0,090 · 300 MWh = 27 MWh; the electricity grid loses more. "yli kolminkertainen" is right (1000 : 300 = 3,3).
- L2-08: exactly one correct choice and exactly one correct reason; answer equals the correct choice text. Every other choice and reason is really wrong, and their feedback is right apart from the Blocking item.
- L2-08 data: 4 % and 9 % match the lesson's Energiateollisuus 2024 figures; the situation is marked "Esimerkkitilanteessa". Scope: only $E_\text{häviö} = p\,E_\text{lähtö}$, the lesson's model; $p$ is the symbol already used in L1-07, L2-05, L3-05.
- Two-stage form (type 1) fits docs/exercise-types.md: wrong reasons carry the common misconception (percentage alone), a true-but-irrelevant idea (length) and the speed-of-light misconception.
- Recomputed every numeric answer by running answers.py and comparing with exercises.json in one script: all 18 within tolerance; unchanged since round 2.
- Round-2 report stands for L1-01 … L3-05; the diff touches only L2-08 and an answers.py comment.
- The hash was unchanged at the start and at the end.
