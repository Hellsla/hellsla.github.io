VERDICT: FAIL
CONTENT-HASH: f4bb3ba46d2d1cef
Delta review (formulas in MAFY form, 2026-11-12) of the version passed at d1021d5831c47cfe.

## Blocking
1. **B, undefined symbol.** `unit.md`, "Tasaisesti kiihtyvä liike": no sentence after the new row $\overline{a}_\text{k} = \frac{\Delta\overline{v}}{\Delta t}$ defines $\overline{a}_\text{k}$ or $\Delta\overline{v}$, and neither has a unit. The next rows switch to a scalar $a$ without the one-dimensional step that the average-velocity sentence gives for $v$. Fix: after the block add "missä $\Delta\overline{v}$ on nopeuden muutos (m/s) ja $\overline{a}_\text{k}$ keskikiihtyvyys (m/s²). Suoraviivaisessa liikkeessä riittää etumerkillinen $a = \tfrac{\Delta v}{\Delta t}$."

## Polish
2. `sovella/tasks.json` and `solutions.md` write $v_\text{ka}$, while the theory writes $v_\text{k}$. Fix: align them.

## Checked
$\overline{v}_\text{k} = \Delta\overline{x}/\Delta t$ is MAFY's form, followed by its signed one-dimensional form. $\overline{a}_\text{k}$ is also MAFY's form, but it lacks the definition in Blocking 1. The other rows are unchanged.
