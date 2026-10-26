VERDICT: PASS
CONTENT-HASH: 9d4f49ca7d999aed

## Blocking

## Polish
- sim-spec.md — the spec still lists only the simState keys; the adapter's get() now also returns Vgas (ml) and VperT (ml/K), which Koe 2 measures — add one clause to the spec.
- inquiry.json exp-2 question — the student's own finite-difference slope (60,2 − 50,0) ml / 60 K = 0,170 ml/K differs slightly from the quoted 0,171 ml/K (= V/T); both give 3,4·10⁻³ 1/K, so this is not an error, but "noin 0,17 ml" would match both routes.

## Checked
- Hash 9d4f49ca7d999aed at start and end; answers.py output equals my independent recomputation for all 12 exercises (67,3; 13,7; 287; 2,6; 87,3; 2,0; 90; 2,0; 890; 5,9; 202; 29,9), all inside tolerance at the stated significant figures.
- Ennuste 2 (isobaric): 50 ml · 353,15/293,15 = 60,2 ml, V/T = 0,1706 ml/K; distractors 200 ml (°C ratio), 50 ml, 110 ml (1 ml/°C) and their feedback physically correct.
- Koe 2 run in Playwright on the preview: mode locked isobaarinen, p stays 100 kPa; rows 20/80/150/−50 °C give V = 50,0/60,2/72,2/38,1 ml, V/T = 0,171 ml/K every row; Vgas and VperT keys present and correct (simState.V·10⁶, ·/T).
- Koe 2 question: 0,1706/50 = 3,41·10⁻³ = 1/(293 K) — correct option and distractor feedback right.
- Ennuste 1/3 and Koe 1: pV = 5,00 J, 25/50/100 ml → 200/100/50 kPa; slider range 20–100 ml covers them; Pa and J units in the table consistent.
- Kertaus 30 N; ruisku table pV 5040/5050/5040/5430/5040 kPa·ml, 168 kPa, "lähes 8 %"; virhe 252,5 ≈ 250 kPa; siirto 1,07 l with mistakes 2,10 and 0,00107; check-2 120 kPa with mistakes 108 and 0,12; exit ticket 160 kPa, 308/280 = 1,1.
- Worked example symbolic first: 1,036 l ≈ 1,0 l (+30 %); misconception 1,00 l → 1,04 l (+3,5 %).
- SVG figures: (V, p) points have constant (x−x₀)(y₀−y) ≈ 8360 px²; (1/V, p) points on the drawn line through the origin; (T, V) figure scaled 1,2 px/K with points at 253–373 K on the line through 0 K.
- sim.js: isothermal p = p₀V₀/V, isobaric V = V₀T/T₀, isochoric p = p₀T/T₀; constants and SI conversions in simState correct; chart ranges contain every reachable state (V ≤ 72,2 ml, p ≤ 250 kPa / 144 kPa).
- Solutions: gauge vs absolute pressure correct (L3-02, L3-03); kelvins in every T ratio.
