VERDICT: FAIL
CONTENT-HASH: 46273f89b6b8de25

## Blocking
1. lesson.md:49 — "sijoittaa paine kilopascaleina ja tilavuus litroina. Silloin tulos on tuhat- tai miljoonakertaisesti väärä" is false: 1 kPa · 1 l = 10³ Pa · 10⁻³ m³ = 1 J, so kPa together with litres gives the right n (example: 101 · 5,0 / (8,31 · 293,15) = 0,2073 mol, the same value as in SI units). A student who checks this finds the lesson wrong. — Name a combination that really goes wrong, e.g. "Toinen virhe on sekoittaa yksiköitä: jos paine on kilopascaleina mutta tilavuus kuutiometreinä, tulos on tuhatkertaisesti väärä. Varminta on muuttaa kaikki perusyksiköiksi."

## Polish
1. lesson.md:8 — the lesson calls the bare number 6,022 · 10²³ the Avogadro constant, but L3-01 gives it as 6,022 · 10²³ 1/mol, and the lesson never writes N = nN_A, which L3-01 needs. — Write "Avogadron vakio N_A = 6,022 · 10²³ 1/mol" and add N = nN_A in display form.
2. exercises.json:90 (L3-02) — No physics problem. The method is the worked example's (n = pV/(RT), then m = nM for two gases; lesson.md:46 already does the air comparison), plus one subtraction. The "perustele" part is answered word for word in lesson.md:10 and :49. This does not break the "same task, new numbers" rule, but it is thin for level 3; the educator decides. — Turn it around: give Δm and ask for the gap volume or its thickness.
3. solutions.md:23 — the CO₂ in a cartridge is mostly liquid, not "kaasu hyvin suuressa paineessa" (L1-05 already says it is partly liquid). — "patruunassa hiilidioksidi on nesteenä suuressa paineessa".
4. sim.js:95 — the lesson's model (lesson.md:12) lets particles collide with each other; the sim leaves those collisions out. — Add "Hiukkasten keskinäiset törmäykset eivät muuta painetta, joten ne on jätetty pois."

## Checked
- R = 8,31 J/(mol·K), N_A = 6,022 · 10²³, M: He 4,0, air 29, CO₂ 44, O₂ 32, N₂ 28, Ar 40 g/mol: all correct.
- Micro-model (lesson.md:12) and exit ticket 3: point particles that interact only in collisions, pressure from wall hits, model fails at high p and low T. Correct, and no ½mv² or kT in the lesson text.
- Helium example: n = 0,2073 mol, m = 0,83 g, air 6,0 g, about 0,04 mol per litre. All correct.
- answers.py: all 12 lines use the right formula, conversions (bar, l, θ + 273,15) and gauge-pressure Δp.
- L2-03: T₂ = 555,3 °C, which implies a polytropic exponent of 1,36, realistic for a diesel (3–5 MPa, about 800 K). Three figures are justified: 30 °C fixes T₁ = 303 K to about 0,2 %. 550 or 560 °C still falls within the 2 % tolerance.
- L3-01: the "a · 10²²" format is consistent (1,298 → 1,3, within tolerance), and the composition argument is correct.
- L3-03: 0,7192 kg; about 2,64 kg at the start, so "yli neljäsosa" is right; atmospheric pressure cancels.
- solutions.md sanity checks recomputed (57 kPa gauge pressure, 1,32 g and 1,81 g, 23,9 l, 2,7 · 10²¹ O₂, 19,9 g and 14,4 g): all correct.
- sim.js calibration: wall impulse per unit perimeter = (kT/Lx + kT/Ly)/(Lx + Ly) = NkT/A exactly when ⟨vx²⟩ = ⟨vy²⟩ = kT/m. thermalize() ensures this and wall bounces preserve it. P_REF = 100 kT/(LXMAX·LY), and the prediction (N/100)(T/300)/V matches pV = nRT with n ∝ N.
- Hash unchanged before and after the review.

```
L2-03 555.3 polytropic n 1.357
L3-03 0.7192 initial kg 2.64
L3-02 5.473
example n 0.2073 kPa*l naive n 0.2073
sim 2D: wall-impulse/perimeter = 0.3318  kT/A = 0.3318
```
