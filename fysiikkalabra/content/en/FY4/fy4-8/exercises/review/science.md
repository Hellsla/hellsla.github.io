VERDICT: PASS
CONTENT-HASH: 98be4db96580125c

## Blocking

## Polish
- content/en/FY4/fy4-8/exercises/solutions.md:149 (L2-05) — the substitution shows $19.5 : 2 = 9.77$, but $19.5 : 2 = 9.75$; the unrounded slope $5.86 : 0.30 = 19.53$ gives $9.77$ — write $19.53\,\text{m/s}^2$ in the substitution.
- solutions.md:276 (L2-10 a) — $1500\,\text{kg}$ has four significant figures and the speeds are exact, so "three figures do not promise too much" is true but not the usual rule; either give four or say three suffice for the comparison.

## Checked
- Hash identical at start and end (98be4db96580125c).
- git diff since the version passed: solutions.md L2-10 Answer only; the d) paragraph moved first, a) now begins "In addition:"; no number, formula or other word changed. exercises.json and answers.py unchanged.
- First line of the answer step, $s \approx 0.26\,\text{m}$, matches `answer` 0.26 (tolerance 0.05); every other part's result still present in order a, b, c, e.
- All 20 numeric answers recomputed in one script with my own formulas (energy conservation, work–energy principle, least-squares lines through the origin for L2-05 and L2-07): equal to answers.py and inside every tolerance.
- L2-10 a: 52 083 J, 144 676 J, 468 750 J; b: ratio 9.00; d: $F = 29\,430\,\text{N}$, $E_{\text{k}0} = 7716\,\text{J}$, $s = 0.2622\,\text{m}$; e: 7.7 kN and 154 kN, twenty-fold; $a = 37.5\,g$; 12 000 kg at 100 km/h for the same distance.
- L2-10 source: quotation, 50 km/h / 80 kg / "3 000 kg", 12 000 kg, pedestrians above 60 km/h agree with the coordinator's verified record; link dated.
- L2-10 model: kg-as-force interpretation and constant force stated in the task; stopping force as net force justified; mean-force limit said.
- L2-10 c: deformation, internal energy, then transfer to the surroundings as heat; no "turns into heat".
- Significant figures: 80 kg two (trailing zero counts) → 0.26 m.
- Multiple choice L1-06, L1-08 and statements L1-09: one correct option each, distractors really wrong, feedback right.
