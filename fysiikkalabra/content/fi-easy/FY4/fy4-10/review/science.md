VERDICT: PASS
CONTENT-HASH: 869cdded1a3067e5

## Blocking

## Polish
- lesson.md:147 — "Kappaleet muuttavat silloin muotoaan" names deformation as the mark of an inelastic collision, but elastic bodies deform too (the spring bumper, the steel balls). — "Kappaleet muuttavat silloin muotoaan pysyvästi tai lämpenevät."
- lesson.md:251 — "Kevyempi osa saa suuremman nopeuden. Siksi kivääri potkaisee taaksepäin" makes the speed difference sound like the reason for the recoil. The recoil comes from the equal and opposite momenta; the speed difference only explains why the recoil is slow. — Move "Siksi kivääri …" to follow "osat saavat yhtä suuret liikemäärät vastakkaisiin suuntiin".
- inquiry.json:464 (check-1) — "siirtyi Maahan" is the usual school answer (C). Strictly, during the fall the Earth already had an equal upward momentum, and the impact cancels both. Optional: "Maa saa yhtä suuren liikemäärän alaspäin" already says enough. No change needed.
- inquiry.json:127 (simulaatio howto) — the sliders allow $v_2 > v_1$ (e.g. $v_1 = 0$, $v_2 = +1{,}0\,\text{m/s}$). Then the gliders never meet and the "Jälkeen" readings stay "…" with no explanation. — In Käyttöohje, one clause saying the gliders collide only if vaunu 1 catches up with vaunu 2.

## Checked
- Recomputed in one script and compared with model.js (node, RK4) and lesson-answers.py: exp-1 tarra $v' = 0{,}40/0{,}30/0{,}24$, $E_\text{k}' = 0{,}048/0{,}036/0{,}029\,\text{J}$; exp-2 kimmoisa $(0{,}20; 0{,}80)$, $(0; 0{,}60)$, $(-0{,}12; 0{,}48)$ with $p$ and $E_\text{k}$ conserved; exp-3 $0{,}63/1{,}26\,\text{m/s}$, $p = 0{,}253$, spring $0{,}24\,\text{J}$. All agree to 4 decimals.
- Predictions 1–3: exactly one correct option each. Distractor values are right ($0{,}42 = 0{,}60/\sqrt2$) and so is the feedback physics.
- Worked example: $v' = 1{,}14 \to 1{,}1\,\text{m/s}$ (2 s.f. justified). $E_\text{k}$ goes from $38{,}3$ to $32{,}5\,\text{kJ}$, $15\,\%$. Solved symbolically first; the conditions (vierimisvastus, short coupling) are stated.
- Kertaus $0{,}30$ / $12\,000$; Etsi virhe $0{,}025$ vs $0{,}475$; siirto $1{,}0\,\text{m/s}$, mistakes $2{,}4$, $0{,}706$ (relative-to-boat reading, correctly explained) and $5{,}76$; check-2 $0{,}15$, mistakes $0{,}60$ and $0{,}20$. All correct.
- Kaava inline example $0{,}072 \to 0{,}036\,\text{J}$. Derivation $2v_1'v_2' = 0$ in "Vastaus alun kysymykseen" is correct.
- Conservation condition (zero net external force or negligible impulse) stated consistently: theory, Tiivistelmä, glossary, sim model box, solutions, exit ticket.
- Figures: tarra (velocity arrow halves, momentum arrow equal); tyypit (momentum arrows 110 px each; animation speeds give exchange, halving, equal-and-opposite); vuorovaikutus (forces drawn on the right carts, equal lengths, $\Delta\overline{p}$ sum zero).
- Simulation: momentum emerges from equal and opposite bumper forces (not an input). The energy budget $E_\text{k}+E_\text{p}+E_\text{sis}$ is closed. The limits (no friction, level track) are stated in Mallin oletukset.
- Experiments: each locks type, $m_1$, $v_1$, $v_2$ and varies only $m_2$. simState exposes u1, u2, pJ, EkJ, and the adapter params match the initial keys.
- Scope: one-dimensional only, within the FY4 central contents. Energy goes into internal energy, never "lämmöksi" (except in a wrong option, which is allowed).
