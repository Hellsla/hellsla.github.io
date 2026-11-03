VERDICT: PASS
CONTENT-HASH: 7e0631f886a7e47c

## Blocking
(none)

## Polish
1. inquiry.json `ennuste-2`, the new third option ("Kun laatikon paino on suurempi kuin lankun paino") — the box is always 40 kg in this prediction, so the option is true or false for every position, not a position. Its feedback is good, but the distractor is easy to dismiss. Rephrase it as a position claim, for example "Kun laatikon paino on suurempi kuin lankun paino ja laatikko on tuen 2 ohi".
2. inquiry.json `ennuste-2`, first option — "sen painopiste on silloin tukien ulkopuolella" now reads as the box's own centre of mass versus the correct option's "yhteinen painopiste". That is a good contrast, but the feedback still says "sen paino"; align the wording with the option.
3. lesson.md figure `komponentit` — the force F is drawn at about 35° while α is unspecified, and the figure sits only in the "Momenttipisteen valinta" text. Add a label for the value of α, or add "esimerkiksi $\alpha = 30^\circ$", so that it matches L3-02.
4. Workload — `piirra` is now optional, which fixes the hour; consider saying in the exercises text which of the 14 exercises are the core (one per level).

## Checked
- Round-1 fixes confirmed in the diff: hook no longer discloses that the plank holds past the support ("Lopulta ... kaatuu"); ennuste-2 now has a misconception distractor and no clearly refuted option; `tarkistus-1` is now an application question with new distractors and fixed Finnish; the component task has a figure and its own step in the theory; `piirra` is optional; the crane picture is removed.
- Path and goals: tasapaino and momenttiehto, tukivoimat, painopiste and tipping, and the täsmennys (components) are all covered; no extra content.
- Predictions can be refuted by the model values (3:1 ratio, N1 = 0 at 3,5 m, x_pp = 3,0 m). The feedback repairs misconceptions and the model is called a model.
- The theory text about the components is correct: the component along the rod passes through the hinge and gives no moment; only F sin α counts.
- The worked example stages, the error-spotting item and `siirto` (1079 N → 1080 N) are unchanged and correct.
- Exit ticket tests the core idea; Finnish (case after number+unit, glossary terms) is consistent.
- Not re-opened: the 390 and 1280 px captures; the layout checks pass in the packet.
