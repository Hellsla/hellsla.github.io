VERDICT: PASS
CONTENT-HASH: 89d7d344021e07ad
SCOPE: delta md-paragraphs,numbers,paragraphs,reflow,typography from 3f48bc8fead4207e base e238aa9

## Blocking

## Polish
- solutions.md:204 (L3-05 Kaava) — $I_\text{LED} = f(U_\text{D})$ brings in function notation that the lesson does not use. Fix: write it in words ("LEDin virta luetaan ominaiskäyrän taulukosta") (C).
- The earlier Polish items (L1-06 causal wording, L2-09 comparison with the lesson's panel, the ex-led description) are not in this diff. They still stand.

## Checked
- Every new Kaava block starts from Kirchhoff's voltage law $U = U_R + U_\text{D}$ (or $U_R + 2U_\text{D}$, $U_R + 3U_\text{D}$) together with Ohm's law $U_R = RI$. It is then solved to $R$ or $I$, as the lesson's Kaava section does. In the reverse-bias task $I = 0$ is correctly set before $U_\text{D} = U$.
- The efficiency blocks start from $\eta = \tfrac{P_\text{hyöty}}{P_\text{otettu}}$ with $P_\text{otettu} = GA$ and end at the lesson's $\eta = \tfrac{P}{GA}$. In L3-04, $\eta = \tfrac{E}{HA}$ is the same ratio for energies, and $E_\text{vuosi} = \eta A\sum H$ follows from it.
- L2-06 and the LED-strip share: $P = UI$, $R = \tfrac{U}{I}$ for the load, and share $= \tfrac{U_RI}{UI} = \tfrac{U-3U_\text{D}}{U}$. All are correct.
- I recomputed every substitution near the diff in one script: 95 Ω, 8,3 mA, 250 Ω, 20,3 %, 0,36, 49,3 W and 5,86 Ω, 25 %, 16,7 %, 207 Ω, 387 Ω, 4683 kWh and 87,7 %, and 13,8 mA. All agree.
- The paragraph splits in L3-04 (a/b/c) and L3-05 (c, Järkevyys) keep the same sentences and numbers in the same order.
- exercises.json: only presentation changed.
- Scope: components only.
- The hash was the same at the start and at the end.
