VERDICT: PASS
CONTENT-HASH: a6f273d0b5ebe0c0
SCOPE: delta added-exercise from b38642a6e641d4f2 base 89bcb63b7431

## Blocking

## Polish
- exercises/solutions.md (fy3-13-L2-10, Kuvaajan lukeminen) — as in round 1: the stated range "$52$–$58\,\text{kPa}$" is slightly wider than tolerance 0,05 (52,1–57,6 kPa). Write "noin $52$–$57\,\text{kPa}$".
- exercises/solutions.md (fy3-13-L2-09 and L2-10, Periaate) — "Pisteet ovat suoralla": the task text now says "lähes suoralla" (neighbouring slopes 0,26–0,28 kPa/°C). Say the same in both solutions, per the guardrail on fits.
- exercises/exercises.json (fy3-13-L1-09) — tolerance 0,04 (±11 °C) on an exact defined value is loose; 0,01 would fit a lookup. Harmless.

## Checked
- Round-1 blocker 1 fixed: L2-09 tolerance is 0,05 (−259,1 … −286,4 °C), which matches the stated hand-drawn range −259 … −286 °C. Reading the 100 °C point as 102 or 103 kPa gives −277,8 or −267,9 °C, both accepted. The uncertainty now reads "noin kymmenen celsiusastetta tai enemmän", which is honest.
- Round-1 blocker 2 fixed: L1-09 Järkevyys now keeps the liquid-nitrogen comparison as a magnitude check only and gives the real reason separately (the kelvin scale starts at absolute zero, so no negative kelvin temperature exists).
- L1-09 recomputed: $\theta_0 = -T_0 = -273{,}15\,{}^\circ\text{C}$ (MAFY 0 °C = 273,15 K), which matches answers.py.
- L2-09 recomputed: $k = 27{,}5/100 = 0{,}275\,\text{kPa/°C}$, $\theta_0 = -75/0{,}275 = -272{,}7\,{}^\circ\text{C}$, which matches answers.py; the least-squares line gives −272,1 °C, also accepted.
- L2-10 recomputed: $\theta = -73{,}15\,{}^\circ\text{C}$, $p = 75 - 0{,}275 \cdot 73{,}15 = 54{,}88\,\text{kPa}$; the independent $p \propto T$ check gives 54,9 kPa. The task states the linear-extrapolation assumption.
- Rigid closed vessel (fixed $n$, $V$) is stated; symbols as in the brief ($k$, $\theta_0 = \theta_1 - p_1/k$). Solutions are complete.
- Figure fy3-3/extrapolation-points gives both tasks what they need and does not give the answer.
- Rest of the set unchanged since PASS; hash same at start and end.
