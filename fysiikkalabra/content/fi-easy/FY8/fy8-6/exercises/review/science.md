VERDICT: PASS
CONTENT-HASH: cea2d4f0fbef37cb

## Blocking

## Polish
- content/fi-easy/FY8/fy8-6/exercises/solutions.md:146 (L2-02) — "Tämä lähes vakiosuuruinen ero ei vaikuta kulmakertoimeen": the lesson says the difference varies from LED to LED and the slope "ei juuri muutu". — Write "ei juuri vaikuta kulmakertoimeen, kun ero on lähes sama kaikilla LEDeillä".
- content/fi-easy/FY8/fy8-6/exercises/solutions.md:473 (L2-09) — the read frequency $5{,}8 \cdot 10^{14}\,\text{Hz}$ has two significant figures, not three. — Justify 517 nm by the exact grid crossing of the line, or give about 520 nm.
- content/fi-easy/FY8/fy8-6/exercises/solutions.md:474 (L2-09) — "Suoran kaava antaisi … $\tfrac{hc}{eU_\text{k}}$": that is the model's formula, not the fitted line's. — Write "Mallin kaava".

## Checked
- This was a full review. One script recomputed all 21 numeric answers from the task text with my own formulas. Every answer matches answers.py and my values within 0,3 %, inside its tolerance. L2-05 with the 1,80 V point included gives 1,82 V, which is still accepted.
- L2-06 (the earlier Blocking item) is fixed. Aino's 5,858 gives −11,6 %, Eero's 6,329 −4,5 % and Salla's 6,868 +3,65 % ($10^{-34}\,\text{J}\,\text{s}$). With $hc/(e\lambda) = 1{,}968\,\text{V}$, Salla's extra 0,16 V cancels the 0,09 V gap and goes past it, as line 350 now says.
- L3-04: the slope is $4{,}208 \cdot 10^{-15}\,\text{V}\,\text{s}$ before and after the correction. The intercept goes from −0,062 V to −0,112 V. $h = 6{,}742$ (+1,7 %). The red LED alone gives 6,497 before the correction and 6,329 after it (−2,6 %, then −4,5 % from 6,626). The "Kaava" line now uses $\approx$.
- L1-05, L3-01: $h = ek$ is right. In L3-01 the least-squares slope is $4{,}212 \cdot 10^{-15}$ and $b = -0{,}164\,\text{V}$ (+1,8 %). The two farthest points give 4,18. L3-02: $\Delta h = 2{,}40 \cdot 10^{-35}\,\text{J}\,\text{s}$.
- L2-08: my fit of the table gives $k = 3{,}976 \cdot 10^{-15}$ and $b = -0{,}074\,\text{V}$, which matches the task. $h = 6{,}376$ and $\Delta h = 0{,}336$, so 6,626 lies inside $h \pm \Delta h$. Exactly one option is correct, and each distractor's feedback is right.
- L1-06: exactly one option is correct. The heating, colour-by-voltage and casing-absorption distractors are wrong, and their feedback gives the right mechanism (band gap).
- Figure `fy8-6/ryhma` against L2-09 and L2-10: the line through (4,6; 1,80) and (7,0; 2,80) gives $f = 5{,}80 \cdot 10^{14}\,\text{Hz}$ at 2,30 V (517 nm, green). Its intercept is −0,117 V. $hf/e = 2{,}895\,\text{V}$, so the difference is 0,095 V. The figure's points lie near the line, and its description gives the reading points without the answers.
- L3-05: $f = 6{,}169 \cdot 10^{14}\,\text{Hz}$ gives 486,0 nm, against 504,1 nm from the direct formula. $\Delta\lambda = 9{,}5\,\text{nm}$, and the deviations are 0,6 % and 4,4 %. The method comparison and the back-check are right.
- L2-07: the half-maximum points 620 and 640 nm give $\Delta E = 0{,}0625\,\text{eV}$, about 3 % of 1,97 eV. The thermal-spread explanation is right. L2-03: 39,4 mW. L3-03: 22,1 % (below 100 %). L2-04: 0,541 eV, and "sisäenergiaksi" follows the guardrail. L1-04: 873 nm (infrared).
- Scope is inside FY8 (photon $E = hf$, LED threshold, Planck's constant from data), and the symbols match the brief. Hash cea2d4f0fbef37cb at the start and at the end.
