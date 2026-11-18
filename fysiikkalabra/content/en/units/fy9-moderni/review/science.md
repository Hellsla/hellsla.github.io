VERDICT: FAIL
CONTENT-HASH: f4531b7790ea5ae7
SCOPE: delta: new tasks s8 (A concrete wall) and s9 (The recession of galaxies) and the changed intro; older tasks s1-s7 untouched

## Blocking
- **A (causality), s8 d Assumptions:** "and the activity of the source does not stay constant. A real wall should therefore be made thicker". A decaying source gives a *smaller* dose rate over time, so this reason points the other way. Scattering is a correct reason; replace the activity clause with one that really raises the dose (a stronger or replaced source, more time in the corridor) or drop it. Same sentence as in fi.
- **Assessment (7), s8 d criterion 4 (transfer, 1 p):** d asks only "How thick must the wall be at least". The criterion scores naming an assumption and its effect, which d does not ask, and "the dose rate is constant" is given in the task text. Ask for it in d or move the point.
- **B (6, consistency), s9 c:** the Principle "moved at the same velocity v all the time and started from the same place as the others" (and the part text "every galaxy has moved at the same velocity", criterion 1 "travelled the distance d") is the explosion-from-a-point picture that s9 d's model answer, its common mistake ("like the fragments of an explosion") and the chapter *The evolution of the universe* reject. State it as distances: "the distances between galaxies have grown from zero at a constant rate", t = d/v = 1/H0.

## Polish
- s9 a: the text gives the grid point (250 Mpc; 18 000 km/s), so the graph_read point is earned by copying the text. The alt-text carries the point for non-visual readers; the bullet could go.
- s9 d criterion 2 requires "space itself expands"; the no-centre argument is criterion 1. Consider accepting criterion 1's argument with any correct expansion picture.
- s8 a: (20 cm; 5.0 µSv/h) is near the axis of a linear graph; a ±0.5 µSv/h reading gives µ = 0.134-0.144 1/cm, outside the 3 % tolerance. (10 cm; 20 µSv/h) is more robust, or widen the tolerance.

## Checked
- Read the en tasks.json entries and solutions of s8 and s9 and the intro in this language's packet. Every number, unit and rounding is the same as in fi (0.14 1/cm, 6.6 µSv/h, 330 h, 2.2 mSv, 3.03 µSv/h, 23.6 -> 24 cm rounded up, 31.6 cm error; 72 km/s/Mpc, 116.7 -> 120 Mpc, 2.333e-18 1/s, 4.286e17 s, 1.358e10 a); the meaning of every criterion, common mistake and accepted method matches fi. Decimal points throughout.
- One script (scratchpad rc_moderni.py) recomputed all of them from the figures' own data (80 µSv/h, half-value 5.0 cm; H0 = 72, nine points, LS slope 72.4) beside answers.py: all agree.
- Physics as in fi: exponential attenuation (half-value route accepted), H = Ḣt, 1 mSv public limit; 1/H0 as the Hubble time with the non-constant rate stated. Points 13 and 13; criteria sum to part points.
- Intro: nine problems match the set. The "Yleisiä virheitä"/"Hyväksytään myös" headings are the parsed fixed headings used by all nine tasks.
- practice.py check OK; hash the same at start and end.
