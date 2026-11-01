VERDICT: DONE

Unit fy14-global-fusion-explorer, "Global Fusion Explorer" (FY14 chapter 8, order 3). Developer report 2026-11-01.
Content hash at hand-over: 7e1ae7d3661b6fbd; after the shared data and map.js update: ce8f1c5ebc2ecf63 (`python3 scripts/units.py hash fy14-global-fusion-explorer`).

## Files
- `unit.json` (kind explorer, 12 sources checked 2026-11-01), `unit.md` (Why, hero, sections Reading, Story, Key idea, Common misconception, Summary), `inquiry.json` (25 activities), `teacher.md`; `lessons/units/fy14-global-fusion-explorer/figures.py` (hero: the Earth with glowing sites joined by arcs; no text).
- The map component (`data-fx="map"`, `data-src="units/fy14/data/facilities.json"`) sits in the tutki stage, followed by six missions *From Competition to Collaboration* (year slider 1958, start years before 1970, year 1985, status Operating, cross-border panels, back to `fy14-fusion-timeline.html` and its *Show on the map* links, which open this page with `#f-<id>`).
- Predictions: countries with machines that started before 1970 (3) and countries with operating facilities in 2026 (12, three continents); both revealed by the theory section *From competition to collaboration*.

## Facts verified (2026-11-01)
- Counts computed in Python from facilities.json: 60 facilities in 14 countries; starts before 1970 in the US, UK, Soviet Union; year filter 1958: 6 facilities (Model A, Model B, Perhapsatron, ZETA, Scylla I, T-1); 1985 without stale entries: T-10, PLT, TFTR, JET, JT-60, ASDEX, TEXTOR (5 countries); status operating: 24 facilities in 12 countries (US, Canada, UK, France, Germany, Switzerland, Spain, Russia, China, Japan, South Korea, India).
- 1958 Geneva conference and declassification (UN Digital Library, Wikipedia Timeline of nuclear fusion, course timeline); 1969 Culham measurement of T-3, about 10 million °C (UKAEA "Mission to Moscow, 50 years on"); JET Joint Undertaking 30 May 1978 (EUR-Lex 78/471/Euratom); Geneva summit 19–21 Nov 1985; ITER Agreement 21 Nov 2006, seven members (Wikipedia ITER); HL-2A built from the magnet coils and vessel of ASDEX (Wikipedia HL-2A); COMPASS sent from Culham to Prague (Wikipedia COMPASS); JT-60SA Japan–EU, first plasma 23 Oct 2023.

## Browser checks
units.py check OK; check_layout 360 and 1280 OK; screenshot.py captures looked at. Playwright: predictions lock on commit and open when the Story section is on screen; model answers stay closed until the student writes; no `.katex-error`, no raw `$`. Map: tiles fail here (OSM blocked; the only console errors are the failed tile requests), list, filters, panels and `#f-jet` work; year 1958 → 6 of 60, status Operating → 24 of 60, search T-3 → its panel.

## Open questions
- The map needs internet for tiles (teacher.md says so); the map canvas itself could not be judged here.
- The counts in the unit depend on facilities.json: if the data or its year logic is fixed (below), update the counts in pred-now/pred-cold, the Story section, the findings model and teacher.md, and the "unknown years" wording in Reading, find-error and check-2.

