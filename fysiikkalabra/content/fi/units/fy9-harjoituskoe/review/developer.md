VERDICT: DONE

Unit fy9-harjoituskoe, "Harjoituskoe" (FY9 chapter 7, order 1). Developer report 2026-11-04.
Content hash at hand-over: 1e35148179fc1f8f (`python3 scripts/units.py hash fy9-harjoituskoe`).
Judged against docs/FY9_PLAN.md "Lesson 16: the mock exam", not the review-lesson form table (teacher 2026-11-04).

## Files
- `content/fi/units/fy9-harjoituskoe/unit.json`: FY9, chapter 7, order 1, kind review, **minutes 360** (the exam is 6 h; the brief's default 75 does not fit), physics, sources [] (see Open questions).
- `unit.md`: Miksi question, hero, three sections placed in Sovella: Kokeen ohjeet {Ohjeet} (structure table, 120 p, Osa I point split 10 × 2 p, where Osa II/III are, allowed tools in general terms), Aikasuunnitelma {Aikataulu} (plan figure to scale: 15 + 50 + 160 + 110 + 25 = 360 min), Itsearviointi (Osa I scoring rule, rubric use, what next). No theory summary.
- `inquiry.json`: learn 3, prior 2, activities: theory (the three sections), text "Osa I: kymmenen lyhyttä kohtaa (20 p)", osa1-1 … osa1-10 (fold tag "Osa I"). All in stage sovella; no Pohdinta, Ennusta, Tutki, Tarkista or exit ticket (inquiry.validate and units.py check require none). The page therefore shows one stage chip "Sovella" plus "Tehtävät".
- `teacher.md`: running it as one 6 h day or split (3 × 2 h, or 75-min lessons), grading with the rubrics, peer check, grade bands explicitly unofficial, after-exam use, differentiation.
- `sovella/tasks.json`, `sovella/solutions.md`; `lessons/units/fy9-harjoituskoe/sovella/answers.py` (also prints Osa I numbers with -v), `sovella/figures.py` (s2 FBD, s8/s9/s10 model graphs); `lessons/units/fy9-harjoituskoe/figures.py` (hero: empty exam hall, no text or people; plan).
- No exit-ticket.json (an exam has none).

## Counts
- Osa I (20 p): 4 multiple choice (FY1 sig figs, FY2 efficiency chain, FY4 ball at apex, FY7 magnet in copper tube), 3 claim + justification choices (FY3 gas pressure K vs °C, FY5 satellite speed, FY6 parallel lamp), 3 numeric (FY5 spring T 0,497 s, FY6 heater R 35,3 Ω, FY8 photon 3,06 eV) with full 8-step solutions and 3 mistakes each. No hints (exam). Correct option positions vary (2,0,1,3,3,0,2); correct option never longer than +0 % / others within 0,72–1,08.
- Osa II (7 × 15 p): s1 Kiuas ja löyly (FY3+FY2+FY6), s2 Laatikko peräkärryssä (FY4, FBD), s3 Urut kylmässä kirkossa (FY5+FY3), s4 Jatkojohto kelalla (FY6), s5 Valo uima-altaan pohjassa (FY7+FY3), s6 Järven pohjasta nostettu ruuhi (FY8+FY1, C-14), s7 Squashpallon lämpötila (experimental design; FY1+FY4).
- Osa III (3 × 20 p): s8 Putoavat kahvinsuodattimet (graph fit, model choice F ∝ v vs v²), s9 Syvälämpökaivo (short source text + data, fit, extrapolate, assess claims; FY1+FY3+FY8+FY2), s10 Jousi ja sen oma massa (T² vs m, effective spring mass).
- Total 165 p in the set; an answered exam is 20 + 4·15 + 2·20 = 120 p. 8 of 10 long tasks combine modules. Every task has skills, links, rubric, Yleisiä virheitä, Hyväksytään myös. Titles checked against all fy9-* tasks: no repeats.

## Numbers computed (answers.py)
s1 5,30 MJ, 29,4 %, 3,12 MJ; s2 4,41 m/s², 55,9 m; s3 131,0 Hz, 128,3 Hz, 0,362 mm (×75 smaller than the air effect), closed 65,5 Hz; s4 0,560 Ω, 14,27 A, 114 W, 70,4 W; s5 48,75°, 2,737 m, 1156 N; s6 1093 a, ±167 a (928–1262 a); s7 76 %, 2,66 m/s; s8 47,1 mN, k = 0,0107 kg/m (F–v line meets v axis at 0,83 m/s), v10 3,32 m/s; s9 slope 17,1 °C/km, intercept 6,7 °C, 109 °C at 6 km, 6,29 MW, 48 kg/s for 10 MW, 120 °C at 6,6 km; s10 k = 25,0 N/m, m_eff 20,5 g (61/3 = 20,3), static k 24,9 N/m. Data generated in Python with small noise (true k_air 0,0107; T = 6,5 + 17,2 z; k = 25,0, m_eff 20 g).

## Checks run
practice.py figures/check units/fy9-harjoituskoe OK (10 tasks, 165 p); units.py figures --check up to date; units.py check: no fy9-harjoituskoe errors; build.py fy9-harjoituskoe → preview; check_layout 360 OK, 1280 OK (after transposing wide tables to two/three columns and moving overlapping figure labels). Playwright 390/1280: all 7 choices answered, 3 numerics "Oikein.", all 10 "tehty" ticks, every details open: no console errors, no raw $, 0 .katex-error. Screenshots looked at: hero, Ohjeet + plan, all four model figures (fixed: plan labels too small at 390, two hidden data points, one label overlap).

## Open questions
- Exam facts (6 h, parts, points, allowed programs) are as the teacher confirmed 2026-11-04 and as fy9-koe states; not re-verified from ylioppilastutkinto.fi (blocked earlier), so unit.json has no sources and the text tells the student to check the board's rules.
- C-14 living activity 0,226 Bq/g and T½ 5730 a are literature values; ruuhi data invented (source_note says so).
- s3 sound speeds are table values for dry air (331,3 / 336,1 / 343,2 m/s); the course itself uses 340 m/s and gives no temperature formula, so the task supplies the table.

## Shared issues
- **I broke a rule once:** while debugging a section-key problem I ran `python3 -c "import build"` from scripts/, which ran the full build at 12:41 UTC and rewrote site/: tracked diffs in site/FY9.html, site/en/fy1-3.html, site/fy9-aallot.html, site/yo-sekoitin.html and new untracked site/fy9-magnetismi-valo.html, fy9-moderni.html, fy9-sahkokentta.html, fy9-tasavirta.html. My attempt to restore them from HEAD was blocked by the permission system, so they are still changed. The coordinator should restore those eight paths (e.g. `git checkout -- <files>` and delete the four new ones) before committing.
- units.py/build: a `## Title {Key}` heading whose key equals its title (`## Itsearviointi {Itsearviointi}`) is not stripped and its section key becomes "Itsearviointi {Itsearviointi}", so build crashes with KeyError while units.py check passes. Worked around by writing `## Itsearviointi`.
- Stage titles are fixed: the exam instructions and Osa I show under the stage chip "Sovella". A unit option for a custom stage title ("Koe") would read better.

## Round 1 fixes

### Science (FAIL → fixed)
1. **Blocking, s9 b) Järkevyys cites a missing source.** Fixed: solutions.md now says "Kallioperän lämpötila nousee Suomessa tyypillisesti noin 15–20 astetta kilometriä kohti, ja tulos on tällä välillä." (no reference to the tiedote).
2. **Blocking, teacher.md shorter version 80 p.** Fixed to $70$ p (20 + 2·15 + 20).
3. Polish, s3 Yleisiä virheitä "kymmenkertaiseksi". Fixed: the change becomes 261 K instead of 12 K and the result about 20-fold.
4. Polish, s5 c) missing condition. Fixed: "Valaisimen vieressä altaan pohjalla oleva sukeltaja …".
5. Polish, 75-min lessons option. Fixed: five sessions, (1) reading/choice + Osa I; (2)–(3) two Osa II tasks each; (4)–(5) one Osa III task each; choices recorded in session 1.
6. Polish, s1 d) answer.value 3,12. Not changed: the reviewer marks it optional and the Hyväksytään myös note covers 3,1 MJ; the numeric tolerance accepts both.
7. Polish, s10 e) √2. Fixed: the model answer now gives √2 ≈ 1,41 without the spring's mass and √(0,620 : 0,320) ≈ 1,39 with the d) value m_j ≈ 0,020 kg added, matching the data.

