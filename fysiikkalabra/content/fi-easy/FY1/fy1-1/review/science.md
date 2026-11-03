VERDICT: PASS
CONTENT-HASH: c665aaeaf308581a

## Blocking
(none)

## Polish
- content/fi-easy/FY1/fy1-1/lesson.md:94 and meta.json:34 (key_concepts "suuruusluokka") — "kymmenpotenssi, joka on lähimpänä lukua" / "lukua lähin kymmenpotenssi" read on a linear scale puts $4{,}0\cdot10^{16}$ nearer $10^{16}$ (3·10¹⁶ away against 6·10¹⁶), which goes against check-1. The lesson states the a ≈ 3 rule in the next sentence, so this is not blocking, but the key-concept box stands on its own → "se on kymmenpotenssien akselilla lukua lähin kymmenpotenssi" (in both places; the summary already says this). The 170 → $10^{2}$ example is correct under either reading.
- content/fi-easy/FY1/fy1-1/inquiry.json:40 (kertaus, option $0{,}0001$) — "Luvussa $10^{-3}$ on ykkösen jälkeen kolme desimaalia. Viimeinen niistä on ykkönen" contradicts itself → "Luvussa $10^{-3}$ on pilkun jälkeen kolme desimaalia. Viimeinen niistä on ykkönen: $0{,}001$."
- content/fi-easy/FY1/fy1-1/inquiry.json:419 (siirto) — "Auringon säde on $7{,}2^\circ$ kulmassa" can be read as the Sun's radius → "auringonsäteet tulevat $7{,}2^\circ$:n kulmassa tikkuun nähden".

## Checked
- The S2 additions are correct: 170 = 1,7·10² gives $10^{2}$; $10^{3} = 1000$ (key_concepts, prior); human gives $10^{0}$ and Everest $10^{4}$; the a ≈ 3 threshold matches round(log₁₀) (√10 ≈ 3,16) and the glossary.
- key_concepts malli, kymmenpotenssi, alkeishiukkanen and perusvuorovaikutus match the glossary and the theory.
- Recomputed: example k = 6,47·10⁴, Δn = 5; exp-2 Δn = 8; exp-3 midpoint −4 with hair n = −4; reflect 42 and 62; siirto 12 732 km (the mistakes 40 000, 6366 and 111 km); check-2 57 917; virhe 109 and about 1,3·10⁶ Earths; p–p Coulomb/gravity ratio 1,2·10³⁶.
- Sgr A*: 2GM/c² with 4,3·10⁶ M☉ gives a diameter of 2,5·10¹⁰ m. Heliopause 120 AU is 1,8·10¹³ m, the Oort cloud 10⁵ AU is 1,5·10¹⁶ m, and the Oort cloud is 17–830 times as far as the heliopause ("kymmeniä tai satoja"). 93 Gly is 8,8·10²⁶ m.
- sim.js: kohdeExp = round(log₁₀ m), and mainObj matches the initial objects of exp-1, exp-2 and exp-3 (water, Earth, universe). The fade threshold (a ≥ 0,5 at S ≈ 0,47 px) gives about 1/1000, which agrees with calc.
- Scale-axis figure: every position is at the right exponent (11,8 px per decade). The ladder, the stadium and pea ratio (4·10⁴) and the cosmic-address sizes are right.
- Each prediction and choice has exactly one correct option, and every distractor's feedback gives the right physics (neutron star, K-40 β⁻ decay, nucleus held by the residual strong force).
- The model's limits (rounded values, the quark's upper limit, observable vs whole universe) are stated where used.
