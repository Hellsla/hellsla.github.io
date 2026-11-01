VERDICT: DONE

Unit fy14-confinement-concepts, "Pinches, lasers and other paths to fusion" (FY14 chapter 6, order 1). Developer report 2026-11-01.

## Files changed
- `content/en/units/fy14-confinement-concepts/unit.md`: Why question; hero; sections *Pinches* {Pinches} (Z- and theta-pinch, kinks and sausages, ZETA 1958, Scylla I 1958 and end losses), *Inertial confinement* {Inertial} (hohlraum, NIF 5 Dec 2022: 3.15 MJ from 2.05 MJ, G ≈ 1.5; eleven ignitions by mid-2026; what it does *not* mean: about 300 MJ of electricity, a few hundred shots a year), *Spherical tokamaks and stronger magnets* {Compact} (aspect ratio, START 1991, MAST-U 2020, STEP as a plan for 2040, the 20 T HTS magnet of 5 Sept 2021), *Private concepts* {Private} (CFS/SPARC, Helion–Microsoft, General Fusion, all labelled as claims; "As of November 2026, no fusion device … has produced net electricity"), Key idea, a staged Worked example (G = 1.54, fusion : electricity = 0.0105), Common misconception (G and Q are not electricity), Summary. Core theory is about 690 words.
- `inquiry.json`: 25 activities. Prediction 1 asks what a current along a plasma column does (revealed by theory-pinch). Prediction 2 asks whether NIF as a whole produced net energy (revealed by theory-inertial). Also a statistics interpret (LLNL shots; G of the record shot = 4.13), a match sort (measured result / public plan / company claim) with a pair discussion, word bank and starters, vocabulary, reflect, a numeric task (needed gain 144), a match of problems to concepts, an optional find-the-error, three checks, an argue task "which path would you fund?" with starters, and the French corner (Laser Mégajoule).
- `unit.json` (14 sources), `teacher.md`, `lessons/units/fy14-confinement-concepts/figures.py` (`hero` with no text, `pinch`, `icf`, `energy`, `aspect`).

## Checks run
- `python3 scripts/units.py figures <id>`, `python3 scripts/units.py check` (21 units ok), `python3 scripts/build.py <id>`.
- `python3 scripts/check_layout.py <id> --width 360` → OK; `--width 1280` → OK.
- `python3 scripts/screenshot.py <id>`; looked at the contact sheets, intro, hero and figures at 390 and 1280 px, every stage, the components and the teacher notes.
- Playwright on `preview/en/<id>.html` (scratchpad script, `scripts/_browser.launch`): every prediction locks without feedback and is revealed only when its reveal target (theory section on screen, or the experiment with enough rows) is reached, with the feedback of the committed option; every wrong option of every plain choice shows its own feedback and the right one is marked correct; every numeric task accepts the answer with a decimal comma and gives the feedback of each listed mistake; every explain task keeps its model answer closed until the student has written something (and, with `after`, until the experiments are done); the reflect lists both predictions; all worked-example steps open; no `.katex-error`, no unrendered `$`, no console errors. All passed. A separate check found no display formula wider than its box at 390 px with every box open.

## Numbers (Python)
- G = 3.15 / 2.05 = 1.54; 3.15 / 300 = 0.0105; laser efficiency 2.05 / 300 = 0.68 %.
- Record 7 Apr 2025: 8.6 / 2.08 = 4.13 (mistakes: 0.242, the inverse, and 6.52, the difference).
- Needed gain 300 / 2.08 = 144 (mistakes: 4.13 and 0.00693).
- Aspect ratio of ITER: 6.2 / 2.0 = 3.1.

## Facts verified (2026-11-01; sources in unit.json)
- Z-pinch, theta pinch, ZETA, Scylla I (Wikipedia). LLNL "Achieving fusion ignition" (shot list, energies, indirect drive). NIF (Wikipedia; about 300 MJ of electricity per shot, shot rate). Spherical tokamak, MAST (Wikipedia), STEP (UKAEA, WNN: West Burton, operating by 2040, >100 MW net as the aim). MIT/CFS 20 T magnet on 5 Sept 2021 (MIT Energy Initiative). SPARC (Wikipedia). Helion (Wikipedia; Microsoft agreement 2023, electricity from 2028). General Fusion (Wikipedia; 2025 staff cuts). Laser Mégajoule (Wikipedia). ITER 2024 baseline (Wikipedia).

## Open questions for the reviewers
- Company dates change quickly. They are labelled as claims and dated, and the teacher notes ask teachers to check them before the lesson.
- "About 300 MJ" of electricity per NIF shot is the commonly cited figure. LLNL gives it only roughly, so the text says "about".

## Shared issues (not edited; reported to the coordinator)
- `scripts/test_inquiry.py <id>` stops at once for FY14 units ("no lesson folder … in content/fi/"), and `check_choices.py` does not know units either. The mechanics were tested by hand with Playwright instead (see Checks run).
- `scripts/inquiry.py` `tex_name`: the UNIT regex `[A-Za-z/%]+[²³]?` does not accept "(°)", so an angle column cannot be named "θ (°)"; I used "pitch angle θ (degrees)".
- Experiment tables show a boolean measure as the raw words true/false, and a `select` parameter as its raw key (p, d, e, a) in the varied column; the `names`/`values` maps do not translate the table cell.
- When an experiment name includes its unit, the initial-state line repeats it (value + unit after a name that already ends in the unit).
- `screenshot.py` captures only step 1 of a staged worked example; the full examples were opened and captured by hand at 390 px.

## Fixes after review (2026-11-01)
- Science 1–2: the text now says "released more energy than the laser energy delivered to its target". The misconception gives LLNL's working definition of ignition (G > 1 on the target) and the physical one (alpha heating beats losses).
- The shot rate is dated: one shot about every two days in 2014, most of them not ignition attempts.
- The 2024 table row is marked as an estimate.
- Visual 1: curly quotes in find-error.
- Pedagogy: the options of review, find-error, check-1 and check-3 are rebalanced. *Pinches* now says that parallel currents attract. The pred-nif feedback names the table and the sort as evidence.
- problems-match is optional (teacher.md updated).
- The French corner uses the shared style.
- Visual: the energy bars are now at least 6 units wide; the "I around the tube" label moved up.
