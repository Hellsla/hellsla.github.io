VERDICT: PASS
CONTENT-HASH: 30456eba01b5ee26

## Blocking
(none)

## Polish
- inquiry.json `mittaus` question — a student who divides the mass in grams by the extension in centimetres (300 g / 9.8 cm = 30.6) lands inside the 7 % tolerance and is told the answer is correct, because g ≈ 10 m/s² makes that wrong method come out close to the right number. Consider a closing sentence in the solution ("the vertical axis is the force in newtons, not the mass") or keep it as is. Assessment, not physics.
- lesson.md "The spring constant from a measurement" vs inquiry.json `simulaatio.calc` — the theory calls $F_\text{v} = kx$ a magnitude, while the sim and its calc box use it as a signed component (negative when the spring is compressed). The calc box says this, so it does not mislead (C), but one sentence in the theory ("in the simulation $F_\text{v}$ also has a sign") would make the two say the same thing.

## Checked
- I recomputed every number in the lesson and the inquiry with my own formulas (worked example 392.4 N/m and 0.1766 J, triangle check, gradient 40 N/m, energies of spring B 0.0625/0.250/1.00 J, k_C = 80 N/m, least-squares fit 29.95 N/m against the 30 N/m read off the line, pinball 3.354 m/s and its three mistake values, check-2 +10 N, check-3 0.15 m, exit ticket 1.0 J). They all agree with lesson-answers.py.
- The kulmakerroin graph is to scale, as it says: the line's gradient is 40.1 N/m in pixels, the points lie within 0.15 N of the line, and the two marked points sit on the line at (0.025; 1.0) and (0.100; 4.0).
- In the suunta and pari figures the force directions are right for a stretched and a compressed spring, the third-law pair is drawn with equal arrows on different objects, and position is drawn as a dimension arrow, not as a force.
- Free-body diagrams: in the worked example G and F are equal on the fish. In virhe the only error is F_2, the block's pull on the spring drawn on the block, which is exactly what the task means. malli-laatikko shows G = N and F = F_μ at constant velocity, with velocity drawn apart from the forces.
- Hero picture: pulling the knob out compresses the spring between the tip and the front wall, which is the correct mechanism.
- Every choice item has exactly one correct option, and each distractor's feedback is right.
- The simulation implements F = −kx, F_k = kx, F_v = kx and E_p = ½kx². Its arrow directions and points of application are right, it shows 6 px/N within the canvas for spring C at ±0.20 m, and its readout rounding gives the 0.063 J the feedback quotes. Its model box states its limits (no friction, the law holds over the whole slider range).
- Experiments: each locks the other parameter, and the measured keys F, Fk, Fv and Ep are all in simState.
- Formula conditions are stated: rest-length origin, the limit of proportionality, the slow stretch for the work. The pinball transfer states that friction, the plunger's mass and the table's tilt are neglected, and with a massless plunger the ball does leave at the rest length.
- Scope fits FY5 "harmonic force and its potential energy", and the period is left to the next chapter.
