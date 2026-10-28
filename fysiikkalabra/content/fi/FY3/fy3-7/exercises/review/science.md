VERDICT: PASS
CONTENT-HASH: 378e4d7ef17c1e99

Delta review over the audit's PASS (ed07fb32bd2bf3da): L1-05 replaced by figure task melting-curve (s from the plateau), LaTeX units elsewhere.

## Blocking
- none
## Polish
- solutions.md:49 — "333 kJ/kg, kolme merkitsevää numeroa" gives no reason, and m = 0,60 kg has two: write 3,3 · 10² kJ/kg (330 is inside the tolerance) or justify the third figure.
- solutions.md:49 says 323…343 kJ/kg is accepted, but tolerance 0,03 on 333 accepts 323,01…342,99, so both stated ends fail. The readings are exact, so this is only cosmetic.
- exercises.json:57 — "−$18\,...$": the minus sits outside the maths; put it inside $...$.
## Checked
- Recomputed: Q = 220 − 20 = 200 kJ, s = 200 kJ / 0,60 kg = 333 kJ/kg; the table value is 334; answers.py 333,3.
- Figure melting-curve: physically consistent, since 2100 · 0,60 · 16 = 20,2 kJ ≈ 20 kJ to warm the ice and 80 kJ / (4190 · 0,60) = 31,8 K after melting (code 31,9). Plateau ends on 20 kJ × 10 °C grid crossings; no part is labelled.
- Melting at constant 0 °C (pure ice, normal pressure) explained correctly; the steeper ice and gentler water slopes agree with c_ice < c_water.
