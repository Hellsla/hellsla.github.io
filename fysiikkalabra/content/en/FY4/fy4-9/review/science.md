VERDICT: PASS
CONTENT-HASH: 262fe62f24805e8c

## Blocking

## Polish

## Checked
Delta review against the Finnish diff since a6af45ae. Compared every changed passage in en: the F_x graph text (figures.json, aria-label, axis labels F_x, hard/soft/equal areas), the sim texts (inquiry.json text/model/calc, lang sims.fy4-9.selite), hook, check-3 option and model answer (we assume, net force, surface force larger by the weight), the rebound passages (-2mv, magnitude 2mv, summary bullet, misconceptions), the mat paragraph and the 'impulse of the net force' wording. All agree with the Finnish; decimal point everywhere. Fixed: the hook said 'over the bar more than two metres up'; now 'over a bar more than two metres high', matching the new Finnish.
Ran: check_i18n (0 errors), build.py fy4-9, figures.py fy4-9 --lang en --check (up to date), check_layout fy4-9 --lang en at 360 and 1280 (OK).
