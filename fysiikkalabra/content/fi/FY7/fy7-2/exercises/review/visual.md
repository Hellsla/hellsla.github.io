VERDICT: FAIL
CONTENT-HASH: 6f5c46b3a62a89ae

## Blocking
- [Major] solutions.md fy7-2-L1-02, **Annettu** — the new inline formula `$|q| = e = 1{,}602 \cdot 10^{-19}\,\text{C}$` breaks onto two lines (after `|q| =`) at 360, 390 and 1280 px (captures q-390-0, ex2-1280-0: "|q| =" ends one line, "e = 1,602 · 10^-19 C" starts the next); an inline formula must never wrap (teacher rule) and the split leaves a dangling equals sign — fix: keep it as one unbreakable group, `${|q| = e = 1{,}602 \cdot 10^{-19}\,\text{C}}$` (a braced group is not split by KaTeX), or write it as two short formulas, `varauksen suuruus $|q| = e$, missä $e = 1{,}602 \cdot 10^{-19}\,\text{C}$`, and check again at 390 px.

## Polish
- [Minor] solutions.md — the same wrapping already occurs in untouched Annettu lines (`q = e = 1{,}602 ...`, `2e = 3{,}204 ...`, `m_\alpha = 6{,}645 ...`, `1\,\text{u} = ...`); the same braced-group fix would cover them.

## Checked
- Delta: changed lines of L1-02 (Annettu, Kaava `|q|vB = \dfrac{mv^2}{r}`, `r = \dfrac{mv}{|q|B}` at 390 px, capture ex-390-0: fractions and bars read correctly) and the chapter-reference edits in L2-03 and L3-02 (plain italic text, no layout effect). Measured every inline formula of the built page at 360, 390 and 1280 px for line breaks; only the L1-02 Annettu line is new.

## Scores
illustrations 5 · typography 3 · Finnish 5 · accessibility 4
