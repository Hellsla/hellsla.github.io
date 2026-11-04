VERDICT: PASS
CONTENT-HASH: d31dfe55c8d54663

## Blocking
none

## Polish
- solutions.md fy1-2-L3-05 — "Vastaus" says "noin 1,5 h" while the stored answer is 1,54 (tolerance 0,03); write "noin 1,5 h (kenttään sopii 1,54)" so a student typing 1,5 sees why it is near.
- exercises.json fy1-2-L3-05 — kWh = 3,6 MJ is now given, good; the question order (Kuinka monta tuntia, Perustele, Onko väite oikein?) ends on a yes/no after "Perustele": put "Onko väite oikein? Perustele." last.
- exercises.json fy1-2-L2-05 — table header "$\text{Yksikkö}$" is a word in math mode; harmless, but plain text would be simpler if the table renderer allows it.

## Checked
- L2-05: cyclist 9,0 m/s (32 km/h) and boat 12,0 knots (6,17 m/s) keep the ranking pikalaiva, juna, pyöräilijä, vene; answers.py and the solution agree (19,5 m/s); the reasonableness line is updated.
- L2-07 rewritten: the student's wrong result is quoted, the unit check is asked before the correct time; solution $1{,}0\,\text{min}$ matches.
- L1-06 feedback and solution now say N and g are derived without implying the prefix makes a new unit; L3-04 solution explains why k stays the same and that units cannot give k.
- L3-05 answer 1,54 h recomputed from 85,0 W and 100 W; consistent with the solution.
- Counts 8/7/5 = 20; data and error tasks unchanged; none repeats the worked example.
- Unit text in LaTeX (m/s, l/s) consistent; no case errors.
