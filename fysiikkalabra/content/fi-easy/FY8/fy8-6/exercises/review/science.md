VERDICT: FAIL
CONTENT-HASH: ed079581d2145774

## Blocking
- content/fi-easy/FY8/fy8-6/exercises/solutions.md:350 (L2-06) — A (quantitative, internal consistency): "Hänen ylimääräinen noin $0{,}16\,\text{V}$ kumoaa osan siitä, että kynnysjännite on … noin $0{,}1\,\text{V}$ pienempi kuin $\tfrac{hf}{e}$". The extra $0{,}16\,\text{V}$ (Salla $2{,}04\,\text{V}$ against Eero $1{,}88\,\text{V}$) cancels the whole difference of about $0{,}09\,\text{V}$ ($\tfrac{hc}{e\lambda} = 1{,}97\,\text{V}$) and goes past it by about $0{,}07\,\text{V}$. That is why Salla's $h$ is $3{,}65\,\%$ too large, as the same solution computes. "Kumoaa osan" says her value should still be too small, which contradicts the computed $+3{,}65\,\%$. — Write that it cancels the difference and goes about $0{,}07\,\text{V}$ past it (e.g. "kumoaa tämän eron ja menee noin $0{,}07\,\text{V}$ sen yli").

## Polish
- content/fi-easy/FY8/fy8-6/exercises/solutions.md:422 (L3-04) — "kynnysjännitteellä $eU_\text{k} = hf$, joten $U_\text{k} \approx \dfrac{h}{e}f + b$": an exact $=$ gives no constant term $b$. Write $eU_\text{k} \approx hf$, as L1-05 and this solution's Periaate do.
- content/fi-easy/FY8/fy8-6/exercises/solutions.md:146 (L2-02) — "Tämä lähes vakiosuuruinen ero ei vaikuta kulmakertoimeen": the lesson says the difference varies from LED to LED and the slope "ei juuri muutu". Write "ei juuri vaikuta, kun ero on lähes sama kaikilla LEDeillä".
- content/fi-easy/FY8/fy8-6/exercises/solutions.md:473 (L2-09) — the read frequency $5{,}8 \cdot 10^{14}\,\text{Hz}$ has two significant figures, not three. Justify 517 nm by the exact grid crossing, or give about 520 nm.
- content/fi-easy/FY8/fy8-6/exercises/solutions.md:474 (L2-09) — "Suoran kaava antaisi … $\tfrac{hc}{eU_\text{k}}$": this is the model's formula, not the fitted line's. Write "Mallin kaava".

## Checked
- One script recomputed all 21 numeric answers from the task text. Every answer agrees with answers.py and with my own formulas within 0,3 %. Tolerances fit the data; L2-05 including the 1,80 V point gives 1,82 V, which is still accepted.
- L1-05, L3-04: the fitted line $U_\text{k} \approx (h/e)f + b$ and $h = ek$ are right. The zero-point offset changes only $b$ ($-0{,}062 \to -0{,}112\,\text{V}$); the slope stays $4{,}208 \cdot 10^{-15}\,\text{V}\,\text{s}$ and $h = 6{,}742 \cdot 10^{-34}\,\text{J}\,\text{s}$ ($+1{,}7\,\%$). A single red LED gives $6{,}497 \to 6{,}329$ ($-2{,}6\,\%$, $-4{,}5\,\%$ after the correction).
- L2-06 line 329: $h_0 = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$ is right. Aino gives $5{,}858$ ($-11{,}6\,\%$), Eero $6{,}329$ ($-4{,}5\,\%$), Salla $6{,}868$ ($+3{,}65\,\%$).
- L2-08: my least-squares fit of the table gives $k = 3{,}976 \cdot 10^{-15}\,\text{V}\,\text{s}$ and $b = -0{,}074\,\text{V}$, matching the task. $h = 6{,}376$ and $\Delta h = 0{,}336$ ($10^{-34}\,\text{J}\,\text{s}$); 6,626 lies inside the interval. Only option 3 is correct, and each distractor's feedback is right.
- L1-06: exactly one correct option. The distractors (heating, the voltage setting the colour, absorption in the casing) are wrong, and their feedback says why.
- L2-09/L2-10 against the figure: the line through (4,6; 1,80) and (7,0; 2,80) gives $f = 5{,}8 \cdot 10^{14}\,\text{Hz}$ (517 nm, green) and an intercept of $-0{,}117\,\text{V}$ ("noin 0,12 V"). $hf/e = 2{,}895\,\text{V}$, so the difference is 0,095 V.
- L3-01: fit $4{,}212 \cdot 10^{-15}\,\text{V}\,\text{s}$, $b = -0{,}164\,\text{V}$, $+1{,}8\,\%$; the two farthest points give $4{,}18$. L3-02: $\Delta h = 2{,}4 \cdot 10^{-35}\,\text{J}\,\text{s}$.
- L3-05: $f = 6{,}169 \cdot 10^{14}\,\text{Hz}$, 486 nm against 504 nm from the formula, $\Delta\lambda = 9{,}5\,\text{nm}$, 0,6 % and 4,4 %. The method comparison is right.
- L2-07: half-maximum points 620 and 640 nm, $\Delta E = 0{,}0625\,\text{eV}$, about 3 % of 1,97 eV; the thermal-spread explanation is right. L2-03/L3-03: 39,4 mW and 22,1 %. L1-04: GaAs 873 nm (infrared).
- Scope inside FY8 (photon $E = hf$, LED threshold); symbols match the lesson. Hash ed079581d2145774 at the start and at the end.
