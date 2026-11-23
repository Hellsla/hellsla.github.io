VERDICT: PASS
CONTENT-HASH: 07f5a40aa7a1ccdb

## Blocking
(none)

## Polish
- exercises/solutions.md:535 (L3-06, carried over) — "$4.2 \cdot 10^{2}\,\text{Mpc}$, about $416\,\text{Mpc}$" gives two precisions side by side. The two-figure reason is right. Fix: keep 416 only as the unrounded intermediate result.
- exercises/solutions.md:401–415 — the substitution rows of this solution still use `\frac` while the Kaava rows now use `\dfrac`. This is style only; change it if the convention is meant to cover every aligned row.

## Checked
- Hash 07f5a40aa7a1ccdb (`--exercises --lang en`) at the start (same as the packet's) and at the end.
- Mechanical check of the diff: when `\dfrac` is replaced back by `\frac`, every removed line equals an added line. So the change is purely `\frac`→`\dfrac` in the Kaava rows; no symbol, number, sign or unit changed.
- The physics of the affected Formula steps was re-read and is unchanged and correct:
  - $E = hc/\lambda$.
  - $d = cz/H_0 = c(\lambda-\lambda_0)/(H_0\lambda_0)$, with the small-$z$ condition stated.
  - $t = 1/H_0$, with constant expansion speed stated.
  - $E = 1100\,hc/\lambda_\text{now}$.
  - $d_\text{B} = d_\text{A} v_\text{B}/v_\text{A}$.
  - $Y = m_\text{He}/m_\text{tot}$.
- exercises.json and answers.py are not in the diff, so the answers and tolerances that were verified last round still hold.
