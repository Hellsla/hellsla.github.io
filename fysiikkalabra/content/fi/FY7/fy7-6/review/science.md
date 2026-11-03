VERDICT: FAIL
CONTENT-HASH: a32bd82d8c0f6140

## Blocking
- lesson.md:163, inquiry.json:90 (ennuste-rako, the correct option's feedback), sim-spec.md — **A, internal consistency.** These say the slit tube's magnet "putoaa lähes vapaasti", that 0,82 s is "lähellä muoviputken 0,45 s:a", and that "rako poistaa lähes koko jarrutuksen". The lesson's own model says otherwise (k/10, vt = 1,5 m/s). The fall takes 1,8 times as long as free fall, and Q = 173,9 mJ, so 89 % of the 196,2 mJ still becomes internal energy (Ek is 22 mJ, against 196 mJ in plastic). koe-2 has students record Q, so they will see 196,0 and 173,9 mJ, which contradicts "nearly free". The johtopäätös model answer does not mention the slit tube's Q. — Fix: either write "putoaa paljon nopeammin kuin ehjässä putkessa", drop "lähellä muoviputken", and add one sentence to the model answer: the magnet still reaches a terminal speed, and most of the energy still becomes internal energy, but the fall takes about an eighth of the time. Or lower the slit k (e.g. k/100) if the model is meant to show near free fall. A real slit tube still brakes, so prefer the wording fix.

## Polish
- lesson.md:160 and the glossary `induktiojarru` — the claim that the braking force grows with speed holds below the brake's critical speed (low magnetic Reynolds number). Real high-speed train eddy-current brakes are past that region. — Write "pienillä vauhdeilla" or "putkikokeen kaltaisissa tilanteissa", or leave it as a level-appropriate simplification.

## Checked
- Ring figure: current direction, B_ind and the repelling N face are correct, and so is the receding case.
- Tube figure and sim rings: anticlockwise from above with B_ind up below the magnet (repels N), clockwise with B_ind down above it (attracts S).
- sim.js: F_j = kv; the closed form y(t), v(t) agrees with my numerical integration: muovi 0,45 s and 4,43 m/s, alumiini 4,24 s, kupari 6,68 s, rako 0,82 s. Q = ΔEp − Ek; steel falls freely.
- Al/Cu k ratio 0,633 from σ and the model limits are stated; energy figure to scale.
- Worked example: Q = 0,29402 J → 0,29 J; Ek is 0,1 %; ΔT ≈ 0,003 K.
- siirto 21 kN; mistakes 25/9/42 kN; a = 8,75 m/s²; ΔEk 630 kJ.
- tarkistus-2 42 mW and its mistakes; virhe and check-1 have exactly one right option each.
