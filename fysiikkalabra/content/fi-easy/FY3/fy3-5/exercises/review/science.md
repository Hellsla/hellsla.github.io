VERDICT: PASS
CONTENT-HASH: 10d12fc7d13ecf10

## Blocking

## Polish
- solutions.md:218 (fy3-5-L1-10): the ±4 % tolerance is explained by "eri taulukoiden arvot poikkeavat hieman". The calorie values differ by under 0,1 %. The real reason is that the two-figure answer, 11 kJ, lies 3,3 % from 11,37 kJ. Name that reason, or drop the sentence.
- solutions.md:215 (L1-10) and 56 (L2-01): the blocks could end in $\Delta U = N \cdot 4{,}1868\,\text{J} + W$ and $Q = \Delta U - \tfrac12(F_1+F_2)s$. Both are correct as they stand.
- exercises.json (L2-08 and L2-01): the two tasks use the same figure and the same line. The physics is consistent, but the overlap is large. This is a pedagogy matter.

## Checked
- I ran answers.py and compared it by script with exercises.json and with my own values. All 23 agree.
- New L1-10: $(2000 \cdot 4{,}1868 + 3000)/1000 = 11{,}37\,\text{kJ}$, and the rounded 11 kJ is inside 4 %. Both $Q$ and $W$ are positive into the system, and the units are converted before adding.
- New L2-08: $\tfrac12(200 + 400) \cdot 0{,}20 = 60\,\text{J}$, inside 3 %. "Ei lämpöä ehdi siirtyä" gives $Q = 0$, so $\Delta U = W > 0$. The figure gives both end points on grid crossings, and its description does not give the area.
- Every changed Kaava block starts from $\Delta U = Q + W$, states the condition on $Q$ or $W$, and solves in symbols. L2-04: $t = (\Delta U - Q)/P$. L3-02: $h = \Delta U/(nmg)$. L3-03: $Q_\text{B} = Q_\text{A} + W_\text{A} - W_\text{B}$. L3-05: $Q_\text{ulos} = E_\text{v} - \Delta U$. All correct.
- L3-01 and L3-04 c): $\Delta U = 0$ is used only with the stated condition, ideal gas at constant temperature.
- L2-07: the answer is 50 J (two figures), and the stored 50,4 is inside 2 %. The wording "osan energiasta lämpönä" follows the guardrails.
- The L2-05 prefix and the caption markers change no physics. The hash was the same at the start and the end.
