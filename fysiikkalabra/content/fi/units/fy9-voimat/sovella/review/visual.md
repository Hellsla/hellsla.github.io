VERDICT: PASS
CONTENT-HASH: 6ee6b7600ee64502

## Blocking
(none)

## Polish
- [Minor] sovella/solutions.md s5 a) — the paragraph break leaves the sentence on measurement 5 as a paragraph of its own between the Periaate and Kaava lines of the structured block — optionally keep it inside Periaate or lead it with a bold label; not needed for use.

## Checked
- Diff origin/main...HEAD for fi: only paragraph breaks (8 new blank lines in solutions.md, inquiry.json model field, tasks unchanged); words, maths, figures unchanged. Same cut as fi (language-neutral layout).
- Read the packet text of solutions.md: every new break falls at a sentence boundary outside inline/display maths (before a voimakuvio fence, after a closing $$, between the equilibrium and the changed-situation part); no paragraph over about 120 words; no split chain.
- Opened captures (fi unit page, same page structure for all languages): stage-sovella-390-3, stage-sovella-390-5 (tasks, hints, Vastaa/Tarkista, Näytä ratkaisu cards: text readable, nothing clipped, no horizontal overflow).
- Gap: the packet lists the Sovella screenshot inventory as stale/missing and screenshot.py has no Sovella page, so the opened model solutions themselves were not seen rendered; the figure s3-graph is unchanged and was not re-inspected. Not a ground for FAIL (unchanged).

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
