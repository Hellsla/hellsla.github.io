VERDICT: PASS
CONTENT-HASH: cc28e1607c126903

Science review (round 2) of the English translation of fy9-aallot (source `content/fi/units/fy9-aallot/`). Reviewed 2026-11-04.

## Checks
- Round 1 had no Blocking science findings. Round-1 Polish 2 (s2 b "third significant figure") and 3 (s1 d string in two segments) are no longer present in the old wording; the guitarist is now "They".
- `check_i18n.py`: en 0 errors; `practice.py check`: en/units/fy9-aallot 6 tasks, 95 points; `units.py check` OK.
- The new figure translations `"S": "N"`, `"K": "A"` in `figures.json` touch only figure labels: the seismic S/P waves in Check 2 (`v_\text{S}`, `v_\text{P}`) are prose/LaTeX in inquiry.json and correctly keep S (English uses S and P waves too). No numbers, formulas, answers or tolerances changed since round 1.

## Blocking
None.

## Polish
1. `unit.md` and kartta: $f_\text{h}$ (beat frequency) and $v_\text{h}$ (listener speed) keep the Finnish subscript h. Defined in the text, so clear; optional.
