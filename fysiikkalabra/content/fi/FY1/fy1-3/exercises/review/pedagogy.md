VERDICT: FAIL
CONTENT-HASH: 9c0e2ae1f4be967f

## Blocking
- exercises.json fy1-3-L2-02 (answer 10.67, tolerance 0.04) vs solutions.md L2-02 Vastaus — the solution now ends "noin $11\,\text{mm}$ (laskimen arvo $10{,}67\,\text{mm}$)" and the Järkevyys uses 11 mm, but the check accepts only 10,63–10,71 mm, so a student who gives the solution's own answer 11 is marked wrong (the same applies to 10,7). Fix: tolerance 0.4 (accepts 10,3–11,1 so 10,67, 10,7 and 11 pass), or return the solution to the stored precision.

## Polish
- exercises.json fy1-3-L2-03 text — "12,4 cm" and "123 mm" are left as plain text while "$0{,}125\,\text{m}$" is LaTeX; the three values should look alike. Write all three as `$12{,}4\,\text{cm}$`, `$0{,}125\,\text{m}$`, `$123\,\text{mm}$`.
- solutions.md L1-05 Vastaus — "virhe-arvio on karkea arvio, joten se ilmoitetaan yhdellä merkitsevällä numerolla" still uses "virhe-arvio" while the task and Kysytty now say "epävarmuus"; write "lukeman epävarmuus on karkea arvio...".
- exercises.json L1-05 prompt — "lukeman epävarmuudeksi arvioidaan puoli asteikkoväliä. Kuinka suuri on lukeman epävarmuus?" gives the question away in the situation sentence; shorten the situation to the scale interval and ask "Arvioi lukeman epävarmuus tällä tavalla."
- Earlier open Polish (repeated formula in each Kaava line, L3-03 duplicating L2-02) still stands; not part of this diff.

## Checked
- LaTeX conversion of numbers with units in L1-01, L1-03, L1-04, L2-01, L2-02, L3-01 and L3-02: values and units unchanged, answers still consistent.
- L1-05 and L3-02 now say "epävarmuus" for the reading instead of "virhe-arvio"; consistent with the lesson's Kaava text (half the smallest division, kokonaisepävarmuus may be larger).
- L1-05 Järkevyys is now physically honest: the reading interval is 1,0 mm wide, total uncertainty may exceed it.
- L2-02 reasoning (each reading 9–12 mm too large, mean between them, about 1 % too much) is correct.
- Finnish of the changed passages is correct; no new terms.
- Hash unchanged at the end.
