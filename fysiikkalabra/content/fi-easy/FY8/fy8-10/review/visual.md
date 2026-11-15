VERDICT: FAIL
CONTENT-HASH: 77b3d6fa4705a0b3

## Blocking
- [Major] lesson.md, inquiry.json, solutions.md (the lifted formulas) — the formula was set as `$$...$$` in the middle of a sentence, so the sentence's closing punctuation (". ", ", ") lands alone at the start of the line after the display block (seen in fy8-1 theory-1280-2 and -3: a lone "." line under the block; ". Tavallinen 365 nm:n UV-A-lamppu..." begins with a full stop). The sentence is broken, and a student reads a stray dot — Fix: close the lead-in sentence before the display (end it with a colon or let the formula stand as its own unit: "Siksi:" / block / next sentence starting with a capital), and put any trailing words after the block in a new sentence; no punctuation may start a line.

## Polish
- [Minor] The aligned blocks themselves (rows, = and ≈ in one column, units upright, thin spaces) read well at 1280 px; the 360 px check is for check_layout.

## Checked
- batch delta review: fy8-1 theory-1280-2, theory-1280-3 opened (the defect is seen there); the same `$$` + punctuation pattern found by grep in this lesson's changed lines (lesson.md, inquiry.json or solutions.md); other captures not individually opened.
