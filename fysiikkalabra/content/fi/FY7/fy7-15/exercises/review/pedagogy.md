VERDICT: FAIL
CONTENT-HASH: 5fb1d833ae7bc6f3

## Blocking
- exercises.json fy7-15-L2-07 text, lead over ~45 words (about 57) in one paragraph. Split points: "...Millä tulokulmalla heijastunut valo on täysin polarisoitunutta?\"" (the original problem) / "Hän kirjoittaa: \"Brewsterin laki on ... $\alpha_\text{B} = 36{,}3^\circ$.\"" (the student's solution); the final "Etsi opiskelijan virhe ..." paragraph already stands alone.
- exercises.json fy7-15-L2-05 tolerance 0.03 (and solutions.md "noin 305–323 lx on hyvä vastaus") — the accepted band 304,6–323,4 lx contains the table's first reading 322 lx, which is exactly the answer of a student who does not subtract the background, the point of the task. Fix: tolerance 0.015 (about 309–319 lx; the correct 314 and any by-eye fit with intercept 6–9 lx still pass) and change the solution's "305–323" to "noin 309–319 lx".

## Polish
- fy7-15-L1-07 and L1-08 repeat existing L1-02/03 (Malus) and L1-04/05 (Brewster) with new numbers. The plan asks for them, but a twist would help, e.g. L1-07 asking the angle for a given fraction of the intensity is L2-02, so rather use a new context (second film in a row at a known angle) and for L1-08 a material not yet used with the water-side question left to L3-02.
- fy7-15-L2-05: the question is not last ("Vähennä taustavalon osuus." follows it); move that sentence before the question.
- solutions.md fy7-15-L3-04 Järkevyys: "lukemat jäävät hieman laskettua pienemmiksi" is not true of every row (60° gives 93 vs 90, 0° gives 1 vs 0); write "lukemat poikkeavat laskennallisista muutaman W/m² verran mittausvirheen vuoksi".
- fy7-15-L3-05: "Tilanne on esimerkki." is odd; drop it. c) compares the two lenses only for glare; add one sentence that polarised glasses also halve unpolarised light while the tinted ones pass 30 %.
- Data tables use decimal points ("1.00", "0.94"); the text uses commas. Use commas if the renderer does not convert them.

## Checked
- Counts 8/7/5 reached; plan items present (sunglasses MC, Malus, Brewster, background-subtracted fit, 40 % graph reading, inverted-ratio error, three polarisers, fisherman).
- Recomputed: L1-07 98,7 W/m², L1-08 55,6°, L2-05 regression slope 313,9 lx and intercept 7 lx, L2-06 50,8°, L2-07 53,7° (36,3° = refraction angle), L3-04 120 W/m² = 12,5 % (table fits 120 sin²2θ), L3-05 36,9° and 7,144 W/m².
- L1-06 distractors (wrong direction, propagation vs vibration direction, plain tinting) are real misconceptions with repairing feedback.
- L3-04 and L3-05 are YO-style, multi-part, with every part answered in its solution; L3-04 does not repeat L3-01 (generalises it to the θ function and data).
- Only 1280 px captures are listed; no 360 px check possible.
