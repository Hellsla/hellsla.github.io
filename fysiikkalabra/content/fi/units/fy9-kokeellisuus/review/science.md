VERDICT: PASS
CONTENT-HASH: d1d051db0ddc4117
SCOPE: delta: round 2, the fixes of round 1 in fy9-kokeellisuus-s7 and -s8; the intro and older tasks s1-s6 untouched
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
- (none)

## Polish
- s8 c Periaate: "Virheen, joka on vakio ja ei riipu virrasta, kutsutaan systemaattiseksi" reads like a definition. A systematic error need not be constant (s7 a now names a scale error, which is proportional). "Vakio virhe on systemaattinen" says the same thing without narrowing the term. (The case "Virheen" should be "Virhettä"; language only.)

## Checked
- Round 1 Blocking 1 (s8 b heating as a cause of nonlinearity) is fixed. Criterion 3 now gives the point for extrapolation to about twice the largest measured current, a coil and supply that can carry it, and checking by measuring. Järkevyys says the model keeps the law linear but it has not been measured in this range. No heating-resistance reason is left in b.
- Round 1 Blocking 2 is fixed: the "$12 : 6{,}2 \cdot 2{,}5\,\text{A}$" item is gone. The b mistake is now $I = kB$ or no reliability assessment, which is a real error.
- Round 1 Polish is all done. s8 d (model answer and criterion 3) names the effect: the current drifts under a voltage-set supply, or the sensor drifts with temperature. s8 a Vastaus says "kaksinumeroisia". s7 a has the scale (calibration) error clause.
- Rounding: s7 c is now $\approx 14\,\%$ (from $14{,}29$), s7 d $\approx 5\,\%$ / $\approx 1\,\%$, and s8 c $3\,\%$ / $0{,}6\,\%$ with the reason (one figure in $0{,}04\,\text{mT}$). All match the data's precision, and the tolerances (14 ± 10 %, 3,1 ± 10 %, 0,65 ± 10 %, 4,9 ± 4 %) accept them.
- One script in the scratchpad recomputed everything: s7 ratios, mean 0,2152, ±0,005, c 0,24 / 0,21 / 14,3 %, mistake 12,5 % ≈ 13 %, d 4,5 % and 0,93 %. s8 k = 2,467 mT/A, n = 1963 1/m, mT/A without conversion gives 1000 times too large (1,96·10⁶), b 4,86 A, range 4,8–5,0 A, c 3,08 % and 0,645 %. All agree.
- The fixes reveal no structure in the task text, calculation chains are aligned rows, and units are language-neutral (1/m, mT/A). Points are still s7 3+4+4+3 and s8 4+3+4+3. The intro says "Kahdeksan", which matches the 8 tasks.
- Packet rebuilt (fixed text present), `practice.py check: OK`, `units.py check` 77 ok; the hash is the same at start and end.
