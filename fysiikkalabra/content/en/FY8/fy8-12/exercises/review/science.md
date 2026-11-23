VERDICT: PASS
CONTENT-HASH: 4334b85dabe8a52a
SCOPE: delta numbers,reflow,typography from 3c71dfde0dd50970 base 4b05399
Mode: delta (work queue 8g: only the Formula steps of the model solutions changed)

## Blocking
(none)

## Polish
- exercises/solutions.md:76–82 (L1-05) — "$E = hf$, from which: $f = c/\lambda$" — $f = c/\lambda$ does not follow from $E = hf$; it is the wave equation, a second basic law. Fix: "$E = hf$ and $c = f\lambda$, from which: …".
- exercises/solutions.md:492–498 (L3-05) — "$R = \dots$, from which: $T = (\tfrac12)^{d/d_{1/2}}$, $R = A T \eta$" — the transmitted fraction and $R = AT\eta$ are separate relations, not consequences of the net-rate formula. Fix: list the three basic relations, then "from which $A = R/(T\eta)$".
- exercises/solutions.md:143–148 (L2-02) — the same: $I_2 = I_1(\tfrac12)^{d_\text{b}/d_{1/2,\text{b}}}$ is the attenuation law applied a second time, not derived from $I_1$. Fix: "and the concrete gives $I_2 = \dots$, so $I_2/I_0 = \dots$".

## Checked
- Hash 4334b85dabe8a52a (`--exercises --lang en`) at the start and the end.
- The packet diff flattens the aligned blocks. I read the real `aligned` blocks on disk (lines 76–590): every row is a correct equation.
- L2-03, L2-06, L3-04: the steps go from the attenuation law to the ratio $=2^{d/d_{1/2}}$, then the ln, then $d_{1/2} = d\ln2/\ln(\dots)$. The algebra is right and the result is unchanged.
- L3-02: both blocks are right. $(\tfrac12)^{d/d_{1/2}} = R_\text{t}/(R_0-R_\text{t})$ inverts to $d = d_{1/2}\ln\frac{R_0-R_\text{t}}{R_\text{t}}/\ln2$, which is the same as answers.py (net rate down to 30/min).
- L2-04: equal fractions give equal exponents, and $d_\text{b}$ is solved correctly.
- L2-01, L1-07: the net counts are formed first and then the rate. Both are right, and the background is subtracted from the count, not from the rate units.
- L3-07: $\ln(R_0/R) = (d/d_{1/2})\ln2$ gives $d$, as before.
- answers.py run against exercises.json: all 21 numeric answers lie within their tolerances. Only solutions.md changed, so the numbers, answers and tolerances are unchanged.
- The symbols ($N_\text{t}$, $d_{1/2}$, $R_\text{t}$) are the same as in the rest of the set. Every unknown is still solved symbolically before substitution.
