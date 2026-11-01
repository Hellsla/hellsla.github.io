VERDICT: DONE

# fy14-fusion-timeline: developer report (2026-11-01)

## Files
- `content/en/units/fy14-fusion-timeline/unit.json`: FY14, chapter 5, order 4, kind explorer, 75 min, 6 sources.
- `content/en/units/fy14-fusion-timeline/unit.md`: Why line, hero, *How to use the timeline*, *The timeline* (the `timeline` component with `{"map": "fy14-global-fusion-explorer.html"}`), *What the timeline shows* (Key idea), misconception, Summary.
- `content/en/units/fy14-fusion-timeline/inquiry.json`: hook + "three events you remember"; predictions `pred-geo` and `pred-time` (both revealed by *What the timeline shows*); exploration sheet Tasks 1–4 (themes by era, claims and checks, timeline to map, turning points); back to predictions; pattern matching, plan-or-fact error, optional own timeline card; three checks, the chapter's big-question paragraph, summary, French corner.
- `content/en/units/fy14-fusion-timeline/teacher.md` (plans for fast pairs and for running out of time).
- `lessons/units/fy14-fusion-timeline/figures.py`: hero (a road from a star to a ring machine through four era landscapes; no text).

## Numbers computed (from timeline.json, counted with the era buttons)
Events by era and theme (discovery / machine / politics / people): modern physics 19/5/0/2 = 26; nuclear age 5/7/9/2 = 23; tokamak race 4/8/3/0 = 15; cooperation 6/26/8/0 = 40; total 104. T-1 (1958) to JET's D–T record (1997): 39 years.

## Checks
`units.py check` OK; build OK; screenshots looked at (timeline, cards, hero). Playwright: both predictions lock and reveal at *What the timeline shows*; all tasks answered; era buttons, search and map links work; no console errors, raw `$` or katex errors. `check_layout.py` 360/1280 FAILs only on the shared timeline component (Shared issue 5).

## Open questions
- The map links open `fy14-global-fusion-explorer.html` (chapter 8); they work only once that unit is published. teacher.md has a fallback.
- ITER dates after 2026 are labelled as the 2024 baseline plan.

## Shared issues (not edited; worked around in the unit)
1. **`scripts/build.py` (about line 420) and `scripts/units.py` `ASSET_REF` (line 48): a `data-src` inside `inquiry.json` is not found.** In the JSON file the attribute is escaped as `data-src=\"units/…\"`, so the regex `data-src="(units/…)"` does not match. The data file is then neither embedded in the page (the timeline shows "could not be loaded (TypeError: Failed to fetch)" from a file or preview) nor counted in the content hash. Fix: match `data-src=\\?"(units/[^"\\]+\.json)\\?"` in both places, or search the decoded activity texts. Workaround: the timeline component of *fy14-fusion-timeline* sits in a `unit.md` section (`## The timeline {Timeline}`) placed by a `theory` activity.
2. **`assets/units/fy14/fx/timeline.js`, the biography line** shows the raw ISO dates, e.g. "Arthur Eddington (1882-12-28–1944-11-22)". Fix: show years only (`born.slice(0,4)`) or `A.date()` for both. Also: the card ids are `ev-<event id>`, so two timelines on one page would repeat ids; prefix them with `el.id`.
3. **`assets/units/fy14/fx/timeline.js` / `units.css`: the theme legend** is reported by `check_layout.py --width 360` as `small … 14 px text: "●Scientific discovery"` (the run still ends OK/see the timeline report). Fix: legend font size at least the body size.
4. **`assets/units/fy14/data/timeline.json`, facts to correct or source:**
   - `jet-first-plasma-1983`: "JET was completed on time and on budget" is not in the cited sources (the Wikipedia JET article gives the cost, 198.8 million EUA, but no such statement). Cite a EUROfusion/UKAEA source for it or remove the clause.
   - `tftr-1982`: "It had been approved in 1976" — PPPL says 1976, Wikipedia says funding was granted in January 1975. Write "approved in the mid-1970s" or name PPPL as the source of 1976.
   - `jet-decision-1978`, date `1978-04-01`: Wikipedia gives 1 April 1978 for the funding approval of the JET Joint Undertaking; I could not open the Council decision itself. Please confirm against a EUROfusion/EU source (I remember a Council decision of 30 May 1978, unverified).
   - `culham-five-1969`: correct in substance; the 1969 paper's authors include the Soviet physicist V. V. Sannikov (Nature 224, 488), a detail worth adding to the card because it shows the cooperation.
   - Checked and correct (no change): Eddington 1920, cyclotron 2 January 1931 and 4.8 MeV in 1932, Ivy Mike (74 t, 10.4 Mt, 1.9 km crater), Huemul dates, Spitzer's 50,000 dollars, ZETA dates (mid-August 1957, 24/25 January 1958, retraction 16 May 1958), Geneva 1–13 September 1958, T-1 end of 1958, Novosibirsk 1968, Symmetric Tokamak (December 1969 – May 1970), oil-crisis budget 40 → 332 million, PLT 20 December 1975 and 24 July 1978, JET 25 June 1983, JT-60 8 April 1985, Geneva summit 19–21 November 1985, ITER 1987 naming.
5. **`assets/units/fy14/css/units.css` / `fx/timeline.js`: the timeline component makes `check_layout.py` FAIL** in *fy14-fusion-timeline*. At 360 px the year strip overflows by 265 px (`.fx-tl-strip svg{min-width:600px}` inside an `overflow-x:auto` box); at 360 and 1280 the legend is 14 px (issue 3); at 1280 the `.fx-msg` count line ("104 events shown.") is 448 px long. Fix: let `check_layout.py` treat content inside `overflow-x:auto` as scrolling, as it does for tables (or let the strip fit at narrow widths), and give `.fx-msg`/`.fx-note` `max-width: var(--measure)`.

## Fixes after review (2026-11-01)
- Science blocking 1: *Claims and checks* now says the three claims "all failed when others checked them. Only ZETA's team withdrew its claim; Huemul was exposed by an inspection, and other laboratories could not repeat cold fusion."
- Science blocking 2–3, polish 2 (timeline.json): fixed in the shared file by the coordinator.
- Science polish 1: Kurchatov feedback: "The head of the Soviet atomic programme described secret Soviet fusion experiments in a lecture in Britain".
- Pedagogy blocking 1: map links kept (published together with fy14-global-fusion-explorer); teacher.md says so, with the fallback.
- Pedagogy blocking 2: cards are now collapsed (shared). Tasks 2, 3 and 5 have their own small timelines (`ids`) beside the task, so on a phone the cards are next to the task; Task 3's small timeline carries the three map links (checked: #f-t-3, #f-jet, #f-jt-60).
- Pedagogy 3: new Task 5a/5b (`task-geo`, `task-steps`, before *What the timeline shows*): count the countries in a small timeline of the events since 2015 (seven) and subtract T-1's year from JET's 16 MW year (39). Both predictions are now revealed after the student has checked the data.
- Pedagogy 4: Task 1 gives the 16 counts; students check one row with the buttons and interpret.
- Visual 3: the seven countries since 2015 are named. Visual 2 (LaTeX in timeline.json card texts) is in the shared data file; not edited.
- How-to and teacher.md updated (closed cards, small timelines, new timing). Option lengths re-balanced (pred-geo, find-error, check-1).
- Checks: units.py check OK, build OK, check_layout 360 and 1280 OK (the earlier component failures are gone), Playwright OK (5 timelines on the page, no console errors).
