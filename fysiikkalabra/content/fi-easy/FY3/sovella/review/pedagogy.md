VERDICT: PASS
CONTENT-HASH: 51c86aaf9a3b697c

## Blocking
None.

## Polish
- fy3-s3 b, Kaava: still one line. A first row `pV = nRT` with n and T constant would match a and c. Not required.
- fy3-s1 b: the Kaava step does not say that P is the power the water receives. The Periaate step does, so this is minor.

## Checked
- Round 2 change, fy3-s3 c Kaava: it now starts from the tank's two states, `p1 Vs = n1 RT` and `p2 Vs = n2 RT`. Subtracting gives `Δp_s Vs = Δn RT`. The air used, at the depth's pressure, gives `pV = Δn RT`. So `V = Δp_s Vs / p` and `t = V/q` follow without a jump. The earlier polish point (n versus Δn) is closed.
- The step "the ambient pressure cancels in the difference" is stated in the Periaate, so a student can follow why gauge readings are enough.
- The litre is written `\textsf{l}` consistently in b and c. The `l/min` unit in the task data matches it. The numbers agree with answers.py (14.7 l, 725 l, 36 min, 89 min).
- The tasks are unchanged and still demand independent application:
  - the situations are authentic (a collector's data table, a pressure-cooker table, a dive);
  - no part names the model;
  - the parts rise in demand;
  - the rubrics are specific and give no points for irrelevant things.
- The common mistakes are real: ambient pressure left out, Celsius used in the gas law, the wrong temperature in b, and the tank compared with surface pressure.
- The d-part model answers say in which direction each assumption changes the result.
- The workload suits a 2 op course. The three tasks differ from each other (data and graph, phase change, gas law).
- I did not judge `docs/coverage/FY3.md`, because the packet does not carry it.
