VERDICT: PASS
CONTENT-HASH: 0aaebdea05a575a8

## Blocking

## Polish

## Checked
Delta review against the Finnish diff since a6af45ae. Compared every changed passage in en: the F_x graph text (figures.json, aria-label, axis labels F_x, hard/soft/equal areas), the sim texts (inquiry.json text/model/calc, lang sims.fy4-9.selite), hook, check-3 option and model answer (we assume, net force, surface force larger by the weight), the rebound passages (-2mv, magnitude 2mv, summary bullet, misconceptions), the mat paragraph and the 'impulse of the net force' wording. All agree with the Finnish; decimal point everywhere. Fixed: the hook said 'over the bar more than two metres up'; now 'over a bar more than two metres high', matching the new Finnish.
Ran: check_i18n (0 errors), build.py fy4-9, figures.py fy4-9 --lang en --check (up to date), check_layout fy4-9 --lang en at 360 and 1280 (OK).

- Delta review of commit 841247de (crushable bumper): inquiry.json `model` and `calc` and the lesson.md force-time figure polygons compared with the Finnish; the new sentences, F = -F_\text{max}\sin(\pi t/\Delta t), the "elastic" qualifier and the figure points agree; the old "force ends immediately" sentence is gone. check_i18n 0 errors, build, figures --check, check_layout 360/1280 OK.

- Delta re-check (round 4): the crushable-bumper model and calc texts in inquiry.json (sine-shaped pulse, mean about $0.64\,F_\text{max}$, half-way maximum, direct integration during the pulse) compared with the Finnish; numbers, formula and wording agree. model.js and sim-spec changes need no translation. check_i18n 0 errors, figures --check and build run.
