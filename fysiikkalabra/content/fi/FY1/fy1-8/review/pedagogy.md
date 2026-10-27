VERDICT: FAIL
CONTENT-HASH: 320dd4262c607fdd

## Blocking
- inquiry.json activity `suunnittele` (stage tutki, before `teoria-osa`) — the student must write a plan with hypoteesi, muutettava/mitattava/vakioitavat muuttujat, a mittausalue "perusteltuna epävarmuudella" and a pöytäkirja before any of these terms or the t ≥ Δt/ε_max rule is taught (they come in Teoriatiivistelmä). `reilu-koe` has the same problem in milder form (its distractors use "muutettava/mitattava" undefined). A student with only fy1-3/fy1-4 cannot do the task and the criteria cannot be self-assessed — fix: move `suunnittele` to stage sovella after the example (before `tee-itse`), and in `reilu-koe` word the question without the undefined terms or define them in its text.

## Polish
- inquiry.json `hook` vs `poytakirja` — the hook says B drove 2,00 m five times with mean 4,74 s; the table has three readings at 2,00 m, mean 4,73 s ("viidellä matkalla ... kolme aikaa"). In a lesson about faithful records this inconsistency is distracting — fix: hook "viidellä matkalla, kolme toistoa kullakin; 2,00 m:n keskiaika 4,73 s", v still 0,42 m/s.
- `ennuste-1` — the hook says "Kumpikaan ei ole laskenut väärin", so the option "Ryhmä A on laskenut väärin" is not a live alternative, and the correct option is clearly the longest — fix: drop that sentence from the hook or replace the option with a real rival (e.g. "Ryhmän B auto kulki hitaammin pitkällä matkalla").
- `poytakirja` at 390 px — the Δt, ε and v columns, which the question needs, are cut off at the edge with no visible sign that the table scrolls — fix: shared table component should show a scroll cue or shadow.
- Graph: the lesson names matka the "muutettava" variable but plots it on the vertical axis; one sentence ("kulmakerroin vaatii, että aika on vaaka-akselilla") in the graph text would stop the clash with the usual "muutettava vaaka-akselille".
- Exercise L1-05 (equal spacing of six distances) tests a fence-post count, not the lesson's idea; replace with a pöytäkirja reading.

## Checked
- Opening question is answered by prediction, Pohjatiedot, table and theory; slot goals covered, no sim needed.
- Figures (setup, ε–t graph, s–t graph) legible at 390 px, labels LaTeX, graph values consistent (0,42 m/s slope, error bars to scale).
- Worked example: seven stages, symbolic first, 1,68 → 1,7 m with check; no repeat in exercises.
- Numbers verified: kertaus, Etsi virhe (2,4 m), siirto (14 m), tarkistus-2 (2,0 %), exit ticket, all exercise answers.
- Option feedback repairs the misconception rather than restating the answer; hints and mistakes sensible.
- Finnish and glossary terms correct; no text wall; levels 5/4/3.
- Workload: one lesson, optional items marked.
