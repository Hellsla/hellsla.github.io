VERDICT: DONE

Fix round after the science review (one Blocking, two Polish), model solution of `fy4-7-L2-10` only; fi, en, fi-easy.

- `exercises/solutions.md` (three languages), Lisähuomio (Blocking, B): the remark now names the place, not the moment: at the place where the slower car stops, the faster car still has 13,3 m of braking distance left, when the drivers begin to react at the same point. The formula row and the values 14,6 m/s and 52 km/h are unchanged; `answers.py` (`v_left`) already computes them for that place.
- `exercises/solutions.md` (three languages), part a (Polish): "Suurin osa ajaa lähellä rajoitusta" replaced: the largest group, almost half, drives at most 10 km/h over the limit; more than half exceed it, so the mean is above the limit.
- `exercises/solutions.md` (three languages), part d (Polish): "risteykset ja taajamat (mittausasemat eivät ole niissä)" replaced by streets, built-up areas and minor roads, with the note that the data covers only main roads (valta- ja kantatiet).

Unchanged: `exercises.json`, `answers.py`, every formula and number.

Checks: lint 0 errors (4 length warnings, as before), check_solutions ok, check_i18n 0 errors (en, fi-easy), check_lesson all ok, layout 360 px OK in three languages (only the known clipped formulas of docs/clipped-formulas.tsv).
