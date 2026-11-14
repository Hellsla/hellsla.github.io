VERDICT: DONE

Unit fy9-koe, "Ylioppilaskoe ja vastaustekniikka" (FY9 chapter 1, order 1). Developer report 2026-11-03.
Content hash at hand-over: 210723c3675594ef (round 1; round 0 was 23902d39dc18f729) (`python3 scripts/units.py hash fy9-koe`).

## Files
- `content/fi/units/fy9-koe/unit.json`: course FY9, chapter 1, order 1, kind review, 75 min, physics. No `sources` (see Open questions).
- `content/fi/units/fy9-koe/unit.md`: Miksi question, hero, sections Koe {Koe}, Täydellinen ratkaisu {Ydinajatus} (steps figure, $a = 2s/t^2$ with its conditions, precision), Tehtäväsanat {Tehtavasanat} (table), Kuvaajat ja kaavat koneella {Kuvaajat} ($k = \Delta y/\Delta x$, graph figure, Graphical Analysis screenshot advice), Yleisiä virheitä {Virheet}, Kertaa tarvittaessa {Kertaa} (chapter links), and a staged 7-stage Esimerkki (bath water, kWh). Theory about 540 words.
- `content/fi/units/fy9-koe/inquiry.json`: 39 activities (generated from a Python script so that the LaTeX stays exact).
- `content/fi/units/fy9-koe/exit-ticket.json` (2 questions), `teacher.md` (75-min plan, diagnostic use, pair work, differentiation, note on exam facts).
- `content/fi/units/fy9-koe/sovella/tasks.json`, `solutions.md`; `lessons/units/fy9-koe/sovella/answers.py`, `figures.py` (model graph T² vs L).
- `lessons/units/fy9-koe/figures.py`: hero (exam desk, no text, no people), steps (seven-step overview), graph (fitted line, slope from two line points).

## Task counts
- Pohdinta 1 hook. Ennusta 6 choice (unit, justification, intermediate rounding, significant figures, slope from the fit, "arvioi").
- Tutki 1 interpret: two original answers A and B to one short task with a 6-point rubric; explain question with model answer and 4 criteria.
- Sovella: Esimerkki + 24-item diagnostic, 3 per module FY1–FY8, folded per module ("Kertaustesti FY1" …): 12 choice, 12 numeric (each with a complete 8-step solution, hints ≤ 3, mistakes). Every feedback names the chapter as a link; FY7 feedback links its chapter too (fy7-10, fy7-5, fy7-4; added 2026-11-04 when FY7 was on the site). FY6 items use fy6-2, fy6-3, fy6-4; FY8 items fy8-1, fy8-2, fy8-3.
- Tarkista: choice (määritä graafisesti), numeric (train acceleration, 0,44 m/s²), explain (helmet, impulse), then exit ticket.
- Tehtävät 4 long tasks, 61 points: s1 calc "Pyörällä vaaralle" 15 p (FY4/FY2), s2 data → graph → fit → interpret "Heiluri ja putoamiskiihtyvyys" 16 p (FY1/FY5), s3 explanation "Termospullo" 14 p (FY3), s4 experimental design "Vedenkeittimen hyötysuhde" 16 p (FY1/FY2/FY3). Each has skills, links, rubric, Yleisiä virheitä and Hyväksytään myös.

## Numbers computed (Python)
- Diagnostic: density 2700 kg/m³; power 0,60 kW; fireplace 26,25 → 26 MJ; Q 458,8 → 459 kJ; tyre 277,4 → 277 kPa; braking 7,8125 → 7,81 m/s²; collision 8,929 → 8,93 m/s; λ 0,7795 → 0,780 m; parallel 72,0 Ω; refraction 28,90°; F = IlB 0,30 N; H line 1,8889 eV, 656,5 → 656 nm. Mistake values recomputed (e.g. 11,58 m/s from kinetic energy, 58,75° and 30,08°).
- Tutki: 20 km/h = 5,556 m/s, a = 1,111 m/s², F = 71,1 N (B writes 7,1 N on purpose).
- Esimerkki: Q = 17 011 400 J = 4,73 kWh. Check-2: 0,4444 m/s².
- Long tasks (answers.py): s1 36 198,9 J, 134,07 W, 214,07 W, 262,7 kJ (12 % of 2200 kJ); s2 fit k = 4,0255 s²/m, intercept 0,062 s², L-axis −0,0154 m, g = 9,807 m/s², first point alone 9,07 m/s² (data generated with g = 9,81, bob radius 1,5 cm, small noise); s3 31 425 J, 1,455 W; s4 167 600 J / 194 400 J = 86,2 %.

