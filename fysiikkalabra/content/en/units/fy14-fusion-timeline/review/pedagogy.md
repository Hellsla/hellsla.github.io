VERDICT: FAIL
CONTENT-HASH: 239a2f7980246a6a

Pedagogy re-review of fy14-fusion-timeline (2026-11-01), after commit 3ed55db3. I rebuilt the page and tested it in Playwright at 390 px. The predictions lock when the student commits and open at `theory-patterns`, after Tasks 5a and 5b. Model answers stay closed until the student writes. No console errors.

## Earlier findings
- **Old Blocking 2 (phone usability) is resolved.** The cards now start closed. The main timeline is about 15,200 px at 390 px, down from 52,000. Tasks 3, 5a and 5b have their own small timelines next to the task (1,100, 4,100 and 1,000 px).
- **Old Polish 3 is resolved.** In `task-geo` the student counts the seven countries and in `task-steps` subtracts the years (39). Both predictions are now revealed after the student has checked the data.
- **Old Polish 4 is resolved.** Task 1 gives the counts. The student checks one row and interprets the list.

## Blocking
1. **The map links still return 404 (old Blocking 1).** The page now has 56 "Show on the map →" links, including the three in Task 3's own small timeline. All go to `fy14-global-fusion-explorer.html`, which does not exist: there is no `content/en/units/fy14-global-fusion-explorer/`. Nothing in the build or the review gate holds this unit back until the map unit is published. "Published together" is a note in `teacher.md`, not a check. `task-map` and its criterion "status taken from the map panel" cannot be done.
   Fix, one of:
   - in `timeline.js`, show "Show on the map" only when the target page exists in the build;
   - leave `"map"` out of the unit's timeline elements until the map unit passes its reviews;
   - give Task 3 a `map` component (`fx/map.js`, `data/facilities.json`) on this page.

   When the map unit exists and is published with this one, this finding is resolved.

## Polish
2. **The small timelines (`ids`) still show the era buttons, the theme menu and the search.** In `task-geo`, choosing an era such as "The birth of modern physics" gives an empty list. Hide the filters when `ids` is set.
3. Task 4 (turning points) still uses the 15,000 px main timeline. Suggest the search or an era button in its prompt.

## Shared issues
- `fx/timeline.js`: the small timelines show filters that do not apply to them (Polish 2), and the links to the map unit are not checked (Blocking 1).
- There are no photographs on the cards yet (the photo pass). The brief asks for them.
