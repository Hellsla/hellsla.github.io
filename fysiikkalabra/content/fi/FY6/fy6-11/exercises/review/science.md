VERDICT: PASS
CONTENT-HASH: b380572990b00c2b

## Blocking

## Polish
- solutions.md:208 — L3-04: the answer $1{,}60 \cdot 10^{-19}\,\text{C}$ (three figures) comes from masses with two figures, and it still has no rounding reason (rule 7, step 6). You could add "kolme merkitsevää numeroa, koska keskiarvo viidestä tuloksesta", or round to $1{,}6 \cdot 10^{-19}\,\text{C}$.
- solutions.md:49 — L1-05: "voima on $120\,\mu\text{N}$ kahden merkitsevän numeron tarkkuudella" says out loud that a trailing zero is not significant, which is allowed under P7 (b) but is clumsy. Simpler: "kahden merkitsevän numeron tarkkuudella kuten varaus $4{,}0\,\text{nC}$".

## Checked
- Hash b380572990b00c2b at the start and at the end.
- I recomputed all 17 numeric answers in one script with my own formulas (E = F/q, F = qE, E = U/d, F/G, v = √(2eU/m), q = mg·tanα/E, q = mgd/U with integer multiples, y = ½a(L/v₀)²). All agree with answers.py and exercises.json. My least-squares slope for L1-05 is 29,9 µN/nC, which is 0,2 % from the key.
- The round-1 blocking items are fixed. L3-01 (:109) now reads 338 V, three figures as in 450 V, and the counts 3e and 4e are exact. L3-02 (:119) reads $4{,}2 \cdot 10^{3}\,\text{km/s}$ eli $4{,}2 \cdot 10^{6}\,\text{m/s}$. The round-1 polish item for L1-02 is done too: only $1{,}0 \cdot 10^{2}\,\mu\text{N}$ is given.
- P7 (b) elsewhere: 600 V has three figures and is never named as limiting. 70 mV, the 20-fold ratio, 50 V, 10° and 15 kV have two, and their justifications are right.
- P7 (c): the L1-09 maximum voltage, 7,5 kV = 3,0 kV/mm · 2,5 mm, is exact, so it needs no rounding.
- L2-05: the products are 408, 393, 408, 390, 408 and 393,6 V, with mean 400,1 V. L2-07: the points within 3 % are x = 0–6 cm, with mean 2,98·10⁴ V/m against U : d = 3,0·10⁴ V/m.
- L3-04: n = 2, 3, 1, 4, 3. L3-05: F/G = 1360, y = 1,67 mm < 2,5 mm, and at double the voltage the drop hits at x = 8,7 mm.
- L2-08 force diagrams: object = the grain; interactions = the Earth and the field only (vacuum). B shows G and F_s both down, with F_s ≈ 2G. Each wrong figure carries only its one intended error.
- L1-06 and L1-07 each have exactly one correct option, and every distractor's feedback is right physics. L3-03 uses tension components without double counting.
- Scope (Coulomb's law and the uniform field) and notation ($\overline{E}$, $\overline{F}_\text{s}$, E = U : d) match the brief.
