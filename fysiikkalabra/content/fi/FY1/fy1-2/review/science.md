VERDICT: PASS
CONTENT-HASH: ac597b2b7b79c1f5

## Blocking

## Polish
- inquiry.json:83 — the new title "Ennuste 2: kauempana oleva luotain" is physically neutral: it states no factor and does not give away the answer. But the prompt talks only about distances of 10^7 km and 10^9 km, not about a probe, and 10^9 km is far nearer than Voyager 2 (about 2·10^10 km). — Consider "Ennuste 2: sata kertaa pidempi matka" or "Ennuste 2: valon kulkuaika kauemmas".
- exit-ticket.json:8 — the answers "4200 m" and "500 µm" lose the significant figures of 4,2 km and 0,50 mm. — Write 4,2·10³ m and 5,0·10² µm, or add a note on this.
- lesson.md:502 — the text calls AU "Maan ja Auringon keskimääräinen etäisyys" and also an exact defined value (fine as C). — Saying "nykyään sovittu tarkaksi arvoksi" would remove the small tension between the two.
- inquiry.json:188 — the text says "sen tarkkuus on lähtötietojen tarkkuus". The constant-speed assumption also limits it. — Consider "ja sitä rajoittavat lähtötiedot ja vakionopeusoletus".
- sim.js (the slider label) — at d = 0 km (Alusta, Aurinko), the label shows "d = 10^{6,00} km" because n is clamped to N_MIN, while the readout says d = 0 km. — Show "< 10^6" when d < 10^6 km.

## Checked
- Delta since f86bfd82: only the title at inquiry.json:83 changed. pedagogy.md is not a lesson file. The round-1 blocking item is fixed: the title no longer states the distractor's tenfold premise.
- Ennuste 2: 10^9 : 10^7 = 100. The correct option, 3300 s, matches the koe-1 value 3340 s. Every distractor (66 s, 330 s, 33 000 s) is wrong, and its feedback is right.
- Round 1 still holds for the unchanged content: every recomputed number (Voyager 2 model, 8,32 min per AU, Neptune, transfer, Mercury, Saturn, area), the koe-1 values from simState.tLight, the isolated experiments, the sim's scale and model with its limits, the scale-list magnitudes, the significant-figure rules, the figures, and the FY1 scope.
- Hash checked at the start and at the end: ac597b2b7b79c1f5.
