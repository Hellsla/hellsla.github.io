VERDICT: FAIL
CONTENT-HASH: 267c472d1f553fa3
SCOPE: delta added-exercise from 3f3114ccfa6f8f33 base 5b3ca4f81c77

## Blocking
- solutions.md fy8-6-L2-06 Kaava (line 329) — `h_0 = 6{,}626\,\text{J}\,\text{s}` lacks the factor $10^{-34}$; the accepted value is $6{,}626 \cdot 10^{-34}\,\text{J}\,\text{s}$, as in Annettu. Fix the value.

## Polish
- solutions.md fy8-6 Kaava rows that remain one-liners (L1-01, L3-01) skip the E = hf, c = f\lambda base; consistent with their level, optional.

## Checked
- 8g diff: the Kaava step now lists the basic laws first (E = hf, c = f\lambda), then the derived formula, symbolic until Sijoitus; each Kaava block is an aligned list, one equation per row (the packet diff shows it flattened). A student can follow the derivation; numbers, answers and levels unchanged.
- The added closing sentences in model answers and the split Vastaus/Sijoitus paragraphs close gaps in the explanations and read clearly.
- Method: delta text in packet plus the aligned Kaava blocks read in solutions.md; no captures needed.
