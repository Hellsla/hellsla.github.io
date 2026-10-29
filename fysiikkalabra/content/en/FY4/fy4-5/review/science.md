VERDICT: PASS
CONTENT-HASH: 6dc7154e3363a512

## Blocking
- none

## Polish
- none

## Checked
- Scope: lesson.md changed passages (free-body-diagram intro, step 3 friction, new step 6 colours, object/point-of-action paragraph, worked-example diagram, summary), inquiry.json (sim howto, solutions, feedback, draw-it-yourself criteria and model answer, elevator prompt), the 13 figures.json entries.
- Compared against the Finnish source (English version): physics unchanged and faithfully translated: friction from the body outline and direction from sliding relative to the surface, velocity blue / acceleration orange / force red, net force not a force, buoyancy/normal-force diagrams, numbers and units. No leftover point model, "as a point", pistemalli, kappalemalli or pisteenä in lesson.md, inquiry.json, solutions.md or figures.json (grep).
- `figures.py fy4-5 --lang en --check` up to date; `check_i18n.py` 0 errors. Nothing needed fixing in this pass.
