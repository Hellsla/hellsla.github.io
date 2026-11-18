VERDICT: FAIL
CONTENT-HASH: fe2328407c0d03bc

## Blocking
- [Major] solutions.md fy7-7-L2-06 (7-15), Kaava, capture open-exercises-L2-1280-8 — the second display block (after "ja poikkeama") starts with a bare "= |e_{0,ennuste} − e_{0,mitattu}| / e_{0,ennuste} · 100 %" with no left-hand side, and the fraction and "· 100 %" wrap onto two rows — house rule: every chain shows what it computes — the reader sees an equals sign with nothing before it — fix: name the quantity, e.g. `$$\begin{aligned} \delta &= \frac{|e_{0,\text{ennuste}} - e_{0,\text{mitattu}}|}{e_{0,\text{ennuste}}} \cdot 100\,\% \end{aligned}$$` (or write "poikkeama = …" with \text), with a symbol defined in the Periaate or a short lead-in, and no hand-split before "· 100 %".

## Polish
- [Minor] Other fy7-7 Kaava blocks not opened individually; same pattern as fy7-6/8/9 (aligned on =), no problem expected.

## Checked
- Delta, hash current. Opened open-exercises-L2-1280-6 (7-14 context) and open-exercises-L2-1280-8 (7-15 Kaava: first block good, second block defective as above).
- Hash identical at start and end.

## Scores
illustrations n/a · typography 3 · Finnish 4 · accessibility 4
