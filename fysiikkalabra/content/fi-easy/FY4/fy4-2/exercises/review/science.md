VERDICT: PASS
CONTENT-HASH: dbea317b70913c2e
## Blocking

## Polish
- content/fi-easy/FY4/fy4-2/exercises/solutions.md:198-200 (L2-08 Periaate) — the new paragraph opens "Se on kolmio ...", whose referent (the area) is in the previous paragraph — start it "Ala on kolmio ..." or keep the two together.
- content/fi-easy/FY4/fy4-2/exercises/solutions.md:77 (vertical throw Kaava) — uses $y$, $y_0$ while the brief's lesson writes $x = x_0 + v_0t + \tfrac{1}{2}at^2$; acceptable for a vertical axis, but one sentence "pystysuora paikka $y$" would tie it to the lesson's equation.
- content/fi-easy/FY4/fy4-2/exercises/solutions.md:79 (vertical throw Sijoitus) — $t \approx 1{,}529\,\text{s}$ is no longer needed for $h$; it is still used in Järkevyys, so it can stay, but saying "nousuaikaa tarvitaan tarkistukseen" would explain why it is computed.

## Checked
- Delta only: seven Kaava rewrites and two paragraph splits; no number, answer, tolerance, task or id changed.
- Vertical throw: from $v = v_0 - gt$ and $y = y_0 + v_0t - \tfrac{1}{2}gt^2$, $v = 0$ gives $t = v_0/g$ and $h = v_0^2/g - v_0^2/(2g) = v_0^2/(2g)$: algebra right; $225/19{,}62 = 11{,}47\,\text{m}$ recomputed, answer $11{,}5\,\text{m}$ unchanged; substitution now goes into the last symbolic form.
- Train: area of triangle + rectangle + triangle, $s = 1162{,}5\,\text{m}$ recomputed.
- Polynomial fit: $v_0 = B$, $a = 2A$ from comparison with $y = y_0 + v_0t + \tfrac{1}{2}at^2$; $v = -1{,}76\,\text{m/s}$ recomputed.
- Scooter: rectangle $v_1t$ + triangle $\tfrac{1}{2}(v_2 - v_1)t$ = mean velocity times time; $22{,}5\,\text{m}$ recomputed.
- $(t^2, x)$ linearisation: $x = \tfrac{1}{2}at^2 = kt^2$, $a = 2k \approx 1{,}15\,\text{m/s}^2$ recomputed; condition "levosta" stated.
- L3-04: interval area $v_1\Delta t + \tfrac{1}{2}(v_2 - v_1)\Delta t = \tfrac{1}{2}(v_1 + v_2)\Delta t$, with the linear-within-interval assumption stated in Periaate; sum $128{,}3\,\text{m}$ recomputed.
- Video vs light gates paragraph split changes no claim.
- Captures opened: none (judged from the text and the packet).
