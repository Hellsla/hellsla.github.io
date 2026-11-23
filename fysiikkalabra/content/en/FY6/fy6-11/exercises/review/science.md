VERDICT: PASS
CONTENT-HASH: 00f8c7564f63ff3c
SCOPE: delta caption-label,md-paragraphs,numbers,paragraphs,reflow,teacher-figure,typography from c8602335ddec9591 base 98218de
Delta from the version I passed (c8602335ddec9591): I judged only the diff in the packet. The packet shows the aligned blocks flattened, so I read the Formula lines in solutions.md on disk.

## Blocking
(none)

## Polish
- lessons/FY6/fy6-11/figures.py:417 (fy6-11-L2-08 option figures): still open from before. The figures label the electric force $\overline{F}_\text{s}$, while the text and feedback use $\overline{F}_\text{e}$. Use one symbol.
- solutions.md:134 (fy6-11-L3-03 Reasonableness): still open from before. "about one fifth of the weight" is inaccurate because $\tan 10^\circ = 0.18$, so the force is nearer one sixth. Write "under a fifth".

## Checked
- solutions.md:25: $W = qEd$ and $W = qU$ give $E = U/d$. This correctly starts from work and the definition of voltage.
- solutions.md:66, 76, 86, 96: each derivation is correct.
  - It starts from $F = qE$ and $E = U/d$.
  - Each one ends in the solved form the unchanged Substitution uses: $qU/d$, $Fd/q$, $qU/(mgd)$ and $F_1 d_1/d_2$.
- Hovering droplet (lines 106 and 229):
  - The balance $F = G$ comes first, as the house rule requires.
  - It leads to $qE = mg$ and $E = U/d$.
  - From these, $q_1U_1 = q_2U_2$ gives $U_2 = U_1 q_1/q_2$, and the Millikan task gets $q = mgd/U$. The $e \approx S/N$ line follows as its own paragraph.
- Electron (line 118): $\Sigma F = ma$ and $eE = ma$ give $a = eU/(md)$. Then $v^2 = 2ad$ gives $v = \sqrt{2eU/m}$. This is correct for a start from rest in vacuum with the weight neglected, and the Principle states those conditions.
- Thread task (line 130): $\Sigma \overline{F} = \overline{0}$ splits into $T\sin\alpha = qE$ and $T\cos\alpha = mg$, which give $q = mg\tan\alpha/E$. The components match the Principle's force list and add no force twice.
- Notation matches the earlier set: $E$, $U$, $d$, $q$, $G$ for weight, overlined vectors.
- Every hunk that only splits paragraphs in L1-06, L1-07, L2-05, L2-07, L2-08, L3-04 and L3-05 keeps the same numbers, signs, units and causal steps.
- Not one Substitution, Answer or answers.py value changed, so the recomputation from my last review still holds:
  - all 19 answers;
  - the Millikan charges $n = 2, 3, 1, 4, 3$ and $e = 1.60 \cdot 10^{-19}\,\text{C}$;
  - L3-05 $y = 1.67\,\text{mm}$.
- The pick-* option figures changed only as teacher-approved images (category teacher-figure). The physics of the options was checked in my previous review.
