VERDICT: PASS
CONTENT-HASH: 3cc6d946afc32a21
SCOPE: delta: round 2, the fixes of round 1 in fy9-kokeellisuus-s7 and -s8; the intro and older tasks s1-s6 untouched
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
- (none)

## Polish
- s8 c Principle: "An error that is constant and does not depend on the current is called systematic" reads like a definition. A systematic error need not be constant (s7 a now names a scale error, which is proportional). "A constant error is systematic" says the same thing without narrowing the term.

## Checked
- Round 1 Blocking 1 (s8 b heating as a cause of nonlinearity) is fixed in the English text. Criterion 3 now reads "the result is extrapolation ... about twice that. The coil and the power supply must be able to carry such a current ... checked by measuring". Reasonableness: "According to the model $B = \mu_0 n I$ the dependence stays linear, but it has not been measured in this range". No heating-resistance reason is left in b.
- Round 1 Blocking 2 is fixed: the "$12 : 6.2 \cdot 2.5\,\text{A}$" item is gone. The b mistake is now inverting the slope ($I = kB$) or no reliability assessment.
- Round 1 Polish is all done. s8 d (model answer and criterion 3) says "the current may drift if the supply regulates voltage, or the sensor reading may drift with temperature". s8 a Answer says "the values read have two figures". s7 a has the scale (calibration) error clause.
- Rounding matches the Finnish text and the data's precision: s7 c "about $14\,\%$", s8 c $3\,\%$ and $0.6\,\%$ with the reason (one figure in $0.04\,\text{mT}$), b $4.9\,\text{A}$. The tolerances in tasks.json are the same as fi and accept them. The decimal point is used throughout. Units are language-neutral (1/m, mT/A, Vs/(Am)), and the chains are aligned rows.
- I recomputed the numbers in the same script as fi: s7 0.2152 ± 0.005, c 0.24 / 0.21 / 14.3 %, mistake 12.5 % ≈ 13 %, d 4.5 % and 0.93 %; s8 k = 2.467 mT/A, n = 1963 1/m (×1000 without conversion), b 4.86 A (range 4.8–5.0), c 3.08 % and 0.645 %. All agree.
- The translation of the fixed sentences is faithful part by part. Points are still 14 + 14. The intro says "Eight", which matches the 8 tasks.
- Packet rebuilt (fixed text present), `practice.py check: OK`; the hash is the same at start and end.
