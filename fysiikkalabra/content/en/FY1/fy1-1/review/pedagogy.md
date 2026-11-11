VERDICT: PASS
CONTENT-HASH: 09da6a2ea3b09622

## Blocking

(none)

## Polish

1. inquiry.json `menetelmat` (optional) — LOPS goal 1 (physics as an experimental science) and the goal on information-gathering methods are served by the core path only through the theory paragraph and the two predictions. The only activity where the student sees how a size is inferred from measurement plus a model is optional. Remove `optional` (it is short, and its question is a good one) or add one sentence to the reflection linking the sim's "model values" to it.
2. inquiry.json `reflect` — the page's Why question is "why can physics study both a proton and the universe", but the reflection only returns to the 42 and 62 orders of magnitude. Add one prompt: which two things (model and measurement) let us know a size we cannot see.
3. inquiry.json `exp-2` question — the choice (nested structures) can be answered without the table, and the feedback's mention of the table is the only link to it. Ask something that uses the recorded rows, for example "how many orders of magnitude from the Sun to the Milky Way". Likewise `tunnista` can be answered by looking up the neutron star in the text and figure; accept it, but the "about 30 times a second" clue is what does the work.
4. inquiry.json `simulaatio.text` — the visible lead is about 46 words, over the 30-word limit of CLAUDE.md Lesson page 4. Cut it to a single sentence and move the rest into *How to use*.
5. lesson.md Common misconception, last sentence of the first paragraph — "objects of very different sizes cannot all be recognised in the same scale picture if they are drawn in the right proportions" is clumsy. Suggested: "Objects whose sizes differ by many powers of ten cannot be drawn in one picture to scale; that is why scale pictures are always schematic."

## Checked

- Learning path: prerequisites (powers of ten, metres) are enough; the opening question is answered; both slot goals are covered, with the structure-of-matter and interactions content inside the teacher's brief.
- pred-1 and pred-2: a student can argue them before the evidence, each wrong option has its own repairing feedback, and exp-1 and exp-2 can refute them (the sim shows n directly). The values are labelled model values.
- The sim at 390 px (capture #2): readable, with the readout in LaTeX and Käyttöohje, Mallin oletukset and Laskennan selitys behind closed boxes; the controls are usable.
- Variable control: the experiments vary only the object and lock nothing; fine for a zoom, but the table is the sim's own data, not an emergent result.
- Worked example: seven stages, one step each, with the calculator hint; it does not repeat the exercises.
- Mistake feedback for the numeric tasks (ratio instead of difference, sign, added exponents) is realistic and repairing.
- The `vuorovaikutukset` and `virhe` distractors reveal real misconceptions (gravity or electromagnetic in the nucleus; difference taken as ratio).
- Figure object-types (#19): legible at 390 px, the description gives the data without naming the answer, colour is not used alone.
- Workload: about one lesson, since exp-3, siirto, virhe and check-3 are optional; the lesson text is dense but kept in short paragraphs under subheadings.
- Not judged: the exercise set (reviewed apart), and the other figure captures at 28×28 px, which are empty and look like capture artefacts.
