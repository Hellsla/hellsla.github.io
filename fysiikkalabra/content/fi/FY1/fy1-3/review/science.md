VERDICT: PASS
CONTENT-HASH: e655f47847d2a009

## Blocking

## Polish
- inquiry.json exp-3, solution — "$0{,}0850\,\text{s}$", but the readout shows $0{,}085\,\text{s}$. Still open.
- lessons/FY1/fy1-3/lesson-answers.py — inq-ice-corrected (62,3 °C) is not used anywhere. Still open.
- Spelling — "virhearvio" and "virhe-arvio" are both used. Pick one.
- exercises/solutions.md L1-02 still writes the error as $\Delta x = x - x_\text{oikea}$. Align it with the lesson's new notation (this belongs to the exercise set).

## Checked
- Round 2: re-check of round-1 Blocking items against the fix diff.
- Δx clash resolved:
  - lesson.md:6 and the Tiivistelmä now define mittausvirhe as the difference $x - x_\text{oikea}$ with no symbol;
  - $\Delta x$ is left only for the positive half-range or uncertainty;
  - the systematic error keeps its own subscripted $\Delta x_\text{sys}$;
  - the exp-2 solution now writes $\bar{t} - T$ throughout, the same as the sim's "ero oikeaan", with the answer 0,30 s unchanged.
- pr-numerot distractor resolved. The feedback now says that 2,40 s shows the clock displays hundredths, and that hand timing is not accurate to a hundredth. This agrees with the correct option and with the resoluutio paragraph. Grammar is fine, and exactly one option is still correct.
- No other "Δx = x − x_oikea" remains in lesson.md, inquiry.json or exit-ticket.json. The rest of the content is unchanged since the round-1 full review.
- Hash identical at start and end.
