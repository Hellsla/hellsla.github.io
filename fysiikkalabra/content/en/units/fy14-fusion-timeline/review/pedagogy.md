VERDICT: FAIL
CONTENT-HASH: c017b09db5bac17d

Pedagogy review of fy14-fusion-timeline (2026-11-01). I built the page and tested it in Playwright at 390 px. `screenshot.py` had not been run for this unit. The predictions lock and open at `theory-patterns`. Model answers stay closed until the student writes. No console errors. The theme counts in `task-themes` match `timeline.json` (26/23/15/40 events; politics 9 of 23).

## Blocking
1. **Task 3 and the 53 map links are broken.** Every "Show on the map →" goes to `fy14-global-fusion-explorer.html`, which returns 404: the unit does not exist in `content/en/units/`. `task-map` (7 minutes of the plan) cannot be done. Its criterion "status taken from the map panel" cannot be met. Fix: place a `map` component (`fx/map.js`, `data/facilities.json`) in this unit for Task 3, or until the map unit is published, drop `"map"` from the timeline data and rewrite Task 3 to use the cards.
2. **Phone usability of the investigation.** At 390 px the timeline is about 52,000 px tall with *All eras* (104 cards, all open) and about 12,600 px with one era. The four exploration tasks are *below* it, so a pair on a phone must scroll tens of thousands of pixels between a task and its data. Fix: in `timeline.js`, collapse cards to date and title, opened on tap. Also put the exploration sheet before the timeline, or give each task a "go to the timeline" link and the timeline a sticky control bar.

## Polish
3. **The predictions are revealed by text, not by the student's own evidence.** `pred-time` says "you will check it in the timeline", but no task asks for it. Add to Task 2 or Task 4: "Search *JET*: in which year came 16 MW? How many years after T-1?" Add "Count the countries in the 1950s and since 2015" for `pred-geo`.
4. **Task 1 workload.** Switching four eras and four themes to write 16 numbers is mechanical. Show the per-theme counts in the count line ("23 events: 5 science, 7 machines, 9 politics, 2 people"). Ask the student to interpret them instead.
5. **The brief asks for authentic photographs** on the timeline. The cards are text only until the photo pass. This makes the timeline much less engaging than the brief intends.

## Checked
The chapter's big question is a writing task with starters and observable criteria. `find-error` and check 3 handle plans as plans. The misconception "history is a straight line" is good. `teacher.md` has plans for fast pairs and for running short of time.

## Shared issues
- `assets/units/fy14/fx/timeline.js`: cards are not collapsible and the list is very long (finding 2).
- The `map` links point to an unpublished unit.
