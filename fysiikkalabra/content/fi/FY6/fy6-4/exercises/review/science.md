VERDICT: PASS
CONTENT-HASH: b76783ab2894e5cb
SCOPE: delta added-exercise from f628c9c4d2493275 base 8f23aa7ae3bd

## Blocking

## Polish
- content/fi/FY6/fy6-4/exercises/solutions.md (fy6-4-L2-09, Vastaus) — "$500\,\text{mA}$, kaksi merkitsevää numeroa" does not show two figures; write $0{,}50\,\text{A} = 5{,}0 \cdot 10^{2}\,\text{mA}$ or "noin $500\,\text{mA}$ ($0{,}50\,\text{A}$)".

## Checked
- Hash b76783ab2894e5cb at start and end; delta: only fy6-4-L2-09 judged.
- Figure topology traced from figures.py: + plate up to node (xL, T); R1 on the top wire from that node to the right side, which runs down to the second node (xR, M); R2 on the middle wire between the same two nodes; the right side continues to the bottom wire and the − plate. R1 and R2 are truly in parallel across the battery; values 9,0 V, 30 Ω, 45 Ω readable; no current shown. Alt text gives the same topology and values.
- Assumptions (ideal battery, wire resistance neglected) are in the task, as in the lesson's example.
- Recomputed: R = 30 Ω · 45 Ω : 75 Ω = 18 Ω; I = 9,0 V : 18 Ω = 0,50 A = 500 mA; branch currents 0,30 A + 0,20 A = 0,50 A; answers.py agrees; unit mA and tolerance 2 % fit.
- Not a repeat of the worked example (different values, answer asked in mA); formulas and notation are the lesson's.
- Solution complete: reading the figure, principle with reason, symbolic R and I before numbers, conversion, substitution with units, check by branch currents and R below the smaller resistor.
