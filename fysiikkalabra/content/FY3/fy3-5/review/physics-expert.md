VERDICT: PASS
CONTENT-HASH: 36ffef8025cd3db6
## Blocking
(none)
## Polish
1. exercises.json:82 (fy3-5-L3-01) — "Mäntää painetaan … 120 N:n voimalla" is the hand's force on the piston; the work on the air also includes p₀ΔV from the atmosphere behind the piston (≈ 7 J), so W = Fs = 18 J is only an idealisation. — Word it as in L2-01: "Mäntä työntää ilmaa … keskimääräisellä 120 N:n voimalla".
2. solutions.md:77 — "Sisäenergia riippuu lämpötilasta ja aineen määrästä. Kumpikaan ei muutu, joten ΔU = 0" is stated in general, but it holds only for a gas with no phase change, and fy3-7 will teach melting at constant T with ΔU > 0. — "Kaasun sisäenergia riippuu (käytännössä) vain sen lämpötilasta ja määrästä …".
3. lesson.md:43 — "kaikki työn tuoma energia ehtisi siirtyä … Q = −150 J" quietly assumes the slow compression takes the same 150 J of work. — "Jos sama 150 J:n työ tehtäisiin niin hitaasti, että …".
4. exit-ticket.json:10–12 — the system is "pullon sisältö", yet the answer has energy moving from the coffee "pullon kylmempiin seiniin", which would cross the system boundary. — Make the system "pullon sisäosa (kahvi, ilma ja sisäseinä)" or say "kahvista pullon sisäilmaan ja sisäseinään".
5. lesson.md:10 — "Eristetyssä systeemissä … sisäenergia pysyy vakiona, vaikka energia sen sisällä vaihtaisi muotoa": by the lesson's own definition, U changes if mechanical energy inside turns into internal energy (a falling weight inside an insulated box). — "… systeemissä, joka ei itse liiku, sisäenergia pysyy vakiona" or "kokonaisenergia pysyy vakiona".
## Checked
- lint 0/0. answers.py output matches all 12 `answer` values within tolerance.
- ΔU = Q + W with W > 0 for work done on the system is used the same way in lesson.md:15–17, the SVG, the example, every solution, answers.py and the exit ticket. Every sign is read correctly from the text.
- Scope: first law only. There is no cmΔT, efficiency or second law. P = W/t, W = Fs and mgh all come from fy3-2.
- Recomputed by hand: L3-02 h = 1,699 m → 1,7 m; L3-01 Q = −18 J; L2-01 Q = −15 J.
- L1-03: W/Q = 2/7 = R/C_p, which is consistent for air at constant pressure.
- L2-03 and L3-03 are physically correct but have the same structure (pedagogy's call).
- Magnitudes, sig figs and units are realistic and consistent.

Python output:
```
{"fy3-5-L1-01": 570, "fy3-5-L1-02": -8.4, "fy3-5-L1-03": 250, "fy3-5-L1-04": -500, "fy3-5-L1-05": -70, "fy3-5-L2-01": -15.0, "fy3-5-L2-02": 160.0, "fy3-5-L2-03": 800.0, "fy3-5-L2-04": 12.0, "fy3-5-L3-01": -18.0, "fy3-5-L3-02": 1.698947, "fy3-5-L3-03": 160}
```
