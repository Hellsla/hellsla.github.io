VERDICT: FAIL
CONTENT-HASH: ade0d0acde13088d

## Blocking
- assets/sims/fy8/fy8-5/sim.js:195 and :265 — the simulation canvas shows Finnish text on the English page: "1s-orbitaali" (state title, also in the 1280 px lab capture) and "osumia" (histogram y-axis label, "hits"). — route both through the translation function ("1s orbital", "hits"), as the control labels already are.
- inquiry.json:285 (`siirto`, unit "kpl") — the answer unit is Finnish words (scripts/check_i18n.py WORD_UNIT flags it); an English student sees "kpl" next to the field. — use "hits" (or no unit).

## Polish
- inquiry.json `hook` — the caption "speaks of a region where the electron is likely to be detected" already gives the core of the answer to the opening question before the student commits. — end the caption at "drawn as blue clouds and two-lobed shapes".
- Exercises have no task on standing waves or nodes (a stated learn goal and a Tarkista item); all eleven tasks are numeric. — add one level 3 reasoning task (count nodes, compare the energy of two states).
- Theory states "the more nodes, the greater the energy" for hydrogen, yet 2s and 2p both have one node and equal energy; the sentence is correct but add "(counting all nodes together)" to avoid a reader inferring that radial nodes alone matter.

## Checked
- Path: Bohr model and double-slit prerequisites, then orbital as a probability region; the opening question is answered in the reflect item and the conclusion.
- Both predictions can be refuted by the simulation (10 vs 1000 measurements; histogram peak at 0.05 nm, not at zero).
- Experiments lock the right parameters and vary one; min 2 rows before reveal; model values are called model values.
- Workload fits one lesson (two predictions, two experiments, optional extras).
- Worked example: seven stages, one step each, units converted by substitution, reasonableness included.
- Figures (string, nodes, cloud, levels) are legible at 390 px, uncluttered, colour never alone; alt text carries the data without the answer.
- Tarkista distractors are real misconceptions (orbit, wall, spread-out electron, nodes); explain criteria are observable.
- Simulation readable at 390 and 1280 px; the wide layout puts experiments beside the sim.
- English text reads naturally; glossary terms (orbital, probability interpretation, wave-mechanical model) used consistently.
