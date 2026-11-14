VERDICT: PASS
CONTENT-HASH: 6c0936636b690650
SCOPE: delta added-exercise from 5e217585a15dde17 base 8f23aa7ae3bd

## Blocking

## Polish
- solutions.md (fy6-11-L1-09, Järkevyys) — the check only repeats the table value (3 kV/mm × 2,5 mm), so it is circular. A real check is, for example, "a 7,5 kV spark across a few millimetres matches the familiar static-electricity spark of some kilovolts", or the inverse: E = U : d = 7,5 kV : 2,5 mm = 3,0 kV/mm.
- solutions.md (fy6-11-L1-09, Vastaus) — the table's breakdown strength is a typical value for dry air at normal pressure. In a gap of a few millimetres the measured sparking voltage is somewhat higher (about 9 kV at 2,5 mm). One clause such as "taulukon arvo on likimääräinen" would keep the result from looking exact. This is a level-appropriate simplification (C), not an error.

## Checked
- Hash 6c0936636b690650 at start and end; only fy6-11-L1-09 was judged (delta added-exercise).
- Physics: in a uniform field E = U : d, and a spark forms when E reaches the breakdown strength, so U_max = E_l·d. The plates are in air and the task states that the field is uniform.
- Recomputed: 3,0 kV/mm · 2,5 mm = 7,5 kV, which equals answers.py and the json (unit kV). The tolerance of 10 % (6,75–8,25 kV) covers table values from about 2,7 to 3,3 kV/mm, so a student using an older or newer MAFY edition is not marked wrong.
- The conversion is right: kV/mm · mm = kV, so the step needs no SI detour. The rounding to two significant figures follows the data.
- Scope: läpilyöntilujuus is one of FY6's central contents (sähköturvallisuus), and E = U : d is the brief's formula, so the task needs nothing the lesson does not teach.
- The solution is complete: given and asked, principle, U = Ed solved symbolically, conversions, substitution, answer with its reason, and a check (weak, see Polish).
