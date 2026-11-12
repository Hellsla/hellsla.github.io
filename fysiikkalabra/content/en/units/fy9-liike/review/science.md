VERDICT: PASS
CONTENT-HASH: 7c3a27204eeae8fd
Delta review (formulas in MAFY form, 2026-11-12) of the fix to the version reviewed at ca31abd20e3d66b5 (FAIL).

## Blocking
(none)

## Polish
1. Sovella writes $v_\text{ka}$, while the theory writes $v_\text{k}$, and the English text never explains the subscript k. Fix: align them, and note that k is MAFY's subscript for average (keskimääräinen).

## Checked
1. The previous Blocking item is fixed (commit c4e866703). The new sentence after the keskikiihtyvyys block defines $\Delta\overline{v}$ (m/s), $\Delta t$ (s) and $\overline{a}_\text{k}$ (m/s²). It gives the signed scalar $a = \Delta v/\Delta t$ for rectilinear motion and says that at constant acceleration the average equals the instantaneous acceleration. All of this is correct, and it fits the rows $v = v_0 + at$ and $x = x_0 + v_0 t + \tfrac12 at^2$ that follow.
2. $\overline{v}_\text{k} = \Delta\overline{x}/\Delta t$ and $\overline{a}_\text{k}$ are MAFY's forms. The English text says the same physics as fi. Nothing else changed.
