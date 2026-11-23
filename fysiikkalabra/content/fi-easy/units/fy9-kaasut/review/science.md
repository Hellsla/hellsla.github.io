VERDICT: PASS
CONTENT-HASH: ab91813f8780e526
SCOPE: full review (fi-easy). The diff since fd4f0479d36b9c00 is in unit.md only: three new pysahdy boxes, and the hero and kone figures redrawn as WebP images with the same LaTeX labels. I also re-judged unit.md, unit.json, inquiry.json, exit-ticket.json, teacher.md, tasks.json, solutions.md and answers.py.

## Blocking
(none)

## Polish
- teacher.md (Arviointi) says "Kaikki aineistot ovat keksittyjä esimerkkejä". This does not hold for s7, which uses real TVO OL3 figures (`source: statistics`). Under Tehtävät it says "muut viisi tehtävää", but the set has nine tasks. Both lines are the same in fi, so fix them in both languages.
- inquiry `pumppu`, mistake value 100.0: putting the gauge reading (0 kPa) into Boyle's law gives 0 kPa, not 100 kPa, so the feedback does not explain this number. fi has the same value.

## Checked
- **Pysahdy boxes (judged first):** I compared each box with fi `unit.md` lines 121, 163 and 191. The physics is the same in each.
  - Box 1: the gauge shows overpressure, and the gas law needs the total pressure, 101 + 230 = 331 kPa.
  - Box 2: a real gas condenses before 0 K, so the extrapolated zero is a prediction of the model.
  - Box 3: Q2 to the colder surroundings is required, so W < Q1.
  - All three agree with Ydinajatus, Kaava, Virheet, lt-6, tarkistus-1 and the exit ticket.
- **Figures:**
  - kone.webp: I measured the arrow widths in pixels at 272 : 178 : 91, which is 1000 : 654 : 335 against Q1 = 1000 J, Q2 = 650 J and W = 350 J. That is to scale within 4 %, and the two outgoing arrows together are as wide as Q1, as the aria-label says.
  - Hero: frost, a cold thermometer and a warm garage, which fits the Miksi question.
- **Recomputed in one independent script:**
  - Hook: 286 / 185 kPa.
  - lt-4: 1,068.
  - aineisto: nA = 0,0602 mol. Its mistakes match: 6,02·10⁻⁵, 60,2 and 0,0361, and 0,0301 for the mixed point.
  - celsius: 113,6 kPa. tyo: 750 J.
  - luukku: 17,66 kN, with mistakes 54,02, 29,43 and 1,8.
  - pumppu: 151,5 kPa, with mistakes 252,5 and 40,4.
  - pallo: 832,3 kg, with mistakes 3451, 2619, 28 701 mol and 87 942.
  - manta: 750 J.
  - tarkistus-2: 58,3 kW, with mistakes 83,3, 17,5 and 7,5.
  - Suction-pump limit: 10,3 m.
  - tarkistus-1 interval: −277…−247 °C, which contains −273,15 °C.
- **Fidelity to fi (checked by script):** inquiry.json, tasks.json and exit-ticket.json have identical numeric fields (34, 180 and 0, no differences). solutions.md, unit.md and teacher.md contain the same numbers. `practice.py check` passes: 9 tasks, 135 points. answers.py is shared with fi; for its s7–s9 recomputation see the previous report.
- **Assessment:** every choice item has exactly one correct option. The distractor feedback is physically right: equal support force, the hydrostatic paradox, Boyle's law, kelvin ratios, n independent of gas type, Q2 unavoidable, the 1/V linearisation, gauge 0 meaning atmospheric pressure, and kPa·l = J.
- **Guardrails:** "lämmöksi" appears only as heat Q2 in the derivation and in a quoted misconception in s7. The first law's sign convention is consistent. The heat-pump COP answer conserves energy. The content stays within FY3.
- **Hash:** ab91813f8780e526 at the start and at the end.
