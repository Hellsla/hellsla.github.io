VERDICT: PASS
CONTENT-HASH: 946bafc94ec96ae9
none

## Blocking
(none)

## Polish
- solutions.md echo tasks (lines 5, 25, 35, 248, 259): "s = vt, s = 2d, d = s/2" is clear; the Principle could say once that s is the whole path there and back, so the symbol s is introduced before the Kaava.
- The packet diff flattens the aligned blocks; the files render as intended (checked in solutions.md).

## Checked
- All changed Kaava now start from basic equations (v = s/t, v = fλ, t = d/v) and simplify symbolically before Sijoitus.
- P/S wave distance: Δt = d/vS − d/vP = d(vP − vS)/(vP vS) gives d = vP vS Δt/(vP − vS); correct.
- Two-station task: d_A² = x² + y², d_B² = (x − 120)² + y² = d_A² − 240x + 14 400, so x = (d_A² − d_B² + 120²)/240; correct, and the algebra is shown in order.
- Bat task: s = d + (d − v_bat t) = 2d − v_bat t gives d = (v + v_bat)t/2; correct.
- Two-layer ultrasound and wave-depth tasks (v = √(gh), λ2 = λ1 √(h2/h1)) are correct.
- Added explanations (S wave absence, gel, frequency vs reflection, why v_P Δt is not the distance) are accurate and each repairs a plausible misconception.
- Substitutions, answers and tolerances unchanged.
