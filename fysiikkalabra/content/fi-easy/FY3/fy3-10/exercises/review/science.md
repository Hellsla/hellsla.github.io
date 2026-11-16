VERDICT: PASS
CONTENT-HASH: 26091b98ad3a677f

## Blocking

## Polish
- content/fi-easy/FY3/fy3-10/exercises/exercises.json:120 — "Moolimassa kertoo, kuinka monta grammaa yksi mooli ainetta painaa" uses *painaa* for a mass. Better: "…mikä on yhden moolin massa grammoina". The meaning is clear (C), but for S2 readers who are learning to tell mass from weight, the exact word helps.
- content/fi-easy/FY3/fy3-10/exercises/solutions.md:209 — "yksi mooli argonia painaa $M$" has the same issue. Better: "yhden moolin massa on $M$".
- lessons/FY3/fy3-10/answers.py:45 — the L1-07 comment says "-> 2,31 l", but the answer and the solution give 2,3 l. Cosmetic.

## Checked
- I recomputed all 22 numeric answers in one script with my own formulas: pV = nRT, the combined gas law, n = m/M, N = nN_A, and my own least-squares fit for L2-06. All are inside tolerance and match answers.py, which is shared with en.
- Every number in the task texts, data tables, answers, units and tolerances is identical to the en version. The correct option is the same in all five choice tasks. The solutions carry the same numbers and steps; no step or justification is dropped in the S2 version.
- The notation follows the brief's fi-easy lesson: T = θ + 273,15 K, R = 8,31 J/(mol·K), absolute pressure, and the kPa·l = J pairing.
- L2-05: the added sentence on total pressure ("myös ilmanpaine mukaan lukien") is correct. The leaked share is 5,5 %, and the reason why pressure alone does not prove a leak is right.
- L2-07: the S2 definition of an isotherm ("käyrä, jossa lämpötila on vakio") is correct. pV is 244 against 305 kPa·l, so B is correct.
- L3-03: the gauge-pressure definition and the reason it cancels are right. Δm = 0,72 kg.
- L3-04: 27,9 g, then 33,7 balloons used and 21,7 left. The cold-gas reasoning is correct.
- L3-05: V₁₀ = 7,38 m³, V₁₅ = 15,7 m³, h ≈ 12,8 km. The "kasvaa kiihtyvästi" justification is correct.
- L1-06, L1-08 and L2-08: the feedback is physically right in Finnish ("tulos olisi päinvastoin liian suuri" for the Celsius distractor).
- `fy3-10/pt-suorat`: the read points give 0,024 mol and 1,67. The ideal-gas assumptions are stated where the pressure is high.
