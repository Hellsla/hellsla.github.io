VERDICT: PASS
CONTENT-HASH: af9c16707d86ff5d

## Blocking
(none)

## Polish
- [Minor] 390 px top — the task tab strip's "2 Napa…" is still overlapped by the Kuuntele button (shared header, not Sovella-specific); check that the strip scrolls.
- [Minor] solutions.md fy7-s4 a) Kaava — "Celsiusasteina lämpötilan lukuarvo…" has a capital C in mid-sentence after a comma: "celsiusasteina".
- [Minor] solutions.md fy7-s2 a) Vastaus — the answer renders as boxed f followed by "Ja U ≈ 9,9 V…" with a capital J; lower-case "ja", or box both results.
- [Minor] solutions.md fy7-s4 e) Annettu — "lasin taitekerroin 1,50, ilman 1,00" give bare values; "ilman taitekerroin 1,00" reads more clearly.
- [Minor] tasks.json fy7-s1 text — "positiivisella varauksella varatut ionit" is still clumsy (round 1 suggestion).

## Round 3 (delta)
The only change since 0c3028a551af5e7c is solutions.md fy7-s1 d) Sijoitus: B's fraction is now split into mv = 1,8281 · 10^-26 kg · 7,251 · 10^5 m/s = 1,3256 · 10^-20 kg · m/s, then "joten" and B = (1,3256 · 10^-20 kg · m/s)/(1,602 · 10^-19 C · 0,400 m) = 0,2069 T. Opened at 340 px: the mv chain breaks at the product sign with the continuation indented, the fraction fits inside its box, and the two "joten" lines separate the steps cleanly (equation, then B, then r10, then Δx). Order principle intact, decimal commas, units upright with thin space, \cdot throughout. check_layout.py FY7-sovella --width 340: OK (also 360). Page scrollWidth equals the viewport at 340. No new finding; nothing else needed re-reading.

## Checked
- Round 2 content kept: hash 0c3028a551af5e7c captures (contact sheets, fig-1, fig-11, fig-20, fig-22, top-390, s2 a), s3 e), s4 a), d), e)) all judged then.
- Round 3: fy7-s1 d) Sijoitus at 340 px (own capture, scratchpad/shots/fi-340.png), layout check at 340 and 360.
- Packet captures are stamped for af9c16707d86ff5d, the current hash.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
