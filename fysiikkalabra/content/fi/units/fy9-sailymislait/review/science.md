VERDICT: PASS
CONTENT-HASH: 7f20b74f0e42076a

Delta review of the FY9 audit fixes (2026-11-10). Previous PASS hash: c2716084d9c1d0b9. The hash was the same at the start and the end of this review.

## Blocking
None.

## Polish
None.

## Checked
- s1 b recomputed: W = 1/2 m v^2 - m g h = 9225 J - 28 959,1 J = -19 734 J = -19,73 kJ; F = |W| / 410 m = 48,13 N; share 68,1 %; a) v = sqrt(2gh) = 26,58 m/s.
- tasks.json answer W = -19.73 kJ (tolerance 0.02) and F = 48.13 N agree with answers.py (-19.734, 48.13) and with the solution (W_muut = -19,7 kJ, F = 48,1 N); answers.py runs and its new assert W < 0 < F holds. The sign now matches the concept criterion (work negative) and the units_precision criterion (negative sign).
- Ennusta lt-1 feedback: the braking distance quadruples only if the mean decelerating force (deceleration) is the same; the condition is now stated, closing a B-type gap (s = v^2/(2a)).
- Preview built with no KaTeX errors.
- Language version checked: fi; the change is the same as in fi, in translation.
