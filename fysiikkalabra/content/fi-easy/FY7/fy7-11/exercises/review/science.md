VERDICT: PASS
CONTENT-HASH: 494809aa821182e9

## Blocking

## Polish

## Checked
- Delta: the packet shows the Kaava steps of L1-04, L1-05, L2-01, L3-01 and L3-03 flattened. On disk (solutions.md:35, 45, 55, 96, 186) each is an aligned block with correct row breaks. Each block is identical to the passed Finnish one, including the L1-05 split row `&+ (180^\circ-2\beta)+(\alpha-\beta)`.
- Derivations are right. L1-04: $\delta = (\alpha_1-\alpha_2)+(\alpha_4-\alpha_3)$ with $\alpha_2+\alpha_3 = A$ gives $\delta = \alpha_1+\alpha_4-A$. L1-05: $\delta_\text{k} = 180^\circ+2\alpha-4\beta$, so $\theta = 4\beta-2\alpha$. L2-01: $\Delta t = L(n_\text{v}-n_\text{p})/c$. L3-03: $\beta = (\theta+2\alpha)/4$ and $n = \sin\alpha/\sin\beta$.
- Each block ends in the form its Sijoitus step uses. Sijoitus, Vastaus, keys and tolerances are unchanged.
- Recomputed: $42{,}0^\circ$; $265\,\text{ns}$; L3-01 $\Delta\delta = 0{,}9659^\circ$, matching the stated exact value $0{,}966^\circ$ (the $0{,}98^\circ$ from rounded intermediates is explained in the answer).
- Model answers of L3-02 (rainbow edges), L3-03 and L3-05 were split into paragraphs only. Every sentence and number is kept.
- exercises.json: no "esimerkkiaineisto" left. The removal makes no data false: the values are given as typical properties, not as measurements.
- Hash 494809aa821182e9 at the start and at the end.
