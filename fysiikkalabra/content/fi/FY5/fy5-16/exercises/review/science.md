VERDICT: PASS
CONTENT-HASH: 306fd4f134ec4fd4

## Blocking

## Polish
- solutions.md (L1-01, L1-04, L1-05, L2-01, L2-08, L3-02, L3-03, L1-09, L1-10, Kaava): the new row $I = 2^{\,n}\,I_\text{v}$ is exact only if a 3 dB step doubles the intensity exactly. The lesson calls the 3 dB step a practical rule ($10\,\text{dB}\cdot\lg 2 \approx 3{,}01\,\text{dB}$), and L2-10's Järkevyys says the same. Writing $I \approx 2^{\,n}\,I_\text{v}$ would match the lesson and would also match the $\approx$ that L1-05 and L3-01 already use for the 6 dB step. This is type C, a fair simplification: every answer is unchanged.

## Checked
- The diff rewrites only the Kaava steps and splits some paragraphs into two (L2-04, L3-01's model answer, L2-10). The split paragraphs keep their wording. Sijoitus, answers and tolerances are unchanged.
- Reference time: equal dose means $I\,t_\text{v} = I_\text{v}\,t_0$, so $t_\text{v} = t_0 I_\text{v}/I = t_0/2^{\,n}$. This derives the lesson's formula from the energy-dose principle the lesson states, and it is right.
- L1-02 and L2-01: two equal independent sources give $L - L_1 = 10\,\text{dB}\cdot\lg 2$. Right.
- L1-03, L1-05, L3-01 and L3-03, the inverse square law: $L_1 - L_2 = 20\,\text{dB}\cdot\lg(r_2/r_1) \approx k\cdot 6\,\text{dB}$ with $2^k = r_2/r_1$. Right, and valid in open space, as the Periaate states.
- L1-06 and L2-06, reverberation: a constant decay rate gives $\Delta L/\Delta t = 60\,\text{dB}/T$, so $T = 60\,\text{dB}\cdot\Delta t/\Delta L$. Right.
- L3-02: the protector divides every phase's intensity by $2^{\Delta L/(3\,\text{dB})}$, so $D_\text{korva} = D/2^{\Delta L/(3\,\text{dB})} \le 1$. Right.
- L1-10: $L_\text{korva} = L - \Delta L$ before $n$ is computed. Right.
- Recomputed in one script: 2,0 h; 73,01; 82 (81,98); 4,0 h; 150 %; 16 m; 0,90 s; 125 %; 46 dB; 2,52 h; 75,6 min. All agree with the solutions.
- No safety statement changed. The reference time is still called a reference value and not a safe time.
- Hash 306fd4f134ec4fd4 at the start and at the end.
