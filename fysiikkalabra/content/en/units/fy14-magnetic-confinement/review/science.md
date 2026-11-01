VERDICT: PASS
CONTENT-HASH: a8a5be11ce98c4fb

Re-review of commit cf5a329b and of the simulation commit 7561f2b5. The previous Polish 1–3 are fixed: the alpha task shows $mv^2/2 = 1.67 \cdot 10^{-15}\ \text{J} \approx 10\ \text{keV}$, the sim model says the fastest speed is 3.3 % of c, and the howto names the sideways drift with $\overline{E}$.

## Blocking
None.

## Polish
None.

## Checked
- New check-2: an electron moves up the page with $\overline{B}$ ⊙. $\overline{v} \times \overline{B} = \hat{y} \times \hat{z} = +\hat{x}$, and the charge is negative, so the force points to the **left**. Only that option is marked correct, and every distractor's feedback is correct.
- Rebalanced options (review, exp-particles, find-error, check-1) were re-read. The physics and the correct answers are unchanged ("1836 times smaller, not larger" is correct).
- The experiment `values` now name the particles and show trapped / escapes. The sim strings no longer state the mirror condition or verdict, so the prediction is not answered before the experiment. The readout still gives $\sin^2\theta$ and $B_0/B_{\max}$, which is correct. `simState.trapped` comes from the model, unchanged. `node tests/models/magnetic.test.js` runs 708 checks, all OK. The model and physics in `sim.js` are unchanged: only the font size and the readout strings changed.
- The worked example (4.17 mm, 26.2 ns), the alpha task (5.08 cm) and the model values in the feedback (20.9 / 10.4 mm, 65.6 / 32.8 ns, loss cone 30°) are unchanged and correct.
