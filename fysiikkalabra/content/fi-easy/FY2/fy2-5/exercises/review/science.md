VERDICT: FAIL
CONTENT-HASH: 514101bffd1fe463

## Blocking
- solutions.md:269 (fy2-5-L2-09, new task), Kaava: "energian säilyminen $E_\text{p} = E_\text{b}$" names the wrong principle (A). Burning 12 kg of petrol and burning wood are two alternatives, not one process. The two energies are equal because the task asks for the same energy, not because energy is conserved. Labelling this as conservation leaves a wrong picture of what conservation means. The Periaate is right: "Energioiden pitää olla yhtä suuret". Fix: "**Kaava:** $E = Hm$ kummallekin polttoaineelle. Energioiden pitää olla yhtä suuret, $E_\text{p} = E_\text{b}$, joten $H_\text{p}m_\text{p} = H_\text{b}m_\text{b}$ ja $m_\text{p} = \dfrac{H_\text{b}m_\text{b}}{H_\text{p}}$".

## Polish
- exercises.json:149 (fy2-5-L2-05, unchanged and outside this delta): "Tehollinen lämpöarvo on se energia, joka puusta oikeasti saadaan lämmitykseen" mixes up the heating value with the useful energy. The heating value leaves out only the condensation heat; the boiler's losses come on top of it, and the lesson's own Kaava says so. Fix: "Tehollisessa lämpöarvossa ei ole mukana savukaasun vesihöyryn tiivistymislämpöä."

## Checked
- I recomputed these in one script, and answers.py matches every numeric answer in exercises.json within its tolerance:
  - L3-01: $120/15 - 120/40{,}6 = 5{,}04 \approx 5{,}0\,\text{kg}$; ±2 % accepts 4,94–5,15.
  - L3-04: oil $47\,880/(0{,}90 \cdot 40{,}6) = 1310 \approx 1300\,\text{kg}$; mass ratio $2{,}53$; $40{,}6/17 = 2{,}39$; $2{,}39 \cdot 0{,}90/0{,}85 = 2{,}53$. The pellet answer of 3313 kg is unchanged.
  - L3-05: oil $36\,000/(0{,}90 \cdot 40{,}6) = 985 \approx 990\,\text{kg}$; the answer 938 kg is unchanged.
  - L1-09 (new): $26{,}7 \cdot 0{,}50 = 13{,}35\,\text{MJ}$; ±4 % accepts 12,8–13,9, so the rounded 13 MJ and neighbouring table values pass. The LHV is the right value for burning, and the hint names MAFY's table. "Noin kaksi kolmasosaa bensiinistä" checks: $26{,}7/43 = 0{,}62$.
  - L2-09 (new): $43 \cdot 12/15 = 34{,}4\,\text{kg}$; ±2 % accepts 34. `fy2-5/lampoarvot` prints 43 and 15 at the bar ends and does not give the answer away.
- Light fuel oil $40{,}6\,\text{MJ/kg}$ (MAFY) is now the same in the L3-01, L3-04 and L3-05 tasks, their tables, the solutions and answers.py. This follows P8.
- The rewritten Kaava lines (bread slice, pellets, petrol, food rations, peat plant, damp wood, pellet burner, L3-04, L3-05) start from $\eta = E_\text{hyöty}/E_\text{sisään}$, $E = Hm$, $P = E/t$ and $e = E/m$, combine them symbolically and substitute into the final form. All intermediate values are right: 0,48 MJ, 578 MJ, 4,465 kg, 3,6, 35 MW, 5,62 kg and 18,4 kW.
- Removing "Esimerkkiaineisto:" from the captions is acceptable. The L2-05, L3-04 and L3-05 task texts still say "esimerkkiaineisto", and L2-07's caption keeps "Esimerkkimittaus".
- Hash 514101bffd1fe463 at the start and at the end.
