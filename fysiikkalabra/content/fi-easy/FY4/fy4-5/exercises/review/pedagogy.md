VERDICT: PASS
CONTENT-HASH: a43ca0c07950edcc

## Blocking

## Polish
- Layout check (`check_layout.py fy4-5 --lang fi-easy`, 360 and 1280 px) reports a figure-label overlap "N / F_y" that is identical in the Finnish preview (generated figure, not translation text).

## Checked
- Delta `git diff a6af45ae` of fi, en and fi-easy for fy4-5; every changed passage compared with the Finnish: L3-03 answer is phrased as in the Finnish: first the two-decimal result and the one-significant-figure-rounded value, then why (difference, decimals); spec blocks sit directly under each Voimakuvio step as in the Finnish. fi-easy: the answer explanation split into short sentences.
- All `voimakuvio` blocks in solutions.md identical to the Finnish (check_i18n enforces); `check_i18n.py` 0 errors; `build.py fy4-5` builds; `figures.py fy4-5 --lang fi-easy --check` up to date.
