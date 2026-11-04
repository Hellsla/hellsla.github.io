VERDICT: PASS
CONTENT-HASH: fbf82dd8d638f8de

Science review, round 2, of the Selkeä suomi translation of fy9-koe (source content/fi/units/fy9-koe/, reviewed).
Checked again: `check_i18n.py` (fi-easy: 0 errors), `practice.py check content/fi-easy/units/fy9-koe` (passes),
and every string changed since round 1 against the Finnish source. Numbers, answers, tolerances, correct flags,
points and formulas are unchanged. The shortened inquiry options (activities 1, 3, 5, 21, 30, 32, 35) keep the
physics of the source: "Kevyempi henkilöauto kiihtyy enemmän" still rests on equal and opposite forces, the
induction option still names a *changing* flux, and the photoelectric option still compares each photon's energy
with the work function.

## Blocking
None. Round-1 Blocking 1 (net transfer) is fixed: `tasks[2].parts[0].criteria[4].detail` and
`tasks[2].parts[3].criteria[0].text` now say *nettona*, and solutions.md s3 a) Periaate explains the word once
("molempiin suuntiin siirtyvä energia lasketaan yhteen").

## Polish
1. Round-1 Polish 2–4 are done (the meter "näyttää jännitettä", "lopputulokseen tulee suurempi virhe", the
   kulmakerroin concept now says "kahdesta pisteestä, jotka ovat kaukana toisistaan").
2. inquiry.json `activities[32]` correct option drops "sinkin" ("suurempi kuin irrotustyö"). The prompt names zinc,
   so it is unambiguous; no change needed.
