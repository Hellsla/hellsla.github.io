VERDICT: PASS
CONTENT-HASH: 63a171be08f0db43

Pedagogy re-review of fy14-fusion-timeline (2026-11-01), after commit 525827b2. I rebuilt the page and tested it in Playwright at 390 px. The predictions lock when the student commits and open at `theory-patterns`, after the student has done Tasks 5a and 5b. Model answers stay closed until the student writes. No console errors.

## Earlier findings
1. **The old blocking finding (map links) is resolved.** `timeline.js` sends a HEAD request for the map page and shows "Show on the map →" only when the page answers. `fy14-global-fusion-explorer` now exists, and its preview page answers 200. The coordinator will publish it in the same PR as this unit, or not publish this unit at all, so a student never meets a broken link.
2. **Phone usability is resolved.** The cards start closed, and Tasks 3, 5a and 5b have their own small timelines next to the task.
3. **The small timelines are fixed.** Those for Task 3 and Task 5b now have no filters, and their legend lists only the themes they show.

## Blocking
None.

## Polish
1. **`task-map` needs a fallback.** The prompt still says "use *Show on the map*" without a condition. If the map unit is ever missing, the link is hidden and the prompt is wrong. Add one sentence: "If a card has no map link, take the site and the status from the card and your teacher." Change the criterion "status taken from the map panel" to "… from the map panel or the card".
2. **`task-geo` still shows filters.** Its timeline holds 23 events, more than the 12-event limit for small timelines, so it keeps the era buttons, the theme menu and the search. An era button other than *From Geneva to ITER* empties the list. Hide the filters for every `ids` selection, or raise the limit.
3. Task 4 still uses the long main timeline. Suggest the search in its prompt.

## Shared issues
- There are no photographs on the cards yet (the photo pass).