## Checks run
practice.py figures/check units/fy9-koe (OK, 4 tasks, 61 points), units.py figures (up to date), units.py check (no fy9-koe errors), build.py fy9-koe (preview built), check_layout.py 360 OK; 1280 fails only on the teacher-notes box (Shared issues). Playwright at 390 and 1280: every choice and numeric answered, model answers and criteria opened, all details open: no console errors, no raw `$`, no `.katex-error`. Screenshots looked at: hero, steps, graph, Tutki card, item 24 with its solution, the pendulum model graph (two label overlaps fixed).

## Open questions
- **Exam facts not verified.** ylioppilastutkinto.fi and its file hosts (tiedostot., info.) are blocked in this session's network (proxy 403), so nothing could be fetched. The page therefore states no numbers: no task count, answer count, points, compulsory part, duration or allowed materials; it tells the student to check the board's rules and the exam instructions. A web search snippet (not a fetch) summarised a 2025 grading-instructions page as: part 1 one 20-point multiple-choice task, part 2 15-point tasks (answer four), part 3 20-point tasks (answer two), at most 7 answers, max 120 points. This matches the peda.net K2025 slide but is unverified. To add once fetched: https://www.ylioppilastutkinto.fi/sites/default/files/sites/default/files/documents/fi_reaaliaineiden_kokeiden_maaraykset.pdf, https://tiedostot.ylioppilastutkinto.fi/kokeet/2025-03-21_FY_fi_vi/grading-instructions.html, with `sources` checked 2026-11-04.
- Graphical Analysis is named as an example graphing program ("kuten Graphical Analysisilla"); whether it is in the current exam software list must be checked too.

## Shared issues
- `scripts/mixer.py` `_entry` crashes in `build.py` (sort key `m[2:]` on `None`) for unit task sets: `own_module` is None for a unit. The unit page itself is written before the crash.
- The preview's teacher-notes box (`.unit-teacher`) is 1152 px wide at 1280 px on a unit with a task set (608 px on fy14-photoelectric without one), so check_layout fails on "line length" at 1280. This is preview-only and in the shared template or CSS.

## Round 1 (2026-11-03)
- Science: testi-15 now has independent noise ("ensimmäisestä riippumatonta kohinaa"), and its feedback says "toisistaan riippumattoman lähteen". In s2 Yleisiä virheitä, squaring t₁₀ and dividing by ten makes T² ten times too large. s2 c Järkevyys is now ±0,3 m/s². Polish: the testi-12 mistake value is 11,57, testi-10 says "noin 0,8 g", and testi-22 uses an ultraviolet lamp.
- Pedagogy: the options of every choice item are rebalanced. The correct option is the longest (or tied) in 3 of 19 items, never by more than 3 %, and every option is within ±30 % of the correct one. unit.md maps the solution headings to the seven steps after the steps figure, and the Esimerkki maps its stage names to the same headings. teacher.md: the 12 choice items of all modules are done in class and the 12 numeric items at home; modules are no longer self-picked. Polish: the Tutki rubric says "oikea vastaus" and no point for a substitution without units, and names its items as the steps. Answer B is set as a list. check-2 has a precision mistake (0,4). The s1 a Järkevyys check is now an energy comparison (a kettle).
- Visual: the source_note prefix is removed, the steps figure has one neutral tint, and the pendulum point labels are at 20 px and clear of the axis.
- Checks: practice.py check OK (61 p), units.py check clean, build OK, check_layout OK at 360 and 1280, Playwright at 390/1280: no console errors, raw `$` or katex errors.

