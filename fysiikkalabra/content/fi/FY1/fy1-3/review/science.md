VERDICT: FAIL
CONTENT-HASH: b32be6c0168d0282

## Blocking
- lesson.md:6, 104, 259 and inquiry.json:234 (exp-2 solution) — A, an internal contradiction left by the fix. The symbol $\Delta x$ is defined twice in this lesson as two different things:
  - the signed, unknown mittausvirhe $\Delta x = x - x_\text{oikea}$ (line 6, Tiivistelmä);
  - three lines after the half-range formula, the positive estimate: "Virhearvio eli mittausepävarmuus ei ole itse mittausvirhe … se on aina positiivinen" (line 104).

  So the same $\Delta x$ is both "possibly negative, unknown" and "always positive, computed". The old sentence that explained the shared notation was removed. exp-2 then calls $\Delta t = \bar{t} - T$ "mittausvirhe", while $\Delta t$ everywhere else is the half-range.
  Fix: give the error itself its own notation, for example "mittausvirhe on erotus $x - x_\text{oikea}$", with no $\Delta x$, and write the exp-2 answer as $\bar{t} - T$, which the sim already labels "ero oikeaan". Or add back one sentence: "Δx tarkoittaa tässä arviota virheen suuruudesta".
- inquiry.json:34 (pr-numerot, the distractor "Nolla on turha") — A, inconsistent with the revised correct option and with lesson.md:110 (resoluutio). The feedback still says "$2{,}40\,\text{s}$ [kertoo] sadasosan [tarkkuudesta] … Loppunolla ilmoittaa, että sadasosat on oikeasti mitattu". For a hand-timed 2,40 s that is exactly the resolution-equals-uncertainty claim the guardrail removes: the correct option's feedback now says the uncertainty is much larger.
  Fix: "$2{,}40\,\text{s}$ kertoo, että kello näyttää sadasosat; lukeman tarkkuus ei silti ole sadasosa, kun aika otetaan käsin."

## Polish
- inquiry.json exp-3, solution — "$0{,}0850\,\text{s}$", but the readout shows $0{,}085\,\text{s}$. Still open from the last round.
- lessons/FY1/fy1-3/lesson-answers.py — inq-ice-corrected (62,3 °C) is not used anywhere. Still open from the last round.
- Spelling — "virhearvio" and "virhe-arvio" are both used (lesson.md:104 has both). Pick one.

## Checked
- The guardrail wordings are now in place:
  - measurement error vs uncertainty;
  - outliers are checked and removed only for a found, documented cause (theory, karkea and all its feedback, virhekäsitys, Tiivistelmä);
  - the half-range is a scatter estimate and a cautious bound for the mean, never called the uncertainty of the mean;
  - the scale-reading sentence word for word, with resolution ≠ uncertainty (hand timing about 0,1–0,2 s).
- karkea: exactly one correct option. The ends-are-wrong distractor and the inflate-Δt distractor stay wrong, and their feedback is right (mean shift 0,19 s; 0,09 → 0,62 s, ×6,9).
- One script recomputed the sim series: exp-1 −0,22 / 0,25 / 0,26 s, n = 40 mean off by 0,0005 s; exp-2 +0,2995 s; exp-3 0,085 / 0,525 s, ratio 6,18. The 2-figure reason (rounding to 0,01 s) is right. Sim sd 0,145 s, so the 0,26 s half-range is plausibly "suurempi kuin Δt_sat".
- Worked example 3,1817 s, 0,120 s, 3,77 % → 3,18 ± 0,12 s, 3,8 %; check-2 2,08 % (an answer of 2 is accepted); siirto 5,44 g and mistakes 5,6 / 27,2 / 4,8 / 28; ice 1,5 / 0,1 °C (×15); exit ticket 19,9 g, Δm 0,1 g, 2 %.
- Every choice item has exactly one correct option. The experiments lock sat/sys (or n/sys), and simState gives mean, puoli and vir.
- Hash identical at start and end.
