VERDICT: DONE

Unit fy9-tasavirta, "Tasavirtapiirit ja sähköenergia" (FY9 chapter 5, order 1). It reviews FY6 chapters fy6-1 to fy6-9. Developer report 2026-11-04.
Content hash at hand-over: 5d2b5d87bf295a65 (`python3 scripts/units.py hash fy9-tasavirta`).

## Files
- `content/fi/units/fy9-tasavirta/unit.json`: course FY9, chapter 5, order 1, kind review, 75 min, subjects physics. `sources` is empty because every dataset is an invented example.
- `content/fi/units/fy9-tasavirta/unit.md` (about 550 words):
  - the Why question (a cottage battery that runs LED lights for over a week but a cool box for only a day) and the hero;
  - `## Ydinajatus` with the concept map; the hook is answered with the `mokki` circuit (0,50 A + 4,0 A = 4,5 A; 200 h vs about 22 h);
  - `## Kaava: Tasavirtapiirit ja sähköenergia` in four parts: virta, jännite ja resistanssi; kytkennät ja Kirchhoffin lait; teho ja energia; paristo ja akku (with the `napa` U(I) figure);
  - `## Yleisiä virheitä {Virheet}` (7 bullets) and `## Kertaa tarvittaessa {Kertaa}` (fy6-1 to fy6-9).
- `content/fi/units/fy9-tasavirta/inquiry.json`, `exit-ticket.json` (2 questions), `teacher.md`.
- `content/fi/units/fy9-tasavirta/sovella/tasks.json` and `solutions.md`.
- `lessons/units/fy9-tasavirta/sovella/answers.py` and `figures.py`. These hold the two s3 model graphs: U(I) with a cut U axis, and the extrapolation to I_k.
- `lessons/units/fy9-tasavirta/figures.py`:
  - `hero`: a cottage at dusk with a solar panel, battery box and cool box, and no text;
  - `kartta`: the concept map, 380 wide, 4 branches;
  - `mokki`: the cottage circuit, with the currents shown in violet #7048e8;
  - `napa`: U = E − R_s I with E, I_k and the slope −R_s.

## Counts
- **Pohdinta:** 1 hook.
- **Ennusta:** 6 choice items, one per misconception, mapped to chapters in teacher.md. The feedback names the chapter as "luvussa *…*". The items are:
  - current is not used up in series;
  - a voltmeter connected in series;
  - a lamp at half the voltage;
  - a parallel resistor added;
  - heating in a parallel connection;
  - headlights dimming while the engine starts.
- **Tutki:** 1 interpret on a constantan wire, R against l with offset 0,30 Ω (`source: example`). The numeric question asks for ρ = 0,500 µΩ·m.
- **Teoriatiivistelmä:** 1 theory activity.
- **Sovella:** 4 choice and 4 numeric. Each numeric has a full solution, 3 hints and the common mistakes.
  - Choice items:
    - find the error in a series resistor's power;
    - read the catalog lamp curve `fy6-3/lamp-curve`;
    - compare two batteries;
    - two resistors in series or in parallel.
  - Numeric items:
    - starter motor R_s 16,0 mΩ;
    - mixed circuit 0,40 A;
    - toaster wire 7,11 m;
    - kettle on the bill 2,09 €.
- **Tarkista:** choice (potential 8,0 V), numeric (E = 4,58 V) and explain (40 W and 100 W lamps in series). The exit ticket follows (5,0 Ω; 6,0 kWh).
- **Tehtävät:** 6 tasks, 95 points. Every task has `skills` and `links`.

  | Task | Title | Type | Points |
  |---|---|---|---|
  | s1 | Takalasin lämmitin | calc | 15 |
  | s2 | Sähköpotkulaudan akku | calc | 15 |
  | s3 | Taskulampun paristot kuormitettuna | data → graph → fit → interpret | 20 |
  | s4 | Kolme väitettä sähköturvallisuudesta | word | 15 |
  | s5 | Noudattaako vastus Ohmin lakia? | experiment: meter resolution and uncertainty | 15 |
  | s6 | Lämminvesivaraaja | cross-module with fy3 heat Q = cmΔT and fy2 kWh | 15 |

## Numbers (computed in Python in answers.py and the scratch generators)
- **s1:** R 11,25 Ω; P 162 W; film thickness 9,78 µm; c 145,8 W; with R_s 0,020 Ω: I 11,0 A, U 12,38 V, P 136,2 W.
- **s2:** 374,4 Wh (1,35 MJ); 27,7 km in 83 min; I 2,50 A, U 35,5 V; efficiency 85,7 % (436,8 Wh from the socket, 6,6 c).
- **s3 fit:** k −0,727 Ω, b 4,625 V. Read from the line: E 4,63 V, R_s 0,733 Ω (0,244 Ω per cell). I_k 6,3 A, more than six times the largest measured current. Lamp 3,6 Ω: I 1,07 A, P 4,11 W (83 % of the source power).
- **s4:**
  - cord 0,68 Ω gives 68 W;
  - kettle 8,70 A plus toaster 3,70 A gives 12,4 A on a 10 A fuse;
  - a bird across 4 cm of line at 600 A sees 1,6 mV.
