VERDICT: PASS
CONTENT-HASH: 21ad5fa41bd43289

## Blocking

## Polish
- solutions.md:226 (L2-08 Kohta c) — when the magnet is pushed right through the coil, the flux first grows and then falls, so the needle swings both ways during one push; one clause would prepare the student for that observation (fi too).

## Checked
- Delta round 1: only fy7-7-L2-08 (FY7-A4) judged, plus three table captions that lost "(esimerkkiaineisto)" (wording only, no number changed); hash identical at start and end.
- Against the Finnish set (passed today) by script: answer 2.0, unit mV, tolerance 0,02 and kind are identical, and every number in the task text and the solution is the same in both languages.
- Recomputed from the task text: $|e_\text{ka}| = N|\Delta\Phi|/\Delta t = 4 \cdot 0{,}25\,\text{mWb} / 0{,}50\,\text{s} = 2{,}0\,\text{mV}$, and $0{,}50\,\text{mV}$ for 2,0 s; ratio 4 = ratio of the times. answers.py gives 2.0. Two significant figures from 0,25 mWb and the times, N exact.
- The task says the flux change is through one turn and that the numbers are an assumed example, because the meter has no scale values; the solution repeats it.
- Source fetched with curl 16 Nov 2026 (HTTP 200): the PhET page is "Faraday's Law" ("how a changing magnetic flux can produce a flow of electricity"). The simulation file has a movable magnet, a four-loop coil with a bulb, a Voltmeter checkbox (off at start), plus and minus marks, a two-loop coil and a flip-magnet button. So the described set-up, "ota käyttöön jännitemittari (Voltmeter)", the example's 4 turns and the remark that the needle's side depends on the magnet's orientation all match.
- a) and b): no voltage with the magnet at rest, inside the coil too; larger deflection with faster motion; the sign reverses with the direction; the bulb lights either way. Correct.
- c): voltage depends on the rate of change of the flux and on N, not on the flux's size; a quarter of the time gives four times the voltage.
- d): $\Phi = BA\cos(2\pi f t)$ and $e_0 = NBA \cdot 2\pi f$ as in the brief; with a load the force on the current-carrying coil opposes the rotation (Lenz), the work against it becomes electrical energy; without a load no current and no energy transfer.
- Scope: induction law and generator, inside FY7.
