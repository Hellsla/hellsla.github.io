VERDICT: PASS
CONTENT-HASH: ed63c3e5b1928717
Review of the recognition chart (queue 9c) and the term change against the version passed at f131fb403db2206f; full on the chart, delta on the rest.

## Blocking
(none)

## Polish
- B: Rows "sarjaan kytketyt -> sama virta" and "rinnan kytketyt -> sama jännite" show a pill (R_kok = ΣR, 1/R_kok = Σ1/R) that does not follow from the choice written beside it. Make the choice "kokonaisresistanssi" and mention the same current or voltage in the sign or aria-label.
- C: "laitteen teho tai energia -> teho P = UI" has no E = Pt; the aria-label has the same gap.
- C: "virta haarautuu -> haarapiste" is fine, but the pill ΣI_t = ΣI_l has no hint that it is the Kirchhoff's first law (aria-label gives it only in words).

## Checked
- 9 rows read; the aria-label matches each row; teacher.md updated to "rivi kerrallaan" and the conditions (Ohm at constant temperature, Joule only for a resistor) are listed there.
- Chart as a recognition chart: start box, then one card per sign with the choice and a dark-green pill; no formula list; 360 px capture readable, no clipped label.
- Placement after Ydinajatus (after Ydinajatus); aria-label read against every row: same rows, same order, same physics, spoken symbols in words, so usable for a screen reader.
- Changed term lines (liikekitka -> liukukitka) in the diff: consistent, physics unchanged.
- teacher.md sentence read against the chart.
- Not looked at: fi-easy and en versions (this report is fi only).
