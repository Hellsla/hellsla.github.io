VERDICT: PASS
CONTENT-HASH: 1aca946ad8dad687

## Blocking
None.

## Polish
1. inquiry.json siirto, hint 3 writes the law as L = 10 dB · lg(...) while the lesson states the MAFY form; equivalent, but the hint could use 10 lg(...) dB for consistency.
2. sim-spec.md and lesson-answers.py docstring still write L = 10 dB · lg(I/I₀) (not student-facing).

## Checked
Full review (lesson.md, inquiry.json, exit-ticket.json, figures, sim-spec.md, sim.js). L = 10 lg(I/I0) dB is MAFY's form and equivalent to the old one; the derived forms (difference, I = I0·10^(L/10 dB)) follow correctly, including the "divide by 10 dB" step. Conditions stated where used: point source, no reflections or absorption, independent sources, free field for treating the meter reading as intensity level; dB(A) and sound-pressure level explained without error. Recomputed in my own script: worked example 3,98·10⁻³ W/m², P = 5,00 W (1 dB ≈ 26 %); 70+60 dB → 1,1·10⁻⁵ W/m², 70,4 dB; 80+80 → 83 dB; sim and experiments 2 m 90,0, 4 m 84,0, 8 m 77,9 dB, I 0,995 → 0,249 mW/m², N = 2/4/10 → 93,0/96,0/100,0 dB; error item 6,5 I0 ≈ 8 dB vs 3,16·10⁻⁶ W/m²; transfer 0,969 dB (mistakes 3,0, 1,76); check 2: 100 (mistakes 1,4, 20); exit 1,0·10⁻⁴ W/m², 84,8 dB; all match lesson-answers.py. Sim computes I = NP/(4πr²) and L directly, simState gives ImW and L; P, N locked in koe 1, P, r in koe 2. Each prediction has one correct option; perception claims (10 dB ≈ twice as loud, 6 dB ≈ a third quieter, 20 dB ≈ four times) are right. Compared with fi: every number, correct option, tolerance, unit and experiment setup is identical (scripted comparison); the shorter sentences keep each causal step.
