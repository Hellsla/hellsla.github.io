VERDICT: PASS
CONTENT-HASH: e40ec7d73b508925

## Blocking
(none)

## Polish
- lesson.md:26 — The ice and steam segments are flatter than the water segment, but their c is about half of water's, so they should be about twice as steep. The sim shows the correct slopes, so the two curves disagree. — Use e.g. `points="70,230 85,200 135,200 200,110 480,110 495,70"` and end the dashed 0 °C line at x=135 (line 27).
- lesson.md:33 — The melting plateau says only "sulaa", while the boiling plateau shows "Q = rm". — Label it "sulaa, Q = sm" so the student sees the two flat parts are the same idea.
- lesson.md:10 — L2-02, L2-04 and L3-01…03 need c for water, which appears only in fy3-6. — Add a short table after the formula: s and r for water; c for ice 2100, water 4190, steam 2000 J/(kg·K).
- exit-ticket.json:8 — The micromodel goal is not tested anywhere. — Extend the q2 answer: "…energia kasvattaa hiukkasten välistä vuorovaikutusenergiaa, ei liike-energiaa, joten lämpötila ei nouse." Or ask for this in L1-05.
- lesson.md:12 — The phase diagram gets one sentence, no figure, and a new word ("sublimoitumispisteet"). — Add a small (T, p) schematic with three labelled regions and a normal-pressure line, or keep only "kiehumispiste riippuu paineesta".

## Checked
- Lint: 0 errors, 0 warnings.
- Prerequisites cover what the lesson assumes: the micromodel and U = kinetic + interaction energy (fy3-5) support line 8, and P = W/t (fy3-2) supports Q = Pt.
- Motivating question (line 3) is one a student would ask; line 8 answers it.
- Each core-idea paragraph adds one idea. The ratios (line 10) and the 80 °C figure (line 50) are correct.
- The example covers the thematic goal (heater, open calorimeter, scale).
- Level 1: 5 problems, each one formula or one graph reading.
- Level 2: 4 problems, each a rearrangement with a conversion or two steps. L2-01 solves for t, not r, so it does not repeat the example.
- Level 3: 3 problems, each combining two ideas with reasoning.
- Exit ticket tests the formula, the constant temperature and the heating curve.
