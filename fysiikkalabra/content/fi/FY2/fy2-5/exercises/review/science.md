VERDICT: FAIL
CONTENT-HASH: 2d9f3d441f3cfbfa

## Blocking
- exercises.json (all texts), solutions.md:49 — Problem: quantities are plain text ("2,0 kg", "12 t", "400 kg", "1200 kJ", "40 g", "1,8 GJ", "85 %", "48 MJ", "25 %", "120 MJ", "2,4 kg", "36 t", "35 %", "3600 s"). The teacher's rule is everything in LaTeX. — Fix: put each one in `$…$`.
- solutions.md:26 (L1-03) — Problem: the conversion is a rule ("megajoulet jaetaan tuhannella"). — Fix: substitute: $312\,000\,\text{MJ} = 312\,000 \cdot (1 : 1000)\,\text{GJ}$.

## Polish
- L1-02, L1-03 — Problem: these use the lesson table's maakaasu 49 MJ/kg (IPCC gives 48,0) and kivihiili 26 (top of the range); see the lesson report. — Fix: follow any correction there. The answers are consistent with the H the tasks give.
- solutions.md:49 (L1-05) — Problem: 40 g is not "hieman alle puolet" of 100 g. — Fix: use a real estimate, e.g. $25 \cdot 0{,}04 = 1\,\text{MJ}$.
- L3-03 — Problem: the solution is not symbolic first. — Fix: write $P = \eta H m : t$ before substituting.
- L1-01 — Problem (language only): "Moottorisahan huoltoasemalta" reads oddly.

## Checked
- All 12 answers were recomputed independently. They match answers.py, and each is within tolerance (the largest gap is 1,2 %, L3-01).
- The conversions in answers.py are right: t → kg, GJ → MJ, kJ → MJ and MJ/s = MW.
- Each solution solves symbolically first (m = E : H; E_sisään = E_hyöty : η) and justifies its rounding.
- Magnitudes are realistic: about 6 l of petrol per 100 km, a 35 MW peat plant, nuts at 24 MJ/kg, 12 MJ per day for a hiker.
- Scope: one efficiency and P = E : t. There is no chain product, no work and no Q = cmΔT. No × appears, and division uses a colon.
- The levels have 5, 4 and 3 tasks, and none repeats the worked example.
