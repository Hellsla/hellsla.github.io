VERDICT: FAIL
CONTENT-HASH: 67ba387cc1473fac

## Blocking
- lesson.md, Esimerkki, vaihe "Tulos" — "Laitteen pituus 1,2 m on alle tuhannesosa fotonien välistä" is false: 1,2 : 940,8 = 0,0013 (the next stage says so) — write "noin tuhannesosa" or "vain noin 0,1 % fotonien välistä".
- lesson.md, Yleinen virhekäsitys, ensimmäinen kappale — "Kuulamallissa toisen raon avaaminen lisäisi osumia kaikkialla" contradicts ennuste-1's feedback ("Kuulamallissakaan osuus ei kasvaisi ... pysyisi samana"), so the student gets two opposite statements about what the bullet model predicts — rewrite: "Kuulamallissa toisen raon avaaminen ei vähentäisi osumia missään kohdassa; todellisuudessa tummiin raitoihin tulee osumia vähemmän kuin yhden raon kanssa", and state in both places whether the comparison is the count n or the share n : N.

## Polish
- inquiry.json ennuste-1 prompt — it says that x0 is a dark fringe "aaltomallin mukaan" and asks "mieti, mitä kuulamalli ja aaltomalli ennustaa", which nearly hands over the answer. Fix: let the student say whether x0 is dark or bright from the matkaero, or drop the "tumma raita" sentence until after the choice.
- inquiry.json compton-data — a "tutki" item before the theory section; the "Hidastumismalli" distractor is not a real student model. Fix: replace it with "fotonin energia ei muutu, mutta suunta muuttuu" or move the item after the theory.
- The four photon models appear only as a list, and no activity asks the student to match a phenomenon (interferenssi, valosähköinen ilmiö, Compton) to a model. Fix: make tarkistus-3 non-optional or add a one-line matching item.
- inquiry.json siirto — the doubling of the momentum change on reflection is not taught before the task and appears only in hint 3. Fix: add one sentence on mirror reflection to Yleinen virhekäsitys.
- Workload is at the upper edge of one lesson (2 predictions, 2 experiments, Compton data, siirto, 12 exercises). The optional items are marked correctly, so no change is needed unless a trial hour overruns.

## Checked
- Opening question is answered by koe-1/koe-2 and the conclusion; the predictions are refutable and the options' feedback repairs the misconception.
- Experiments lock hiukkanen/raot/x0 and vary one thing; the model values are named as model values.
- Compton table (0,0711 to 0,0760 nm) matches Δλ = 0,00243·(1−cos θ).
- Example: hf = 3,138e-19 J, N/t = 3,19e5 1/s, d = 941 m; one step per stage, plausibility check present.
- Tarkistus-2 answer 794,9 eV, distractors 1,273e-16 and 516 700 are real slips; siirto answer 290,5 µN; the Etsi virhe item is sound.
- Figures buildup, patterns and compton are legible at 390 px and do not show the answer before the predictions.
- Simulation at 390 and 1280 px is readable; controls are not clipped.
- Finnish and glossary terms (aalto-hiukkasdualismi, Comptonin ilmiö, kaksoisrakokoe) are consistent.
- Exit ticket tests the dualism idea and p = h/λ.
