VERDICT: PASS
CONTENT-HASH: 65ae78ca19f3d63b

## Blocking
(none)

## Polish
- [Minor] Plain-Finnish phrase "häviävän pieni virta" (lesson.md, Lähdejännite mitataan ilman virtaa) is a physics idiom the student may not know; it is a faithful translation and the sentence beside it says what it means. Left.

## Checked
- All `$...$` in lesson.md, inquiry.json, exit-ticket.json, exercises, solutions identical to the Finnish, decimal comma and `$...$` kept (script, line by line).
- All numbers in every string equal the Finnish. The one differing math-token order (inquiry feedback of Ennuste 1, option 1) is only a reordering of the same two readings (1,561 V at 0,195 A; 1,333 V at 1,333 A).
- Physics identical: model, formulas, graph slope, series/parallel, caveats, car starting, short circuit; terms lähdejännite, napajännite, sisäinen resistanssi, oikosulku used correctly and consistently.
- Prediction keys, `answer` fields and criteria unchanged.
- meta.json key_concepts: 4 items (within 3-5), every `explain` between 15 and 18 words (limit 25), no digits and no `$`, definitions correct (lähdejännite without current; napajännite with current and below E; sisäinen resistanssi in series with the source; oikosulku through a conductor, largest current, dangerous).
- Re-review after the concept-review commit: ex L1-05 points relabelled as model points (text, solution, figure description), napajännite explanation conditioned on current being drawn, matching the Finnish; no numbers changed; captures retaken.
