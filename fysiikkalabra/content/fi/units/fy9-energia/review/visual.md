VERDICT: PASS
CONTENT-HASH: 300bb0101bde0453
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- B `sovella/solutions.md` s7 c) and e): the list items of the model answer render as lines that begin with a literal hyphen ("- Lämpöoppi. …"), not as a bullet list, at 390 and 1280 px. Readable, and the same as the already passed s4 b) and s5 b), c), so it is the shared solution component's behaviour: fix it there (render a list inside Mallivastaus as a list), not per task.
- C s7 c), last paragraph: "Lämmitykseen ja akun sisäenergiaksi kulunut energia" joins two verbs' complements under one participle. Clearer: "Lämmitykseen kulunut ja akun sisäenergiaksi muuttunut energia sekä suurempi työ vastusvoimia vastaan otetaan kaikki samasta akusta."
- C s7 source line: the link text also holds "Tarkistettu 16.11.2026" (the other units' source lines link the source name only).

## Checked
- Captures re-made for this hash (stamp 300bb0101bde0453). Opened: stage-exercises-390-47…59 (s7 card, source link, bullet list, table, parts a–e, every solution, common mistakes, accepted answers, rubric a–d), stage-exercises-1280-34, -35, -38, contact-6, contact-13.
- Table (Auto / Ilmoitettu (WLTP) / Mitattu) fits at 390 px, units in LaTeX; aligned rows keep `=` in one column; nothing clipped; case endings ($-32\,{}^\circ\text{C}$:seen, $30\,\%$:sta, Model Y:llä) correct.
- "Johda itse": stage-selita-390-3 and stage-selita-1280-3: the three rows P1, P2, P3 are aligned at `=`, centred, unclipped; selita-390-4 for "Yleisiä virheitä" (sisäenergiaksi, kokonaishyötysuhdetta).
- Item 18 hunks read in the diff: inquiry.json feedback, s1 ("noin $70\,\%$"), s3 d), s6 c)–d), unit.md, ketju aria-label: each carries the decision out and reads naturally.
