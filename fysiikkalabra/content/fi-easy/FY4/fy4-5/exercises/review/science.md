VERDICT: PASS
CONTENT-HASH: a43ca0c07950edcc

## Blocking

## Polish
- Layout check (`check_layout.py fy4-5 --lang fi-easy`, 360 and 1280 px) reports a figure-label overlap "N / F_y" that is identical in the Finnish preview (generated figure, not translation text).

## Checked
- Delta `git diff a6af45ae` of fi, en and fi-easy for fy4-5; every changed passage compared with the Finnish: L3-03 answer "0,061 N ≈ 0,06 N" with the justification that the normal force is a difference and the decimals of the buoyancy 0,10 N decide; the 12 spec blocks beside the Voimakuvio steps (G, N, T, F, F_mu values, directions, @-options, komponentit lines) compared line by line with the Finnish. Numbers and units agree.
- All `voimakuvio` blocks in solutions.md identical to the Finnish (check_i18n enforces); `check_i18n.py` 0 errors; `build.py fy4-5` builds; `figures.py fy4-5 --lang fi-easy --check` up to date.
