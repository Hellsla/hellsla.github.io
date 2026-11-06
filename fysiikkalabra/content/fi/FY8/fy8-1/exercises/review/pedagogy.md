VERDICT: PASS
CONTENT-HASH: 28d419cc967191aa

## Blocking
(none)

## Polish
- exercises.json fy8-1-L2-07 (set was PASS before, not the new task) — the stem quotes the student's intercept "-2,1 eV", so the boxed answer W = 2,14 eV is reachable as |intercept| = 2,1 eV inside the 3 % tolerance without the slope work part b) asks for — box f_0 (5,17e14 Hz) instead, which needs the slope.
- exercises.json fy8-1-L2-07 a) — the question restates the answer ("Mitä leikkauspiste kertoo ja mistä rajataajuus luetaan?"); shorten to "Mikä virhe opiskelijan päättelyssä on?".

## Checked
- New task fy8-1-L1-09 (true/false, five statements, type 8): situation first, question last as its own sentence; two true (2, 4), three false (1, 3, 5).
- Each false statement is one of the chapter's warned errors: brighter light gives enough energy (1), doubled intensity doubles E_k (3), accumulation delay (5). Each has its own feedback that names the error.
- The true statements are numerically checkable by the lesson's own tools: 3,10 - 2,50 = 0,60 eV. Intensity gives the number of electrons.
- No true/false statement is identifiable by form: lengths are similar and the hedging is the same.
- Stays within the lesson (E = hf, hf = W + E_k,max, intensity vs frequency). No de Broglie.
- The solution sets the calculation first, then 1 to 5 in order. Each line gives its reason, not only the verdict.
- Levels, counts, Finnish and units of the rest of the set not re-opened (PASS before).
Method: text only (packet, exercises.json, solutions.md, git diff of the new task); no renders were opened. Long formula chains are wrapped by scripts/mathlayout.py per CLAUDE.md, so no separate 300 px finding.
