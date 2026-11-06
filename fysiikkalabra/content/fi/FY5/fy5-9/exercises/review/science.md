VERDICT: PASS
CONTENT-HASH: 628ca4af401209e3

## Blocking

## Polish
- fy5-9/exercises/exercises.json:20 (L2-08, correct reason and reason 1 feedback) and solutions.md:191 — "jousen voima riippuu vain poikkeamasta" and "Jousen voima −kx on Kuussa sama". For a vertical spring, the spring force at equilibrium equals the weight, which is smaller on the Moon. It is the net restoring force about the shifted equilibrium that is −kx. Write "jousivärähtelijän palauttava voima $-kx$ riippuu vain poikkeamasta tasapainoasemasta", which matches the lesson's "paino siirtää vain tasapainoasemaa".
- exercises.json:20, choice 4 feedback — "Tässä on sekoitettu massa ja paino" does not describe the mistake. The mistake is assuming that the pendulum depends on mass. Suggest: "Tässä on oletettu, että heilurinkin jaksonaika riippuu massasta."

## Checked
- New task L2-08 (type 1, two-stage): √(9,81/1,62) = 2,461, so T_K = 2,46 s. The spring period stays 1,00 s, because T = 2π√(m/k) has no g. The answer string equals the correct option.
- Exactly one option and one reason are correct. Reason 4 is a true statement that does not explain the answer, as the type requires. The correct option's feedback gives the numbers but not the reason.
- The distractors catch the lesson's warned mass idea (choice 4, reason 3) and a missing square root (×6). Lengths and hedging are similar across the options, and no option stands out by form.
- The assumptions are stated in the task: small swings, no air resistance, the same length, spring and masses.
- The phantom-aligned ratio chain in the solution is three short lines. From the text it fits 300 px. I did not render it.
- answers.py ran once. All numeric answers agree with exercises.json within tolerance.
- The hash was the same at the start and at the end.
