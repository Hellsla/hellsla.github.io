VERDICT: PASS
CONTENT-HASH: 1d23f75557c706fd

## Blocking

## Polish
- The Finnish needs no changes.

## Checked
Compared lesson.md, inquiry.json (all 305 fields), exit-ticket.json, meta.json and figures.json against the Finnish. A script found the same keys, non-text values, numbers (decimal comma kept) and $...$ counts in every field; no difference. No decimal point in any text or LaTeX (the JSON numeric values like 4.0 are data, as in the Finnish). Figure aria-labels and figures.json keep every number (2 m, 8 m, +6 m, -5 m, 20/120/170 m, 4 km). The SVG bodies of the lesson and of the inquiry graphs are identical to the Finnish ones (only aria-labels differ). Worked example and all computations re-checked by hand (2,5 m/s, 170 m, 39 m, 13 m, 4,8 s). Ran check_i18n (0 errors), build.py fy4-1, check_layout.py fy4-1 at 360 and 1280 px (OK), figures.py fy4-1 --lang fi-easy --check (up to date). Nothing needed fixing.
- Delta review (1d23f75557c706fd): Delta since the passed version: the Finnish exp-1 and exp-3 Vastaus lines changed a colon to a comma (punctuation only); the plain-Finnish lines already use a full stop and short sentences and carry the same values (4,0; -3,0; 1,5 m/s, two significant figures). Physics and numbers unchanged. check_i18n fi-easy 0 errors.
