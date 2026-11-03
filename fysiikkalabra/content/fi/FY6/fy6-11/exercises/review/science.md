VERDICT: FAIL
CONTENT-HASH: ca9f4a8b0d987104

## Blocking
- exercises/exercises.json:91 (fy6-11-L3-02) — (B, missing condition) the electron is said to accelerate from rest across 1,0 cm and reach $4{,}2 \cdot 10^{6}\,\text{m/s}$; this holds only in vacuum (in air it would collide long before) — add "Levyt ovat tyhjiössä." to the task and "tyhjiössä, joten muita voimia ei ole" to the solution's Periaate.
- exercises/solutions.md:34 (L1-04), :113 (L3-03) (also the short forms at :14, :24, :44, :55, :65) — (A, course rule) "kentän voimakkuuden … yhteys $E = U : d$" and "kentän voimakkuus $E = 1{,}5 \cdot 10^{5}\,\text{N/C}$"; E is lähdejännite elsewhere in FY6, so the field must be named "sähkökentän voimakkuus $E$" — rename.

## Polish
- solutions.md:45 (L1-05) — "ruudukkoviivojen risteykseen $(4{,}5\,\text{nC};\ 135\,\mu\text{N})$, sillä $135\,\mu\text{N}$ on puolivälissä viivojen $130$ ja $140$ välissä" contradicts itself (a point halfway between lines is not a crossing) — "suora kulkee pisteen $(4{,}5\,\text{nC};\ 135\,\mu\text{N})$ kautta, puolivälissä viivojen 130 ja 140 µN välissä".
- solutions.md L3-01 Vastaus — "noin $340\,\text{V}$ (tarkemmin $338\,\text{V}$)": give one answer with its precision.

## Checked
- All 12 answers recomputed independently: 4,0·10⁴ N/C; 100 µN; 1,5·10⁴ V/m; 70 mV; 3,0·10⁴ N/C; 2,0 mN; 15 kV; 20,4; 0,45 mN; 337,5 V; 4194 km/s; 23,1 nC — match answers.py and exercises.json.
- fq-graph: least-squares slope through the origin of the four points 29,9 µN/nC; the drawn line reaches (4,5 nC; 135 µN) = 3,0·10⁴ N/C; slope read from the fitted line, not a raw point.
- L3-03 force balance (T sin α = qE, T cos α = mg) correct and stated from the forces; L3-01 qU constant at fixed m, g, d; L3-02 v = √(2eU/m), 1,4 % of c, classical OK.
- L2-04 inverse proportionality to d (not 1/d²) with the condition "kaukana levyjen päistä" in the task.
- L1-04 membrane 1,0·10⁷ V/m over 7 nm = 70 mV, plausible resting potential; L2-01 field below air breakdown.
- Symbolic solving first, conversions (kV, mm, cm, nC, µN, g) correct, rounding by the limiting datum.
