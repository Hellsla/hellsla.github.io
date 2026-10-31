VERDICT: PASS
CONTENT-HASH: 7a678bca2cd371ba

## Blocking

## Polish
- inquiry.json check-3 prompt — "explain why a high jumper is not injured" is more absolute than the model answer and criteria ("the risk of injury is lower"); same in the Finnish source ("ei loukkaannu") — "is much less likely to be injured" in both languages.
- inquiry.json siirto solution, Reasonableness — "80 N … does not hurt" echoes the retired "small force does no harm" claim — "is easily held" (both languages).

## Checked
- New mat explanation (same Δp, so same impulse of the net force; surface force = net force + weight, also smaller; longer stopping time → smaller average net force and surface force → less strain, lower injury risk) is identical in Key idea, check-3 model answer and misconception, and matches content/fi word for word in physics; no "does not harm" claim is left.
- Definitions, the derivation from ΣF = ma, N·s = kg·m/s, and momentum vs kinetic energy are correct.
- Signs (rebound −2mv) and the worked example: Δp = 3.48 kg·m/s, 870 N → 8.7·10² N, weight 0.569 N, sign slip 145 N.
- Simulation model.js was run in node: stops at Δt 0.0393/0.0785/0.157 s, F_max 80.0/40.0/20.0 N, I = Δp = −2.000 N·s; rebound I = Δp = −4.000; masses 0.5/1/2 kg give I −1/−2/−4. The half-sine pulse is consistent (v = v1(1+cos)/2 → 0, mean 2/π·F_max ≈ 0.64 F_max as stated); max compression 0.283 m < 0.32 m.
- Experiments lock m, v1 and the type and vary only the bumper (exp-1), the type (exp-2) or m (exp-3); feedback numbers match the runs.
- Retrieval 1.5 m/s; figure 9.0 = 9.0 kg·m/s; Kaava example 2.0 N·s → 1.0 m/s; find-the-error −4.0 kg·m/s; transfer 80 N (mistakes 4.0, 0.2, 800); check-2 triangle 5.4 N·s → 12 m/s (43 km/h, average 450 N = half the peak); check-1 ±120 kg·m/s.
- Exactly one correct option per choice item, distractor feedback right; exit ticket right.
- All numbers, answers and correct flags in inquiry.json, exit-ticket.json and meta.json equal content/fi (scripted comparison); hash 7a678bca2cd371ba at start and end.
