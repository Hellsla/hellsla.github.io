VERDICT: PASS
CONTENT-HASH: ebe98a22a12cb8f4

## Blocking

## Polish

## Checked
- Delta (work queue 8g): I read all 13 changed Kaava steps on disk as aligned blocks.
- L1-03 and L2-01 derive $\lambda = \ln 2/T_{1/2}$ from $N = N_0 e^{-\lambda t}$ at $t = T_{1/2}$.
- L1-08 and L3-01 take ln of the decay law to get $t = T_{1/2}\ln(A_0/A)/\ln 2$. L2-05, L3-02 and L3-04 do the same for net rates and for the two-time ratio.
- L2-02 goes from $A = \lambda N$ to $N = A T_{1/2}/\ln 2$. L2-04 adds $m = N m_\text{ydin}$, which gives the mass law.
- L2-06 gives $R_0/4$ at $2T_{1/2}$. L3-03 cancels $A_0$ in the share $p$. L3-05 uses $\lambda_\text{eff} = \lambda_\text{fys} + \lambda_\text{bio}$, which gives $1/T_\text{bio} = 1/T_\text{eff} - 1/T_\text{fys}$. L2-09 subtracts the background $B$ before taking the logarithm.
- All of the algebra above is correct.
- The other changes only split paragraphs. In L1-09 the sentence on graph D was moved to its own paragraph unchanged: $800\,\text{kBq}\cdot e^{-1} = 294\,\text{kBq}$, recomputed. The L2-06 b) explanation and the L2-08 c), d) texts are also split only.
- One script checked the answers: all 22 stored answers agree with answers.py within tolerance.
- The hash was the same at the start and at the end.
