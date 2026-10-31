VERDICT: PASS
CONTENT-HASH: ce5fa4eb155feea0

## Blocking
None. The blocking point from the previous review is fixed. teacher.md now says that a missed $L_1$ makes every ordinal one too small. The slope and λ stay correct, and the constant term changes from $-(\lambda/4+e)$ to about $\lambda/4 - e$, which the page's $n = 0$ hint reveals. A skipped middle resonance gives a double gap and a kink. I recomputed this from $L_n + e = (2n-1)\lambda/4$, and it is correct.

## Polish
None open. All three polish points are applied:
- "halkaisijasta" for the end correction;
- $T = (\theta/{}^\circ\text{C} + 273{,}15)\ \text{K}$;
- the standing-wave alt text now says the second node is λ/2 from the piston, which matches the drawing.

## Checked
- Theory: a node at the closed end; the antinode slightly outside the open end at $e$ ($\approx 0{,}6\,r$), the same for every resonance at one $f$. Nodes are $\lambda/2$ apart, and a node and its antinode are $\lambda/4$ apart.
- $L_n + e = (2n-1)\lambda/4$; for a tube open at both ends $L_n + 2e = n\lambda/2$. Resonances are $\lambda/2$ apart, and $e$ cancels in the differences.
- Slope of $L_n$ against $n$ is $\lambda/2$, with constant term $-(\lambda/4+e)$; the model figure matches.
- Uncertainty:
  - $\lambda/2 = (\bar L_N - \bar L_1)/(N-1)$;
  - $\Delta(\lambda/2) = (\Delta L_N + \Delta L_1)/(N-1)$;
  - $\Delta v/v = \Delta f/f + \Delta\lambda/\lambda$;
  - half-range with the reading accuracy as the floor, and the rounding rule;
  - "sopusoinnussa" wording.
- $v = 331{,}3\ \text{m/s}\cdot\sqrt{T/273{,}15\ \text{K}}$ (dry air; humidity raises $v$ slightly).
- Extension: $\lambda = v\cdot(1/f)$ is a line through the origin with slope $v$.
- Figures: `figures --check` reports them up to date, and the geometry parameters are unchanged from the version I rendered. The graphs contain no data, and the generator display is blank.
- No invented frequency, volume level or measurement anywhere. The result template is now $(\ldots \pm \ldots)\ \text{m/s}$, and the teacher gives the volume limit and the accuracy of $f$.
- The pedagogy edits (prediction 1, the intro and the "useimmat" wording in the O mode) add no physics error.
- Card p. 10 (item 15): the aim, the equipment and the hints are covered.
