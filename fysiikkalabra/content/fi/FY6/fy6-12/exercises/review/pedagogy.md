VERDICT: PASS
CONTENT-HASH: 2e352fcfcb383439
Round: 1

## Blocking
(none)

## Polish
- solutions.md:192 — "kaksi merkitsevää numeroa kuten potentiaaleissa" is doubtful: 30 V and 120 V are not clearly two-figure values (the same slip was flagged in fy6-9 round 2); write "kaksi merkitsevää numeroa" or drop the clause.
- exercises.json:267 — rows 1 and 2 carry a reason ("koska ..."), rows 3 and 4 are bare calculations, so a test-wise student looks for the error in rows 3 or 4; give row 3 a short reason as well ("koska elektroni kulkee potentiaalieron läpi").
- exercises.json:267 — the correct option's feedback starts "Oikein, tämä rivi on väärin: ... Oikein U = ..."; drop the second "Oikein" ("Laskettaessa tulee U = 90 V").
- exercises.json:267 — first paragraph is 46 words; split the data and the constant into two paragraphs.
- solutions.md:180 — the line U = V_B - V_A = 120 V - 30 V = 90 V is 307 px at 16 px, just over 300 px; split it into two lines.

## Checked
- Text only (no render); widths measured by KaTeX at 16 px: row 4 chain 196 px, solution lines 197-307 px.
- Recomputed: U = 90 V, E_k = 90 eV = 1,442·10^-17 J; row 4 as written (120 eV to 1,9·10^-17 J) is arithmetically right for its input, so exactly one row is wrong.
- Rows 1 and 2 are physically correct (negative charge moves to higher potential; E_p = qV falls); neither is an accidental second error.
- Distractors catch the chapter's warned mistakes: row 1 (every charge goes to lower potential), row 2 (potential versus potential energy); the new error itself (potential instead of potential difference) is what the lesson means by "potentiaaliero, ei nollakohta".
- "Laskussa ei ole virhettä" is last and its feedback points to row 3 without naming the reason before the choice is made.
- Stays within the chapter (E_p = qV, W = qU, eV); no new quantity; question is the last sentence, rows are situation.
- Not a duplicate of L2-06 (a verbal claim) or L1-07 (zero point); level 2, kind error + reasoning.
- Finnish correct, case after number and unit fine; 21 tasks (8/8/5).
- Hash unchanged at the start and end.
