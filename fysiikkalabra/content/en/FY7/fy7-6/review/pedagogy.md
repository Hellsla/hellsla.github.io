VERDICT: PASS
CONTENT-HASH: d18c5c8e6452dfbc

## Blocking

## Polish
- Earlier polish items stand; none is Blocking.

## Checked
- Changed Sijoitus step of the braking task: v1^2 - v2^2 = 625 - 100 = 525 m^2/s^2 is correct.
- F = 2400 kg * 525 m^2/s^2 / (2 * 30 m) = 1 260 000 / 60 = 21 000 N = 21 kN, matching the Kaava step F = m(v1^2 - v2^2)/(2s) and the stated Vastaus and Järkevyys (a = 8,8 m/s^2, 630 kJ).
- The split is a better staged step for the student: the difference of squares is computed first, then inserted; no answer is disclosed earlier.
- check_layout.py fy7-6 --width 340: OK for fi, en and fi-easy.
- Nothing else changed (git diff shows only this solution string per language).
