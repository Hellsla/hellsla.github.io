VERDICT: DONE

Round 1 (draft). 8 new exercises added at the end of their levels: L1-06, L1-07 (multiple choice), L1-08, L2-05, L2-06, L2-07 (data tables), L3-04 (data, linear range), L3-05 (slope uncertainty). The 12 existing exercises, ids, answers and solution content are unchanged.

- exercises.json: new tasks with `kind`; `choices` on L1-06/07; `data` on L2-05/06/07 and L3-04.
- solutions.md: 8 new blocks; three existing Järkevyys lines (L1-02, L1-03, L1-04) only had plain-text quantities turned into LaTeX for the lint.
- answers.py: fit() least-squares helper; answers for the new numeric tasks computed from the table data.

lint_lesson.py: 0 errors (warnings: three new solutions over 220 words, older inquiry.json plain units). check_solutions.py: ok.
