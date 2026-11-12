VERDICT: PASS
CONTENT-HASH: d08caf4c2d0b85dc
SCOPE: delta added-exercise from a5e3a606c3d94d47 base 141dc47a8c70
Mode: delta
Round: 2

## Blocking

## Polish
- solutions.md L1-10 Järkevyys: "puuhun, jonka lämpöarvo on noin $16\,\text{MJ/kg}$". The chapter *Polttoaineet ja lämpöarvo* gives air-dry firewood $15\,\text{MJ/kg}$ (pellets 17). Fix: write "ilmakuivaan polttopuuhun (noin $15\,\text{MJ/kg}$)" so the numbers match between chapters.
- Earlier items (L1-09 "likimain eristetyn", L3-04 c), L1-07 option 3) are still open. They are outside this delta.

## Checked
- Hash d08caf4c2d0b85dc at the start and the end. I judged only the added L1-10 and L2-08.
- L1-10 replaces the round-1 $c\,m\,\Delta T$ task (blocking item resolved). $E = Hm$ is inside the FY2 scope notes and the task text gives it. The task is marked as invented ("Kuvitellaan"). There is no isolated-system claim, and the chemical energy → kinetic + thermal chain is correct.
- L1-10 recomputed: $43\,\text{MJ/kg} \cdot 2{,}0\,\text{kg} = 86\,\text{MJ}$, the same as answers.py (86.0). A table value of 42 or 44 MJ/kg gives 84 or 88 MJ, within ±2,3 % and inside the 4 % tolerance. H = 43 MJ/kg agrees with the fy2-5 heating-value figure (bensiini 43). Two significant figures follow from m = 2,0 kg. The check 86 MJ ≈ 24 kWh is correct.
- L1-10 solution: the formula is given before the substitution, the no-conversion statement is correct, and the order-of-magnitude estimate is a real check.
- L2-08 recomputed: $700 - (300+300) = 100\,\text{J}$, $p = 14{,}29\,\%$, the same as answers.py (14.285714). The answer 14 % is 2,0 % away, inside the 3 % tolerance.
- L2-08 round-1 polish items are fixed. The "puolivälissä" reasoning is gone, the answer is rounded to whole percents with the right reason (readings to 100 J), and the check is the energy sum 600 J + 100 J = 700 J.
- L2-08 physics: the system is isolated (as in the worked example), friction converts mechanical energy into thermal energy and creates none, and the unknown is solved symbolically first. The figure kitka-pylvaat gives A and B as the solution reads them and does not reveal the answer.
