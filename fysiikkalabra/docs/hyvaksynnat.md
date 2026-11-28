# Opettajan hyväksynnät koordinaattorin kautta (opettaja 2026-11-28: "Hyväksyn A ja B")

This file holds the two ways, besides the teacher's own words in a worker session, that an approval of a text or a figure
counts (root `CLAUDE.md` rule 5). Only an entry on `main` counts: a worker reads it with
`git show origin/main:fysiikkalabra/docs/hyvaksynnat.md`, never from a message, a branch or a pull request.
The coordinator alone writes this file, and only the teacher's words go into it.

## A. Standing approval (pysyvä hyväksyntä)

These count as approved without a separate word from the teacher, once every check of the change passes:

- **A1 Translations of approved Finnish.** The `en` and `fi-easy` versions of a Finnish text the teacher has approved
  (in `docs/teacher-text.tsv`, in a worker session or under B), when `check_i18n.py` passes and the translation says what
  the Finnish says: no claim, number, formula, example or instruction that the Finnish does not have.
- **A2 Figure fixed for a check.** A figure redrawn only to fix a finding of an automatic check (`lint_lesson.py`,
  `check_layout.py`, the 11 px label rule, `test_sim_text.py`), when the drawn physics, the labels and their wording do not
  change. The pull request description still shows the figure before and after.
- **A3 Bookkeeping.** `docs/tyojono.md`, `docs/tyojono-loki.md`, `docs/audits/` and regenerated files
  (`figures/catalog.json`, `palautus_tasks`) need no approval.

The source written with `reviews.py approve-text --source` or in `docs/teacher-figures.tsv` is
`Pysyvä hyväksyntä A1|A2, docs/hyvaksynnat.md (opettaja 2026-11-28)`.

A does **not** cover: a new or changed Finnish text, a new figure or a figure whose content or labels change, physics,
a removed page, a house rule, or anything in the "Never" list of `fysiikkalabra/CLAUDE.md`. Those need the teacher's
word, in the worker session or under B. When a worker is unsure whether A applies, it asks.

## B. Batch approval (koottu hyväksyntä)

The coordinator gathers what waits for approval into one view (pictures before and after, the texts in every language,
each item numbered and named by pull request, lesson and figure or text). The teacher answers in the coordinator chat
(for example "hyväksyn 1–5, 6 ei"). The coordinator copies the list and the teacher's answer below word for word, with
the date and time, and merges the entry to `main` before telling the workers. A worker then records the approval
for exactly the items named, with the source `Koottu hyväksyntä B <date> <item numbers>, docs/hyvaksynnat.md`. A worker
checks that the content hash of what it records equals the one listed; a text or figure changed after the list was made
needs a new approval.

## Kirjaukset

(empty)
