VERDICT: PASS
CONTENT-HASH: 2ab8e54bc5beb6bd
SCOPE: delta: en tasks fy9-aallot-s7 (fy5-12/ruudukko-tehtava) and s8 (fy5-13/kuvio-tehtava) in sovella/tasks.json and solutions.md, and the changed intro (git diff 49ba8f9 HEAD); fidelity to fi; s1-s6 not re-judged. Language: en.

## Blocking
(none)

## Polish
- s7 c: the task ignores the loudness difference from unequal distances, yet the model answer adds "not completely silent because the farther loudspeaker is heard slightly more weakly". Physically right; "in practice" would reconcile it with the stated simplification.

## Checked
- Recomputed in one script: s7 s1 = 12*0.50 = 6.0 m, d = 2.5 m, s2 = sqrt(42.25) = 6.5 m, ds = 0.50 m; lambda = 343.4/343 = 1.0012 m; ds/lambda = 0.50, destructive for in-phase sources; next maximum ds = lambda gives f = 686.8 Hz (answer 687, 690 inside 2 %). s8 lambda = 2*1.20/4 = 0.600 m; v = 30 m/s; f3 = 3*30/2.40 = 37.5 Hz; f1 = 12.5 Hz, f2 = 25 Hz, 20 Hz gives 1.6 loops (lambda 1.5 m), not a natural frequency.
- Figure source (lessons/FY5/fy5-12, fy5-13 figures.py): S2 five squares above S1, P twelve squares right of S1, square 0.50 m; string 1.20 m in four loops, five nodes. Readings in the solutions match.
- Physics: interference conditions for in-phase sources; wave speed on a string set by tension and mass per unit length, unchanged when f changes; nodes at both ends, f_n = n v/(2L). Scope FY5. Significant figures justified (exact counts, 0.50 m, 343 Hz).
- Assessment: criteria sum to part points (s7 4+2+3+3, s8 3+3+4+3); common mistakes are real errors; Hyväksytään myös covers phase wording and ratio routes.
- Fidelity to fi: ids, figures, points, criteria, answers and tolerances identical; every number in s7/s8 text, criteria and solutions matches fi.
- Intro: "Eight problems", matches.
- Hash 2ab8e54bc5beb6bd (units.py hash --lang en) at start and end.
