VERDICT: PASS
CONTENT-HASH: c0821c73c198f4f9

## Blocking
(none)

## Polish
- L2-07 (feedback and solution) — "$Q > 0$" is used without saying that Q is the energy released; same as the Finnish, so left as is.
- L3-05 solutions.md — the Reasonableness line compares with the lambda decay (37.8 MeV, L2-02); mirrors fi, fine.

## Checked
- New exercises L1-06..08, L2-05..07, L3-04..05: ids, level, kind, answers (1; 5; 3; 0.797 MeV; 218.5 MeV), units, tolerances (0.02; 0.005 for L3-05), correct flags and choice order match fi; a script diff of all non-text fields of exercises.json against fi found none.
- All numbers in texts, data tables (0.662, 1.173, 1.332, 1.461, 2.615; 139.570, 938.272, 1115.683, 497.611) and LaTeX equal fi, decimal point used throughout.
- Recomputed: L1-08 charge +1 e; L2-05 rows 1,3,5,6,7 are hadrons = 5; L2-06 reactions 3 (L), 5 (q), 7 (B) forbidden = 3; L3-04 (2.615-1.022)/2 = 0.7965 = 0.797 MeV, annihilation photons 0.511 MeV; L3-05 497.611-279.140 = 218.471 MeV.
- Solutions prose for the 8 new tasks follows the fi steps and numbers; no Finnish left in en.
- Fixed wording: L3-05 text "decayed at the V places" -> "decayed at the tips of the V" (matches the solution).
- check_i18n.py en: 0 errors.
