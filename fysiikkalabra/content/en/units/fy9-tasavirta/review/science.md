VERDICT: PASS
CONTENT-HASH: fe414bd9a9a971c6
SCOPE: full (en), this change first: three new ```pysahdy boxes in unit.md, three figures (hero, mokki, piiri) now a webp under the same LaTeX labels, paragraph breaks in the tarkistus-3 model answer. The unit hash was the same at the start and the end.

## Blocking
None.

## Polish
- unit.md, first pysahdy box: the question says "the cooler", but the text, hook and figure say "cool box". Use one name.
- unit.md, third pysahdy box: "Part of the emf is used up in the internal resistance" is the Finnish "kuluu" put word for word into English, and the Battery paragraph already says the same. It is fine at this level (C). Clearer: "there is a voltage drop $R_\text{s}I$ across the internal resistance".
- teacher.md (the Finnish file says the same): "the other five problems" and "the other five of the Part II type, 95 points in total" are out of date. The set has eight tasks: s1, s2 and s4–s6 at 15 points each, s3 20, s7 16, s8 18, so 129 points in total. This is only the teacher's note and no student sees it, so it does not block.

## Checked
- The pysahdy boxes have the same physics as the Finnish ones (fi unit.md lines 101–180). Parallel branches get the source voltage, which is right with no wire or internal resistance, as the cottage model assumes. In series the same current makes $P = RI^2$ grow with $R$, which matches the theory sentence above the box. $U = E - R_\text{s}I$ for discharging matches the derivation and the charging note.
- I recomputed every number in one script with my own formulas, and all of them agree with the text. The script covered:
  - the cottage currents and hours ($0.50$, $4.0$, $4.5\,\text{A}$; $200\,\text{h}$, $22\,\text{h}$)
  - the wire fit: slope $7.07\,\Omega/\text{m}$, intercept $0.30\,\Omega$, $\rho = 0.50\,\mu\Omega\cdot\text{m}$, the mistakes $1.999$ and $0.5203$, the $22\,\%$ claim
  - every prediction and Apply option (one correct option each, every distractor wrong and its feedback right)
  - the four numeric tasks with their mistakes and solutions
  - the three checks (8.0 V; 4.58 V; 1320/530 Ω, 0.12 A, 20/8 W)
  - s1–s8: every answer, intermediate value and number in the reasonableness checks. This included the least-squares fit of s3 (4.625 V, 0.727 Ω, matching "Hyväksytään myös"), the error limits of all three s5 readings ((96±9), (100±4), (102±3) Ω) and the s6 heat and shower energies.
- The criterion points add up to each part's points in every task. The answers and points of the en tasks.json are identical to the fi set.
- Models and conditions are stated: Ohm's law at constant temperature, the filament lamp read point by point as $U/I$ (not the tangent), constant $E$ and $R_\text{s}$, extrapolation flagged as an estimate, the charging current direction, the efficiency model. Scope stays within FY6 plus FY3 $Q = cm\Delta T$ and FY1 graphing. Energy goes to internal energy, as P1 requires.
- No data presented as measured is invented: every task and the investigation carries an invented/example source note.
