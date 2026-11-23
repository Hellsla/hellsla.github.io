VERDICT: PASS
CONTENT-HASH: add6ed1f8827f58d
none

## Blocking

## Polish
- content/en/FY5/fy5-1/exercises/solutions.md:169 — L2-06 Formula splits the last row by hand inside the bracket (`m_B r_B \\ &\qquad - m_C r_C`) — write it on one row and let the layout wrap it (same as the Finnish).

## Checked
- Hash the same at the start and the end (add6ed1f8827f58d). Judged the diff against the files on disk (the packet's diff flattens the aligned blocks; on disk they are proper `aligned` rows).
- Every rewritten Formula starts from the basic equation and ends in the form Substitution uses: L1-01, L1-02, L1-03, L1-05, L2-01, L2-02, L2-03, L2-04, L2-05, L2-06, L2-07, L3-01, L3-02, L3-03, L3-04, L3-05, L1-10. Algebra right ($F = M/d$, $r = M/F$, $F = M/(d\sin\alpha)$, $r_2 = F_1r_1/F_2$, $F_\text{chain} = F_\text{pedal}d/R$, $M = F(d-e)$, $M = Fd\cos 45^\circ$, $M = F\,OP$).
- L2-07: $d$ and $e$ now defined before the block, consistent with the Given line; $r = 0.240\,\text{m}$, $M = 21.6\,\text{Nm}$.
- Signs agree with the Principle in L2-03 ($+F_1r_1$, $-F_2r_2$), L2-06 and L3-03 (both anticlockwise, $2Fd$).
- Recomputed all 17 answers in one script: 37.5; 9.6; 150; 0.30; 17.21; 29.75; 7.0; 230.9; 25.1; 0.1177; 21.6; 61.87; 1.0; 48; 70.875 (787.5 N, 47.25, 31.5); 165.5 (A 240, C 200); 15. answers.py and exercises.json agree; units and tolerances unchanged.
- Paragraph splits change no number or wording; caption marker removal changes no data.
- Structure and numbers identical to the Finnish set.
