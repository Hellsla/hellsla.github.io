VERDICT: PASS
CONTENT-HASH: 84d549d1956256c7

## Blocking
(none)

## Polish
- inquiry.json:402 — the rubric criterion "Vertasin mallia JPL:n arvoon" asks for something the tarkistus-3 prompt (line 397) does not ask for (guardrail: a criterion asks only what the task asks) — add "Vertaa mallin arvoa JPL:n ilmoittamaan arvoon." to the prompt, or drop the criterion.
- lesson.md:252 — "Jos s₀ ≠ 0, suora on yhtä jyrkkä" does not say what it is compared with — write "yhtä jyrkkä kuin samalla nopeudella origosta alkava suora".
- lesson.md:235 — the section uses $s$ for distance travelled ("kuljettu matka $s$"), but the formula section and the summary use $s$ for position and $\Delta s$ for distance. Under the stated assumption $s_0 = 0$ this is correct, but writing $\Delta s$ (or "paikka $s$ = matka") would match the rest of the text.
- inquiry.json:314 (siirto, Järkevyys) — "6 m/s on noin 22 km/h" only reverses the conversion that was just made. A rough order-of-magnitude comparison (for example a typical cycling speed of 15–30 km/h) would be a real check.

## Checked
- Worked example recomputed: 2922 days, v = 1 325 462 km/vrk = 0,0088602 AU/vrk, s = 145,59 AU ≈ 145,6 AU ≈ 2,18·10¹⁰ km. The 15.2.2026 model value is 143,26 ≈ 143,3 AU against JPL's 143,05 AU, a difference of 0,15 %. The yearly check (3,2 AU/a, ≈ 26 AU) is right. The opening question's "yli 20 miljardin km" (≈ 2,18·10¹⁰ km) holds.
- The gravity-slowing claim is correct and suitably hedged ("osin"). The value is labelled as a model value everywhere (example, tarkistus-3, hook).
- Graph figure measured from the SVG: 9,6 px/m and 68,8 px/s. Both lines have v = 3 m/s, the upper starts at s₀ = 5 m, and the slope triangle 2 s → 4 s gives Δs = 6 m, matching the aria label. Motion figure spacings are equal (115 px). Hero markers are equally spaced.
- Ennuste 1 and 2, koe-1, koe-2, johtopäätös: 6 + 2·4 = 14 m, s/t = 5,0 and 3,5, Δs/t = 2,0 m/s. Exactly one option is correct in each, and every distractor's feedback is correct.
- Experiments: s₀ and v are locked, only t varies (step 0,5 s, 0–10 s). simState provides s and ds. All values stay inside the 0–60 m track.
- sim.js implements s = s₀ + vt. The slope readout uses (pos(6) − pos(2)) / 4,0 s = v and matches the calc box. The model box states its limits.
- Etsi virhe: 23 m vs 33 m. Siirto: 21,6 km/h = 6,0 m/s gives 390 m; the mistake values 1092 and 270 are correct. Tarkistus-2: v = 3,0 m/s, s₀ = 4,0 m; mistakes 7 and 3 are correct.
- Check-c2 (horizontal line = rest) and tarkistus-1 (Δs ∝ t when s₀ ≠ 0): exactly one correct option in each, and the feedback is right.
- Exit ticket: 90 km/h · 1/3 h = 30 km.
- Scope stays inside FY1: linear model and direct proportionality; no vectors or forces beyond a qualitative mention of gravity. The "positive speed, one direction" condition is stated.
