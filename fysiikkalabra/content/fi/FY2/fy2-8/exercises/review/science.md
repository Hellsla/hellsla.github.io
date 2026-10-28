VERDICT: PASS
CONTENT-HASH: 65e8dbee4a6e41bb

## Blocking

## Polish
- exercises/solutions.md (L2-04 Kaava) — "$e_\text{kWh} = e_\text{MJ} \cdot 3{,}6\,\text{MJ/kWh}$" puts a number in the formula; a symbol for the conversion factor, substituted afterwards, would keep "symbols first" strict.

## Checked
- All 12 answers recomputed in one script with my own formulas: identical to answers.py and exercises.json; every stated rounded answer inside its tolerance (closest L1-05 2,04 % of 3 %, L2-03 2,00 % of 3 %, L1-03 1,85 % of 2 %).
- Round-2 blocker fixed: every Järkevyys conversion now substitutes the factor (L1-01, L1-02, L1-05, L2-01, L2-02, L2-03).
- Round-2 polish taken: L3-01 and L3-03 Kaava now symbolic ($m = e \cdot V \cdot h$, $: N$) with units kept in the substitution; $25$ in LaTeX.
- No student-visible number outside LaTeX in exercises.json or solutions.md.
- Data: table values match IPCC AR5 WG III Annex III medians; petrol 69 g/MJ and diesel 74 g/MJ are IPCC 2006 defaults, consistent with 32 and 36 MJ/l.
- L3-02 yields marked as rounded example values and realistic; 100 km² vs 2,0 km², ratio 50; ha → km² by substitution.
- Every solution has the seven parts; principles apply; L2-03, L3-01, L3-02 solved symbolically before substitution; L2-04 correctly separates fuel energy from electricity.
- L3-01: 736 g/kWh below coal 820 — conclusion right, crudeness stated. L3-03: 4,14 right.
- Scope: m = e · E only, no FY3 content; no ×; written division as colon (solved fractions only in symbols).
