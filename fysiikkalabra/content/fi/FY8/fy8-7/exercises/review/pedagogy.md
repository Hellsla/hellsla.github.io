VERDICT: PASS
CONTENT-HASH: 550d4a2308e6dc21

## Blocking
(none)

## Polish
- exercises.json fy8-7-L1-09 stem — two unrelated settings (laser and LED at 650 nm; quantum dots A and B) are introduced before the five statements, and statements 2, 3 and 5 need neither. A student has to look up which statement refers to which setup. Fix: name the setup in each statement, or open with "Kysymys koskee laseria ja kvanttipisteitä" and keep one context.
- statement 3 ("lämmitetään riittävän kuumaksi") — the brief says only that inversion is made by pumping. That thermal equilibrium always has more atoms on the lower level is the solution's claim, not the lesson's. Reword the statement to "Populaatioinversio syntyy, kun laseraine vain lämmitetään" so that it uses what the lesson teaches.
- statements 2 and 5 are the two long, "koska ..." sentences and are both true; shorten them or add a long false one so that length is no clue.

## Checked
- New task fy8-7-L1-09 (true/false, type 8): two true (2, 5), three false (1, 3, 4). The false ones are the lesson's warned mistakes: laser light has more energetic photons (1), heating gives inversion (3), a smaller dot gives longer wavelength (4).
- Feedback for each statement names the error and does not reveal the others.
- 1,91 eV for 650 nm verified; the workload is five short judgements at level 1.
- Stays within the lesson (stimulated emission, inversion by pumping, resonator axis, dot size).
Method: text only (packet, exercises.json, solutions.md, git diff of the new task); no renders were opened. Long formula chains are wrapped by scripts/mathlayout.py per CLAUDE.md, so no separate 300 px finding.
