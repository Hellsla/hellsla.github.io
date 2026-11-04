VERDICT: PASS
CONTENT-HASH: 652c6d5613fc0f41

Round 2. Round 1 had no Blocking items. This round checks the Polish fixes (`git diff HEAD~1`) and the whole 20-task set again. Mode: full.

## Blocking

## Polish
- exercises.json:217 (L2-07) — the setup (hot metal into water, equilibrium temperature) is still the same as L2-04 and the lesson example. Part a), the error analysis, is what makes it new (carried over). — Optionally use another context, for example a hot iron nail dropped into tea.

## Checked
- Round-1 Polish taken up: L2-05 b) now says "noin 1 %" (4138 compared with 4190 is 1,2 %), and Järkevyys now calls the 1 % gap measurement scatter, not losses. L3-04 now states "Huoneen lämpötila on 20 °C", which the check uses. L3-05 now explains the two significant figures (k varies by ±3 % between intervals) and puts the scatter down to the 0,1 °C readings. L2-06 now explains the check (water has the largest c of common liquids).
- L1-06 has been rewritten. Exactly one option is correct, and its text equals `answer`. The new density distractor is wrong for the reason its feedback gives (the masses are equal, and ΔT = Q/(cm) has no density in it). The reflection distractor is wrong because the task gives both the same heat. The "aine ei vaikuta" distractor is right to point to c. The solution matches the new options.
- L2-07 solution: the units are now carried through the substitution (77 J/K, 2095 J/K, 49 600 J / 2172 J/K = 22,84 °C), and the numbers are unchanged.
- L3-04 Järkevyys: "muutaman prosentin liian suuri" matches 4286 compared with 4190 (+2,3 %) and a 6 W loss (3 % of 200 W).
- I recomputed all 19 numeric answers in one script with my own formulas. All match answers.py and exercises.json within tolerance. The L3-05 k values are 0,599, 0,587, 0,612, 0,582, 0,614 and 0,590 W/K.
- The physics from round 1 still holds. Q = cmΔT is used only where the state does not change. Notation (c, m, ΔT, C = cm) is the lesson's. The levels match the plan in docs/exercise-bank/FY3.md.
- The deterministic layout checks at 360, 768 and 1280 px pass.
