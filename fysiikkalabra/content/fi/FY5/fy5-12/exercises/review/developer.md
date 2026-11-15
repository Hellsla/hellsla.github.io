VERDICT: DONE

Round 1, work queue 19: one new source-based task, nothing else touched.

**New task:** `fy5-12-L2-10` (teacher's label FY5-A2, "Missä kaksi ääniaaltoa vahvistaa toisiaan?"), level 2, kind data + model + reasoning. Answer box: part c), smallest positive path difference of destructive interference, $\Delta s = \lambda/2 = 0{,}40\,\text{m}$ (unit m, tolerance 0.02); constructive $0{,}80\,\text{m}$ is in the solution.

**Files:** `exercises.json` and `solutions.md` in fi, en and fi-easy (task appended to level2, solution appended at the end); `lessons/FY5/fy5-12/answers.py` (three lines before the print).

**Tarkennukset:**
- Link: the Finnish versions use PhET's Finnish page (`/fi/simulations/wave-interference`, text "PhET – Wave Interference (Aaltojen interferenssi)"); English keeps the teacher's link.
- Added to the situation: which screen (the second, Interferenssi), wave type sound, start both sources with the green buttons; runs in the browser. Without it the student cannot find the right view.
- b) got "Selitä muutos aallonpituuden avulla", so the part asks for physics, not only an observation.
- Last paragraph names the answer-box part.

**Notes:**
- Existing `fy5-12-L2-01` has the answer $\lambda = 0{,}80\,\text{m}$ from $\Delta s = 0{,}40\,\text{m}$ (the same pair of numbers, reversed question, different geometry). The teacher's numbers were kept.
- Lint: 0 errors; a length warning (512 words) for the new four-part solution. check_solutions ok. check_i18n: no line about fy5-12 (the one en error is fy5-16's).
- Layout check at 360 px not run (brief: no builds outside the lesson).
