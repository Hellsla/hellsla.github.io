VERDICT: PASS
CONTENT-HASH: c05a8657af84848d

## Blocking
(none)

## Polish
- [Minor] solutions.md a-, b-, c-, s2-a-, s3-kohdat — `$$\begin{aligned}…$$` display maths sits inside a running sentence and is followed by ", joten …" or "." on its own line. This is unchanged from the baseline; at 390 px the stray punctuation line reads slightly oddly. Optional: end the sentence before the display, or put the continuation in the next sentence.
- [Minor] solutions.md fy5-s1 d) — the sentence "Kuorma ei siis heitty ulospäin…" is now its own paragraph right after the "Kuljettajan selitys" paragraph. It reads as a conclusion, so the split is fine; only a thought: "siis" is slightly redundant after the split.

## Checked
- Source-only review (the screenshot inventory is empty, so there are no captures; the packet permits judging from source for this paragraph-split change). No figure was opened and no figure claim is made. The figures were not touched by the diff.
- Hash run at start and end: c05a8657af84848d.
- Read the full solutions.md diff (word-diff against origin/main): every split lands at a thought boundary (Periaate → method, Mallivastaus → Johtopäätös → real-crane remark, Kuljettajan selitys → conclusion, Mallivastaus → Epävarmuus → Poikkeaman syy). No `$…$` or `$$…$$` is broken across a paragraph, no bold label is orphaned from its text, and the label-per-line structure (Annettu, Kysytty, Periaate, …) is intact.
- tasks.json: the three edited task texts (s1 d, s3 Jupiter, s4 urut) were split at the premise, assumption and question boundaries. The `$…$` units with `\\,\\text` are unchanged, with correct case endings (`$15\,\text{m}$:n`, `$9{,}93\,\text{h}$:n`). The instruction sentence now stands alone as the last paragraph, which improves task clarity.
- Display aligned blocks are short, broken at `=`/`\\`, and break nothing at phone width by structure.

## Scores
illustrations 4 (not re-inspected) · typography 4 · Finnish 4 · accessibility 4
