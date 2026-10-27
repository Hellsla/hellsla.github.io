VERDICT: FAIL
CONTENT-HASH: ce24300394b810dd

## Blocking
- inquiry.json check-2 solution — "892 kg/m³, kolme numeroa kuten 101 ja 171 kPa" breaks NOTES §2: the difference Δp = 70 kPa (and Δh = 8,0 m) has two figures — Fix: answer 890 kg/m³, justified by Δp = 70 kPa and Δh = 8,0 m.
- inquiry.json exp-1 question solution — the substitution gives 49,0 kPa / 5 m = "9,8 kPa/m", yet the answer is 9,81 kPa/m "kuten g"; the result does not follow from the working, and the difference 49,0 kPa has three figures — Fix: 9,80 kPa/m (three figures, as the difference 49,0 kPa has), compared with ρg = 9,81 kPa/m in Järkevyys.
- lesson.md:374 (Esimerkki, Tulos) — the justifications contradict each other: F gets two figures because h = 12 m has two, but p = p₀ + ρgh gets three "like 101 kPa", although ρgh (≈ 1,2·10² kPa) comes from the same depth — Fix: give the depth as 12,0 m (p ≈ 219 kPa) or give p ≈ 220 kPa.

## Polish
- solutions.md:1044 (L3-03) — by the addition rule 3,3 + 15,7 = 19,0 kPa; "19 kPa like 0,40 m" is not the rule taught for sums.
- solutions.md:994 (L2-02) — "katsotaan kolmen numeron tarkkuudella" is weak; state the data with three figures.
- solutions.md:1008 (L2-04) — overpressure written $p$; use $\Delta p$ as elsewhere.

## Checked
- All 12 answers.py lines recomputed independently; all match exercises.json within tolerance.
- Worked example: 117 720 Pa, 218 720 Pa, 1765,8 N, ≈ 180 kg; the window's net force correctly uses ρgh.
- Each solution's principle applies (rest, constant ρ, connected column, net overpressure); symbolic first; the cm², kPa, bar and MPa conversions are right.
- The reasonableness checks are real (back-substitution, 10 kPa/m, the L3-02 ratio 2500 = 0,25 m² / 1 cm²).
- siirto 0,757 m and its mistakes 10,3 and 0,000757.
- pred-1 and pred-2 numbers (150/199, 98→122, 199→223, about 12 %) and every option's feedback.
- virhe 29 kPa; check-3 ≈ 1,8 N; the exit ticket 49/150 kPa; the dam at 30 m ≈ 290 kPa.
- sim.js implements p₀ + ρgh, its limits stated; the simState keys exist; exp-1 locks ρ and exp-2 locks h; the readouts 150,1/199,1 kPa.
- Figures: brick areas 1:3, graph line 101→199 kPa.
- Scope inside FY3 (p = F/A, hydrostatic pressure, force as a scalar normal to the surface).
