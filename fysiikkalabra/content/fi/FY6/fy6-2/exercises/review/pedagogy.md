VERDICT: PASS
CONTENT-HASH: d98092f0c14ecbc1

## Blocking

## Polish
- solutions.md fy6-2-L2-01 Sijoitus/Vastaus — the Sijoitus ends "= 10,6 %" and the Vastaus "noin 11 %"; add "(pyöristys: 10,6 → 11)" so the rounding step is visible to a student who stops at 10,6 %. exercises.json answer 10,57 with relative tolerance 0,08 accepts 10,6 and 11 (and 10), so the check is fine.
- Earlier polish stays open: L2-03 is a near copy of the worked example; L1-05 and some others are one-step substitutions.

## Checked
- Delta L2-01: Vastaus now "noin 11 %, kaksi merkitsevää numeroa, koska ensimmäinen numero on 1" — follows the brief's rounding rule (one significant figure, two if the first is 1) and is consistent with Järkevyys ("lähes 11 %"); the earlier 10 %/11 % mismatch is resolved.
- answers.py comment matches solutions.md; the answer value 10,57 in exercises.json is unchanged.
- Capture L2-1280-1/-2 (opened): solution steps readable, Muunnokset, Sijoitus and Vastaus agree.
- Finnish reads well; nothing else changed.
