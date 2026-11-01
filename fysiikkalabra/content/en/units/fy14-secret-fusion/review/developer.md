VERDICT: DONE

# fy14-secret-fusion: developer report (2026-11-01)

## Files
- `content/en/units/fy14-secret-fusion/unit.json`: FY14, chapter 5, order 1, kind history, physics + English + French, 75 min, 16 sources.
- `content/en/units/fy14-secret-fusion/unit.md`: the Why line, the hero, six narrative sections placed in Investigate (*Stars* 1920–1939, *War* 1938–1952, *Huemul*, *Machines* with the pinch figure, *ZETA* with the neutron-direction figure, *Geneva 1958*), Key idea + Common misconception (about 300 words, the theory summary), three optional biographies (Richter, Spitzer, Sakharov), Summary.
- `content/en/units/fy14-secret-fusion/inquiry.json`: hook + pair `explain`; two predictions (`pred-secret` revealed by *War*, `pred-zeta` revealed by *ZETA*); a jigsaw reading in groups of four with word bank and starters, expert notes (`explain`), an `order` task of eight events; key idea + reflection; optional biographies and comparison; Apply: ZETA's temperature in eV (`numeric`, seven-step solution, three listed mistakes), claim/evidence/motive `match`, headline error `choice`, pair debate and paragraph (`explain`); Check: three `choice` checks (figure-eight, Z- vs theta pinch, Geneva 1958) and a transfer `explain` (cold fusion 1989), summary, French corner (`say`).
- `content/en/units/fy14-secret-fusion/teacher.md`: timing, jigsaw organisation, fast pairs / short of time, assessment, difficulties, extensions.
- `lessons/units/fy14-secret-fusion/figures.py`: hero (a locked laboratory at night with a glowing ring; no text, no answer), `pinch` (Z-pinch and theta pinch: current, field $\overline{B}$ green, force $\overline{F}$ red), `neutrons` (isotropic vs beam-like neutron emission).

## Facts verified (all checked 2026-11-01; sources in unit.json)
Eddington 1920 (Cardiff); Gamow 1928; Atkinson–Houtermans 1929; Cockcroft–Walton 1932; Oliphant, Harteck, Rutherford 1934 (tritium, helium-3); Rutherford "moonshine" 1933; Bethe 1938–39; fission December 1938; Ivy Mike 1 November 1952; Thomson–Blackman patent 1946; UK classification after Fuchs's 1950 confession (ZETA article); Tamm–Sakharov proposal October 1950, Stalin's decision 5 May 1951, Artsimovich; Project Sherwood; Huemul: Richter arrived 1948, Perón 24 March 1951, Balseiro's inspection 5–8 September 1952, closure 22 November 1952; Richter born 21 February 1909 in Falkenau, died 1991; Spitzer 1951, 50,000 dollars, Matterhorn, Model A 1953; pinch effect, kink and sausage instabilities, Perhapsatron, Harwell and Aldermaston teams; ZETA: mid-August 1957, about a million neutrons per pulse, press conference 24 January 1958 ("90 percent certain"), Rose's direction measurement, retraction 16 May 1958; Geneva 1–13 September 1958 (UN record, FPA); T-1 end of 1958; Sakharov 1921–1989, Nobel Peace Prize 1975, exile 1980; Spitzer 1914–1997.

## Numbers computed (Python, CODATA)
$k_\text{B} T$ for $5.0 \cdot 10^{6}\ \text{K}$: $6.905 \cdot 10^{-17}\ \text{J} = 431\ \text{eV}$ (exact constants 430.9 eV); for $1.0 \cdot 10^{6}\ \text{K}$: 86.2 eV; $1\ \text{eV} \approx 11\ 600\ \text{K}$; $10\ \text{keV}$ ≈ 116 million K; ratio $10\ 000 : 431 \approx 23$.

## Checks
`units.py check` OK; build (draft); `check_layout.py` 360 and 1280 OK; screenshots looked at (hero, pinch and neutron figures, order component). Playwright (Chromium via `_browser.launch`): both predictions lock without feedback and reveal at their sections; every choice, the numeric task and every `explain` answered (model answers stay closed until the student writes); `match` and `order` work; no console errors, no raw `$`, no `.katex-error`.

## Open questions
- The narrative in Investigate is about 1,300 words; the jigsaw splits it so that each student reads about 300 words plus *ZETA* and *Geneva*. The teacher may prefer to give the reading as homework before the lesson.
- Photographs marked: `huemul-island`, `zeta-harwell`, `ronald-richter`, `lyman-spitzer`, `andrei-sakharov`.

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
5. **`assets/units/fy14/css/units.css` / `fx/timeline.js`: the timeline component makes `check_layout.py` FAIL** in *fy14-fusion-timeline* (strip `min-width:600px` overflows 265 px at 360; legend 14 px; `.fx-msg` line 448 px at 1280). Fix: treat `overflow-x:auto` content as scrolling in `check_layout.py`, and `max-width: var(--measure)` on `.fx-msg`/`.fx-note`. Details in that unit's report.

## Fixes after review (2026-11-01)
- Pedagogy 1: new `zeta-data` interpret before *ZETA*: neutron shares along and against the current, before and after reversal (70/30 → 30/70, badge `example`: simplified numbers showing the pattern Rose reported). `pred-zeta` is now revealed by evidence the student handles first.
- Pedagogy 2 / visual 2: `pred-secret` correct option "It was too close to hydrogen-bomb physics and fuel." (both reasons, no dangling "Their"); feedback updated; distractor shortened so the correct option is neither longest nor shortest.
- Pedagogy 3: sort item now "Governments feared that fusion neutrons could make bomb fuel." (motive).
- Pedagogy 4: teacher.md: `check-write` is homework; Investigate re-timed with the ZETA data (3 min).
- Pedagogy 5: `check-1`, `check-3` correct options lengthened (generator now warns on shortest as well as longest).
- Science 1: check-3 Fuchs feedback now says atomic bomb and early hydrogen-bomb ideas before 1950.
- Visual 1: `pinch`: field rings drawn as back half (faint, behind the column) and front half with arrowheads (downwards at the front, right-hand rule for I to the right); a copper arrowhead on the last coil turn shows the coil current. aria-label updated.
- Visual 3: Summary bullet on accelerators now matches the section. Visual 4: `neutrons` key in ink.
- Checks: units.py check OK, build OK, check_layout 360/1280 OK, Playwright (both predictions lock and reveal; no console errors, raw `$` or katex errors), pinch figure looked at.
