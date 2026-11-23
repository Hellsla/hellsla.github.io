VERDICT: PASS
CONTENT-HASH: 542c67f826a69f89
SCOPE: full (unit.md, inquiry.json, teacher.md, unit.json, sovella tasks.json, solutions.md, answers.py, figures.py); first the three new ```pysahdy boxes, checked against content/fi/units/fy9-lampo/unit.md. Language: en.

## Blocking
(none)

## Polish
- s3 d: the rubric says the one-run result is "about 12 %" too large (2.54/2.26 = 1.125), the model answer "about 13 %" (600/530 = 1.13). Both are defensible, but they should give the same figure. The model answer also writes $P_\text{h}$ (and so does the figure label) where the task and rubric write $P_\text{loss}$.
- s5 b: the required cup heat capacity is 1890 J : 25.7 K = 73.5 J/K, given as "about 70 J/K". That is acceptable; "about 74" would be exact.
- Carried over from the earlier report: s8 calls 333 kJ/kg "the table value" while the rest of the unit uses 334 kJ/kg. Neither is wrong.

## Checked
- Pysähdy boxes (1 coffee and heat, 2 where the melting energy goes, 3 the final temperature of ice and water): each question and answer says the same physics as the Finnish box at fi lines 13, 110 and 197. No condition is added or lost.
  - Box 1 matches the guardrail definition: heat is energy in transfer, so a body has no heat.
  - Box 2: the energy raises the interaction energy, not the kinetic energy (C-level, consistent with Formula, tarkistus-1, virhe-sulaminen).
  - Box 3 is conditioned on ice and water coexisting, the same as Thermal balance and lt-5.
  - No contradiction with Common mistakes.
- Other diffs:
  - The hero SVG is now a raster image; it holds no numbers and its aria-label is unchanged.
  - The tarkistus-3 model text is split into paragraphs; its words and numbers are identical.
- Recomputed every number in one script with my own formulas (scratchpad recompute.py):
  - unit text: 21/334/419 kJ and curve break points 355/774 kJ
  - lt-3 5.2; lt-5 8.4 kJ, 33.4 kJ, 25 g
  - aineisto 2083 J/(kg·K) and mistakes 1250/20833/129.6
  - virhe 167 kJ
  - amme 13.79 kg (mistakes 11.76/10.81/464)
  - juhlajaat 2.027 kg (mistakes 12.78/2.24/2.164)
  - masto 180 mm (mistake 1073)
  - katko 0.886 K
  - tarkistus-2 3.88 kg (mistakes 0.573/0.00108/0.0647)
  - s1 21.88 GJ, 17.37 h, shares 82/16/2 %, 2.7 h and 14 h
  - s2 81.6 K, 1.667 kW, 35.8 %, 33 kg
  - s3 least-squares fit r = 2.263 MJ/kg with intercept 68.9 W; line at 100 W is 4.1 g and at 1100 W 136.7 g; read value 2.256 MJ/kg and 70 W; one-run value 2.54 MJ/kg
  - s4 3.1 MJ/(m²·cm)
  - s5 370.8 and 333.0 kJ/kg, 431 kJ/kg
  - s6 31.48 K, 133.7 K, 40.2 %, 240 s, 7.5 and 3 kW
  - s7 0.222 K/s, 900 J/(kg·K), 360 s (358 s with 896)
  - s8 2083 J/(kg·K), 333 kJ/kg, 270.2 kJ, 0.30 kg (wrong route 0.36 kg)
  - Every answer is inside its tolerance.
- Physics: models state their conditions (Q = cmΔT only without a change of state, constant pressure for phase changes, expansion formulas up to about 100 K, U-value at steady temperatures). Causal mechanisms are right (the s4 snow insulation, the s7 d loss growing with the temperature difference, engine braking). No "energy becomes heat" wording. Scope is FY3 with FY2/FY4 links.
- Assessment: exactly one correct option in each choice item, and every distractor's feedback is right. Rubric points add up to the part points. "Hyväksytään myös" covers the alternative routes.
- Hash 542c67f826a69f89 (units.py hash fy9-lampo --lang en) at start and end.
