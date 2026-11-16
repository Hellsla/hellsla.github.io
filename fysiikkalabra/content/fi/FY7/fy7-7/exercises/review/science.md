VERDICT: PASS
CONTENT-HASH: d26ffd421626a1cb

## Blocking

## Polish
- solutions.md:217 (L2-08 Kohta c) — when the magnet is pushed right through the coil the flux first grows and then falls, so the needle swings both ways during one push; one clause would prepare the student for that observation.

## Checked
- Delta round 1: only fy7-7-L2-08 (FY7-A4) judged, plus the three captions that lost "(esimerkkiaineisto)" (wording only, no number changed); hash identical at start and end.
- Recomputed: $|e_\text{ka}| = N|\Delta\Phi|/\Delta t = 4 \cdot 0{,}25\,\text{mWb} / 0{,}50\,\text{s} = 2{,}0\,\text{mV}$ and $0{,}50\,\text{mV}$ for 2,0 s; ratio 4 = ratio of the times. answers.py agrees; unit mV and tolerance 2 % fit two significant figures.
- The task says the flux change is through one turn and that the numbers are an assumed example, not read from the simulation; the solution repeats this.
- Source fetched 16 Nov 2026 (HTTP 200): the PhET page is "Faraday's Law" ("how a changing magnetic flux can produce a flow of electricity"). The simulation file itself names a movable bar magnet, a light bulb circuit with a 4 loop coil, an optional voltmeter (checkbox Voltmeter), a second 2 loop coil and a control that flips the magnet. So the task's description (magnet, coil, lamp, voltmeter to switch on), the example's 4 turns and the solution's remark that the needle's side depends on the magnet's orientation all match.
- a) and b): no voltage with the magnet at rest, also inside the coil; larger deflection with faster motion; sign reverses with direction; the lamp lights either way. Correct induction physics.
- d): flux $\Phi = BA\cos(2\pi f t)$ changes continuously, sign of $e$ alternates, $e_0 = NBA \cdot 2\pi f$ grows with $f$ (as in the brief); with a load the field exerts on the current-carrying coil a force that opposes the rotation (Lenz), the turbine's work against it becomes electrical energy; without a load no current and no energy transfer. Mechanism and energy account correct.
- Scope: induction law and generator, inside FY7; symbols as in the brief.
