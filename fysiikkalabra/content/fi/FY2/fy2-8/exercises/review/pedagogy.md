VERDICT: PASS
CONTENT-HASH: 3f12bb56f3517b66

## Blocking

## Polish
- exercises.json L3-02 — the task is the longest in the set (about 90 words: two yields, a unit relation, a numeric and an interpretive question). Fix: split into situation (city, two options with yields), then the numeric question, then the interpretive sentence as its own last line; the interpretive answer is not checked, so say "Perustele lyhyesti" to mark it as a written part.
- exercises.json L3-02 — the numeric answer (100 km²) checks only the biomass area, while the question asks to compare with the solar park; the student can skip the solar calculation. Fix: ask for the ratio of the areas as the numeric answer (50 kertaa) and keep the km² values in the solution.
- exercises.json L1-04 — a level 1 task with no situation, only two coefficients and a ratio, and it no longer uses m = e · E. Fix: open with a situation ("Naapurit vertailevat sähkönsä päästöjä: ...") and state the question last; keep it as the single comparison item.
- Still open from round 1: no `mistakes` feedback in exercises.json for the expected slips (GWh not converted, grams instead of kg or t); add if the schema allows.

## Checked
- Levels 5 / 4 / 3 per the rubric; no task repeats the worked example (gas, 4800 kWh, tonnes).
- Round-1 polish closed: written division uses a colon in the solutions (`E = 12 \cdot 10^{6}\,\text{g} : 490\,\text{g/kWh}`, `m_\text{auto} : m_\text{bussi}`); symbolic `\dfrac{E}{q}` in L3-02 may stay (NOTES §1).
- Round-1 polish closed: L3-01 and L3-02 now end with an interpretive question and the solution has a "Johtopäätös" (coal electricity gives no benefit over petrol; land use is what the coefficient does not show); the slot's täsmennys (land use) is practised.
- Answers recomputed: L1-04 490 : 41 = 11,95 → 12 (tolerance covers 11,8 to 12,2); L3-02 100 GWh : 0,010 GWh/ha = 10 000 ha = 100 km²; solar 200 ha = 2,0 km², ratio 50; L3-01 736 → 740; L3-03 4,14 → 4,1. Consistent with answers.py.
- Every changed solution keeps the seven parts: given, asked, principle in words (L3-02 explains yield per hectare by analogy with e · E), symbols first, conversions by substitution (1 ha = 0,01 km²), significant figures stated, rounded-number check.
- L2-04 solution now says why g/kWh of a fuel differs from the table's g/kWh of electricity.
- LaTeX: every number with unit in the diff is now in `$...$`; decimal comma in the source; case endings (`$100\,\text{km}$:llä`) correct.
- Levels 3 yield data are marked as rounded example values, not statistics.
- Hash at the end: 3f12bb56f3517b66 (unchanged).
