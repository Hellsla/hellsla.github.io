VERDICT: PASS
CONTENT-HASH: 4cfa8a8208c7ac15

Delta review over the audit's PASS (497163bfee90ee02): L1-03 (c m ΔT of 0,30 kg water) replaced by a figure task (fy3-14/energy-bars: 25 kJ water, 5 kJ warming the ice, 60 kJ melting all; how much ice melts).

## Blocking
- none
## Polish
- none
## Checked
- Figure code: bars end at 25, 5 and 60 kJ on a 5 kJ grid (labels every 10 kJ); screenshot matches; the description does not give the melted mass.
- Case: 5 ≤ 25 < 5 + 60 kJ -> ice left, final 0 °C, wording matches the guardrail boundary cases; water does not freeze (25 ≥ 5).
- m_s = (25 − 5) kJ / 334 kJ/kg = 0,05988 kg = 59,9 g -> 60 g; answers.py = 59,88; energy balance 5 + 20 = 25 kJ right.
- Tolerance 0,02 -> 58,8–61,2 g; rejects 25/334 = 74,9 g (forgetting to warm the ice) and "all melts" 180 g.
- Consistency: all ice 60/334 = 0,180 kg; its warming 5 kJ means ΔT ≈ 13 K with c = 2100 J/(kg·K), plausible ("pakastimesta", no temperature given).
- Isolated vessel stated; 2 s.f. from the read 20 kJ right.
