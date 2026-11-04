VERDICT: DONE

Unit fy9-aallot, "Värähtely, aallot ja ääni" (FY9 chapter 4, order 1). It reviews FY5 chapters fy5-7 to fy5-17. Developer report 2026-11-04.
Content hash at hand-over: 510226a7fdf49c1d (`python3 scripts/units.py hash fy9-aallot`).

## Files
- `content/fi/units/fy9-aallot/unit.json`: course FY9, chapter 4, order 1, kind review, 75 min, subjects physics. `sources` is empty because every dataset is an invented example.
- `content/fi/units/fy9-aallot/unit.md`: the Why question (a lifeguard's whistle heard under water), hero, `## Ydinajatus` (concept map, the hook answered with the to-scale `pilli` figure), `## Kaava: Värähtely, aallot ja ääni` in three parts (värähtelijät: f = 1/T, F = −kx, T = 2π√(m/k), T = 2π√(l/g); aallot: v = fλ, interference conditions, standing waves with the `ominais` figure; ääni: beats, both Doppler formulas, I = P/(4πr²), L in dB, d = vt/2), `## Yleisiä virheitä {Virheet}` (7 bullets), `## Kertaa tarvittaessa {Kertaa}` (all 11 chapters). The theory is about 540 words.
- `content/fi/units/fy9-aallot/inquiry.json`, `exit-ticket.json` (2 questions), `teacher.md`.
- `content/fi/units/fy9-aallot/sovella/tasks.json` and `solutions.md`. `lessons/units/fy9-aallot/sovella/answers.py` and `figures.py` (the two s3 model graphs: T(l), and T² against l with the fit).
- `lessons/units/fy9-aallot/figures.py`: `hero` (a swimming hall, no text), `kartta` (concept map, 380 wide), `pilli` (the same 3,0 kHz wave in air and water over 1 m to scale), `ominais` (string, open pipe and closed pipe at the fundamental).

## Counts
- Pohdinta: 1 hook. Ennusta: 6 choice items, one per chapter (mapped in teacher.md). Every option's feedback names the chapter as "luvussa *…*".
- Tutki: 1 interpret on the resonance frequencies of two 0,600 m tubes (one open, one closed; `source: example`). The numeric question asks for the speed of sound, 342,6 m/s.
- Teoriatiivistelmä: 1 theory activity with 4 sections.
- Sovella: 4 choice (find the error in an echo-sounder depth; read the catalog graph `fy5-10/yt-kuvaaja`; music heard round a corner (diffraction); two machines 88 → 91 dB and the allowed time). 4 numeric, each with a full solution, 3 hints and mistakes: car suspension 1,47 Hz; boat waves 1,72 m/s; train Doppler 27,5 m/s; outdoor concert speaker 178 m.
- Tarkista: choice (interference at 3,40 m and 4,25 m, 200 Hz), numeric (earthquake distance from the S−P delay, 119 km), explain (spring vs pendulum, effect of mass). All three have `practice` links. Exit ticket follows.
- Tehtävät: 6 tasks, 95 points.
  - s1 Kitaran kieli ja viritys (calc, 15)
  - s2 Lepakko saalistaa (calc: wavelength, echo, double Doppler, 15)
  - s3 Heilurin jaksonaika ja putoamiskiihtyvyys (data → graph → linearise T² vs l → fit → interpret, 20; cross-module with fy1 measurement)
  - s4 Festivaali rantapuistossa (word: dB with distance, diffraction of bass, noise exposure, 15)
  - s5 Äänen nopeus kaiusta (experiment: result, uncertainty from the spread, improvements, 15)
  - s6 Benjihyppy sillalta (cross-module with fy4 energy: free fall, spring energy, max force, period, 15)
- Every task has `skills` and `links`.

## Numbers (computed in Python: answers.py and scratch generators)
- s1: v 142,6 m/s; λ 3,12 m; fret position 577 mm, fret spacing 70,8 mm; beats 1,5 Hz → 108,5 Hz.
- s2: λ 11,3 mm; distance 2,04 m; reflected frequency 31,08 kHz (Δf 1078 Hz).
- s3: T² fit k 4,040 s²/m, b 0,055 s², g 9,77 m/s² (fit) / 9,78 m/s² (read from the line); l-intercept −1,4 cm (deliberate offset, the measured length is 1,5 cm short); l for T = 2,00 s 0,977 m.
- s4: 99,98 dB at 40 m, 79,98 dB at 400 m; λ 5,67 m at 60 Hz vs 0,085 m at 4 kHz; allowed time 15 min.
- s5: v 354 m/s; spread ±0,07 s gives ±52 m/s (14,6 %); range 309–415 m/s.
- s6: 18,8 m/s; lowest point 39,6 m; max acceleration 26,2 m/s²; period 4,87 s.
- Hook: 3,0 kHz; 350 → 1500 m/s; λ 0,12 → 0,50 m.

## Checks
- `units.py figures fy9-aallot` written; `practice.py figures units/fy9-aallot` up to date.
- `practice.py check units/fy9-aallot`: OK, 6 tasks, 95 points. `units.py check`: 40 units OK.
- `physics_phrases.py` on the unit finds 0 sentences.
- `build.py fy9-aallot` builds the preview.
- `check_layout.py --width 360` and `--width 1280`: OK.
- Playwright (`_browser.launch`) at 390 and 1280:
  - all 11 choice items answered with feedback, and all 6 numeric items answered ("Oikein.");
  - the explain model and both "Olen tehnyt ratkaisun" models opened, all details opened, all 6 solutions visible;
  - no console or page errors, 0 `.katex-error`, no raw `$`, no horizontal scroll.
- I looked at the hero, `kartta`, `pilli`, `ominais`, the catalog graph and both s3 graphs at 390, and the page top at 1280. Fixed:
  - `kartta` rows with √ overlapped (row spacing 34 → 52);
  - `pilli` label "λ ≈ 0,12 m" ran off the right edge (1 m = 400 units, labels size 24);
  - `ominais` labels enlarged and fractions written as λ/2, λ/4;
  - an unwrappable inline √ formula in s6 b split into three steps.

## Open questions
- All data are invented examples (`source: example`).
- `ominais` S/K labels are about 14 px at 390 px; a reviewer may want them larger.
- The s3 b text asks to "muodosta suure, jonka kuvaaja on suora", which prompts the linearisation without naming the formula, as in fy9-sailymislait.
- s6 treats the bungee cord as an ideal spring (stated in the task).

## Shared issues
None. The `fy5-10/yt-kuvaaja` catalog figure is reused as a Sovella choice figure.

## Round 1 fixes

Science (Blocking)
1. `jousitus` Periaate: now "koriin ja kuljettajaan vaikuttavat paino ja jousten harmoninen voima. Paino vain siirtää tasapainoasemaa, joten …".
2. s4 a: model answer (solutions.md) and the `assumptions` criterion (tasks.json) now say "Malli on karkea arvio: ilma ja maasto vaimentavat ääntä, mutta myötätuuli ja heijastukset voivat nostaa tasoa." (also pedagogy 2).
3. s4 b: "Bassot eivät välttämättä ole voimakkaampia: vaikka matalat ja korkeat äänet olisivat lähtiessään yhtä voimakkaita, aita vaimentaa korkeat."
4. s5 b: step is now $343\,\text{m/s} - 0{,}6\,\tfrac{\text{m/s}}{{}^\circ\text{C}} \cdot 15\,{}^\circ\text{C}$; answers.py `s5-v5C` = `343 - 0.6 * (20 - 5)` (334, unchanged).

Science (Polish)
5. s3 c Järkevyys: hand timing 0,1–0,2 s, 1–2 % of $t_{10}$ and 2–4 % of $T^2$; conclusion unchanged.
6. s3 intercept: b model answer says 0,055–0,056 s²; d Annettu says 0,056 from the read-off points and that the graph reads 0,055 with no effect on the result; the d criterion now uses 0,056 (l ≈ 0,976 m either way).
7. s5 a Periaate: "vaihteluvälin puolikas on karkea arvio hajonnasta, joka valitaan tässä tuloksen epävarmuudeksi".
8. tarkistus-3: criterion and model say the formula $T = 2\pi\sqrt{l/g}$ holds for small swings.
9. unit.md Ydinajatus: "Ääni on pitkittäinen paineaalto. Sen korkeus määräytyy taajuudesta ja voimakkuus intensiteetistä."
10. s2 c Periaate: one sentence that the bat is first the source and then the listener, speed $v_\text{l}$ (kept the symbol, now explained).

Pedagogy (Polish)
1. `aineisto` source_note: "Putken päätä ei ole korjattu." (also visual 5).
3. teacher.md: if time runs short, *Juna ohittaa laiturin* and *Ulkoilmakonsertin kaiutin* are home work for everyone.
4–6. Not changed (optional coverage, s6 setting for a later revision, s3 b hint accepted by the reviewer).

Visual (Polish)
- `pilli`: λ brackets and labels in ink, not red; the blue arrow is labelled "etenee"; the title says "paineaalto"; alt text updated.
- `fy9-aallot-s3-lin`: intercept dot and label in green (GOOD), label moved off the l axis.
- `kartta`: each branch has a grey linking phrase (toistuva liike · värähtely etenee · aalto ilmassa); alt text updated.
- unit.md: "Ajanhetken kuva ja yhden kohdan kuvaaja sekaisin".

Checks rerun: practice.py figures/check (6 tasks, 95 p), units.py figures/check (ok), build.py fy9-aallot, check_layout 360 and 1280 OK, Playwright at 390 and 1280 with all details open: no console errors, 0 katex-error, no raw `$`, no horizontal scroll; pilli, kartta and s3 graph screenshots inspected.
