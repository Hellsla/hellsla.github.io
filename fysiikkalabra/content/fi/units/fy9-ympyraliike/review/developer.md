VERDICT: DONE

Unit fy9-ympyraliike, "Tasapaino, ympyräliike ja gravitaatio" (FY9 chapter 3, order 4). It reviews FY5 chapters fy5-1 to fy5-6. Developer report 2026-11-04.
Content hash at hand-over: fc0aa5da26550049 (`python3 scripts/units.py hash fy9-ympyraliike`).

## Files
- `content/fi/units/fy9-ympyraliike/unit.json`: course FY9, chapter 3, order 4, kind review, 75 min, subjects physics. `sources` is empty because every dataset is an invented example.
- `content/fi/units/fy9-ympyraliike/unit.md` contains, in order:
  - the Why question: a satellite TV dish never turns, although the satellite moves at about 3 km/s;
  - the hero;
  - `## Ydinajatus`: the force diagram first, then ΣF = 0 and ΣM = 0, or ΣF = mv²/r; the concept map; the hook answered with the to-scale `geo` figure;
  - `## Kaava: Tasapaino, ympyräliike ja gravitaatio`, in three subsections: the moment and equilibrium with the `tilanteet` FBDs; uniform circular motion; gravitation and satellites;
  - `## Yleisiä virheitä {Virheet}` (6 items);
  - `## Kertaa tarvittaessa {Kertaa}` (fy5-1 … fy5-6).
- `content/fi/units/fy9-ympyraliike/inquiry.json`, `exit-ticket.json` (2 questions: a carousel speed, and the force at 3r), `teacher.md`.
- `content/fi/units/fy9-ympyraliike/sovella/tasks.json` and `solutions.md`.
- `lessons/units/fy9-ympyraliike/sovella/answers.py` and `figures.py`. The figures are the two s3 model graphs: F(T), and F against 1/T² with the line and its extension to 8,0 N.
- `lessons/units/fy9-ympyraliike/figures.py`:
  - `hero`: a winter house with a dish and a satellite on a dashed arc, no text;
  - `kartta`: the concept map, 380 wide;
  - `geo`: the polar view to scale, r ≈ 6,6 R, with v, F, the line of sight and a faint copy 6 h later;
  - `tilanteet`: three FBDs drawn with fbd.py (a plank on two supports, a car at the top of a bump, a satellite).

## Counts
- **Pohdinta:** 1 hook (the dish).
- **Ennusta:** 6 choice items, one per chapter fy5-1 … fy5-6; teacher.md maps them. All feedback names the chapter as "luvussa *…*".
- **Tutki:** 1 interpret on the catalog graph `fy5-6/vr` (source: model). It asks for the GPS period: 11,98 h, tolerance 0,04, with 3 mistakes.
- **Teoriatiivistelmä:** 1 theory activity.
- **Sovella:** 4 choice items:
  - find the error in a chest-lid moment;
  - read the catalog graph `fy5-4/kuvaaja`;
  - a painter on a plank;
  - the satellite's force diagram.

  Then 4 numeric items, each with a full solution, 3 hints and mistakes: pedal moment 72,41 Nm, snow shovel 142,8 N, phone on a roundabout 27,62 km/h, science satellite 98,43 min.
