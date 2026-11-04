VERDICT: FAIL
CONTENT-HASH: 1381e6fc2a8531a8

## Blocking
- [Major] exercises.json fy8-3-L1-08 (3-8) vs fy8-3-L2-07 (3-15) — the same computation with the same numbers: L1-08 asks the photon energy for $n = 1 \to 3$ ($12{,}1\,\text{eV}$), L2-07 b) asks it for $n = 3 \to 1$ ($12{,}1\,\text{eV}$, same Sijoitus line); L1-08 is also the same type as the existing L1-02 ($4 \to 1$); solving either gives away the other, so the bank has a duplicate and the plan's L1 variety (docs/exercise-bank/FY8.md) is not met — change L1-08 to a different transition, for example absorption $n = 2 \to 4$ (answer $2{,}55\,\text{eV}$), and update text, answer, solution and answers.py together.

## Polish
- [Minor] solutions.md fy8-3-L2-05, L2-06, L2-07 — the answers to the written parts (why the points are on a line; the student's error; which photons pass) are in Periaate, while Vastaus holds only the boxed result (open-exercises-L2-1280-7, -9, -10) — repeat the conclusion in one sentence under Vastaus.
- [Minor] exercises.json fy8-3-L2-07 — the student's quotation is set with »…» while the rest of FY8 uses ”…” — use ”…”.
- [Minor] solutions.md fy8-3-L3-04 Sijoitus — one dense paragraph of about twenty numbers (open-exercises-L3-1280-5/6) — set the trial for $m = 1, 2, 3$ as short separate lines.
- [Minor] exercises.json fy8-3-L2-06, L3-04, L3-05 data tables — the $\lambda$ header is left of the right-aligned numbers (open-exercises-L2-1280-8, L3-1280-5) — align headers with the values (template matter).

## Checked
- Opened open-exercises-1280-6, -7, -8 (L1-06, L1-07, L1-08), open-exercises-L2-1280-5 to -11 (L2-05, L2-06 with the figure fy8-3/levels-task, L2-07), open-exercises-L3-1280-4 to -8 (L3-04, L3-05).
- The figure shows $E_1$ to $E_4$ at $-8$, $-5$, $-3$, $-2\,\text{eV}$, matching the solution of L2-06; axis, units and labels legible, the figure is safe (no transition shown). Tables, LaTeX quantities, upright units, decimal commas, answer boxes and solution cards render intact, nothing clipped at 1280 px. Answers match solutions (13,6 eV; 3; 12,1 eV; 365 THz; 97,3 nm; 122 nm).
- Exercise captures exist only at 1280 px; the 360 px layout check is ok.

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 4
