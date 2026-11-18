VERDICT: PASS
CONTENT-HASH: 9b44845a75fe196a
SCOPE: delta: the new Sovella itsenäisesti tasks s7 (Kärry radalla, figure fy4-1/ex-kolme-osaa) and s8 (Kaksi kulkijaa samalla tiellä, figure fy4-1/ex-kaksi-kappaletta) with their solutions, and the unit intro; s1–s6 untouched. 

## Blocking
- (none)

## Polish
- [Minor] sovella/solutions.md s7 Yleisiä virheitä, last item: "tai kuljetusta matkasta" is ungrammatical; write "tai kuljetun matkan perusteella".
- [Minor] fy4-1/ex-kaksi-kappaletta alt text says "Kappale A/B" while task s8 says "kulkija"; the figure is shared, so only note it, or name both ("kulkija") in the task text.
- [Minor] s7 and s8 graphs are small at 390 px (tick labels about 9 px); legible, but a larger render would help.

## Checked
- Captures opened (fi, 390 px, stage-exercises parts 50, 51, 53, 54, 55, 59, 60, 62, 64, 69): the s7 and s8 task cards with their (t,x) graphs, the opened solutions, the aligned calculation rows (a–d), the fractions and the answer boxes, and the self-assessment rows. Nothing is clipped or overflowing; the graphs are legible with units on both axes and the points marked; the axes of s7 and s8 use the figure palette (A blue, B orange, no force/velocity colour clash).
- check_layout.py at 360 px for all three language pages: OK, with one known clipped formula from docs/clipped-formulas/FY9.tsv; it is in the older text (fy9-liike: `(20 km/h + 60 km/h) : 2 = 40 km/h`), not in s7 or s8.
- Finnish and translations are cut identically (671 lines and 71 display blocks per solutions.md), so the layout carries over.
