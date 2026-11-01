VERDICT: DONE

Unit fy14-classical-limits, "When classical physics ran out of answers" (FY14 chapter 1, order 1). Developer report 2026-11-01.
Content hash at hand-over: see `python3 scripts/units.py hash fy14-classical-limits`.

## Files
- `content/en/units/fy14-classical-limits/unit.json` — chapter 1, order 1, 12 sources checked 2026-11-01.
- `content/en/units/fy14-classical-limits/unit.md` — Why question; hero; sections *Reading the curves* {Curves} (investigation, figure `curves`), *Light is an electromagnetic wave* {Waves} (review, figure `spectrum`), Key idea, *The ultraviolet catastrophe* {Catastrophe} (figure `catastrophe`), Formula: Wien's law and Planck's energy packets, staged Worked example (7 stages), Common misconception, Summary. An HTML comment names `data-src="units/fy14/data/timeline.json"` so that build.py embeds the timeline data and the content hash covers it (see Shared issues 1).
- `content/en/units/fy14-classical-limits/inquiry.json` — 26 activities: hook (Kelvin's two clouds, 27 April 1900), pair talk, EM-spectrum review (`order`); two committed predictions (peak shift → revealed by the Key idea section, after the *Curves* evidence; the classical sharing idea, `layout: models` → revealed by the *Catastrophe* section); peak-table investigation (`interpret`, source model) with a numeric task (blue star, 290 nm, one mistake feedback); graph description (explain, word bank, starters); theory; reflect; worked example; thermal-camera numeric (308 K, three mistakes); optional find-error (°C in Wien's law); misconception; the **timeline** component (era `modern-physics`, its biographies) with a six-event `order` task and the pair biography task (explain, word bank, starters); three checks; explanation with starters; summary; French corner with `say`.
- `content/en/units/fy14-classical-limits/teacher.md` — 75-minute timing, fast pairs / short of time, organisation and preparation, assessment, difficulties, extensions.
- `lessons/units/fy14-classical-limits/figures.py` — `hero` (classical temple under two dark clouds, glowing furnace; no text, no people), `spectrum` (log-scale EM spectrum with the visible band enlarged), `curves` (Planck's law at 4000, 5000, 6000 K, model values, peaks marked), `catastrophe` (Planck vs Rayleigh–Jeans at 5000 K).

## Checks run
- `units.py figures` (up to date), `units.py check` (no error for this unit; other threads' units show their own errors), `build.py fy14-classical-limits`.
- `check_layout.py --width 1280` OK. `--width 360`: one line, the timeline's year strip (Shared issues 2); everything else OK.
- `screenshot.py` captures inspected (hero, figures at 390 and 1280, timeline, components, stages); fixed label overlaps in `spectrum` and `curves`, the sun/smoke clash in the hero, two too-wide formulas.
- Playwright (`_browser.launch`), every task answered once: both predictions lock without feedback after commit and reveal when their theory section has been on screen; numeric tasks accept the answer; every explain keeps its model closed until text is written; `order` components check; no console errors, no `.katex-error`, no raw `$` with every box open.

## Facts verified (WebFetch, 2026-11-01)
- Kelvin's lecture "Nineteenth-Century Clouds over the Dynamical Theory of Heat and Light", Royal Institution, 27 April 1900; the clouds (aether/Michelson–Morley; breakdown of equipartition); the "nothing new to be discovered" quote is misattributed (teacher extension) — Wikipedia *Lord Kelvin*.
- Maxwell's theory 1864; Hertz's experiments 1886–1889 — Wikipedia *Heinrich Hertz*.
- Black body term Kirchhoff 1860; filament ≈ 2700 K — *Black-body radiation*. Wien 1893, b = 2.897771955e-3 m·K, Sun peak ≈ 500 nm, skin ≈ 10 µm — *Wien's displacement law*.
- Rayleigh June 1900, complete derivations by Rayleigh and Jeans 1905, agreement at long wavelengths — *Rayleigh–Jeans law*. Ehrenfest named the ultraviolet catastrophe in 1911 — *Ultraviolet catastrophe*.
- Planck's law presented 19 October 1900, quantum derivation 14 December 1900, "an act of despair" — *Max Planck*, *Planck's law*; Rubens and Kurlbaum's long-wavelength measurements at the PTR in Berlin, 7 October 1900 — *Heinrich Rubens*.
- Sun effective temperature 5777 K (text: "about 5800 K") — *Sun*. h, k_B exact (SI 2019) — *2019 revision of the SI*. Fotoni station on filament / black-body radiation — helsinki.fi material bank.

## Numbers (Python, exact h, c, k_B)
- Wien: λmax = b/T: 2000 K 1449 nm, 3000 K 966 nm, 4000 K 724 nm, 5000 K 580 nm, 6000 K 483 nm (also found numerically from Planck's law), 10 000 K 289.8 nm; 5772 K 502 nm; 300 K 9.66 µm; 9.4 µm → 308.3 K (35 °C); 400 °C = 673 K → 4.31 µm.
- Worked example (rounded constants as printed): λmax = 2.898e-3/2700 = 1.073e-6 m; hc = 1.9865e-25 J·m; E = 1.851e-19 J = 1.155 eV.
- Figures: Planck's law relative to the 6000 K peak (5000 K peak 0.40, 4000 K 0.13); Rayleigh–Jeans/Planck at 5000 K drawn until it leaves the graph.

## Open questions
- `fy14-photoelectric` (not edited) says Planck "on 14 December 1900 … presented a new law"; strictly, the law was presented on 19 October and the quantum derivation on 14 December 1900. This unit gives both dates; the photoelectric text is not wrong enough to contradict, but its reviewer may want to align it.
- The peak table is labelled "model values" (Planck's law), not raw measurements.

## Shared issues
1. `scripts/build.py` (around line 420) embeds component data only for `data-src="units/…json"` found literally in unit.md or inquiry.json; inside inquiry.json the quotes are JSON-escaped (`data-src=\"…\"`), so a component placed in an inquiry activity is not embedded and fails with "Failed to fetch" from file: and in screenshots. Likewise `units.py` `ASSET_REF` does not see it, so the data file is missing from the content hash. Fix: match `data-src=\\?"(units/[^"\\]+)` in both. Workaround here: an HTML comment in unit.md naming the data file.
2. `assets/units/fy14/units.css` `.fx-tl-strip svg{min-width:600px}` makes the year strip scroll inside its box at 360 px (by design), but `check_layout.py` reports it as "svg 265 px" overflow. Either let `check_layout.py` skip SVGs inside an `overflow-x:auto` container, or drop the min-width below about 480 px.
3. `assets/units/fy14/data/timeline.json` `bohr-model-1913`: `"place": "Manchester"`. Bohr developed and published the 1913 papers after returning to Copenhagen (Privatdocent at the University of Copenhagen from autumn 1912; Wikipedia *Niels Bohr*). Proposed: `"country": "Denmark", "place": "Copenhagen"`, text "who had worked in Rutherford's laboratory in 1912".
4. `templates/inquiry.js` (section 1): a prediction tied to a theory section is revealed as soon as any pixel of that section has intersected the viewport, even before the student commits (e.g. on first load while the Predict box is closed and the next stage is short). Then the feedback appears at once on commit. Proposed: count the section only after the prediction is committed, or use a threshold (e.g. 40 % of the section, or its first paragraph, visible). Workaround here: every theory reveal points at the explanation section that follows the evidence (Key idea, Catastrophe, Bohr, Sun), not at the evidence section right after the Predict box.
5. The timeline's `intro` paragraph (`.fx-prompt`) has no max-width, so a long intro exceeds the 44 rem line length at 1280 px; this unit gives the intro in its own text instead.
