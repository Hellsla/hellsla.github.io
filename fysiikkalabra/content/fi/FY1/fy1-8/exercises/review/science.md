VERDICT: PASS
CONTENT-HASH: c768525a69b2d6df

## Blocking
- none

## Polish
- content/fi/FY1/fy1-8/exercises/solutions.md:187 — in fy1-8-L3-05 the one aligned block uses $\Delta T$ for the temperature change (row 1) and $\Delta T_\text{lasku}$ for the uncertainty of the fall (row 3), so the same letter means two different things — consider naming the uncertainty differently (for example $\delta T_\text{lasku}$) or saying in the Tunnetut row that $\Delta T_\text{lasku}$ is the uncertainty. This is not an error; the symbols are defined.

## Checked
- The diff has only two lines: fi solutions.md:105 (L3-02) and :187 (L3-05). In both, the first row is now $r = -\Delta T/\Delta t$.
- With $\Delta T = T_\text{loppu} - T_\text{alku}$ and $\Delta t = t_\text{loppu} - t_\text{alku}$, $-\Delta T/\Delta t$ equals the second row $(T_\text{alku} - T_\text{loppu})/(t_\text{loppu} - t_\text{alku})$ exactly. The cooling rate is positive, as the Sijoitus needs. The round-1 sign error (A) is fixed.
- I recomputed the numbers in my own script. L3-02: $r_1 = 2{,}4$ and $r_2 = 1{,}0\,\text{K/min}$, so $\Delta r = 1{,}4\,\text{K/min}$; for comparison $-(68{,}0-80{,}0)/5{,}0 = 2{,}4$. L3-05: $r = 2{,}0\,\text{K/min}$, $T_\text{lasku} \ge 20\,\text{K}$, $t = 10\,\text{min}$. None of these changed.
- I grepped for any $\Delta T/\Delta t$ row left without its minus sign: there is none.
- No answer, unit, tolerance, task text or answers.py line changed.
- The hash was c768525a69b2d6df at the start and at the end.
