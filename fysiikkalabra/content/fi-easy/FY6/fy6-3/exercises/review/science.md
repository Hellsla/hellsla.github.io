VERDICT: PASS
CONTENT-HASH: 0403a43777fa1082
SCOPE: delta answers,comments,md-paragraphs,numbers,reflow,structure,typography,wording from 950adae5af06a27a base 8f23aa7

## Blocking

## Polish
- exercises/solutions.md:427 (L1-10 Järkevyys) — "paksumpi johto antaisi pienemmän resistanssin" is not a check of this result; compare with the lesson's table value instead: $1{,}7 \cdot 10^{-8}\,\Omega\cdot\text{m}$ gives $0{,}45\,\Omega$ too.

## Checked
- New L1-10: $R = \rho \dfrac{l}{A} = 1{,}678 \cdot 10^{-8} \cdot 40 : (1{,}5 \cdot 10^{-6})\,\Omega = 0{,}4475\,\Omega \to 0{,}45\,\Omega$; MAFY value 1,678·10⁻⁸ Ω·m matches docs/mafy-arvot.tsv (Resistiivisyyksiä, 20 °C); the lesson's 1,7·10⁻⁸ gives 0,453 Ω, inside the 3 % tolerance; 2 sf from the wire data right; 1,5 mm², 40 m realistic.
- New L2-08: every table point $U : I = 40{,}0\,\Omega$; slope of $I(U)$ is $\dfrac{1}{R}$ and the solution says so and why the lesson's axes give $R$ directly; $P = UI$ is given in the task text (not yet a chapter formula), 0,90 W and 3,60 W, ratio 4,0 right; 3 sf from 15,0 V and 0,375 A right; data labelled example data, not presented as PhET output.
- L2-08 d): mechanism right (filament heats, resistivity rises, Ohm's law needs constant temperature; curve bends below the line in an $I(U)$ graph); fit sentence uses the guardrail wording.
- Simulation (PhET CCK: DC) resistor is ideal, as stated; ammeter in series, voltmeter across the resistor, voltage read from the meter: right.
- answers.py: both new lines compute the physics above; asserts hold; all 20 answers recomputed in one script agree.
- Kaava steps of L1-02…L3-03 now start from $R = \dfrac{U}{I}$ or $R = \rho \dfrac{l}{A}$ and solve symbolically; L3-01 now shows $4 \rho \dfrac{l_1}{A_1} = 4 R_1$; all algebra right, numbers unchanged.
- Captions: only "(esimerkkiaineisto)" removed; reflowed Periaate and model answers identical in content.
- Hash identical at start and end.
