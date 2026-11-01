VERDICT: FAIL
CONTENT-HASH: 80abae277caa0b18

## Blocking
- [Major] lesson.md Esimerkki, Järkevyys (example-390-2) — the inline `\tfrac{4{,}0\,\text{m/s} + 8{,}72\,\text{m/s}}{2} \approx 6{,}36\,\text{m/s}` is set by the page as its own block. The numerator and denominator are in a script-size font, about 7 px at 390 px, so the fraction is hard to read — this is the check that closes the worked example, and on a phone it cannot be read comfortably — write the average as a written division, "$(4{,}0\,\text{m/s} + 8{,}72\,\text{m/s}) : 2 \approx 6{,}36\,\text{m/s}$" (house rule: a division in text is a colon), or as a `\dfrac` in display.

## Polish
- [Minor] lesson.md Yksikkömuunnokset "(m, m/s, m/s²)" and inquiry.json prompts "Vastaa yksikössä m/s." / "m/s²." (exp-3, putoaminen, siirto) — units are plain text (standing rule 2026-11-01, untouched text) — write "$\text{m}$, $\text{m/s}$, $\text{m/s}^2$" and "yksikössä $\text{m/s}^2$".
- [Minor] inquiry.json exp-3 prompt — "Piirrä kuvaajasta lukemillasi pisteillä tangentin kulmakerroin" is wrong: a slope is calculated, not drawn, and the points are already given — "Laske näiden pisteiden avulla tangentin kulmakerroin eli kärryn hetkellinen nopeus tällä hetkellä." For science: the prompt gives the right end as $16\,\text{m}$, but the hint and solution use $16{,}2\,\text{m}$.
- [Minor] sim-390, sim-1280 — the open origin marker covers the "0" tick on the $x$ and $v$ axes — move the origin label left or below.
- [Minor] theory-1280-2 — inline formulas break across lines ("$\tfrac12 \cdot$ / $a\,t \cdot t$", "$A\,t^2 +$ / $B\,t + C$"), and exp-2 intro has $v_0 = 6\,\text{m/s}$ where everything else is $6{,}0$ — keep each formula on one line (a non-breaking unit) and write $6{,}0\,\text{m/s}$.
- [Minor] fall-points (fig-2-390) — the data points are small dots, not the house filled r 6 circles with a white ring. Figure "area" writes $at$ while the text writes $a\,t$ — use one form.

## Checked
- contact-1…6 (triage); fig-2, fig-3 (strobe), fig-4 (tv-graph), fig-5 (tangent), fig-6 (area), fig-9 (check-tv) at 390
- intro-1280 (hero), theory-1280-1, theory-1280-2
- example-390-2 (Sijoitus, Tulos, Järkevyys)
- sim-390, sim-1280; lab-1280-2 (Johtopäätös, putoaminen table)
- open-tarkista-1280-1 (feedback inside its card, check-tv)
- Strobe: spacing grows, $\overline{v}$ blue, $\overline{a}$ orange and constant, deceleration row correct. Hero stones spaced about 1:3:5:7.

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 4
