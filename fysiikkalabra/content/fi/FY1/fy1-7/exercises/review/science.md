VERDICT: PASS
CONTENT-HASH: 6f84f2c00e8197fd
SCOPE: delta round 1 (work queue 8g, Kaava steps from basic equations)

## Blocking
- none

## Polish
- none

## Checked
- I checked every changed Kaava step. Each starts from $\rho = m/V$ and solves symbolically, for:
  - $m = \rho V$ and $V = m/\rho$;
  - $m = \rho abc$;
  - $\rho = m/(V_2 - V_1)$ and $\rho = (m_\text{yht} - m_0)/V$;
  - equal masses giving $V_\text{Al}/V_\text{Cu} = \rho_\text{Cu}/\rho_\text{Al}$;
  - the mixture $\bar\rho = (\rho_1V_1 + \rho_2V_2)/(V_1 + V_2)$;
  - the wire length $L = m/(\rho\pi r^2)$;
  - the intercept form $m_\text{yht} = m_0 + \rho V$;
  - the error with the probe volume;
  - the two-metal system, whose substitution step $(\rho_\text{Cu} - \rho_\text{Al})V_\text{Cu} = m - \rho_\text{Al}V$ is right;
  - the sphere $\rho = 6m/(\pi d^3)$.
- The former separate display lines, the final forms of these steps, are now inside the Kaava block. No content was lost.
- I recomputed the numbers myself: 94,5 g; 400 cm³; 1800 kg; 1,93 kg; 1,975 kg; 8900 and 788 kg/m³; 3,32; 4,42 g/cm³; 71,1 m; 920 kg/m³; 39,9 cm³; 0,448 kg. None changed.
- The hash was 6f84f2c00e8197fd at the start and at the end.
