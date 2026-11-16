VERDICT: PASS
CONTENT-HASH: 8c7f9a99572a11aa

## Blocking

## Polish
- lesson.md:201 — "In the hub dynamo of a bicycle, a magnet turns in the middle of the coils": in a typical hub dynamo the stator coil sits fixed on the axle and the ring magnet turns around it with the hub shell. The physics (relative motion changes the flux) still holds — write "a ring magnet turns around the coils when the wheel turns".
- exit-ticket.json:8 — the answer says the voltage is zero at the maximum because "ΔΦ : Δt" is zero. That is the instantaneous rate (the slope of the tangent), and it holds only for a smooth maximum. Write "the tangent of the flux graph is horizontal, so the instantaneous rate of change of flux is zero".
- inquiry.json:94 (ennuste-vauhti, "It halves" feedback) — "the voltage grows from −20.0 mV to −40.0 mV": the signed value decreases, so say "its magnitude grows from 20.0 mV to 40.0 mV".
- lesson-answers.py — `sim-e-in-v0.30` / `sim-t-in-v0.30` use a speed the slider cannot set (max 0.20 m/s), and no text uses them. Drop them or use 0.15 m/s.
- lesson.md:374 — "The magnitude is always positive" → "never negative" (it is zero when the flux does not change).

## Checked
- I recomputed every number in one script (worked example 0.20 V and 0.80 mV per turn; sim −20/−40 mV, Δt 1.00/0.50 s, e·Δt = −20 mV·s at v = 0.05–0.20; N = 5/20 → −10/−40 mV; virhe 72/0.72/0.36 V; siirto 4.8 V and its mistakes 0.008/0.0048/4800; rod 0.50 V, 50 V, 1.0 V; exit 20 mWb). All agree with the text and lesson-answers.py.
- Faraday's law, Φ = BA (perpendicular condition stated), and e = vBl (mutually perpendicular, equilibrium eE = evB, then U = El) are each derived with their conditions. The derivation from the swept area matches. All inside FY7 scope, with no self-induction.
- Rod figure: v to the right with B into the page gives a downward force on the electron. The lower end is −, the upper end +, E points down and F_s points up: all correct.
- Graph figure (said to be to scale): pixel positions match t = 0.5/1.5/2.5/3.5 s, Φmax = 2.0 mWb and ±20 mV for N = 10, l = 0.10 m, v = 0.10 m/s, B = 0.20 T, field 0.20 m wide. It matches the sim's default run.
- Flux figure: at 55° tilt three of five lines pass through the loop (cos 55° ≈ 0.57). The parallel loop lies between the lines.
- sim.js implements the model: overlap(x), e = ∓NBlv, 0 inside the field. finish() samples e_tulo at mid-entry and e_sisalla at mid-inside. t_tulo = l/v. The 8 s axis fits the slowest run. The limits (sharp edge, no current, no braking, model values) are stated in `model`.
- koe-1 locks B and N and varies v; koe-2 locks v and B and varies N. simState gives e_tulo, t_tulo and e_sisalla at those values.
- Predictions, kertaus, virhe and check-1 each have exactly one correct option, and every distractor's feedback gives the right reason.
- The johtopaatos and tarkistus-3 model answers agree with the theory. The criteria ask only for what the experiments give.
- The English sim interface is translated (1280 px and 390 px captures).
