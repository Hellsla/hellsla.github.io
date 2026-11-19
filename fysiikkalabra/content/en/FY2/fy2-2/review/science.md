VERDICT: PASS
CONTENT-HASH: 1bf0b1235b3c3d94

## Blocking
(none)

## Polish
- inquiry.json tarkistus-1, wrong option "run out": its feedback now says "almost everything has spread as heat", while it lists "light, sound and thermal energy" first. That is fine, but "light and sound are also absorbed and become thermal energy" would show why the word is "almost" and not "all" (optional).

## Checked
- batch delta review: the conclusion's model answer now says energy is conserved and some of it ends up as thermal energy at each step. This is now the same as lesson.md:418 and the summary (line 571). The old "a large part at every step" claimed more than the theory does, and the new wording drops it. The FY2 "thermal energy … spreads as heat" wording fits the guardrail. In tarkistus-1, "almost everything" in both feedbacks now matches the correct option's "almost entirely", which closes my earlier polish item. There is still exactly one correct option, and the distractor's feedback still says why it is wrong (energy does not run out). The Artemis caption now says "thermal energy" instead of "heat", which keeps heat as energy in transfer. Worked example: I recomputed 450 kJ − 110 kJ = 340 kJ. The new rounding reason is right (a difference is rounded to the least precise decimal place, here tens of kJ), and it no longer depends on calling 110 kJ exact. The sum check is unchanged. The hash was the same at the start and the end.
