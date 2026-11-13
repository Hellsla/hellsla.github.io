VERDICT: PASS
CONTENT-HASH: d7633bb66bf5dcc9

## Blocking
(none)

## Polish
- inquiry.json `gammaspektri` text and question: the text already says the nucleus emits both photons one after the other, and the prompt repeats the cascade. The student only adds two read values and does not have to reason out why the sum is the level energy. Fix: drop "one after the other" from the text and let hint 2 introduce the cascade.
- inquiry.json `pohdi` (optional): the opening question about why gamma radiation accompanies alpha decay is answered only here and in the theory. If a student skips this box, the hook's second half is never worked on. Fix: remove `optional`, or add a one-line gamma follow-up to the conclusion's criteria.
- inquiry.json `ennuste-1`: the prompt already says an alpha particle has two protons and two neutrons, so the prediction is close to deduction rather than something the data can surprise. This is fine for a first-contact lesson, but "argue why" in the justify field would give the reasoning more weight.
- The two cloud-chamber photos in lesson.md carry no task (for example "which is alpha?"). They are good illustrations, but they could ask the student to act on them in the sim's "More to investigate" tasks.
- The experiment table's "decays next by" column shows alpha / beta minus. A reader with no vision gets Z, N and A only by recording. This is acceptable, since the readout text carries the same values.

## Checked
- Learning path: prerequisites (photon energy, level differences) are retrieved in the optional `kertaus`. The new content (Z, N, A, three decays, gamma levels) matches the slot's two goals and nothing more.
- Predictions commit before the evidence; every wrong option's feedback repairs a named misconception (electron in the nucleus, charge sign, mass number). Both predictions can be refuted by steps 0–5 of koe-1 (min 6 records, covering both alpha and beta rows).
- The simulation (1280 px capture) is a data-driven series chart. Its readout is clean, its text sits behind Käyttöohje / Mallin oletukset / Laskennan selitys, and the speed control is present. The data are labelled as NNDC model values.
- The gamma-spectrum figure (390 px) is legible, shows the needed peak values, and the cobalt-60 level scheme is not shown before the task.
- The worked example has seven stages, and the unit conversion is shown by substitution. It reuses no task text.
- The three checks cover concept (a Ba* gamma emission), calculation (technetium wavelength) and explanation with observable criteria. The siirto task (U-235, 7 alpha decays) has three progressive hints and real mistake feedback.
- The exit ticket tests the two core ideas (decay equation, nucleon count).
- Workload is about one lesson, and the optional items are marked.
- English is clear; no glossary conflicts. Page form is fine.
