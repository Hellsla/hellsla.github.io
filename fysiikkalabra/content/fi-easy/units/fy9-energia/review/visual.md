VERDICT: FAIL
CONTENT-HASH: 3c8c8618ecbaa2da
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- [Major] sovella/solutions.md, fy9-energia-s7 c) and e), **Mallivastaus** (captures stage-exercises-390-56, -58, -59; 1280-40): the list is not rendered as a list. The page shows the raw markers ("- *Lämpöoppi.* …", "- *Sähköoppi.* …", "- *Mekaniikka.* …"; "- *Olosuhteet vaihtelevat.* …", "- *Hajontaa ei tunneta.* …", "- *Parempi testi.* …") inside one paragraph (`<p>… vastaan.<br />- <em>Lämpöoppi.</em> …`). In c) that is one block of about 330 words, over a phone screen, in a selkeä suomi text. Cause: the list starts on the line right after the lead sentence. Fix: an empty line between the lead sentence and the first `- ` row in both answers (as the closing paragraph "Kaikki tämä energia…" already has); rebuild and check that each answer shows a lead paragraph and a three-item bulleted list. s5-c in the same file (list directly after "**Mallivastaus:**") renders correctly.

## Polish
- B. sovella/solutions.md, s5-b **Mallivastaus** ("Ryhmän johtopäätös ei ole perusteltu. … - *Teho arvokilvestä.* …"): the same raw markers in untouched, earlier passed text; the same empty line fixes it.
- C. The s7 source line shows "Tarkistettu 16.11.2026" inside the link; the other units show only the source name. Harmless.

## Checked
- Hash at start and end: 3c8c8618ecbaa2da. Captures re-made (163).
- Opened at full size: stage-exercises-390-49 … -63 (the whole s7: card, source link, table, parts a–e, all solutions, common mistakes, rubric); stage-exercises-1280-36, -39, -40; stage-selita-390-3, -4.
- s7: source link visible and correct; table readable at 390 and 1280 px; `aligned` rows have `=` in one column; nothing clipped; numbers with units in LaTeX; case endings correct ($-32\,{}^\circ\text{C}$:seen, $30\,\%$:sta, $75\,\text{kWh}$:n).
- Johda itse: the three rows $P_1 = \eta_1 P_\text{o}$, $P_2 = \eta_2 P_1$, $P_3 = \eta_3 P_2$ are aligned and fit at 390 px.
- Item 18 sentences: read in the diff, grammar and terms correct; the inquiry feedback seen only on contact sheets 7 and 8.
