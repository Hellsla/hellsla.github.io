VERDICT: DONE

Lesson-form retrofit (lint: 5 errors, 1 warning → 0/0).

lesson.md
- Ydinajatus: new inline SVG after the micro-model paragraph: two equal containers with the same six particles, short velocity arrows (kylmä kaasu) vs long ones (kuuma kaasu), labels $p_1$ and $p_2 \gt p_1$ in foreignObject; a one-line caption says it is schematic.
- Kaava: new to-scale SVG of the kelvin and celsius scales side by side (0 K / −273,15 °C, 273,15 K / 0 °C, 373,15 K / 100 °C) with $T = \theta + 273{,}15$ between them; all values with units in foreignObject LaTeX.
- Esimerkki: problem now ends with the question; five stages (Kuvaaja · Kulmakerroin · Kaava ratkaistuna · Sijoitus · Järkevyys). Slope and θ calculations start with symbolic rows (k = Δp/Δθ, θ = −p₀/k); p = p₀ + kθ is in display. Text, graph and all numbers unchanged.

answers.py (new): reproduces every existing exercise answer, so the WARN is resolved; no number changed.

solutions.md, inquiry.json, sim.js, exercises.json, exit-ticket.json, tests: unchanged (solutions had no lint findings; section titles kept).

check_lesson: all ok; test_inquiry: 30 passed; 390 px figures checked for overlap/clipping.
