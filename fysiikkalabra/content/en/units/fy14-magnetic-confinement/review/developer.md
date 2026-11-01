VERDICT: DONE

Unit fy14-magnetic-confinement, "Charged particles and magnetic confinement" (FY14 chapter 4, order 2). Developer report 2026-11-01. The old throwaway scaffold was replaced completely.

## Files changed
- `content/en/units/fy14-magnetic-confinement/unit.md`: Why question; hero; sections *The magnetic force on a moving charge* {Lorentz}, Formula: Radius and period of the orbit, *Along the field: helices and magnetic mirrors* {Mirror} (pitch angle, sin²θ ≥ B₀/B_max, loss cone, radiation belts), *Why a ring, and why it is still hard* {Torus} (drifts in a curved, uneven field), *One particle is not a plasma* {Collective} (collisions, turbulence, instabilities, ZETA), a staged Worked example (deuteron in 5.0 T), Common misconception, Summary. Core theory is about 610 words.
- `inquiry.json`: 25 activities. A sim activity on `fy14/magnetic` with howto, model and calc. Prediction 1 asks how the circle changes with B (revealed by exp-field, min 3). Prediction 2 asks which particles a mirror holds (revealed by exp-mirror, min 3). Experiments: exp-field (proton, 2.0 · 10⁶ m/s, vary B; measures r in mm and T in ns), exp-mirror (along view, vary the pitch angle; measures trapped), and an optional exp-particles (vary the particle; question on m/q). Also a conclusion explain (after both experiments) with starters, an `order` component, theory, vocabulary, reflect, a numeric task (3.5 MeV alpha in 5.3 T → 5.08 cm), three checks, an argue task with starters, and the French corner.
- `unit.json` (sim fy14/magnetic, 8 sources), `teacher.md`, `lessons/units/fy14-magnetic-confinement/figures.py` (`hero` with no text, `lorentz`, `mirror`, `torus`).

## Checks run
- `python3 scripts/units.py figures <id>`, `python3 scripts/units.py check` (21 units ok), `python3 scripts/build.py <id>`.
- `python3 scripts/check_layout.py <id> --width 360` → OK; `--width 1280` → OK.
- `python3 scripts/screenshot.py <id>`; looked at the contact sheets, intro, hero and figures at 390 and 1280 px, every stage, the components and the teacher notes.
- Playwright on `preview/en/<id>.html` (scratchpad script, `scripts/_browser.launch`): every prediction locks without feedback and is revealed only when its reveal target (theory section on screen, or the experiment with enough rows) is reached, with the feedback of the committed option; every wrong option of every plain choice shows its own feedback and the right one is marked correct; every numeric task accepts the answer with a decimal comma and gives the feedback of each listed mistake; every explain task keeps its model answer closed until the student has written something (and, with `after`, until the experiments are done); the reflect lists both predictions; all worked-example steps open; no `.katex-error`, no unrendered `$`, no console errors. All passed. A separate check found no display formula wider than its box at 390 px with every box open.
- Experiments run in the browser: exp-field rows at B = 1, 2, 3 T gave r = 20.9, 10.4, 6.96 mm and T = 65.6, 32.8, 21.9 ns, matching r = mv/(|q|B). exp-mirror at 60°, 80° and 90° gave trapped = true (loss cone 30°). exp-particles gave p 20.9 mm, d 41.7 mm, e 0.0114 mm at 1 T.

## Numbers (Python, CODATA 2022 masses)
- Deuteron, 1.0e6 m/s, 5.0 T: r = 4.17e-3 m, T = 2.62e-8 s (about 38 million turns per second).
- Alpha, 3.5 MeV: v = 1.30e7 m/s, r = 5.08 cm in 5.3 T (mistakes: 10.2 cm, which uses charge e, and 0.0508, which is in metres). Energy ratio alpha : 10 keV deuteron = 335 ("about 340").
- Proton, 2e6 m/s, 1 T: r = 20.9 mm, T = 65.6 ns (the exp-field check). Mirror ratio 4 gives a loss cone of 30°.

## Facts verified (2026-11-01)
- Lorentz force, gyroradius and magnetic mirror (Wikipedia); radiation belts as a natural mirror. ZETA 1958 and the kink instability (Wikipedia, Z-pinch). Drifts in a purely toroidal field (Wikipedia, Tokamak). ITER 5.3 T (US ITER fact sheet), plasma size (CIEMAT wiki).

## Open questions for the reviewers
- The sim's experiment column for the particle shows the raw keys p, d, e, a (shared issue below). The question text names them.

## Shared issues (not edited; reported to the coordinator)
- `scripts/test_inquiry.py <id>` stops at once for FY14 units ("no lesson folder … in content/fi/"), and `check_choices.py` does not know units either. The mechanics were tested by hand with Playwright instead (see Checks run).
- `scripts/inquiry.py` `tex_name`: the UNIT regex `[A-Za-z/%]+[²³]?` does not accept "(°)", so an angle column cannot be named "θ (°)"; I used "pitch angle θ (degrees)".
- Experiment tables show a boolean measure as the raw words true/false, and a `select` parameter as its raw key (p, d, e, a) in the varied column; the `names`/`values` maps do not translate the table cell.
- When an experiment name includes its unit, the initial-state line repeats it (value + unit after a name that already ends in the unit).
- `screenshot.py` captures only step 1 of a staged worked example; the full examples were opened and captured by hand at 390 px.
