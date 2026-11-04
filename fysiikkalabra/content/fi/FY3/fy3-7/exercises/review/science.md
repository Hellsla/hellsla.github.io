VERDICT: FAIL
CONTENT-HASH: b26bfec407966e18

## Blocking
- solutions.md:238 (L3-05 Järkevyys) — **A**: "koska tiivistyminen sitoo paljon energiaa" gives the wrong direction. Condensation releases energy (guardrail "Freezing and condensation release energy"), and the same line goes on to say "luovuttaa tiivistyessään". In a task about why steam burns, this leaves exactly the wrong picture. — Replace it with "koska höyry luovuttaa tiivistyessään paljon energiaa (r on suuri)".

## Polish
- exercises.json:62 (L1-06, feedback of the correct option) — "hiukkasten välisten sidosten muuttamiseen" can be read as bonds breaking. — Use the guardrail wording "hiukkasten keskinäisten vuorovaikutusten muuttamiseen", as in the option text and the solution.
- solutions.md:167 (L2-06 Periaate) — "pysyy vakiona 100 °C:ssa" holds only at normal pressure, and the lesson stresses that the boiling point depends on pressure (**B**, minor). — Write "pysyy kiehumispisteessä, normaalipaineessa noin 100 °C:ssa".
- exercises.json:147 (L2-05) — anyone who reads the plateau straight from the rows (20 s → 150 s) gets 312 kJ/kg, −6,6 %, which is rejected. Extrapolating both ends is the hidden step. — Add the hint "arvioi, milloin lämpötila tarkalleen saavuttaa 0 °C ja milloin se alkaa nousta", or widen the tolerance.
- exercises.json:282 (L3-04) — the plateau taken from the table rows (4 → 30 min) gives 18,7 kJ, just outside ±6 % of 20 kJ. — Widen the tolerance to 0,08, or ask for the extrapolated start and end in the task, as the solution does.
- exercises.json:215 (L2-07) — part a) is a single subtraction from a table (level 1), and the plan asked for reading a phase diagram (figure). L2-06 b) repeats L2-01 (P t = r m on a hotplate). — Consider a phase-diagram figure, or a pressure that needs interpolation (for example 60 kPa), to bring it up to level 2.

## Checked
- I recomputed all 18 answers in one script. They agree with answers.py and exercises.json.
- L2-05: the table matches the model (ice reaches 0 °C at 17,5 s, melting lasts 139,2 s and ends at 156,7 s, then 1,9 °C at 160 s and 13,4 °C at 180 s). s = 334 kJ/kg.
- L2-07: the boiling points match steam tables (60,1 / 69,1 / 81,3 / 90,0 / 100,0 °C), Δ = 18,7 K, and the explanation in b) is right.
- L3-04: P = 11,98 W, plateau 3,24 → 30,89 min, Q = 19,9 kJ and s ≈ 199 kJ/kg. This is realistic for stearic acid (melting point ≈ 69 °C, about 200 kJ/kg), and the implied c of the solid, about 1,9 kJ/(kg·K), is plausible. The plateau is explained correctly (released energy = heat lost).
- L3-05: m_h = 23,5 g, m_v = 0,386 kg (16×), 94 % of the energy from condensation. The burn argument is right.
- L1-06 and L1-07 MC: exactly one correct option each, with sound distractor feedback. L1-08: 0,602 kg.
- L2-06: the error is identified correctly (power changes the evaporation rate, not the temperature), and m = 0,40 kg.
- Q = sm / Q = rm are used only at constant temperature, and Q = cmΔT between phase changes.
- Notation (s, r, c, P t, Δm) matches the lesson.
- L3-04 and L3-05 render at 1280 px without overflow.
