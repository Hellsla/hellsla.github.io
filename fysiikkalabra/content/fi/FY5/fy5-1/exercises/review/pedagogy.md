VERDICT: PASS
CONTENT-HASH: 845bbf8761a73937
SCOPE: delta, Kaava steps rewritten (basic equation, then simplified symbolically)

## Blocking
(none)

## Polish
1. solutions.md:159 (error analysis, wrench measured from the edge) — the Kaava step now shows r = d − e without saying what d and e are (the old line said "missä d on mitattu pituus ja e matka reunasta akselille"). Periaate does describe the 0,030 m, but add the symbols to Annettu or Periaate: "mitattu pituus d ja matka reunasta akselille e".
2. solutions.md:149 (weights on a stick) — the last Kaava row is broken by a \qquad continuation; fine on a phone, but a one-line final form would read better at 1280 px.

## Checked
- Every changed Kaava now starts from the basic equation (M = Fr, G = mg, M_p = F_p d) and simplifies symbolically (r = d, then M = Fd, then F = M/d) before any number. This is the rule's order.
- The source is aligned blocks with one equation per row. The 1280 px capture of L1-02 shows the rows aligned, with no clipping.
- Sijoitus, Vastaus and the numbers are unchanged, so the principle and the check still follow the Kaava. Nothing is skipped.
- The long Vastaus (bicycle gears) and the Mallivastaus/Periaate paragraphs are split into short paragraphs of one idea each, which helps readability. The content is the same.
- The equal-moments task (F2 r2 = F1 r1) now starts from M2 = M1, which is right.
- The ΣF = 0 and ΣM = M1 + M2 = 2Fd task now shows the sum of moments as a step, which is the teaching point.
- L1-10 (grid figure) was not touched by this diff, apart from adding the F·OP form. The earlier PASS stands.
- Text and captures read only; the figure fy5-1/ruutu gives the same data in its description and does not show the answer.
