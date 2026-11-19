VERDICT: PASS
CONTENT-HASH: 3c2b769c96eb1c66

## Blocking

## Polish
- lessons/FY3/fy3-3/lesson-answers.py:1 — computes only the retrieval item (20, 8); the worked example (−270 °C), siirto (122; mistakes 404, 83,8), virhe (128 kPa, 1,07), check-c2 (1,035) and check-2 (−273 °C) are not computed there — add them (all recomputed correct here).
- content/fi-easy/FY3/fy3-3/inquiry.json:102 — pred-2 feedback on "seinää on vähemmän": "hiukkaset palaavat seinälle nopeammin" holds for the walls the piston moves towards; for the top and bottom walls the same hits fall on a shorter wall. Could say "osumia on enemmän seinän pituutta kohti" without the return-time cause.
- content/fi-easy/FY3/fy3-3/inquiry.json:382 — check-2 hint 2: "…\theta}$, Paine on nolla" (comma then capital); make it two sentences.
- content/fi-easy/FY3/fy3-3/inquiry.json (pr-pumppu) — ΔT for a Celsius difference and the answer "20 °C" are acceptable; this chapter introduces the kelvin, so the correct feedback could add "= 20 K".

## Checked
- One script: worked example endpoints k = 0,37 kPa/°C → θ₀ = −270,3 °C (least squares −271 °C; data agree with p ∝ T within 0,4 kPa); 2 s.f. justified.
- siirto 121,67 → 122 kPa; mistakes 404 (Celsius ratio) and 83,84 (inverted) match; virhe 128,2 kPa; check-c2 3,5 %; check-2 −273 °C; pred-1 ×2 and √2 = 1,41; 327/27 = 12,1.
- Conditions stated where used: p ∝ T for thin gas at constant V and n; KE ∝ T for thin gas; Mallin rajat (liquids/solids, interaction energy, ice vs water at 0 °C, motion does not stop at 0 K) matches the guardrails.
- Causality: V↓ → more frequent hits, same impulse; T↑ → more frequent and harder hits; consistent in theory, sim boxes, feedback, exit ticket, model answers.
- Every choice item has exactly one correct option; each distractor's feedback names the actual error.
- sim.js: 2D impulse per time per wall length averaged over both axes gives exactly N v²/(2A); pRef uses the same effective width, so pRel fluctuates about pTheory = 100(T/300)/V; speed control changes only pace; window reset on state change. Simplifications (2D, no collisions, one speed) are stated in Mallin oletukset.
- exp-1 (V locked 1,0, T varied, 150–600 K reachable) and exp-2 (T locked 300 K, V 2,0 → 1,0) isolate their variable; simState has theta, vRel, pRel, pTheory.
- Figures: kelvin scale to scale (328 px/273,15 K = 1,20 = 120 px/100 K); extrapolation plot points at 100…137 kPa, dashed line to −270 °C, axis at −300 °C as the text says; micro-model schematic, same count of particles.
- Scope: FY3 central contents (systeemi, tilanmuuttujat, lämpötila); pressure only as F/A from collisions.
- Hash identical at start and end.
