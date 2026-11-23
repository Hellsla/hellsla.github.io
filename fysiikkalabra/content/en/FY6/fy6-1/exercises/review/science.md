VERDICT: PASS
CONTENT-HASH: 510344e7120d02fd
SCOPE: delta md-paragraphs,numbers,teacher-figure,typography,wording from 6a32e9655e538bee base 98218de

## Blocking

## Polish
- solutions.md fy6-1-L2-06 b) — still "No current flows through the lamp" while the Principle says "almost all of the current flows through the wire" (C-level, slightly inconsistent) — write "practically no current flows through the lamp".
- solutions.md fy6-1-L3-05 Formula — the new aligned block uses $t$ both for the counting time in $\tfrac{N}{t}$ (1 s) and for the travel time $t = \tfrac{s}{v}$ (14 h) — name the second $t_\text{travel}$ or say "per second" for the first.
- solutions.md fy6-1-L3-04 Formula — $Q = It$ and then $Q = \sum I_k t$ in one block reuse $Q$ for the general definition and the total; fine at this level, but "$Q_\text{total}$" would read more clearly.

## Checked
- Diff only: every Formula line rewritten as an aligned block starting from the definition ($I = Q/t$, $U = E/Q$, $Q = Ne$) and solving for the unknown; each block is algebraically the same as the one passed, no new law, no condition dropped.
- L2-02/L1-08 $N = It/e$, L2-04 $Q = I_1t_1 + I_2t_2$, L2-08 $E = UQ$ with rectangle + triangle area, L3-05 $v = I/(ne)$: derivations correct.
- All numbers in the changed lines recomputed in one script with my own formulas (20, 1800, 30, 108 C, 9.99·10¹⁷, 40 kJ, 11 C, 8.0 h, 1.2, 9.36·10¹⁹, 22.8 C / 0.38 A, 0.310/0.306 A, 12.5 Wh, 3.35 Ah, 3.73 V, 45 kJ, 7.2 %, 0.0192 mm/s, 14.5 h, 140 J): all agree.
- answers.py and exercises.json unchanged since the version passed.
- Paragraph splits keep every causal step (current not used up, electrons opposite to conventional current, signal vs drift, short-circuit warning).
- Picture fy6-1-kaavio-malli is a teacher-approved figure; its code still matches the model answer (cells in series, + at top, current arrow from +).
- Hash read at start and end: unchanged.
