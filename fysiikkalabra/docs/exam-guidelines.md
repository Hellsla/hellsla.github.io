# Esimerkkikokeen laatimisohje (exam guidelines)

The one brief for writing a course's Esimerkkikoe (example exam), teacher 2026-11-05. It holds general principles of
good Finnish upper-secondary physics course exams. It holds no questions, paraphrases, data or figures of any real exam,
and the pipeline never needs a reference exam: an exam is written from the course content (curriculum.json, the
chapters), LOPS2019 goals, this file and the house rules (CLAUDE.md, NOTES.md).

Files: `content/fi/<COURSE>/koe/{tasks.json,solutions.md,review/}`, `lessons/<COURSE>/koe/{answers.py,figures.py}`,
page `site/<COURSE>-koe.html` (scripts/practice.py, the Sovella itsenäisesti format plus `sections`, `max_points` and
parts of kind `choice`). Command: `/exam <COURSE>`.

## Confidentiality (overrides everything below)

- A teacher's own exams are private input. They never enter the repository, a commit, a PR, a log, a packet, a review,
  project memory or an agent prompt, not even as an extract or a paraphrase. Read them, if at all, outside the
  repository, and delete local copies afterwards.
- Every task is written from scratch: no copied, paraphrased or renumbered questions, no reused distinctive situation,
  dataset, diagram or sequence of sub-questions. Standard physics (laws, methods) naturally overlaps; the tasks do not.
- Before each commit: list the staged files, check no reference file or extract is among them, read the staged diff,
  and compare the new tasks against the references by situation and structure (not only by words). An automated
  similarity check is a help, never a guarantee.

## Structure (default; adapt with a reason)

| Osa | What | Rule | Max |
|---|---|---|---|
| 1 | Perusosaaminen: 10 multiple-choice items of 2 p | answer all | 20 p |
| 2 | Perustehtävät: four tasks of 15 p | answer two | 30 p |
| 3 | Soveltavat tehtävät: two tasks of 20 p | answer one | 20 p |

Maximum 70 p; the page shows the offered points (20 + 60 + 40 = 120 p) apart from the maximum. A course may use a
10 p Osa 1 (five items, maximum 60 p) when its content is mostly quantitative, as FY4. FY1 and FY2 keep the 20 p Osa 1:
the introductory courses test more foundations by compulsory items. Each course is one exam of about
120 minutes (`minutes`); a school may combine two short courses into one sitting.

## Osa 1: understanding, not recall

- Ten items over the whole course, roughly in chapter order, one or two per chapter. Four options (three to five
  allowed), one correct, no penalty for a wrong answer.
- Use the item types that reveal understanding (development ideas, teacher 2026-11-05): choose the graph that matches
  a situation; order of magnitude; predict a change (grows, shrinks, stays); unit and dimension; a true statement
  about a graph or data; the conclusion the data support with its uncertainty $\Delta x$; ranking; the correct energy
  or force picture with typical misconceptions as distractors.
- At most one or two items that only ask a definition; even then the options test the meaning, not the wording.
- Distractors are real student errors (wrong prefix step, too many digits, confusing power and energy), never jokes.
- Each item's solution is one `**Perustelu:**` step that says why the right option is right and why the most
  tempting wrong one is wrong.

## Osa 2: standard problems (15 p)

- Two to four parts. Typical shapes: data table → draw the graph → read or fit → interpret; a situation → compute →
  judge the result; a phenomenon → explain with the course's concepts, then a short calculation.
- Across the four tasks: at least one graph from data, one explanation part, one task with measurement uncertainty or
  reliability, and the course's main quantitative model. A student who chooses any two still meets the course's core.
- Typical points: drawing a graph 4–5 p, a calculation part 3–6 p, an explanation 3–5 p.

## Osa 3: extended applications (20 p)

- An authentic situation with source material (a short text, a table, a graph): four or five parts that connect several
  chapters, need a model the task does not name, and end with evaluation (is the model valid, what limits the
  precision, which choice is better and why).
- Difficulty comes from choosing and connecting, never from long arithmetic or tricky wording. The first part is
  accessible, so every student can start.
- The two tasks differ in kind (for example one experimental and data-driven, one a societal or technological judgment
  with numbers).

## Language and statements

- Short, natural Finnish; the situation first, then the parts. No bold in statements (teacher's rule). Every symbol,
  number and unit in LaTeX, decimal comma, `\cdot` for multiplication.
- Do not name the formula or the method in a demanding part. Give the data the solution needs (a constant the
  student cannot know is given; one that belongs to the course's data booklet may be left to the booklet, say so).
- Invented situations and data are marked `source: example`; real data name their source and year.

## Model solutions and marking

- Every part has the complete solution of CLAUDE.md "Lesson form" 7 (calc: Annettu · Kysytty · Periaate · Kaava ·
  Muunnokset · Sijoitus · Vastaus · Järkevyys; word: Kysytty · Periaate · Mallivastaus; graph: Kysytty · Kuvaaja ·
  Mallivastaus), then Yleisiä virheitä and, when there is one, Hyväksytään myös.
- Every number of a solution is recomputed by `answers.py` from the task data; `practice.py check` compares it.
- Rubric criteria (at most 4 p each) sum to the part's points and award reasoning, method, the result with unit and
  precision, and interpretation. A propagated error loses points once; a rounding difference of the last digit loses
  none; an equation that is irrelevant earns nothing. Alternative valid methods earn the same points.

## Checks before review

`python scripts/practice.py check <COURSE>/koe` (structure, selection rules, maximum, rubric sums, solutions, numbers),
`python scripts/build.py <COURSE>-koe`, `python scripts/check_layout.py <COURSE>-koe --width 360` (768, 1280), then the
science and pedagogy reviewers from `practice.py packet <COURSE>/koe --role …` and the visual reviewer.
