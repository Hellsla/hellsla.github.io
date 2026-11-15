VERDICT: FAIL
CONTENT-HASH: 84d6ec5cc3c7cb42

## Blocking
1. lesson.md:407 — **B**: "In a lift the normal force of the floor is in the direction of the motion and does work." This holds only for a lift moving up. In a lift moving down (check-2 and the drawing task) the normal force points against the motion and does negative work. The Summary states it as if it always held. — Write "In a moving lift the normal force of the floor is parallel to the motion, so it does work: positive when the lift moves up, negative when it moves down."

## Polish
1. inquiry.json:178 (johtopaatos prompt) — "still stops almost as far from the top", but the hook, the theory and the model answer say *equally* far (60.0 m in every row of the model table). Drop "almost".
2. exit-ticket.json:4 — "Only the component of the force along the motion does work, $W = Fs$": $W = Fs$ is the parallel-force case. Fine at this level, but "$W = F_s s$" or "the component along the displacement times the distance" would match the sentence.

## Checked
- One script recomputed every lesson and inquiry number: lift 648.6 N → 650 N and 66 kg, parachute 78.5 kJ, table x1/v/x2 for 30°/20°/10° (10.4/9.87/49.6 … 34.0/7.14/26.0, sum 60 m = h/μ, frictionless 10.8 m/s), Tutki a = 1.023 m/s² (mistakes 10.83, −0.643), worked example 8.69 m/s (13.0 m/s frictionless, a = 1.51 m/s²), siirto 95.6 kJ (mistakes 0.975, 96.62, 95 647.5), check-2 48.27 kg (61.73, 473.55), suitcase T = 150 N < 177 N.
- hissi-kuvaaja (figures.py) is consistent: 650 N for 1.0–3.0 s and 550 N for 9.0–12.18 s bring the lift back to rest (2.05 m/s ÷ 0.643 m/s² = 3.18 s).
- Hero is to scale as its caption says: both flags are 520 px horizontally from the top for a 130 px height (μ ≈ 0.25), and both slopes have tan α > μ.
- Force diagrams (kolme, esimerkki, voimakuvio blocks, malli-laukku criteria): the forces are right, the friction points up the slope, the acceleration and velocity are drawn apart from the forces, N > G when accelerating up, N = mg cos α.
- W_μ = −μmgx: its conditions are stated (straight surface, same μ, no other perpendicular force, bend and air resistance, tan α > μ).
- Every prediction, choice and check has exactly one correct option, and each distractor's feedback is right (pred-1, pred-2, kertaus, table choice, check-1, check-3).
- The energy wording follows the guardrails: "internal energy", sliding friction, no "into heat".
