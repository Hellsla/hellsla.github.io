VERDICT: PASS
CONTENT-HASH: 1612b61416342d9f
Mode: full
Round: 2

## Blocking
(none)

## Polish
- content/fi/FY2/fy2-1/exercises/exercises.json:141 — L1-09 statement 3 feedback says "likimain eristetyn", while the task states the system is assumed to be isolated. "oletettu eristetty systeemi" would match the task.
- solutions.md L3-04 c) and exercises.json L1-07 third option: the Polish items from the earlier round 3 (a constant total presented as caused by conservation; "Ympäristö kuuluu systeemiin") are still open. Not blocking.

## Checked
- Hash 1612b61416342d9f at start and end of this round; the diff from 18b454cd1 to HEAD touches only L1-09 (exercises.json, solutions.md).
- Round-1 blocking item fixed: statement 1 feedback now says "osa pallon mekaanisesta energiasta muuttui törmäyksessä ...", the right mechanism (kinetic energy at the floor, not potential energy).
- Round-1 Polish fixed: statement 5 and its feedback now both say "pallossa, lattiassa ja ilmassa", the same as the model answer.
- "ääneksi" removed from statement 4, its feedback and Periaate; thermal energy alone is consistent across all five statements and the solution.
- Key recomputed from the model (isolated system, mechanical energy dissipated each bounce): 1 T, 2 F, 3 T, 4 F, 5 T; matches answer, true flags and Mallivastaus.
- Each false statement is wrong for the reason its feedback gives; Mallivastaus "ei lattiaa korkeammalta saatua potentiaalienergiaa" is correct with the floor as the zero level.
- Scope and notation: E_alussa = E_lopussa, E_p + E_k, no expressions; 1 m in SI notation. No number, so no answers.py line is needed.
