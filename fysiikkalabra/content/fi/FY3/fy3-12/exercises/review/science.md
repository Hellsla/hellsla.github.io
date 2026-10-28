VERDICT: PASS
CONTENT-HASH: df8f923b0fdab0bc

## Blocking

## Polish
- lessons/FY3/fy3-12/answers.py:16 — the comment ends "-> 240" but the answer is 238 W/m² — match the comment to exercises.json.
- exercises/solutions.md:19 (L1-02 Järkevyys) — "vanhan oven arvo on uuden oven luokkaa … kuten odottaa sopii" is not a real check: an old door is expected to be worse than a new one — compare with a typical old door (about 1–2 W/(m²·K)), or drop the "kuten odottaa sopii".

## Checked
- All 12 answers recomputed in one script from the task text with my own formulas. All agree with answers.py and exercises.json, and every tolerance covers the rounded Vastaus (430 W, 150 €, 210 kWh, 0,14 K, 980 kWh).
- P = UAΔT is used with its constant-temperature condition. Parallel parts add (L2-01). ΔT goes across zero with the sign (L1-01, L1-02, L2-03).
- L1-05 and L2-04 are energy balance with albedo: (1 − r)·340 and (r₁ − r₂)·340. The hypothetical nature of the 1 %-point change is stated. The comparison with the 1,0 W/m² imbalance is right.
- L3-01: Q = cmΔT applies (no change of state, as stated). The thermos explanation is correct: the vacuum stops conduction and convection, shiny surfaces reflect radiation, and the remaining loss goes through the neck and lid.
- L3-02: 1,6 · 10²² J per year, 0,14 K in ten years for the top 700 m layer (its mass 2,6 · 10²⁰ kg is consistent with the ocean area). The atmosphere comparison (about 28 K) supports "kymmeniä kelvinejä".
- L3-03: electricity saved = Q/ε with the seasonal mean ε, as the task gives it. The argument against the neighbour (the pump moves heat, and its electricity scales with the heat demand) is correct.
- Units (Wh → kWh, vrk → h, a → s) and the significant-figure reasons are right. The symbols match the lesson.
