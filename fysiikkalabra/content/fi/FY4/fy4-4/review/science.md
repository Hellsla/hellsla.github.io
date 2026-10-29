VERDICT: PASS
CONTENT-HASH: 765120860b916cad

## Blocking

## Polish
- inquiry.json:178, 229, 282, 290 — measure labels write the units as plain "(N)", "(kg)", "(m/s)" after a LaTeX symbol; `$\Sigma F_x$ ($\text{N}$)` would match the teacher's all-LaTeX rule fully (the symbols themselves are now LaTeX: round-1 item fixed).
- lesson.md (Miksi-vastaus, "Lastin paino ei sinänsä vedä autoa taaksepäin") — true on level ground; the hook and figure show a level road, so C, but "tasaisella tiellä" would make it explicit.

## Checked
- Round-1 blockers fixed: measure labels are LaTeX ($\Sigma F_x$, $a_x$, $v_x$, $m$); Yleinen virhekäsitys now states "Kun ilmanvastus jätetään huomiotta". Sim string now horizontal (both ends at `top + 8`).
- Recomputed in one script: worked example G = 4708,8 N, a = 1,02 m/s² up (forgetting G: 10,8); siirto 7000 N and mistakes 25 200 / 5,0 / 13 734; check-2 1,0 (1,67, 2,33); check-3 1,67 m/s², N = 11,8 N; exp model values 1,0/2,0 and 2,0/1,0 m/s²; exit ticket ×4: all agree.
- Sim: a = ±F/m, constant pull, no friction (said in `model`); exp-3 stops at 0,75 s, x_max 0,76 m, so the reversal is seen within 1,0 s; fastest runs end at 0,75 s inside the track; fitted slope exact; simState gives sumFx, a, v, m.
- Experiments isolate the varied parameter (locked alku/suunta/m; alku/suunta/F; alku/F/m).
- Figures: "kokonaisvoima" to scale (T/G 0,765, F_μ = T/3, net force a hollow green $\Sigma\overline{F}$ apart); "nosturi" T/G 1,0/1,0/1,3/0,7 agrees with each motion; "esimerkki" T/G 1,10.
- Valitse: exactly one correct (T > G while slowing on the way down); b, c, d each carry one error; d without F would be correct, as its feedback says.
- Force-diagram rules: rectangle body everywhere incl. the sim; G from centre, N from the contact face apart from G, T from the top, friction from the bottom edge; no motion vector drawn as a force; v blue, a orange, forces red.
- Notation: vectors \overline{}, products \cdot, no \vec/\mathbf/×; canvas labels LaTeX.
- Causality: truck answer names the road's forward force on the tyres and the mass, not the weight; ΣF = ma written only after the diagram and positive direction.
- Hash identical at start and end.
