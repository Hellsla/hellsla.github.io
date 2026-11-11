VERDICT: PASS
CONTENT-HASH: 77345b49fdf269d8

## Blocking

## Polish
- lesson.md:322 — "directly proportional to the mean kinetic energy of the particles": air, N₂ and CO₂ also rotate. — use the guardrail wording, "the mean kinetic energy of the particles' motion from place to place".
- inquiry.json punnitus solution, Reasonableness — "$5.00 \cdot 0.041$" has no unit or source. — "about $0.041\,\text{mol}$ per litre ($1/24\,\textsf{l/mol}$)".
- inquiry.json taulukko — row 3 is $3.91$, $2\,\%$ low; my sim run gave $3.98$. It is within the noise, so optional.

## Checked
- Recomputed every number in one script with my own formulas, and all match: the four m/M values, R from the mean (8.32) and from He (8.302) with the C/l/kPa mistakes, the worked example (0.2073 mol, 0.83 g, air 6.0 g, 24 l/mol), virhe, siirto (2645 kg; mistakes 9870 and 2.64; the 3360·293/373 check), check-c2 (1.068), check-2 (3.0, 2.25, 1.69), the exit ticket (0.601 mol), exp-2 (50, 70.7, 4.00, 0.50) and every pV/(NT) entry in taulukko.
- Sim physics: 2D kinetic theory p = NkT/A, the impulse per perimeter length, ⟨vx²⟩ = ⟨vy²⟩ = kT/m kept exactly, v ∝ √T, and an isothermal change of V (stated in the model box).
- Ran the preview in Playwright with simAdvance(20): measured/model is 0.975–1.046 over 9 states, including exp-1, exp-2 and check-2's state. At N = 20 the 2 s averages vary by ±14 % (sd 6 %), so the "≈ ±10 %" claim holds.
- exp-1 and exp-2 lock T and V and vary only N, and simState gives pMeasured and hitRate. The new exp-2 tolerance of 0.1 accepts only N = 50 on the step-10 slider.
- Figures to scale: the He/air arrows are 2.67 against √(29/4) = 2.69, the mole bars 7.25 and 11.0, the 2T arrows √2 longer, 2N has twice the particles, V/2 half the height.
- Exactly one correct option in each choice. The distractors' feedback names the real mechanism (hit rate against momentum per hit, no particle collisions).
- Limits (high p, low T), absolute pressure, kelvins and 1 kPa·l = 1 J are stated where they are used, and the lesson stays within FY3's central contents.
- The weighing data is labelled invented, and the sim's numbers are called model values.
