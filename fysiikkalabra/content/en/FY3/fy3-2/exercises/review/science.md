VERDICT: PASS
CONTENT-HASH: 9aedda62aa253b0d

## Blocking

## Polish
- solutions.md (fy3-2-L3-01, L2-09, Formula): the blocks stop at $F_\text{avg} = W/s$ and do not substitute the work expression, so the house rule "simplify symbolically to the end" is not fully met. A last row would fix it: $F_\text{avg} = \dfrac{\tfrac12 F s_1 + F s_2 + \tfrac12 F s_3}{s}$, or $\dfrac{F_1 s_1 + F_2 s_2}{s}$ for L2-09. The physics is right.
- solutions.md (fy3-2-L3-04, Formula): $W = \tfrac12 F s$ holds for a force that grows linearly from zero, which part a) establishes. Writing it as $F_\text{max}$ and $s_\text{max}$ would make clear which values are meant.

## Checked
- The diff changes only the Formula steps and splits paragraphs. I compared the non-Formula text with whitespace removed: it is identical before and after.
- Every Formula block starts from its basic law ($W = Fs$, $P = W/t$, $F = G = mg$ for a slow lift, the trapezium area) and solves for the asked quantity in symbols. Checked: L1-02, L1-04, L1-05 ($P = Fvt/t = Fv$), L1-07, L2-01, L2-02, L2-03, L2-04, L2-05, L2-06, L2-07, L3-01, L3-02, L3-03, L3-04, L3-05, L1-09 ($W = \rho V g h$) and L2-09.
- L3-02: writing $\Delta U = n m g h$ assumes all the work becomes internal energy, as the principle states. L3-05: $P = Fv$ is used with a constant speed and $F = G$.
- Recomputed in one script: L3-01 $30\,\text{N}$, L3-03 $45.4\,\text{min}$, L2-06 $229.8\,\text{W}$. Each matches.
- The FY3 scope holds: no $E_\text{k}$, no $\cos\alpha$ and no Newton's laws.
- The hash was the same at the start and the end.
