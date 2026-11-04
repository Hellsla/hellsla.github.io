VERDICT: PASS
CONTENT-HASH: 02a46dce04663f3e

Follow-up review of the fix commit 2c31ff041 (delta from cc6a622ee50a1fe4). Change: lesson.md:113, the paragraph after $P = UA\Delta T$.

## Blocking

## Polish
- inquiry.json:67, :126, :135, :167 — "sisällä pysyy $0\,{}^\circ\text{C}$" is right inside the stated model (graph "laskettu mallilla"); "mallissa" would make the link explicit (C).

## Checked
- New wording "Mallissa oletetaan, että laukun sisälämpötila on $0\,{}^\circ\text{C}$ niin kauan kuin jäätä on. Silloin $\Delta T$ on ulkolämpötila celsiusasteina." turns the fact into a stated model assumption; it agrees with the Ydinajatus (only the ice–water mixture stays at about $0\,{}^\circ\text{C}$) and with $t = sm/(UA\Delta T)$.
- grep of "$0\,{}^\circ\text{C}$" in lesson.md and inquiry.json: no contradiction with the new sentence.
- Earlier: ice and meltwater at the same temperature, energy goes to melting while ice remains (guardrails: changes of state); $334\,\text{kJ} \approx 4{,}19\,\text{kJ/(kg·K)} \cdot 80\,\text{K}$; area $0{,}80\,\text{m}^2$.
- Hash same at start and end.
