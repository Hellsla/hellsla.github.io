VERDICT: PASS
CONTENT-HASH: 053a725bd0d21a9e

## Blocking
- none

## Polish
- none

## Checked
- Scope: solutions.md (free-body-diagram lines of the solutions: "as a rectangle", no point model; every figure line).
- Compared against the Finnish source (plain Finnish version): physics unchanged and faithfully translated: friction from the body outline and direction from sliding relative to the surface, velocity blue / acceleration orange / force red, net force not a force, buoyancy/normal-force diagrams, numbers and units. No leftover point model, "as a point", pistemalli, kappalemalli or pisteenä in lesson.md, inquiry.json, solutions.md or figures.json (grep).
- `figures.py fy4-5 --lang fi-easy --check` up to date; `check_i18n.py` 0 errors. Synced to Finnish commit 000c8ad0 (push sentence, friction wording, objects drawn as they look, check-3 details, howto checkbox name, L1-05 task and Voimakuvio line, L3-01 colours, new suunnat description); re-checked, no problems.
