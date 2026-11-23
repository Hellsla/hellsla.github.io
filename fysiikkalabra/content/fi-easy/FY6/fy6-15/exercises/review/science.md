VERDICT: PASS
CONTENT-HASH: 250518ce070eda9b
SCOPE: delta answers,comments,md-paragraphs,numbers,reflow,structure,typography,wording from 8abfa7ae354d5e31 base b5600a6

## Blocking

## Polish
- solutions.md:98 — L2-01 Kaava uses $I_\text{lisä}$ without naming it (the current of the added load) — name it in the Periaate or the Kaava line.
- solutions.md:182 — L2-09 Kaava reads "Kohta b): $P = UI$, josta …": the other Kaava steps now go row by row in an aligned block. This one should start the same way ($P = UI$, then $I = P : U$).

## Checked
- Kaava steps (L1-02, L2-01, L2-02, L2-06, L3-01, L3-02, L3-03, L3-04, L3-05; on disk as aligned blocks): each starts from the basic law ($P_k = UI_k$, current sum, $P = RI^2$, $U = RI$, series voltages $U = U_1 + U_2$, $\Delta T = kP$) and simplifies symbolically to the form that is substituted. Every row is correct and the notation matches the brief ($I_\text{s}$, $P_1 + P_2 + \dots$, $I = U : R$).
- One script recomputed every numeric answer from the task data with my own formulas and compared them with answers.py and exercises.json. All agree: 2300 W, 480 W, 22,68 W, 4,84, 2,27 mA, 50 mA, $k = 0{,}2974$ K/W → 20,50 A, 6,167 kΩ.
- New L2-09: $I = 800\,\text{W} : 230\,\text{V} = 3{,}478\,\text{A}$ (key 3.478261, tolerance 0.02). Three significant figures fits the P7 rule (230 V, 800 W). The power-factor-one condition is stated in both the task and the Periaate.
- L2-09 c): the assumption is stated (the panel outlet sits between the distribution board and the loads). At power factor one the two currents are in phase, so the cable segment can carry 16 A + 3,478 A = 19,5 A without the fuse seeing it. The heating ratio $(19{,}478 : 16)^2 = 1{,}48$ is right. The shock hazard is conditional ("jos vaihtosuuntaaja ei lopeta syöttöä"), so it does not overstate the inverter's behaviour.
- L2-09 d): the CE marking is correctly described as the manufacturer's own declaration, not an authority's approval, and the claim is judged false for both "turvallinen" and "sallittu". answers.py comments match the solution.
- Could not open the Tukes page (bot protection). The solution names the hazards "fysiikan perusteella" and does not quote the bulletin, so this is not blocking.
- Removing "(esimerkkiaineisto)" from four captions follows the teacher's no-provenance-badge rule. The data and physics are unchanged.
- Paragraph splits (L1-04, L1-09, L3-03, L3-04, L3-05) change no claim or number.
- Hash identical at start and end.
