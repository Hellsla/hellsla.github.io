VERDICT: PASS
CONTENT-HASH: 702b7c7a415dfe04

## Blocking

## Polish
- exercises/solutions.md:126 (L3-03 Järkevyys) — "kahdella numerolla pienin sopiva massa 1,5 kg": the computed minimum is 1,511 kg, so 1,5 kg is slightly below it (lasts about 5,96 h). Say "noin 1,5 kg (laskettu vähimmäismassa 1,51 kg)" instead of calling 1,5 kg the smallest sufficient mass.
- exercises/solutions.md L3-02 Periaate — "Koska 251 400 J > 167 000 J … loppulämpötila on yli 0 °C" is right here; for consistency with the lesson's guardrail wording, the closing check could also mention that equality would give exactly 0 °C.

## Checked
- All 12 answers recomputed in one script with my own formulas: 4,48 MJ; 452 kJ; 26,9 W; 250,5 kJ; 14,0 kW; 1,617 kg; 648,8 kJ; 0,857 kg/s; 91,1 g; 25,95 K; 8,057 °C; 1,511 kg — all match answers.py and exercises.json; tolerance 0,02 admits the rounded answers.
- L3-02 checks "does all ice melt" first (251 400 J > 167 000 J) and the energy balance 183 880 J both sides.
- L3-03 assumptions stated in the task (drinks cool at once, ice warms then melts, wall power at 0 °C inside); energy terms 486 000 J + 50 280 J over 355 000 J/kg right.
- L1-03 uses the given 2,0 °C inside (ΔT = 28 K); L2-01 states "vain jäätä"; Q = cmΔT used only without phase change, as each Periaate says.
- Magnitude checks real (coolant tens of kW, glycol needs ~20 % more flow than water, sauna stones fall 26 K, heating alone 3,4 K).
- Solutions symbolic first; notation (P = UAΔT, P = c(m/t)ΔT, Q = sm, Q = rm) matches the lesson brief; melting described with the guardrail wording; scope within FY3.
