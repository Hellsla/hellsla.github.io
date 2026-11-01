VERDICT: PASS
CONTENT-HASH: c107808fdf27e4d4

Pedagogy re-review of fy14-iron-curtain (2026-11-01), after commit 3ed55db3. I rebuilt the page and tested it in Playwright at 390 px. Both predictions lock when the student commits. `pred-verify` opens at `theory-d` and `pred-thomson` at `theory-thomson`. Model answers stay closed until the student writes. No console errors.

## Earlier findings: all resolved
1. **The old blocking finding is resolved.** The `learn` goals no longer name the laser measurement or independent verification. Nothing above `pred-verify` answers it now.
2. `thomson-data` comes before the Thomson section. The student reads a width-versus-temperature table (32, 65 and 129 nm for 0.10, 0.40 and 1.6 keV). From it the student finds "four times the temperature, twice the width" and places the measured 100 nm at about 1 keV. The distractor "the width doubles when the temperature doubles" targets the right misconception. The `model` badge and the note are honest about where the numbers come from.
3. `doubt` now comes after the pair exchange and says so.
4. The `pred-thomson` prompt no longer gives away the Doppler link.
5. The `report` prompt now says it can be finished at home.

The unit meets the brief for *Science Across the Iron Curtain*:
- why the two sides cooperated (`why-invite`, the role-play);
- evidence versus circumstances (`doubt`, the sorting, `find-error`, check 3);
- why independent verification matters (the Key idea, the report, the transfer task, check 1).

## Blocking
None.

## Polish
1. `thomson-data`: ask the student to say *between which rows* 100 nm lies before they choose. This makes the interpolation an explicit step, not just one choice among options.

## Shared issues
- The `pair` note is still rendered after the textarea (`scripts/inquiry.py`).

2026-11-01: re-checked the intro sentence changed to "written for this course from historical documents" (Sources and verification no longer published); accurate, clear at B1-B2, no remaining pointer to a hidden section in unit.md or inquiry.json.
