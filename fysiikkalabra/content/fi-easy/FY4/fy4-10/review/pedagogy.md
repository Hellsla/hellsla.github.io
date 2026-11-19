VERDICT: PASS
CONTENT-HASH: 869cdded1a3067e5

## Blocking
(none)

## Polish
- lesson.md "Systeemi ja sen kokonaisliikemäärä" — "Esimerkki ovat vaunujen puskurien voimat toisiinsa törmäyksessä." — "Esimerkkejä ovat vaunujen puskurien voimat törmäyksessä."
- inquiry.json `simulaatio.text` — the visible lead is about 31 words (limit 30); move the sentence "Pylväät näkyvät ennen törmäystä ja joka hetki." to `howto`.
- inquiry.json `pred-3`/`exp-3` are optional but `reflect` and the theory's räjähdys section rely on them; if a student skips them the räjähdys law is met only in theory and the example/siirto task. Consider one line in `johtopaatos` or `reflect` that works without exp-3.
- lesson.md Newton's cradle caption — "Liikkuva kuula näkyy kuvassa epäselvänä" does not teach the point; say which balls move before and after, tied to the nopeuksien vaihto.
- exp-1 compares only three m2 values with v1 fixed; fine for the claim, but the explain `johtopaatos` could ask for one row quoted as evidence (criterion 1 already asks "omista mittausriveistä").

## Checked
- Path: prior (liikemäärä, impulssi, Ek) -> Newton 3 -> conservation -> collision kinds -> räjähdys; hook question answered in "Vastaus alun kysymykseen" (algebra is within reach: squares and subtraction); no 2D collisions, slot goals only.
- Predictions 1-2 are refutable by exp-1/exp-2 (reveal min 2); wrong options carry misconception-specific feedback; correct options cite model values; I recomputed the sim numbers (0,30 m/s; 0,042 J, 0,029-0,048 J; 0,20/0,80/-0,12/0,48 m/s; 0,63/1,26 m/s) and they agree.
- Variable control: only m2 varies, the rest is locked; the model simplifications (no friction, rigid track) are stated in `model`.
- Reasoning: the explain tasks have observable criteria matching their questions; check-1 distractors are real misconceptions (lost momentum, "lämmöksi", external force on a subsystem); Etsi virhe targets the sign error with a diagnosable answer.
- Worked example has seven stages, one step each, with a sensible-result check (15 % energy loss recomputed); the siirto task has three progressive hints and mistake feedback; solutions are complete.
- Figures (captures hero, 2, 3, tyypit): recognisable, uncluttered, colour paired with labels; descriptions give the same data without the answer. The hero matches its aria-label.
- Simulation at 390 px: controls and readouts legible, text behind Käyttöohje, Mallin oletukset, Laskennan selitys, speed control present.
- Exit ticket tests the core idea (condition for conservation, räjähdys) in two questions.
- Workload fits one lesson (core path: 2 predictions, 2 experiments, 1 explain, 2 checks; extras optional).
- Hash was 869cdded1a3067e5 at start and end (the default-language hash differs; I used --lang fi-easy as the packet says). Exercises not judged (separate review).
