VERDICT: PASS
CONTENT-HASH: 10d591ce090a7302

## Blocking

## Polish
1. exit-ticket.json:4 — "Only the component of the force along the motion does work, $W = Fs$": $W = Fs$ is the parallel-force case. Fine at this level, but "$W = F_s s$" or "the component along the displacement times the distance" would match the sentence.

## Checked
- Round 1 blocking item fixed: lesson.md:502 (Summary) now says the floor's normal force does positive work when the lift moves up and negative when it moves down, and limits "no work" to a body sliding on a stationary surface. Round 1 polish "almost" removed from the johtopaatos prompt.
- Hook (Pohdinta) no longer states how the scale reading changes; its sled sentence is consistent with h/μ.
- One script recomputed every lesson and inquiry number from the task data: lift 648.6 N → 650 N, 66 kg; parachute 78.5 kJ; Tutki a = 1.023 m/s² (mistakes 10.83, −0.643); table 30°/20°/10° x1, v, x2 (10.39/9.87/49.61, 16.48/9.24/43.52, 34.03/7.14/25.97, sums 60.0 m = h/μ), frictionless 10.85 m/s; worked example 8.69 m/s (31 km/h, h 8.55 m, 13.0 m/s frictionless, a 1.51 m/s², v² 75.6); siirto 95.6 kJ (mistakes 0.975, 96.62); check-2 48.27 kg (61.73, 473.55, G 539.6 N); suitcase T = 150 N < 177 N. lesson-answers.py agrees.
- hissi-kuvaaja: 650 N for 1.0–3.0 s and 550 N for 9.0–12.18 s return the lift to rest (2.05 m/s ÷ 0.643 m/s² = 3.18 s); capture matches.
- Force diagrams measured from the SVG: lift N/G = 1.106 ≈ (g + a)/g; parachute F_d = G; slope and worked-example N = G cos 20°, F_μ ≈ 0.2 N, G_x = G sin 20° dashed; friction up the slope from the outline; velocity and acceleration apart in their own colours; no third-law pairs on one body. F_v in the voimakuvio blocks maps to F_d via fbdspec SYMBOLS.
- W_μ = −μmgx and x1 + x2 = h/μ: conditions stated (straight surfaces, same μ, no other perpendicular force, short bend, air resistance small, tan α > μ).
- Every prediction, choice and check has exactly one correct option; each distractor's feedback names the right physics (kertaus, pred-1, pred-2, table choice, check-1, check-3).
- Worked example and numeric solutions: symbolic first, signs from the stated positive directions, rounding justified, real reasonableness checks.
- Energy wording follows the guardrails: internal energy, sliding friction, no "into heat"; the misconception and Summary agree with the theory.
