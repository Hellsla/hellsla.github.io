VERDICT: PASS
CONTENT-HASH: 1c29d0e03aeb4958

Round 1 (exercises): full review; new YO-skill task fy7-13-L2-08 (ennuste muutoksesta), the rest of the set PASS before. Checked from the text only; no renders.

## Blocking

## Polish
- exercises.json:247 (L2-08, option "3-kertaiseksi") — "varjostin siirtyy puolet lähemmäs" is clumsy — fix: "varjostimen etäisyys hilasta puolittuu".
- solutions.md:172 (L2-08) — "tangentti on jo selvästi siniä suurempi" at 11,2° is a 2 % difference — fix: "tangentti on jo noin 2 % siniä suurempi".
- Carried over: L3-05 "0,36 % pienempi" precision; integer-answer step rule (tooling); plan's picture questions.

## Checked
- Hash 1c29d0e03aeb4958 at start and end.
- L2-08 physics: d₁ = 1,00 · 10⁻⁵ m, θ₁ = 3,727°, x₁ = 2,00 m · tan θ₁ = 13,03 cm (the given 13,0 cm agrees); d₂ = 3,333 µm, θ₂ = 11,24°, x₂ = 19,88 cm; ratio 1,526 → "noin 1,5-kertaiseksi" right.
- L2-08 distractors recomputed: 3 · 2 = 6 (screen read the wrong way), 3 (screen ignored), 1/2 (grating ignored), 1/3 · 1/2 = 1/6 (denser grating read as bending less). Each feedback names its own error correctly.
- Form: all five options have the same form; the correct one is not the longest. Direction (kasvaa/pienenee) stated in each option.
- Solution: complete, θ from the grating equation before x = L tan θ, tan used (not sin) as the lesson teaches, small-angle cross-check 3 : 2 = 1,5. Display lines under about 300 px (text estimate).
- answers.py output equals exercises.json for all 18 numeric answers; the new comment line agrees (13,03 → 19,88 cm, 1,53).
- Scope: grating equation and tan θ = x : L from this lesson only.
