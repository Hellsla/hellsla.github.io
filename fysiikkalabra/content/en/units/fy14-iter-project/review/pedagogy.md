VERDICT: FAIL
CONTENT-HASH: 62919df3860876fd

Pedagogy review of fy14-iter-project (2026-11-01). Built with `python3 scripts/build.py fy14-iter-project`, served over HTTP and tested in Playwright at 390 and 1280 px. Both predictions lock on commit with no feedback. `pred-why` opens at `theory-why` and `pred-schedule` at `theory-schedule`. All 5 model answers stay closed until the student writes. No console errors and no `.katex-error`.

## Blocking
1. **`inquiry.json` `timeline` (Investigate 1): the timeline is far too long on a phone, and the task does not match it.**
   - With `"eras": ["cooperation"]` the component shows all **40** events of 1985–2026. Every card is already fully open (about 2,200 words), and 18 of the cards are not about ITER.
   - At 390 px the activity is **20,865 px** tall, about half of the 42,300 px page. At 1280 px it is 12,900 px. A student must scroll about 25 screens to reach `theory-why` and the rest of Investigate.
   - The task says "Open at least five cards", but the cards cannot be opened because they are already open.
   - In the 27 minutes that `teacher.md` plans for Investigate, this is not workable.
   - Fix (in the unit): add `"themes": ["politics"]`. This leaves 8 cards (1985, 1987, 2005, 2006, 2007, 2014, 2023, 2024), most of them about ITER. Then rewrite the task as "Read the cards. Note year, what happened, and cooperation / progress / problem." If the assembly cards of 2020, 2025 and 2026 are wanted, use a filter that keeps them, or tell students to type *ITER* in the Search box and read five cards. The longer-term fix is under Shared issues.

## Polish
2. `order-story` `explain` gives **1988** for "Four partners start the conceptual design". `unit.md` (*Why*, *Summary*) says the design started in **1987**. Make them consistent: "In 1987 the four partners agreed; conceptual design ran 1988–1990".
3. `pred-schedule` is close to a pure guess of a number. Ask students to justify with the size of the delays (defects, pandemic). Otherwise this is fine, and nothing before it gives the answer away.
4. Workload: the site source (about 330 words), the pair discussion, the 8-item sort, the 8-item order and the 60–80-word paragraph make Apply full. The time plan in `teacher.md` is realistic only after fix 1.

## Checked
- The Why line and the hero do not answer either prediction.
- CLIL:
  - word bank and sentence starters for every argue/write task (pair-host, write-why, role-play, check-explain);
  - a pair discussion and an optional role-play;
  - the short written task has a model and observable criteria.
- Options are balanced, and the correct option moves between positions and lengths.
- The French corner uses the Finnish *y* and nasal vowels.
- The brief's points for this unit are covered: why ITER was proposed, cooperation, Cadarache, the Members, and the challenges.
- `teacher.md` has a plan for fast pairs and for running short of time.

## Shared issues
- `assets/units/fy14/fx/timeline.js`: cards are always fully expanded, and the only filters are era and theme. Proposed fixes:
  - a `query` or `ids` data option, so that a unit can preset the events it shows;
  - a `collapsed: true` option that shows only the year and title until a card is opened.
- `scripts/screenshot.py` captures data components over `file:`, so they fail to load there (already reported by the developer).
