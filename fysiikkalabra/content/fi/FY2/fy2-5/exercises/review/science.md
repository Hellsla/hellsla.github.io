VERDICT: PASS
CONTENT-HASH: da86523c46c3ef3e
SCOPE: delta caption-label,md-paragraphs,numbers,reflow,typography,wording from 5ca23e469a626f1f base 5b3ca4f

## Blocking

## Polish
- solutions.md L3-01, L2-05 Kaava/Sijoitus — the Kaava ends with $\Delta m = E(1/H_1 - 1/H_2)$ but the Sijoitus computes the two masses and subtracts them; it is right, and the aligned rows now show every quantity, but substituting into the derived form would follow "substitute into the last symbolic form" exactly (C).
- Earlier items outside this delta (L2-08 104 MJ figures, L1-06 distractor, L2-09 axis wording) are still open.

## Checked
- Hash da86523c46c3ef3e at the start and the end; diff judged against base 5b3ca4f (the version passed as 5ca23e469a626f1f), round-1 changes and the round-2 fixes.
- L2-09 Kaava (my round-1 Blocking item): "energian säilyminen" is gone; it now reads "$E = Hm$ kummallekin polttoaineelle ja energioiden on oltava yhtä suuret, $E_\text{p} = E_\text{b}$", the task's condition, as asked; $m_\text{p} = H_\text{b}m_\text{b}/H_\text{p} = 34{,}4\,\text{kg}$.
- L2-05 and L3-01 Sijoitus are now aligned rows each starting with its quantity ($m_{40}$, $m_{20}$, $\Delta m$; $m_\text{puu}$, $m_\text{öljy}$, $\Delta m$); same numbers and units as before.
- Every other rewritten Kaava starts from $\eta = E_\text{hyöty}/E_\text{sisään}$, $E = Hm$, $E = em$, $P = E/t$ and combines symbolically before substitution; each combination is algebraically right. L2-01 keeps the food-label meaning (energy available to the body).
- exercises.json: only the "Esimerkkiaineisto:" marker removed from captions (teacher-approved); data unchanged and realistic.
- Recomputed in one script with my own formulas: 480 kJ; 578 MJ; 4,47 kg; 5,04 kg; 3,6; 35 MW; 5,63 kg; 18,4 kW; 3313 kg; 937 kg; 34,4 kg: all agree with answers.py and exercises.json within tolerance; no answer, unit or tolerance changed.
