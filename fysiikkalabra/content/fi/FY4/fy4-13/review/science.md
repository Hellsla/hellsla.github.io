VERDICT: FAIL
CONTENT-HASH: d1d8ce15626f5d7b

## Blocking
- content/fi/FY4/fy4-13/lesson.md:411 (Tiivistelmä, third bullet) — **A**: every `\frac` in this bullet is a literal TAB followed by `frac` (an escaped `\t` in the source; preview/fy4-13.html carries it too). The page therefore shows all four summary formulas wrong: a, T for the cart and for the two hanging bodies come out as `frac{m_2}{m_1+m_2}g`, and so on. The latex check did not catch it. — Replace each TAB+`frac` with `\tfrac` (or `\frac`), then grep the lesson files for `\t` characters.

## Polish
- lesson.md:406 / exit-ticket.json:3 / lesson.md:301 — The reason T₁ = T₂ is worded three ways: "koska lanka on kevyt", "kevyt lanka ja kitkaton väkipyörä", and "lanka kevyt ja väkipyörä kitkaton". Use one wording everywhere: "kevyt lanka ja kevyt, kitkaton väkipyörä" (guardrails: one explanation, the same words).
- lesson.md:404 — "osa sen painosta kuluu … kiihdyttämiseen" treats a force as something used up. Better: "punnuksen kokonaisvoiman $G_2 - T = m_2 a$ on osoitettava alas, joten $T < m_2 g$".
- inquiry.json:186 (exp-1 solution, Vastaus) — The rounding reason is muddled ("kaksi merkitsevää … kuten … 3,27 N"). In a difference, the decimal places decide: 4,9 N has one decimal, so the answer is 1,6 N.
- inquiry.json:398 (siirto, Järkevyys) — "Punnus on kevyempi kuin kärry, joten kiihtyvyys jää alle g" is a non sequitur: a < g for every mass. What the lighter weight gives is a < g/2.
- Sim readout shows ΣF₁ and ΣF₂ directly. That makes the exp-1 and exp-2 questions ("laske taulukon arvoista") a read-off rather than a calculation. The physics is right; whether this matters is the pedagogy reviewer's call.

## Checked
- Recomputed every lesson and inquiry number in one script (scratchpad recompute.py): pred-1/2, exp-1/2 (1,635 N; 0,736 N), aineisto 3,27 N, siirto 0,3073 kg, check-1 3,27, check-2 3,363 N, check-3 3,27 m/s² and 5,23 N, Esimerkki 2,80 m/s² and 4,20 N. All are correct, and each rounded student answer stays inside its relative tolerance.
- Distractors and mistake values (0,2446; 0,2032; 4,48; 5,61; 1,63) are each really wrong, and each feedback names the right error. Exactly one option is correct in kertaus, pred-1, pred-2, virhe and check-1.
- Force diagrams (tilanne, esimerkki, atwood, malli-atwood, virhe): one diagram per body, and each body is a rectangle. G is drawn from the centre, N from the contact surface beside G, T from the attachment point. Arrows are to scale (checked against px lengths). T₁ and T₂ are explicitly *not* a third-law pair. v (blue) and a (orange) are drawn beside the bodies, never as forces. virhe has exactly one error, G₂ drawn on the cart.
- sim.js implements the same model for both situations, including m₁ > m₂ (dir). simState carries T, a and G1 at every experiment value. Equal masses do not start, which is stated. exp-1 and exp-2 lock tapa and m2 and vary only m1.
- Conditions (light, inextensible string; light, frictionless pulley; no friction or air resistance) are stated in Ydinajatus, Esimerkki, sim model, siirto and checks. Conventions hold: overline vectors, \cdot, no ×, LaTeX symbols.
- Scope: FY4 "voimakuvio ja liikeyhtälö", slot example F.
- Hash d1d8ce15626f5d7b at start and end.
