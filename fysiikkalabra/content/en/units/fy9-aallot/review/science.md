VERDICT: PASS
CONTENT-HASH: 79ddac07b1cdc0c8
Delta review (formulas in MAFY form, 2026-11-12) of the version passed at 271c1d1ab8c947a2.

## Blocking
(none)

## Polish
1. `unit.md`, the sentence after the sound block: $A$ is the amplitude elsewhere in the unit but the area in $I = \tfrac{P}{A}$, and the subscript H means beats in $f_\text{H}$ and the observer in $v_\text{H}$. Fix: add "(here $A$ is an area, not the amplitude)". Also say that L and H are the Finnish initials used by MAFY (lähde = source, havaitsija = observer).
2. `inquiry.json` (the Doppler items) writes the source speed as $v_\text{s}$, and Sovella writes the beat frequency as $f_\text{h}$. Both are defined there, but they differ from the theory's $v_\text{L}$ and $f_\text{H}$. Fix: rename them, or add "(in the theory $v_\text{L}$)" to the first hint.

## Checked
I recomputed the four Doppler rows ($f_0 = 440$ Hz, $v = 343$ m/s, a speed of 20 m/s): source towards 467.2 Hz, away 415.8 Hz; observer towards 465.7 Hz, away 414.3 Hz. These are MAFY's forms with its conditions: one of them moves, slower than sound. $\overline{F} = -k\overline{x}$ explains the sign. $I = P/A$ is given with $A = 4\pi r^2$ for a point source without reflections. The map nodes ($\overline{F} = -k\overline{x}$, $f_\text{H}$, $f = f_0 v/(v - v_\text{L})$) match the theory. The English text says the same physics as fi. The other rows are unchanged.
