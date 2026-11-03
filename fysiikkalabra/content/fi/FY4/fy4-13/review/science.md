VERDICT: PASS
CONTENT-HASH: fd519394807ca743

## Blocking

## Polish
- inquiry.json:196 (exp-2) and :115 (sim calc box) — exp-2 asks for m_1 = 1,0 kg with m_2 = 0,50 kg, where m_1 is the heavier body, but the calc box and the theory state the two-body formulas for m_2 > m_1 only (the sim correctly uses |m_2 − m_1| and flips the direction) — add to the calc box: "jos m_1 > m_2, kappaleet vaihtavat rooleja: m_1 laskee ja m_2 nousee".
- exit-ticket.json:9 — "Paino on alas ja jännitysvoima ylös, joten jännitysvoima on pienempi kuin paino": the directions alone do not imply T < m_2 g; the reason is that the net force m_2 a points down — write "koska punnus kiihtyy alas, m_2 g − T = m_2 a > 0, joten T < m_2 g".
- inquiry.json:263 (exp-2 solution, Vastaus) — "kolme merkitsevää numeroa kuten taulukon lukemissa, mutta erotuksella on vain kaksi" is confusing — say "Erotuksessa ratkaisevat desimaalit: lukemat ovat sadasosan tarkkuudella, joten 0,74 N".
- inquiry.json:428 (check-1, g-distractor) — "kokonaisvoima on paino miinus jännitysvoima" holds for the lighter body only as a signed (negative) value — "kummankin kokonaisvoima on painon ja jännitysvoiman erotus, joten kiihtyvyys on pienempi kuin g".
- lesson.md (Ydinajatus, T_1 = T_2) — "Kevyt lanka ja kitkaton väkipyörä" omits "kevyt" for the pulley, which the chapter's assumption sentence states; C here, but repeat it for consistency.

## Checked
- All lesson and inquiry numbers recomputed in one script with my own formulas (example 2,80 m/s² / 4,20 N; pred-1/exp-1 3,27 N, 1,635 N; exp-1 table 2,45/3,27/3,68 N; pred-2/exp-2 3,68 N, 0,736 N; aineisto 3,265 N and its data agree with the model, s = 0,801 m; siirto 0,3073 kg and both mistake values; check-2 3,363 N and three mistakes; check-3 3,27 m/s², 5,23 N).
- Every choice item: exactly one correct option; each distractor's feedback names the right physics (kertaus third-law pair, pred-2 sum of weights, virhe G_2 on the cart).
- Figures to scale: tilanne T/G_2 = 2/3, G_1 = 2G_2; esimerkki T/G_2 = 0,714; atwood (0,30/0,60 kg) T/G_1 = 4/3, G_2/T = 3/2; N = G_1 on the carts; no third-law pair in one diagram; v and a not drawn as forces.
- virhe figure (fbd.py, wrong=): exactly one error, the hanging body's weight drawn on the cart.
- sim.js implements both models (a, T, ΣF signs, dir for m_1 > m_2), one force scale, N = G_1, equal masses do not start; exp-1/exp-2 lock tapa and m_2 and the sim offers every value asked; simState gives T, a, G1.
- Exit ticket 3: doubling m_1 increases T (3,27 → 3,92 N for 1,0 → 2,0 kg) while staying below m_2 g — correct.
- Assumptions (light inextensible string, light frictionless pulley, no friction or air resistance) stated at point of use; scope within FY4 central contents.
