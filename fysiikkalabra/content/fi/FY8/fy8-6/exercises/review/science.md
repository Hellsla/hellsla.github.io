VERDICT: FAIL
CONTENT-HASH: 2f5f896a98ba9818

## Blocking
- exercises/solutions.md:78–84 (fy8-6-L1-05) — **A/B, internal consistency.** The new Kaava says "Kynnysjännitteellä $eU_\text{k} = hf$, ja suoran yhtälö on $U_\text{k} = kf$" and $k = \tfrac{U_\text{k}}{f}$. That makes the fitted line pass through the origin and defines the slope as the ratio at one point. This contradicts the task's own Periaate ($eU_\text{k} \approx hf$, "likimain suora"). It also contradicts L3-01, L3-04 and L3-05, which say the line need not pass through the origin and carry an intercept $b$ (about $-0{,}11\,\text{V}$). The guardrail says a line through the origin needs a physical reason and a slope is read from the fitted line. — Fix: write $eU_\text{k} \approx hf$, so $U_\text{k} \approx \tfrac{h}{e}f + b$, and $k = \tfrac{\Delta U_\text{k}}{\Delta f} \approx \tfrac{h}{e}$, which gives $h \approx ek$. The answer is unchanged.
- exercises/solutions.md:422 (fy8-6-L3-04) — **B/A, internal consistency.** The new Kaava says "$eU_\text{k} = hf$, joten $U_\text{k} = \tfrac{h}{e}\,f$". That is a line through the origin. The same task's Kuvaajan lukeminen fits a line with intercept $b = -0{,}062\,\text{V}$ (corrected $-0{,}112\,\text{V}$), and its Periaate says $\approx$. — Fix: $eU_\text{k} \approx hf$, so $U_\text{k} \approx \tfrac{h}{e}f + b$ and the slope is $k \approx \tfrac{h}{e}$. The answer is unchanged.

## Polish
- exercises/solutions.md:421–422 (L3-04) — the slope is called $m$ in Kuvaajan lukeminen and $k$ in Kaava. Use one symbol.
- exercises/solutions.md:99, 125, 270 (L2-01, L2-02, L1-07) — "elektronin energia on yhden fotonin energia, $eU_\text{k} = E$" is stated as a fact. In L2-02 it is the task's explicit assumption, which is fine. In L2-01 and L1-07, adding "mallissa" or "likimain" would match their Periaate.

## Checked
- Hash 2f5f896a98ba9818 at the start and the end. `git diff 64d4935`: only solutions.md changed (Kaava blocks, split paragraphs). exercises.json and answers.py are unchanged.
- L1-04 and L1-06: $E_\text{g} = hf = \tfrac{hc}{\lambda}$ gives $\lambda = \tfrac{hc}{E_\text{g}}$. This is right under the stated $hf \approx E_\text{g}$.
- L2-03 and L3-03: $I = Ne$, $P = NE$ and $E = \tfrac{hc}{\lambda}$ give $P = \tfrac{Ihc}{e\lambda}$ and the ratio $\tfrac{P\lambda e}{hcI}$. Both are right.
- L2-04 and L2-07: $\Delta E = hf_1 - hf_2 = \tfrac{hc}{\lambda_1} - \tfrac{hc}{\lambda_2}$. The energy that stays in the phosphor becomes internal energy, which follows the guardrail.
- L2-05: $I_1 = k(U_1 - U_\text{k})$ gives $U_\text{k} = U_1 - \tfrac{I_1}{k}$. This is right.
- L2-06, L3-05 and L2-10: $h = \tfrac{eU_\text{k}\lambda}{c}$, $\lambda = \tfrac{hc}{eU_\text{k}}$ and $U_\text{malli} = \tfrac{hf}{e}$ are right as model comparisons.
- The split paragraphs (Aino/Salla/Eero, the LED bandwidth, $\Delta h = e\,\Delta k$) keep every claim and number.
- The numbers did not change. answers.py runs.
