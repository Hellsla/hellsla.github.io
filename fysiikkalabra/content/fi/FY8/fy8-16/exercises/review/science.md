VERDICT: PASS
CONTENT-HASH: 1530a872a68fd59f
SCOPE: delta md-paragraphs,numbers,reflow,typography from 35eb2ff6a77795e8 base 64d4935

## Blocking

## Polish

## Checked
- Hash 1530a872a68fd59f at the start and at the end.
- The diff only changes `\frac` to `\dfrac` in the Kaava steps of L1-05, L2-01, L2-02, L2-03, L2-04, L3-01, L3-03, L2-05, L2-09, L3-05, L2-06 and L3-06. No symbol, number, operand or line order changed, which settles the earlier Polish item. No Kaava lead-in line still uses inline `\frac`.
- The physics carries over from the previous PASS unchanged:
  - $z = \tfrac{\lambda - \lambda_0}{\lambda_0}$ and $v = cz$ (at small $z$), with $v = H_0 d$ giving $d = \tfrac{cz}{H_0}$.
  - $t = \tfrac{1}{H_0}$.
  - $E = \tfrac{1100\,hc}{\lambda_\text{nyt}}$.
  - $d_\text{B} = d_\text{A} \tfrac{v_\text{B}}{v_\text{A}}$.
  - $Y = \tfrac{2n}{n+p}$.
  - $H_0 = \tfrac{\sum dv}{\sum d^2}$.
  - $d = \tfrac{0{,}10\,c}{H_0}$.
  - $k = 1 + z$.
- exercises.json and answers.py are untouched by the diff.
