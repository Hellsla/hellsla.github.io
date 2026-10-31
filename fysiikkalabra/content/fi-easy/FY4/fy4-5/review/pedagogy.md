VERDICT: PASS
CONTENT-HASH: 2e816a88aae946ab

## Blocking

## Polish
- Layout check (`check_layout.py fy4-5 --lang fi-easy`, 360 and 1280 px) reports a figure-label overlap "N / F_y" that is identical in the Finnish preview (generated figure, not translation text).

## Checked
- Delta `git diff a6af45ae` of fi, en and fi-easy for fy4-5; every changed passage compared with the Finnish: reads naturally; same stages, hint order and exit ticket; the changed sentences keep the teaching order (ice-only model in the inquiry, pull and push as the compared cases, the extra T-vs-F remark placed in the model box). fi-easy: short sentences, one idea each (the T/F remark split into four sentences, "vuorotellen" explained by the same scene), terms as before.
- All `voimakuvio` blocks in inquiry.json and lesson.md identical to the Finnish (check_i18n enforces); `check_i18n.py` 0 errors; `build.py fy4-5` builds; `figures.py fy4-5 --lang fi-easy --check` up to date.
