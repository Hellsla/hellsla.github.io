VERDICT: PASS
CONTENT-HASH: 227a47f287a871f2
Mode: delta (Formula steps rewritten as aligned derivations from the basic equations)
Round 1

## Blocking
(none)

## Polish
- solutions.md fy5-13-L3-05 Formula — $v_\text{open} = f_1 \cdot 2L$ and $v_\text{closed} = f_1 \cdot 4L$ appear with no source. The old line derived them from $f_1 = v/(2L)$ and $f_1 = v/(4L)$, and also said $n$ is odd for the closed tube — start the chain from $f_n = n\,v/(2L)$ and $f_n = n\,v/(4L)$ ($n$ odd). The Principle states both, so this is not wrong.

## Checked
- The only changes are the 16 Formula lines; no other line changed (script).
- Each chain now starts from the standing-wave condition ($L = n\lambda_n/2$, or $L = n\lambda_n/4$ with $n$ odd) and $v = f\lambda$, and is solved in symbols to the old end formula the Substitution uses.
- L1-01, L1-02 and L1-08: $f_1 = v/(2L)$ gives 41.0 Hz, 515 Hz and 100 Hz.
- L1-03: $f_1 = v/(4L)$ gives 32.7 Hz.
- L2-02: $v = 4Lf$ gives 340 m/s.
- L2-03: $L = 3v/(2f_3)$ gives 33.3 cm. L2-04: $v = 2Lf/n$ with $n = 4$ gives 60.0 m/s.
- L2-01, L1-09 and L2-09: $\Delta f = (v_2 - v_1)/(2L)$ and $\Delta f = v/(2L)$ give 5.38 Hz, 640 Hz and 31.25 Hz.
- L3-01: $f_\text{c} = f_\text{o}/2$ gives 131 Hz.
- L3-02 and L3-03: adjacent resonances differ by $f_1$ (open) or $2f_1$ (closed); this gives 110 Hz and 0.500 m.
- L2-06: $L_1 = \lambda/4 - e$ and $L_3 = 5\lambda/4 - e$, so $\lambda = L_3 - L_1 = 0.670$ m, $v = 343$ m/s and $e = 0.45$ cm.
- L2-05 and L3-05: the mean of $f_n/n$ with $v = 2Lf_1$ (or $4Lf_1$) gives 122.8 m/s and 331 m/s. The Substitutions, answers and tolerances are unchanged.
- Hash is the same at the start and the end.
