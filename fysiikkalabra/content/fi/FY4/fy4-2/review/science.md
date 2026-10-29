VERDICT: FAIL
CONTENT-HASH: b20a577adb43a192

## Blocking
- lesson.md:547 (also the heading :546, Tiivistelmä :644) — **B**: "siirtymä on kuvaajan ja aika-akselin väliin jäävä pinta-ala" is stated generally, but it holds only if the area below the time axis (v < 0) counts as negative. This lesson itself investigates a reversal (Koe 2, Ennuste 2: v goes from +6 to −6 m/s), and the sim's Laskennan selitys says the negative part counts negatively, so the theory and the summary leave a wrong picture there and contradict the sim box. — Fix: add one clause at :547 and :644, e.g. "aika-akselin alapuolinen pinta-ala (v < 0) lasketaan negatiivisena", and keep "alle jäävä" only where v > 0.

## Polish
- lesson.md:540 — "nopeus kasvaa joka sekunti määrän $a$" right after the lesson stresses negative a — write "muuttuu".
- sim.js road(): the velocity arrow is capped at 110 px (|v| > 18 m/s, reachable with v0 = 6, a = 3), yet Käyttöohje says the arrow's length shows the magnitude — scale the arrow to the run's max |v|, or say it is capped.
- sim.js graphV(): the area under v = 0 is shaded in the same colour as the area above it, though the calc box says it counts negatively — use a second tint for v < 0.
- Experiment panel (shared template, seen in exp-2 shots): "Alkutila: v_0 = 6 m/s, a = -2 m/s²" is plain text, not LaTeX, and has no decimal comma — this breaks the teacher's "all symbols LaTeX" rule. Fix it in the shared component.
- lesson.md tv-graph figure: the label "a > 0" is in the velocity blue. Acceleration is orange everywhere else, so colour the label neutral or orange.

## Checked
- Teacher rules: no × or \times anywhere; vectors use \overline{v}, \overline{a} (lesson :365, figures, sim); velocity is blue #1971c2 and acceleration orange #e8590c in the strobe figure, the hero, the sim and Käyttöohje; there are no forces in this chapter.
- Strobe figure: cart gaps are 1:3:5 (accelerating) and 5:3:1 (braking to rest), velocity arrows step evenly, the acceleration arrow is constant and reversed when braking. Hero stone gaps are 1:2,98:4,98:6,96.
- Tangent figure: the dashed line really is tangent at P (slope 0,766 vs 0,766). ex-tangent, ex-tv, check-tv and fall-points match their data.
- Worked example: √76 = 8,72, t = 9,44 s, v = 8,72 m/s, rejected root −25,4 s, average-velocity check gives 60 m.
- Free-fall fit recomputed (numpy): A = 4,884, B = 0,126, C = 0,0013, g = 9,77 m/s²; the mistake 2s/t² = 10,4 m/s².
- Hook (1,23 m; 4,9 m), retrieval 3,0 m/s, exp-1 (1,4,9 m; 5,0 m), exp-2 (v = 2, 0, −2 m/s; x(3) = 9,0 m; back at the origin at 6 s), transfer 1,875 m/s² and 40 s, check-2 32 m, check-3 4,9 m and 14,7 m: all correct.
- Predictions, Etsi virhe and checks: exactly one correct option each, and every distractor's feedback is right.
- Sim: implements v = v0 + at and x = v0t + ½at², the tangent slope is v, simState gives x and v, the experiment initial values are inside the slider ranges, and v0 and a are locked.
- Conditions are stated: small air resistance, constant a, x0 = 0 in the model box, "yleensä" in the fit sentence.
- Exit ticket matches the theory: speed falls when v and a point in opposite directions, mass does not matter in free fall, tangent method.
