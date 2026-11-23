VERDICT: PASS
CONTENT-HASH: 02af06d85c6fff13
SCOPE: delta md-paragraphs,numbers,reflow,typography from ceed05861c35b96a base 64d4935

## Blocking
(none)

## Polish
- exercises/solutions.md fy8-6-L3-04 Formula — the row says "$eU_\text{k} = hf$, so $U_\text{k} \approx \tfrac{h}{e} f + b$": the model relation gives no $b$; write "$eU_\text{k} \approx hf$, and the fitted line is $U_\text{k} = kf + b$" as L1-05 now does.
- exercises/solutions.md fy8-6-L3-02 Formula — say that $\Delta h = \tfrac{h_\text{max} - h_\text{min}}{2}$ is half the range of the steepest and shallowest lines (an estimate; guardrails "Showing uncertainty"). Carried from the last round.

## Checked
- Hash 02af06d85c6fff13 at the start (same as the packet's) and at the end.
- Diff: only the Formula rows of L1-05 and L3-04 changed. No numbers, answers, answers.py or tolerances changed.
- L1-05: $eU_\text{k} \approx hf$, fitted line $U_\text{k} = kf + b$, $k = \Delta U_\text{k}/\Delta f \approx h/e$, $h = ek$. Correct, and it now fits the guardrail on fits (a line through the origin needs a physical reason; the intercept absorbs the offset of the threshold voltages). Recomputed $h = 1.602\cdot10^{-19} \cdot 4.10\cdot10^{-15} = 6.568\cdot10^{-34}\,\text{J}\,\text{s}$, matches.
- L3-04: recomputed the least-squares fit of the five LEDs. Frequencies 4.759 to 6.447 $\cdot 10^{14}$ Hz, slope $4.208\cdot10^{-15}\,\text{V}\,\text{s}$, intercept $-0.062\,\text{V}$ before the correction and $-0.112\,\text{V}$ after it, $h = 6.742\cdot10^{-34}\,\text{J}\,\text{s}$, deviation $+1.7\,\%$. All match the solution and answers.py.
- L2-06: $h_0 = 6.626 \cdot 10^{-34}\,\text{J}\,\text{s}$ is back (solutions.md line 351, and line 454 in L3-04).
- `\dfrac` in the new rows renders the same physics; there is no notation conflict with the brief.