- **Tarkista:** a choice (a swing at its lowest point), a numeric (wheelbarrow, 235,4 N) and an explain (the satellite's mass cancels). All three have practice links. The exit ticket follows.
- **Tehtävät:** 6 tasks, 95 points; every task has `skills` and `links`.
  - s1 Veneen traileri ja aisapaino (calc, 15)
  - s2 Sääsatelliitti napojen yli (calc, 15)
  - s3 Keskeisvoima pyörivällä alustalla (data → graph → linearise to 1/T² → fit → interpret and extrapolate, 20)
  - s4 Pyörivä avaruusasema (word, 15)
  - s5 Kiven massa metrimitalla (report critique and design, 15)
  - s6 Vuoristoradan silmukka (cross-module with FY4 energy, fy4-8, 15)

## Numbers (answers.py; `practice.py check` compares them with tasks.json)
- s1: drawbar force 444,6 N (45,3 kg), axle 5,39 kN, boat moved 11,1 cm, with the canister 32,4 kg.
- s2: v 7,44 km/s, T 101,4 min, F 31,5 kN (78 % of mg), turn 25,4°, about 2830 km at the equator.
- s3: the line read at (0,50; 1,01) and (2,50; 4,91) gives k 1,95 N s², so m 0,198 kg (−1,2 %). T_min = √(k/8,0 N) = 0,494 s, without the small intercept; the least-squares fit is close.
- s4: T 21,0 s for 1 g at r 110 m; g at 400 km is 8,69 m/s².
- s5: m_k 114,3 g (the student's 142,9 g ignores the stick's own moment).
- s6: v at the bottom 22,76 m/s, N 3,70 kN; at the top 11,21 m/s, N 165 N.
- Hook: r 42 157 km, 35 800 km above the surface, v 3,07 km/s.

## Checks
- `units.py figures` and `practice.py figures` are up to date.
- `practice.py check units/fy9-ympyraliike`: OK, 6 tasks, 95 points.
- `units.py check`: 40 units OK.
- `physics_phrases.py` on each file: 0 sentences.
- `build.py fy9-ympyraliike` builds the preview.
- `check_layout.py --width 360` and `--width 1280`: OK. I fixed these first:
  - a concept-map row overlap;
  - wide inline fractions in s1, s2 and s5 and in the snow-shovel hint, now split so the moment sum or γM is computed first;
  - unbreakable `;` lists in s3, now separate formulas.
- Playwright (`_browser.launch`) at 390 and 1280:
  - all 11 choice groups answered correctly, all 6 numeric items show "Oikein.";
  - the explain model and criteria opened, all details opened;
  - no console errors, 0 `.katex-error`, no raw `$`, no horizontal scroll.
- I looked at the hero, kartta, geo, tilanteet, both s3 graphs, the catalog graphs and the solution steps. I moved the "6 h myöhemmin" label in geo, which was clipped.

## Open questions
- All data are invented examples. The s3 noise is about 1,5 %, and the s2 orbit (830 km) is realistic, not a real satellite.
- s3 d drops the small fitted intercept (0,03 N) when it extrapolates; the solution says so. A reviewer may prefer keeping it, which gives 0,495 s.
- s4 asks for 1 g on a ring of radius 110 m (2,85 rpm). The model answer does not discuss the comfort limit of rotation rate; a reviewer may want it mentioned.

## Shared issues
- `scripts/physics_phrases.py <unit dir>` crashes with a traceback (read_text on a directory). Running it per file works.
- `scripts/inquiry.py fy9-ympyraliike` reports "no lesson folder" for units; `units.py check` validates them instead.
- None of these block the unit. The catalog figures `fy5-6/vr` and `fy5-4/kuvaaja` are reused on purpose.

## Round 1 fixes

Blocking (science 1–2, pedagogy 1–2, visual 1–2):
- Condition "Kaavat pätevät, kun vauhti on vakio" (science 1, pedagogy 1): unit.md now says that $a_\text{n} = \tfrac{v^2}{r}$ holds also at one instant when the speed changes, because at the highest and lowest points there is no tangential force. s6 b Periaate in solutions.md adds "Pohjalla tangentin suuntaista kokonaisvoimaa ei ole".
- Lumilapio Sijoitus "olkapään suhteen" (science 2, pedagogy 2, visual): now "takakäden suhteen".
- s3 d wording (visual, pedagogy 4): now "Mikä on lyhin kierrosaika, jolla alustaa saa pyörittää tällä kärryllä ja etäisyydellä?".

Polish:
- teacher.md Nopeat (science 3, pedagogy 5): asks "millä nopeudella".
- tarkistus-1 feedback $T$ for chain force (science 4, pedagogy 9): now $F - G = m\tfrac{v^2}{r}$, "ketjujen voima $F > G$".
- s2 d "43 kertaa kauempana" (science 5): model answer says "43 kertaa korkeammalla" and adds that the slant distance to Finland is over $38\,000\,\text{km}$; rubric says "yli 40 kertaa kauempana".
- Tutki GPS tolerance (pedagogy 3): 0,04 → 0,07 (accepts about 11,2–12,8 h).
- s5 a "oikein" (pedagogy 7): removed.
- tilanteet figure (visual): $\overline{N}$ label moved above the arrow tip, clear of the car; panel-title fractions are `\dfrac` (panels re-spaced, height 640 → 690); Earth arc and "Maa" are grey instead of velocity blue.
- Not changed: pedagogy 6 (weightlessness repeated; review repetition is intended), pedagogy 8 (set-up sketches for s1, s5, s6: not cheap), visual s1 a inline fractions (house style for Järkevyys), catalog figure label size and 1280 column (shared files).

Checks rerun: practice.py figures/check OK (6 tasks, 95 p), units.py figures/check OK, build OK, check_layout 360 and 1280 OK, Playwright at 390 and 1280: no console errors, no `.katex-error`, no raw `$`; the tilanteet figure was inspected at 390.

## Ratkaisutavan tarkistus (2026-11-12)
- s1 a), c): varsille symbolit $r_\text{t}$, $r_\text{v}$, $r_\text{k}$ (ei lukuja momenttiyhtälössä); aisapaino $m_\text{a}=F/g$ ja $\Delta x$ ratkaistu symboleilla.
- s2 b): osuus $q = F/(mg) = \gamma M/(g r^2)$ ratkaistu symboleilla.
- s5 a): varret $d_\text{p}$, $d_\text{k}$, $d_\text{m}$ symboleina; niiden lasku terän paikasta Muunnokset-kohtaan.
- inquiry lumilapio ja tarkistus-2: varret symboleina.
- Vastaukset eivät muuttuneet. fi-easy ja en vastaavasti.