- **s5:** R 96,2 / 100,0 / 102,0 Ω; relative uncertainty 9,2 / 4,2 / 2,8 %.
- **s6:**
  - heating 300 l from 15 °C to 70 °C takes 69,1 MJ = 19,2 kWh, which is 6,40 h at 3,0 kW;
  - standing loss 66,7 W (584 kWh a year);
  - at 220 V: 2,74 kW, 13,0 A, 17,6 Ω;
  - shower 2,33 kWh.

## Checks
- `units.py figures fy9-tasavirta`: written, then up to date. `practice.py figures units/fy9-tasavirta`: written.
- `practice.py check units/fy9-tasavirta`: OK, 6 tasks, 95 points.
- `units.py check`: 42 units OK. `physics_phrases.py`: 0 sentences.
- `build.py fy9-tasavirta`: builds. `check_layout.py --width 360` and `--width 1280`: OK.
- Playwright (`_browser.launch`) at 390 and 1280:
  - all 11 choice items, all 7 numeric items (including the Tutki question) and the explain model gave "Oikein." or showed the model;
  - every "Olen tehnyt ratkaisun" was ticked, every details element opened, and both s3 graphs were visible;
  - no console or page errors, 0 `.katex-error`, no raw `$`, no horizontal scroll.
- I looked at the hero, `kartta`, `mokki`, `napa`, both s3 graphs and the page top at 390 and 1280. I fixed these hero problems:
  - the crescent moon had a dark overlay disc; it is now a single path;
  - the shore ended in a hard vertical edge; it now curves down;
  - the reflection streaks floated beside the jetty; they are removed;
  - the birch overlapped the spruce; it has been moved.

## Open questions
- All data are invented examples (`source: example`).
- In the theory, E is the emf, so energy is written W. A note says so.
- Household 230 V AC appears in s4, s6 and the kettle numeric and is treated with DC laws (effective values), as in fy6-7. A reviewer may want a sentence about this.
- The s3 a graph cuts the U axis at 3,6 V and marks the cut with a zigzag. The task text and the solution mention the cut.
- s3 b accepts R_s with a tolerance of 0,06 Ω, because values read from a hand-drawn line vary.

## Shared issues
- `scripts/test_inquiry.py` and `scripts/check_choices.py` do not accept units (they expect chapter ids), so I used my own Playwright script instead.
- `build.py fy9-tasavirta` also rebuilds the preview indexes and module pages (en, fi-easy and others). This is shared output, and other agents' builds do the same.
- The catalog figure `fy6-3/lamp-curve` is reused as a Sovella choice figure. No change was needed.

## Round 1 fixes

Science
- B1 s5 a Vastaus: now "eli mittarien virherajojen mukaan todellinen arvo on todennäköisesti välillä noin 88–106 Ω".
- P1 Tutki Järkevyys: "jopa 20 %" → "noin 22 %".
- P2 s3 d (solutions.md and the tasks.json criterion): "hieman mittausalueen yläpuolella, joten malli pätee siihen todennäköisesti hyvin".
- P3 unit.md "Paristo ja akku": added "missä U on nimellisjännite" (+5 words; theory stays about 600).
- P4 s2 d Periaate: added "Mallissa akun lähdejännite on latauksen aikana keskimäärin nimellisjännitteen 36 V suuruinen."
- P5 keitin Järkevyys: "Keitin on kodin suuritehoisimpia laitteita mutta ei suurimpia energian kuluttajia".
- P6 s5 b Periaate: "Metallin ja hiilikalvon resistanssi muuttuu lähinnä lämpötilan mukana".

Pedagogy
- B1 Tutki source_note: numbers and material removed ("Arvot on laskettu mallista, ja niihin on lisätty mittausjohtojen resistanssi ja lukemien kaltaista vaihtelua.").
- B2 s3 source_note: E and R_s removed ("Luvut on laskettu mallista, ja niihin on lisätty mittausten kaltaista vaihtelua.").
- P1 lue-kuvaaja: prompt gives only the 3,0 V reading and asks the student to read other values from the graph.
- P2 s5 c criterion 4 and model answer: now "virtamittari sarjassa ja jännitemittari vastuksen rinnalla" plus the meter-effect estimate.
- P3 teacher.md: if time runs short, the fit is done on a ready graph or the intercept goes home.
- P4 not changed: varying the potkulauta/akkuvertailu and paahdin/s1 pairs means rewriting a choice item and its numbers; left for a later round (the repetition is deliberate review of W = UQ and R = ρl/A).
- P5 tarkistus-3 criterion 4: now says either statement earns the mark.

Visual
- P1 source-note pill radius: shared component, see Shared issues.
- P2 the two rewritten notes no longer start "Keksitty esimerkki"; the other notes already start with the subject.
- P3 measured in the DOM at 390 px: every label in `mokki` and `napa` renders at 14,3 px, so not enlarged.
- P4 `mokki`: label is now "kylmälaukku"; the circuit moved 20 px left to make room.
- P5 noted: theory has only the 5 words of science P3 added.

Checks rerun: practice.py figures/check (6 tasks, 95 p), units.py figures/check (OK), build fy9-tasavirta, check_layout 360 and 1280 OK, Playwright at 390 and 1280: no console errors, no raw $, no .katex-error, scroll width equals viewport.

Shared issues (round 1): the source-note badge should use a smaller border radius when the note wraps to several lines (visual P1).
