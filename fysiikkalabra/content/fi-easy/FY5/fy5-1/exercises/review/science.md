VERDICT: PASS
CONTENT-HASH: ef00ff8a2f8f9fa0
none

## Blocking

## Polish
- content/fi-easy/FY5/fy5-1/exercises/solutions.md:149 — L2-06 Kaava splits the last row by hand inside the bracket (`m_B r_B \\ &\qquad - m_C r_C`) — write it on one row and let the layout wrap it (same as the Finnish).

## Checked
- Hash the same at the start and the end (ef00ff8a2f8f9fa0). Judged the diff against the files on disk (the packet's diff flattens the aligned blocks; on disk they are proper `aligned` rows, identical to the Finnish).
- Every rewritten Kaava starts from the basic equation and ends in the form Sijoitus uses; algebra right in all 17 blocks.
- L2-07: $d$ and $e$ defined before the block, consistent with the task (edge 0,270 m from the hand, axis 0,030 m from the edge towards the hand); $r = 0{,}240\,\text{m}$, $M = 21{,}6\,\text{Nm}$.
- New L1-10: force perpendicular to $OP$ at $P$, so $r = OP = \sqrt{4^2+3^2} = 5$ ruutua $= 0{,}50\,\text{m}$, $M = 15\,\text{Nm}$; figure fy5-1/ruutu attached; reasonableness check (horizontal force: 0,30 m, 9,0 Nm) right. Same as the reviewed Finnish task.
- Recomputed all 17 answers in one script with my own formulas; answers.py and exercises.json (fi-easy) agree, units and 2 % tolerances fit.
- Caption marker removal changes no data; paragraph splits change no number.
