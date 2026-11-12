VERDICT: PASS
CONTENT-HASH: 560ecb7e9c19d6a1
Delta review (formulas in MAFY form, 2026-11-12) of the fix to the version reviewed at f4bb3ba46d2d1cef (FAIL).

## Blocking
(none)

## Polish
1. `sovella/tasks.json` and `solutions.md` write $v_\text{ka}$, while the theory writes $v_\text{k}$. Fix: align them.

## Checked
1. The previous Blocking item is fixed (commit c4e866703). The new sentence after the keskikiihtyvyys block defines $\Delta\overline{v}$ (m/s), $\Delta t$ (s) and $\overline{a}_\text{k}$ (m/s²). It gives the signed scalar $a = \Delta v/\Delta t$ for rectilinear motion and says that at constant acceleration the average equals the instantaneous acceleration. All of this is correct, and it fits the rows $v = v_0 + at$ and $x = x_0 + v_0 t + \tfrac12 at^2$ that follow.
2. $\overline{v}_\text{k} = \Delta\overline{x}/\Delta t$ and $\overline{a}_\text{k}$ are MAFY's forms. Nothing else changed.
