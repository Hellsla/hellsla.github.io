VERDICT: PASS
CONTENT-HASH: a1ebebb8289eeabd

## Blocking

## Polish
- inquiry.json johtopaatos model — "$\Delta l = 6{,}0\,\text{mm}$" next to "$12{,}0\,\text{mm}$" and the predictions' "$6{,}00\,\text{mm}$" — write $6{,}00\,\text{mm}$ for consistency.
- inquiry.json olomuodot correct option — the "weaker interactions" mechanism fits solids and liquids. A gas at constant pressure expands because $V \propto T$ (luku *Kaasujen tilanmuutokset*). The lesson's own wording ("lähes vapaita, vakiopaineessa") is enough at this level (C). A pointer to the next chapter could be added.
- inquiry.json check-3 model — "noin sata kertaa": $3{,}4 \cdot 10^{-3} / 36 \cdot 10^{-6} \approx 94$. This is fine as an order of magnitude.

## Checked
- One script recomputed 28 numbers from the task data with my own formulas: worked example ($86{,}4\,\text{mm}$, $0{,}072\,\%$), pred-1/pred-2 model values, olomuodot table ($0{,}36$, $2{,}1$, $11$, $34\,\text{cm}^3$), virhe ($28$ vs $1{,}8\,\text{mm}$, ×15), siirto ($44\,\text{mm}$, mistakes $0{,}044$ and $110$, glass ratio ≈ 41, $43\,\text{mm}$ with glass), check-2 ($23 \cdot 10^{-6}$, mistakes 46 and 15,3) and the exit ticket ($21\,\text{mm}$). All agree.
- Model conditions: the linear formula is stated for solids up to about $100\,\text{K}$, and a liquid's $\gamma$ only near $20\,{}^\circ\text{C}$ (guardrail). $\gamma \approx 3\alpha$ is derived for small changes. Gas expansion is stated at constant pressure.
- Mechanism: the asymmetric interaction makes the mean spacing grow, and the particles do not grow. The particle figure, the glossary, pred-3 and check-3 say the same. The sim's symmetric vibration is disclosed in its `model` box and in the pred-3 feedback.
- Water anomaly: maximum density near $4\,{}^\circ\text{C}$, the lake freezes from the top. check-1 has exactly one correct option and its distractor feedback is right.
- Hole in a plate grows; the shrink fit is explained correctly (check-c2).
- Signs: cooling gives negative $\Delta T$ and $\Delta l$ (theory, sim readout, conclusion).
- sim.js implements $\Delta L = \alpha L_0 (T - 20\,{}^\circ\text{C})$ with constant $\alpha$. The exaggeration ×100 is printed. "alle $0{,}3\,\%$" holds (max $0{,}23\,\%$). The amplitude $\propto \sqrt{T}$ (K) is a fair picture. The ΔT range of at most $100\,\text{K}$ matches the stated validity.
- Experiments: exp-1 locks material and L0 and varies T; exp-2 locks material and T and varies L0. simState gives `dT`, `dL` (m) and `rel`, and the adapter exposes `material`, `L0` and `T`.
- Tables of α and γ are realistic (steel 12, Al 23, Cu 17, glass 9, borosilicate 3,3; water 0,21, ethanol 1,1, petrol 0,95, air 3,4 ·10⁻³).
- Every prediction and choice item has exactly one correct option, and each distractor's feedback names the actual misconception.
