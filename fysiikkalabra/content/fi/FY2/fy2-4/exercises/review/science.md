VERDICT: PASS
CONTENT-HASH: 7cbf518ecd23380a

## Blocking
(none)

## Polish
- exercises.json:256 (fy2-4-L2-08) — Row 2 uses E_o = P_o·t, which needs a steady power, and the option feedback says "tasaisella teholla", but the task does not say it (B, minor). Write "ottaa sähköverkosta tasaisesti tehon 2,5 kW".
- exercises.json:256 (fy2-4-L2-08) — η = 60 % is low for a 2,5 kW motor (typically 80–90 %), but possible for a small or old motor. Optionally use E_a = 510 kJ (85 %); the error pattern (η = E_o : E_a > 100 %) is unchanged.
- lessons/FY2/fy2-4/answers.py — unlike fy2-3, there is no comment line for L2-08 (multiple choice, no number). Add "# fy2-4-L2-08 is multiple choice: no number (η = 360 kJ : 600 kJ = 0,60)".
- solutions.md L3-05 (carried over) — "lämmöksi muuttuu" counts only the direct heat. The light also ends up as thermal energy, so write "suoraan lämmöksi".
- docs/exercise-bank/FY2.md:29–30 (carried over) — the plan still lists c·m·ΔT and chain-efficiency tasks (FY3). Update it.

## Checked
- New task L2-08, recomputed: 2,5 kW = 2500 W, 4,0 min = 240 s, E_o = 600 000 J = 600 kJ, E_h = 240 kJ, and the correct η = 360 : 600 = 0,60 = 60 %. The student's 600 : 360 = 1,67 is the inverted ratio.
- Exactly one option is correct (Rivi 4). Rows 1–3 really are correct, and their feedback is right: 1 W·s = 1 J, and conservation gives E_o = E_a + E_h. The "ei virhettä" feedback rightly uses η ≤ 100 %, in the guardrail's sense.
- Solution: η = E_a/E_o is stated symbolically, every row is checked, and the check 60 % + 40 % = 100 % ties back to Row 3. The notation (E_a, E_o, E_h, P_o) matches the lesson.
- Scope: one device's η and E = P·t only, with no work, no c·m·ΔT and no chain. "Liike-energia" for the motor output is used the same way as in L1-01, L1-07 and L2-01.
- answers.py: every numeric answer agrees with exercises.json within tolerance (L2-05 4,29 → 4,3; L3-04 3,14 → 3,1; L3-05 6,89 → 6,9). The rest of the set is unchanged since the previous PASS (f04f800b).
- The hash was 7cbf518ecd23380a at the start and at the end.
