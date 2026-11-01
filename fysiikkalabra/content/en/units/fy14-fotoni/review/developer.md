VERDICT: DONE

Unit fy14-fotoni, "Fotoni lab visit: modern physics experiments" (FY14 chapter 9, big question "What can we measure about light and electrons ourselves?"). Developer report 2026-11-01.
Content hash at hand-over: 50ba844bc762df91 (`python3 scripts/units.py hash fy14-fotoni`).

## Files
- `content/en/units/fy14-fotoni/unit.json` — kind `lab`, minutes 150 (a lesson before and a lesson after the visit; see open questions), 15 sources checked 2026-11-01 (the Fotoni material bank, the Fotoni page, six Fotoni work instructions, Wikipedia, iter.org).
- `content/en/units/fy14-fotoni/unit.md` — Why question; hero; *Before the visit: the physics of each station* {Stations} (e/m figure); *Planning a measurement* {Planning} (variables, Δx, half range, safety); *During the visit: lab worksheet* {Worksheet} (plain headings and tables, printable); *After the visit: what the stations show* {Evidence}; Key idea (modern physics and fusion); Formula: A straight-line fit (slope, extreme lines, percentage difference); staged Worked example (h from five LEDs, fit, Δh, seven steps, fit graph); *Writing a lab report in English* {Report}; Common misconception; Summary.
- `content/en/units/fy14-fotoni/inquiry.json` — 38 activities. Think about it: hook, review choice, pair discussion with sentence starters. Predict: three committed predictions (brighter LED at the stopping voltage, stronger coil field, single photons) and an optional fourth (hotter filament), all `reveal: {"after": "theory-main"}` (the after-visit evidence section). Investigate (before/during): station physics, station match, planning and safety, safety match, pair plan with word bank and starters, the worksheet, language for observations. Theory summary (after): evidence + key idea (438 words), reflect, vocabulary match. Apply: formula + worked example, e/m numeric (complete solution, two mistakes), own-data analysis (explain with hints), optional band-spacing numeric, group task on modern physics (word bank, starters), report structure, `order` component, report discussion writing task (word bank, starters, model, criteria), misconception. Check: three choices (agreement within uncertainty, axes for e/m, reporting repeated counts), sentence starters + argue task, summary, French corner with `say`.
- `content/en/units/fy14-fotoni/teacher.md` — the three parts, lesson 1 and lesson 2 timings (75 min each), the visit (Fotoni's own programme, stations and group sizes), **printing the worksheet section**, fast pairs, running out of time, preparation, assessment criteria, difficulties, extensions.
- `lessons/units/fy14-fotoni/figures.py` — `hero` (three stations on a bench, two faceless students, no text), `em` (e/m tube along the coil axis: B ⊙ green, v blue, F red, r), `fit` (example data with the least-squares line).
- `docs/fy14/fotoni-worksheet.md` and `/mnt/project-files/fy14/fotoni-worksheet.md` — the standalone printable worksheet (same tables, safety list, useful equations in Unicode so it prints from any Markdown viewer).

## What Fotoni confirms (material bank and instructions, read 2026-11-01)
- Bank: photoelectric effect 3 stations × 1–3 students (Planck's constant from stopping voltages; 5:30 video recommended; short instruction on request); e/m 2 × 1–3; double slit 1 × 1–4 (demonstration, analysis of pre-collected data, report; 7:25 video must be watched before; the ready data file is "not for visiting groups"); Millikan qualitative 1 × 1–4; hot filament 1 × 1–4; spectra 3 × 1–5; IR/climate package (not used).
- Fotoni page: upper-secondary visits = introduction about 15 min, lab work about 60 min, research department 30–60 min; choose works in advance; bring laptops; second floor of Physicum, Kumpula.
- Photoelectric (short instruction): LEDs (only red named) on a vacuum tube, intensity control, counter-voltage with fine adjustment; steps red LED → intensity up → stopping voltage → intensity up at U_s → other LEDs; table λ, f, U, E; fit E_k,max = hf − W; intercept negative and far from the points. **No mercury lamp.**
- e/m: helium-filled tube, heated cathode, 100–300 V, coils, N = 130, R = 0.15 m, B = Nμ₀I/((5/4)^{3/2}R), two currents 1–2 A × three voltages, r 3–5 cm, graph 2U vs B²r²; do not touch the glass with the magnet.
- Double slit: photodiode for bright light; dim green lamp, photomultiplier and counter (10 s, manual) for single photons; d = 0.3556 mm, L = 49 cm; repeated counts for the spread. (The instruction's own text mentions a 700 nm result that conflicts with its 550 nm lamp; the unit uses only d, L and "the wavelength given at the station".)
- Hot filament: lamp, collimator, prism, light sensor on an arm with an angle sensor, software computes T from the electrical power; 7, 8, 9, 10 V; avoid long 10 V.
- Spectra: hand spectroscope, Vernier spectrometer, hydrogen, oxygen and water-vapour tubes, energy-saving lamp, Logger Pro.
- Millikan: atomiser, alpha source, about 500 V, microscope camera; qualitative: drops that suddenly rise or speed up.
Where a detail is not confirmed (LED colours and wavelengths, meter types, the radius-reading method), the worksheet asks students to fill in the instrument and the source of each value.

## Other facts verified
- e/m = 1.75882 · 10¹¹ C/kg (CODATA; Wikipedia *Mass-to-charge ratio*); Helmholtz field (4/5)^{3/2} μ₀nI/R (Wikipedia); Millikan and Fletcher 1909, charge in multiples of e (Wikipedia *Oil drop experiment*); Balmer lines 656.3, 486.1, 434.0, 410.2 nm (Wikipedia); tungsten melts at 3695 K (Wikipedia); ITER spectroscopic instruments cover visible to X-ray and measure impurity species and ion temperature (iter.org diagnostics); h exact 6.62607015 · 10⁻³⁴ J·s (SI 2019).

## Numbers (Python, exact constants unless the text shows rounded ones)
- Example LEDs (invented, labelled as such): 625, 590, 525, 470, 405 nm → f = 4.797, 5.081, 5.710, 6.379, 7.402 (10¹⁴ Hz), table 4.80 … 7.40; U_s 0.55, 0.69, 0.93, 1.17, 1.60 V. Least squares on the table values: k = 3.9644 · 10⁻¹⁵ V·s, b = −1.3407 V, h = 6.3516 · 10⁻³⁴ J·s; extreme lines (±0.02 V at the end points): k_max = 1.09/2.60e14 = 4.192e-15, k_min = 1.01/2.60e14 = 3.885e-15, Δh = 1.602e-19 · 0.307e-15/2 = 0.246e-34 → 0.3e-34 (rounded up); difference −4.1 % (−4.2 % with the rounded 6.351 shown).
- e/m task: (4/5)^{3/2} = 0.71554; μ₀NI = 2.4504e-4 T·m; B = 1.1689e-3 T; B²r² (r = 0.041 m) = 2.2969e-9; e/m = 1.7415e11 C/kg (−1.0 %); mistakes: diameter 0.435e11, no factor 2 0.871e11. Radii at N = 130, R = 0.15 m: 1.5 A/200 V 4.08 cm (in Fotoni's 3–5 cm range).
- Band spacing: 550e-9 · 0.49 / 0.3556e-3 = 7.579e-4 m = 0.758 mm.
- Wien: b/700 nm = 4140 K; at 3695 K λ_max = 784 nm. Photon at 550 nm = 2.25 eV.
- Counts 412, 389, 405, 398, 421: mean 405, half range 16, √405 = 20.1.

## Checks
`units.py figures` (up to date), `units.py check` (no fotoni errors), `build.py fy14-fotoni`, `check_layout` 360 OK and 1280 OK, `screenshot.py` (looked at intro, every stage, figures, components, teacher). Playwright at 390 and 1280: the four predictions lock on commit with no feedback, feedback opens only after *After the visit: what the stations show* is on screen; every plain choice shows its feedback; all six explain tasks keep the model closed until the student writes; both numerics give the mistake feedback and accept the answer; match and order components check; all worked-example steps opened; no console errors, no raw `$`/TeX, no `.katex-error`. HTML of the page balanced (checked with a parser).

## Open questions
- Length: the unit is two 75-minute lessons around the visit (`minutes: 150`), because the brief asks for before, during and after in one unit and the registry has one unit for chapter 9. If the course wants one lesson per unit, the after-visit part could become a second unit (registry change needed).
- Fotoni's photoelectric station uses LEDs. Stopping-voltage results with LEDs depend on the LED's spectral width; the unit names this only as a possible systematic error, without a direction.
- The double-slit "pre-collected data" is "not for visiting groups"; the worksheet records counts the group sees at the demonstration. The teacher should confirm with Fotoni what visitors measure.
- Photo placeholder: `<!-- photo: fotoni-photocell-station -->` in the worked example (a photo of the Fotoni photocell station would help).

## Shared issues (not edited)
1. `scripts/build.py` `FIG` regex: `<table>.*?</table>\s*<p>(<svg…` is lazy but anchored only at the first `<table>`, so when a later table is directly followed by an SVG figure, the match starts at the *first* table of the page and swallows everything between (here the whole worksheet), producing a `fig-row` that breaks the HTML (the page's `.page` closed early; the sticky nav then pulled the scroll back, failing check_layout's heading test). Fix: `<table>(?:(?!</?table>).)*</table>` (as the `<ul>` branch already does). Workaround here: a sentence between the worked-example table and its graph.
2. `templates/inquiry.js` (or lesson.js) numeric `mistakes` feedback is inserted without KaTeX typesetting: `$…$` shows raw (also in fy14-photoelectric's planck-data, e.g. "4.12"). Fix: call the typeset function on the output after setting the mistake text. Workaround here: mistake feedback written in words.
3. `scripts/inquiry.py` renders `explain.pair` as `<p class="pair"><p>…</p></p>` (nested `<p>`, invalid HTML); use a `<div class="pair">`. The criteria box links to `#exercises`, which a unit without exercises does not have.
4. Pilot `content/en/units/fy14-photoelectric` says students measure Planck's constant at Fotoni "with a real photocell and a mercury lamp" (unit.md Formula section, teacher.md, planck-data text "like the measurement at Fotoni"). Fotoni's instruction uses LEDs: change to "a photocell and LEDs of different colours" (the mercury-lamp example table can stay as an example, without "like the measurement at Fotoni").

## Fixes after review (2026-11-01)

Content hash after the fixes: 9da4587953c810e1.

### Pedagogy
1. (Blocking) `theory-main` (Evidence + Key idea) has `"fold": "Lesson 2: after visit"` and the title "After the visit: open in lesson 2". Tested in Playwright at 390 and 1280: with the fold closed and on screen, none of the four predictions opens; they open only once the fold is opened. The teacher.md text about the predictions now refers to the fold.
2. Lesson 2: `em-task` is optional; Apply is 25 minutes (15–40); the French corner is "if time allows" and listed under running out of time.
3. Printing: teacher.md makes `docs/fy14/fotoni-worksheet.md` (export to PDF) the way to print. The page section is for screen and laptops. The A4 claim is removed.
4. Lesson 1 timing (20–40 min) includes the double-slit video (7:25, required) and the photoelectric video (5:30, recommended, or as homework).
5. The e/m worksheet now has an observation table on the page and in the md file: the bar magnet; $U$ kept the same, coil current up (prediction 2); coil current kept the same, $U$ up.
6. `report-order`: the part labels are removed, so students sort by content and tense. The prompt says so, and the explanation lists the order.

### Science
1. Key idea: "A charged particle circles around a magnetic field line and slides along it. Your electron beam shows the circling part, because it moves perpendicular to the field. A tokamak bends the field lines into closed loops inside the vessel…"
2. Half range: in *Planning* it is an estimate of the spread of single readings, used as Δx of one reading and not the uncertainty of the mean. The vocabulary feedback and the check-3 feedback ("Half the range of the single counts…") say the same.
3. Misconception: the uncertainty estimates how far the true value may be. Scatter shows part of it. Systematic errors (for example the LED band) do not show as scatter, and repeating does not reduce them.
4. Oil drops (Evidence and `stations-match` feedback): "Millikan's measurements showed that the charge changes in whole steps of e".
5. `pred-photons` feedback: "a photon can free one electron". The hot-filament feedback now says lamp filaments are tungsten.

### Visual
1. `emtube()`: the ⊙ marker moved from (328, 108) to (290, 62), and the B label moved inside the bulb to its left. The top marker moved to (150, 50). The v label is clear (checked in the 390 capture).
2. Worksheet md: "the mean; Δx of one reading ≈ (largest − smallest)/2, that is, half of the range".
3. Printing: see Pedagogy 3.
4. Inline maths with `\cdot` or `\pm` is wrapped in `{…}` in unit.md and inquiry.json (including steps 1 and 7 of the worked example). The range is written as ${(6.1\ \text{to}\ 6.7) \cdot 10^{-34}\ \text{J} \cdot \text{s}}$. The percentage difference is one display line with `\dfrac`.
5. Page and md worksheet aligned: 5 position rows with a "Counts at different positions" lead, e/m observation tables, and an oil-drop research question in both. The md file was copied again to /mnt/project-files/fy14/.
6. teacher.md Fast pairs uses $2U$ against $B^2r^2$.
7. Every explain task and the three check choices have `practice` (links to #tutki, #selita, #sovella). The page no longer links to #exercises.
8. The `report-order` analysis item has no unbreakable formula; with it, the order row overflowed at 360 px.

### Checks
`units.py check` (no fotoni errors), `figures --check` up to date, `build.py fy14-fotoni`, `check_layout` 360 OK and 1280 OK, `screenshot.py` re-run (88 captures). Playwright at 390 and 1280: the fold gates the reveals; plain choices, explain models, numerics and fx components all work; no console errors, no raw TeX, no `.katex-error`.

### Shared issue (from the pedagogy review, not edited)
- `templates/inquiry.js`: the pending text "Feedback appears when you have read the theory section" misleads in a lab unit. A per-prediction `pending` text would help.
