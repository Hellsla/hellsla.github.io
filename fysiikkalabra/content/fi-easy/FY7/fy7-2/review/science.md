VERDICT: PASS
CONTENT-HASH: 95e436a1b8ea1958

Follow-up review of the fix commit 2c31ff041 (delta from ef39ca99fa2409f7). Change: inquiry.json:141, sim `calc` box (Laskennan selitys).

## Blocking

## Polish
- lesson.md:275 — "Säde on kääntäen verrannollinen varaukseen ja kenttään" → "varauksen suuruuteen $|q|$ ja kenttään", to match $r = mv/(|q|B)$.
- inquiry.json `pohdi`, `tarkistus-4`, `siirto` keep $r = mv:(qB)$ and $qvB$ for positive ions only (correct); "(positiivinen ioni, $|q| = q$)" would match the lesson's convention.

## Checked
- Earlier blocking item resolved: "Magneettisen voiman suuruus on $|q|vB$" and "Lukemien voimat $F_\text{m} = |q|vB$ ja $F_\text{s} = |q|E$"; the vector $q\overline{E}$ stays signed. Correct for the negative hydrogen ion; matches sim.js `Math.abs(P.q)`.
- Consistency: grep of plain $qvB$/$qE$/$qU$ — lesson.md only in the worked example ($|q| = q$ stated); no inquiry item with plain $q$ involves a negative particle.
- Signed $\overline{F}_\text{s} = q\overline{E}$ vs $F_\text{s} = |q|E$, $E_\text{k} = |q|U$, $F_\text{m} = |q|vB\sin\alpha$, $r = mv/(|q|B)$, selector, spectrometer and summary consistent.
- Right-hand rule and track-sign check correct.
- Recomputed: $3{,}2 \cdot 10^{-14}\,\text{N}$, $r = 5{,}2\,\text{cm}$, ratio about $10^{12}$; example $3{,}00 \cdot 10^5\,\text{m/s}$, $20{,}0\,\text{u}$, Ne-22 27,4 cm; electron radius 1840 times smaller; LHC 6,8 TeV = $1{,}1 \cdot 10^{-6}\,\text{J}$.
- Kertaus $8{,}8 \cdot 10^5\,\text{m/s}$; koe-1 10,4 / 20,9 cm; koe-2 24 / 48 fN; Etsi virhe 6,46 cm; transfer 0,225 T (mistakes 0,159, 0,00712); tarkistus-3 6,2 cm; exit $3{,}0 \cdot 10^5\,\text{m/s}$.
- Each choice has exactly one correct option; experiments lock all but the varied parameter; captions fair (C).
- Hash same at start and end.
