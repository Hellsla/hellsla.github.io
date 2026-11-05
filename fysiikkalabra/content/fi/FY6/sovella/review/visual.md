VERDICT: PASS
CONTENT-HASH: a34f3aab0e6c03cc

Scope (teacher's ruling "katselmoi vain muuttuneet osat"): `git diff e7fb0232a -- content/*/FY6/sovella` plus what the changed sentence touches. The fi content change is one sentence, the fy6-s4 d **Periaate** in solutions.md. en and fi-easy did not exist at e7fb0232a, so for them the diff since their last PASS (24b2a3b87) applies. It is the same one sentence. The packet's full mode was narrowed to that scope.

## Blocking
None.

## Polish
None in scope.

## Checked
- **Fresh captures:** ran `python3 scripts/screenshot.py FY6-sovella --if-stale`, which wrote 135 captures. The stamp is a34f3aab0e6c03cc.
- **review/shots/FY6-sovella-page-390-37.png:** s4 d PERIAATE renders the new sentence. The KaTeX $+Q$ and $-Q$ are inline, with no overflow and normal line breaks at 390 px.
- **review/shots/FY6-sovella-page-390-40.png, -42.png, stage-fy6-s4-390-9.png:** the s4 rubric next to it is unchanged.
- **Typography:** the Finnish is natural, and the plural "varaukset" with the math symbols reads correctly.
- **Hash:** the same at the start and at the end.

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 5 (the changed text only)
