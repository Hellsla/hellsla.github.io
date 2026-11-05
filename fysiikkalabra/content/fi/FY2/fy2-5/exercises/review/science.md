VERDICT: PASS
CONTENT-HASH: 112961aec0c7f838
Round: 2

Since round 1 (18b454cd1 → HEAD) the only change to fy2-5's exercise set is one solutions.md line, from commit 442c889ba. In the L3-04 Sijoitus, the twelve-month sum is now split into groups of four months. exercises.json and answers.py are unchanged. The packet was regenerated, mode full.

## Blocking

## Polish
- content/fi/FY2/fy2-5/exercises/solutions.md:205 (L2-08 Arvio) — "bensiini on lähes $40\,\text{MJ}$ kilogrammaa kohti" is wrong, because 43 is more than 40. Write "yli $40\,\text{MJ}$" or "noin $43\,\text{MJ}$".
- solutions.md:203 and exercises.json:275 (L2-08) — "$104\,\text{MJ}$" has three significant figures, but the data (26 MJ/kg and 4,0 kg) have two. Write "noin $100\,\text{MJ}$", or note that unrounded values are kept for the ranking.
- exercises.json:60 (L1-06, second distractor) — "riippumatta määrästä" makes no sense in the sentence (carried over).
- L3-04 and L3-05 — both still follow the same chain m = E/(ηH). Level 3 in the plan asks for emissions too (carried over).

## Checked
- Round-2 line: 6700 + 1300 + 5300 = 13 300 kWh, the same total as before, and each group's sum is right. The rest of the line (47 880 MJ, 3313 kg, 1237 kg, 4024 kg, +710 kg) is unchanged. L3-04 gives 3313,5 kg against the answer 3300 (+0,41 %, tolerance 0,02). Language only: "joten … joten" is repeated.
- L2-08 (unchanged since round 1): the energies 64,5 / 75 / 104 / 120 MJ match the `order` list, the gaps are at least 10 MJ and the conversions are right. The mass-order and H-order claims are true, and the `prompt` names the quantity and the direction.
- All 18 numeric answers were recomputed in one python run, all within tolerance; the largest deviation is L2-07 (+2,3 %, tolerance 0,03). L1-06 and L2-06 each have exactly one correct option.
- Hash 112961aec0c7f838 at start and end. FY2 scope: no c·m·ΔT, one efficiency per chain, and energiasisältö e is kept apart from lämpöarvo H.
