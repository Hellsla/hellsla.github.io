VERDICT: FAIL

Scope: lesson.md, exercises.json (text), solutions.md, exit-ticket.json, sim-spec.md, sim.js (Finnish strings), glossary.json entries for fy3-2. Checked against glossary.json and CLAUDE.md conventions.

## Issue kinds
- Grammar (1, real): lesson.md line 19, "laskea osissa suorakulmioista, kolmioista ja puolisuunnikkaista" has wrong case government (reads as "in parts from rectangles"). Fixed in the diff below with "jakamalla se suorakulmioihin, kolmioihin ja puolisuunnikkaisiin". No number, formula or LaTeX touched.
- Spelling: none.
- Punctuation / decimal comma / units: clean. No decimal points in Finnish text; all number-plus-unit modifiers have correct case (80 N:n, 1,2 m:n, 36 kJ:n, 45 kJ:n, 1,5 kN:n, 850 kg:n, 30 m:n, 10 N:sta, 30 N:iin, 40 N:iin, 40 N:ssä, 2,0 kg:n, 180 W:n, 50 m:n, 3,0 m/s:n, 20 N:n, 6 kW:n, 40 N:n). Plain spaces before units are used throughout, same as content/_gold (CLAUDE.md mentions a thin space, but the gold lesson does not use one either).
- Terminology: consistent with glossary.json (työ, energia, teho, joule, lämpömäärä, paino, nostovoima). No synonyms invented. Glossary definitions for the four fy3-2 terms plus lämpömäärä are grammatical and agree with the lesson text.
- Reading level: suitable for 16-19-year-olds.

## Nits (not in the diff, stylistic or optional)
1. lesson.md line 61: "se voi nostaa kappaleen energiaa" is figurative; "kasvattaa kappaleen energiaa" would be more precise.
2. Extent adverbial is inconsistent: exercises.json L1-01 "25 metrin matkan" (accusative) vs L1-04 "6,0 m:n matka" (nominative), both in passive sentences. Both are accepted usage, so it is only an inconsistency.
3. sim-spec.md (human-written): "kun painaa Vedä-painiketta" uses a generic 2nd/3rd-person verb; "kun painetaan" is more standard.
4. solutions.md L1-02 "15 kg:n hyllyn nostamista reilun metrin" is a bit elliptical; "reilun metrin korkeuteen" would read more smoothly.
5. meta.json "glossary" does not list "lämpömäärä", although glossary.json lists fy3-2 for it and the lesson and L3-02 use it. Out of scope for this review (meta.json), flagged for the orchestrator or human.

## Diff
```diff
--- a/content/FY3/fy3-2/lesson.md	2026-10-24 14:52:31.631949909 +0000
+++ b/content/FY3/fy3-2/lesson.md	2026-10-24 14:52:31.651224491 +0000
@@ -16,7 +16,7 @@
 ```
 missä W on työ (J), F voiman suuruus (N) ja s kappaleen kulkema matka (m). Yksi joule on työ, jonka yhden newtonin voima tekee yhden metrin matkalla: 1 J = 1 N·m.
 
-Jos voima muuttuu matkan aikana, työ on (s,F)-kuvaajassa voimakäyrän ja s-akselin väliin jäävä pinta-ala. Vakiovoimalla pinta-ala on suorakulmio, jonka ala on F · s, joten sama laskusääntö toimii molemmissa tapauksissa. Monimutkaisen kuvaajan pinta-alan voi laskea osissa suorakulmioista, kolmioista ja puolisuunnikkaista.
+Jos voima muuttuu matkan aikana, työ on (s,F)-kuvaajassa voimakäyrän ja s-akselin väliin jäävä pinta-ala. Vakiovoimalla pinta-ala on suorakulmio, jonka ala on F · s, joten sama laskusääntö toimii molemmissa tapauksissa. Monimutkaisen kuvaajan pinta-alan voi laskea jakamalla se suorakulmioihin, kolmioihin ja puolisuunnikkaisiin.
 
 Kun nostat kappaleen hitaasti ylös, nostovoima on yhtä suuri kuin kappaleen paino G = mg (edellinen oppitunti). Nostotyö korkeudelle h on siis:
 ```latex
```
