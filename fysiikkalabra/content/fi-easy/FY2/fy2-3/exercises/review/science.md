VERDICT: PASS
CONTENT-HASH: 9bd85e906508526b
SCOPE: delta md-paragraphs,numbers,reflow,typography,wording from e603919a2eee171f base 29cd249

## Blocking

## Polish
- solutions.md:216 (six lights, year): "$P = \dfrac{E}{t}$, josta $E = P_\text{yht}\,t$" swaps the symbol while it solves. Fix: "$P = \dfrac{E}{t}$, josta $E = P\,t$; kokonaisteholla $E = P_\text{yht}\,t$ ja $P_\text{yht} = 6 \cdot P$, joten $E = 6\,P\,t$".
- solutions.md:363 (L2-09 d), paragraph only moved): "osa muuttuu sisäenergiaksi, joka siirtyy lämpönä ympäristöön" is FY3 wording. The guardrails keep "lämpöenergia" in FY2, and the scope notes leave internal energy out of FY2. Fix: "osa muuttuu lämpöenergiaksi, joka siirtyy lämpönä ympäristöön".

## Checked
- Every rewritten Kaava line now starts from $P = \Delta E/\Delta t$ or $E = P\,t$ (the definition the lesson teaches). It combines the basic relations symbolically before any number: sauna $\text{hinta} = P\,t \cdot \text{yksikköhinta}$; LED $\Delta E = (P_1 - P_2)\,t$; device day $E_\text{yht} = P_1 t_1 + P_2 t_2 + \dots$; graph $P_\text{A}/P_\text{B}$ as a ratio of quotients; grid $E = (P_\text{k} - P_\text{t})\,\Delta t$; fridge $E = \text{osuus} \cdot P\,t$.
- Electric car: $k = (E/s) \cdot 100\,\text{km}$, the consumption per 100 km in kWh. Solving it gives $s = (P\,t/k) \cdot 100\,\text{km}$, which is correct in units and algebra. $2{,}3 \cdot 8{,}0 / 18 \cdot 100 = 102{,}2\,\text{km}$.
- Recomputed: $6{,}0 \cdot 2{,}5 \cdot 0{,}20 = 3{,}0$ €; $0{,}0090 \cdot 8760 = 78{,}84\,\text{kWh}$; $0{,}052 \cdot 1460 = 75{,}92\,\text{kWh}$, giving $15{,}18$ €; $47{,}0/119{,}0 = 0{,}395$, giving $346\,\text{kWh}$ and $43{,}2$ €; $1{,}50/0{,}833 = 1{,}80\,\text{kW}$; $3{,}0 \cdot 10^3/8760 = 0{,}3425\,\text{kW}$; grid deficit $2800\,\text{MWh} = 2{,}8\,\text{GWh}$; $8{,}0 \cdot 0{,}41 = 3{,}3\,\text{snt}$. All agree with the solutions.
- The paragraph splits (two-device comparison, slope task, L3-02, L3-04, L3-05, L2-09) leave every claim and number as it was.
- answers.py matches every numeric answer in exercises.json within its tolerance. No answer, unit or tolerance changed.
- Hash 9bd85e906508526b at the start and at the end.
