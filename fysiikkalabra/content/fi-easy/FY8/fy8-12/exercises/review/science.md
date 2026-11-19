VERDICT: PASS
CONTENT-HASH: 81b5cf5d2daaa058

## Blocking

## Polish
- solutions.md (fy8-12-L1-07, L3-02 Järkevyys): $\text{min}^{-1}$ now sits next to $\tfrac{1}{\text{s}}$ in the same sentence ("$1620\,\text{min}^{-1}$ on noin $27\,\tfrac{1}{\text{s}}$"). This is physically correct. Writing both rates the same way ($\text{s}^{-1}$) would only be more consistent. Optional.

## Checked
- Hash 81b5cf5d2daaa058 (`reviews.py hash fy8-12 --exercises --lang fi-easy`) at the start and the end.
- The whole diff is covered by a script. It joined every removed line and every added line, collapsed the whitespace and swapped `\tfrac{1}{\text{min}}` for `\text{min}^{-1}` and `"1/min"` for `"min⁻¹"`. After that, the removed text and the added text are identical (7208 characters each). No word, number, sign or formula changed. The rest of the diff only cuts paragraphs and adds blank lines.
- Unit change: $\tfrac{1}{\text{min}} \to \text{min}^{-1}$ in L1-07 (task text and unit field) and in L2-09 (unit field). The two forms are the same unit. The answers 1530 and 141,4 and the tolerances 0,02 are unchanged. The task text and the unit field now agree in L1-07.
- I recomputed the numbers the changed lines touch: L1-07 $1215/0{,}75\,\text{min} - 90\,\text{min}^{-1} = 1530\,\text{min}^{-1}$. L3-02 $d_{1/2} = 11{,}0\,\text{mm}\cdot\ln 2/\ln(2370/600) = 5{,}55\,\text{mm}$ and $d = 34{,}99\,\text{mm} \to 35\,\text{mm}$. L2-09 $800\cdot 0{,}5^{2{,}5} = 141{,}4$. L1-05 $hc/E = 9{,}8412\cdot 10^{-8}\,\text{m}$. All four agree with answers.py and the solutions.
- Split paragraphs (L2 Järkevyys moved to its own paragraph; the beta/gamma model answer; the RIVM a, c, d model answers; L3 d) uncertainty; Comptonin/parinmuodostus b, c): the words are in the same order and no causal step was lost. Each "koska" stays in the same paragraph as its claim.
- L1-05: the blank lines inside the `$$ … \begin{aligned}` block are the same as in the Finnish version. In the fi-easy preview they render as one display block, so the physics shown is unchanged.
