VERDICT: PASS
CONTENT-HASH: d7d0fa102f301d1d

Round 2: solutions.md:89 tab character replaced by "\text{mol}"; the round-1 blocking item is fixed.

## Blocking
- none
## Polish
- exercises/solutions.md:89 — "koska tilavuus ja paineiden lukemat ovat … kahden numeron tarkkuudella": the volume 2,00 l has three; the limiting datum is the read pressure difference 40 kPa. Name that one.
- exercises.json:91 (L3-02) — "$1{,}20\,\text{m}$ × $1{,}00\,\text{m}$": a × in text; NOTES §1 asks for \cdot.
## Checked
- Line 89 now ends "$0{,}0233$–$0{,}0247\,\text{mol}$"; no literal tab left.
- n_A − n_B = 40 000 Pa · 0,00200 m³/(8,31 · 400 K) = 0,02407 mol; tolerance 0,03 → 0,0233–0,0248 mol, matches the stated range.
