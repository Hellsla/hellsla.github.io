VERDICT: PASS
CONTENT-HASH: 3b8667a9b79b6a03

## Blocking

## Polish
- exercises/solutions.md (L2-05) — the solution now gives $2{,}270\,\text{eV}$ (four figures) while exercises.json shows the answer 2.27; consider answer 2.270 so the shown answer and the solution agree (inside tolerance either way).

## Checked
- Round-1 blocking items fixed: L2-05 now four significant figures, justified by $546{,}3\,\text{nm}$ and the constants ($hc/\lambda = 2{,}2698\,\text{eV} \to 2{,}270$); L2-07 names only the limiting datum, the reading $16{,}4\,\text{mm}$ ($\pm 0{,}05\,\text{mm} \cdot 12\,\text{nm/mm} \approx 0{,}6\,\text{nm}$, so $497\,\text{nm}$ stands).
- Recomputed in one script: L2-05 2.2698 eV, L2-07 $12{,}01 \cdot 16{,}4 + 299{,}6 = 496{,}6\,\text{nm}$; answers and tolerances unchanged and consistent.
- New L2-09: blue Hg line read at $436\,\text{nm}$ (figure lamp-spectrum draws 405/436/546/577/579 nm to scale); $hc/\lambda = 2{,}844\,\text{eV}$, answer 2.84, tolerance 3 % covers a reading a few nm off; description does not give the energy.
- New L3-06: $3{,}0617 - 2{,}2711 = 0{,}7907\,\text{eV}$ = answers.py; shared upper level 7³S₁ stated in the task; Hg 6³P₂ − 6³P₀ = $5{,}461 - 4{,}667 = 0{,}794\,\text{eV}$ confirms; two-figure reason (difference of near-equal energies) sound; model answer for c) right (alternative transitions, $E_\text{y}$ cancels).
- "lämmöksi" → "sisäenergiaksi" in L3-03, L3-05 task and solutions: consistent with the guardrail (heat is energy in transfer); no number changed.
- Raw source of L2-09 Sijoitus checked: separate display rows ($hc$, $E$ in J, $E$ in eV), not one merged chain.
- Hash identical at start and end.
