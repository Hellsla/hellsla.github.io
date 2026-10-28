VERDICT: FAIL
CONTENT-HASH: db6b52d85406321f

## Blocking
- solutions.md:117 (L3-03 Sijoitus): "$\dfrac{1{,}447\cdot10^{5}\,\text{s}}{3600\,\text{s/h}}$" converts with a conversion factor. The teacher's standing rule is conversion by substitution. Fix: since $1\,\text{h} = 3600\,\text{s}$, $1\,\text{s} = \tfrac{1}{3600}\,\text{h}$, so $1{,}447\cdot10^{5}\,\text{s} = 1{,}447\cdot10^{5}\cdot\tfrac{1}{3600}\,\text{h} = 40{,}2\,\text{h}$. Alternatively, count the hours: $1{,}447\cdot10^{5}\,\text{s} : 3600\,\text{s} = 40{,}2$.

## Polish
- solutions.md L3-02 Muunnokset: "$3474\,\text{km/px}$" reads like a conversion factor. It is the drawing's scale, so say so: "jokainen $3474\,\text{km}$ on yksi kuvapiste", then $4{,}498\cdot10^{9}\,\text{km} : 3474\,\text{km} = 1{,}295\cdot10^{6}$, i.e. that many px. That matches L1-05.

## Checked
- One script recomputed answers.py independently. All 12 answers agree; the largest deviation is 0,12 % (L1-03, rounded to 2 sf by design). Tolerance 0,02 accepts correct rounding.
- Round 1 blockers fixed: L1-01, L1-02 and L2-03 now substitute the unit's value (µm → $10^{-3}\,\text{mm}$, km → $10^{-3}\,\text{Mm}$, km² → $100\,\text{ha}$). L3-01 counts the AU with ":".
- The intermediate values are right: $4{,}498\cdot10^{9}\,\text{km}$ and $1{,}295\cdot10^{6}\,\text{px}$ (L3-02), $2{,}169\cdot10^{10}\,\text{km}$ and $1{,}447\cdot10^{5}\,\text{s}$ (L3-03), $9{,}462\cdot10^{12}\,\text{km}$ (L3-01), $1\,325\,462\,\text{km}$ (L2-04).
- The significant-figure justifications are correct: 384 400 km is read as 4 sf; 1920 px and 86 400 s are exact.
- The reasonableness checks are real estimates (L3-03: 145 · 8,3 min ≈ 20 h one way; L3-01: 525 600 : 8,3 ≈ 63 000).
- No ×, \times or slash divisions; \cdot and ":" are used throughout.
- The physics is within FY1 scope (s = vt, t = s : c, N = ft, area as a product) and uses the brief's symbols.
