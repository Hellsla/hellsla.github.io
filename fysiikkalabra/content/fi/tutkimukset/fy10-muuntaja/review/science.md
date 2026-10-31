VERDICT: PASS
CONTENT-HASH: 647edb9070a9fdbf

## Blocking
None.

## Polish
None open. All three points from the previous review are fixed:
1. teacher.md now recommends a true-RMS meter at least for $I_1$. It says why: the magnetising current is not sinusoidal. It also says that the lower bound ($U_1 I_1 \ge P_1$, so the calculated η cannot exceed the true η) assumes correct RMS readings.
2. Teoriaa now says "Vastuksen teho … $P = UI$" and adds the in-phase condition for other devices. It agrees with the next paragraph on the primary.
3. Model graph: equal scales, ticks at 1 and 2 on both axes, a 45° line through the origin, and no data points.

## Checked (delta and unchanged physics)
- **Theory, light-load sentence.** It was removed from the shared theory and only $U_1 I_1 \ge$ the real input power remains, which is correct. The light-load remark stays in the extension tuki and in teacher.md, where it is correct.
- **Osa A (O).** One reading per combination, "since the points smooth random errors". This is correct and is limited to random errors.
- **Curve-fit wording.** "mallin mukainen käyrä (suora, jos …)" is correct.
- **Q4.** The neutral "Jos muuttui" wording adds no physics issue.
- **Unchanged from the previous review.**
  - Ideal model: the conditions (no leakage, no winding resistance, no core losses) and the derivation of $U_2/U_1 = N_2/N_1$.
  - Efficiency: the magnetising-current mechanism and the lower-bound claim.
  - Load: the voltage drop is explained by winding resistance and leakage, iron losses against copper losses ($\propto I^2$) for η against $P_2$, and the uncertainty propagation.
  - AC: effective values.
  - Safety: mains never on the primary, no secondary short circuit and no ammeter alone across a coil. No limits are invented; all come from the teacher.
  - Figures: no fabricated data, and the circuit matches figures.py.
- `investigations.py check` passes, and the hash was verified as 647edb9070a9fdbf. The last change, which splits the Δη/η formula into a two-line aligned block, is equivalent to the old formula.
