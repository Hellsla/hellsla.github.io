VERDICT: PASS
CONTENT-HASH: d987214288ef5624
## Blocking

## Polish
- content/en/FY4/fy4-6/exercises/exercises.json:350 — the new opening says the points "come from an experiment" and no longer calls them example data or says "kinetic". The figure's own description still says "esimerkkiaineisto". For honesty about invented data, consider "(example data)" after "experiment", and in the Finnish as well.

## Checked
- Diff (L2-09 opening, wording only): "a wooden block was pulled along a table" still implies sliding, that is kinetic friction. That is the same friction as for the decelerating block, so the model $a = F_\mu / m$ still holds.
- Numbers unchanged: line through the origin fitted to fy4-6/mittaus, slope $\approx 0.21$, $F_\mu \approx 1.68\,\text{N}$ at $N = 7.85\,\text{N}$, $a \approx 2.1\,\text{m/s}^2$ (answers.py agrees).
- The Finnish diff makes the same change with the same meaning.
- answers.py run: every numeric answer equals exercises.json.
- Script comparison with content/fi for all tasks: answers, units, tolerances, correct flags and every number identical.
