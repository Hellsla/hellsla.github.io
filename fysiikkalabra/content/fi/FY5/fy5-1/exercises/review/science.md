VERDICT: PASS
CONTENT-HASH: 93d3c3e0471d2a02
none

## Blocking

## Polish
- content/fi/FY5/fy5-1/exercises/solutions.md:149 — L2-06 Kaava still splits the last row by hand inside the bracket (`m_B r_B \\ &\qquad - m_C r_C`) — write it on one row and let the layout wrap it (carried over from the previous round, not part of this diff).

## Checked
- Hash the same at the start and the end (93d3c3e0471d2a02). Judged only the diff: L2-07 Kaava now defines $d$ (mitattu pituus) and $e$ (matka reunasta akselille) before the aligned block.
- The definitions match the Annettu line and the task text: $d = 0{,}270\,\text{m}$ from the outer edge to the hand, $e = 0{,}030\,\text{m}$ from the edge to the axis towards the hand, so $r = d - e$ is right (the edge lies beyond the axis).
- Block $r = d - e$, $M = Fr$, $M = F(d-e)$ is symbolic before Sijoitus, which substitutes the same symbols.
- Recomputed in one script with my own formulas: $r = 0{,}240\,\text{m}$, $M = 21{,}6\,\text{Nm}$; answers.py and exercises.json agree (21.6 Nm, tolerance 2 %). Re-ran all 17 numeric answers: all agree.
- The previous round's finding is fixed; nothing else in the set changed.
