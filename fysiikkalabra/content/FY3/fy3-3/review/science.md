VERDICT: FAIL
CONTENT-HASH: 6167b77d298d349a

## Blocking
- solutions.md:89 (L2-04) — The answer "4,0, two significant figures because the temperatures are given in whole degrees" does not follow. Whole degrees give T_yö = 100 K and T_päivä = 400 K to the kelvin, which is three figures each, so the quotient has three figures (4,00), as the house rule also says for 3-figure data. The stated reason is false. — Fix: give 4,00 and justify it ("kelvinlämpötilat 100 K ja 400 K tunnetaan kelvinin tarkkuudella, kolme numeroa"), or give a correct reason for 4,0.
- solutions.md:79 (L2-03) — "Two significant figures because an extrapolated value is only an estimate" is not a precision argument. It also differs from the worked example, which uses the rule correctly. The 2 figures really come from the difference of readings: Δp = 137 − 110 = 27 kPa has two figures, so k = 0,39 kPa/°C and kΔθ ≈ 23 kPa, and 110 − 23 = 87 kPa to the whole kPa. — Fix: state that reason (NOTES §2: a difference of readings has the figures of the difference).

## Polish
- solutions.md:28, 48 (L1-03, L1-05) — Adding the exact 273,15 keeps the reading's decimals (L1-01, L1-02 and L2-01 argue it that way), but these two argue from "significant figures like 77,4 K / 2,7 K". By the decimal rule the results would be −195,8 °C and −270,5 °C. The values given are allowed under the house 3-sf rule, but the reasoning contradicts L1-01/02. Use the house rule as the stated reason, or the decimal rule throughout.
- solutions.md:68 (L2-02) — The number is right, but the reason "three figures like the given pressures" is not: Δp = 33 kPa has two figures, so k = 0,33 and k·35 ≈ 12 kPa, and 90,0 + 12 = 102 kPa to the kPa. Say this, as the worked example does.
- solutions.md:115 (L3-03) — "absoluuttinen nollapiste, jossa liike-energia on nolla" contradicts the lesson's careful "pienimmillään" (lesson.md, glossary, check-3). Use "pienimmillään", or say "in the model".
- inquiry.json:368 (check-2 solution) — "Kuvaajan lukeminen: Kuvaajasta luetaan…", but the task gives a table, not a graph. Say "taulukosta".
- exit-ticket.json:12 — "−273 °C": write −273,15 °C (≈ −273 °C), consistent with the lesson.

## Checked
- All 12 exercise answers recomputed independently: they match answers.py and exercises.json and sit inside their tolerances. The data are consistent with p ∝ T (L2-02 122,9; L2-03 137,2 kPa).
- Worked example: the endpoint slope 0,37 gives −270 °C (least squares −271 °C). The 2-figure justification follows the difference rule. The check 136,6 vs 137 kPa is right.
- siirto 121,7 → 122 kPa; mistakes 404 and 83,8 are correct; virhe 128 kPa, ≈7 %; check-2 −273 °C; pred-1 ratio 1,9995; the misconception's 1,035.
- Each stated principle (constant V and n ⇒ p ∝ T; equal degree size ⇒ ΔT = Δθ) applies to its task, and the conversions are right.
- sim.js: the pressure from wall impulse per length, averaged over both axes, is exactly N v²/(2·Wc·Hc), with no direction bias. pRef is consistent, p ∝ T/V, vRel = √(T/300), and the simulated-time window is independent of the speed setting.
- exp-1 and exp-2 lock V or T respectively; the slider ranges and steps reach the suggested values; simState gives theta, vRel, pRel and pTheory.
- All prediction keys and feedback numbers (100→200, 50→100, 1,41² ≈ 2) agree with the model.
- The extrapolation figure is to scale (0,945 px/°C, 1,375 px/kPa, the axis at −300 °C), and so is the kelvin-scale figure (1,2008 px/K).
- Model limits (2D, no collisions, equal speeds) are stated in `model`.
- Scope is within FY3's central contents.
