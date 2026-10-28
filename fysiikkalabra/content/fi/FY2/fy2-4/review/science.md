VERDICT: FAIL
CONTENT-HASH: 9afe1413fb973d68

## Blocking
- inquiry.json:112, 243; lesson.md:156 — The lesson presents the model's assumption (efficiency independent of load) as a property of real devices. It tests this on a petrol engine, whose efficiency falls strongly at light load. "muuttuu hieman kuormituksen mukaan" (112) understates that. The model answer (243), "ei riipu tehosta", reads the model's assumption back as a finding. — Fix: the `model` box should say that real efficiency depends on load, strongly for an engine and little for a motor near its rated power. At 243 say "mallissa" for input power; independence from time holds generally. At 156 qualify the input-power clause, or move Koe 1 to the motor or the kettle.

## Polish
- inquiry.json:62, 66, 71, 75 — "Simulaation malli kumoaa/tukee" treats the sim's preset 25 % as evidence about engines. That is circular. Say "tyypillinen arvo on noin 25 % (mallin arvo)".
- lesson.md:44 — The efficiencies are realistic and honestly labelled as typical rounded values. FY2's scope asks for a named source (e.g. Motiva), and the engine value should be labelled as an average in use.
- Experiment intro (template): "laite = auto" shows the internal key, and "20000 W" is not in LaTeX.

## Checked
- One Python run recomputed answers.py and lesson-answers.py, and all values match: 36 kJ, 25 %, 250 W (mistakes 1250 and 15 000 W), 80 % (mistakes 20 and 125 %), and 30 % and 333 %.
- The formulas η = E_a : E_o = P_a : P_o and E_o = E_a + E_h are correct, and their condition (steady power) is stated.
- Both SVG figures are to scale: figure 1 is 6/114 of 120 px, and figure 2 uses 1,6 px/W for 60/3/57 W and 10/3/7 W.
- The worked example is symbolic first, converts by substitution, rounds to 2 s.f. with a justification and ends with a real check.
- The sim implements the model: 100, η · 100 and (1 − η) · 100 px, and E = P t. Canvas and readout are LaTeX (screenshots), with η labelled "tyypillinen".
- Koe 1 and Koe 2 isolate P_o and t respectively, simState has the measured keys, and the capture shows the initial state (20 kW, 10 s).
- No ×, written division uses a colon, and conversions are substitutions.
- No FY3/FY4 content: no work, Q = cmΔT, E_k/E_p, chain products or heat-engine theory.
- The exit ticket is correct.
