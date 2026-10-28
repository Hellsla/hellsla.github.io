VERDICT: PASS
CONTENT-HASH: 30919a669a7969f5

## Blocking

## Polish
- solutions.md:89 (L2-04, reasonableness check) — "$216\,\text{Wh} \approx 0{,}22\,\text{kWh}$" converts with no substitution step. — Write $216 \cdot 10^{-3}\,\text{kWh}$.

## Checked
- I recomputed all 12 answers in one script, independently of answers.py: 2000, 40, 60, 3500, 3,0, 3,0 €, 54 000, 1200, 78,84, 15,18, 342,5 and 102,2. They match answers.py, and every stated answer (79, 15, 340, 100) lies within its tolerance.
- Each solution has all seven parts, is solved symbolically before substitution, does its conversions by substitution (min → h, W → kW, Wh → J, kWh → J) and gives a real reasonableness check.
- Round-2 findings are fixed: the plain-prose numbers are now LaTeX, L2-01 uses $1\,\text{h} : 60$, and L1-05 gives $1{,}1 \cdot 10^{7}\,\text{J}$.
- L3-02 answers its "suurempi vai pienempi, miksi" part: the average power is small next to the sum of the nameplate powers.
- Magnitudes are realistic: kettle, microwave, sauna heaters, 3000 kWh/a per household, an EV at 18 kWh/100 km and 2,3 kW socket charging.
- Scope is FY2. There is no ×, and inline divisions use a colon.
