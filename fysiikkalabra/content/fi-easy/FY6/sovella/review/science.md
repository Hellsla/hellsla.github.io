VERDICT: PASS
CONTENT-HASH: eb7e7e6059e14f57

Scope (teacher's ruling "katselmoi vain muuttuneet osat"): `git diff e7fb0232a -- content/*/FY6/sovella` plus what the changed sentence touches. This translation did not exist at e7fb0232a. Its diff since its last PASS (24b2a3b87) is one sentence, the fy6-s4 d **Principle/Periaate** in solutions.md, the same change as in fi. The packet's full mode was narrowed to that scope.

## Blocking
None.

## Polish
None.

## Checked
- **New Periaate:** "Kondensaattorin toisella levyllä on varaus $+Q$ ja toisella $-Q$. Energia on varastoitunut levyjen väliseen sähkökenttään." This is correct and equivalent to fi. It matches fi-easy fy6-13 lines 51, 393 and 398.
- **Consistency:** $Q$ agrees with s4 c. Rubric criterion 1 ("säilyttää varauksensa ja energiansa") is consistent with the lesson's definition of $Q$.
- **Unchanged parts:** the Mallivastaus (300 V, about 15 J, 0,30 A) is unchanged.
- **Checks:** practice.py check fi-easy is OK (4 tasks, 60 points). The hash is the same at the start and at the end.
