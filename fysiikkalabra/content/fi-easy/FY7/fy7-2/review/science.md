VERDICT: FAIL
CONTENT-HASH: ef39ca99fa2409f7

## Blocking
- B (internal consistency: signed q vs |q|) — content/fi-easy/FY7/fy7-2/inquiry.json:141 (sim `calc`, Laskennan selitys) — "Magneettisen voiman suuruus on $qvB$" and "Lukemien voimat $F_\text{m} = qvB$ ja $F_\text{s} = qE$" give a magnitude as a signed product, although the sim's particle menu includes the negative hydrogen ion ($-e$) and sim.js computes `Math.abs(P.q)`. The lesson now writes every magnitude with $|q|$. — Fix: "Magneettisen voiman suuruus on $|q|vB$ …" and "Lukemien voimat $F_\text{m} = |q|vB$ ja $F_\text{s} = |q|E$ on laskettu lähtövauhdilla." (The fi version has the same text.)

## Polish
- lesson.md:275 — "Säde on kääntäen verrannollinen varaukseen ja kenttään" → "varauksen suuruuteen $|q|$ ja kenttään", to match $r = mv/(|q|B)$.
- inquiry.json `reflect`, `tarkistus-4` and `siirto` keep $r = mv:(qB)$ and $qvB$ for positive ions only, which is correct, but one clause such as "(positiivinen ioni, $|q| = q$)" would match the lesson's convention.

## Checked
- Signed $\overline{F}_\text{s} = q\overline{E}$ (direction) vs $F_\text{s} = |q|E$, $E_\text{k} = |q|U$, $F_\text{m} = |q|vB\sin\alpha$, $r = mv/(|q|B)$, selector, spectrometer and summary: consistent; worked example states $|q| = q$.
- Right-hand rule: thumb along v, fingers along B, palm pushes F gives $q\,\overline{v}\times\overline{B}$; a positive charge in a B out of the page turns clockwise; track-sign check (B into the page, curving down, so negative) correct.
- Ydinajatus numbers recomputed: $3{,}2 \cdot 10^{-14}\,\text{N}$, $r = 5{,}2\,\text{cm}$, weight $1{,}6 \cdot 10^{-26}\,\text{N}$, ratio about $10^{12}$.
- Worked example recomputed: $v = 3{,}00 \cdot 10^5\,\text{m/s}$, $m = 3{,}324 \cdot 10^{-26}\,\text{kg} = 20{,}0\,\text{u}$, Ne-22 at 27,4 cm.
- Selector field directions ($\overline{E}$ up, B out of the page) give opposite forces; electron radius 1840 times smaller.
- LHC: 26,7 km, 1232 dipoles, 8,3 T, 6,8 TeV = $1{,}1 \cdot 10^{-6}\,\text{J}$; relativity caveat stated.
- Kertaus $8{,}8 \cdot 10^5\,\text{m/s}$; koe-1 10,4 / 20,9 cm; koe-2 24 / 48 fN, $v = E/B$.
- Etsi virhe 6,19e5 m/s, 6,46 cm; transfer $B = 0{,}225\,\text{T}$ (mistakes 0,159 and 0,00712); tarkistus-3 6,2 cm; exit ticket $3{,}0 \cdot 10^5\,\text{m/s}$.
- Each choice has exactly one correct option; experiments lock everything but the varied parameter.
- Photo captions (aurora, electron-beam tube, 1939 cyclotron) are fair (C).
