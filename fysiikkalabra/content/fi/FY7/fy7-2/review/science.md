VERDICT: PASS
CONTENT-HASH: 29fe996265405d42

Full review (scope: a changed line carries a formula). The change of this round: signed charge $q$ in the vector law $\overline{F}_\text{s} = q\overline{E}$, magnitude $|q|$ in $F_\text{s} = |q|E$, $E_\text{k} = |q|U$ (with "kiihdyttävä jännite"), $F_\text{m} = |q|vB\sin\alpha$, $r = mv/(|q|B)$, $m = |q|B_2r/v$, the selector condition, contribution, prior, summary and exit ticket; chapter references renamed.

## Blocking

None.

## Polish

1. inquiry.json `simulaatio.calc` — "magneettinen voima, jonka suuruus on $qvB$" and "Lukemien voimat $F_\text{m} = qvB$ ja $F_\text{s} = qE$": the sim offers the negative hydrogen ion ($-e$), and sim.js already uses `Math.abs(P.q)`. Write $|q|vB$ and $|q|E$ there so the box says what the theory now says.
2. The remaining $qU$, $qvB$, $r = mv : (qB)$ in inquiry.json (kertaus, ennuste-2/3, johtopäätös, pohdi, virhe, siirto, tarkistus-1/3/4) concern only positive particles (proton, alpha, deuteron, Ne⁺, B⁺), so they are right by the lesson's "Positiivisella hiukkasella $|q| = q$". Optional: `pohdi` (generic $r = mv : (qB)$) could use $|q|$ too.

## Checked

- Sign/magnitude: vector law with signed $q$, every magnitude formula with $|q|$, direction rule for $\pm$; $W = |q|U$ limited to an accelerating voltage and a particle from rest. Consistent across Ydinajatus, Kaava, selector, spectrometer, accelerator, Tiivistelmä, prior, contribution and exit ticket.
- Recomputed with my own formulas (agree with lesson-answers.py): proton $1{,}0\cdot10^6$ m/s, $0{,}20$ T: $F = 3{,}20\cdot10^{-14}$ N, $r = 5{,}22$ cm, weight $1{,}64\cdot10^{-26}$ N (ratio $2\cdot10^{12}$, "noin $10^{12}$" C).
- Example: $v = 3{,}00\cdot10^5$ m/s, $m = 3{,}324\cdot10^{-26}$ kg $= 20{,}01$ u; Ne-22 at $27{,}4$ cm. Exit/misconception ratio $m_p/m_e = 1837$ ≈ 1840.
- Inquiry: kertaus $4{,}38\to8{,}75\cdot10^5$ m/s; koe-1 $d = 10{,}4/20{,}9$ cm; koe-2 $E/B = 1{,}0\cdot10^6$ m/s, $24/48$ fN; virhe $4{,}57\to6{,}46$ cm; siirto $B = 0{,}225$ T, mistakes $0{,}159$, $0{,}00712$; tarkistus-3 $6{,}22$ cm, mistake $12{,}4$. Each choice has exactly one correct option with right feedback; tarkistus-2 right-hand rule correct (field into page, rightward $v$: $+$ pushed up).
- Experiments isolate the varied parameter (koe-1 only $v$, koe-2 only the particle) and the sim's `simState` gives `d`, `vLoppu`, `poikkeama`, `Fm15`, `Fs15`.
- sim.js: force from signed $q$ in $\overline{F} = q(\overline{E} + \overline{v}\times\overline{B})$ components, readouts with $|q|$; gravity omitted with stated reason; non-relativistic limit stated (LHC caveat present). LHC $6{,}8$ TeV $= 1{,}09\cdot10^{-6}$ J.
- Photo captions (aurora, fine-beam tube, Berkeley cyclotron): physics correct.
- Hash same at start and end.
