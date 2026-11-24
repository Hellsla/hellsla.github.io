VERDICT: PASS
CONTENT-HASH: 1d7c1d40a93f5836

## Blocking

## Polish
- inquiry.json tarkistus-3 (model, criteria[2]) — "Arvo on mallin arvo, koska nopeus ei ole täysin vakio" mixes up two things. A value is a model value because it is computed from a model and not measured; that would still be true if v were exactly constant. The deceleration is the reason the model is only approximate. — Suggested wording: "Arvo on laskettu mallilla eikä mitattu. Malli on likimääräinen, koska Auringon vetovoima hidastaa luotainta hieman"; adjust criterion 3 the same way.
- lesson.md "Nopeus kuvaajasta" — the `kaavat` name "keskivauhti" sits next to the sentence "kulmakerroin on nopeus". This is right only because every example moves in the positive direction, which the Kaava section says. It is level C, but one clause ("tässä, kun liike on positiiviseen suuntaan, vauhti = nopeus") would remove any doubt.
- sim.js cartShape — the wheel turns by `v*tau*0.9` rad, but rolling at 7.67 px/m with a 5.5 px radius needs about 1.39 rad/m, so the wheels look as if they slip. This is presentation only.
- Scope note gives 119,7 AU for the heliopause crossing; the lesson uses 119,0 AU (Burlaga et al. 2019, Nature Astronomy, the published value) and states its source. That is acceptable. Its model value for Feb 2026 is 142,6 AU and not the brief's ~143, and the lesson explains the 0,5 AU difference correctly (Earth–Sun geometry up to ~1 AU). Teacher may want to confirm the choice of source.

## Checked
- One-script recomputation: worked example 2922 d, 0,0088602 AU/vrk, 144,89 → 144,9 AU, 2,17·10¹⁰ km. Feb 2026: 2659 d → 142,56 AU. Deceleration GM/r² at 130 AU gives Δv ≈ 0,09 km/s over 8 a ("noin 0,1 km/s" correct). 1 a ≈ 3,2 AU.
- Pysähdy boxes (18 m, 25 m/s, 72 km/h = 20 m/s), virhekäsitys 10/14 m, ennuste-2 14 m, virhe 23 m vs 33 m, siirto 390 m (mistakes 1092, 270), tarkistus-2 s₀ = 4,0 m (mistakes 7, 3), exit ticket 30 km and 10 m: all correct, one correct option each, distractor feedback right.
- Graph figure measured from SVG coordinates: 3 m/s lines, s₀ = 5 m, triangle Δt = 2 s, Δs = 6 m, ticks to scale. Motion figure intervals equal.
- Sim implements s = s₀ + vt; readout s, Δs and slope (pos(6)−pos(2))/4 = v; ranges fit 0–60 m (10 + 5·10); v ≥ 0,5, so positive direction as the model box says.
- koe-1/koe-2: s₀ and v locked, t varied, simState gives s and ds; t > 0 required, so s:t is defined; suggested 8 s is within 0–10 s. Conclusion model answer matches (5,0; 3,5; 2,0 m/s) and calls them model values.
- Kertaus (s, t) slope Δt/Δs consistent; check-c2 horizontal line = rest is correct.
- Scope: s = s₀ + vt only, no forces/vectors beyond sign; within FY1.
- Hash identical at start and end.
