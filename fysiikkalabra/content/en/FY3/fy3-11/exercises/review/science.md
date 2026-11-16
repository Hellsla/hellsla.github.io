VERDICT: PASS
CONTENT-HASH: 04a69ae855461354
Round: 1
Mode: delta

## Blocking

## Polish

## Checked
- New fy3-11-L2-10 (Motiva PDF, heat pump COP). The model is Q₁ = Q₂ + W and ε = Q₁/W, so Q₁ = εW = 10 kWh and Q₂ = (ε − 1)W = 7.5 kWh. The key is 7.5 kWh with a 2 % tolerance, and two significant figures fit 4.0 and 2.5 kWh. The values are recomputed independently.
- Part a) matches the guardrail: a heat pump has a coefficient of performance, not an efficiency; the heat from outdoors is not in the denominator; "300 per cent" is inexact; an electric heater is practically 100 %.
- Part c) is right: a larger temperature difference (colder outdoors or warmer heating water) lowers ε. The figure of 1–2 at −25 °C is from the source, and at ε = 1 the pump has Q₂ = 0, like an electric heater.
- Part d) closes the energy balance: 2.5 + 7.5 = 10 kWh. The claim is shown false.
- The limits of the model (COP at one moment, 1.4–3 over the year for the houses studied) agree with the source facts. The quotations are translated faithfully.
- The aligned b) chains keep the same numbers, signs and units as the Finnish. A scripted comparison found identical answer, unit, tolerance and kind, and the same numbers in the text and in every solution section.
- Captions: only "(example data)" removed.
- Hash identical at start and end.
