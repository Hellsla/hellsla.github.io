VERDICT: PASS
CONTENT-HASH: 95f447a9c89c7a99

> Carried over from the lesson's review (content/fi/FY3/fy3-8/review/pedagogy.md) when the exercises got a folder and reviews
> of their own (2026-10-28). That review passed the whole lesson, these exercises, solutions and answers.py included,
> at the CONTENT-HASH above; `reviews.py carry --exercises` recorded that the PASS holds for the moved files. The report
> below is the original, word for word: findings about the lesson text are not about this exercise set.

## Blocking
(none)

## Polish
1. inquiry.json:4 (learn, 2nd goal) — "Tutkit kokeilla, mistä sauvan pituuden muutos riippuu." describes an activity, while the other two goals state what the student will be able to do; CLAUDE.md asks for goals from the student's side ("Osaat ..."). Fix: "Osaat päätellä kokeen avulla, mistä sauvan pituuden muutos riippuu."
2. lesson.md, "Ydinajatus" — the paragraph under "### Miksi aine laajenee?" is two sentences and then a second paragraph; fine as is, but the figure (particles) now follows the paragraph about distance, which is the one it explains. No change needed; noted only so a later edit keeps the figure there.
3. Earlier Polish items (L2-03 Järkevyys sentence and the five older items) are not touched by this diff and still stand as optional.

## Checked
- Diff is a restructuring of "Ydinajatus" into three short "###" subsections plus a new `learn` list; no sentence lost a physical reason or causal step (the particle-repulsion/attraction asymmetry, water anomaly and liquid/gas reasoning are all intact).
- Each paragraph now holds one idea and is well under 120 words; the "lämpölaajeneminen" term is bolded once at its definition, as house rules allow.
- The particles figure still sits directly after the paragraph it explains.
- Subheadings name their content (Miksi aine laajenee?, Lämpölaajeneminen arjessa, Eri aineiden lämpölaajeneminen) and match the glossary term.
- `learn` has three one-line goals matching the slot (mikromalli; kiinteät aineet, nesteet, kaasut; laskeminen) and no more.
- Finnish in the new and moved text reads correctly (case forms, no stray grammar).
- Content hash unchanged at start and end of the review.
