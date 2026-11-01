VERDICT: PASS
CONTENT-HASH: 9b8e68e634f060d3

Pedagogy review of fy14-binding-energy (2026-11-01). Page built with `python3 scripts/build.py fy14-binding-energy` and tested in Playwright at 390 px. `check_layout.py --width 360` is all OK, and there are no console errors and no raw `$`.

## Blocking
None.

## Polish
1. `inquiry.json` `explorer-text`: the text says "Test prediction 2", but the explorer's Think question never asks the student to test it. It asks for the top three $B/A$ values and for the D–T and U-235 arrows; the explorer has no Fe + Fe reaction, and nothing points to $A \approx 112$. A student can do the whole investigation without testing `pred-iron`, and then only the theory answers it.
   - The data has $^{107}\text{Ag}$ and $^{120}\text{Sn}$.
   - Add to `question`: "Then choose silver-107 or tin-120 ($A$ close to $112$) and compare its $B/A$ with iron-56: would fusing two iron nuclei climb the curve or go down it?"
   - Also add a criterion about this to `explorer-findings`.
2. `teacher.md`, Extension ideas: "find a reaction of light nuclei that releases more energy per nucleon than D–T" cannot be done here, because `reactions` limits the explorer to `dt`, `dd-he3` and `u235`, and none of them beats D–T per nucleon. Either add the reaction the extension means to `reactions` (if the data has it), or reword the extension as a calculation with the AME2020 masses of D and He-3.
3. `inquiry.json` `hook`: the hook says that energy added to the tea makes it heavier. This prepares the reasoning for `pred-mass` well without stating the answer, so it can stay. The Why line ("joining nuclei … release energy") nudges students towards "every fusion releases energy" in `pred-iron`, which is a useful trap; `back-to-predictions` resolves it.
4. `inquiry.json` `check-3`: the correct option "$^{56}\text{Fe}$, at the peak of the curve" contains the words of the question's concept. The distractors give *reasons* ("because …"). Make the correct option a reason too, for example "$^{56}\text{Fe}$, because medium nuclei are bound best".

## Shared issues
- `assets/units/fy14/fx/binding.js`: at 390 px the labels $^{4}\text{He}$, $^{56}\text{Fe}$ and "fusion" overlap points and each other near the left edge and the peak (capture `fx-1-390`). The visual reviewer should judge this.

## Checked
- Predictions:
  - `pred-mass` and `pred-iron` lock on commit with no feedback.
  - They open with `theory-main` and `theory-curve`.
  - `pred-mass` is tested by the student's own calculation of $\Delta m$ (`mass-data`).
  - Nothing earlier gives the answers: the hook, the hero, the review feedback and the prior list.
- The model answers stay closed until the student writes.
- The staged worked example (helium-4) has all seven stages.
- Theory is about 550 words.
- The checks target real misconceptions: binding energy as stored energy, $B$ against $B/A$, joules against MeV.
- Word bank and sentence starters at both writing tasks; pair work with the explorer.
- The French corner is fine.
- `teacher.md` has the timing, a plan for fast pairs and a plan for running out of time.
