VERDICT: PASS
CONTENT-HASH: a34f3aab0e6c03cc

Scope (teacher's ruling "katselmoi vain muuttuneet osat"): `git diff e7fb0232a -- content/*/FY6/sovella` plus what the changed sentence touches. The fi content change is one sentence, the fy6-s4 d **Periaate** in solutions.md. en and fi-easy did not exist at e7fb0232a, so for them the diff since their last PASS (24b2a3b87) applies. It is the same one sentence. The packet's full mode was narrowed to that scope.

## Blocking
None.

## Polish
None.

## Checked
- **Course alignment:** the new Periaate now uses the course's own corrected model, as in fy6-13. That lesson names the misconception "ladattu kondensaattori on kokonaisuutena varattu" and answers it with $+Q$/$-Q$ and energy in the field. The sovella solution no longer contradicts what the lesson just taught.
- **Readability:** splitting the old sentence makes the step clearer: the plates' charges, then where the energy is, then "Jännite ei katoa…". Each sentence has one idea, and the length is about the same as before.
- **Fit to the question and rubric:** the Periaate still leads to the d answer, which asks about danger, safe discharge and current. Rubric criterion 1 ("säilyttää varauksensa ja energiansa") is consistent with the lesson's definition of the capacitor's charge $Q$. Points are unchanged (14 for s4, 60 in total), and practice.py check is OK.
- **Hash:** the same at the start and at the end.
