VERDICT: PASS
CONTENT-HASH: f28649f7c45795b2
Round: 1

New since the last PASS (commit 18b454cd1): the ordering task fy2-5-L2-08 in exercises.json and solutions.md. Mode: full. Every numeric answer was recomputed again.

## Blocking

## Polish
- content/fi/FY2/fy2-5/exercises/solutions.md:205 (L2-08 Arvio) — "bensiini on lähes $40\,\text{MJ}$ kilogrammaa kohti" is wrong, because 43 is more than 40. Write "yli $40\,\text{MJ}$" or "noin $43\,\text{MJ}$".
- solutions.md:203 and exercises.json:275 (L2-08) — "$104\,\text{MJ}$" has three significant figures, but the data (26 MJ/kg and 4,0 kg) have two. Ranking alone does not need rounding. Still, "noin $100\,\text{MJ}$", or a note that unrounded values are kept for the ranking, would match the other solutions.
- exercises.json:60 (L1-06, second distractor) — "riippumatta määrästä" makes no sense in the sentence (carried over).
- L3-04 and L3-05 — both still follow the same chain m = E/(ηH). Level 3 in the plan asks for emissions too (carried over).

## Checked
- L2-08 recomputed. The energies are 64,5, 75, 104 and 120 MJ, so the `order` list (bensiini, polttopuu, kivihiili, jyrsinturve) is correctly smallest to largest. The gaps between neighbours are at least 10 MJ, so no tie depends on rounding.
- L2-08 conversions are right (1500 g = 1,5 kg; 0,0040 t = 4,0 kg). The claim that ranking by mass swaps wood and coal is true (by mass the order is 1,5 < 4,0 < 5,0 < 12). The claim that ranking by H gives a different order is also true (by H it is the full reverse).
- L2-08 `prompt` names the quantity (E) and the direction (pienimmästä suurimpaan), as docs/exercise-types.md type 9 requires. The solution explains the order with E = Hm, the lesson's notation.
- The heating values in L2-08 are the lesson table's values (43, 15, 26, 10 MJ/kg).
- answers.py vs exercises.json: one python run over all 18 numeric answers. Every one is within its tolerance, and the largest deviation is L2-07, 18,42 vs 18 (+2,3 %, tolerance 0,03). L1-06 and L2-06 each have exactly one correct option.
- answers.py has no line for L2-08. That is correct, because the task is non-numeric.
- FY2 scope: there is no c·m·ΔT, and each chain has only one efficiency. The food tasks keep energiasisältö e apart from lämpöarvo H, as the guardrail requires.
