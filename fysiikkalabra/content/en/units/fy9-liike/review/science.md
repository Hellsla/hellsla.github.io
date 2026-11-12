VERDICT: FAIL
CONTENT-HASH: ca31abd20e3d66b5
Delta review (formulas in MAFY form, 2026-11-12) of the version passed at 47fff9ff6ab0e619.

## Blocking
1. **B, undefined symbol.** `unit.md`, "Uniformly accelerated motion": no sentence after the new row $\overline{a}_\text{k} = \frac{\Delta\overline{v}}{\Delta t}$ defines $\overline{a}_\text{k}$ or $\Delta\overline{v}$, and neither has a unit. The next rows use a scalar $a$ without the one-dimensional step given for $v$. Fix: add "where $\Delta\overline{v}$ is the change in velocity (m/s) and $\overline{a}_\text{k}$ the average acceleration (m/s²). In linear motion the signed $a = \tfrac{\Delta v}{\Delta t}$ is enough."

## Polish
2. Sovella writes $v_\text{ka}$, while the theory writes $v_\text{k}$, and the English text never explains the subscript k. Fix: align them, and note that k is MAFY's subscript for average (keskimääräinen).

## Checked
$\overline{v}_\text{k} = \Delta\overline{x}/\Delta t$ is MAFY's form, followed by its signed one-dimensional form. $\overline{a}_\text{k}$ is also MAFY's form, but it lacks the definition in Blocking 1. The English text says the same physics as fi. The other rows are unchanged.
