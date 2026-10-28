VERDICT: FAIL
CONTENT-HASH: 3f12bb56f3517b66

## Blocking
- exercises/solutions.md:9, 19, 48, 58, 68, 78 — conversions in the Järkevyys checks are bare equalities, against the teacher's standing rule (conversions by substitution); the round-1 main chains are now fixed. L1-01 "$75\,000\,\text{g} = 75\,\text{kg}$" and "$820\,\text{g/kWh} \cdot 3000\,\text{kWh} = 2460\,\text{kg}$" (skips the grams); L1-02 "$2400\,\text{g} \approx 2{,}4\,\text{kg}$"; L1-05 "$1000\,\text{g} = 1\,\text{kg}$"; L2-01 "$4 \cdot 10^{8}\,\text{g} = 400\,\text{t}$" and "$460\,000\,\text{kg} = 460\,\text{t}$"; L2-02 "$820 \cdot 3600\,\text{g} \approx 2{,}95\,\text{t}$", "$12 \cdot 3600\,\text{g} \approx 0{,}043\,\text{t}$"; L2-03 "$12 \cdot 10^{6}\,\text{g} = 12\,\text{t}$". — Fix: add the substituted step, e.g. "$= 75\,000 \cdot 0{,}001\,\text{kg} = 75\,\text{kg}$", "$= 4 \cdot 10^{8} \cdot 10^{-6}\,\text{t} = 400\,\text{t}$", "$= 460\,000 \cdot 0{,}001\,\text{t}$".

## Polish
- exercises/solutions.md:94, 115 (L3-01, L3-03 Kaava) — the "symbolic" formulas carry numbers (74 g/MJ, 36 MJ/l, 25); write them with symbols (e.g. $m = e \cdot h \cdot V$, $m_\text{bussi} = e_\text{b} h_\text{b} V_\text{b} : N$) and substitute after.
- exercises/solutions.md:117 (L3-03 Sijoitus) — "$74 \cdot 30 \cdot 36\,\text{g}$" drops the units l and MJ; keep them so they visibly cancel.
- exercises/solutions.md:119 — "25 matkustajalle" outside LaTeX.

## Checked
- All 12 answers recomputed in one script with my own formulas: identical to answers.py and exercises.json; every rounded answer inside its tolerance (closest L1-05 2,04 % of 3 %, L2-03 2,00 % of 3 %, L1-03 1,85 % of 2 %).
- Data: lesson-table values match IPCC AR5 WG III Annex III medians; petrol 69 g/MJ and diesel 74 g/MJ = IPCC 2006 defaults (69,3 / 74,1), consistent with 32 and 36 MJ/l.
- L3-02 land-use yields marked "pyöristettyjä esimerkkiarvoja" and realistic (solar park ≈ 0,5 GWh/ha·a; energy-crop electricity ≈ 0,01 GWh/ha·a); 100 km² vs 2,0 km², ratio 50 right; ha → km² by substitution.
- Round-1 blockers fixed (L2-02 now "$2\,908\,800 \cdot 10^{-6}\,\text{t}$"; L3-02 rewritten).
- Magnitudes realistic: e-car 18 kWh/100 km, petrol 6,0 l, bus 30 l/100 km.
- Every solution has the seven parts; principles apply; L2-03 and L3-02 solved as fractions before substitution; L2-04 check correctly separates fuel energy from electricity.
- L3-01: 736 g/kWh below coal 820 — conclusion right, comparison's crudeness stated. L3-03: 4,14 right.
- Scope: m = e · E only, no FY3 content; no ×; written division as colon.
