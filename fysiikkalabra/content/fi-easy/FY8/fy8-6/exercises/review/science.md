VERDICT: PASS
CONTENT-HASH: ed079581d2145774
SCOPE: delta answers,md-paragraphs,numbers,reflow,structure,typography,wording from 6ef02eec981df84d base 5fb8362

## Blocking

## Polish
- content/fi-easy/FY8/fy8-6/exercises/solutions.md:417 (L3-04) — "kynnysjännitteellä $eU_\text{k} = hf$, joten $U_\text{k} \approx \dfrac{h}{e}f + b$": an exact $=$ cannot give a line with a constant term $b$. Write $eU_\text{k} \approx hf$, as L1-05 now does and as the Periaate step of this solution says.
- content/fi-easy/FY8/fy8-6/exercises/solutions.md:473 (L2-09) — earlier Polish item still open: the read frequency $5{,}8 \cdot 10^{14}$ Hz has two significant figures, not three.
- content/fi-easy/FY8/fy8-6/exercises/solutions.md:474 (L2-09) — earlier Polish item still open: "Suoran kaava antaisi … $hc/(eU_k)$" is the model's formula, not the fitted line's.

## Checked
- L1-05 Kaava (line 79–84): $eU_\text{k} \approx hf$; the fitted line is $U_\text{k} = kf + b$, so $U_\text{k} \approx (h/e)f + b$; the slope is $k = \Delta U_\text{k}/\Delta f \approx h/e$, so $h = ek$. This is correct and matches the lesson ("suora ei yleensä kulje origon kautta", $h \approx ek$). The fix is done.
- L3-04 Kaava: the line form $(h/e)f + b$ and the slope form $\Delta U/\Delta f$ are now right. A constant zero-point offset changes only $b$, which is consistent with the Periaate step and the intercepts $-0{,}062 \to -0{,}112$ V. For a single LED, $h = eU_\text{k}\lambda/c$ is right.
- Recomputed: L1-05 $1{,}602 \cdot 10^{-19} \cdot 4{,}10 \cdot 10^{-15} = 6{,}568 \cdot 10^{-34}$ J s (✓ $6{,}57$). L3-04 $1{,}602 \cdot 10^{-19} \cdot 4{,}208 \cdot 10^{-15} = 6{,}741 \cdot 10^{-34}$ J s (✓ $6{,}74$, $+1{,}7\,\%$).
- L2-06 (line 329): $h_0 = 6{,}626 \cdot 10^{-34}$ J s, with the power of ten back.
- The diff changes no numbers or answers. The rest of the set holds from the previous PASS.
- Hash ed079581d2145774 at the start and at the end.
