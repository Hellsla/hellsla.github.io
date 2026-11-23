VERDICT: FAIL
CONTENT-HASH: 4c8bf127299ad252
SCOPE: delta (Stop and think boxes only, git diff origin/main)

1. Blocking:
- B (internal consistency/order): the `mirror` and `torus` figures were moved out of their own sections and up into the Lorentz-force section (lines 125-143), just after the `lorentz` figure. The mirror figure shows v_par, v_perp, the pitch angle theta, B_0, B_max and the condition sin^2 theta >= B_0/B_max. None of these is defined until "Along the field" (line 163), and the torus idea comes only at line 182. The reader sees both figures before the text that explains them, far from their paragraphs. Fix: put `mirror` back after "...escape through the ends." with the v_par box after it, and `torus` back after "...so there are no ends." with the ring box after it. The F = 0 box stays after the `lorentz` figure.
2. Checked: box 1 (F = |q|vB sin alpha = 0 along the field) is correct and supported by lines 11-15. Box 2 (v_par shrinks: no work is done, so E_k is constant and more of the motion goes into circling) is correct at this level (C) and follows lines 17 and 165. Box 3 (closed field lines have no ends) follows line 184. Markup is well formed. Hash is the same at start and end.
