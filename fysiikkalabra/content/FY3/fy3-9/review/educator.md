VERDICT: FAIL
CONTENT-HASH: 10f5daa923494e9f

## Blocking
1. lesson.md:10, :19 — The core skill in the goals (meta.json: "kääntäen verrannollisuus graafisesti p = vakio·1/V") is only asserted: "Jos laki pätee, pisteet ovat origon kautta kulkevalla suoralla". The lesson never shows why plotting against 1/V gives a line. — After line 19, add a display formula `p = \text{vakio} \cdot \frac{1}{V}` and one sentence: "Kun vaaka-akselille merkitään x = 1/V, yhtälö on muotoa y = kx kuten FY1:n suoralla, joten kuvaaja on origon kautta kulkeva suora, jonka kulmakerroin on k = pV."
2. exercises.json:64 (L2-03) — "Anna se jouleina" needs kPa·ml → J (10³ · 10⁻⁶ = 10⁻³). The lesson never says that pV has the unit joule. It is the only exercise on the core skill. Together with the column, the graph and the fit, it is more than a level 2 task. — Add to lesson.md after :19: "Tulon pV yksikkö on Pa · m³ = N/m² · m³ = N · m = J, ja kätevästi 1 kPa · 1 l = 1 J." Alternatively, ask for the slope in kPa·ml (and update answer and tolerance in answers.py).

## Polish
1. lesson.md:12 — The chip-bag answer comes right after the kelvin sentences, introduced with "Tämä vastaa…". A student may think the bag swells because of temperature, but the cause is the pressure drop (Boyle). — Move the sentence to the end of line 8, after "Tätä sanotaan Boylen laiksi": "Tämä vastaa alun kysymykseen: …".
2. lesson.md:12 — The paragraph describes the two constant-pressure and constant-volume laws but does not use the names from line 6. — "…pysyy vakiona (isobaarinen tilanmuutos)…" and "…pidetään vakiona (isokoorinen tilanmuutos)…".

## Checked
- Lint: 0 errors, 0 warnings. Hash unchanged from start to end.
- Motivating question (chip bag on a plane) is everyday and is answered.
- Prerequisites used correctly: micro-model and kelvin (fy3-3), p₀ + ρgh and ylipaine (fy3-4, L3-01–03), gas expansion (fy3-8:20).
- The four glossary terms are defined at first use (line 6). All are in glossary.json.
- Level 1: one formula each. The °C→K step matches the precedent in fy3-8.
- L1-02 solves for V₂ like the example, but the context is new (compression in a tank). It is not a repeat.
- Levels 2–3 fit the rubric, apart from L2-03 (Blocking 2).
- Exit ticket: Boyle calculation, the 1/V linearization and the kelvin ratio. These are the three core ideas, not details.
