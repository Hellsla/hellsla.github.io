VERDICT: PASS
CONTENT-HASH: 1116cfbed2d7e149
Delta review (formulas in MAFY form, 2026-11-12) of the version passed at c2dcaa79f3905e0c.

## Blocking
(none)

## Polish
1. `unit.md`, the sentence after the sound block: $A$ is the amplitude elsewhere in the unit (it is in the summary, the formula map and $\tfrac12 kA^2$) but the area in $I = \tfrac{P}{A}$. The subscript H is the beat frequency in $f_\text{H}$ and the observer in $v_\text{H}$. Both follow MAFY and both are defined, but a student can mix them up. Fix: add "(tässä $A$ on pinta-ala, ei amplitudi)" after the intensity definition.
2. `inquiry.json` (the Doppler items) writes the source speed as $v_\text{s}$, and `sovella/tasks.json` and `solutions.md` write the beat frequency as $f_\text{h}$. The items define these themselves, so nothing contradicts the theory, but the symbols differ from its $v_\text{L}$ and $f_\text{H}$. Fix: rename them in the next task pass, or add "(teoriassa $v_\text{L}$)" to the first hint.

## Checked
I recomputed the four Doppler rows ($f_0 = 440$ Hz, $v = 343$ m/s, a speed of 20 m/s): source towards 467.2 Hz, away 415.8 Hz; observer towards 465.7 Hz, away 414.3 Hz. These are MAFY's forms with its conditions: one of them moves, slower than sound. $\overline{F} = -k\overline{x}$ explains the sign. $I = P/A$ is given with $A = 4\pi r^2$ for a point source without reflections. The map nodes ($\overline{F} = -k\overline{x}$, $f_\text{H}$, $f = f_0 v/(v - v_\text{L})$) match the theory. The fi-easy text says the same physics as fi. The other rows are unchanged.
