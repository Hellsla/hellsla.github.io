VERDICT: PASS
CONTENT-HASH: d1c6e6bd72420c6b

## Blocking

## Polish
- exercises/solutions.md (every changed Kaava, e.g. the L1 photon-energy and Hubble-distance tasks) — the display block opens mid-sentence after "ja $$". The physics is right. Whether it renders cleanly is for the visual reviewer to look at.

## Checked
- Hash d1c6e6bd72420c6b (`reviews.py hash fy8-16 --exercises --lang fi-easy`) at the start and the end.
- `git diff origin/main`: only solutions.md changed, and every removed line is a `**Kaava:**` line. Answers, answers.py, tolerances and the Sijoitus steps are unchanged.
- Photon energy $E = hf$, $f = c/\lambda$ gives $hc/\lambda$. The CMB photon energy $E = 1100\,hc/\lambda_\text{nyt}$ agrees with $\lambda = \lambda_\text{nyt}/1100$.
- Hubble distance chains: $v = cz$, $v = H_0 d$, then $d = cz/H_0 = c(\lambda-\lambda_0)/(H_0\lambda_0)$. These are correct. The small-$z$ condition for $v = cz$ is still stated in the unchanged text.
- Hubble time: $t = d/v = d/(H_0 d) = 1/H_0$.
- Ratio of two galaxies: $d_\text{B} = d_\text{A}v_\text{B}/v_\text{A}$ from the same $H_0$.
- Helium mass fraction: $Y = m_\text{He}/m_\text{yht} = 2n/(n+p)$ (equal nucleon masses assumed; stated).
- Triple-alpha: $Q = \Delta m\,c^2$ with $\Delta m = 3m_\text{He}-m_\text{C}$, using atomic masses. The electrons balance: 6 = 6.
- Fit: the slope $\Delta v/\Delta d$ and the least-squares fit through the origin $H_0 = \sum dv/\sum d^2$ are both right. Temperature scaling: $T = (1+z)T_\text{nyt}$ is correct.
