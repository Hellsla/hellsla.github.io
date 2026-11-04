VERDICT: PASS
CONTENT-HASH: 271c1d1ab8c947a2

Science review (round 3) of the English translation of fy9-aallot (source `content/fi/units/fy9-aallot/`). Reviewed 2026-11-04.

## Checks
- No translation file changed since round 2 (only the shared figlib fix and the figure redraw). Physics, numbers, answers, formulas and tolerances remain as in the round-2 PASS.
- Redrawn figures checked against the source: concept map formulas (F = -kx, T = 2π√(m/k), T = 2π√(l/g), v = fλ, Δs = nλ, f_n = n·v/(2L), beats, Doppler, L = 10 dB·lg(I/I0)) intact; pilli 350/3000 ≈ 0.12 m and 1500/3000 = 0.50 m; ominais N/A placement correct for string, open and closed tube; s3 slope (3.69 − 0.46)/0.80 ≈ 4.04 s²/m, intercept 0.055 s². Decimal points throughout.
- `check_i18n.py`: en 0 errors; `practice.py check`: en/units/fy9-aallot 6 tasks, 95 points; `units.py check`: 77 units ok.

## Blocking
None.

## Polish
1. `unit.md` and the concept map: $f_\text{h}$ (beat frequency) and $v_\text{h}$ (listener speed) keep the Finnish subscript h. Defined in the text, so clear; optional.
