VERDICT: PASS
CONTENT-HASH: 4e78ccdf13e1a945

## Blocking

## Polish
- lesson.md:290 (theta-graph aria-label): it says "n = 1.332", but the text below says $n = 1.3315$. The peak is 42.3° either way. The same note was made on the Finnish version. Optionally write "n = 1.3315".

## Checked
- Translation fidelity: after normalising the decimal separator, every number in lesson.md (text and figure labels), inquiry.json, exit-ticket.json, exercises.json and solutions.md equals the Finnish source, which passed. The figure geometry (all 8 SVGs, labels removed) is identical. The inquiry structure (initial, locked, vary, measure keys, answers, tolerances, mistake values, correct flags, reveal/after, min, optional) is identical.
- Recomputed in one script (scratchpad fy711_recompute.py): crown speeds 198 111 / 196 053 km/s; worked example 34.88° / 34.47° / 0.41°; virhe 39.2° / 34.5°; siirto 25.396 mm (mistakes 11.23 and 3464.1); tarkistus-2 1945.94 km/s.
- koe-1 Δδ = 0.527 / 0.702 / 0.942 / 1.395 / 4.446° (A = 30…70°); 38.44° / 39.83° at 60°. The sim capture at A = 30° shows 19.4° / 19.9° / 0.53°, and my values are 19.41° / 19.94°.
- koe-2: 40.0° at 40°, minimum 38.43° at about 49–50°, 50.25° at 80°. Exactly one option is correct, and every piece of feedback is right.
- Rainbow: 42.30° at α = 59.50° and 40.63° at α = 58.82°. Secondary bow 50.5° / 53.5°; θ(90°) = 14.7° ("about 15°"). Exit ticket: 42 − 50 = −8°.
- The English wording keeps the physics: colour is fixed by frequency; the mechanism of the electron response growing towards UV absorption; the condition that the prism equations hold when the ray can leave; "from the direction the sunlight came from"; the observer figure's aria-label (the violet ray from the upper drop passes above the eye, and the red ray from the lower drop hits the ground).
- The sim's en strings (lang/en.json sims.fy7-11) have the right terms (angle of deviation, refractive indices at 656 / 405 nm, the TIR message). The model box says its readouts are model values.
