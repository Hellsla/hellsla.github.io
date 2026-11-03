VERDICT: PASS
CONTENT-HASH: 8f61e76d68ecc7d3

## Blocking

## Polish
- lessons/FY8/fy8-6/lesson-answers.py (tarkistus-2 comment) — "-> 6,68e-34 J s" while inquiry.json tarkistus-2 answers 6,7e-34 with two figures; align the comment.

## Checked
- Round 1 blocking fixed: lesson.md Kaava now says "likimain sama luku", consistent with 1,88 V measured vs 1,97 V from hc/(eλ).
- Round 1 polish fixed: laser diode line about 1 nm in text, figure (figures.py:87, alt text), glossary and exit ticket; siirto Järkevyys no longer ties 940 nm to the 0,1 V offset; ennuste-2 feedback states the energy condition, not photon creation as the gate; exit ticket "Arvioi kynnysjännite"; lesson-answers koe-2 comments 0,011 / 0,188 / 1,98 mA.
- One-script recompute: hc/(eλ) 1,968–3,062 V; LSQ k = 4,054e-15 V s, b = −0,050 V, h = 6,494e-34 J s (−2,0 %); mistakes 4,05e-15 and 1,22e-6 distinct.
- Sim model I = (s/R)ln(1+e^{(U−U_k)/s}) in sim.js matches calc text; koe-1 17,8/13,9/11,1/0,11/0/0 mA; koe-2 0,011…28,9 mA, extrapolation 1,879 V, slope 55,4 mA/V.
- Experiments isolate the varied parameter (U locked in koe-1, λ locked in koe-2); simState gives I.
- Worked example 6,515e-34 J s, −1,7 %, symbolic first, three figures justified by the differences.
- siirto 953,8 nm; tarkistus-2 6,675e-34 J s from (4,6; 1,80) and (7,0; 2,80); exit ticket 3,06 V.
- Every choice item has exactly one correct option; distractor feedback (offset shifts line not slope, λ-axis not linear, colour fixed by band gap) correct.
- Band picture, eU_k ≈ hf ≈ E_g, extra energy to heat, offset reasons; scope within FY8.
- Exercise findings in exercises/review/science.md.
