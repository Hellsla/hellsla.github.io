VERDICT: PASS
CONTENT-HASH: 9bccab069f2e3300

## Blocking

## Polish
- lesson.md:113 (pics/fy3/fy3-15-sankey.webp) — the figure says it is to scale (100 MW = 40 units). Measured in the webp (centre lines, 2.548 px per unit), the outflows are right: flue gas ≈ 41 MW, condenser ≈ 243 MW, generator ≈ 15 MW, electricity ≈ 201 MW, and the scale bar ≈ 100 MW. But the input band is only ≈ 478 MW wide (should be 500), and after the flue gas ≈ 438 MW (should be 460). The band therefore widens by about 4–5 % where it splits. No reader can see this, so it leaves no wrong picture; widen the input band to 200 units the next time the picture is regenerated.
- inquiry.json kertaus, option "Q₂ = 0", feedback — "Juuri siksi energia säilyy" reads as if releasing the heat were the reason energy is conserved. Say "Energia säilyy, joten 800 MJ = 280 MJ + Q₂".
- inquiry.json kertaus, option "1080 MJ", feedback — "Laskit lämmöt yhteen" — W is work, not a heat. Say "Laskit Q₁:n ja W:n yhteen".
- inquiry.json tyypit, generator distractor, feedback — "hyötysuhde … yli 0,95" does not match the lesson's generator-and-transformer stage, 0,945 (figure) and 0,950 (worked example). Say "noin 0,95" or "generaattorin yksin yli 0,95".
- lesson.md:132 — the second reason (not a heat engine) explains why there is no compulsory heat loss, not why the numbers cannot be compared (carried from the earlier round).

## Checked
- One script recomputed every number: kertaus 520 MJ and 0,35; chain 460/211,6/200 MW with losses 40/248,4/11,6 MW and product 0,400; the mean 0,775; the ketju answer and every one of its mistakes (270, 211,6, 288,4, 300); CHP waste 48 MW and 0,88; ΔPs/ΔPk 0,17; the 174 MW case 130 MW and 0,76, with mistake 150; pause 0,342; worked example 0,38038, 228 MW, 372 MW, condenser 306 MW, boiler 54 MW, generator 12 MW; siirto 8,64 MW, 155,52 and 164,16 MW, 5,6 %; virhe 342 and 540 MW; check-2 216 MW and 0,900; exit ticket 0,432. All agree with the text.
- The stacked CHP graph's pixel coordinates are to scale (0,6 px/MW, 1,84 px/MW). The bar chart is to scale (0,5 px/MW).
- Condenser figure: q_m is the same at both ends, T₂ = T₁ + ΔT, and P_L = c·q_m·ΔT is used where no change of state occurs. The text says P_L is not all of P_h.
- Guardrails: "siirtyy lämpönä ympäristöön" is used throughout. The heat-engine loss is "ei voi välttää kokonaan". Electrical and total efficiency are kept apart, and the different value of electricity and heat is stated.
- Each choice item has exactly one correct option, and each distractor's feedback is correct. In pred-2, Cem is correct and the other three speakers are wrong.
- Worked example: solved symbolically first, its rounding is justified and its balance check is real.
- Scope: efficiency and energy chains only, with no FY4 mechanics.
- The hash was the same at the start and at the end.
