VERDICT: PASS
CONTENT-HASH: c5c376b42c58397a

## Blocking

## Polish
- exercises.json L1-04, L1-05 — one formula but also a Celsius-to-kelvin conversion; the rubric puts conversions at level 2 — fine to keep as the first isobaric and isochoric drills, or move one to level 2.
- inquiry.json hook — the question "Mikä pussin ilmaan vaikuttava tekijä muuttuu" is long; shorter: "Mikä pussin ilmassa muuttuu lennon aikana, ja voiko muutoksen laskea?"
- lesson.md Ydinajatus — the plane-bag explanation (paragraph after the first figure) gives the answer to the hook before the reflect step; acceptable because theory comes after the committed predictions, but the sentence "Kireässä pussissa ... kovalta" is hard to follow for a first reader.
- inquiry.json exp-1 — column header "pV (J)" together with the 1 kPa · 1 ml = 0,001 J remark is a heavy intro; consider showing it only in the sim table note.
- sim.js / page — Playwright at 390 px found no speed control (hidas · normaali · nopea) and no "Lisätietoja" button, though the particles are animated (house rule 3; fy3-1 preview lacks Lisätietoja too, so possibly a shared-template gap) — add or confirm it is out of scope.

## Checked
- Playwright 390 and 1280 px: no horizontal overflow; pred-1 wrong option (100 kPa) commits, shows "Ennusteesi on tallessa. Palaute näkyy, kun olet tehnyt mittaukset." and the feedback stays hidden.
- Koe 1: Aseta alkutila, record 50 ml (100000 Pa, 5,00 J), slider to 25 ml, record (200000 Pa, 5,00 J); feedback then appears and matches the table.
- Reflection shows own prediction ("Ennustit: ...") with prompts for unanswered ones and the En/Kyllä revise question.
- Hash at start c5c376b42c58397a (rechecked at end).
- Prior items (p = F/A, gas expansion in fy3-8) match prerequisites fy3-4 and fy3-8; retrieval item is answerable.
- Predictions 1-3 are refutable by exp-1/exp-2; wrong options have repairing feedback; reveal gated on min measurements.
- Variable control: exp-1 locks mode and T, varies V; exp-2 locks mode and V, varies T; ranges fit the sim.
- No answer to the hook is disclosed before commitment; feedback is gated, theory follows the experiments.
- Interpret table (pV 5040 except 30 ml 5430) supports the stated answer and the three distractor feedbacks.
- Worked example staged in five steps, symbolic first; figures present at Ydinajatus and Kaava; paragraphs under about 120 words.
- Exercises 5/4/3; exit ticket tests the core idea (Boyle, 1/V graph, kelvin).
- Finnish reads correctly, glossary terms used consistently; no case errors found.
- Workload about an hour: three predictions, two experiments, one interpretation, one transfer, three checks.
