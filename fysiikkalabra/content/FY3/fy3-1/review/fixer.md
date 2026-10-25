VERDICT: DONE

Human-ordered change (not a reviewer finding): g is always written in m/s², never N/kg.

1. lesson.md: g paragraph rewritten (g = same quantity as FY1 free-fall acceleration; G = mg in newtons when m in kg and g in m/s², 1 N = 1 kg·m/s², FY4; weight is a measure of the interaction, not the cause of any motion); table header "g pinnalla (m/s²)"; worked example, bathroom-scale sentence and summary bullets converted.
2. exercises.json, exit-ticket.json: unit in texts converted; numbers and answers unchanged (5/4/3).
3. solutions.md: all given/substitution lines converted; numbers unchanged.
4. sim.js: header comment ("g is written in m/s² (project rule)"), BODIES comment, readout text; behaviour unchanged.
5. tests/sims/fy3-1.json: expected readout strings and note updated, no assertion loosened.
6. sim-spec.md, meta.json, glossary.json: no N/kg present, unchanged.

Checks: grep N/kg in fy3-1 (excluding old review reports), glossary.json, tests/sims/fy3-1.json is empty; build --all OK; check_latex OK; test_sims fy3-1 PASS.
Files changed: lesson.md, exercises.json, solutions.md, exit-ticket.json, sim.js, tests/sims/fy3-1.json, review/fixer.md.
New hash: 307c0dfc144588a5

All reviewers must run again.
