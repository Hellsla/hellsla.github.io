VERDICT: PASS
CONTENT-HASH: 120a47aa4437ec30

## Blocking

## Polish
- inquiry.json ennuste-rako, correct option feedback — the slit-tube fall time, 0,82 s, is "noin kaksinkertainen" the plastic tube's 0,45 s. The ratio is 1,8. — "lähes kaksinkertainen" would be more exact.
- lesson.md:160 and the glossary `induktiojarru` (carried over from round 1) — the claim that the force grows with speed holds below the brake's critical speed. — Add "pienillä vauhdeilla", or keep it as a level-appropriate simplification.

## Checked
- Round-1 blocker fixed. lesson.md:263 now says the magnet "putoaa paljon nopeammin" and that the braking "ei katoa kokonaan". The ennuste-rako feedback drops "lähellä muoviputken". The johtopäätös model answer adds "rakoputkessakin Q = 173,9 mJ". sim-spec says "heikentää jarrutusta selvästi mutta ei poista sitä". All of these agree with the model (k/10, vt = 1,5 m/s), and no "lähes vapaasti" is left.
- My independent numerical integration of m dv/dt = mg − kv agrees: muovi 0,45 s, alumiini 4,24 s / 195,6 mJ, kupari 6,68 s / 196,0 mJ, rako 0,82 s / 173,9 mJ, and ΔEp is 196,2 mJ.
- sim.js is unchanged since round 1: closed-form y(t) and v(t), Q = ΔEp − Ek, steel falls freely, and the Al/Cu ratio is 0,633.
- Ring and tube figures: the current directions, B_ind and the induced poles are right for both approach and recession.
- Worked example: Q = 0,29402 J → 0,29 J, Ek is 0,1 %, ΔT ≈ 0,003 K.
- siirto: 21 kN, with mistakes 25/9/42 kN. tarkistus-2: 42 mW, with mistakes 4,32/0,518.
- virhe and check-1 each have exactly one correct option, and every distractor's feedback is right.
