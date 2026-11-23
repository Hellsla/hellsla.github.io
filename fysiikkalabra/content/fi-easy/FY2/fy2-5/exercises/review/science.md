VERDICT: PASS
CONTENT-HASH: b1a4001c20ea8979
SCOPE: delta answers,comments,md-paragraphs,numbers,reflow,structure,teacher-figure,typography,wording from 02606fa88d01b0b2 base c7f5e91

## Blocking

## Polish
- exercises.json:149 (fy2-5-L2-05, unchanged) — "Tehollinen lämpöarvo on se energia, joka puusta oikeasti saadaan lämmitykseen" mixes up the heating value with the useful energy. The boiler's losses come on top of the heating value. — Fix: "Tehollisessa lämpöarvossa ei ole mukana savukaasun vesihöyryn tiivistymislämpöä."
- solutions.md (L2-05, L3-01) — the Kaava ends in $E\left(\frac{1}{H_1} - \frac{1}{H_2}\right)$, but the Sijoitus computes the two masses separately. Both are correct. — Fix (optional): add a row $\Delta m = 120\,\text{MJ}\left(\frac{1}{15} - \frac{1}{40{,}6}\right)\frac{\text{kg}}{\text{MJ}}$, so that the substitution goes into the final form.

## Checked
- L2-09 Kaava (round-2 fix): equality is now justified by "energioiden on oltava yhtä suuret" and no longer by conservation. $H_\text{p}m_\text{p} = H_\text{b}m_\text{b}$ gives $43 \cdot 12/15 = 34{,}4\,\text{kg}$, and the answer 34 kg is inside ±2 %. `fy2-5/lampoarvot` prints 43 and 15 and does not give the answer away.
- L2-05 and L3-01 Sijoitus (round-2 fix): each is now an aligned block with one equation per row. $m_{40} = 19{,}23$, $m_{20} = 13{,}61$, $\Delta m = 5{,}62\,\text{kg}$; $m_\text{puu} = 8{,}0$, $m_\text{öljy} = 2{,}96$, $\Delta m = 5{,}04\,\text{kg}$.
- Light fuel oil 40,6 MJ/kg (MAFY) is the same in the L3-01, L3-04 and L3-05 texts, the table, the solutions and answers.py. Recomputed: oil 1310 kg and 985 kg; the mass ratio $2{,}53 = 2{,}39 \cdot 0{,}90/0{,}85$; 710 kg extra at $\eta = 0{,}70$; 3313 kg, 937 kg and 2824 kg.
- L1-09 (ethanol): the MAFY LHV of 26,7 MJ/kg suits burning, and $26{,}7 \cdot 0{,}50 = 13{,}35\,\text{MJ}$. The ±4 % tolerance covers neighbouring table values.
- Rewritten Kaava lines (bread slice, pellets, petrol, rations, peat plant, burner, L3-04, L3-05) start from $\eta = E_\text{hyöty}/E_\text{sisään}$, $E = Hm$, $P = E/t$ and $e = E/m$, combine symbolically and substitute into the final form: 0,48 MJ, 578 MJ, 4,465 kg, 3,6, 35 MW and 18,4 kW.
- answers.py matches all 20 numeric answers within tolerance (one script, `python -I`).
- Hash b1a4001c20ea8979 at the start and at the end.
