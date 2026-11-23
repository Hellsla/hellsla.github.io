VERDICT: PASS
CONTENT-HASH: f8a8e923c8dbc625
SCOPE: delta caption-label,md-paragraphs,numbers,paragraphs,reflow,teacher-figure,typography from b380572990b00c2b base 98218de
Delta review of the Kaava steps rewritten to start from the basic equations (queue 8g) and of the model answers split into paragraphs. Categories and base come from `reviews.py` scope for science.

## Blocking

## Polish

## Checked
- The hash was f8a8e923c8dbc625 at the start and at the end. The packet's diff shows the aligned blocks flattened, so I read the actual Kaava lines on disk (solutions.md:25–126, :223). They are proper `aligned` blocks.
- The chains start from the right basics: $W = qEd = qU$ for $E = U : d$; $F = qE$; $F = G$ with $qE = mg$ for hovering drops; $\Sigma F = ma$ for the electron; $\Sigma \overline{F} = \overline{0}$ with the tension components $T\sin\alpha = qE$ and $T\cos\alpha = mg$ (no double counting). Each is solved in symbols before substitution, and every algebraic step is right.
- L2 drop task: $q_1U_1 = mgd = q_2U_2$ gives $U_2 = U_1 q_1 : q_2$, which is right because $m$, $g$ and $d$ are fixed.
- The paragraph splits (L1-06 model answer, L2-07 parts a–c, L2-08 figure explanations, L3-04, L3-05 principle and parts) keep every sentence, number and causal step. The physics is unchanged.
- The notation matches the brief: $\overline{E}$, $\overline{F}$, $E = U : d$, $F = qE$.
- I recomputed in one script: 15 000 V/m; 2,0 mN; 15 kV; F : G = 20,4; 0,45 mN; 337,5 V; 4,19·10³ km/s; 23 nC; q₁ = 3,20·10⁻¹⁹ C. All agree with the solutions.
- The teacher-approved pick figures and the caption-marker removal are carried (teacher-figure, caption-label). No answer, tolerance or option correctness changed.
