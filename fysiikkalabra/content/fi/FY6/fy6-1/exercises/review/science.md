VERDICT: PASS
CONTENT-HASH: 9415e187cfda526d

## Blocking

## Polish
- solutions.md:173 — L3-05 b): the chain writes $5{,}2 \cdot 10^{4}\,\text{s} : 3600\,\text{s/h} = 14{,}5\,\text{h}$, but the rounded value gives $14{,}4\,\text{h}$ (unrounded $52\,060\,\text{s}$ gives $14{,}46\,\text{h}$) — carry the unrounded $5{,}21 \cdot 10^{4}\,\text{s}$ or write $\approx 14\,\text{h}$; the final answer ($14\,\text{h}$) is right.
- solutions.md:144 vs :164 — L2-05 a) rounds a sum of interval charges by significant figures ("kuten virroissa", $23\,\text{C}$), L3-04 a) rounds a sum of interval energies by the decimal-place rule ($12{,}5\,\text{Wh}$). Both are defensible; you could make them use the same rule (by the L3-04 rule L2-05 would keep $22{,}8\,\text{C}$). This does not block: tolerance 2 % takes either.
- solutions.md:9 — L1-01's reasonableness check uses $P = UI$ ($21\,\text{W} : 12\,\text{V}$), which this chapter does not teach yet. You could replace it with a comparison the brief gives (the table's $2\,\text{A}$ charger).

## Checked
- I recomputed all 16 numeric answers in one script with my own formulas (I = Q/t, U = E/Q, Q = Ne, trapezoid sums, E = ΣUIt, v = I/(ne)). All agree with answers.py and exercises.json; the L2-07 means ($0{,}310$, $0{,}306\,\text{A}$) and the L3-04 b)/c) values ($3{,}35\,\text{Ah}$, $3{,}73\,\text{V}$, $45\,\text{kJ}$, $7{,}2\,\%$) agree too.
- Significant figures against P7: trailing zeros counted as significant (30 s, 40 s, 150 C, 3000 mAh), and in every case the limiting datum named is the real one (12 V, 3,7 V, 0,080 A, 0,25 A). The 2-figure answers (1,1·10² C, 40 kJ, 1,0·10¹⁸) fall inside the tolerances.
- L3-04's added justification is correct: the products of 2-figure data are each at 0,1 Wh precision, and so is the sum.
- The figures give exactly the data the solutions read: virta-kuvaaja (0,40 A for 0–20 s, 0,10 A for 20–50 s) and lataus-kuvaaja (rectangle 0–40 s, triangle 40–100 s). Neither shows the answer.
- kaavio-malli: the cells are in series the right way (− of the upper cell to + of the lower), and the current arrow runs from + along the top wire. It matches the model answer.
- L1-06, L1-07: exactly one correct option, and the feedback of every distractor is right physics (conventional direction, open loop, the air gap as an insulator).
- L1-09: the truth values of statements 1–5 are right ($18\,\text{C}$, $54\,\text{J}$, the 3,0 J/C reading).
- L2-06: the bypass is called a short circuit, with a safety note; nothing claims that a current is used up.
- L2-07: terms as in the guardrails (resolution = smallest display step); the differences have both signs; the conclusion is "does not support", worded correctly.
- Scope: everything stays inside FY6 jännite/sähkövirta and the brief's formulas; notation matches the lesson (I, Q, t, U, E, N, e).
