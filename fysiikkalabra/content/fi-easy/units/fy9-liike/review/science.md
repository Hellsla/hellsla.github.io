VERDICT: PASS
CONTENT-HASH: e3f6843d4048f9ea
Delta review (formulas in MAFY form, 2026-11-12) of the fix to the version reviewed at 908bafcc86338340 (FAIL).

## Blocking
(none)

## Polish
1. `sovella/tasks.json` and `solutions.md` write $v_\text{ka}$, while the theory writes $v_\text{k}$. Fix: align them.

## Checked
1. The previous Blocking item is fixed (commit c4e866703). The new sentence after the keskikiihtyvyys block defines $\Delta\overline{v}$ (m/s), $\Delta t$ (s) and $\overline{a}_\text{k}$ (m/s²). It gives the signed scalar $a = \Delta v/\Delta t$ for rectilinear motion and says that at constant acceleration the average equals the instantaneous acceleration. All of this is correct, and it fits the rows $v = v_0 + at$ and $x = x_0 + v_0 t + \tfrac12 at^2$ that follow.
2. $\overline{v}_\text{k} = \Delta\overline{x}/\Delta t$ and $\overline{a}_\text{k}$ are MAFY's forms. The fi-easy text says the same physics as fi. Nothing else changed.
