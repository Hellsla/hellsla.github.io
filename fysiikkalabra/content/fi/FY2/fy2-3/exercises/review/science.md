VERDICT: FAIL
CONTENT-HASH: 9ec8a2c9617d8801

## Blocking
- exercises/solutions.md:109 (L3-02 Järkevyys) — "340 W vastaa kolmen television (80 W) jatkuvaa käyttöä" is wrong: 3 · 80 W = 240 W. — Write "noin neljän television (4 · 80 W = 320 W)".
- exercises/solutions.md:86 (L2-04) — "$9{,}0 : 1000\,\text{kW}$" is dimensionally wrong (a quantity divided by 1000 kW) and is not a conversion by substitution (teacher rule). — Write $9{,}0\,\text{W} = 9{,}0 \cdot 10^{-3}\,\text{kW} = 0{,}0090\,\text{kW}$.
- exercises/solutions.md:96 (L3-01) — "$52\,\text{W} = 0{,}052\,\text{kW}$" is stated without the conversion step (rule 7(4); substitution). — Write $52\,\text{W} = 52 \cdot 10^{-3}\,\text{kW}$.
- exercises.json:14, 22 and most task texts; solutions.md Järkevyys prose (e.g. lines 8–9, 69, 109) — quantities with units appear as plain text (8,0 W, 1200 W, 72 000 J, 2000 W). The teacher's rule is that everything is in LaTeX. — Put each one in $…$.

## Polish
- solutions.md:69 (L2-02) — "15 W sopii puhelimelle" endorses an unrealistic magnitude: a phone in use draws about 1–5 W, so the battery lasts hours, not one hour. — Turn the check around: at 15 W charging the battery fills in about an hour; at 2 W of use it lasts about 7 h.
- solutions.md:8 (L1-01), L2-03, L3-02, L3-03 — "2000 W, kolme merkitsevää numeroa" cannot be read from 2000 or 1200. — Write $2{,}00 \cdot 10^{3}\,\text{W}$, $1{,}2 \cdot 10^{3}\,\text{W}$, $3{,}4 \cdot 10^{2}\,\text{W}$ and $1{,}0 \cdot 10^{2}\,\text{km}$.
- solutions.md:99 (L3-01) — "muutaman kympin sijaan" is confusing as a check. — Compare the annual saving with the cost of an LED lamp instead.
- solutions.md L2-01 Järkevyys — the rounded check (6 · 2 = 12 kWh → 2,4 €) does not reach 3,0 €. — Use 6 kW · 2,5 h ≈ 15 kWh directly, or scale by 2,5 : 2.

## Checked
- I recomputed all 12 answers in one script: 2000, 40, 60, 3500, 3,0, 3,0 €, 54 000, 1200, 78,84 → 79, 15,18 → 15, 342,5 → 340 and 102,2 → 100. All agree with answers.py and lie within tolerance, and rounding to the data's figures stays inside it.
- Magnitudes are realistic: kettle 2 kW, microwave 1,2 kW, sauna heaters 3,5–6 kW, a 15 Wh phone battery, 3000 kWh/a per household, an EV at 18 kWh/100 km, 2,3 kW socket charging.
- Each solution solves symbolically before substituting. The kWh → J conversions are done by substitution.
- Scope is FY2: no work, no Q = cmΔT, no efficiency chain. No × anywhere.
