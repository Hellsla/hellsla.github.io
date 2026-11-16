VERDICT: FAIL
CONTENT-HASH: 38cc4c54b28cc1de

## Blocking
- [Major] inquiry.json 257 (Esimerkki 3: Etsi virhe, prompt; captures fy5-17-390-inq50km-0.png, fy5-17-1280-inq50km-0.png) — the student's quoted calculation was lifted to a display block, and the full stop and the closing quotation mark that followed it now open the next line: ".” Missä on virhe?" at 390 and 1280 px — a line beginning with a full stop and a closing quote is a visible punctuation error in the task's question, new with this change — close the quotation before the block and drop the stray mark, e.g. "Opiskelija päättelee, että S-aalto jää P-aallosta jälkeen $2{,}5\,\text{km}$ joka sekunti, ja laskee: $$…$$ Missä on virhe?", or keep the quote and put the full stop inside the formula with the closing ” on the sentence before.

## Polish
- [Minor] inquiry.json 63 (feedback "Oikein. …") — the lifted block keeps \tfrac, so the substitution "1540 m/s · 65 · 10^−6 s : 2" is set in script size inside a display block, small at 1280 px; a display formula takes \dfrac (NOTES §1).
- [Minor] inquiry.json 58 and 63 — these two blocks are centred, the solution boxes left-aligned (shared style).

## Checked
- Delta: inquiry.json 58, 63 (choice feedback) and 257 (Etsi virhe prompt).
- Own captures from preview/fy5-17.html?ratkaisut=1, details open, feedback un-hidden, 390 (dpr 2) and 1280 px, in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis2-fi-13/: fy5-17-{390,1280}-inq50km-0.png, fy5-17-{390,1280}-fb010-0.png, fy5-17-{390,1280}-d0050-0.png (sheets sheet-fy5-17-390-2.png, sheet-fy5-17-1280-2.png, sheet-fy5-17-feedback.png).
- The blocks themselves are sound: relations in one column, "65 µs" and "65 · 10^−6 s" whole, nothing clipped, no page overflow.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 5
