VERDICT: FAIL
CONTENT-HASH: 85be4e6f81859eff

## Blocking
- content/en/FY2/fy2-4/inquiry.json:262 — A (assessment). The conclusion `johtopaatos` now comes after koe-2 (incandescent lamp, 40 W), and its prompt and model answer are about the lamp only. Its third self-assessment criterion still asks for the petrol engine: "I said that the losses of a petrol engine are a large part of the power taken and that they are heat". The prompt does not ask for this and the model answer does not show it. koe-1 is now optional, so a student on the core path may never have seen the engine's numbers. The Finnish source has the same leftover (content/fi/FY2/fy2-4/inquiry.json, criterion "bensiinimoottorin häviöt …"). — Fix: make the criterion fit the lamp, for example "I said that the remaining $95\,\%$ of the energy the lamp takes is losses, mostly heat (thermal energy)". If the criterion should ask about the time instead, word it as it is in the model answer.

## Polish
(none)

## Checked
- Delta review, round 3, inquiry.json diff only: koe-1 and ennuste-1 are now optional, the koe-1 hint now uses kJ, and the conclusion is moved to koe-2.
- ennuste-1 and koe-1 are both optional, and ennuste-1 reveals its answer after koe-1. The optional flags agree, and no core item depends on koe-1 except the criterion above. pohdi lists ennuste-1 but is itself optional.
- koe-1 hint: $600\,\text{kJ}$ and $450\,\text{kJ}$ give $450 : 600 = 0.75$, which matches the model ($\eta = 0.25$, $P_o = 60\,\text{kW}$, $t = 10\,\text{s}$) and the answer 75 %.
- Recomputed the conclusion's model answer for the locked koe-2 setup (lamp, $\eta = 0.05$ in sim.js, $P_o = 40\,\text{W}$, which the slider reaches: 10–100 W in steps of 5). It gives $P_a = 2.0\,\text{W}$; $t = 10$ and $20\,\text{s}$ give $E_o = 400$ and $800\,\text{J}$, $E_a = 20$ and $40\,\text{J}$, a ratio of 5 % on both rows and 95 % losses. All of these agree with the text.
- The model answer's physics is right: at constant power the time cancels, and $\eta = E_a/E_o = P_a/P_o$. It calls the numbers model values and states the model's assumption of constant efficiency.
- The prompt asks only for what koe-2's table and readout give ($E_o$, $E_a$ and the readout of $P_a$). simState holds Eo, Ea and Pa.
- Hash run at the start and at the end: unchanged, 85be4e6f81859eff.
