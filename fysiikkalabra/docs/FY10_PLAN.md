# FY10 – Kokeellinen fysiikka: plan

Working title and subtitle *Tutki, mittaa ja raportoi.* (teacher's brief 2026-10-30). Kiviruukin lukio's
school-specific course; registry entry `FY10` in `local-courses.json`, page `site/FY10.html` (status `planning`).
Nothing below is an approved course description until the teacher says so.

## Aim
Genuine experimental reasoning: research questions linked to theory, experimental design and variables, reliable
data, graphs and models, uncertainty and reliability, evidence-based conclusions, reproducible reports. Real
measurements before simulations; no fabricated data presented as observations. A full pathway must work without
every FY1–FY8 module; advanced work is an optional extension.

## Two structures
1. **Learning pathway** (themes, not a lesson count): research questions → hypotheses, models, predictions →
   design, variables, controls → measurement methods → graphical analysis and modelling → uncertainty and
   reliability → reporting and conclusions → independent investigation. Progression guided → partly guided →
   independent.
2. **Investigation library**: one canonical page per investigation, linked from FY10 and from any module or course
   that uses it; browsable by topic, prerequisites and demands. Not grouped "FY1 experiments, FY2 experiments …".

## Three separate classifications per investigation (or per variant)
- Physics knowledge **F1** basic · **F2** intermediate · **F3** advanced (approximate; exact prerequisites listed).
- Experimental complexity **E1** basic · **E2** intermediate · **E3** advanced. Safety is assessed apart.
- Support mode **Ohjattu · Osittain ohjattu · Itsenäinen tutkimus**, on one shared page (no copies per mode).
The brief's example table (jousivakio F1/E1, värähtelymenetelmä F2/E3, heiluri F2/E2, uppokuumennin F2/E2,
Planck LEDeillä F3/E2, hissi F2/E3) is preliminary until verified against method, equipment and analysis.

## Reporting framework
`FY10 – Työselostuspohja` (teacher's template, 5 pages): 1 Tutkimuskysymys ja tavoite · 2 Tausta ja teoria
(graafinen malli, hypoteesi) · 3 Koejärjestely ja menetelmä (välineet, kuva, toteutus, työturvallisuus) ·
4 Mittaustulokset · 5 Tulosten käsittely ja graafinen analyysi · 6 Tulos · 7 Johtopäätökset · 8 Luotettavuus ja
mittausepävarmuus · 9 Lähteet, plus a checklist before returning. Teach why each section exists; support fades
from examples to reminders to independent writing; a rubric on reasoning, method, analysis, interpretation and
reliability, not formatting. No invented grading rules.

## Source documents
The three PDFs supplied 2026-10-30 (Esimerkkityöt 17 p., FY10 – Työselostuspohja 5 p., YO 2024 11.A 1 p.) stay out
of this public repository. **`docs/fy10/inventory.md`** is the full inventory (phase B): 29 distinct investigation
cards with physics, modules and published chapters, F/E levels, support modes, TVT, equipment, safety and every gap.
Main findings: the blanks are in the PDFs themselves (lost aims and values, not extraction errors); two cards are
printed twice; two lack titles; six lack equipment lists; four need safety values from the real equipment; the
pendulum card names Espoon yhteislyseo (check authorship before adapting wording); the template's second way of
estimating the slope's uncertainty is missing.

## Proposed pathway (phase B, for the teacher's review)
Each theme gets one or two investigations from the library. The early ones need only FY1–FY4, whose chapters are
published, so a student without FY5–FY8 can follow the whole core path; FY5–FY8 investigations are options.

| Theme | Core investigation (F/E, mode) | Options |
|---|---|---|
| 1 Tutkimus ja tutkimuskysymykset | Pudotus- ja pomppukorkeus (F1/E1, O) · YO 2024/11 diagnostic: find the error in each section | Lämmön johtuminen lämpökameralla |
| 2 Hypoteesit, mallit ja ennusteet | Leikkiauton nopeus korkeuden funktiona (F1–F2/E2, O): predict $v^2 \propto h$ before measuring | Liikemäärän säilyminen törmäyksissä |
| 3 Suunnittelu, muuttujat ja vakioidut suureet | Heiluri (F2/E2, OO): choose the variable, control amplitude and mass | Tuulivoimala (one factor) |
| 4 Mittausmenetelmät | **Jousivakio, voima ja venymä** (F1/E1, O→OO) | Äänennopeus (F1/E2, I) |
| 5 Graafinen analyysi ja mallit | Uppokuumentimen hyötysuhde (F2/E2, OO) | Valaistusvoimakkuus ja etäisyys; Kappaleen jäähtyminen; Kaasun tilanyhtälö |
| 6 Epävarmuus ja luotettavuus | **Jousivakio kahdella menetelmällä** (F2/E3, OO): compare results within uncertainties | Hyppy voimalevyllä (two methods) |
| 7 Raportointi ja johtopäätökset | YO 2024/11 revisited independently; full report of one earlier investigation | — |
| 8 Itsenäinen tutkimus | student's choice from the library, mode I | Hissi, Muotokerroin, Kapasitanssi, Planck, Muuntaja, Taitekerroin … |

**First investigations to build** (one PR each, in this order):
1. *Jousivakion määrittäminen* (phase E): one page, method 1 core and method 2 extension, three support modes;
   needs a short Hooke's law explanation (no chapter yet) and FY5 guidance for the oscillation method.
2. *Pudotus- ja pomppukorkeus*: the gentlest start, physics only FY4 energy.
3. *Uppokuumentimen hyötysuhde*: after the teacher supplies the current limit; gives FY3 its first *Sovella kokeellisesti* link.

## First investigation (phase E)
*Jousivakion määrittäminen*: force–extension with a linear fit (FY4), extension via oscillations compared with it
(FY4 + FY5, FY5 not yet published: prerequisite guidance instead of a link). Links to the published chapters
*Mittaaminen ja mittauksen luotettavuus* and *Graafinen esitys ja suoran sovittaminen*; connects to the YO autumn
2024 problem 11 case (one most significant error and its correction per section; no answers revealed at once).

## Decisions awaiting the teacher
1. Official goals, scope (credits) and assessment of FY10 (the page shows none).
2. Whether the FY10 row should also appear on the English and selkosuomi front pages (now: a note that it is in
   Finnish only).
3. Approve or change the proposed pathway and the first three investigations above.
4. Equipment facts the cards lost: the heater's current limit, laser class, the school's motion sensors, force plate
   and video-analysis software (and which Graphical Analysis version students use).
5. Whether the Esimerkkityöt wording may be adapted (the pendulum card names Espoon yhteislyseo) or the cards are
   rewritten from scratch.
6. The second way to estimate the slope's uncertainty for the report template (§5).
7. Whether the investigation library gets its own public index page or lives only inside FY10 at first, and where
   public teacher guidance lives.
