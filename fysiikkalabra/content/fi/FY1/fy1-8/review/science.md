VERDICT: FAIL
CONTENT-HASH: 3b526855315a1b03

## Blocking
- inquiry.json:40 — kertaus, correct option's feedback: `(4{,}9 - 4{,}6) : 2\,\text{s} = 0{,}15\,\text{s}` now reads as "0,3 divided by 2 s" (unit 1/s), so the colon sweep made the unit placement wrong/ambiguous — write `(4{,}9\,\text{s} - 4{,}6\,\text{s}) : 2 = 0{,}15\,\text{s}`.
- inquiry.json:195 — Etsi virhe, correct option: `0{,}60 \cdot 0{,}2 : 0{,}050\,\text{m} = 2{,}4\,\text{m}` reads as division by 0,050 m (result unit 1/m·…) — write `0{,}60\,\text{m/s} \cdot 0{,}2\,\text{s} : 0{,}050 = 2{,}4\,\text{m}`.

## Polish
- inquiry.json:231 — siirto mistake feedback `0{,}3 : 0{,}030 = 10\,\text{s}`: unit appears only on the result — `0{,}3\,\text{s} : 0{,}030 = 10\,\text{s}`.
- inquiry.json:197 — "käsikellolla ei voi mitata millimetrien matkaa": the wrong result 0,024 m is 2,4 cm — "parin senttimetrin matkaa".

## Checked
- Notation sweep (a196d94): other `/` → `:` replacements correct and unambiguous (ε = Δt : t̄, v = s : t̄, Δs : Δt, t : s, t_min = Δt : ε_max, 23,7 s : 5, 1,7 m : 0,42 m/s, 0,2 s : 4,05 s); no `×`/`\times`; remaining `/` are unit fractions; measurement uncertainty written Δt throughout.
- Display formulas ε = Δt/t and t ≥ Δt/ε_max correct with conditions (Δt roughly constant, reaction time).
- Worked example: 0,2 : 0,050 = 4 s, 0,42 · 4 = 1,68 → 1,7 m; check 4,05 s, 4,9 %, 0,50 m → 17 %.
- Group B table recomputed (means, half-ranges, ε 12/6,1/2,8/3,2/2,5 %, v 0,39–0,42); A ±0,10, B ±0,01 m/s; 0,39 ± 0,05.
- graafi slope 0,42 (mistakes 2,4, 2,1); siirto 14 m (0,14, 10); tarkistus-2 2,0 % (4,0, 0,02); exit ticket 10 s.
- Figures to scale: setup 150 px/m, ε = 0,2 s/t curve (20 %, 5 %, 2 %), graafi points, ±Δt bars and fitted line (0,419 m/s).
- Hash identical at start and end.
