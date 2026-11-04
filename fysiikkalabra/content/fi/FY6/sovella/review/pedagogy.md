VERDICT: FAIL
CONTENT-HASH: 6f3465d0e19501e5

## Blocking

1. fy6-s1 d, conclusion criterion (1 p): it requires "systemaattinen virhe on todennäköisesti hajontaa suurempi, joten R_s on pikemmin yläraja". The task gives no size for the drift (only "laski hitaasti"), and the data (residuals alternate in sign, max 0,02 V) show no drift. The student cannot reach this from the data, and the criterion "conclusion perustuu aineistoon" is violated. Fix: give a drift figure (e.g. U fell about 0,03 V in a minute at constant current) so the systematic effect can be compared with 0,08 Ω, or soften the criterion to "perustelee, kumpi virhe todennäköisesti hallitsee, ja sanoo mihin tieto perustuu". Also note that drift is confounded with the slope because I was raised monotonically; the model answer should say this.
2. fy6-s2 d, assumptions criterion (1 p of 4): the question never asks for an assumption, and the task text already says "Oleta lamppujen resistanssit vakioiksi". The point is awarded for restating the given. Fix: add to the question ("Mikä oletus laskussa on, ja miten se vaikuttaa tulokseen?") or give the point to the effect only (hot filament has higher R than cold; 4,3 A is then an upper-side estimate if the lamps are at full temperature, etc.).

## Polish

- s1 b: Rs tolerance 0,08 but "Hyväksytään" range -1,1…-1,3 V/A is 8,3 % off; align them.
- s2 d: a 3,15 A fuse at 4,3 A (about 1,4 times rated) may take long to blow. The sentence "katkaisee ennen kaapelin vaarallista lämpenemistä" is stated as certain; add "riittävän nopeasti" or a caveat.
- s4 d: the discharge instruction (resistor, insulated tools) is in a model answer. Add one line "älä yritä itse" so it does not read as a how-to.
- Coverage: no task on diode/LED/solar cell (fy6-14) or battery charging (fy6-9); graph competency only in s1. Acceptable for four tasks, but say so in the intro or consider swapping part of s4.
- Point totals are uneven (15, 15, 16, 14); fine but check the exam scale.
- s3 c: first criterion bundles drag and terminal-velocity reasoning in one point; consider splitting.

## Checked

- Scope: capacitor only qualitative discharge, no exponential, no capacitor connections; circuits and vector notation follow scope notes. Link targets fy6-2/4/5/6/8/10-13/15 exist.
- Each part's criteria points sum to the part points (all 16 parts).
- Shared keys used correctly and tags (transfer/concept/math/experiment) match their competencies; every part has a rubric that a grader could apply.
- Numbers match answers.py (practice.py check OK); s1 residual max 0,02 V matches the task text.
- Tasks are unfamiliar contexts and mostly do not name the formula (s3 b, s4 b, s2 c are good transfer). Parts are ordered a to d from calculation to explanation; criteria and model answers are consistent.
- Figures: s1/s2/s3 task figures show no results; the model graph is in the solution only.
- Note: .claude/agents/pedagogy-reviewer.md was not found at that path; I judged from the packet only.
