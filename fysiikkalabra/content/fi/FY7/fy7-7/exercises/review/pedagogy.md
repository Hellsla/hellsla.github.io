VERDICT: PASS
CONTENT-HASH: c2299a6720da2db8

Round 1 (new task fy7-7-L1-09, graph choice; rest of set PASS before)

## Blocking
(none)

## Polish
- exercises.json:106, :122 — "jaksonajaksi on luettu taajuuden lukuarvo millisekunteina" (40 Hz becomes 40 ms) is a contrived slip; a natural one is mixing T and f or using 1 : 40 = 0,25 s. Keep the 2x2 design but name the slip plainly: "taajuuden lukuarvo $40$ on merkitty jaksonajaksi ms:ssa".
- The chapter's warned phase mistake (voltage maximum when the flux is maximum) has no distractor; the stem's "nolla ja kasvamassa hetkellä t = 0" removes it. Acceptable; if a fifth option is possible, a cosine curve would use it.
- solutions.md:198 — "neljä täyttä jaksoa" and the reading rule are good; add that the grid values (volts on the y axis, ms on the x axis) are what to read.

## Checked
- 5,0 V times root 2 = 7,07 V, T = 25 ms: option B correct; the 2x2 design (each option shares one feature with two others) means the correct one cannot be found by form.
- Distractors catch the chapter's warned mistake (effective value read as peak: A and C).
- Figure alt texts (figures.py PICK_DESC plus per option) fully describe axes, peak, zeros and number of periods.
- Within chapter: U = U0 : root 2 and T = 1 : f only; level 1 is fair (two values read off, no calculation chain).
- Feedback of the correct option states the two numbers but no extra reason stage (single-stage).
- Checked from text and the figure source only (no renders; pedagogy role); inline formulas measured as KaTeX renders at 390 px: T 106 px, e0 120 px, fit.
