VERDICT: DONE

Unit fy14-fusion-reactions, "Fusion reactions: from the Sun to deuterium and tritium" (FY14 chapter 3, order 2). Developer report 2026-11-01.
Content hash at hand-over: c24379ba79d6f049.

## Files
- `content/en/units/fy14-fusion-reactions/unit.md` — Why must a reactor be hotter than the Sun's centre?, hero (Sun's dense core beside a tokamak with a thin plasma ring; no text), *The proton–proton chain* {Chain} (`ppchain` figure, Q from AME2020), Key idea (Coulomb barrier ≈ 0.5 MeV at 3 fm, ³⁄₂kT ≈ 2 keV, tunnelling: Gamow 1928, Atkinson–Houtermans 1929; `barrier` figure, Coulomb curve to scale), Formula: Sharing the energy of D–T fusion (balanced reaction, momentum → 14.1 + 3.5 MeV), *Fusion in the laboratory* {Lab} (Oliphant, Harteck, Rutherford 1934; Sun vs reactor table; ITER plan values dated; neutrons leave, alphas heat), staged worked example (energy share), optional Oliphant biography, misconceptions (incl. "hotter than the Sun" is temperature only), summary.
- `inquiry.json` — 29 activities: hook, review; three predictions (tunnelling, models layout → theory-key; energy share → theory-formula; why not the pp reaction → theory-chain); 1934 Nature letter as a source with an evidence choice; `reaction` component (part reaction) with question; word bank + starters; process description (pair); theory; vocabulary; reflect; worked example; Lab theory + word bank + pair comparison "Sun vs reactor"; `reaction` energy scales + numeric (1.04·10⁷ kg of coal per kg of D–T); optional pp-chain `order`; misconceptions; optional biography; three checks (neutron's share, balancing D+D → ³He + n, the "ten times hotter" claim); transfer explain (what the neutrons do) with starters; summary; French corner.
- `unit.json`, `teacher.md`, `lessons/units/fy14-fusion-reactions/figures.py`.

## Facts verified (2026-11-01)
- Oliphant, Harteck, Rutherford, Nature 133, 413 (letter dated 9 March 1934): D+D → ³H + p and ³He + n, effects from 20 kV, too large at 100 kV, proton beams no comparable effect, "too early to draw definite conclusions" (ChemTeam reproduction); Oliphant bio — Wikipedia.
- pp chain: 26.73 MeV, ~2 % to neutrinos, ~9 Gyr per proton, Bethe & Critchfield 1938 — Wikipedia. D–T 3.5 / 14.1 MeV, Sun's core power density 276 W/m³ — Wikipedia, Nuclear fusion.
- ITER: 150 million °C, about ten times the Sun's core, plasma about a million times thinner than air (iter.org "Hotter than the sun"); plasma volume 840 m³, 500 MW planned (iter.org "The Tokamak"). Marked as plans; ITER "under construction (as of November 2026)".

## Numbers (Python, AME2020 + CODATA 2018)
- pp steps (atomic masses): 1.442 MeV (incl. annihilation), 5.493 MeV, 12.860 MeV; total 2·1.442 + 2·5.493 + 12.860 = 26.731 MeV.
- k e² = 1.440 MeV·fm; at 3 fm 0.480 MeV; touching radii 1.2(2^⅓+3^⅓) = 3.24 fm → 0.444 MeV. ³⁄₂kT at 15.7 MK = 2.03 keV (ratio 236); at 150 MK 19.4 keV. Turning point at 0.10 MeV: 14.4 fm.
- Share: m_α = 4.001506 u, m_n = 1.008665 u; with Q = 17.6 MeV: E_n = 14.06, E_α = 3.54 MeV; with Q = 17.589 MeV: 14.05 and 3.54 (teacher.md). Neutron speed 5.19·10⁷ m/s (0.173 c).
- 3.37·10¹⁴ / 3.25·10⁷ = 1.04·10⁷ kg coal. ITER plan 500 MW / 840 m³ = 0.60 MW/m³. Sun core 150 g/cm³ vs ~4·10⁻¹⁰ g/cm³ (n ≈ 10²⁰ m⁻³) → "more than a hundred billion times denser".

## Checks
units.py check, build, check_layout 360/1280 (OK), screenshot.py (64 captures), Playwright run: predictions lock and reveal at their theory sections; reaction steps, scales, order, all choices/numeric/explains work; no console errors, KaTeX errors or raw $.

## Open questions
- The reaction component shows the answer of prediction 2 (3.5 / 14.1 MeV) in its header; it is placed after the predictions, as evidence.
- The 0.5 MeV barrier is my estimate at 3 fm (stated as such); Wikipedia's Nuclear fusion article quotes about 0.1 MeV for D–T (a different convention for where the barrier is taken). Reviewers may prefer one phrasing.
- Photo placeholder: `<!-- photo: mark-oliphant -->`.

## Shared issues (not edited; for the coordinator)
1. `scripts/build.py` (unit branch, the `embedded` loop, about line 419): the data files a component reads are found with `re.findall(r'data-src="(units/[^"]+\.json)"', md_text + inquiry.json text)`, but inside inquiry.json the attribute is JSON-escaped (`data-src=\"units/…\"`), so a component placed in inquiry.json gets no embedded copy and fails from `file:` (CORS) and offline. `scripts/units.py` `ASSET_REF` has the same blind spot, so the data file is not in the content hash. Fix: also match `data-src=\\\\"` (or parse inquiry.json and search the decoded strings). Workaround in my units: an HTML comment in unit.md naming `data-src="units/fy14/data/nuclides.json"`.
2. `assets/units/fy14/units.css` / `fx/reaction.js` energy-scales chart: at 390 px the bar track is 210 px wide but the axis row is 314 px (`.fx-sc-axisrow` keeps an empty label column while the bar rows stack the label above), so the bars do not line up with the logarithmic axis on a phone (D–T ends near 10¹² instead of 3.4 · 10¹⁴). At 1280 px they match. Fix: give the axis row the same grid columns as the bar rows at narrow widths.
3. `fx/binding.js`: at 390 px the graph labels (axis numbers, nuclide labels, "fusion"/"fission") are about 8–10 px, below the 14 px rule, and the $^{56}\text{Fe}$ label touches the $B/A$ axis title.
4. `docs/fy14/writing-guide.md` says there is no `pair` field on `explain`, while the pilot unit uses it as text; I did not use it.
