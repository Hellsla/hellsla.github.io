VERDICT: PASS
CONTENT-HASH: e655f47847d2a009

Round 2: re-check of round-1 Blocking items against the fix diff.

## Blocking
- none. Round-1 item (check-2 answer 2.1 vs solution "2 %") is resolved by the rule `tolerance` is relative: 2.1 with 0.05 accepts 1,995–2,205, so 2 passes.

## Polish
- lesson.md Kaava — "Keskiarvon epävarmuus on yleensä sitä pienempi, ja sitä pienempi, mitä enemmän mittauksia on" is garbled. Write: "Keskiarvon epävarmuus on yleensä pienempi kuin yksittäisen tuloksen, ja sitä pienempi, mitä enemmän mittauksia on."
- inquiry.json exp-1 question — the correct option is two lines long and discloses the plateau value; shorten and keep the number in the feedback.
- pred-2 prompt states the 0,30 s systematic error and an option offers "noin 0,30 s", so the prediction can be read off the prompt; consider dropping the number from the prompt.
- Etsi-virhe and exit ticket: pick one rounding rule for the suhteellinen virhe (one significant figure like the virhe-arvio) and keep it in both.

## Checked
- Diff: $\Delta x = x - x_\text{oikea}$ replaced by plain "erotus $x - x_\text{oikea}$" in Ydinajatus, summary and exp-2 solution, so $\Delta x$ now means only the uncertainty; this removes my earlier symbol-clash Polish. Grammar fine.
- New pr-numerot feedback ("luettu kymmenesosina … kello näyttää sadasosat … tarkkuus ei silti ole sadasosa käsin") is correct, consistent with the lesson's resolution-vs-uncertainty paragraph, and the item still has one correct option.
- exp-2 solution: "Kaava: erotus $\bar{t} - T$", substitution 2,70 − 2,40 = 0,30 s unchanged and correct.
- Rest of the lesson unchanged since the full review; hand-checked numbers still hold.
- Hash unchanged at the end.
