VERDICT: PASS
CONTENT-HASH: d8c5f62dda0ab6fa

## Blocking
(none)

## Polish
1. lesson.md "Induktioliesi: kattilan pohja on toisiokäämi" — "Oikosuljettu tarkoittaa, että kierros on suljettu eikä siinä ole kuormaa." is circular and confusing, since the base's resistance is exactly what heats. Fix: "Oikosuljettu tarkoittaa, että virta pääsee kiertämään suljetun silmukan, eikä sitä ole kytketty erilliseen laitteeseen."
2. lesson.md "Yleinen virhekäsitys" — "Tehojen suhde korotetaan toiseen potenssiin." is too abstract for fi-easy. Fix: "Kaksi 10 dB:n osuutta pienentävät tehon kahdesti kymmenesosaan, joten jäljelle jää 0,1 · 0,1 = 0,01 eli 1 %."
3. lesson.md "Miksi etäisyys ratkaisee" — "Ferriitti magnetoituu ferromagneettisen aineen tavoin" leans on an unglossed term for an easy reader; add "ferromagneettinen eli vahvasti magnetoituva, kuten rauta" at first use.
4. inquiry.json (same as en) — workload: four predictions, two experiments, measurement, conclusion, transfer and three checks is long for fi-easy readers; make ennuste-kela with koe-2 or mittaus-lataus `optional`.
5. Kuituyhteys section has no ray figure of core and cladding, and total internal reflection has no student task (goal in the slot); add a small figure or a short choice.

## Checked
- Same inquiry structure as en: 21 activities, same correct options, hints, mistakes, optional flags and numeric answers (script comparison); only the reveal `pending` texts differ, as translated.
- fi-easy inquiry.json names, units and table headers are Finnish (owner's decision); decimal commas in sim and text accepted.
- Glossary terms (langaton lataus, induktioliesi, pyörrevirta, vaimennus, kokonaisheijastuminen, valokuitu) used consistently; case after number+unit correct ($3\,\text{mm}$:n, $17\,\text{km}$:n).
- Sentences short, terms glossed inline (pyörrevirta, tasasuuntaa, absorboituu); reading level suitable.
- Figure captures (charger, hob, graph) labelled in Finnish and legible at 390 px; sim readout and boxes legible.
- Worked example staged; common-mistake feedback repairs the decibel error.
- Hash unchanged at end.
