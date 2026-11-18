VERDICT: PASS
CONTENT-HASH: 2e5d53eab6b173d8
SCOPE: delta kaava-step rewrite and paragraph splits, round 1
## Blocking

## Polish

## Checked
- L2-06 Kaava: $x_{0\text{A}} + v_\text{A}t = x_{0\text{B}} + v_\text{B}t \Rightarrow (v_\text{A} - v_\text{B})t = x_{0\text{B}} - x_{0\text{A}}$. The algebra is right and ends in the unchanged $t$ formula. The derivation starts from the two motion equations and the meeting condition, as the house rule asks.
- L3-04 Kaava: $x = k\,x_\text{ohj}$ and $v = k\,v_\text{ohj}$ follow from one scale factor for every length. Substituting $x_\text{ohj} = x_{0,\text{ohj}} + v_\text{ohj}t$ gives $x = x_0 + vt$ with $x_0 = k\,x_{0,\text{ohj}}$, and $t = (x - x_0)/v$ is right. It agrees with the substitution ($0{,}39\,\text{m}$, $0{,}80\,\text{m/s}$, $7{,}0\,\text{s}$). The new $x_0$ and $v$ are the lesson's symbols for the true values.
- L3-05 Kaava: $x_{0\text{R}} + v_\text{R}t = v_\text{P}t - v_\text{P}t_0 \Rightarrow x_{0\text{R}} + v_\text{P}t_0 = (v_\text{P} - v_\text{R})t$. The algebra is right and the $t$ formula is unchanged.
- The rest of the diff (L1-06 Mallivastaus, L3-04 and L3-05 Järkevyys, L1-09 option discussion) only splits paragraphs. Its words, numbers, signs and units are identical.
- The caption marker removal in exercises.json changes no physics.
- No number, answer, unit or tolerance changed, so answers.py needs no recomputation for this delta.
- Hash 2e5d53eab6b173d8 at start and end.
