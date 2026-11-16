VERDICT: PASS
CONTENT-HASH: 22126cca58c08cf9
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- C `sovella/tasks.json` c and d: "teho muuttuu sisäenergiaksi" is loose (energy changes form, power is its rate); it was as loose before the change. For science: consider "Kuinka suurella teholla sähköenergiaa muuttuu jatkojohdossa sisäenergiaksi?" at a later edit.

## Checked
- Hunks: solutions.md d) Periaate (lähtökitka eli täysin kehittynyt lepokitka), c) Kysytty (johdon sisäenergiaksi muuttuva teho); tasks.json criterion of d and the questions c and d of Jatkojohto kelalla. Grammar and terms correct; the model answer's "suurin mahdollinen lepokitka" stays consistent with the new term.
- Captures opened: `fy9-harjoituskoe-stage-exercises-390-13.png`, `-390-16.png`, `-390-25.png`, `-390-28.png`, `-1280-10.png`, `-1280-19.png`: inline formulas whole at 390 px, the longer question d wraps in two lines beside its points, nothing clipped.
- The first `screenshot.py --if-stale` run failed once with a UnicodeDecodeError (a preview being rebuilt at the same time); the rerun wrote 179 captures for this hash.
- The changed places were found in the built `fi` page by their position in each stage; the contact sheets were not used for triage. No figure and no added task in this unit's diff; the rest stands under the previous PASS.
