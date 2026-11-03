VERDICT: PASS
CONTENT-HASH: 6efd6dde9d89f690

## Blocking
(none)

## Polish
- inquiry.json ennuste-1 / ennuste-2 prompts — they state "virtamittari kytketään sarjaan" and "vahingossa sarjaan", and ennuste-2 gives both resistances, so the how and most of the why of the hook question are visible before the student has committed to anything. Fix: add an optional commit item first ("Piirrä/valitse, mihin kytket kummankin mittarin") and move the resistance values to a hint opened after the answer; or word ennuste-2 without "vahingossa sarjaan".
- Scope — the slot goals name connection, multimeter, range and the meter's effect; the virheraja formula, error-bands figure, the whole worked example, Etsi virhe, siirto, tarkistus-2 and exit question 2 are about error limits. The worked example does not model the lesson's main skill (connecting a meter). Fix: keep (it matches the measurement-uncertainty prior) but trim to one error-limit task in Sovella, or add a short connection/range worked case.
- lesson.md Esimerkki "Tulos" — relative limits "2 % ja 0,67 %" come from the rounded limits; the unrounded ones are 1,8 % and 0,63 %. Fix: compute from 0,0275/1,50 and 0,0095/1,500, or say "noin".
- inquiry.json koe-1 intro — asks "mitä mittarille tapahtuu" with the meter beside the lamp, but at 200 mA with three batteries the model fuse does not blow (about 145 mA); the lesson text says it "voi" blow. Fix: say in the intro to also try *pariston rinnalle*, where the fuse does blow.
- lesson.md Virherajan laskeminen — "mittarin lukema ei ole täsmälleen mitattavan suureen todellinen arvo" reads awkwardly. Fix: "Mittarin lukema ei ole täsmälleen sama kuin mitattavan suureen todellinen arvo."

## Checked
- Path from fy6-1 (current, voltage) to series/parallel, resistance, wrong connections is followable; hook question answered in Ydinajatus and the figures.
- Both predictions are refutable by the sim; each wrong option's feedback repairs its misconception; koe-1/2/3 lock and vary one parameter, min 2.
- Koe-3 (optional) lets the student see decimals and OL; johtopäätös after koe-1/2 with observable criteria.
- Worked example is seven stages, one step each; calculations and rounding check out (0,0275 V, 0,0095 V).
- Etsi virhe distractors are real mistakes; siirto (152 %), tarkistus-2 (6,23 mV) and their mistake values are correct.
- Exit ticket tests OL and the error limit; reasonable.
- Figures (#3–#7) legible at 390 px, wrong-connection figure shows the two failures with I and I ≈ 0 labels.
- Phone: sim (#2) fits, readout and selectors readable.
- Finnish: terms as in the glossary; no case errors found.
