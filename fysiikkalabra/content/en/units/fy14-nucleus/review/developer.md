VERDICT: DONE

Unit fy14-nucleus, "Building nuclei: isotopes and nuclear notation" (FY14 chapter 2, order 1). Developer report 2026-11-01.
Content hash at hand-over: 32e35f45c81f307f.

## Files
- `content/en/units/fy14-nucleus/unit.md` — Why question (why protons do not fly apart), hero, *Inside the atom* {Particles} (particle table), Key idea (Z, isotopes, hydrogen isotopes figure), Formula: Mass number and nuclear notation (notation figure), *The force that holds the nucleus* {Forces} (range figure), staged worked example (iron-56: N, R = r0·A^(1/3), density; seven labelled stages), optional *The people behind the neutron* (Chadwick), Common misconception, Summary. An HTML comment names the data file (shared issue 1).
- `content/en/units/fy14-nucleus/inquiry.json` — 24 activities: hook, review choice; three committed predictions (one more neutron → revealed by theory-main; what holds the nucleus, models layout → theory-forces; N vs Z in heavy nuclei → theory-forces); Isotope Builder (`isotopes`, zmax 26, six check tasks incl. deuterium, tritium, helium-3, carbon-14, iron-56, the unbound diproton); table of stable nuclei (NUBASE2020) with an N/Z numeric task; word bank + sentence starters; pair conclusion; theory; `match` vocabulary; reflect; worked example; Coulomb-force numeric (58 N); optional error-spotting (oxygen-17); misconception; optional biography; three tarkista choices (isotopes, U-235 neutrons, why heavy nuclei need neutrons); explain (tritium vs helium-3) with starters; summary; French corner with `say`.
- `content/en/units/fy14-nucleus/unit.json`, `teacher.md` (75-min timing, fast pairs / out-of-time plan, criteria, difficulties, extensions).
- `lessons/units/fy14-nucleus/figures.py` — hero (atom cloud, magnified nucleus; no text), `hydrogen`, `notation`, `ranges` (labels ≥ 26 units in 600-wide figures).

## Facts verified (2026-11-01)
- Rutherford nucleus 1911; R = r0·A^(1/3), r0 ≈ 1.25 fm (I use the common 1.2 fm and call it an estimate); nucleus 1/60 000 (H) to 1/27 000 (U) of the atom — Wikipedia, Atomic nucleus.
- Proton identified 1917–1920, named 1920; 1836 electron masses — Wikipedia, Proton. Chadwick 1891–1974, Cavendish, Nature letter February 1932, Po–Be radiation on paraffin; Nobel 1935 — Wikipedia, nobelprize.org.
- "Isotope": Margaret Todd to Soddy, 1913, Greek "same place" — Wikipedia, Isotope.
- Nuclear force attractive ~0.7–2.5 fm, repulsive core < 0.7 fm, charge independent — Wikipedia, Nuclear force.
- Deuterium about 1 in 6420 (text: "about one in 6400") — Wikipedia, Deuterium. Tritium 12.3 a, C-14 5700 a, stability — NUBASE2020 via the course data file.

## Numbers (Python, CODATA 2018)
- k e²/r² at 2.0 fm = 57.7 N (at 1 fm 231 N); a = 3.4·10²⁸ m/s²; Coulomb/gravity for two protons 1.24·10³⁶.
- Fe-56: R = 1.2 fm · 56^(1/3) = 4.59 fm; nucleus mass 9.286·10⁻²⁶ kg; ρ = 2.29·10¹⁷ kg/m³; teaspoon 1.15·10¹² kg; ρ/ρ(iron 7874) ≈ 2.9·10¹³.
- N/Z: Fe 1.15, Sn-120 1.40, Au-197 1.49, Pb-208 1.537.

## Checks
units.py check (ok), build, check_layout 360 and 1280 (OK), screenshot.py (54 captures, looked at intro, figures, builder, stages). Browser test with Playwright: all three predictions lock without feedback and reveal after their theory sections; every choice, numeric (wrong then right) and explain (model closed until text) answered; components ready; no console errors, no .katex-error, no raw $.

## Open questions
- The drawing of the nucleus in the builder and hero is a picture of counts; the builder's legend says so.
- Photo placeholder: `<!-- photo: james-chadwick -->`.

## Shared issues (not edited; for the coordinator)
1. `scripts/build.py` (unit branch, the `embedded` loop, about line 419): the data files a component reads are found with `re.findall(r'data-src="(units/[^"]+\.json)"', md_text + inquiry.json text)`, but inside inquiry.json the attribute is JSON-escaped (`data-src=\"units/…\"`), so a component placed in inquiry.json gets no embedded copy and fails from `file:` (CORS) and offline. `scripts/units.py` `ASSET_REF` has the same blind spot, so the data file is not in the content hash. Fix: also match `data-src=\\\\"` (or parse inquiry.json and search the decoded strings). Workaround in my units: an HTML comment in unit.md naming `data-src="units/fy14/data/nuclides.json"`.
2. `assets/units/fy14/units.css` / `fx/reaction.js` energy-scales chart: at 390 px the bar track is 210 px wide but the axis row is 314 px (`.fx-sc-axisrow` keeps an empty label column while the bar rows stack the label above), so the bars do not line up with the logarithmic axis on a phone (D–T ends near 10¹² instead of 3.4 · 10¹⁴). At 1280 px they match. Fix: give the axis row the same grid columns as the bar rows at narrow widths.
3. `fx/binding.js`: at 390 px the graph labels (axis numbers, nuclide labels, "fusion"/"fission") are about 8–10 px, below the 14 px rule, and the $^{56}\text{Fe}$ label touches the $B/A$ axis title.
4. `docs/fy14/writing-guide.md` says there is no `pair` field on `explain`, while the pilot unit uses it as text; I did not use it.

## Fixes after review
Content hash after the fixes: c3553fea1e86a21a (2026-11-01).
- Science, Polish:
  - The proton date now matches the source: "in experiments from 1917 to 1920".
  - The text now says "practically the same chemistry".
- Pedagogy, Polish:
  - The `pred-heavy` options are rebalanced: the correct option is "More neutrons, $N > Z$, for attraction without repulsion.", and all three are 51–63 characters.
  - Builder task 6 now ends: "Neutrons have no charge, so they cannot cancel anything; they add attraction."
  - Options in `pred-glue`, `find-error` and `check-3` are balanced, so the correct option is no longer the longest.
- Visual, Polish:
  - The inline equalities in the worked example's Given and Unit conversions are braced.
  - Notation figure: 14 and 6 moved 7 units towards the C.
  - Ranges figure:
    - The electric-force labels start at 0.4 fm, and the red bar stays full-colour to 65 % of its length.
    - The "r (fm)" label moved 6 units left, because check_layout reported it 2 px outside the figure at 1280.
- Shared: the isotope readout is a component issue (isotopes.js). It was being changed while I worked; at one point check_layout failed at 360 (`{A = Z + N = 1 + 0 = 1}`), but it passes after the committed version.
- Checks: units.py check, build, check_layout at 360 and 1280, screenshot.py and the browser run (predictions, reveals, components, KaTeX, console) all pass.
