VERDICT: PASS
CONTENT-HASH: 2eb18a63c0e1ad44

## Blocking

## Polish
- exercises.json:343 (fy6-3-L2-08) — "Taulukossa on samalla kytkennällä tehty esimerkkimittaus" reads as if the table was actually measured in the simulation, while answers.py says it is example data and was not read from it — write "laadittu esimerkkiaineisto" or similar (the label esimerkkiaineisto already stops this being blocking).
- exercises.json:343 (fy6-3-L2-08) — the task asks for I(U) with U on the horizontal axis, but the chapter's ominaiskäyrä has I horizontal (slope R). The solution explains that the slope here is 1/R, so nothing is wrong. Using the chapter's axes would make it simpler and match L2-05 and L1-09.

## Checked
- One independent script recomputed all 20 numeric answers (L2-05 and L3-02 as least-squares lines through the origin) and compared them with exercises.json: every one is inside its tolerance.
- L2-08: R = ΔU/ΔI = 15,0 V : 0,375 A = 40,0 Ω; every point gives U : I = 40 Ω. Tolerance 0,02 fits three significant figures.
- L2-08 c): P = UI is given in the task (FY6 content, sähköteho). 0,90 W at 6,0 V and 3,60 W at 12,0 V; the ratio of 4 is used as a real check.
- L2-08 b)/d): the line through the origin has a physical reason (no voltage, no current), and the fit sentence is the guardrail's ("yleensä"). The lamp's curve bending below the line is right for these axes. The mechanism (metal resistivity rises with temperature, so the Ohm's-law condition fails) matches the glossary and the brief.
- L2-08 a): the meter placement (ammeter in series, voltmeter across the resistor, read U from the meter) is correct. The simulation's resistor is said to be an ideal constant-R model.
- Reflowed chains (L2-03 and the rest): same numbers, signs and units in the same order; no physics change.
- The other 19 tasks were already passed; they still give the same answers, symbols and conditions as the brief (R = U : I, R = ρl : A, the constant-temperature condition).
- Hash read at start and end: unchanged.
