VERDICT: DONE

Unit fy14-binding-energy, "Mass defect and binding energy" (FY14 chapter 2, order 2). Developer report 2026-11-01.
Content hash at hand-over: 9b8e68e634f060d3.

## Files
- `content/en/units/fy14-binding-energy/unit.md` — Why (both joining and splitting release energy; worded so that it does not answer the iron prediction), hero (fusion and fission flashes, no curve, no text), Formula: Mass–energy equivalence (1 u·c² = 931.5 MeV), Key idea (mass defect, binding energy, atomic masses; `ladder` figure), *Binding energy per nucleon* {Curve}, *Fission and fusion* {Reactions} (Q = B_after − B_before; `qbars` figure; Hahn–Strassmann, Meitner–Frisch), staged worked example (He-4 binding energy from AME2020), optional Meitner biography, misconceptions, summary.
- `inquiry.json` — 23 activities: hook (hot tea is heavier by 7·10⁻¹³ kg), review; predictions (He-4 mass vs parts → theory-main; fusing two Fe-56 → theory-curve); AME2020 mass table with Δm numeric; Binding Energy Explorer (`binding`, reactions D–T, D–D, U-235) with a question; word bank + starters; pair conclusion; theory; vocabulary match; reflect; worked example; D–T Q-value numeric (17.59 MeV, complete solution, check by binding energies); optional error-spotting (proton mass with atomic mass → 27.3 MeV); misconception; optional biography; three checks; explain (why stars cannot fuse iron) with starters; summary; French corner.
- `unit.json`, `teacher.md`, `lessons/units/fy14-binding-energy/figures.py` (numbers read from nuclides.json).

## Facts verified (2026-11-01)
- AME2020 masses in assets/units/fy14/data/nuclides.json; B/A recomputed from them agrees with the file to 0.0001 MeV (H-2 1.1123, He-4 7.0739, Fe-56 8.7904, Ni-62 8.7946, U-235 7.5909).
- Einstein 1905 paper (Annalen der Physik, 21 Nov 1905); 1 kg ≈ 9.0·10¹⁶ J — Wikipedia, Mass–energy equivalence. Ni-62 8.7948 / Fe-56 8.7906 MeV, deuteron 2.2245 MeV — Wikipedia, Nuclear binding energy.
- Fission: Hahn and Strassmann 19 Dec 1938, published 6 Jan 1939; Meitner–Frisch explanation, Feb 1939, name "fission"; ~200 MeV — Wikipedia, Nuclear fission. Meitner 1878–1968, fled July 1938, Christmas 1938 with Frisch, 1944 Chemistry prize to Hahn alone, meitnerium — Wikipedia, Lise Meitner.

## Numbers (Python, AME2020 + CODATA 2018)
- He-4: Δm = 0.030377 u, B = 28.296 MeV, B/A = 7.074 MeV; 0.753 % of the free mass; with a bare proton mass 0.029280 u → 27.27 MeV (the error task).
- D–T: Δm = 0.018883 u, Q = 17.589 MeV = B(He-4) − B(D) − B(T); in joules 2.82·10⁻¹² J.
- U-235 + n → Ba-141 + Kr-92 + 3n: Q = 173.3 MeV (the figure and the explorer); B before 1783.9, after 1957.1 MeV. Fission 200/236 = 0.85 MeV per nucleon; D–T 3.52 MeV per nucleon.
- Deuteron 0.002388 u → 2.2246 MeV; tea 0.25 kg · 4186 J/(kg·K) · 60 K = 62.8 kJ → 6.99·10⁻¹³ kg.

## Checks
units.py check, build, check_layout 360/1280 (OK), screenshot.py (50 captures), Playwright run as for the other units: predictions lock and reveal after their theory sections, all tasks answered, no console errors, no KaTeX errors or raw $.

## Open questions
- The text gives "about 200 MeV" per U-235 fission and the explorer/figure 173 MeV for one split; the text and teacher notes explain the difference (later decays of the fragments etc.).
- Photo placeholder: `<!-- photo: lise-meitner -->`.

## Shared issues (not edited; for the coordinator)
1. `scripts/build.py` (unit branch, the `embedded` loop, about line 419): the data files a component reads are found with `re.findall(r'data-src="(units/[^"]+\.json)"', md_text + inquiry.json text)`, but inside inquiry.json the attribute is JSON-escaped (`data-src=\"units/…\"`), so a component placed in inquiry.json gets no embedded copy and fails from `file:` (CORS) and offline. `scripts/units.py` `ASSET_REF` has the same blind spot, so the data file is not in the content hash. Fix: also match `data-src=\\\\"` (or parse inquiry.json and search the decoded strings). Workaround in my units: an HTML comment in unit.md naming `data-src="units/fy14/data/nuclides.json"`.
2. `assets/units/fy14/units.css` / `fx/reaction.js` energy-scales chart: at 390 px the bar track is 210 px wide but the axis row is 314 px (`.fx-sc-axisrow` keeps an empty label column while the bar rows stack the label above), so the bars do not line up with the logarithmic axis on a phone (D–T ends near 10¹² instead of 3.4 · 10¹⁴). At 1280 px they match. Fix: give the axis row the same grid columns as the bar rows at narrow widths.
3. `fx/binding.js`: at 390 px the graph labels (axis numbers, nuclide labels, "fusion"/"fission") are about 8–10 px, below the 14 px rule, and the $^{56}\text{Fe}$ label touches the $B/A$ axis title.
4. `docs/fy14/writing-guide.md` says there is no `pair` field on `explain`, while the pilot unit uses it as text; I did not use it.

## Fixes after review
Content hash after the fixes: c4cb2276f3c98102 (2026-11-01).
- Science:
  - "A large $B/A$ means a tightly bound nucleus." The claims about stability and mass per nucleon are removed.
  - Meitner and Frisch: "explained it at Christmas 1938 (published February 1939)". The teacher note now says "the end of 1938".
- Pedagogy:
  - The explorer question now asks students to compare silver-107 or tin-120 ($A \approx 112$) with iron-56, testing prediction 2.
  - `explorer-findings` has a matching question, model sentence (silver-107, 8.55 MeV) and criterion.
  - `check-3`'s correct option is now a reason: "because medium nuclei are bound best".
  - The teacher extension is now a calculation of D + He-3 with AME2020 masses: Q ≈ 18.4 MeV, 3.7 MeV per nucleon.
  - `li6` was added to the explorer's reactions, so the fusion unit's tritium-breeding extension works.
- Visual, Blocking:
  - The Formula and Substitution chains are broken one term per line.
  - The explorer no longer preselects a nuclide and highlights only H-2, He-4 and Fe-56.
- Visual, Polish:
  - `${1\ \text{u} \cdot c^2 = 931.5\ \text{MeV}}$` is braced.
  - The Answer now reads $\Delta m = 0.0304\ \text{u}$, with the significant-figure reason.
  - Ladder figure: one label, "$B = 28.3\ \text{MeV}$", under "add". The drawing moved 30 units right to make room.
  - `check-2`'s 3.6·10⁻¹³ MeV distractor was replaced by 22.2 MeV, a power-of-ten error, to balance the option lengths.
- After the shared update: no text quotes the old binding.js labels or values.
- Checks: all pass, as for fy14-nucleus.
