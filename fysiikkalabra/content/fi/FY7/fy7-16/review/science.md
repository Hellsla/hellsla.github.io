VERDICT: PASS
CONTENT-HASH: e7fc6c136ce16cf8

## Blocking

## Polish
- lesson.md:335 (Tiivistelmä) — "osa energiasta muuttuu käämien sisäenergiaksi: mittauksessa lataus vei noin 47 % enemmän" credits the whole surplus to the coils. The interpret solution says it went to the coils and the electronics. Write "käämien ja elektroniikan sisäenergiaksi".
- lesson.md:336 — "eikä sähköä johtamaton lasi lainkaan" reads as if the glass never warms. The theory says it warms from the hot pan. Write "eikä lasiin synny pyörrevirtoja".

## Checked
- Round-1 fixes: STEP = Φ(20, 20, 3) : 6,5 gives 6,5 levels at 3 mm, so 6 dark lines (6,5 → 6), and 1,28 at 20 mm, so 1 line. The figure, aria-label, koe-1 and sim-spec agree.
- ennuste-kela feedback, koe-2 intro, the johtopäätös model and criterion 3 now say the voltage grows up to about 35 mm (1,247 V) and then falls (40 mm: 1,229 V). The model agrees.
- Both check-1 feedbacks state "samalla kelan virralla", and "lämpenee vain vähän" matches the theory.
- Recomputed independently in one script (Neumann double integral for the coil mutual inductance instead of elliptic integrals): every e0(z, R1) value, Φ0 = 0,501 µWb, 19,74 %, the half point at 8,8 mm ("noin 9 mm"), and 3 mm optimum at R1 = 20 mm. All agree with lesson-answers.py.
- Fibre: 16,7 km halving, 1,58 % after 100 km, graph endpoints 35 % and 16 %, 4,9 µs/km, worked example 0,0502 mW (symbolic first, 7 steps), tarkistus-2 25,1 %, exit 20 dB.
- siirto 0,775 mT and its mistakes (9,30; 4,87; 7,75 · 10⁻⁵ mT); Ravenscraft 47,3 % and its mistakes (6,75; 147,3; 32,1).
- The decibel clause (dB add, power ratios multiply) and the virhe item are consistent.
- Hob figure: eddy current opposite to the coil current (× / • swapped); the sim at 3 mm, 20 mm reads 4,404 V, 100,0 %.
- koe-1 and koe-2: initial values, locks and simState keys (phi0, e0, osuus) are right.
- Each prediction has exactly one correct option, and the distractor feedbacks are right.
