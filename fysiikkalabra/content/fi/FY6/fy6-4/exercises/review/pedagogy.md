VERDICT: PASS
CONTENT-HASH: 43cd3baad13c0746
SCOPE: delta numbers from f3db54128b103065 base e000744

## Blocking
- none

## Polish
- L3 E12 Kaava: `R_sarja = R_a + R_b` is now stated without the `U = RI` step; add `U = (R_a + R_b) I` and `U = R I` (carried over, not blocking).
- Heater task (I_rinnan / I_sarja): the step from `I = U/R` to `R_sarja / R_rinnan` is still not written out (carried over).

## Checked
- Diff only removes the bare $\Sigma U = 0$ / $\Sigma I = 0$ labels from Kaava rows (all solutions); each row now starts at the plain statement ($I = I_1 + I_2$, $U = U_1 + U_2$, $R_\text{sarja} = R_a + R_b$), so the chapter no longer uses Kirchhoff notation before it is taught: the earlier Polish on this is resolved.
- Aligned rows (`&=`) stay consistent: every step still follows from the previous one, and the Periaate lines state the same rule in words.
- No answer, number or figure value changed; the figure tasks (task-parallel, task-mixed) are untouched and still give all values.
- Levels, task wording, Finnish and phone captures are unchanged from the passed version.
