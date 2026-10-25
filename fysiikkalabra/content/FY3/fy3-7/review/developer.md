VERDICT: DONE

Lesson-form retrofit (lint: 3 errors, 2 warnings → 0/0; check_lesson all ok; test_inquiry 30 passed; 390 px screenshot checked, no clipped or overlapping labels).

lesson.md
- Ydinajatus: new inline SVG after the first paragraph, a schematic micro model (ordered solid, disordered touching liquid, sparse moving gas) with "sulaa" and "höyrystyy" arrows; 600×300, currentColor, 24 px text, aria-label.
- Kaava: the existing heating-curve figure brought to house style: 24 px text, `Q`, `Q = sm`, `Q = rm` as LaTeX in foreignObject, labels repositioned, aria-label says it is schematic. Curve geometry unchanged.
- Esimerkki: staged into 4 stages (Tunnetut ja kysytty · Kaava ratkaistuna r = Pt/Δm · Sijoitus, symbolic first row · Järkevyys). Numbers and the loss explanation unchanged.

solutions.md
- L3-01 and L3-02: Kaava lines symbolic (T₁, T₀, T₂ named in Annettu) and solved for the asked quantity; numbers only in Sijoitus. L3-01 Järkevyys shortened to stay under the 130-word limit. No answers changed.

No changes to inquiry.json, sim.js, exercises.json, answers.py, exit-ticket.json or tests.
