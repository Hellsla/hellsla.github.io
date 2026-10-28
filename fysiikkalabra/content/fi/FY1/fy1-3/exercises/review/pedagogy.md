VERDICT: PASS
CONTENT-HASH: f6ea8ce2311e052c

Round 2 and 3: re-check of round-1 Blocking items against the fix diffs (tolerance is relative).

## Blocking
- none. Round-1 item L2-02 (answer 10.67, solution "noin 11 mm") is resolved: relative tolerance 0.04 accepts 10,24–11,10, so 11 and 10,7 pass.

## Polish
- exercises.json fy1-3-L2-03 text — "12,4 cm" and "123 mm" are plain text while "$0{,}125\,\text{m}$" is LaTeX; write all three as LaTeX.
- solutions.md fy1-3-L1-05 Vastaus — still says "virhe-arvio" while the task and Kysytty say "epävarmuus"; use one term.
- exercises.json fy1-3-L1-05 prompt — gives the half-interval rule in the situation and then asks for it; shorten the situation.
- Earlier open items (repeated formula in Kaava lines, L3-03 duplicating L2-02) stand.

## Checked
- LaTeX conversion of numbers with units in the tasks listed in the delta; values, units and answers unchanged.
- L2-02 reasoning (each reading 9–12 mm too large, mean between) correct; L1-05 Järkevyys honest about total uncertainty.
- Finnish of changed passages correct.
- Round 3: L1-02 now writes the mittausvirhe as $x - x_\text{oikea}$ in Kysytty, Kaava and Sijoitus (no Δx), matching the lesson; wording is correct, +0,3 cm unchanged, and Δ is no longer overloaded.
- Hash unchanged at the end.
