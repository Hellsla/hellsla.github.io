VERDICT: PASS
CONTENT-HASH: 10d12fc7d13ecf10

## Blocking

## Polish
- solutions.md:218 (fy3-5-L1-10): the ±4 % tolerance is explained by "eri taulukoiden arvot poikkeavat hieman". The calorie values differ by under 0,1 % (4,184 against 4,1868 J). The 4 % is really there because the two-figure answer, 11 kJ, lies 3,3 % from 11,37 kJ. Name that reason, or drop the sentence.
- solutions.md:215 (L1-10): the block could end in $\Delta U = N \cdot 4{,}1868\,\text{J} + W$. Likewise L2-01 (line 56) could end in $Q = \Delta U - \tfrac12(F_1+F_2)s$. Both are correct as they stand.
- exercises.json (L2-08 and L2-01): the two tasks use the same figure, with the same straight line from 200 N to 400 N. The physics is consistent (fast compression: $\Delta U = W = 60\,\text{J}$; L2-01: $\Delta U = 45\,\text{J}$, so $Q = -15\,\text{J}$), but the overlap is large. This is a pedagogy matter, not a science one.

## Checked
- I ran answers.py and compared it by script with exercises.json and with my own calculation. All 23 stored answers agree. New L1-10: $(2000 \cdot 4{,}1868 + 3000)/1000 = 11{,}374\,\text{kJ}$, and the rounded 11 kJ is inside the 4 % tolerance. New L2-08: $\tfrac12(200 + 400) \cdot 0{,}20 = 60\,\text{J}$, with 3 % tolerance, which matches "58,2…61,8 J".
- L2-08 physics: "niin nopeasti, ettei lämpöä ehdi siirtyä" gives $Q = 0$, so $\Delta U = W$. The piston does work on the air, so $W > 0$. The figure gives both end points on grid crossings, and its description does not give the area.
- L1-10: 1 cal = 4,1868 J (the MAFY international-table calorie). $Q$ and $W$ are both positive into the system. The units are converted before adding. Correct.
- Every changed Kaava block starts from $\Delta U = Q + W$. It then states the condition on $Q$ or $W$ (insulated, no work, constant-$T$ ideal gas) and solves in symbols. L2-04: $t = (\Delta U - Q)/P$. L3-02: $h = \Delta U/(nmg)$. L3-03: $Q_\text{B} = Q_\text{A} + W_\text{A} - W_\text{B}$, from a state function. L3-05: $Q_\text{ulos} = E_\text{v} - \Delta U$. All are correct.
- L3-01 and L3-04 c): $\Delta U = 0$ is used only with the stated condition, ideal gas at constant temperature.
- L2-07: the answer is now given as 50 J (two figures, as the data), and the stored 50,4 is inside 2 %. The wording is now "siirtävät osan energiasta lämpönä ilmaan", as the guardrails ask.
- L2-05: the prefix "Syventävä tehtävä." changes no physics.
- Caption markers were removed; no data changed. The hash was the same at the start and the end.
