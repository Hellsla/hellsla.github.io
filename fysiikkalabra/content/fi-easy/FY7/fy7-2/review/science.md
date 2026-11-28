VERDICT: PASS
CONTENT-HASH: a7ba32c6ba5e8651

## Blocking

## Polish
- lesson.md:79 — "Voiman suuruus riippuu vain varauksen suuruudesta $|q|$, ei etumerkistä" reads as if $F_\text{s}$ did not depend on $E$ — "Voiman suuruuteen vaikuttaa varauksen suuruus $|q|$, ei sen etumerkki."
- inquiry.json:140 (simulaatio `model`) — "noin $10^{12}$ kertaa pienempi kuin magneettinen voima" holds at the default settings only; the slider allows $B = 0$ — "pienempi kuin kentän voimat".
- lesson.md:244 — "Kun vauhti kasvaa, magneettikenttää vahvistetaan" sits before the near-c caveat at line 248; "kun energia kasvaa" would avoid a speed-only picture for the LHC (C as written).
- inquiry.json:339 (siirto `solution`) — two-step substitution; the house rule asks to simplify to $B = \sqrt{2mU/q} : r$ before substituting (numbers unchanged, 0,225 T).

## Checked
- Recomputed in one script (own formulas) every number of lesson.md, inquiry.json and exit-ticket.json; all agree with lesson-answers.py: $F = 3{,}2\cdot10^{-14}$ N, $r = 5{,}2$ cm, $F:G \approx 2\cdot10^{12}$; Ne example $3{,}324\cdot10^{-26}$ kg = 20,01 u, Ne-22 at 27,4 cm; $m_p/m_e = 1837$; LHC $1{,}09\cdot10^{-6}$ J; kertaus 4,4→8,8·10⁵ m/s with distractors 1,8·10⁶ and 7,0·10⁶; virhe 6,19·10⁵ m/s, 6,46 vs 4,57 cm; siirto 0,225 T, mistakes 0,159 and 0,00712 T; tarkistus-3 6,2 cm (12,4 cm mistake, proton 3,1 cm); exit ticket 3,0·10⁵ m/s.
- Ported sim.js `compute` (Boris) to Python: koe-1 proton at 0,20 T gives $d$ = 5,22/10,44/15,66/20,89 cm with $v_\text{end}$ unchanged (matches $2mv/(qB)$, within the 22 cm detector); koe-2 gives $y = 0$ for proton, deuteron, alpha and H⁻, $F_\text{m} = F_\text{s}$ = 24,0 fN (alpha 48,1 fN).
- Experiments: koe-1 locks particle, B, direction, E and varies v; koe-2 locks v, B, direction, E and varies the particle; measured keys d, vLoppu, poikkeama, Fm15, Fs15 exist in simState.
- Directions: right-hand rule (thumb v, fingers B, palm F) = $q\overline{v}\times\overline{B}$; force-dir, circle-path (clockwise, B out), spectrometer (E up, B₁ and B₂ out, F_s up/F_m down, deflection down) and track-sign (curves down, B in → negative) all correct; sim force $q(v_yB_z, -v_xB_z)$ and plate signs agree.
- r-graph to scale (pixel check: proton 10,4 cm, deuteron 20,9 cm at 2,0·10⁶ m/s).
- Every prediction, check and Etsi virhe has exactly one correct option; each distractor's feedback names the right physics.
- Conditions stated: perpendicular, homogeneous field, $v \ll c$, vacuum, gravity neglected, LHC relativistic caveat; scope inside FY7 central contents and the slot.
- Hero: lighter, abundant C-12 beam curves tighter than the rare heavier beam.
