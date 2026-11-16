VERDICT: PASS
CONTENT-HASH: e0441f2e5cde3648
Mode: full

## Blocking

## Polish
- content/fi-easy/FY4/fy4-8/exercises/solutions.md:150 (L2-05 Vastaus) — "korkeudet $h$ on annettu kahdella" holds for 0,10–0,30 m but not for 0,05 m (one figure); say "useimmat korkeudet" or leave.
- solutions.md:276 (L2-10 a) — $1500\,\text{kg}$ has four significant figures and the speeds are exact; "kolme numeroa ei lupaa liikaa" is true but not the usual rule; give four or say three suffice for the comparison.

## Checked
- Hash the same at the start and the end (e0441f2e5cde3648).
- git diff since the version passed: solutions.md L2-10 Vastaus only; the d) paragraph moved first, a) now begins "Lisäksi:"; no number, formula or other word changed. exercises.json and answers.py unchanged.
- First line of the answer step, $s \approx 0{,}26\,\text{m}$ with its reason (80 kg, two figures), matches `answer` 0.26 (tolerance 0.05); parts a, b, c, e follow with every result present.
- All 21 numeric answers recomputed in one script with my own formulas: equal to answers.py and inside every tolerance (L2-05 9,766; L2-06 −19,93 kJ, forces 94/107/157 N; L2-07 1,144 N; L3-04 54,89 N, v = 6,87 m/s; L3-05 63,9 %).
- L2-10 a: 52 083 J, 144 676 J, 468 750 J → 52,1; 145; 469 kJ; b: 4-fold for any mass, 9-fold, 9,00.
- L2-10 d: F = 29 430 N; E_k0 = 7716 J; work principle solved in symbols first, s = 0,2622 m → 0,26 m; checks a = 37,5 g, v²/(2a) = 0,262 m, 12 000 kg at 100 km/h for the same distance.
- L2-10 e: 7,7 kN over 1,0 m, 154 kN ≈ 150 kN over 0,05 m; constant force named as a model limit.
- Source values and quotation agree with the coordinator's verified record (read 16.11.2026); kg-as-force interpretation given in the task.
- L2-10 c: deformation → internal energy → transfer to the surroundings as heat; never "muuttuu lämmöksi".
- Figure tasks L2-08 (m = 0,50 kg, h = 1,02 m) and L2-09 (2,5 N) agree with the figure code.
