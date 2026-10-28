VERDICT: PASS
CONTENT-HASH: e6d7ee0e2e1ea72d

## Blocking

## Polish
- solutions.md L2-03, L3-01, L3-03 (`\dfrac{m}{e}`, `\dfrac{m_\text{bensa}}{E}`, `\dfrac{120\,\text{km}}{100\,\text{km}}`, `\dfrac{74 \cdot 30 \cdot 36\,\text{g}}{25}`) — the teacher's rule is written division with a colon, as the lesson does ($820 : 12$). Write `E = m : e`, `V = 120\,\text{km} : 100\,\text{km} \cdot 6{,}0\,\textsf{l}` and so on.
- The set is 12 of 12 the same `m = e \cdot E` computation. Level 3 is "reasoning" in name only: L3-02 is a sum of two products. Give two level-3 tasks a closing interpretive sentence the student answers (not only a number), for example in L3-01 "Mitä tulos kertoo sähköauton hyödystä kivihiilisähköllä?", and add one task that uses a non-emission criterion (land use, transport) so the exercises cover the slot's täsmennys.
- L1-01, 02, 04, 05 are the same one-step task (energy in kWh, one coefficient); only the context changes. Replace one with a task that gives the emission and asks for E or the comparison (L2-03 already does the former), or make L1-03 the model for others (a quantity per 100 km).
- exercises.json carries no common-mistake feedback, unlike the inquiry's numeric items. The expected slips (GWh not converted, answer in g instead of kg or t, L2-04 dividing by 3,6) could be given `mistakes` with a repairing message, if the schema allows.
- L2-04 and L3-01 use combustion-only coefficients (g/MJ) beside the lifecycle coefficients of the table. The tasks say so, which is good; add one line to L2-04's solution saying why a g/kWh value of a fuel and of electricity are not the same thing (the solution's "Järkevyys" already hints at it).

## Checked
- Levels 5 / 4 / 3 per the rubric; level 2 has a unit conversion (L2-01, L2-04), a rearrangement (L2-03) and a difference of two cases (L2-02); no task repeats the worked example (4800 kWh, gas, tonnes) as it stands.
- Answers recomputed: 72, 2,46, 216, 172,2, 1,176, 460, 2,9088, 24 490, 248,4, 736, 20 320, 4,14; the rounded values stay inside every tolerance, so a student rounding to the data's figures is accepted.
- Every solution has the seven parts: given, asked, principle explained in words, symbolic formula, conversions (or "ei tarvita" with a reason), substitution with units, answer with significant figures, check with a rounded estimate.
- Conversions are by substitution (1 g = 0,001 kg, 1 GWh = 10^6 kWh, g/MJ · MJ/kWh), no helper quantity beyond what is needed.
- Finnish: no errors found; context labels ("Esimerkkitalous", "Esimerkkitilanne") mark invented situations; real data (bensiini 32 MJ/l, 69 g/MJ, diesel 36 MJ/l, 74 g/MJ) are plausible and match the lesson's tarkistus-2.
- 1280 px capture: the answer and solution open in one column, with no empty area.
- Hash at the end: e6d7ee0e2e1ea72d (unchanged).