### Pedagogy (PASS)
1. Osa I all auto-checked. Not changed: Itsearviointi already states that the page checks Osa I and how to self-score; adding written items would change the inquiry types the page can check. Left for a later round if wanted.
2. s8 d) named the model. Fixed: "Määritä c-kohdan kuvaajasta valitsemasi mallin verrannollisuuskerroin $k$."
3. First choice counts. Fixed: unit.md Itsearviointi adds "Oikeassa kokeessa vastausta ei voi muuttaa palautteen nähtyään, joten älä vaihda valintaasi."
4. Osa I method point self-marked. Note only; no change.

### Visual (PASS)
1. Opened model figures at 390 px under 14 px. Not changed: shared layout (details padding / figure width) as the reviewer says; listed under Shared issues.
2. Plan figure dashes crossed "Osa II"/"Osa III". Fixed in lessons/units/fy9-harjoituskoe/figures.py: the middle dividers stop short of the label (top and bottom stubs); the Osa II quarter dividers are unchanged.
3. s10 intercept label. Fixed: the label (now 22 px) sits below the line at m ≈ 0,09 kg with a leader to the circled intercept. The old position hid the m = 0,100 kg point; all six points now show.
4. Stage chip "Sovella" / luonnos banner. Shared; already under Shared issues.
5. OSA I chip wrapping. Not changed: fold-chip CSS is shared.

Checks rerun: practice.py figures/check (OK, 10 tasks), units.py figures/check (45 units ok), build fy9-harjoituskoe, check_layout 360 and 1280 OK; Playwright at 390 and 1280 with all answers marked done and all details open: no console errors, 0 .katex-error, no raw $, no horizontal overflow. Screenshots of the plan figure and the s10 graph checked.

### Shared issues (added)
- Figures inside opened model answers render at about 0,5 scale at 390 px, so tick labels fall under 14 px; needs a template change (details padding / figure width).
- Fold-chip CSS: the "OSA I" chip wraps above the title for some cards at 390 px.

## Ratkaisutavan tarkistus (2026-11-12)
- s3 b): suhteellinen muutos ratkaistu symboleilla ($\varepsilon = v'/v - 1$), sijoitus samalla kaavalla.
- s3 c): $\Delta f/f_0 \approx -\alpha\Delta T$ johdettu kaavassa ja sijoitettu.
- s4 c): $U_\text{j} = R_\text{j} I$ (Ohmin laki) lisätty ennen $P = R I^2$.
- s9 c): $k$ ja $T_0$ määritelty kaavarivillä.
- s10 b), c): sovitteen $T^2 = am + b$ symbolit $a$, $b$ määritelty ja $m_\text{j} = b/a$ johdettu.
- Samat muutokset fi-easy- ja en-tiedostoihin. Vastaukset eivät muuttuneet.

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
