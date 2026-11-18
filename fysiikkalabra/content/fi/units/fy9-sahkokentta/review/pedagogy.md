VERDICT: PASS
CONTENT-HASH: 261376c3ea53b297
SCOPE: delta: new tasks s7 (Alfahiukkanen levyjen välissä) and s8 (Vihreä merkkivalo) and the changed intro; older tasks untouched

## Blocking
- (none)

## Polish
- s8 d: the prompt asks what the results tell about the LED and Ohm's law, but the fourth criterion (communication, 1 p) rewards explaining why an LED cannot be connected straight to a source and what the series resistor does. A student who answers exactly what is asked loses the point. Add "ja miksi LEDin kanssa tarvitaan etuvastus" to the prompt, or fold the point into the concept criterion.
- s7 b: the concept criterion requires "Painovoima on mitätön" unprompted; the solution justifies it only in Järkevyys. Make it "Hyväksytään myös" or leave it out of the scored text.
- s7 c: the "Hyväksytään myös" route ($v^2 = 2as$) skips the energy concept point the rubric gives; say how that route is scored.
- s8 figure: nothing marked, so the 2,2 V plateau must be found by the student; good. An alt-text sentence naming the axes ($I$ in mA, $U_\text{D}$ in V) as the task text does would help a reader who cannot see the plot (shared with fy6-14 ex-led).

## Checked
- Read the fi packet's s7 and s8 tasks, solutions and the answers.py lines, and the changed intro (eight tasks, matches the set).
- Demand: both are unfamiliar, authentic set-ups with a graph the student must read, four parts of rising demand (read, apply, combine, interpret). Neither text or heading names the model: s7 does not say "energy principle" or "slope"; s8 does not say Kirchhoff or divider. s7 d (zero level) and s8 d (LED is not ohmic) are real conceptual checks, not recall.
- Rubric: points per criterion sum to part points (s7 4/4/4/3, s8 4/4/3/4); no points for irrelevant things apart from the s8 d note above.
- Numbers recomputed by hand: E 5,0 kV/m, a 2,41·10^11, v 98,2 km/s, V -50 V; I 17,27 mA, P 65,6 mW, share 63 %, R_min 126,7 Ω, R 440/110 Ω. Results rounded to two significant figures like the data; calculation chains are aligned rows; units are plain.
- Solutions: stepwise, principle named with the chapter, Järkevyys checks (work check, power sum); common mistakes are real (2e vs e, 250/5 without conversion, 6,0/220).
- Task names and figure names agree ($V$, $x$, $U_\text{D}$, $I$). Workload fits an exam-style set. practice.py check OK. Layout: shots.md 390 px captures exist for the current hash; hash unchanged at the end.
