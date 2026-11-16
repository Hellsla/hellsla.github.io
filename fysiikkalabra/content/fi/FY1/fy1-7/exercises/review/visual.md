VERDICT: PASS
CONTENT-HASH: 6a0a33a715c949de
SCOPE: delta added-exercise from c913477ce1626a3e base 9df3f06ae3cc

## Blocking
- none

## Polish
- [Minor] fy1-7-L2-09 solution, Muunnokset — one sentence is broken by two display blocks ("Maalle [block] m = 5,97·10^24 kg, Saturnukselle [block]"), and Maa's m stands outside the block while Saturnus's m is inside it. Readable, but a row per planet, each with d and m in one block, would be calmer.
- [Minor] fy1-7-L2-10 solution table — the header $\tfrac{m}{V}\,(\tfrac{\text{kg}}{\textsf{l}})$ has a very small nested fraction; a single $\rho\,(\text{kg/l})$ column header would read better on a phone. The litre $\textsf{l}$ ("9 l") looks like a capital I next to the digit, the project convention but worth a thin space check.
- [Minor] fy1-7-L2-09 solution b) — the range "690–1640" breaks at the dash at a line end; a non-breaking form avoids it.
- for science: fy1-7-L2-09 d) says Saturnus has "vain noin puolet" of Neptunus's density; 687 : 1638 is about 0,42, so "alle puolet" might be more accurate.

## Checked
- fy1-7-open-exercises-L2-1280-12 (L2-09's Annettu with the 8-planet table, Kysytty to Mallivastaus b), -13 (Kaava, Muunnokset, Sijoitus, Mallivastaus c), -14 (d, Vastaus, Järkevyys, task 7-19 with its Annettu), -15 (table, Kysytty to Muunnokset) and -16 (Sijoitus to Järkevyys) at readable resolution.
- check_layout.py fy1-7 --width 360: OK in fi, en and fi-easy.
- Maths: units upright with thin spaces, decimal comma, powers of ten with \cdot, ρ_Maa subscripts as text, aligned rows with `=` in one column, answers set apart, order principle → formula → substitution → result → interpretation kept. The tables fit the column without sideways scroll.
- Finnish: natural and clear, glossary terms consistent, situation then questions, source links given. Both tasks use the lesson's own wording (tiheys, keskitiheys). No figure in the exercises (the graph is the student's task); the task link cards need no alt text.
- The other 22 exercises were not re-reviewed (unchanged).

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 5
