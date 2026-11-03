VERDICT: PASS
CONTENT-HASH: f420280082218658

## Blocking

## Polish
- inquiry.json:243 — the feedback says that $b T$ "antaisi metrien aallonpituuden". The unit of $b T$ is m·K², so it is not a length at all. — Say that the unit does not come out as metres, so the formula cannot be right.
- lesson.md:332 — microwaves make the water molecules "värähtelemään". The mechanism is that the polar molecules turn back and forth with the field. — Write "kääntyilemään edestakaisin".
- assets/sims/fy7/fy7-9/sim.js:7 — the header comment says "no glow below about 750 K", but the code starts the glow and the colour names at 800 K. — Change the comment to 800 K.
- glossary.json "aallonpituus" — the definition ("samalla tavalla liikkuvan väliaineen kohdan") needs a medium, but this chapter's EM wave has none. — Add "tai kentän".

## Checked
- Recomputed independently: c = fλ examples (3,0 m; 12 cm); Wien values 9,66/9,44/3,62 µm; 502 nm → 5773 K; 900 °C → 2,47 µm vs 3,22 µm; 2430 °C → 1072 nm (mistake 1193 nm); lava 1380 K = 1107 °C (mistakes 1380, 1653,15). All agree.
- Planck M_λ in sim.js and lesson-answers.py: 2πhc²/λ⁵, exact SI constants. Golden-section peaks (300 K 9659 nm, 3000 K 966 nm, 4500 K 644 nm, 6000 K 483 nm) match a dense scan; λ_max T = 2,898·10⁻³ m·K. The sim finds the peak and does not use Wien's law.
- Visible share: 300 K ≈ 10⁻²⁰ % (the "alle 0,01 %" claim holds), 2700 K 7,0 %, 5800 K 43,9 %.
- Figure "curves" is to scale: the peak x-positions and heights (100,0; 40,2; 13,2 MW/(m²·µm)) match the pixels, and the 380–750 nm band is placed right.
- Experiments: koe-1 locks the range and varies T, and 3000–6000 K peaks stay inside 0–3000 nm. In koe-2 the 300 K peak (9,7 µm) is inside 0–30 µm. simState gives lmax.
- Predictions: each has exactly one correct option, and the feedback numbers are model values. The Etsi virhe item has one correct option, and so does check-1.
- Spectrum table boundaries, the ionising part, the X-ray tube as a decelerating charge, Kirchhoff (shiny metal emits less), and Stefan–Boltzmann 2⁴ = 16 are all correct and in scope.
- Kelvin requirement and the black-body condition are stated wherever Wien is used. The model answers and the exit ticket (⅓) agree with the theory.
- Hash was the same at start and end.
