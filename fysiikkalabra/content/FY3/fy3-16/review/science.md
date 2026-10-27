VERDICT: FAIL
CONTENT-HASH: 61a36246a094afb0

## Blocking
- inquiry.json:197 (loyly solution, Vastaus) — rounding justified "kuten massassa 0,25 kg ja lämpötilan muutoksessa 90 K", but the share r/(cΔT + r) does not depend on m (the same solution's Järkevyys says m cancels); the limiting datum is ΔT = 90 K alone. — "kaksi merkitsevää numeroa, koska lämpötilan muutos 90 K (100 °C − 10 °C) on kahdella numerolla; massa supistuu".

## Polish
- inquiry.json:121 (kayra) — "t₀ on kolmannen ja neljännen viivan välissä": the t = 0 axis is drawn as a grid line too, so counting from it gives 2–3 h. — "3 h:n ja 4 h:n pystyviivojen välissä".
- exit-ticket.json:8 — 176 kJ has three figures from 0,40 kg and 25 °C. — 1,8·10² kJ.
- inquiry.json:353 (check-3 model) — uses 0,20 kg of 20 °C water that the prompt never gives; criterion "noin 13 %" too. — Give the water in the prompt or write "esimerkiksi".
- solutions.md:119 (L3-03) — "samaa suuruusluokkaa kuin tehtävässä, jossa juomia ei ole" checks nothing; drop it. 1,5 kg is just under the computed minimum 1,51 kg: say it is the minimum to two figures.
- solutions.md L1-03 Järkevyys — "sulattaa jäätä tuntikausia" though the bag (2,0 °C) has no ice. — "riittäisi sulattamaan noin 0,3 kg jäätä tunnissa".

## Checked
- One script recomputed all 12 exercises and 5 inquiry numerics: all match answers.py; stated answers within 1,1 % of exact (tolerances 2–4 %); mistake values are what the named errors give.
- Worked example: 292 100 J / 33,6 W = 8,69·10³ s = 2,41 h, symbolic first; checks (2,76 h × 0,87; initial rise 19,2 K/h) correct and real.
- Both T(t) graphs to scale: plateaus 2,41 h and 3,68 h; exponential rise with τ = C/(UA) matches the paths within 2 px.
- Bar figure 334 / 42 / 335 kJ to scale; cooling-circuit schematic correct.
- L3-02: all-ice-melts test, T = 8,06 °C, balance 183 880 J both sides, two figures from the difference 84 400 J.
- Table Pt = 334 kJ on every row; pred-2 and its 2,2 h distractor right.
- Etsi virhe: 62,9 kJ < 267 kJ, 0,19 kg melts, mean 10,7 °C.
- Formulas inside FY3 contents; conditions (constant T during phase change, inside 0 °C while ice remains) stated.
- Content hash identical at start and end.
