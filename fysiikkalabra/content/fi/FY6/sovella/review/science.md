VERDICT: PASS
CONTENT-HASH: a34f3aab0e6c03cc

Scope (teacher's ruling "katselmoi vain muuttuneet osat"): `git diff e7fb0232a -- content/*/FY6/sovella` plus what the changed sentence touches. The fi content change is one sentence, the fy6-s4 d **Periaate** in solutions.md. en and fi-easy did not exist at e7fb0232a, so for them the diff since their last PASS (24b2a3b87) applies. It is the same one sentence. The packet's full mode was narrowed to that scope.

## Blocking
None.

## Polish
- s4 d rubric criterion 1 still says "säilyttää varauksensa ja energiansa". That is correct under the lesson's definition (fy6-13: "Kondensaattorin varauksella $Q$ tarkoitetaan toisen levyn varauksen suuruutta"), so it needs no change.

## Checked
- **New Periaate:** "levyillä on varaukset $+Q$ ja $-Q$, ja energia on varastoitunut levyjen väliseen sähkökenttään". This is physically correct. It removes the old implication that the capacitor holds a net charge, or holds its energy "on the plates". It matches fy6-13 lines 51, 250 and 393 (total charge zero, energy in the field).
- **Symbol $Q$:** consistent with s4 c ("Kondensaattorin varaus on $Q = CU$") and with the teacher's note $Q = CU = 0{,}099\,\text{C}$.
- **Rest of d:** "Jännite ei katoa" and the Mallivastaus (300 V, ≈15 J, 0,30 A, a 10 kΩ discharge resistor with 9 W) are unchanged and still agree with the Periaate.
- **Checks:** practice.py check is OK (4 tasks, 60 points). The hash is the same at the start and at the end.
