VERDICT: PASS
CONTENT-HASH: f1306d3bece1b9c4

## Blocking

## Polish
- inquiry.json check-3 model — "Hissin nostovoima on kuorman painon suuruinen" holds only while the lift moves at constant speed (the theory states this condition before W = Gh); the work result itself is right because the lift starts and stops at rest — add "tasaisella nopeudella" so the model answer does not suggest F = G during acceleration.
- sim-spec.md — "työ muuttuu lämmöksi" contradicts the guardrail (heat is energy in transfer); the student-facing sim `model` box already says it correctly ("kasvattaa laatikon ja lattian sisäenergiaa") — align the spec with it.
- inquiry.json pred-1/pred-2 prompts, check-2 "30 N", virhe "40 N" — a few numbers with units still plain text after the LaTeX conversion (not a physics issue).

## Checked
- Definitions: work as force along the motion × distance, W = 0 for the perpendicular carrying force, Joule's experiment as work → internal energy; heat as transfer, never stored (Joule distractor feedback correct, guardrail wording).
- Scope: no E_k/E_p/cos α; W = mgh introduced with the constant-speed condition and G = mg from the previous chapter; P = Fv with its condition (uniform motion, force along motion).
- Recomputed in one script: pr-paino 98 N, pred-1 600/1200 J, pred-2 600 J and 120 → 30 W, Aino 1,96 kJ, worked example ½·40 N·0,20 m = 4,0 J, siirto 240 W, check-1 ratio 3, check-2 180 J, exit ticket 98 J and 20 J — all agree.
- Joule table: ΔU/W = 0,990–0,992 every row, consistent with the "same-direction small loss" feedback; Joule 1850 ≈ 4,15–4,16 J per g·°C, modern 4,19 J correct; data labelled invented.
- Exactly one correct option in pr-paino, pred-1, pred-2, pred-3, Joule question, virhe, check-1; every distractor's feedback names the right reason.
- Experiments: exp-1 locks F,t and varies s; exp-2 locks F,s and varies t; simState carries W and P at the initial 60 N, 10 m, 5 s.
- sim.js implements W = Fs, P = W/t, area filled linearly with u; speed control changes pace only; model box states friction = pull, constant speed, values are model values.
- Worked example: seven stages, symbolic first, conversion cm → m, 2 s.f. justified, real check with the mean force; spring-work figure to scale (0,20 m and 40 N ticks verified).
- Kiuas sentence: electrical energy → internal energy → transferred as heat, guardrail-consistent.
