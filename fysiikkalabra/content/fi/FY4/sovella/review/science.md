VERDICT: PASS
CONTENT-HASH: 479fb8e6c72f07ad

## Blocking
None. Round-1 item verified:
1. fy4-s1 source_note now says both tables are model data, not measured: in the first the acceleration is constant, in the second it falls with speed because of air resistance, and both carry small noise. This matches answers.py and part e. Fixed.

## Polish
- An intercept of $a_0 = 0{,}43$ (equal to the lowest-speed point) is at the edge of a fair reading.
- Carried over: s2 c $8{,}74$/$8{,}75$; s3 c "pääosin selkänoja".

## Checked
- Round 3: e "Hyväksytään myös" now states $\mu_\text{A} \approx 0{,}022$–$0{,}026$, matching $a_0 = 0{,}43$–$0{,}47$ ($0{,}0260$–$0{,}0219$). Fixed.
- Round-1 polish is applied:
  - e $a_0$ tolerance $5\,\%$ ($0{,}4275$–$0{,}4725$) covers $0{,}43$–$0{,}47$.
  - "virhe on noin viidesosa c-kohdan arvosta" is right ($0{,}006/0{,}030$).
  - Part a says "lähes vakio", which matches the drag curvature ($\pm 0{,}05\,\text{m/s}$, noise-sized).
- e rubric split: graph_read now covers reading $a_0 \approx 0{,}45$, and error_sources covers $\mu_\text{A} \approx 0{,}024$, the $0{,}006$ shift (larger than $0{,}002$, smaller than $0{,}015$) and that repetition does not remove it. Both match the solution. The points are unchanged (e 5, task 19).
- Unchanged from round 1 and still valid:
  - Fit $a_0 = 0{,}449\,\text{m/s}^2$, $k = 0{,}00432\,\text{m}^{-1}$ (model $0{,}00434$), $\mu_\text{A,0} = 0{,}0241$.
  - Run A integrated with drag gives slope $0{,}386 \approx 0{,}39\,\text{m/s}^2$.
  - B's correction $0{,}004$ is less than A's $0{,}006$, so parts d and e are consistent.
  - The extrapolation argument (friction independent of speed, drag going to $0$) is sound and in scope.
- c tolerances cover the accepted ranges. practice.py check OK. The hash was the same at start and end.
