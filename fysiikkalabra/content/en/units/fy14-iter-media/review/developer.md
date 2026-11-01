VERDICT: DONE

Unit fy14-iter-media, "ITER: promise, progress and reality" (FY14 chapter 7, order 4). Developer report 2026-11-01. Content hash at hand-over: 03667762f34381de.

## Files
- `unit.md`: Why line, hero (old newspaper and tablet with tokamak drawings, grey lines only, magnifier; no text), ThenNow (official information 2018 vs Nov 2026 table), Key idea (date, claim type, who says it), Physics (energy release, difficulty), misconception, summary. Selita about 262 words.
- `inquiry.json` (23 activities): hook, retrieval (where fusion energy comes from); predictions (official first-plasma date in 2018 → reveal theory-thennow; what goes out of date → reveal theory-thennow); choose and read an article (HS 2018, Yle 2020, Yle 2005) with a reading strategy; reading notes under six headings; claim sorting (result / plan / opinion, from the verified Yle articles); the table; comparison task; key idea + physics; word bank + pair discussion; reflect; the 300-word writing task with the six content points of the brief, 7 criteria, outline and a ~300-word model (based on Yle 2020); error-spotting; optional peer feedback; 3 checks; correction-note explain; summary; French corner.
- `unit.json` (9 sources), `teacher.md` (article status, timing, scoring scale, difficulties, fast pairs / short of time), `figures.py`.

## Facts verified (2026-11-01)
- Yle 28 June 2005 "Koeluontoinen fuusioreaktori Ranskaan" and Yle 14 Jan 2020 (Anu Leena Koskinen; VTT Tampere, Timo Määttä, 54 cassettes, ~20 Finnish companies, EU aim 2050s, Tampere parts in 5–10 years) — read via WebFetch.
- 2018 official plan: 2016 baseline, first plasma 2025, D–T 2035 (ITER PDF 2024); "halfway" and ~€20 billion, Bigot DG — phys.org 6 Dec 2017. Earlier first-plasma plan 2020 — Wikipedia. Nov 2026: 2024 baseline, six of nine modules (ITER PR 29 July 2026), all six central solenoid modules stacked 23 June 2026 (timeline.json), ~€5 billion more (Wikipedia), tungsten wall (ITER PDF), UK left / Switzerland back (iter.org Members), Barabaschi since 2022.

## Open questions
- **HS 2018 (dynamic.hs.fi/2018/iter/) could not be opened (hs.fi blocked).** The unit makes no claim about its content; the teacher checks notes on it. Whether students can open it without a subscription is unknown.
- The brief's Yle link 20-153568 is not about ITER (see Shared issues).

## Shared issues (not edited)
1. `scripts/screenshot.py` opens the pages as `file://`, so components that fetch a data file (`timeline`, `iter`, `map`) show "could not be loaded (TypeError: Failed to fetch)" in the captures. Over HTTP (python3 -m http.server -d preview) they load and work; I checked this. Proposed fix: serve `preview/` with a local HTTP server in screenshot.py (and check_layout.py), as the components need it.
2. The course brief links Yle "https://yle.fi/a/20-153568" for the ITER media task, but that page is an Yle Oppiminen French lesson, *Osa 4: Ravintolat, kahvilat, baarit* (2012, updated 2016), about restaurants and cafés. It is not about ITER. The media unit uses two verified Yle ITER articles instead (2020 and 2005) and says so in teacher.md. Proposal: offer the café page to the developer of `fy14-fr-cafe`.
3. `scripts/test_inquiry.py` / `check_choices.py` do not cover units (known); I tested predictions, reveals, model answers, choices, numeric and components with my own Playwright script over HTTP.
4. `docs/FY14_PLAN.md` says the B1M video's spoken content could not be read. The channel's own page (theb1m.com/video/inside-iter-worlds-largest-nuclear-fusion-reactor) publishes the narration as an article; the plan could mention it as the verification source.

## Fixes after review (content hash ce7528c836feb20f)
- Blocking (pedagogy 1): pred-2018 replaced by pred-ages, "Which kind of statement in a careful 2018 article is most likely to be out of date by 2026?" (plans and forecasts / results / opinions / none), with a justification; revealed by the table *ITER then and now*. Back-to-predictions updated.
- Tungsten wall: "decided 2023, part of the 2024 baseline".
- Table shortened (topics "first plasma", "D–T operation", "wall facing the plasma"; construction cell "6 of 9 vessel modules in the pit (July 2026)"); the solenoid fact moved to a sentence under the table.
- notes model shows the format (two headings filled in), not full notes; claims prompt tells HS readers to sort the Yle statements too; writing task starts "Start in class and finish at home"; title "Writing task: “ITER: promise, progress and reality”"; check-explain starter uses `<em>` (no literal asterisks); LaTeX for −269 °C and 150 million °C in model texts and the sort; `$\text{D–T}$` in running text.
- teacher.md: Yle 2020's "puhdistuskasetit" noted as a loose description that students can check.
- check-3 options rebalanced (correct no longer the longest).
- Checks as for the project unit: all OK.
