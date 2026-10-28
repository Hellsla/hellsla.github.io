VERDICT: FAIL
CONTENT-HASH: d343b548cba8c730

Delta review over the audit's PASS (1148bc79f3cd67b1): L2-04 (molar volume at −30 °C) replaced by a figure task (fy3-10/pt-suorat, n_A − n_B from two p(T) lines); other texts' numbers turned into LaTeX.

## Blocking
- exercises/solutions.md:89 — the Vastaus line ends "$0{,}0233$–$0{,}0247\,(tab)ext{mol}$": the "\t" of "\text" was written as a literal tab, so the unit renders as broken maths ("extmol"). Fix: "\,\text{mol}".
## Polish
- exercises/solutions.md:89 — "koska tilavuus ja paineiden lukemat ovat … kahden numeron tarkkuudella": the volume 2,00 l has three; the limiting datum is the read pressure difference 40 kPa. Name that one.
- exercises.json L3-02 — "$1{,}20\,\text{m}$ × $1{,}00\,\text{m}$": a × in text; NOTES §1 asks for \cdot (pre-existing, made visible by the LaTeX pass).
## Checked
- Figure code: A slope 0,25 kPa/K, B 0,15 kPa/K; points (200; 50), (400; 100), (200; 30), (400; 60) on 100 K / 10 kPa grid crossings; screenshot matches; lines through the origin as p = nRT/V requires.
- n_A = 100 kPa · 2,00 l /(8,31 · 400 K) = 0,06017 mol, n_B = 0,03610 mol, difference 0,02407 mol -> 0,024 mol; reading at 200 K gives the same.
- Tolerance 0,03 -> 0,02328–0,02472 mol, matches the solution's stated range; rejects n_A or n_B alone and any °C-based reading.
- answers.py = 0,024067; conversions (40 kPa = 40 000 Pa, 2,00 l = 0,00200 m³) right; ratio 100:60 = n_A:n_B ≈ 1,7 right.
- Task gives V, R and the ideal-gas assumption; values to read are not in the text.
- Other changes (LaTeX of 278 K, 425 g, 44 g/mol, 10,0 l, 2,40 kg, 15 °C, …) keep the same values.
