VERDICT: FAIL
CONTENT-HASH: 158c51c2692dd49b

## Blocking
- Numbers with units are still plain text, against the teacher's all-LaTeX rule: exercises.json:56 ("15 Wh"), exercises.json:82 and solutions.md:92 ("365 vuorokautta"), solutions.md:89 ("365 vuorokaudessa") and solutions.md:119 ("hieman yli 100 km"). — Write $15\,\text{Wh}$, $365\,\text{vrk}$ and $100\,\text{km}$.

## Polish
- solutions.md:56 (L2-01) — "$1\,\text{min} = \tfrac{1}{60}\,\text{h}$" uses a fraction for a written division, and the teacher prefers the colon. It is acceptable as a formula line; optionally write $1\,\text{min} = 1\,\text{h} : 60$.
- solutions.md:48 (L1-05) — the aside "$1{,}08 \cdot 10^{7}\,\text{J}$" carries three significant figures from two-figure data. — Write $1{,}1 \cdot 10^{7}\,\text{J}$.

## Checked
- I recomputed all 12 answers in one script: 2000, 40, 60, 3500, 3,0, 3,0 €, 54 000, 1200, 78,84 → 79, 15,18 → 15, 342,5 → 340 and 102,2 → 100. They match answers.py, and every stated answer lies within its tolerance.
- All round-1 blockers are fixed: L3-02 now compares with 4 · 80 W = 320 W, L2-04 and L3-01 convert W → kW by substitution, and most quantities are now in LaTeX.
- Each solution has all seven parts, solves symbolically before substituting and gives a real reasonableness check (L2-02 now uses 15 W charging and 2 W use).
- Magnitudes are realistic: kettle 2 kW, microwave 1,2 kW, sauna heaters 3,5–6 kW, 3000 kWh/a per household, an EV at 18 kWh/100 km and 2,3 kW socket charging.
- Scope is FY2: no work, force or efficiency chain. There is no ×.
