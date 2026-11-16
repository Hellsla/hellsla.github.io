VERDICT: PASS
CONTENT-HASH: 300f0acc09180cf2

## Blocking

## Polish
- exercises/solutions.md:68 (L1-04 Järkevyys) — "$6\,\text{s} : 0{,}8 \approx 7{,}5\,\text{s}$" has the wrong unit on the speed. Fix: $6{,}0\,\text{m/s} : 0{,}8\,\text{m/s}^2 \approx 7{,}5\,\text{s}$.
- exercises/solutions.md:347 (L3-05 Vastaus) — "kolme merkitsevää numeroa kuten massassa ja nopeuksissa", but $7{,}9\,\text{m/s}$ has two figures and $h$ is a trapezoid estimate. Fix: give the reason as the initial speed $46{,}0\,\text{m/s}$ and the mass, or answer $2{,}2\,\text{kN}$ (tolerance 0,03 accepts it).
- L3-04 Vastaus b) — $16{,}33 \to 16\,\text{m}$ is rounded down, which is right for an "enintään" value (P7), but the text does not say so. Fix: add "pyöristetään alaspäin, koska kyse on suurimmasta sallitusta pituudesta".

## Checked
- I recomputed all 19 numeric answers in one script with my own formulas from the task texts. All agree with exercises.json and answers.py to 1e-3: L1-01…L1-05, L1-08, L2-01…L2-07, L2-09, L3-01…L3-05.
- Recomputed side values: L3-04 $v = 7{,}67\,\text{m/s}$; L3-02 deceleration $0{,}857\,\text{m/s}^2$ with stop at $8{,}67\,\text{s}$, matching the ex-hissi figure; L2-07 range $0{,}306\ldots0{,}335$; L3-05 trapezoid $h = 55{,}625\,\text{m}$ and the distance mean ($2{,}21\,\text{kN}$) vs the time mean ($1{,}76\,\text{kN}$), with the right reason given.
- L2-06 data fit uniform deceleration ($v_0 \approx 4{,}0\,\text{m/s}$, stops just after $5\,\text{s}$), so the mid-interval method holds.
- L2-07 uses a pushed box at constant speed, so it measures μ, not μ₀; the reason is stated.
- L2-08: exactly one supported conclusion; the uncertainty-interval reasoning, the "absence of evidence" and the extrapolation feedback are all right.
- L1-06 and L1-07: one correct option each, and each distractor's feedback is right.
- L1-08: the error ($N = mg$ on a slope) is correctly diagnosed, and the factor $1/\cos 30^\circ$ checks out.
- Force diagrams in the solutions: friction up the slope or backward, normal force perpendicular, components dashed, v and a apart from the forces, and equations from the stated axes.
- Every task is inside FY4 (Newton II, energy principle, friction). L2-04's $P = W/t$ is prior knowledge.
- Rounding: L1-04 and L1-05 use two figures from $6{,}0$ / $0{,}15$; the others use three.
