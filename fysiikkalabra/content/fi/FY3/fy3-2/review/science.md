VERDICT: PASS
CONTENT-HASH: 5c8a80d7c914a070

## Blocking

## Polish
- lessons/FY3/fy3-2/sim-spec.md:1 — the spec still says the work "muuttuu lämmöksi", the phrasing this round removed from the Joule figure; the student-facing sim box (`model`) already says it correctly (work raises the internal energy of box and floor) — align the spec: "kasvattaa laatikon ja lattian sisäenergiaa".
- lesson.md:287 (crane caption) — "kuorman potentiaalienergia kasvaa" names E_p, which the FY3 scope note leaves to FY4; the theory text says "nostetun kappaleen energia kasvaa" — use the same words in the caption.
- lesson.md:222 — "voimalla on siirtymän suuntainen komponentti" hints at components (cos α, FY4) while the formula section treats only a force along the motion; acceptable (C), but "voima on siirtymän suuntainen" would match the formula's condition exactly.

## Checked
- Joule figure (changed): label "työ → sisäenergia" and aria-label match the text and guardrail "heat is energy in transfer"; capture at 390 px reads correctly.
- Definitions W = Fs (constant force along the motion), area under (s,F), W = Gh = mgh at constant speed, P = W/t = Fv (uniform motion, force along it) — conditions stated where used.
- Worked example: symbolic ½F_max·s first, 4,0 J recomputed, sig. figs and average-force check right; spring-work figure to scale (40 N at 0,20 m).
- work-graphs, lift-work (F = G arrows equal, "ei mittakaavassa") and carry-lift figures agree with the text.
- inquiry numbers recomputed: 98 N, 600/1200 J, 120/30 W, 240 W, 98 J (590/490 J distractors), 180 J, 4,0 J, exit ticket 20 J — all right; exactly one correct option in each choice; distractor feedback correct.
- Joule interpret: table ratios 0,990–0,992, "simulated" source stated, 4,16 J/(g·°C) for 1850 vs 4,19 today correct; the "vesi varastoi lämmön" distractor's feedback is right.
- exp-1/exp-2: initial F = 60 N, s = 10 m, t = 5 s; locks isolate s and t; simState gives W and P.
- sim.js implements W = Fs, P = W/t, area fill linear in distance; speed control changes pace only; model box states friction = pull, constant speed.
- pred-3 / check-c2: perpendicular supporting force does zero work, air resistance neglected stated.
- Scope: no Newton's laws, E_k or work-energy theorem used.
