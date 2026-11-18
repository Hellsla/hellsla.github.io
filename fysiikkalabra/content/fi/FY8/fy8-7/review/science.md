VERDICT: PASS
CONTENT-HASH: 3edfe13d49a1760c

## Blocking

## Polish

## Checked
- Round 2 blocking item resolved. In fi, en and fi-easy inquiry.json, the feedback for the correct option and for distractor 2 now gives $633\,\text{nm}$ and $\approx 1{,}96\,\text{eV}$, the same as the prompt. No stale 650 nm, 656 nm or 1,89 eV text is left in the Kertaa item in any language.
- I recomputed hc/λ with h = 6,626·10⁻³⁴ Js, c = 2,998·10⁸ m/s and e = 1,602·10⁻¹⁹ C: 633 nm gives 1,959 eV, which rounds to 1,96 eV. lesson-answers.py `kert-633-eV` gives 1,958921, and the two agree.
- The round 2 polish item is resolved. The hydrogen `kert-656-eV` line and its comment were removed, and `mis-650` and `mis-405` (1,91 eV and 3,06 eV) are unchanged and still right.
- The physics is right. The 633 nm red line of a He-Ne laser comes from a transition in neon. The prompt treats E₁ as a general lower level, not the ground state, and that is consistent with the line.
- There is exactly one correct option, "energia on tasojen erotus $E_2 - E_1$". Distractor 2 (the energy of the upper level) is wrong, and its feedback says so with the right relation $hf = E_2 - E_1$.
- Distractor 3: spontaneous emission goes in random directions, and its feedback fits the prompt. Distractor 4: spontaneous decay in about 10⁻⁸ s is the typical order of magnitude, and its feedback is right in all three languages.
- en and fi-easy say the same physics and numbers as fi, with the decimal point in en and the decimal comma in fi and fi-easy.
- The content hash was the same at the start and at the end.
