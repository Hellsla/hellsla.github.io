VERDICT: PASS
CONTENT-HASH: 43de509f8395fe82

## Blocking

## Polish
- assets/sims/fy4/fy4-11/sim.js:150,209 draw the canvas label `s_\text{j}` as a literal (shared code, not a lang key), so the en simulation still shows s_j while the en text uses s_b. Move the label to a `sims.fy4-11` key in a later change to the shared sim.

## Checked
Compared en lesson.md, inquiry.json, exit-ticket.json, meta.json, figures.json and sims.fy4-11 with the Finnish: every number, formula, step, justification, hint, feedback and model answer kept; nothing added (check_i18n 0 errors).
Physics terms right (reaction/braking/stopping distance, deceleration, normal force, weight, friction, static/kinetic friction, momentum, impulse, average force F_avg as in fy4-9); en decimal point everywhere, in LaTeX and figures.
Fixed: Finnish subscripts s_j, t_j, s_p, t_p replaced by s_b, t_b, s_stop, t_stop in text, figures (figures.json) and sim readout; "head-on collision" for nokkakolari changed to "frontal collision" (a car into a wall).
check_latex, figures --check --lang en and check_layout (360 px) pass; figure labels "no belt:"/"with belt:" read clearly at 360 px, no overlap.

## Follow-up (orchestrator, 2026-10-30)
- The simulation canvas label for braking distance now comes from lang (`sims.fy4-11.lab_sj`): en shows $s_\text{b}$, matching the en readouts and lesson (the Polish item above). The Finnish and fi-easy resolved code is unchanged.
