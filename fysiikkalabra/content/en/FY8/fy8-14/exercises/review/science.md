VERDICT: PASS
CONTENT-HASH: 3fa68b4c45b18eee
SCOPE: delta md-paragraphs,numbers,reflow,typography,wording from 207d724bbb879a97 base 64d4935
Mode: delta (work queue 8g: Formula steps rewritten as basic laws then derived formula)

## Blocking
(none)

## Polish
- exercises/exercises.json fy8-14-L2-08 (carried over) — the stated reading accuracy is $0.1\,\text{cm}$, but the box tolerance is 0.06 (about 4 %). A reading of 1.2 cm for bone, still inside that accuracy, gives 1.76 cm and is rejected. Fix: widen the tolerance to about 0.09, or ask for the reading to 0.05 cm.
- exercises/solutions.md:504 (L2-09, carried over) — "three significant figures like the half-life read from the graph": $T_{1/2}$ is read only to about ±5 min. Fix: give the result as 330 min ± 15 min, or $3.3\cdot10^2\,\text{min}$.
- exercises/exercises.json fy8-14-L2-08 text (carried over) — "bone can be replaced by a layer of soft tissue" runs opposite to what part c asks. Fix: "a layer of bone and a layer of soft tissue are equivalent when they let through the same share".

## Checked
- Hash 3fa68b4c45b18eee (`--exercises --lang en`) at the start and the end.
- A word-level diff of the old and new text: only the Formula steps of the nine solutions changed. No number, given value or answer changed. exercises.json and answers.py did not change.
- Nurse dose: $\dot H_2 = \dot H_1(r_1/r_2)^2$, then $H = \dot H_2 t$, so $H = \dot H_1 (r_1/r_2)^2 t$. Correct, under the point-source condition stated in the Principle.
- Radiotherapy entry dose: $D_\text{beam} = D_\text{session}/n$, $D_\text{entry} = kD_\text{beam}$, $D = N k D_\text{session}/n$. Correct: only one beam passes the entry point.
- Calcification ratio: $I_\text{A}/I_\text{B} = 2^{d/d_{1/2}^\text{bone} - d/d_{1/2}^\text{tissue}}$ is correct, and the common $I_0$ and the other layers cancel properly.
- Lead shield and calibration plate: the chain from the attenuation law to the ratio $=2^{d/d_{1/2}}$, then the ln, then $d$ is correct. In the calibration, $d_{1/2} = d_{20}\ln2/\ln(R_0/R_{20})$ and $d_x$ are right.
- PET-CT: $A_0 = am/(\tfrac12)^{t/T_{1/2}}$ and $H = kA_0 + H_\text{CT}$ are right. The dose coefficient applies to the injected activity, and the activity falls only by decay, as the task states.
- answers.py run against exercises.json: all 20 numeric answers lie within their relative tolerances.
- Every chain starts with the quantity and is simplified symbolically before substitution. The notation is the same as in the rest of the set.
