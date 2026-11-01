VERDICT: DONE

Unit fy14-sun-puzzle, "The puzzle of the Sun's energy" (FY14 chapter 3, order 1, kind history). Developer report 2026-11-01.
Content hash at hand-over: 8e99d0c59ea3fbba.

## Files
- `content/en/units/fy14-sun-puzzle/unit.md` — Why hasn't the Sun burned out?, hero (Sun over a layered cliff with a fossil; no text), *Three candidate explanations* {Candidates} (chemical ≈ 5000 a, Helmholtz 1854, Kelvin 1862 and 1887, geology/biology conflict, Curie–Laborde 1903), Key idea (Eddington, Cardiff 24 Aug 1920; Aston; 0.71 % from AME2020; short quotations), Formula: t = E/L and E = 0.0071·m·c² (`estimates` log-scale figure), staged worked example (lifetime ≈ 10¹⁰ a with three numbered assumptions and a discussion of them), optional Eddington biography, misconceptions, summary.
- `inquiry.json` — 25 activities: hook, review; predictions (Sun of coal → theory-candidates; competing explanations, models layout → theory-key); data table + coal-lifetime numeric; Eddington 1920 extracts (public domain) with a source-evidence choice; `order` timeline (1854–1939); word bank + starters; pair discussion "Kelvin against the geologists"; theory; vocabulary; reflect; worked example; mass-loss numeric (4.26·10⁹ kg/s); optional Kelvin–Helmholtz numeric (3.1·10⁷ a); optional error-spotting (Mc²/L); misconceptions; optional biography; three checks; explain for a younger student with starters; summary; French corner.
- `unit.json`, `teacher.md`, `lessons/units/fy14-sun-puzzle/figures.py`.

## Facts verified (2026-11-01)
- Eddington's address: 24 Aug 1920, British Association, Cardiff (telescoper.blog); text in Nature 106 (1920) read from the University of Colorado copy; quotations checked word for word ("vast reservoir…", "sub-atomic energy…", "But Aston has further shown conclusively that…", "1 part in 120…").
- Helmholtz 1854; Kelvin 1862 "most probable that the sun has not illuminated the earth for 100,000,000 years"; Kelvin 1887 about 20 million years; Curie and Laborde 1903, about 200 000 times coal — Kragh, arXiv:1609.02834. Gamow 1928, Atkinson–Houtermans 1929, Bethe 1938–39 — Kragh, arXiv:2209.00072.
- Sun: M 1.988·10³⁰ kg, L 3.828·10²⁶ W, age 4.6 Gyr, core 15.7 MK, 4.26 Mt/s, lifetime ~10–11 Gyr, red giant in ~5 Gyr — Wikipedia, Sun. Eddington bio — Wikipedia. Anthracite 32.5 MJ/kg — Wikipedia, Heat of combustion. World energy ~590 EJ (2024) — Wikipedia/Energy Institute.

## Numbers (Python, the rounded inputs of the text)
- Coal Sun: 3.25·10⁷ J/kg · 1.99·10³⁰ kg / 3.83·10²⁶ W = 1.69·10¹¹ s = 5350 a.
- GM²/(RL) = 9.91·10¹⁴ s = 3.14·10⁷ a.
- Nuclear: 0.0071 · 0.10 · M · c² = 1.27·10⁴⁴ J → 3.32·10¹⁷ s = 1.05·10¹⁰ a. Mc²/L = 1.48·10¹³ a.
- 4·m(¹H) = 4.031300 u, He-4 4.002603 u → 0.712 %; Eddington's 1.008/4 → 0.79 % ("1 part in 120"; explained in teacher.md).
- L/c² = 4.26·10⁹ kg/s; over 1.45·10¹⁷ s → 6.2·10²⁶ kg = 0.031 % of M. One second of sunlight / 5.92·10²⁰ J per year ≈ 6.5·10⁵ years ("half a million").

## Checks
units.py check, build, check_layout 360/1280 (OK), screenshot.py (55 captures), Playwright run: predictions lock and reveal at their theory sections; timeline, numeric (wrong/right), source question and explains (model closed until text) work; no console errors, KaTeX errors or raw $.

## Open questions
- Kind is `history`; the unit still has physics calculations (the brief's lifetime estimate).
- Photo placeholder: `<!-- photo: arthur-eddington -->`.

## Shared issues (not edited; for the coordinator)
1. `scripts/build.py` (unit branch, the `embedded` loop, about line 419): the data files a component reads are found with `re.findall(r'data-src="(units/[^"]+\.json)"', md_text + inquiry.json text)`, but inside inquiry.json the attribute is JSON-escaped (`data-src=\"units/…\"`), so a component placed in inquiry.json gets no embedded copy and fails from `file:` (CORS) and offline. `scripts/units.py` `ASSET_REF` has the same blind spot, so the data file is not in the content hash. Fix: also match `data-src=\\\\"` (or parse inquiry.json and search the decoded strings). Workaround in my units: an HTML comment in unit.md naming `data-src="units/fy14/data/nuclides.json"`.
2. `assets/units/fy14/units.css` / `fx/reaction.js` energy-scales chart: at 390 px the bar track is 210 px wide but the axis row is 314 px (`.fx-sc-axisrow` keeps an empty label column while the bar rows stack the label above), so the bars do not line up with the logarithmic axis on a phone (D–T ends near 10¹² instead of 3.4 · 10¹⁴). At 1280 px they match. Fix: give the axis row the same grid columns as the bar rows at narrow widths.
3. `fx/binding.js`: at 390 px the graph labels (axis numbers, nuclide labels, "fusion"/"fission") are about 8–10 px, below the 14 px rule, and the $^{56}\text{Fe}$ label touches the $B/A$ axis title.
4. `docs/fy14/writing-guide.md` says there is no `pair` field on `explain`, while the pilot unit uses it as text; I did not use it.

## Fixes after review
Content hash after the fixes: 193182898c9dcf0e (2026-11-01).
- Science, Blocking:
  - Reasonableness no longer claims mixing. The burning region "slowly grows outwards and reaches fresh hydrogen".
  - Teacher note: Eddington's "1 in 120" comes from rounding helium to 4. His values give 0.79 %, about 1 in 126. With helium at 4.003 the loss is 0.72 %. A change of mass scale cannot change the fraction.
- Science, Polish:
  - Radium "over its whole decay".
  - Gamow (alpha decay, 1928), then Atkinson and Houtermans (stars, 1929).
  - `check-explain`: "A helium atom …".
  - Kelvin prompt: "from 1862 to the 1890s … from about 100 million to a few tens of millions of years".
- Pedagogy:
  - The `review` feedback no longer hints at pred-models. It now ends: "Keep this in mind for later in the lesson."
  - `find-error` options are rebalanced.
  - `check-explain` uses $E = \Delta m \cdot c^2$.
  - `check-3` now tests the 70 % hydrogen assumption: shorter, longer or no change.
- Visual:
  - The Key idea display is split into three lines.
  - Kelvin's 1862 claim reads "for less than 100 million years" in the text and in the order component.
  - The estimates aria-label says "about 5000 years" and "about 10 billion years".
  - `find-error` uses $t = Mc^2/L$.
  - Hero: all rock layers now end on the single cliff-face line, with no wedges.
- `check-1` options are rebalanced.
- Checks: all pass. No display overflows at 360.
