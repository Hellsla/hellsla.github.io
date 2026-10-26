VERDICT: PASS
CONTENT-HASH: 2162817a4f5061b6

## Blocking

## Polish
- solutions.md:821 (L3-03) — the solution relies on "ideaalikaasun sisäenergia riippuu vain lämpötilasta ja määrästä", but the task never calls the gas ideal — add "ideaalikaasu" to the task text (carried over from round 1).
- exercises.json L2-04 — 2,0 kJ in 40 s is 50 W of heat into a cold jug, about 3× realistic — for example Q = 1,0 kJ and ΔU = 11 kJ (t stays 40 s) (carried over).

## Checked
- Round-2 diff (eb71c79: exercises.json, exit-ticket.json, inquiry.json) word by word: only symbols wrapped in `$…$` (Q, W, ΔU, ΔT, T, V = 75 %); every number, sign and unit is identical. The exit ticket's "+300 J", "−120 J" and "300 J − 120 J = 180 J" kept their signs and values in LaTeX.
- Experiment table headers through `inquiry.tex_name`: W (J), Q (J), ΔU (J), ΔT (K), T (K) and p/p₀ → `$p/p_0$` keep their meaning and units; "männän nopeus" and "seinät" stay words. The koe-2 capture shows the maths headers.
- One script recomputed all 12 exercises (my values = answers.py = exercises.json), plus siirto 5,4 J (mistakes 6,6 and 599,4), check-2 30 J (230 and 10), virhe 160 J, exit ticket 180 J, worked example 110 J, and the model's ΔT/W ≈ 2,79 K/J = 1/C.
- ΔU = Q + W with W done on the system is consistent in the formula, figures, worked example, solutions, hints and feedback. The content is the first law only, and W = Fs and G = mg stay within the FY3 scope.
- sim.js, sim-spec.md, lesson.md, solutions.md and answers.py are unchanged since round 1. In round 1 I ran the sim headless: slow insulated 40,8 J / ΔT 114 K, fast 47,2 J / 132 K, conducting Q = −35,1 J, p/p₀ 1,33. These still match pred-1, pred-2 and koe-2.
- koe-1 and koe-2 each lock the other parameter. simState provides W, Q, dU, dT, T and p.
- Every correct option and every feedback is physically right.
- Figures 1–3: the arrow directions, the hot → cold heat flow and the sign panels are correct.
- Hash identical at start and end.
