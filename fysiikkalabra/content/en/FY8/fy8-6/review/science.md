VERDICT: PASS
CONTENT-HASH: 53dcedb9affe67c8

## Blocking

## Polish
- lessons/FY8/fy8-6/lesson-answers.py:79 — `exit-1` computes hc/(eλ) for 470 nm (2.64 V) while exit-ticket.json asks for the violet 405 nm laser diode (3.06 V) — compute it at 405 nm so the script backs the exit ticket.
- lessons/FY8/fy8-6/lesson-answers.py:74 — the tarkistus-2 comment says "-> 6,68e-34" while inquiry.json answers 6.7e-34 with a two-figure reason — align the comment.

## Checked
- Round-1 polish fixed: the worked example now writes 1.602, 1.22, 3.00, 6.515 with decimal points; symbolic h = e(U₂ − U₁)/(f₂ − f₁) before substitution, 6.52e-34 J s, −1.7 %, round-number check 6.4e-34.
- Recomputed in one script with my own formulas: worked example 6.515e-34; aineisto fit k = 4.054e-15 V s, b = −0.050 V, h = 6.494e-34 (−2.0 %); koe-2 extrapolation 1.879 V, slope 55.6 mA/V; siirto 953.8 nm; tarkistus-2 6.675e-34; exit ticket 3.06 V; red/blue photons 1.97/2.64 eV — all agree with the text and lesson-answers.py.
- Sim model (s = 0.035 V, R = 18 Ω, U_k table) unchanged in sim.js; koe-1 currents 17.8 / 13.9 / 11.1 / 0.109 mA, blue and violet ≈ 0; koe-2 0.188 mA at 1.80 V, 6.73 mA at 2.00 V, 28.9 mA at 2.40 V match every feedback.
- Model U_k lie 0.06–0.12 V below hc/(eλ): "about 0.1 V" and the shift-not-slope argument hold; frequencies 4.76–7.40e14 Hz match the figure.
- Physics: band-gap photon hf ≈ E_g, eU_k ≈ hf, colour independent of voltage (extra energy as heat), LED band 20–40 nm vs laser diode ~1 nm, threshold by extrapolating the straight part — consistent across theory, summary, misconceptions, choices, model answers and exit ticket.
- Each choice item has exactly one correct option; distractor feedback correct (incl. virhe: forcing through origin, λ axis not linear).
- koe-1 locks U, varies λ; koe-2 locks λ, varies U; simState gives I at those values.
- Units: C·V/Hz = J s; sig-fig reasons stated; model values called model values.
