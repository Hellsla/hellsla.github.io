VERDICT: PASS
CONTENT-HASH: 20765954e1e52615

## Blocking

## Polish
- solutions.md:225 (L2-08 Part b/c) — when the magnet is pushed right through the coil the flux first grows and then falls, so the needle swings both ways during one push; one clause would prepare the student for that observation (same remark as on the Finnish set).

## Checked
- Delta round 1: only fy7-7-L2-08 (FY7-A4) judged; hash identical at start and end.
- Recomputed from the task text: $|e_\text{ka}| = N|\Delta\Phi|/\Delta t = 4 \cdot 0.25\,\text{mWb} / 0.50\,\text{s} = 2.0\,\text{mV}$ and $0.50\,\text{mV}$ for 2.0 s; ratio 4 = ratio of the times. answers.py agrees; unit mV and tolerance 2 % fit two significant figures.
- English against Finnish by script: answer 2.0, unit, tolerance, kind and every number of the task text and the solution are the same.
- The task says the flux change is through one turn and that the numbers are an assumed example, not read from the simulation; the solution repeats this.
- Source fetched 16 Nov 2026 (HTTP 200): the PhET page is "Faraday's Law" ("how a changing magnetic flux can produce a flow of electricity"; learning goals name the coil, the bulb's brightness and the magnitude and sign of the voltage). The simulation file (HTTP 200) names a movable bar magnet, a light bulb circuit with a 4 loop coil, an optional voltmeter ("Play with or without voltmeter connected"), a 2 loop coil and "Flip Magnet". So the task's description, the example's 4 turns and the solution's remark that the needle's side depends on the magnet's orientation match the source.
- a) and b): no voltage with the magnet at rest, also inside the coil; larger deflection with faster motion; sign reverses with the direction of motion; the bulb lights either way. Correct.
- c): $\Delta\Phi = 0$ at rest, rate of change decides, sign follows the sign of $\Delta\Phi$. Correct.
- d): $\Phi = BA\cos(2\pi f t)$, $e = e_0\sin(2\pi f t)$, $e_0 = NBA \cdot 2\pi f$; with a load the force on the current-carrying coil opposes the rotation (Lenz), the work against it becomes electrical energy; without a load no current and no energy transfer. Mechanism and energy account correct.
- Scope: induction law and generator, inside FY7.
