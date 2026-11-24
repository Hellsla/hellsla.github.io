VERDICT: PASS
CONTENT-HASH: 47096b4080381fb6

## Blocking

## Polish
- inquiry.json:276 (exp-3 intro) and the exp-3 choice feedbacks: "etumatka $x_\text{B} - x_\text{A}$" is negative at the start of case 5 (runner B 5 m behind), while the lesson defines etumatka as the distance the leading body is ahead (positive). Here it is the signed difference, so "paikkojen ero $x_\text{B} - x_\text{A}$" would match the theory and the sim's calc box ("kun kappaleet liikkuvat positiiviseen suuntaan, se on B:n etumatka").
- lesson.md "Kolmas virhe …": "Kohtaamisen näkee vain $(t,x)$-kuvaajasta" is fine as "näkee suoraan"; the same lesson finds the passing moment from equal areas in the $(t,v)$ graph, so "suoraan" would avoid a seeming contradiction.

## Checked
- One script recomputed every number with my own constant-acceleration model: figure tilanne/kohtaus (12 s, 36 m), kaava/vt (t = 0 and 6,0 s, 2v = 12 m/s, both areas 9 m), worked example (roots −2,0 s and 8,0 s, 64 m, 16 m/s, greatest gap 25 m at 3,0 s), cases 1, 4 and 5 (10 s / 50 m; −10 s; 1,55 s and 6,45 s with a = 1,0 m/s²), pr-paikka (25/50/10 m), siirto (8,0 s, 24 m/s, 96 m), check-2 (6,0 s; mistakes 15, 30, 10 s); all agree with lesson-answers.py and the texts.
- Figure polylines measured against their axes: kohtaus, kaava (x = t²), vt (shaded triangles 0–3 s and 3–6 s), esimerkki (16 + 6t vs t², meeting at 8 s, 64 m), ei-kohtaa capture (3t vs 20 + 5t): all to scale.
- Worked example: seven stages, symbolic quadratic solution before substitution, negative root rejected with its reason, check by the other position function.
- sim.js: x = x0 + v0 t + ½at², v = v0 + at, meetings from the quadratic restricted to 0 < t ≤ 12 s; CASES match the texts; model box states point bodies, constant acceleration, no friction or drag, model values.
- Sim in Playwright (fi-easy preview): case 3 at t = 3, 8 s gives gap 25 m, then x_A = x_B = 64 m, v_A = 16 m/s, meetings 1; case 5 meetings 1 at 2 s, 2 at 7 s; case 1 at 10 s x = 50 m, gap 0; case 4 never meets. Experiments lock `tapaus`, vary `t` (0,5 s steps reach every suggested time); measured keys xA, xB, vA, gap, meetings exist in simState.
- Predictions 1–3, exp-3 question, ei-kohtaa, virhe, check-1: exactly one correct option each; every distractor's feedback states the right physics and numbers.
- Explain model answers (johtopaatos, check-3) and exit ticket agree with the theory (max gap at equal speeds, passer faster, negative root before start).
- Guardrail "higher line": the text uses the required wording and restricts "edellä" to motion in the positive direction.
- Scope: uniform and uniformly accelerated rectilinear motion, FY4 central content; no later-course physics.
- Hash 47096b4080381fb6 (--lang fi-easy) at start and end.
