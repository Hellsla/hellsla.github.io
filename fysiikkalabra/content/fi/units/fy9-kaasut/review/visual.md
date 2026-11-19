VERDICT: PASS
CONTENT-HASH: 7f3ceb36bf9a1f73

## Blocking
(none)

## Polish
- [Minor] capture gap: the shots have no capture of the Sovella solutions that the diff touches, so the paragraph breaks were judged from the diff plus the rendering of the same solution component in the Tehtävät stage.

## Checked
- git diff origin/main...HEAD (excluding review/): only solutions.md changed; blank lines inserted between paragraphs (Periaate, Mallivastaus, a sentence after a display formula); words, maths and figures unchanged; no break lands inside a formula.
- Read sovella/review/visual.md (earlier PASS, same conclusion).
- Opened stage-sovella-390-4 (fi): KaTeX rows, answer box, reasonableness block and hints render cleanly at 390 px.
