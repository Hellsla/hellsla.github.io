VERDICT: PASS
CONTENT-HASH: e2a6a2d65fc2e7ac

## Blocking
- (none)

## Polish
- exercises.json:141 and solutions.md:186 fy7-1-L1-09 — "koska yksittäistä magneettinapaa ei ole" / "ettei yksittäisiä napoja ole" claims more than the lesson's "eikä yksittäistä napaa ole havaittu"; write "koska yksittäistä magneettinapaa ei ole havaittu".
- glossary.json:4708 (outside the exercise set, listed as a term of this lesson) — "kenttäviiva" is defined only for the electric field (lines start at + and end at − charges), which contradicts L1-09 statement 3 (closed magnetic loops); add a magnetic-field sentence or a separate term.

## Checked
- Round 1, full mode; only L1-09 is new (type 8, five statements, 2 true / 3 false). The rest of the set was PASS before and is unchanged (hash identical start and end).
- Statement 1 (cut magnet, warned mistake), 2 (beside the side the needle points to the S end; the stem's "Maan kenttä paljon heikompi" makes it determined), 3 (S→N inside, closed loops; the lesson's field-line figure draws the inside lines S→N, checked in figures.py:88–110), 4 (N end to Earth's magnetic S pole, the chapter's first warned mistake), 5 (lines of the total field never cross, B = B₁ + B₂): truth values and feedback all correct.
- Solution Kysytty · Periaate · Mallivastaus complete, one line per statement; answers.py comment agrees.
- No statement is identifiable by form (similar lengths, no lone hedge).
- All 15 numeric answers of the chapter recomputed in one script against answers.py and exercises.json: all within tolerance.
- Text only: no render made; L1-09 has no formula chain wider than one short inline vector sum.
