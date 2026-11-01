VERDICT: DONE

Unit fy14-tokamak-stellarator, "Tokamak or stellarator?" (FY14 chapter 6, order 2). Developer report 2026-11-01.

## Files changed
- `content/en/units/fy14-tokamak-stellarator/unit.md`: Why question; hero; sections *Twisting the field lines* {Twist} (why a purely toroidal field fails; poloidal + toroidal = helical), Formula: The toroidal field (B = μ₀NI/(2πR) with the `toroidal` figure), *The tokamak* {Tokamak} (Tamm and Sakharov, plasma current, central solenoid as a transformer, disruptions), *The stellarator* {Stellarator} (Spitzer 1951, 3D coils, optimisation, W7-X), *Pulsed or steady?* {Operation} (inductive limit, ITER 15 MA for 300–500 s; neutral beams, RF waves, bootstrap current; WEST 1337 s on 12 Feb 2025), Key idea, a staged Worked example (ITER's TF field at R = 6.2 m → 5.29 T), Common misconception, Summary. Core theory is about 650 words.
- `inquiry.json`: 24 activities. Prediction 1 asks whether a purely toroidal field holds a plasma (revealed by theory-twist). Prediction 2 asks whether a tokamak must always run in pulses (revealed by theory-operation). Investigate uses the `reactors` component (`{"checks": false, "start": "tokamak", "note": false}`: its checks and note would repeat the unit's own checks and argue task), with a pair discussion, word bank and starters, and a statistics interpret of long plasmas (Tore Supra 390 s, EAST 1056 s, W7-X about 480 s, WEST 1337 s, ITER plan 300–500 s; ratio 3.43). Also theory in three parts, vocabulary match, reflect, a numeric task (inner-edge field 7.81 T), an optional find-the-error, three checks, the chapter's question "Which design?" as an argue task with starters, and the French corner (WEST at Cadarache).
- `unit.json` (10 sources), `teacher.md` (timing, a bagel or paper-strip demo for toroidal/poloidal, a plan for fast pairs and for running out of time, assessment, difficulties, extensions).
- `lessons/units/fy14-tokamak-stellarator/figures.py`: `hero` (a tokamak with flat D coils and a stellarator with tilted coils round a wavy plasma; no text), `toroidal` (top view to ITER scale: 18 coils, plasma 4.2–8.2 m, B = 7.8 / 5.3 / 4.0 T computed in the file).

## Checks run
- `python3 scripts/units.py figures <id>`, `python3 scripts/units.py check` (21 units ok), `python3 scripts/build.py <id>`.
- `python3 scripts/check_layout.py <id> --width 360` → OK; `--width 1280` → OK.
- `python3 scripts/screenshot.py <id>`; looked at the contact sheets, intro, hero and figures at 390 and 1280 px, every stage, the components and the teacher notes.
- Playwright on `preview/en/<id>.html` (scratchpad script, `scripts/_browser.launch`): every prediction locks without feedback and is revealed only when its reveal target (theory section on screen, or the experiment with enough rows) is reached, with the feedback of the committed option; every wrong option of every plain choice shows its own feedback and the right one is marked correct; every numeric task accepts the answer with a decimal comma and gives the feedback of each listed mistake; every explain task keeps its model answer closed until the student has written something (and, with `after`, until the experiments are done); the reflect lists both predictions; all worked-example steps open; no `.katex-error`, no unrendered `$`, no console errors. All passed. A separate check found no display formula wider than its box at 390 px with every box open.

## Numbers (Python, μ₀ = 4π · 10⁻⁷ T·m/A)
- N = 18 · 134 = 2412, I = 68 kA. B(6.2 m) = 5.29 T, B(4.2 m) = 7.81 T, B(8.2 m) = 4.00 T. Mistake values: 5.29 and 4.00 (wrong radius) and 0.434 (one coil's 134 turns).
- 1337 s / 390 s = 3.43 (mistakes: 0.292, the inverse, and 947 s, the difference). 1337 s = 22 min 17 s.
- check-2: 6.0 T · 3.0 / 6.0 = 3.0 T.

## Facts verified (2026-11-01; sources in unit.json)
- Tokamak (Wikipedia): Tamm and Sakharov, early 1950s; drifts in a toroidal field; plasma current and transformer; disruptions.
- Stellarator (Wikipedia): Spitzer 1951; no induced plasma current; "inherently steady-state".
- W7-X (Wikipedia, and the `reactors` component header): 50 non-planar + 20 planar coils; first plasma 10 Dec 2015; 8 min and 1.3 GJ in Feb 2023.
- WEST: 1337 s on 12 Feb 2025 with lower hybrid drive (CEA; Wikipedia gives 22 min 17 s); Tore Supra 6 min 30 s in Dec 2003 (Wikipedia). EAST: 1056 s on 30 Dec 2021 (Wikipedia; a 1066 s record of 20 Jan 2025 is not in the table).
- ITER: 18 TF coils of 134 turns at 68 kA, 5.3 T (US ITER fact sheet); CS drives 15 MA for 300–500 s; peak 11.8 T (iter.org magnets); R = 6.2 m, a = 2.0 m (CIEMAT wiki).

## Open questions for the reviewers
- The interpret table compares durations only. Energy (for example W7-X's 1.3 GJ) is left as an extension in teacher.md.
- The simple Ampère formula ignores the coils' finite size. It reproduces ITER's quoted 5.3 T, which the reasonableness step notes.

## Shared issues (not edited; reported to the coordinator)
- `scripts/test_inquiry.py <id>` stops at once for FY14 units ("no lesson folder … in content/fi/"), and `check_choices.py` does not know units either. The mechanics were tested by hand with Playwright instead (see Checks run).
- `scripts/inquiry.py` `tex_name`: the UNIT regex `[A-Za-z/%]+[²³]?` does not accept "(°)", so an angle column cannot be named "θ (°)"; I used "pitch angle θ (degrees)".
- Experiment tables show a boolean measure as the raw words true/false, and a `select` parameter as its raw key (p, d, e, a) in the varied column; the `names`/`values` maps do not translate the table cell.
- When an experiment name includes its unit, the initial-state line repeats it (value + unit after a name that already ends in the unit).
- `screenshot.py` captures only step 1 of a staged worked example; the full examples were opened and captured by hand at 390 px.
