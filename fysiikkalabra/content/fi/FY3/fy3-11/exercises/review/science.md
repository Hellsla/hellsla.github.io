VERDICT: PASS
CONTENT-HASH: 5cb4d86d56728236

## Blocking

## Polish
- exercises.json (fy3-11-L2-04) — "480 kW" alone does not show that its final zero is significant; the solution now declares it so. Acceptable, but the task could make it unambiguous (e.g. $480\,\text{kW}$ with "kolmen numeron tarkkuudella", or $0{,}480\,\text{MW}$).
- Earlier polish points (P_o named once, answers.py docstring, L3-04 Q₁, L2-09 stroke) remain optional.

## Checked
- Delta: L2-04 Periaate, L2-04 Vastaus, L3-01 Vastaus typo ("polttoatehon" → "polttoainetehon"), L3-02 Periaate.
- L2-04 recomputed: P_o = 480/0,400 = 1200 kW, P_hukka = 720 kW; answer 720, tolerance 0,02 unchanged.
- L2-04 rounding now three figures (480 kW read as three, 40,0 %), which matches 720 kW as given; the old reason ("two first figures certain") was self-contradictory. fi-easy and en solutions give the same three-figure reason, so the languages agree.
- L3-01 keeps two figures from 96 MW; ΔP = 240 + 200 − 320 = 120 MW unchanged.
- "hukkalämpöön, joka siirtyy ympäristöön" (L2-04, L3-02): energy conservation stated right, the waste heat leaves to the surroundings, matching the L2-04 question (pakokaasut, jäähdytysvesi) and the heat-engine model; no "heat created" picture.
- L3-02 W = ηQ₁ and P = ηρVH/t unchanged.
- No numbers, symbols or answers.py changed; hash 5cb4d86d56728236 the same at start and end.
