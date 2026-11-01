VERDICT: DONE

Unit fy14-plasma, "Plasma: the fourth state of matter" (FY14 chapter 4, order 1). Developer report 2026-11-01.

## Files changed
- `content/en/units/fy14-plasma/unit.md`: Why question; hero; sections *What is a plasma?* {Plasma} (ionisation, 13.6 eV, Langmuir 1928, quasi-neutrality), *Plasma in nature* {Nature} (stars, lightning, northern lights over Lapland with FMI frequencies), Key idea (p = nkT, temperature vs pressure), Formula: The triple product (Lawson, nTτ_E ≥ 3 · 10²¹ keV·s/m³ near 14 keV), a staged seven-step Worked example (pressure of ITER's plasma), Common misconception (Sun's core 280 W/m³ vs fusion plasma), Summary. Core theory is about 650 words, formulas included.
- `inquiry.json`: 23 activities. Two predictions: what makes the aurora glow (revealed by theory-states) and how the pressure of ITER's plasma compares with that at the centre of the Sun (revealed by theory-pressure). Also a match sort, statistics interpret (density ratio), pair discussion with word bank and starters, a vocabulary match, reflect, a numeric Lawson task, an optional find-the-error, three checks, an argue task with starters, and the French corner (`say`).
- `unit.json`: 11 sources, checked 2026-11-01. `teacher.md`: 75-min timing, organisation, a plan for fast pairs and for running out of time, assessment, difficulties, extensions.
- `lessons/units/fy14-plasma/figures.py`: `hero` (aurora over a fell, lightning, the Sun, a cut-open tokamak; no text), `ionisation`, `pressure` (log bars). Labels 24 units.

## Checks run
- `python3 scripts/units.py figures <id>`, `python3 scripts/units.py check` (21 units ok), `python3 scripts/build.py <id>`.
- `python3 scripts/check_layout.py <id> --width 360` → OK; `--width 1280` → OK.
- `python3 scripts/screenshot.py <id>`; looked at the contact sheets, intro, hero and figures at 390 and 1280 px, every stage, the components and the teacher notes.
- Playwright on `preview/en/<id>.html` (scratchpad script, `scripts/_browser.launch`): every prediction locks without feedback and is revealed only when its reveal target (theory section on screen, or the experiment with enough rows) is reached, with the feedback of the committed option; every wrong option of every plain choice shows its own feedback and the right one is marked correct; every numeric task accepts the answer with a decimal comma and gives the feedback of each listed mistake; every explain task keeps its model answer closed until the student has written something (and, with `after`, until the experiments are done); the reflect lists both predictions; all worked-example steps open; no `.katex-error`, no unrendered `$`, no console errors. All passed. A separate check found no display formula wider than its box at 390 px with every box open.

## Numbers (Python, k = 1.380649e-23 J/K)
- p = 2nkT = 2 · 1.0e20 · k · 1.5e8 K = 4.14e5 Pa; p : p_air = 4.09.
- Sun's core 2.65e16 Pa : 4.14e5 Pa = 6.4e10 ("some 60 billion").
- 1 keV = 1.16e7 K. τ_E = 3e21 / (1.0e20 · 15) = 2.0 s (mistakes: 1.72e-7, which uses T in kelvins, and 0.5, which inverts the ratio).
- Air 2.5e25 m⁻³ : 1.0e20 = 250 000 (the interpret answer).

## Facts verified (2026-11-01; sources in unit.json)
- Sun's core: 1.57e7 K, 150 g/cm³, 2.65e16 Pa, 276.5 W/m³ (Wikipedia, Solar core).
- Lightning: about 30 000 °C, about 30 kA (Wikipedia). Aurora: 100–150 km, O 557.7 / 630.0 nm, N₂ blue/violet, keV electrons (Wikipedia, Aurora). Auroral oval about 2500 km from the pole; Kilpisjärvi–Utsjoki about 3 clear nights in 4, Helsinki about one a month (FMI).
- Langmuir named plasma in 1928. Lawson's report of 1955 was published in 1957. Wurzel & Hsu (2022) give an ignition triple product of about 2.9e21 keV·s/m³ near 14 keV. ITER density and temperature from the CIEMAT wiki and iter.org.

## Open questions for the reviewers
- The ignition triple product is rounded to 3 · 10²¹. Some textbooks use 1e21 for a slightly different (breakeven) condition, and the text says which condition it uses.
- `<!-- photo: aurora-lapland -->` is left for the photo pass.

## Shared issues (not edited; reported to the coordinator)
- `scripts/test_inquiry.py <id>` stops at once for FY14 units ("no lesson folder … in content/fi/"), and `check_choices.py` does not know units either. The mechanics were tested by hand with Playwright instead (see Checks run).
- `scripts/inquiry.py` `tex_name`: the UNIT regex `[A-Za-z/%]+[²³]?` does not accept "(°)", so an angle column cannot be named "θ (°)"; I used "pitch angle θ (degrees)".
- Experiment tables show a boolean measure as the raw words true/false, and a `select` parameter as its raw key (p, d, e, a) in the varied column; the `names`/`values` maps do not translate the table cell.
- When an experiment name includes its unit, the initial-state line repeats it (value + unit after a name that already ends in the unit).
- `screenshot.py` captures only step 1 of a staged worked example; the full examples were opened and captured by hand at 390 px.
