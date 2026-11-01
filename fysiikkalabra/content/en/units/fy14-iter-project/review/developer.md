VERDICT: DONE

Unit fy14-iter-project, "ITER: why, where and who" (FY14 chapter 7, order 1). Developer report 2026-11-01. Content hash at hand-over: 6fd354047c49d122.

## Files
- `content/en/units/fy14-iter-project/unit.md`: Why line (no answer given), hero, sections Why (Geneva 1985, reasons for sharing), Schedule (2016 vs 2024 baseline table + figure, reasons), Members (shares, in kind, Domestic Agencies, ITER Organization, Council, DG), Challenges (technical vs organisational, status Nov 2026), misconception, summary. Theory summary (selita) about 306 words.
- `inquiry.json` (24 activities): hook, retrieval choice; 2 predictions (why share → reveal theory-why; new schedule → reveal theory-schedule); timeline component (era cooperation) with an explain question; site contest source (interpret + choice); word bank + pair discussion on the host; theory; challenge sorting (match); reflect; order component (milestones); error-spotting choice; 60–80-word newsletter paragraph (short written task, model + criteria); optional role-play Moscow 2005; 3 checks, big-question explain, summary, French corner with `say`.
- `unit.json` (9 sources, checked 2026-11-01), `teacher.md` (75-min timing, organisation, assessment, difficulties, fast pairs / short of time, extensions).
- `lessons/units/fy14-iter-project/figures.py`: hero (Provence site, cranes, convoy; no text, no people), schedule (2016 vs 2024 baseline to scale, labels 26 units in a 600-wide figure).

## Facts verified (2026-11-01)
- Geneva Nov 1985 Gorbachev–Reagan; 1987 four partners (EC/Euratom, Japan, USSR, USA), CDA 1988–90, EDA 1992–98/2001; US left 1998, back 2003; China, Korea 2003, India 2005 — Wikipedia ITER; timeline.json.
- Site: candidates Clarington (withdrawn Dec 2003), Vandellòs, Cadarache, Rokkasho; EU choice 26 Nov 2003; Dec 2003 deadlock (EU, China, Russia vs Japan, Korea, US — Wikipedia); Moscow 28 June 2005; Broader Approach (JT-60SA, materials facility) — iter.org/node/18040; first DG Kaname Ikeda (Wikipedia). ~75 km north of Marseille; 180 ha / 42 ha platform; requirements; Manosque school; 104 km itinerary — iter.org ITER France, facts.
- Members, shares 45.6 % / 9.1 %, ~nine-tenths in kind, Domestic Agencies, 100 % of results and IP shared, UK left after Brexit, Switzerland in F4E from 1 Jan 2026 — iter.org Members. Agreement 21 Nov 2006, Organization 24 Oct 2007 — Wikipedia. Barabaschi appointed Sept 2022, in office Oct 2022 — iter.org/print/whatsnew/352. ~5,000 people (2026) — iter.org facts.
- 2016 baseline first plasma 2025, full current 2033, D–T 2035; 2024 baseline SRO 2034, D–D 2035, full magnetic energy 2036, D–T 2039; reasons — ITER PDF 3 July 2024. ~€5 billion extra — Wikipedia. Bevel and thermal-shield defects, repairs — iter.org/node/20387. Sixth of nine modules 28 July 2026, ~six months ahead — ITER press release 29 July 2026.

## Open questions
- "In 2022 ... defects found" and "stopped the assembly for about two years": the ITER article (Sept 2023) implies 2022; timeline.json states the two-year stop. A reviewer may want a primary source with the exact date.
- Photo placeholder `<!-- photo: iter-site-aerial -->` in the site source.

## Shared issues (not edited)
1. `scripts/screenshot.py` opens the pages as `file://`, so components that fetch a data file (`timeline`, `iter`, `map`) show "could not be loaded (TypeError: Failed to fetch)" in the captures. Over HTTP (python3 -m http.server -d preview) they load and work; I checked this. Proposed fix: serve `preview/` with a local HTTP server in screenshot.py (and check_layout.py), as the components need it.
2. The course brief links Yle "https://yle.fi/a/20-153568" for the ITER media task, but that page is an Yle Oppiminen French lesson, *Osa 4: Ravintolat, kahvilat, baarit* (2012, updated 2016), about restaurants and cafés. It is not about ITER. The media unit uses two verified Yle ITER articles instead (2020 and 2005) and says so in teacher.md. Proposal: offer the café page to the developer of `fy14-fr-cafe`.
3. `scripts/test_inquiry.py` / `check_choices.py` do not cover units (known); I tested predictions, reveals, model answers, choices, numeric and components with my own Playwright script over HTTP.
4. `docs/FY14_PLAN.md` says the B1M video's spoken content could not be read. The channel's own page (theb1m.com/video/inside-iter-worlds-largest-nuclear-fusion-reactor) publishes the narration as an article; the plan could mention it as the verification source.
