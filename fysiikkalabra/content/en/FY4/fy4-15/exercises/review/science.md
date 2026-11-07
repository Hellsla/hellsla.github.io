VERDICT: FAIL
CONTENT-HASH: fb42449d8c0361ed
Mode: delta (Periaate of L2-02 and L2-08 rewritten to the undisturbed-wind reference power)

## Blocking
- exercises.json:31, :104, :236 (L1-04, L2-02, L2-08 task texts) — B, internal consistency: the tasks still ask for / give "the power of the wind flowing through the rotor" (roottorin läpi virtaavan tuulen teho), while the edited solutions and the brief now define ½ρAv³ as the reference power of the *undisturbed* wind through the swept area and say the flow at the rotor is slower. With the new definition, L2-02's answer 44,9 % is a fraction of the reference power, not of the power flowing through the rotor. — Fix: in all three texts, "the power that the undisturbed wind carries through the swept area" (as in the lesson's example).
- exercises.json:243, :247 and solutions.md:224 (L2-08 feedback and model answer) — B: "ρAv, the mass of air flowing through the rotor per second" contradicts the brief's statement that the mass flow at the rotor is not ρAv. — Fix: "ρAv, the mass of undisturbed air carried through the swept area per second" (the proportionality argument is unchanged).

## Polish
- solutions.md L2-08 Järkevyys "Tuulen teho on P : η ≈ 4,9 MW" — say "vertailuteho" to match the new Periaate.

## Checked
- Recomputed: L1-04 ½ρAv³ = 480 kW; L2-02 η = 2·758 000/(1,25·5281·512) = 0,4485 → 44,9 %; L2-08 0,40·½·1,25·7854·10³ = 1,96 MW → 2 MW, reference 4,9 MW; distractors 0,2 MW and 20 kW unchanged and right.
- The new Periaate wording (undisturbed wind, swept area, reference power, η as its fraction) is physically correct and matches the brief.
- Hash identical at start and end.
