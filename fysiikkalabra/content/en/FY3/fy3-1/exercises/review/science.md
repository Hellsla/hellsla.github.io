VERDICT: PASS
CONTENT-HASH: cf6d9ce17e1d805b
Mode: translation
Round: 2

## Blocking
(none)

## Polish
- none

## Checked
- Scripted comparison of fy3-1-L1-09 against the reviewed Finnish: same kind/fbd select, answer (diagram B), 4 choices, one correct flag, figures pick-weight-only/pick-rest/pick-long-pull/pick-extra on the same options, numbers (0.50 kg, 4.9 N, 9.81 m/s2, 4.905 N) and decimal marks.
- Recomputed G = 0.50 * 9.81 = 4.905 N, about 4.9 N = reading, so G and F equal length (B); C (F twice G, about 9.8 N) and D (F_k acts on the meter) are rightly wrong; A misses the hook force.
- Force-diagram checklist: object = body; Earth and hook interactions only; F_k named as the body's force on the meter, not drawn on the body; no motion-force; at rest so forces balance without Newton's laws (FY3 scope kept).
- English is natural, decimal point used, no Finnish left.
- check_i18n.py: no message for fy3-1; build.py fy3-1 succeeds.
- Option figure descriptions in figures.json (pick-rest, pick-weight-only, pick-long-pull, pick-extra) compared with lessons/FY3/fy3-1/figures.py and the Finnish: English text matches the drawn forces (G down from the centre, F up from the top face, F_k down from the bottom face), the lengths (equal; F twice G; all three equal; only G) and the order of the options; no aria-label in Finnish left.
