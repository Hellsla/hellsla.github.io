VERDICT: PASS
CONTENT-HASH: 72a265bfa9067748
SCOPE: delta added-exercise from c109fb6875e61c4c base 9df3f06ae3cc

## Blocking
- none

## Polish
- [Minor] fy1-4-L2-09 task (4-18), data table — the table caption "Ilman lämpötila vuorokauden aikana (keksitty esimerkkiaineisto)" wraps to five lines in a narrow table that fills under half the card, leaving an empty right side; and the table comes after the sentence "Vastauskenttään tulee …", so the answer instruction is not the last thing before the field. Let the caption use the card width, or move the table before that sentence.
- [Minor] fy1-4-L2-09 solution — "Kaava" shows the first formula as a two-row block and the model $T(t)=\ldots$ as plain text after it ("ja lineaarinen malli …"); reads fine, only slightly uneven.

## Checked
- fy1-4-open-exercises-L2-1280-12 (task 4-18 with its data table, answer field, opened Annettu) and -13, -14 (the whole solution: Kysytty, Periaate, Kaava, Muunnokset, Sijoitus, Vastaus, Järkevyys) at readable resolution.
- check_layout.py fy1-4 --width 360: OK in fi, en and fi-easy.
- Maths: KaTeX renders, units upright with thin space, decimal comma in the table and prose, ${}^\circ\text{C/h}$ correct, chain aligned at `=` in rows, answer set apart, order principle → formula → substitution → result → interpretation kept. No plain-text quantities. No figure in the exercise (data table only; the graph is the student's task).
- Finnish: instructions say what to do (a to d), the situation comes first and the question last; terms match the glossary (kuvaaja, lineaarinen malli, kulmakerroin as muutosnopeus). The set still reads as one with its neighbours.
- The other 22 exercises were not re-reviewed (unchanged).

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 4
