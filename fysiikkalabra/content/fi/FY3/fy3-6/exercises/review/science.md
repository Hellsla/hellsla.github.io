VERDICT: PASS
CONTENT-HASH: 09782c554ddc3f1d

Delta review over the audit's PASS (13bc0d2daf5f4e53): L2-02 replaced by figure task heating-line (c from P, m and the graph).

## Blocking
- none
## Polish
- solutions.md:69 says 870…930 J/(kg·K) is accepted, but tolerance 0,03 on 900 accepts 873…927. The readings are exact grid crossings; narrow the stated range or set tolerance 0.034.
## Checked
- Recomputed: c = Pt/(mΔT) = 100 W · 180 s / (0,50 kg · 40 K) = 900 J/(kg·K); answers.py 900; it matches aluminium 900 in the lesson table.
- Figure heating-line: (0 s; 20 °C) and (180 s; 60 °C) on 20 s × 10 °C grid crossings; the description has no slope and no c.
- Assumption "all the heater's energy goes into the block" is stated (guardrail: linear heating only with small losses); two significant figures from 0,50 kg are justified.
