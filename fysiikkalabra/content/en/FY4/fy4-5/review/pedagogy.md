VERDICT: PASS
CONTENT-HASH: 294c630836cf3089

## Blocking

## Polish
- Worked-example figure — since N moved right, its label sits right next to the label of the dashed component T_y (they nearly touch). Move the N label left (e.g. lab=(-30, 6)).

## Checked
- Delta e71366d4 (rule 5): in the worked example, N now starts at the bottom surface 20 units right of the centre, clearly beside G. In the balloon diagram, G and the buoyancy both start at the centre; they point opposite ways with different lengths, which is easy to read. N pushes down onto the top surface. lattia, rinne, lamppu, hissi and the models already had G at the centre and N at the surface, apart.
- The text was not changed. The point-of-application paragraph (lesson.md:154) still says "weight from the centre, normal force from the contact surface", which matches the figures.
- The figures are shared with fi (lessons/FY4/fy4-5/figures.py) and differ only in their translated labels, so the geometry check above holds here too.
- Scope: lesson.md changed passages (free-body-diagram intro, step 3 friction, new step 6 colours, object/point-of-action paragraph, worked-example diagram, summary), inquiry.json (sim howto, solutions, feedback, draw-it-yourself criteria and model answer, elevator prompt), the 13 figures.json entries.
- Natural English wording; terms consistent (free-body diagram / situation diagram; voimakuvio / tilannekuva); the situation-diagram vs force-diagram distinction is clear to a student; figure alt texts read well and match the redrawn figures.
- `figures.py fy4-5 --lang en --check` up to date; `check_i18n.py` 0 errors. Synced to Finnish commit 000c8ad0 (push sentence, friction wording, objects drawn as they look, check-3 details, howto checkbox name, L1-05 task and Voimakuvio line, L3-01 colours, new suunnat description); re-checked, no problems.
