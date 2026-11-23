VERDICT: PASS
CONTENT-HASH: d1d2bc69e563c49b

## Blocking
None.

## Polish
None.

## Checked (delta 2026-11-23)
- `git diff HEAD` of investigation.md and figures.py: only the aria-labels of the `model` and `linear` figures changed ("Kuvaaja:" -> "Mallikuvaaja:", "Newtonin jäähtymislain mukaan" -> "Newtonin jäähtymislain mallin mukaan"). Drawn paths, axes, labels and model constants (T_ROOM, T0, K) unchanged.
- Physics of the new wording: correct. They are model curves, not data, and "Kuvaajassa ei ole mittauspisteitä" still holds. The model description is still right: the difference halves in each interval t½ = ln 2 / k, ln(T − T_huone) is linear in t with slope −k, and T approaches T_huone without going below it.
- `git diff 57de8ab9a6 HEAD` (since the previous PASS): investigation.md changed only in the SVG drawing of the hero and setup figures (visual review). The prose, formulas, model assumptions and teacher.md are unchanged. The setup's aria-label still has the probe away from the bottom and walls and a separate room thermometer.
