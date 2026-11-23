VERDICT: PASS
CONTENT-HASH: 185e679af584e570

## Blocking
- none

## Polish
- none

## Checked
- I checked every changed Kaava step. Each starts from the line $y = kx + b$ or $k = \Delta y/\Delta x$ and solves symbolically for the asked quantity:
  - $t = (h-b)/k$ and $t = (s-b)/k$;
  - $k = m/N$;
  - $b = m_1 - kV_1$, $b = l_1 - km_1$ and $b = x_1 - vt_1$;
  - $r = y_2/y_1$;
  - point-slope $s = s_1 + k(t - t_1)$;
  - the slope ratios $|k_1|/|k_3|$ and $k_\text{B}/k_\text{A}$;
  - the relative-slope uncertainty;
  - $k_\text{max}$, $k_\text{min}$ with mean and half-difference.
- I recomputed the numbers myself:
  - r = 1,76;
  - the uncertainty ratio is 16;
  - $k_\text{B}/k_\text{A}$ = 2,90 unrounded, against the solution's 7,84/2,71 = 2,89, which is inside the tolerance and unchanged;
  - ε = 15,8 %.
- No number, answer or tolerance changed.
- The paragraph splits (L1-07, L2-07 spring, L2-08, L3-01, L3-02 d) keep every sentence. These include the elastic-limit reasoning, "väli on arvioitu rajaus eikä varma raja" and the weather-model limits.
- The only exercises.json change is that the esimerkkiaineisto marker was taken out of the captions, with the teacher's approval. No physics changed.
- The hash was 185e679af584e570 at the start and at the end.
