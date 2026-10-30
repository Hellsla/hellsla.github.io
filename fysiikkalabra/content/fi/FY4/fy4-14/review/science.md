VERDICT: PASS
CONTENT-HASH: b7a38f681e4f54f3

## Blocking

## Polish
- lesson.md:183 (figures.py `_phase`), :333 (`_rise`) — the captions say *mittakaavassa*, but the orange acceleration arrows are drawn as offset + k·a, not in proportion to a. In *pudotus* the middle arrow is 2/3 of the first, though F_v = G/2 gives a = g/2. In *ylos* the falling/rising a arrows are 0,68 : 1, though |a| is 5,81 : 13,81 (the ΣF arrows there are right, 0,42). — Draw a ∝ |a|, or limit "mittakaavassa" to the forces, as *varjo* already does.
- inquiry.json:700 (pred-3 feedback) — "noin 3,9 kN, viisinkertaiseksi" is the 80 kg run, but the prompt names no mass. — Add "$80\,\text{kg}$:n hyppääjällä".

## Checked
- All lesson-answers.py numbers recomputed with my own Euler run and closed forms. They match: v_T 47,6/54,9/61,4 m/s, head down 88,6 m/s, canopy 5,11 m/s, F_v,max 3,92 kN = 5,0 G, a_max 39 m/s², hook 198 km/h and 18 km/h, example −18,43 m/s² (F_v = 2,88 G), siirto 303,9 N and its mistakes 367,9/573,2/671,8/735,8, check-2 627,8 N and the 352 mistake.
- Figure *vt*, read from the SVG coordinates: the 60/100 kg plateaus are 47,6/61,5 m/s, the values at 5 s and 10 s match tanh, and the free-fall line has slope g. *pudotus*, *varjo*, *esimerkki* and *ylos* forces are to scale (F_v = ½G, 3G, 2,88G, ΣF = G ± F_v).
- The round-1 B/A fixes hold: the start is at rest relative to the air, "kun ilman tiheys on sama", "samankokoisista ja samanmuotoisista" (lesson, summary, glossary, exit ticket 1), and no *vapaa pudotus* for a fall with air resistance.
- sim.js implements G − kv² = ma, the k ramp, the push/pull point of F_v and the simState keys G, vT, Fv and FvMax. Experiments 1–3 each lock everything except the varied parameter.
- Force diagrams (checklist): weight from the centre, F_v as a push to the lower face or from the top under the canopy, ΣF hollow and apart, v and a off the body. No third-law pairs and no point particles. Each valitse distractor has one error (b direction, c invented F, d missing F_v).
- Predictions, experiment questions and check-1 each have exactly one correct option, and every feedback is right. Check-3's criteria, model figure (F_v > G, a up) and equation are consistent.
- Worked example: solved symbolically first, 3 sf justified, a real check. Scope: F_v is qualitative, and kv² appears only as the sim's model.
