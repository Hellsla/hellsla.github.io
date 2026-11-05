# Exercise types for YO-exam skills

Teacher 2026-11-05 (Kehitysideat): multiple-choice forms that train the skills of the YO exam, about one per chapter.
Every form is checked in the browser deterministically (inquiry.js 2, 2b, 2c) and its answer and model solution open
after "Olen tehnyt ratkaisun", like any written task. The schema is in README "Exercise schema"; lint_lesson.py
(`exercise_choice_errors`) enforces it, test_exercise_bank.py and test_inquiry.py test it.

| Type | Encoding | What the wrong options carry |
|---|---|---|
| 1. Perustelumonivalinta (two-stage) | `choices` + `reasons` | a reason that fits a common wrong idea, or a true statement that does not explain the answer |
| 2. Kuvaajan valinta | `choices` with `figure` per option | the typical graph confusions ($s$–$t$ vs. $v$–$t$, slope vs. value) |
| 3. Voimakuvion valinta | `choices` with `figure` per option (fbdspec diagrams) | a missing or an extra force, a "force of motion", wrong direction or length |
| 4. Virheen löytäminen | `choices`: the lines of a worked solution (one wrong) and "Laskussa ei ole virhettä" last | each line's own check |
| 5. Suuruusluokka | `choices`: values a factor 10–100 apart | the reasoning that gives each wrong magnitude |
| 6. Ennuste muutoksesta | `choices`: kasvaa / pienenee / pysyy samana (with the factor) | the dependence read the wrong way |
| 7. Yksikkö ja dimensio | `choices`: expressions or units | the unit each one really has |
| 8. Väitteet tosi/epätosi | `statements` (3–6, at least one true and one false) | each statement's reason in its feedback |
| 9. Järjestäminen | `order` (3–6 items in the correct order; `prompt` names the quantity and direction) | the solution explains the order |
| 10. Mittausdata | `data` table or a graph figure + `choices` of conclusions | conclusions the data do not support, e.g. differences within the uncertainty $\Delta x$ |

Pilot: FY1, one type per chapter (2026-11-05). Every task still has a complete written model solution (solutions.md,
Kysytty · Periaate · Mallivastaus) and the same task in every language.
