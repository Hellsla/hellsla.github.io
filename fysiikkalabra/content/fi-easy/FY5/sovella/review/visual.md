VERDICT: PASS
CONTENT-HASH: 476e5a46d60c1b04

## Blocking

## Polish
- [Minor] solutions.md:19 (fy5-s1 b, **Sijoitus**; captures easy-390-600000Nm_882900-0, easy-1280-600000Nm_882900-0) — the full stop that closes the display sits detached at the far right of the last row, about 90 px after "= 1 012 020 Nm", at both widths: the trailing ` &` opens an extra column and the build puts the sentence punctuation after it — new with this change; the number itself reads correctly — fix in the shared build (punctuation before a trailing `&`), or let the sentence continue after the block with a word instead of a punctuation mark.
- [Minor] task-card rubric formulas (tasks.json equation / units_precision / calculation details) are centred in their box while the solution's display formulas are left-aligned — shared style, not from this change; align them the same way when the shared layout is next touched.

## Checked
- Reflow review of the diff against origin/main (solutions.md 10 formulas, tasks.json 3); the page outside the changed formulas was not re-judged (passed on main).
- Own captures of preview/fi-easy/FY5-sovella.html with ?ratkaisut=1 and every details box open, 390 and 1280 px, in /tmp/claude-0/-home-user-hellsla-github-io/ec927bcd-bc65-54ed-bfcf-2386619399a5/scratchpad/vis2-sk/: easy-{390,1280}-600000Nm_882900-0, -882_9kNm_470_9-0, -2000kg_9_81-0, -1200kNm_392_4-0 (the three formulas of "Kuinka paljon voisi lisätä"), -600000Nm_9_81-0, -421_8-0, -160000km-0 and -1, -0_028s_2_1_984-0, -k_mgx-0, -0_265kg_19_9-0, -mgrmax_mpgrp-0, -335_8-0; read on the sheets sheet-easy-390-0/1 and sheet-easy-1280-0/1, the b) block also at full size.
- Every row starts with a relation, a sign or a whole quantity; no row breaks inside a quantity; equals signs in one column; units upright, thin spaces, decimal comma intact; sentence punctuation follows the formula (except the item above).
- Measured in the same run: 15 visible display formulas per width, none wider than its box, no page overflow at 390 or 1280 px.
- Wide screen: the b) block keeps two rows and the labelled chains (v, r, k, v') keep their rows; one-relation formulas join to one row. Known, not a finding.
- Hash the same at the start and the end.

## Scores
illustrations 4 (not re-judged) · typography 4 · Finnish 4 · accessibility 4
