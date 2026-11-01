VERDICT: PASS
CONTENT-HASH: d996ffa7f72afcaa

First pedagogy review of fy14-global-fusion-explorer (2026-11-01). The page was built with `python3 scripts/build.py fy14-global-fusion-explorer`, served on port 8775 and tested in Playwright at 390 and 1280 px. The map tiles are blocked in this sandbox (the only console errors are failed tile requests), so I tested the list, the filters, the panels and the hash links. The map canvas could not be judged.

## Blocking
None.

## Polish
1. Workload of the writing tasks. The unit has a findings paragraph, a 60–90-word museum label and a 100–140-word final paragraph. The findings task and `check-write` ask for nearly the same content: counts for two years, machines that cross borders, and one limitation. The findings model is also 146 words for "four or five sentences".
   - Cut `findings` to "three sentences from your table" and shorten its model to match.
   - Or turn `check-write` into a transfer, for example: "Explain to a minister why Finland works through EUROfusion instead of building its own machine, using the explorer."
2. `find-error`, option lengths: the options are 85, 86, 53 and 62 characters. The two long options differ by more than 30 % from the short ones, so a student can narrow the choice by length. The correct option is not the longest. Shorten the two long ones, for example to "The explorer is a selection, not every lab." and "Nothing: others began only after T-3 in 1969."
3. `teacher.md`, *Common difficulties*: it says that TEXTOR shows only "Germany" in 1985. The list now shows "West Germany until 1990 (today Germany)". Update the note, or delete it.
4. `pred-cold`: students who did *Science across the Iron Curtain* know the three secret programmes. The question asks about the explorer's data, so it remains a fair prediction. A note "(in the explorer's selection)" in the options' feedback is already there.

## Checked
- Predictions: neither the hook, the Why line, the hero, the review question nor the Think model gives the counts.
  - In the browser, `pred-cold` and `pred-now` lock with no feedback and stay closed through Reading, the explorer and the missions.
  - They open at *Story* with the committed option's own feedback.
  - The missions are real evidence: the student counts first.
- Every count the missions ask for matches the browser:
  - 1958: 6 facilities in 3 countries;
  - 1963 → 1964: 6 → 4, with Model A leaving after 1963;
  - 1985: 8 facilities in 6 countries;
  - 2026, and Status Operating: 24 facilities in 12 countries;
  - COMPASS has two records, and Model A's panel note explains the ten-year rule.
- Data literacy is taught well: the list is a selection, end years are unknown, today's country names are used, and results can be company-reported. `find-error` and `check-2` test this, with feedback that repairs the misconception.
- Mission 6 links to `fy14-fusion-timeline.html`. The timeline has 56 *Show on the map* links of the form `#f-<id>`, and a fresh load of `#f-jet` opens JET's panel.
- CLIL: there is a word bank and sentence starters for the missions, the findings, the label, the final paragraph and the Think task. There is pair work with swapped roles, a vocabulary match and a French corner. The English is B1–B2.
- All four model answers stay closed with an empty answer and with 5 characters.
- There is no horizontal scroll at 390 px. The 75-minute plan includes plans for fast pairs and for running out of time (missions 1, 3 and 4).

## Shared issues
1. `assets/units/fy14/fx/map.js`, the first tap on a search result is lost. `form.addEventListener('change', draw)` fires when the search field loses focus, and `draw()` rebuilds the list between pointer-down and click. So after typing "COMPASS" (mission 5), the first tap or click on a result does nothing and the second works. I reproduced this with mouse and touch at 390 px. Fix: do not redraw on `change` from the search input (it already redraws on `input`), or keep the existing buttons when the filtered set has not changed.
2. `map.js`, a hash link from the timeline (`#f-jet`) opens the panel but does not scroll to it. On a phone the student lands at the top of the page with the panel about 1000 px below. Fix: call `panel.scrollIntoView()` after `show()` for a hash on load, with `scroll-margin-top` for the sticky stage bar. After a list click, the panel's first line is partly under the stage bar.
3. The reflection says "the data does not support your prediction". This is already known.
