VERDICT: PASS
CONTENT-HASH: 813e39295d5df5d4

Scope (teacher's ruling "katselmoi vain muuttuneet osat"): `git diff e7fb0232a -- content/*/FY6/sovella` plus what the changed sentence touches. This translation did not exist at e7fb0232a. Its diff since its last PASS (24b2a3b87) is one sentence, the fy6-s4 d **Principle/Periaate** in solutions.md, the same change as in fi. The packet's full mode was narrowed to that scope.

## Blocking
None.

## Polish
- s4 d: in "the battery that charges it", "it" now follows "the plates…the field". The referent (the capacitor) is still clear from context. "that charges the capacitor" would be crisper.

## Checked
- **New Principle:** "The plates of a capacitor carry the charges $+Q$ and $-Q$, and the energy is stored in the electric field between the plates". This is correct and is a faithful rendering of the fi sentence. It matches en fy6-13 line 393 (total charge zero, energy in the field).
- **Consistency:** $Q$ agrees with s4 c ($Q = CU$). Rubric criterion 1 ("keeps its charge and energy") is consistent with the lesson's meaning of $Q$ as the magnitude of one plate's charge.
- **Unchanged parts:** the Model answer numbers (300 V, about 15 J, 0.30 A) are unchanged.
- **Checks:** practice.py check en is OK (4 tasks, 60 points). The hash is the same at the start and at the end.
