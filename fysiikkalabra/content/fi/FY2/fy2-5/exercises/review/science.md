VERDICT: PASS
CONTENT-HASH: 554062ddfd509c38
Round: 3

Since round 2 the only change is uncommitted, one line of solutions.md in the working tree. In L3-04, the three month groups now read "… eli 6700", "… eli 1300" and "… eli 5300" in place of "= …". exercises.json and answers.py are unchanged. The packet was regenerated, mode full.

## Blocking

## Polish
- content/fi/FY2/fy2-5/exercises/solutions.md:205 (L2-08 Arvio) — "bensiini on lähes $40\,\text{MJ}$ kilogrammaa kohti" is wrong, because 43 is more than 40. Write "yli $40\,\text{MJ}$" or "noin $43\,\text{MJ}$".
- solutions.md:203 and exercises.json:275 (L2-08) — "$104\,\text{MJ}$" has three significant figures, but the data (26 MJ/kg and 4,0 kg) have two. Write "noin $100\,\text{MJ}$", or note that unrounded values are kept for the ranking.
- exercises.json:60 (L1-06, second distractor) — "riippumatta määrästä" makes no sense in the sentence (carried over).
- L3-04 and L3-05 — both still follow the same chain m = E/(ηH). Level 3 in the plan asks for emissions too (carried over).

## Checked
- Round-3 line: the group sums are unchanged and right (2100 + 1900 + 1600 + 1100 = 6700; 600 + 250 + 200 + 250 = 1300; 600 + 1100 + 1600 + 2000 = 5300). "eli" is read here as "which is", and it does not change the meaning. 6700 + 1300 + 5300 = 13 300 kWh, the same total as before, and each group's sum is right. The rest of the line (47 880 MJ, 3313 kg, 1237 kg, 4024 kg, +710 kg) is unchanged. L3-04 gives 3313,5 kg against the answer 3300 (+0,41 %, tolerance 0,02). Language only: "joten … joten" is repeated.
- L2-08 (unchanged since round 1): the energies 64,5 / 75 / 104 / 120 MJ match the `order` list, the gaps are at least 10 MJ and the conversions are right. The mass-order and H-order claims are true, and the `prompt` names the quantity and the direction.
- All 18 numeric answers were recomputed in one python run, all within tolerance; the largest deviation is L2-07 (+2,3 %, tolerance 0,03). L1-06 and L2-06 each have exactly one correct option.
- Hash 554062ddfd509c38 at start and end. FY2 scope: no c·m·ΔT, one efficiency per chain, and energiasisältö e is kept apart from lämpöarvo H.
