VERDICT: FAIL
CONTENT-HASH: 2c00c7827a1d53fa

## Blocking
- exercises/exercises.json:146 (fy5-11-L2-05, kind experiment) — B: the times are hand-stopped ("mittaa kellolla", stop after the echo) yet given to 1 ms and lie on a line within 0,3 ms; a hand-stopped clock scatters by about 0,1–0,2 s (guardrails, "a stopwatch shows 0,01 s, but hand timing is uncertain by about 0,2 s"), more than the whole 0,117 s echo delay at 20 m. The task teaches a method that cannot give these data. — Keep the numbers and the difference method but change the timing: the clap and the echo are recorded with a phone (or a sound-card app) whose recording starts with an unknown but constant delay, and the delays are read from the waveform. Adjust solutions.md:106 ("reaktioaika" → the constant offset) to match.

## Polish
- exercises.json:183 (L2-06) — the plan asks for ripple-tank pictures (figure); a table of verbal descriptions is given instead. Add a c) asking the rule (taipuminen vs. b/λ).
- exercises.json:261 / solutions.md:175 (L3-04) — c) could add the real reason extra soundings are needed on a steep slope: the first echo comes from the nearest bottom point, not from straight below, so the vertical model underestimates the depth there.
- exercises.json:104 (L1-08) and L3-04 — echo sounding also in fy5-17-L1-03; inverse question, not a duplicate.
- Solution "Kaava"/"Sijoitus" lines with long inline formulas show as empty boxes in the 1280 px captures, in old tasks (L2-01) and new (L3-04) alike: site-wide inline-formula change, handled by the other thread.

## Checked
- All answers recomputed in one script (L1-08 48 ms, L2-05 342,9 m/s with residuals ≤ 0,3 ms and t_r = 0,040 s, L2-06 b/λ = 0,5…8,0, L2-07 32°, L3-04 depths 40,0–71,8 m and slopes 12,5/22,1/35,1/14,5/23,9°, L3-05 200, AM 1,8, tv 1200, light 1,1·10⁹): all agree with answers.py and solutions.
- L1-06: exactly one correct option; every distractor's feedback right (fixed end inverts, no loss, speed unchanged).
- L3-04 sig figs (19 ms → 2 sf); stated assumptions match the solution.
- L3-05 inside the teacher-approved plan (radio vs. light); assumption (only edge diffraction) stated; no contradiction with c).
- Notation (α, β, λ, b, v = fλ) as in the lesson; scope within reflection/diffraction; no refraction task added.
- No duplicate of an existing fy5-11 task or of fy5-10/fy5-12 tasks; levels fit (L2-07 is light for level 2 but acceptable as error analysis).