## Ratkaisutavan tarkistus (2026-11-12)
- sovella s2 c): vastaus 9,8 m/s², kaksi merkitsevää numeroa (luettu 0,46 s² on kaksinumeroinen; aiemmin 3 numeroa ja ±0,3 m/s² keskenään ristiriidassa).
- unit.md Vastauksen tarkkuus: rajaa tarkkuuden mitattu lähtöarvo, tarkat määrät ja muunnoskertoimet eivät rajoita.

## YTL- ja Abitti-tietojen tarkistus (FY9-valmentaja PR 1, 2026-11-14)

Alkuperäislähteet luettiin curlilla 14.11.2026 (lukupäivä kaikille alla). Väitteet koskevat sekä `fy9-koe`:ta että
`fy9-harjoituskoe`:ta (fi, en, fi-easy); sama taulukko on kummankin `review/developer.md`:ssä.

Lähteet:
- [M-reaali] Reaaliaineiden kokeiden määräykset ja ohjeet, hyväksytty 4.6.2025, koskee ensimmäisen kerran syksyä 2025:
  https://www.ylioppilastutkinto.fi/fi/tutkinnon-toimeenpano/maaraykset-ja-ohjeet/koekohtaiset-maaraykset-ja-ohjeet/reaaliaineiden
- [M-yleiset] Yleiset määräykset ja ohjeet, hyväksytty 8.5.2026, koskee ensimmäisen kerran syksyä 2026 (Abitti 2), luku 2.3.6 Koeaika:
  https://www.ylioppilastutkinto.fi/fi/tutkinnon-toimeenpano/maaraykset-ja-ohjeet/yleiset-maaraykset-ja-ohjeet
- [Liite 2] Kokelaan tietokonetta koskevat ohjeet, hyväksytty 8.5.2026:
  https://www.ylioppilastutkinto.fi/fi/tutkinnon-toimeenpano/maaraykset-ja-ohjeet/yleiset-maaraykset-ja-ohjeet/liite-2-kokelaan
- [Oheis] Koejärjestelmän oheisohjelmat, päivitetty 17.4.2026:
  https://www.ylioppilastutkinto.fi/fi/tutkinnon-toimeenpano/kokeen-tekniset-jarjestelyt/koejarjestelman-oheisohjelmat
- [HVP-K26] Hyvän vastauksen piirteet, fysiikka 25.3.2026: https://tiedostot.ylioppilastutkinto.fi/kokeet/2026-03-25_FY_fi/grading-instructions.html
- [HVP-S25] Hyvän vastauksen piirteet, fysiikka 17.9.2025: https://tiedostot.ylioppilastutkinto.fi/kokeet/2025-09-17_FY_fi/grading-instructions.html
- [Abitti-26] Ylioppilaskokeet keväällä ja syksyllä -26?: https://www.abitti.fi/kokelaalle/ylioppilaskokeet-kevaalla-ja-syksylla-26/
- [Pisterajat] https://www.ylioppilastutkinto.fi/fi/tutkinnon-suorittaminen/pisterajat ja
  https://www.ylioppilastutkinto.fi/fi/tutkinnon-suorittaminen/kokeiden-arvostelu
- cheat.abitti.fi (koeympäristön ohjeet) on JavaScript-sovellus; sen sisältöä ei saatu luettua tekstinä.

