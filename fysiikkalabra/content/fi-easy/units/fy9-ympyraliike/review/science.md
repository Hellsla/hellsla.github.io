VERDICT: PASS
CONTENT-HASH: ca70b3b450bf3201

Science review, round 2, of the Selkeä suomi translation (fi-easy) of fy9-ympyraliike against the reviewed Finnish
source. Checks rerun: `check_i18n.py` (fi-easy: 0 errors); every `$…$` formula of unit.md (88), teacher.md (16) and
sovella/solutions.md (371) identical to the source, none lost or added; headings identical; JSON data of inquiry.json,
unit.json, exit-ticket.json and sovella/tasks.json (answers, tolerances, correct flags, points) identical (field-by-field
walk, 0 data differences); no decimal point in any formula. The round-1 recomputation of all numbers (GPS 12,0 h,
72 Nm, 143 N, 27,6 km/h, 98,4 min, 235 N, trailer 444,6 N / 45,3 kg / 5,39 kN, s2 7,44 km/s, s4 21,0 s, s5 114,3 g,
s6 22,76 m/s, exit 2,5 m/s, geo 42 160 km) still applies: no number changed since round 1.

## Round-1 findings

- Blocking 1 (Lähtötaso 5, wrong definition of "kääntäen verrannollinen"): **fixed**. The feedback now reads "kun
  toinen kasvaa kaksinkertaiseksi, toinen pienenee puoleen", followed by "Kaksinkertainen etäisyys antaa neljäsosan
  voimasta", which is correct and directly answers the 1/r misconception.
- Polish 2 (pallosymmetrinen): fixed: "massa on jakautunut samalla tavalla joka suuntaan keskipisteestä, kuten Maassa."
- Polish 3 (key_concepts "voiman varsi"): fixed; vaikutussuora is now explained ("suorasta, jonka suuntaan voima
  vaikuttaa"); both sentences within 25 words; $r = d\sin\alpha$ is correct for the angle between force and arm.

## Blocking

None.

## Polish

1. The new mistake feedback in activities[13] ("varsi on kammen pään vaakasuora etäisyys akselista $d\cos 35^\circ$")
   is correct and now matches hint 2. No action needed.
