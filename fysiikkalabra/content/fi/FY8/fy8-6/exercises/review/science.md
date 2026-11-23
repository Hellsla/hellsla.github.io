VERDICT: PASS
CONTENT-HASH: 44874ddf209d177a

## Blocking

## Polish
- exercises/solutions.md:422 (fy8-6-L3-04) — the Kaava still opens "kynnysjännitteellä $eU_\text{k} = hf$, joten $U_\text{k} \approx \tfrac{h}{e}f + b$". An exact equality would give $b = 0$, so the "joten" does not follow. The intercept and the slope $k = \tfrac{\Delta U_\text{k}}{\Delta f} \approx \tfrac{h}{e}$ are now right, so this is not blocking. — Write $eU_\text{k} \approx hf$, as in L1-05 (line 78) and in this task's own Periaate.
- exercises/solutions.md:194 (fy8-6-L3-01) — the Kaava is still "$k = \dfrac{h}{e}$" with an equals sign, but the task fits $b = -0{,}164\,\text{V}$. This line was not changed. For consistency with L1-05 and L3-04, write $k \approx \tfrac{h}{e}$.
- exercises/solutions.md:99, 125, 270 (L2-01, L2-02, L1-07) — the new Kaava rows say "elektronin energia on yhden fotonin energia, $eU_\text{k} = E$". This is fine where the task states it as its assumption (L2-02). In L2-01 and L1-07, "likimain" would match their Periaate (carried over from last time).

## Checked
- Hash 44874ddf209d177a at the start and at the end.
- L1-05 (line 78): the aligned block now reads $U_\text{k} \approx \tfrac{h}{e}f + b$, $k = \tfrac{\Delta U_\text{k}}{\Delta f} \approx \tfrac{h}{e}$, $h = ek$. This fixes the earlier finding; $h = 6{,}568 \cdot 10^{-34}\,\text{J}\,\text{s}$.
- L3-04: the line now has its intercept $b$ and the slope as $\Delta U/\Delta f$, which fixes the earlier finding. $h = 6{,}742 \cdot 10^{-34}\,\text{J}\,\text{s}$ ($+1{,}7\,\%$), and the single-LED values are $6{,}497$ and $6{,}329 \cdot 10^{-34}\,\text{J}\,\text{s}$.
- L2-06 (line 323): $h_0 = 6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$ carries its power of ten. Aino, Eero and Salla get $5{,}858$, $6{,}329$ and $6{,}868 \cdot 10^{-34}\,\text{J}\,\text{s}$, or $-11{,}6$, $-4{,}5$ and $+3{,}65\,\%$.
- The new Kaava rows start from $E = hf$ and $c = f\lambda$ (and from $I = Ne$ and $P = NE$) and derive the combined formula. Each aligned block is algebraically right: L1-04 gives $873{,}2\,\text{nm}$, L2-01 $2{,}638\,\text{V}$, L2-02 $6{,}304 \cdot 10^{-34}\,\text{J}\,\text{s}$, L2-03 $39{,}4\,\text{mW}$, L2-04 $0{,}541\,\text{eV}$ and L3-03 $22{,}1\,\%$. All were recomputed.
- L1-07 gives $539{,}1\,\text{nm}$. L2-05 gives $U_\text{k} = 1{,}857\,\text{V}$, against the comparison value $1{,}908\,\text{V}$. L2-07 gives $\Delta E = 0{,}0625\,\text{eV}$ and a peak of $1{,}97\,\text{eV}$. L3-05 gives $486{,}0\,\text{nm}$ by the line, $504{,}1\,\text{nm}$ directly and $\Delta\lambda = 9{,}5\,\text{nm}$. L2-10 gives $\Delta U = 0{,}095\,\text{V}$.
- The split paragraphs (L1-06, L2-06, L2-07, L3-02) keep every claim and number. exercises.json and answers.py were not touched by the diff.
