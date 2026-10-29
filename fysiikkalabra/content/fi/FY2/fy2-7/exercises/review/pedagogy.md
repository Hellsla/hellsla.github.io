VERDICT: PASS
CONTENT-HASH: 4c9468244fe46189

## Blocking

## Polish
- exercises.json:14 — the task asks two questions ("Lue kuvasta, kuinka suuri osa ... häviää. Kuinka paljon ...") and the question is not the only last sentence-level ask; keep the reading as a hint-like step — "Kuinka paljon energiaa kaukolämpöverkossa häviää viikon aikana? Lue häviön osuus kuvasta. Anna vastaus megawattitunteina." (situation, then question last).
- solutions.md fy2-7-L1-02 — "Kuvaajan lukeminen" names a diagram a graph — "Kuvan lukeminen".

## Checked
- Delta: L1-02 now needs the Sankey figure; the 9 % share is only in the figure (no 9 % in the text), so the figure is needed and the answer is not given away.
- Figure description gives a reader who cannot see it the same shares (96/4 and 91/9 %) without the answer; figure is legible at 390 px (labels 100 %, 9 %, 91 %).
- Answer 0,09 · 360 MWh = 32,4 MWh is right; tolerance 0,03 accepts 31,4 to 33,4 (also the earlier 33 from 9,2 %) and rejects the 10 % guess (36).
- Solution step by step: picks the lower stream, reads 9 %, converts to 0,09, multiplies; stresses share of lähtevä; Järkevyys cross-checks 91 %.
- answers.py matches the answer; level 1 still one formula with a value read off a figure; not a repeat of the 245 MWh example.
- Earlier PASS conclusions for the untouched exercises hold.
