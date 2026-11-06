VERDICT: FAIL
CONTENT-HASH: d394fe65746f5dd5

## Blocking
- exercises.json fy8-5-L1-09, state E ("aallossa on neljä solmupintaa") — the brief teaches only "vetyatomissa mitä enemmän solmuja, sitä suurempi energia" and never that the number of nodes is n - 1 (n = 5). The solution itself calls this a trap (E is not n = 4), and a level 1 task may not carry a trap the lesson did not prepare. Fix: give state E as "5s-tila" or "tila, jonka pääkvanttiluku on 5", or teach n - 1 in the lesson first. If the lesson's figure does teach n - 1, this is Polish and the verdict PASS; the brief omits figures, so I could not verify.

## Polish
- solutions.md fy8-5-L1-09 — the solution says "Tilan aallossa on yhteensä n - 1 solmua" as a fact. If the rule stays, state what a node is.
- exercises.json fy8-5-L1-09 — if state E is changed, the 3d/4s trap (letters do not change energy) stays the task's point and is prepared by the brief. Good.

## Checked
- New task fy8-5-L1-09 (ordering, type 9): five states, prompt names the quantity and the direction ("pienimmästä suurimpaan"). Energies -13,6, -3,40, -1,51, -0,850, -0,544 eV; order B, D, A, C, E verified.
- The sign trap (negative energies: the most bound state is the smallest) is covered in the solution; the 3d below 4s trap is prepared by the brief ("kirjaimet d ja p eivät muuta energiaa").
- Level 1 otherwise fits: one step per state, no new formula.
Method: text only (packet, exercises.json, solutions.md, git diff of the new task); no renders were opened. Long formula chains are wrapped by scripts/mathlayout.py per CLAUDE.md, so no separate 300 px finding.
