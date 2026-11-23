VERDICT: PASS
CONTENT-HASH: b4a317e3e12c35cd

## Blocking

## Polish

## Checked
- The diff only changes `\frac` to `\dfrac` in the Kaava rows of 12 solutions. In every changed line, the symbols, the numbers and the order of the rows are the same as before. No Kaava row has a `\frac` left.
- These chains are unchanged and still correct:
  - $E = hf$, $f = c/\lambda$, so $E = hc/\lambda$
  - $d = v/H_0 = cz/H_0 = c(\lambda - \lambda_0)/(H_0\lambda_0)$
  - $t = d/(H_0 d) = 1/H_0$
  - $E = 1100\,hc/\lambda_\text{nyt}$
  - $d_\text{B} = d_\text{A}v_\text{B}/v_\text{A}$
  - $Y = 2n/(n + p)$
  - $H_0 = \Delta v/\Delta d$ and $H_0 = \sum dv/\sum d^2$
  - $d = 0{,}10\,c/H_0$
- The six `\frac` left in the file are in the L2 Sijoitus rows (lines 389–404), outside this change. Recomputed:
  - $6{,}6/656{,}3 = 0{,}010056$
  - $14{,}6/486{,}1 = 0{,}030035$
  - ratio $2{,}987$

  All agree with the solution.
- The small-$z$ condition for $v = cz$ is still stated next to the change (lines 110 and 437).
- Hash b4a317e3e12c35cd at the start and at the end.
