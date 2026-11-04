VERDICT: PASS
CONTENT-HASH: 60566c60301b819d

Follow-up review of the fix commit 2c31ff041 (delta from 29fe996265405d42, whose full review is kept below). Change: inquiry.json:141, `simulaatio.calc` now writes the magnetic force magnitude $|q|vB$ and the readouts $F_\text{m} = |q|vB$, $F_\text{s} = |q|E$ (earlier Polish 1).

## Blocking

None.

## Polish

1. The remaining $qU$, $qvB$, $r = mv : (qB)$ in inquiry.json (kertaus, ennuste-2/3, johtopäätös, pohdi, virhe, siirto, tarkistus-1/3/4) concern only positive particles, so they are right by "Positiivisella hiukkasella $|q| = q$"; `pohdi` could use $|q|$ (C).

## Checked

- New calc box: magnitudes with $|q|$, the vector force $q\overline{E}$ kept signed, direction rule for a positive charge — correct, and now matches sim.js (`Math.abs(P.q)` in readouts) for the negative hydrogen ion.
- Consistency: grep of plain $qvB$/$qE$/$qU$ — lesson.md uses them only in the worked example, which states "positiivinen, joten $|q| = q$"; no inquiry item with plain $q$ involves a negative particle.
- Sign/magnitude across Ydinajatus, Kaava, selector, spectrometer, accelerator, Tiivistelmä, prior, contribution and exit ticket: consistent.
- Recomputed: proton $1{,}0\cdot10^6$ m/s, $0{,}20$ T: $3{,}20\cdot10^{-14}$ N, $r = 5{,}22$ cm, weight ratio $2\cdot10^{12}$; example $v = 3{,}00\cdot10^5$ m/s, $m = 20{,}01$ u, Ne-22 at $27{,}4$ cm; $m_p/m_e = 1837$.
- Inquiry: kertaus $4{,}38\to8{,}75\cdot10^5$ m/s; koe-1 $10{,}4/20{,}9$ cm; koe-2 $1{,}0\cdot10^6$ m/s, $24/48$ fN; virhe $4{,}57\to6{,}46$ cm; siirto $0{,}225$ T (mistakes $0{,}159$, $0{,}00712$); tarkistus-3 $6{,}22$ cm. One correct option each; tarkistus-2 right-hand rule correct.
- Experiments isolate the varied parameter; `simState` gives `d`, `vLoppu`, `poikkeama`, `Fm15`, `Fs15`.
- sim.js: $\overline{F} = q(\overline{E} + \overline{v}\times\overline{B})$ with signed $q$; gravity omitted with reason; non-relativistic limit stated. LHC $1{,}09\cdot10^{-6}$ J.
- Hash same at start and end.
