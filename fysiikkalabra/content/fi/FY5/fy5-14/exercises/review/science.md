VERDICT: PASS
CONTENT-HASH: 5cd3571020c4ddc7

## Blocking

## Polish

## Checked
- light delta review (teacher 2026-11-07), LOPS extension marking: diff vs origin/main: only the text prefix 'Syventävä tehtävä.' / 'Extension task.' on L1-04, L2-03, L2-04, L2-05, L2-07, L3-01, L3-04 and L2-03's core flag removed; data, answers, solutions and answers.py unchanged. The seven are exactly the tasks that calculate a Doppler frequency, so they match the lesson's move of the formulas to Lisätiedoksi; the remaining Doppler task L1-07 (core) is qualitative (constant, higher pitch; fronts denser in front) and needs no formula. No physics changed.
- Round 2 (commit 4ff432a8f), checked against the text only, not renders. "Voimakkain piikki" replaces the ambiguous "Korkein piikki" in the task, in statement 1's feedback and in the solution, so "korkea" no longer means both pitch and peak height. The physics is unchanged: pitch comes from f1 = 330 Hz.
- Statement 2 ("Saman sävelen soittava huilu kuulostaa erilaiselta kuin viulu, koska sen yläsävelet ovat eri voimakkaita.") is true and no longer hedged, which removes the round-1 form cue. The statements now have no hedges at all.
- Statement 4's feedback now ends "kasvaa äänen voimakkuus, ei korkeus", the lesson's own wording.
- The verdicts are unchanged and right: 2 and 5 true; 1, 3 and 4 false. The three warned mistakes are still covered, and each statement's feedback gives its reason.
- The solution matches the task (voimakkain piikki). answers.py is unchanged, and running it with python3 -I gives the same 16 numeric answers. The rest of the set is unchanged.
