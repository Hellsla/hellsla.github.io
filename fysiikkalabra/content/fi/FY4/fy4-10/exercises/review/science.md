VERDICT: PASS
CONTENT-HASH: fec4683407094eec

## Blocking

## Polish
- solutions.md:69 (L2-02, existing) — "muuttuu … muodonmuutoksiksi, sisäenergiaksi ja ääneksi": still lists the deformation as an energy form — write "muuttuu muodonmuutoksissa sisäenergiaksi ja ääneksi", as in L1-06.
- solutions.md:159 (L2-05) — "Koe 2 on täysin kimmoton, koska vaunut jäävät kiinni toisiinsa": not stated in the task, only inferable from the data — write "koska vaunuilla on törmäyksen jälkeen sama nopeus 0,37 m/s eli ne liikkuvat yhdessä".
- exercises.json:175 (L2-06) — kind "graph", but no graph is drawn or read; the speeds are taken from two table rows — ask for the (t, x) graph in a) or drop "graph".
- exercises.json:266 (L3-05) — "vaunu liukuu" with μ ≈ 0,20 called "tavallinen liukukitkakerroin": wheeled carts roll and have much smaller resistance — say "kappale/palikka A" (with a felt base) or "vaunu, jonka pyörät on lukittu".
- exercises.json:74 (L1-07) — skater throwing a ball is structurally the same as L1-03 (skaters push apart from rest, find the other's speed) — e.g. give the skater an initial velocity.

## Checked
- I recomputed all 20 answers in one script with my own formulas: 0,3429; 1,8; 73,4 %; 46,7 %; 0,50; 79,4 km/h (μ 0,50/0,70 → 72,5/85,8 km/h); 1,175 N. All agree with answers.py. A least-squares fit for L3-05 gives a = 1,98 m/s², 1,19 N and v₀ = 1,00 m/s, inside the tolerance.
- L2-05: momentum 0,300 → 0,302/0,296/0,299; E_k kept 98/61/73 %. All physically possible.
- L2-06: speeds 0,51/0,11/0,27 m/s, p 0,204 → 0,206; lines meet at t ≈ 1,96 s, consistent with the text.
- L3-04: energy principle with μ(m_A+m_B)g, then momentum across the collision. The 56 % kinetic-energy loss is correct. The conclusion holds over the whole μ range.
- L3-05: momentum is used only across the collision; the friction impulse 0,6·1,96·0,06 ≈ 0,071 N·s explains the student's 12 % deficit.
- L1-06: exactly one correct option; L2-07 sign error modelled correctly (0,70 vs 0,50 m/s).
- Scope: 1-D only, with the energy principle and friction from FY4; there is no 2-D content. Notation (v, v′) matches the brief. Plan items and 8/7/5 levels are covered.
- Lint now 0 errors (warnings only).
- Round 2: L1-06 feedback (exercises.json:65) and Periaate (solutions.md:123) now say "muodonmuutoksissa sisäenergiaksi ja ääneksi"; the round-1 blocker is resolved. Hash is the same at the start and at the end.
