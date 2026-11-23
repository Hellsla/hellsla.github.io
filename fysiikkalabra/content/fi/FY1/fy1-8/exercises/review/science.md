VERDICT: PASS
CONTENT-HASH: 0134f21ed9127ea2
SCOPE: delta round 1 (work queue 8g, Kaava steps from basic equations)

## Blocking
- none

## Polish
- none

## Checked
- I checked every changed Kaava step. Each one starts from its basic equation and solves for the asked quantity:
  - $s = vt \Rightarrow v = s/t$;
  - mean, half-range and ε;
  - $s = vt \Rightarrow t = s/v$, $\varepsilon = \Delta t\,v/s$;
  - slope $v = \Delta s/\Delta t$, used twice;
  - midpoint and half-difference of $v$;
  - cooling rate $r = \Delta T/\Delta t$ with $\Delta r = r_1 - r_2$;
  - the time budget $t_\text{kok} = t_\text{val} + Nnt_\text{toisto}$ solved for $n$;
  - the mean difference against Δt, and $d$ and $k$;
  - the inequality chains ε ≤ ε_max giving $T_\text{lasku} \ge \Delta T/\varepsilon_\text{max}$ and $t \ge \Delta t/\varepsilon_\text{max}$, each rounded to the safe side.
- I recomputed the numbers myself: 0,417 m/s; 2,5 %; 10 %; 0,42 and 0,30 m/s; 0,033 m/s; 1,4 K/min; n = 4,0; k = 3,75; 10 min; 1,37 km. None changed.
- The new symbols $p$ and $\Delta r$ are defined in their own rows. No answer, unit or tolerance changed.
- The hash was 0134f21ed9127ea2 at the start and at the end.