| # | Väite | Lähde (luettu 14.11.2026) | Tulos |
|---|---|---|---|
| 1 | Koe tehdään tietokoneella; kuvaaja liitetään kuvakaappauksena; kaavat kaavaeditorilla | Liite 2 (oma tietokone ja kokelassovellus); Abitti-26 ("Oheisohjelmasta voi edelleen liittää kuvakaappauksia osaksi koevastausta avotehtävissä") | tietokone ja kuvakaappaus oikein; **kaavaeditori tarkistamatta** (cheat.abitti.fi ei lukeutunut); ei muutosta |
| 2 | Koe kestää kuusi tuntia (360 min) | M-yleiset 2.3.6: "Koe on suoritettava kuuden tunnin kuluessa …", aikaisintaan klo 9.00 | oikein |
| 3 | 11 tehtävää kolmessa osassa, vastataan seitsemään | M-reaali 2.2 (fysiikka 11 / 7); HVP-K26 ja HVP-S25 (Osa 1, 2, 3) | oikein |
| 4 | Osa I pakollinen, yksi tehtävä, 20 p; monivalintoja, väittämiä, lyhyitä kysymyksiä | HVP-K26: "Vastaa tehtävään 1", 20 väittämää à 1 p; HVP-S25: monivalintoja à 2 p ym. | oikein (muoto vaihtelee, kuten sivu sanoo); harjoituskokeen 10 × 2 p on harjoituksen oma mitoitus |
| 5 | Osa II: 4 tehtävää seitsemästä, kukin 15 p | HVP-K26, HVP-S25: 7 tehtävää, "Vastaa neljään", 15 p | oikein |
| 6 | Osa III: 2 aineistotehtävää kolmesta, kukin 20 p | HVP-K26, HVP-S25: 3 aineistotehtävää, "Vastaa kahteen", 20 p | oikein |
| 7 | Enimmäispisteet 120 p | M-reaali 2.3; HVP-K26 "Koe yhteensä 120 p" | oikein |
| 8 | Graphical Analysis esimerkkinä kuvaajaohjelmasta | Oheis: Vernier Graphical Analysis Pro v6.2.0 ("lukiot voivat asentaa omalla asennuskoodillaan") | oikein esimerkkinä; ei muutosta |
| 9 | Apuvälineet: laskin, taulukkolaskenta, kuvaajaohjelma, kaavaeditori, kokeen taulukot ja kaavat | M-reaali 3: "ei saa käyttää apuvälineinä erillisiä laskimia eikä erillisiä taulukkokirjoja"; Oheis: Abicus-funktiolaskin, Collabora Calc, GeoGebra, MAFY-taulukot ja MAOL digitaulukot (lukion asentamina) | **epätarkka → korjattu**: harjoituskoe "Apuvälineet" fi/en/fi-easy: "tietokoneen laskinohjelmaa" ja lause "Erillistä laskinta tai taulukkokirjaa fysiikan kokeessa ei saa käyttää." Kaavaeditori tarkistamatta (kohta 1) |
| 10 | Arvosanarajat päätetään joka kokeessa erikseen pisteiden jakauman perusteella | Pisterajat: "Lautakunta päättää arvosanojen pisterajat kullakin tutkintokerralla erikseen …", SYK-menetelmä | oikein |

Ohjelmamuutos syksystä 2026: syksyn 2026 tutkinnosta alkaen koe tehdään Abitti 2:lla (M-yleiset koskee ensimmäisen
kerran syksyä 2026; Abitti-26: oheisohjelmat eroavat Abitti 1:stä, kuvakaappaukset toimivat edelleen). Sivujen
väitteet eivät nimeä Abitti 1:n ohjelmia, joten muutos ei tee niistä vääriä; Graphical Analysis on Abitti 2:n listalla.

Havainnot, joita ei muutettu (väitteiden ulkopuolella, opettajan päätettäviksi):
- `fy9-koe`:n hero-kuvassa on pöydällä erillinen laskin; M-reaali 3 kieltää erilliset laskimet. Kuva on katselmoitu; muutos vaatisi kuvan uudelleenpiirron ja hyväksynnän.
- `fy9-koe` "Sähköinen koe" kuvaa aineistot Osan III piirteeksi; HVP-K26:ssa myös 5/7 ja HVP-S25:ssä 4/7 Osan II tehtävistä on aineistotehtäviä. Ei väärä väite, mutta voisi mainita.
- Harjoituskokeen ylimääräisten vastausten ohje (lasketaan ennen mallivastauksia valitut) on harjoituksen oma sääntö; M-reaali 2.5:n mukaan oikeassa kokeessa lasketaan pienimmän pistesumman antavat vastaukset.
