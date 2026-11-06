VERDICT: PASS
CONTENT-HASH: 4e883ea054d82bf0

## Blocking

## Polish
- content/fi/FY4/fy4-2/exercises/exercises.json:283 (L2-08) — the text opens with "Esimerkkiarvot:", which reads as if the numbers were not the task's data — drop the prefix ("Pyöräilijä ajaa …").
- exercises.json L2-08 choices — no distractor touches this chapter's warned mistakes (a = 0 when v = 0; negative a always slowing); they test the s ∝ v₀²/a dependence instead. Acceptable for this form; optionally make the "Pysyy samana" feedback name the sign idea ("pienempi hidastuvuus" ≠ shorter stop).
- lessons/FY4/fy4-2/answers.py:40 — the other multiple-choice answers (L1-06, L1-08, L2-07) are recorded as strings, L2-08 is not — add `a["fy4-2-L2-08"] = "Kasvaa 2-kertaiseksi"` with the comment s = v₀²/(2|a|): 8,0 m → 16 m.
- content/fi/FY4/fy4-2/exercises/solutions.md:193 (L2-08) — "Jarrutusmatka on … pinta-ala" is the displacement; true here because v > 0 throughout — add "koska nopeus on koko ajan positiivinen".

## Checked
- New task fy4-2-L2-08 (Ennuste muutoksesta, type 6): recomputed s = v₀²/(2|a|) = 64/8 = 8,0 m and 64/4 = 16 m, ratio 2; t = 2,0 s and 4,0 s; check 32 m − 16 m = 16 m. Exactly one correct option.
- Physics: uniform deceleration, positive direction = motion, a negative, t = (0 − v₀)/a sign-consistent; magnitudes realistic for a bicycle (4 m/s² dry, 2 m/s² wet).
- Distractors: 4× (t doubled, squared, a halving forgotten), ½ (dependence read backwards), unchanged (only v₀ counted); each feedback says why. The correct option is not identifiable by form (four short parallel phrases); its feedback adds only the times and distances.
- Scope: triangle area under (t,v) and x − x₀ = v₀t + ½at² are both taught in this chapter; no v² = v₀² + 2as needed.
- Solution complete (Kysytty/Periaate/Mallivastaus), symbolic first, real check with the second formula; notation v₀, a, t, s as in the lesson.
- All 21 answers: answers.py run once and compared: 17 numeric answers within tolerance; MC answers L1-06, L1-08, L2-07 match their correct choice text; L2-08 one correct choice.
- Inline formulas (text only, not rendered): the longest, s₂ = 8,0 m/s · 4,0 s + ½ · (−2,0 m/s²) · (4,0 s)², is ≈ 350 px unbroken; KaTeX can break inline math after "=" and "+", so pieces stay ≈ 200 px. Visual should confirm at 390 px. The 360 px layout check passed.
- Hash identical at start and end.