## Shared issues
1. **assets/units/fy14/fx/map.js, `live()`**: a retired facility with `end: null` counts as operating in every later year (Model A 1953, Perhapsatron, Scylla I, T-10, NSTX, HL-2A, FTU appear "operating in 2026"; T-10 even as "Soviet Union" in 2026). Proposed fix: for `status === 'retired'` and `end == null`, treat the facility as live only in its start year (or add `end_approx` to the data and use it), and mark such lines "end unknown". The unit currently teaches students to spot this.
2. **facilities.json, t-3**: `start: null`, so T-3, the key device of the Cold-War story, never appears under any year; between 1960 and 1974 no Soviet machine is shown at all. Proposed: `start: 1962` (List of fusion experiments; the note already gives 1960/1962) with the uncertainty in `note`, and an end year if one can be verified.
3. **facilities.json, country_then**: TEXTOR (1981–2013) and Wendelstein 7-AS (1988–2002) are labelled "West Germany" for their whole life, though most of it was in reunified Germany (after 3 October 1990). Proposed: drop `country_then` for them or say "West Germany, from 1990 Germany" in `note`.
4. **facilities.json, compass**: start 1989 and "Built at Culham (1989), restarted in Prague in 2006"; Wikipedia's COMPASS article gives 1992–2002 in the UK and transfer to Prague in autumn 2004 (operation in Prague from 2006). Check the Culham start year (COMPASS-C/-D) and add the transfer year.
5. **facilities.json, coverage**: no 1960s–70s machines outside the US/UK/USSR (e.g. France's TFR at Fontenay-aux-Roses, 1973), so the 1975 view shows only the US and the USSR. Adding a few verified European and Japanese machines of the 1970s would make the year filter tell the history more fairly.
6. **map.js, panel focus on a phone**: when a list button is pressed, `panel.focus()` scrolls the panel under the sticky stage bar, hiding its first line at 390 px. Proposed: `scroll-margin-top` on `.fx-map-panel` (units.css) equal to the bar height.

## Update after the shared data fix (2026-11-01)
facilities.json and map.js changed (retired machines with real end years, unknown ends counted to `last_seen` or start + 10, T-3 from 1962, COMPASS split into Culham 1989–2002 and Prague 2008–2021, TFR and Pulsator added). Shared issues 1, 2, 4 and 5 above are resolved; issue 3 was resolved by dropping `country_then`.
- Counts recomputed in Python with the new `live()` rule and checked in the browser: 63 facilities in 14 countries; before 1970 in 3 countries; 1958: 6 in 3; 1963: 6, 1964: 4 (Model A and Perhapsatron leave after start + 10); 1970: T-3 and ST; 1973: ST, TFR, Pulsator; 1985: 8 in 6 (TFR, T-10, PLT, ASDEX, TEXTOR, TFTR, JET, JT-60); 2026: 24 in 12 (Canada in, Italy out), equal to status Operating.
- Rewritten: Reading (unknown end years are counted ten years or to `last_seen`, the panel note says which; COMPASS's two records), missions 2–5 (watch Model A leave after 1963, the 1973 newcomers, year 2026, COMPASS search), findings and check-write models, find-error (now: the explorer is a selection; IPP founded 1960, first listed machine Pulsator 1973; source added to unit.json), check-2 (Model A counted only to 1963), Story (TFR and Pulsator 1973; 24 facilities in 12 countries), unit.json note (63), teacher.md counts and difficulties.
- Rechecked: units.py check, build, check_layout 360/1280 OK, screenshots, Playwright (predictions, 7 choices, models after writing, year filter at 1958/1963/1964/1965/1970/1973/1985/2026, COMPASS search, Model A panel note, `#f-jet` opens JET; only the OSM tile requests fail).

New shared issue:
7. **facilities.json, country_then for TEXTOR and W7-AS**: with `country_then` dropped, the 1985 list shows ASDEX as "West Germany (today Germany)" but TEXTOR (Jülich, also West Germany in 1985) as plain "Germany", so students may count two countries. The unit counts 6 and teacher.md explains it. A per-period label (or a note "West Germany until 1990") would make the list consistent.

## Science and pedagogy review fixes (2026-11-01), hash 3259381ff4df8e48
- Blocking 1: Summary now says the large programmes of the US, USSR and UK were secret until 1958 and that the explorer shows machines only in these three countries before 1970 (no claim that research was limited to them).
- Blocking 2: check-write model, its starter, prompt and criterion say "Before 1970" instead of "During the Cold War"; learning goal says "the early Cold War years".
- Polish: Story notes the selection leaves out West Germany's first Wendelstein stellarators (1960); find-error feedback mentions them too; find-error options shortened to 43–49 characters; teacher.md TEXTOR line now matches the data ("West Germany until 1990"). Shared issue 7 above is resolved by the data.
- Rechecked: units.py check, build, check_layout 360/1280, screenshots, Playwright (only OSM tile requests fail).
