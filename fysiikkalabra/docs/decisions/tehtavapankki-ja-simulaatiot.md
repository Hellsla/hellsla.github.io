# Exercise levels, exercise bank, lesson folder, simulations (from CLAUDE.md)

Siirretty `fysiikkalabra/CLAUDE.md`:stä sellaisenaan (työjono 0b, 2026-11-17). Kaikki tämän tiedoston säännöt ovat voimassa; CLAUDE.md:ssä on niiden lyhyt muoto ja viite tähän tiedostoon. Sisältö on englanniksi kuten alkuperäinen.

## Exercise levels
Level 1 (perustehtävät): one formula or one step of reasoning, values given. Level 2 (soveltavat): two steps, a conversion, a rearrangement, or measured data to work with. Level 3 (haastavat): reasoning, two ideas, modelling, data interpretation or an unfamiliar context, in the spirit of the YO exam's problem solving. None repeats the worked example. The counts are minimums (`curriculum.json` `exercise_levels`, default 5/4/3, and `exercise_total`): **the exercise bank** (teacher 2026-11-04) gives every FY1–FY8 chapter at least 20 exercises, about 8 + 7 + 5 (the topic may shift it), more where extra tasks are pedagogically justified; a module's `exercise_total` is set to 20 when all its chapters have them. Existing exercises, their ids and solutions are kept: new ones are added beside them with the next free ids. Beside the calculations, which stay plentiful, the bank mixes conceptual multiple choice (`"choices"`), justified qualitative answers, experimental design, error analysis and graph reading, and 2–3 **aineistotehtävää** in most chapters, mostly among the level-2 tasks (a table of measurements, `"data"`, or a graph by its figure id: read, fit, judge the model or the uncertainty). `"kind"` names what a task practises (`courses.EXERCISE_KINDS`); `python scripts/exercise_bank.py <COURSE>` reports each chapter's counts and mix; the plan per chapter is `docs/exercise-bank/`.

## Lesson folder and assets
`content/fi/<course>/<id>/`, what a reader reads (another language has the same files under `content/<lang>/`):
```
meta.json          id, course, title, goals, prerequisites, glossary, sim (true | "<sim folder>" | false), solutions (all; first and none are not used since 2026-10-27)
lesson.md          Ydinajatus, Kaava, Esimerkki (staged), misconception, summary; inline SVG figures
inquiry.json       the inquiry sequence: contribution, prior, activities by stage (format in docs/inquiry.md)
exit-ticket.json   1–3 quick questions the checks do not ask
review/            science.md, pedagogy.md, visual.md (legacy.md on a prototype; audit.md, audit-<role>.md from /quality-audit), carry.tsv, developer.md, checks.txt, usage.tsv; packets and shots git-ignored
exercises/         the exercise set, reviewed apart from the lesson (teacher 2026-10-28, README "Exercises"):
  exercises.json   three levels (schema in README)         solutions.md    one complete solution per exercise (CLAUDE.md Lesson form 7, NOTES §3)
  review/          its own science.md, pedagogy.md, visual.md, carry.tsv, developer.md
```
`lessons/<course>/<id>/`, the same for every language:
```
answers.py         computes every exercise answer (part of the exercise set)    figures.py      the lesson's figures (scripts/figures.py writes them into lesson.md)
lesson-answers.py  the numbers of lesson.md and inquiry.json, when there are any (part of the lesson)
sim-spec.md        the simulation's one-paragraph spec: what the student can find out with it
sim.js             FY3 only: the lesson's simulation (its visible texts are in lang/fi.json "sims", called with __('key'))
```
Simulations live in `assets/sims/<course>/<name>/` (sim.js exposing `window.simState` and `defineSimAdapter()`, its sim.css and images; FY3's stay as `sim.js` in `lessons/FY3/<id>/`; every text a simulation shows is in `lang/fi.json` under `sims.<name>`, never a literal in sim.js), pictures in `assets/pics/<course>/` referred to as `pics/<course>/<file>`; `assets/shared/` only for what several courses use (`assets/README.md`). A simulation with no motion of its own (its picture follows only its controls, the pointer and its own events) is listed in `STATIC` in `templates/sim-embed.js` and drawn on demand instead of 60 times a second (2026-11-05, performance); `test_sims.py` fails a listed sim that changes on its own or draws differently from the continuous loop (`?simloop=1`). A new static sim is added there, never by a flag in its sim.js (that would stale its reviews).

