VERDICT: PASS
CONTENT-HASH: b8d7e629c4b251af

## Blocking
- none

## Polish
- inquiry.json ketju-lampo hints[1] — "Veteen ei päätynyt energia on alkuenergian ja veteen siirtyneen energian erotus" is clumsy — "Veteen päätymätön energia on alkuenergian ja veteen siirtyneen energian erotus".
- lesson.md "Arjen energioiden suuruusluokat on koottu kuvaan, jossa jokainen väli on kymmenkertainen" and fig "tikapuut" caption "jokainen väli on 10-kertainen" — the labelled ticks (1 J, 1 kJ, 1 MJ) are 1000x apart, only the minor ticks are 10x; say "jokainen pieni väli".
- lesson.md Esimerkki "Tulos" — 340 kJ is claimed to be two significant figures, but a trailing zero is ambiguous; say "kymmenen kilojoulen tarkkuudella".
- Prediction ennuste-2 prompt ("pieniä pisteitä Maan pinnalla") nudges towards the wrong answer; neutral wording would let the prediction do more work.
- Workload: two predictions, two experiments, interpret, explain, three checks and exercises is near an hour's limit; the optional flags on kertaus, pohdi, virhe and tarkistus-3 keep the core path fine.

## Checked
- Opening question (bicycle energy from the Sun, where it goes) is answered by the chain figure, example and conclusion; goals met without E_k/E_p expressions.
- Predictions are refutable from table values; option feedback repairs the misconception and is gated.
- Figures 1 to 3 legible at 390 px, colour never alone, descriptions give the data; sim readout and controls usable at 390 px.
- Staged example one step per stage; unit conversion shown by replacing the prefix.
- Checks test concepts with misconception distractors; explain criteria observable.
- layout 1280 px now OK for fy2-2 (check_layout fy2-2 --width 1280); the packet's FAIL did not reproduce.
