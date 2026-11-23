VERDICT: PASS
CONTENT-HASH: a44fd4204ae2b916
Mode: delta (Formula steps rewritten as aligned derivations from the basic equations)
Round 1

## Blocking
(none)

## Polish
- solutions.md fy5-16-L1-01, L2-01, L2-02, L2-07, L3-01, L3-04, L3-05, L1-09, L2-09 Formula — the new row $I = 2^{\,n} I_\text{ref}$ with $n = (L-L_0)/(3\,\text{dB})$ is exact only for steps of $10\lg 2 = 3.01\,\text{dB}$. The set itself uses 3.01 dB in L1-02, and the reference time $t_\text{ref} = t_0/2^{\,n}$ is the 3 dB exchange rule — write $I \approx 2^{\,n} I_\text{ref}$ (as L1-03 and L2-03 already use $\approx$ for 6 dB). The difference (0.3 %) does not affect any answer.

## Checked
- All 15 Formula diffs: the dose chains now start from the equal-energy condition $I\,t_\text{ref} = I_\text{ref}\,t_0$, which gives $t_\text{ref} = t_0/2^{\,n}$. The level chains start from $L = 10\,\text{dB}\cdot\lg(I/I_0)$, in which $I_0$ cancels in differences. All of them reach the old end formulas.
- L1-02: $L_1 + 10\,\text{dB}\lg 2$ gives 73 dB. L2-01: $+3$ dB, then 4.0 h.
- L1-03, L2-03, L3-02, L3-05: point source, $I \propto 1/r^2$, so $\Delta L = 20\,\text{dB}\lg(r_2/r_1) \approx k\cdot 6$ dB for $r_2/r_1 = 2^k$. This gives 82 dB, 16 m and 46 dB; the 46 dB adds the second equal source (+3 dB).
- L2-04 and L2-05: a constant decay rate, $\Delta L/\Delta t = 60\,\text{dB}/T$, gives $T = 0.90$ s.
- L2-02 and L3-01: $n = 3$ gives 1.0 h and 150 %. The dose is $1 + 0.25 = 125$ %, and $n = -1$ gives 16 h correctly.
- L3-04: the protector lowers the intensity by $2^{\Delta L/3\,\text{dB}}$, so the dose is divided by the same factor; condition $D_\text{ear} \le 1$.
- L1-09: $8\,\text{h}/2^{5/3} = 2.52$ h. L2-09: 93 dB gives 75.6 min. L2-10: the exact $10^{(L_2-L_1)/10\,\text{dB}}$ form is right.
- The non-formula hunks are only paragraph splits (script: identical text). The Substitutions, answers and tolerances are unchanged.
- Hash is the same at the start and the end.
