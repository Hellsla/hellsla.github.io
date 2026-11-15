VERDICT: PASS
CONTENT-HASH: 2606efea8263d215

## Blocking
- none

## Polish
- lessons/FY3/fy3-2/sim-spec.md — "työ muuttuu lämmöksi" (work turns into heat) breaks the heat guardrail; the student-facing sim `model` text correctly says internal energy. Spec only, no student sees it — reword when the spec is next touched.
- lesson.md crane photo caption — "the load's potential energy increases": E_p is FY4 per the scope note; the theory says "the energy of the lifted object" — consider the same words (C, not an error).
- sim.js readout — decimal comma (120,0 W, 10,0 m) on the English page; language/visual, not physics.

## Checked
- Full review (figure change, proofreading round 1): hash equal at start and end.
- Definitions: work (force with a component along the displacement, W = Fs for a constant force in the direction of motion), joule, power P = W/t = Fv with its condition (steady speed, force along motion), heat vs work in Joule's paragraph — all correct and inside FY3 scope (no cos α, no E_k/E_p theory).
- Causality: carrying sideways → supporting force ⟂ displacement → zero work, muscles still use energy; Cem's feedback correctly ties the vertical force to steady speed with air resistance ignored.
- Recomputed in one script: pr-paino 98 N; pred-1 600/1200 J; pred-2 120/30 W; pred-3 1.96 kJ; Joule table ΔU/W ≈ 0.99; worked example 4.0 J; siirto 240 W and mistakes 9.6, 0.24; check-1 ratio 3; check-c2 98 J and distractors 590/490 J; check-2 180 J and mistakes 240/120; exit 20 J. All agree.
- Joule 1850 value 4.16 J per g·°C and present 4.19 J — correct.
- Worked example: symbolic W = ½F_max s before substitution, conversion, 2 s.f., average-force check real.
- Figures: spring-work "to scale" verified (75.6 px per 0.05 m, 42.75 px per 10 N, apex at (0.20 m, 40 N)); lift-work F and G arrows equal (58 px), "not to scale" stated; work-graphs areas labelled correctly.
- Simulation: W = Fs, P = W/t, Wdone = W·u; speed control changes pace only; model box states constant speed, friction = pull, values are model outputs not measurements; simState carries F, s, t, W, P.
- Experiments: exp-1 locks F, t and varies s (W measured); exp-2 locks F, s and varies t (W, P) — each isolates its parameter; slider ranges reach the suggested values.
- Assessment: exactly one correct option in every choice item; every distractor's feedback names the actual misconception.
