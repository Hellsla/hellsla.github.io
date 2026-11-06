VERDICT: PASS
CONTENT-HASH: 8e6d80f219b9595c

## Blocking

## Polish
- None.

## Fixed
- No text change needed in this translation.

## Checked
- New task fy4-5-L1-09 (force diagram select, constant velocity, G=N, F=F_mu, options A-D with figures pick-pitka/lisa/tasainen/nopeus) compared with the reviewed Finnish: same id, level, kind, answer, tolerance, correct flags, choice and reason order, every number and formula.
- Recomputed the physics: constant velocity gives F = F_mu and N = G; A (F = 2 F_mu), B (F_k acts on the pusher), D (v drawn as a force) are wrong, C correct.
- solutions.md block matches the Finnish step by step (same equations and numbers).
- figures.json: the four pick-* descriptions match the Finnish and figures.py (arrow lengths, F_k, red v arrow, friction at the corner); no description names the correct option
- check_i18n shows nothing for fy4-5; build.py fy4-5 succeeds.
