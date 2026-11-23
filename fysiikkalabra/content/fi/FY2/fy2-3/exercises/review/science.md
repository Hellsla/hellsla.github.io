VERDICT: PASS
CONTENT-HASH: 9f921f95949e73e1
SCOPE: delta md-paragraphs,numbers,reflow,typography,wording from 633302ba5d59bc16 base 29cd249

## Blocking

## Polish
- solutions.md L2-04 Kaava — "$P = \dfrac{E}{t}$, josta $E = P_\text{yht}\,t$" switches from $P$ to $P_\text{yht}$ in one step; "josta $E = P\,t$; kokonaisteholla $E = P_\text{yht}\,t$" reads correctly (C).
- solutions.md L2-09 a) — the "sähköä tuottava joutuu maksamaan" sentence from my previous report is unchanged (C).
- Earlier item: L1-09 "hp" for metric horsepower (C) is still open.

## Checked
- Hash 9f921f95949e73e1 at the start and the end; only solutions.md changed since base 29cd249 (exercises.json and answers.py untouched).
- Every rewritten Kaava starts from $P = \Delta E/\Delta t$ or $E = P\,t$ and simplifies symbolically before substitution: L2-01 hinta $= P\,t \cdot$ yksikköhinta; L3-01 $\Delta E = (P_1 - P_2)\,t$; L2-05 $E_\text{yht} = \Sigma P_i t_i$; L1-10 ratio $(\Delta E_\text{A}/\Delta t_\text{A}) : (\Delta E_\text{B}/\Delta t_\text{B})$; L3-04 $E = (P_\text{k} - P_\text{t})\,\Delta t$ for the deficit hours; L3-05 $E = \text{osuus} \cdot P\,t$.
- L3-03: the defining relation $k = (E/s) \cdot 100\,\text{km}$ for consumption per 100 km is dimensionally right (kWh) and gives $s = P\,t \cdot 100\,\text{km} / k$.
- Recomputed in one script with my own formulas: 3,0 €; 78,8 kWh; 15,18 €; 342 W; 102 km; 1,80 kW; 2,8 GWh; 346 kWh and 43,2 €; −40 snt; plus every other numeric answer: all agree with answers.py and exercises.json within tolerance, units unchanged.
- The md-paragraph splits (L1-06, L1-07, L1-08, L2-07, L3-02, L3-04, L3-05, L2-09) move no number and change no claim; L2-09 d) still says internal energy transferred as heat.
