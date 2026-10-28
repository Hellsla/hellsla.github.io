VERDICT: FAIL
CONTENT-HASH: bff7149aaf35caf4

## Blocking
- content/fi/FY3/fy3-9/lesson.md:124, :340, :480 — (B) "tilavuus / paine on suoraan verrannollinen kelvinlämpötilaan" and "suoran jatke kulkee origon ... kautta" are stated without the condition the guardrails require (p ∝ T and V ∝ T hold for a thin gas far from condensing, with a fixed amount of gas), and the extrapolation to 0 K is not marked as the model's prediction. The lesson is also inconsistent with its own inquiry.json, whose `contribution` and `prior` say "harvan kaasun" and "kun kaasun määrä pysyy samana" — add "suljetun, harvan kaasun" (or "kun kaasu on kaukana tiivistymisestä") in the Kaava sentence at :340 and the Tiivistelmä item at :480, and one clause after :340 such as "Todellinen kaasu tiivistyy ennen kuin 0 K saavutetaan; jatke näyttää, mihin harvan kaasun malli johtaisi."
- content/fi/FY3/fy3-9/inquiry.json:446 — (A, assessment) check-3's fourth criterion ("kaasun määrän on pysyttävä samana eli ruisku ei saa vuotaa") asks for something the prompt does not ask (the prompt asks only why the piston moves slowly and why the data go into (1/V, p)); a criterion asks only what the task asks — drop it, or extend the prompt ("…ja mitä muuta koejärjestelyssä on varmistettava?").

## Polish
- content/fi/FY3/fy3-9/lesson.md:124 — the isochoric pressure rise gets no mechanism in the theory (pred-2's feedback has it: faster particles hit more often and harder); one clause would close the causal chain.

## Checked
- One Python run recomputed every number: example 1,036 l (+30 %, pV 80,8 kPa·l); misconception 1,035 → 1,04 l; kertaus 30 N and every distractor (300 N, 0,030 N, 3,3·10⁸ N); pred-1 200 kPa, pV 5,00 J; pred-2 60,2 ml, V/T 0,171 ml/K, 1/293 = 3,41·10⁻³ 1/K; ruisku pV 5040 vs 5430 (+7,7 %), 168 kPa; virhe 252,5 ≈ 250 kPa; siirto 1,0693 → 1,07 l (mistakes 2,10 l, 1,07·10⁻³); check-2 120 kPa (mistakes 108, 0,12); exit ticket 160 kPa and 308/280 = 1,1.
- Boyle's conditions (fixed amount, constant T, absolute not gauge pressure, ordinary p and T) stated; microscopic explanation (same speed, twice as many hits) right and consistent in theory, figure, pred-1 and check-1.
- Figures generated from pV = 2000 kPa·ml and p₀/273,15 K; scales and points consistent.
- Simulation: pV/T = constant in three modes, speed ∝ √T; simState `p` (Pa), `constant` (J in isothermal), adapter `Vgas` (ml), `VperT` (ml/K) match the experiments' labels; exp-1 locks mode and T, exp-2 locks mode (isobaric holds p).
- Exactly one correct option in every choice item; the ruisku item's "leak" distractor correctly refuted (a leak lowers pV).
- Hash identical at start and end.
