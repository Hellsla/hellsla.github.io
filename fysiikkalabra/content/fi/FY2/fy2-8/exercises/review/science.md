VERDICT: FAIL
CONTENT-HASH: e6d7ee0e2e1ea72d

## Blocking
- exercises/solutions.md:67 (fy2-8-L2-02) — "2\,908\,800\,\text{g} = 2{,}9088\,\text{t}" converts grams to tonnes without the substitution step the teacher's standing rule requires (Muunnokset already states $1\,\text{g} = 10^{-6}\,\text{t}$). — Fix: "$= 2\,908\,800 \cdot 10^{-6}\,\text{t} = 2{,}9088\,\text{t}$".
- exercises/solutions.md:107 (fy2-8-L3-02) — same: "2{,}032 \cdot 10^{10}\,\text{g} = 20\,320\,\text{t}". — Fix: "$= 2{,}032 \cdot 10^{10} \cdot 10^{-6}\,\text{t} = 20\,320\,\text{t}$".

## Polish
- exercises/solutions.md:68 (L2-02) — the two figures come from $12\,\text{g/kWh}$ (and 3600 is ambiguous); name that datum in the rounding reason.
- exercises/solutions.md:109 (L3-02) — "sekoitus pienentää päästöjä yli puoleen" is ambiguous in Finnish; say "alle puoleen (noin 41 %)" of the all-gas emission.
- L3-01 and L3-03 compare petrol/diesel combustion CO2 only (IPCC 2006 factors) with lifecycle CO2-eq for electricity; L3-01 says so, L3-03 compares like with like — fine; consider "hiilidioksidia" rather than "hiilidioksidiekvivalenttia" wording consistency in L3-01's question.

## Checked
- All 12 answers recomputed in one script from the task texts with my own formulas: identical to answers.py and exercises.json; every rounded answer within its tolerance (largest 2,0 % on L1-05 tol 3 %, L2-03 tol 3 %; L1-03 1,9 % tol 2 %).
- Data: table values match IPCC AR5 WG III Annex III medians (hydro 24, coal 820, wind 12, PV rooftop 41, gas 490, biomass dedicated 230); petrol 69 g/MJ and diesel 74 g/MJ = IPCC 2006 defaults (69,3 / 74,1), NCV-consistent with 32 and 36 MJ/l.
- Magnitudes realistic: e-car 18 kWh/100 km, petrol 6,0 l/100 km, bus 30 l/100 km, rooftop 4200 kWh/a.
- Every solution has the seven parts, solves symbolically first (L2-03 $E = m : e$ as fraction, L3-01, L3-03), stated principle applies, checks are real checks (L2-04 notes per-fuel vs per-electricity energy correctly).
- L3-01: 736 g/kWh below coal 820 — conclusion right. L3-03: 13 248 g : 3196,8 g = 4,14 right.
- Scope: m = e·E only, no FY3 content; no ×, no plain-text calculation steps.
