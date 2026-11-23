VERDICT: PASS
CONTENT-HASH: 260b819a49c95404
SCOPE: delta md-paragraphs,numbers,typography from 0b42b5134a5c6175 base 5b3ca4f

## Blocking
- none

## Polish
- solutions.md fy6-7-L2-06, L2-07, L3-05 Kaava — still one inline line joined with "ja" rather than the stacked derivation of the other tasks; the physics is right, so it is only a matter of form.

## Checked
- Rewritten Kaava blocks (L2-01, L2-02, L2-03, L2-04, L3-01, L3-02, L3-03, L1-07, L2-05, L3-04, L2-08) start from $E = Pt$, $P = UI$, $U = RI$, $K = aE$ and derive the form substituted; every row is right. L3-01's $E_2 = E_1$ (same energy, different power) and L3-02's $K = K_\text{perus} + aE$ are the right principles.
- The hash changed during the review (4fe3e018 → 260b819a): L3-04's row $S = aE_\text{varaaja}$, which read as a cost rather than a saving, was replaced by $K_\text{kallis} = a_\text{kallis}E$, $K_\text{halpa} = a_\text{halpa}E$, $S = K_\text{kallis} - K_\text{halpa}$. That is correct, and I judged this version.
- Recomputed in one script (my formulas vs answers.py vs exercises.json): 0,80 kWh; 480,24 kJ; 6,70 €; 75,92 kWh; 7,33 h; 371,3 kWh; 4,99 kWh; 0,93 €; 299,3 kWh; 2,5 kWh → 0,45 €. All agree.
- Paragraph splits in L2-09 Periaate and part d) change no claim: $P_\text{ka} = kP_\text{käy}$ and $k \approx 0{,}39$ at $100\,\text{W}$ are still marked as an order of magnitude, not as source data.
- Content hash checked at start and end (redone for the mid-review edit).
