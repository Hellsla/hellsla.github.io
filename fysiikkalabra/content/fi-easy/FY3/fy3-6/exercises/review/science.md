VERDICT: PASS
CONTENT-HASH: 89e1824f0f4efd16

## Blocking
(none)

## Fixed
- nothing needed fixing in the new task L2-08

## Polish
- none (the sig-fig remark on "243 kJ" in the Finnish review is mirrored identically; the Finnish file is not touched)

## Checked
- Compared L2-08 (find the error) in exercises.json and solutions.md with the reviewed Finnish: stem lines 1-4, answer "line 4", five choices, one correct flag, feedback, numbers (-180 K, 1350, -243 000 J, 243 kJ) identical.
- Physics recomputed: 450*3.0*(-180) = -243 000 J; sign means the plate gives out heat; Delta T equal in K and degC; line 4 is the only wrong line.
- Format: Finnish decimal comma as in fi; check_i18n silent for fy3-6; build.py fy3-6 succeeds.
