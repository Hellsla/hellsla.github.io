VERDICT: PASS
CONTENT-HASH: 005ee7bc5d2c433f
SCOPE: delta caption-label,md-paragraphs,reflow,typography,wording from af25454f80bec980 base 76ce6753c0f0
Delta from the version passed earlier (commit 76ce6753c0f0 holds af25454f80bec980): the marker taken out of captions, a heat-into rewording in L1-06, and solution paragraphs split with the words unchanged.

## Blocking
- none

## Polish
- solutions.md fy6-10-L2-09 Kuvaajan lukeminen: after the split, the new paragraph begins "Se on pienimmän neliösumman sovitus", and "Se" now refers back across a paragraph break. Fix: start it with "Kulmakerroin on pienimmän neliösumman sovitus".
- solutions.md fy6-10-L3 (zero point), Periaate: the paragraph that begins "Koevaraus on kuitenkin lähempänä…" belongs to the sentence about x < 0 that ends the paragraph before it. Fix: move "Alueella $x < 0$ voimat ovat vastakkaiset." to the start of that paragraph.

## Checked
- exercises.json L1-06 feedback: "Varaus ei muutu miksikään muuksi eikä katoa" is correct (charge is conserved) and follows the guardrail heat-into rule. The wrong option keeps its "lämmöksi" wording, as the guardrails allow for a distractor.
- solutions.md L1-06 Mallivastaus: removing "Varaus ei muutu lämmöksi" and adding "Varaus säilyy" keeps the reasoning complete and correct, and exactly one option is still correct.
- L2-09, the L3 zero point and the L3 hanging balls: the paragraph splits leave every word, number and formula unchanged, and the physics is the same as the version passed earlier (F = mg tan θ, r = 2L sin θ, q = 41 nC; zero point beyond q₂).
- No number, symbol, answers.py line or figure changed in the diff.
- Content hash checked at the start and the end.
