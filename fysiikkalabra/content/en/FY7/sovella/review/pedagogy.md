VERDICT: PASS
CONTENT-HASH: 13bbadfdc5fe3724

## Blocking
None.

## Polish
- The intro sentence lists seven topics for five tasks (it mirrors the Finnish exactly). A student cannot map list to tasks; "Five tasks bring the module together" followed by a shorter list, or one clause per task, would read better. Not a translation fault, so optional.
- fy7-s4 figure description states the peak lies on the 2.0 um gridline, which is also the graph_read answer of part a. Same accessibility trade-off accepted in the Finnish round 2; unchanged.

## Checked
- Faithfulness: tasks.json against the reviewed Finnish, structurally (same keys, part and criterion counts, point values) and numerically (every number identical apart from decimal comma to point). No step, justification, criterion or common mistake dropped or added; the "Evaluate ..." parts and the rubric wording keep the same demand (no heading or prompt names the model or formula).
- Course terms: analysing magnet, velocity selector, effective value, critical angle, cladding/core, grating, line density, thin film are the standard English terms and used consistently between tasks, solutions and figure labels. "Slab", "pyrometer", "roller operator" fit the mill context.
- Finnish leakage: tasks.json, figures and all SVG labels are English. The only Finnish in solutions.md are the practice.py headings `### Hyväksytään myös` / `### Yleisiä virheitä`; on the built page (preview/en/FY7-sovella.html, solutions opened, 390 and 1280 px) they render as "Also accepted" / "Common mistakes", so students see no Finnish. figures.json keys are the Finnish lookup strings, values English.
- Worked solutions: diagram before equation in s1 a); fy7-s1 d) Sijoitus carries the Round 3 split (mv = ... then B), recomputed 1.3256e-20 kg m/s and 0.2069 T. Numbers in the s2-s5 solutions match answers.py.
- Captures: six figures at 390 px are legible, labels English (silicon wafer, analysing magnet, relative intensity, visible, cladding, core, air); no horizontal scroll (scrollWidth 390); 1280 px layout is a normal single column. check_layout --width 340 passes for en.
- Workload and variety are as in the passed Finnish (83 points, five tasks); the 20-minute-per-task estimate polish from the fi report applies equally.
