VERDICT: PASS
CONTENT-HASH: 1fd82ba49312a3cf

## Blocking

## Polish
- content/fi/FY7/fy7-15/lesson.md:587 (Esimerkki, Tulos) — "kolmella merkitsevällä numerolla kuten intensiteetti 840" names only the intensity. The angle 35° has two significant figures, and ±0,5° moves I₂ over 278–285 W/m². — Fix: "kolmella merkitsevällä numerolla kuten intensiteetti $840\,\text{W/m}^2$; kulma $35^\circ$ katsotaan tarkaksi."
- lessons/FY7/fy7-15/lesson-answers.py:39 — the comment "≈ 359 lx" disagrees with the fitted slope 360,72 lx that the script computes and that inquiry.json uses (360,7). — Fix: "≈ 360,7 lx".
- Scope: numeric Malus tasks beyond "kvalitatiivisesti" stay the teacher's call (round 1).

## Checked
- Round-1 blocking fix: the third misconception now says "lisäkalvo voi vain vähentää läpi tulevaa valoa". This agrees with the theory ("absorboi") and with ennuste-kolme's distractor and feedback.
- One script recomputed every number with my own formulas, and all agree: Malus 0,75/0,50/0,25; Brewster 53,1°/36,9° (by Snell's law, not 90° − α_B)/56,3°; worked example 281,8 → 282 W/m²; koe-1 37,5 % and its mistakes 75/43,3/33,3; ennuste values 46,7/37,5/12,5; koe-2 12,5 % (9,375 % at 30°); virhe 25/50; siirto 2,128 m and its mistakes 1,203/1,279; tarkistus-2 2,066 mW and its mistakes 3,214/1,033/2,934; exit ticket 56,3°.
- mittaus after the developer's edit: a least-squares fit gives A = 360,72 lx, B = 14,64 lx and ΔA = 2,37 lx, with residuals within ±3 lx. The solution's graph reading through (0; 15) and (1,0; 375) lies on the fitted line (375,4 at 1). The slope is read from the line, not from raw points, as the guardrails ask.
- fig-5 points and line to scale; mittaus is badged `example`, not presented as measured.
- Mechanisms are correct: the film's chains absorb the field component along them, unpolarised light is halved because of the even split, I ∝ amplitude², and reflected light is s-polarised (parallel to the surface, perpendicular to the plane of incidence). Sunglasses, LCD, phone and 3D are right.
- sim.js: I₁ = 50 %, then Malus stage by stage. d and cos² are right for two sheets, and simState gives i1, i2 and i3 for koe-1 (n = 2, θ₁ locked) and koe-2 (n = 3, θ₁ and θ₃ locked). Limits stated in `model`.
- Each choice item has exactly one correct option, and every distractor's feedback is right. The explain model answers, criteria and exit ticket match the theory.
