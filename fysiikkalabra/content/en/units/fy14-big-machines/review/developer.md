VERDICT: DONE

# fy14-big-machines: developer report (2026-11-01)

## Files
- `content/en/units/fy14-big-machines/unit.json`: FY14, chapter 5, order 3, kind history, 75 min, 17 sources.
- `content/en/units/fy14-big-machines/unit.md`: Why line, hero, sections *After the stampede*, *Heating beyond the current* (with the `heating` figure), *Stronger magnets*, *Oil, money and big machines* (with the `budget` chart), *Geneva 1985* (joint statement quotations, Reykjavik, Vienna 1987, design phases, US exit and return, Cadarache 2005, agreement 2006, cost growth, the 2024 baseline dated "as of November 2026" and labelled as plans), Key idea + misconception (about 260 words), Summary.
- `content/en/units/fy14-big-machines/inquiry.json`: hook, review `choice` (Lawson conditions); predictions `pred-heat` (revealed by *Heating*) and `pred-budget` (revealed by *Oil*); a "newspaper desk" reading guide; data table of the machines (`interpret`, `source: statistics`); source question on the joint statement (`explain`); `order` task 1973–1988; key idea + reflection; Apply: neutral-beam speed (`numeric`, seven steps), find-the-error `choice` on the 1978 record, group debate on public money in 1976 and today + paragraph; Check: three `choice` checks (why neutral, superconductors, Geneva 1985) and a transfer `explain` comparing Geneva 1958 and 1985; summary; French corner.
- `content/en/units/fy14-big-machines/teacher.md`.
- `lessons/units/fy14-big-machines/figures.py`: hero (a huge tokamak hall with faceless people for scale; no text), `heating` (ohmic current, neutral beam, radio waves), `budget` (bar chart to scale, one series, direct labels).

## Facts verified (2026-11-01)
Ohmic heating limit 20–30 million K, NBI and RF heating, T-7 first superconducting tokamak 1979 (Wikipedia *Tokamak*); PLT operational 20 December 1975, about 60 million degrees on 24 July 1978, Innsbruck August 1978; PLT injectors 40 keV, four for PLT (OSTI); 2.4 MW and 6.5 keV ions (PRL 43, 270, 1979); T-15 superconducting, first plasma 1988; oil embargo October 1973 – March 1974, targets that had supported Israel in the Yom Kippur War; US fusion budget FY1973 40, FY1978 332, FY1984 469 million dollars (FPA); TFTR approved 1975/1976 (sources differ; unit says mid-1970s), construction 1980, operation 1982, D–T from December 1993, 10.7 MW 1994; JET site end of 1977 after a long debate, Joint Undertaking 1978, first plasma 25 June 1983; JT-60 8 April 1985 (JAERI, Naka); INTOR 1978; Gorbachev General Secretary 11 March 1985; Geneva 19–21 November 1985, no arms-control breakthrough; joint statement wording (Reagan Library); Velikhov's role; Reykjavik October 1986, Vienna March 1987, CDA 1988–1990, EDA 1992–1998, US 1998/2003, Cadarache June 2005, agreement 21 November 2006; 2024 baseline (SRO 2034, D–T 2039); cost 5.9 → about 18–22 billion euros.

## Numbers computed
Budget ratio $332 : 40 = 8.3$; deuterium atom $m = 2.014101778\ \text{u} = 3.3445 \cdot 10^{-27}\ \text{kg}$; $E_\text{k} = 40\ \text{keV} = 6.409 \cdot 10^{-15}\ \text{J}$; $v = \sqrt{2E_\text{k}/m} = 1.958 \cdot 10^{6}\ \text{m/s}$ ($0.65\ \%$ of $c$); 60 million K ↔ 5.17 keV; ion cyclotron frequency of deuterium at 3 T: 22.9 MHz (teacher extension).

## Checks
`units.py check` OK; build; layout 360/1280 OK (after shortening the machine table and moving two chart labels); screenshots looked at. Playwright: predictions lock and reveal at their sections; all tasks answered; `order` works; no console errors, raw `$` or katex errors.

## Open questions
- The joint statement is quoted only in the fragments I could verify; the full paragraph is in the Reagan Library source.
- Photographs marked: `jet-torus-hall`, `geneva-summit-1985`.

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
