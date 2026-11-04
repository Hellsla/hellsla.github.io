# Sovella itsenäisesti FY6 (fi): developer packet

Course: FY6 Sähkö, 2 op. Content hash now: e3b0c44298fc1c14 (python scripts/practice.py hash FY6). Reports: science=missing, pedagogy=missing, visual=missing

## Scope
Central contents: jännite ja sähkövirta tasavirtapiireissä; resistanssi ja Ohmin laki; sähköteho ja Joulen laki; vastusten kytkennät ja Kirchhoffin lait; akut ja akun latauspiiri; Coulombin laki ja homogeeninen sähkökenttä; potentiaalienergia ja potentiaali homogeenisessa sähkökentässä; kondensaattori ja kondensaattorin energia; puolijohteet, diodi ja LED komponentteina virtapiirissä; sähköturvallisuus: sulake, suojausluokitus ja läpilyöntilujuus
Goals: osaa tutkia kokeellisesti sähköön liittyviä ilmiöitä ja tehdä sähköopin perusmittauksia; osaa käyttää kentän ja potentiaalin käsitteitä sähkökentän kuvaamisessa; tuntee sähkölaitteisiin ja sähköenergian siirtoon liittyviä turvallisuusnäkökohtia
Scope notes: Plan approved by the teacher 2026-11-03 (16 chapters from the LOPS FY6 contents, not from a timetable): circuit and measuring first, then Ohm, connections, Kirchhoff with potential, power and household energy, source voltage and batteries; then charge with Coulomb's law, the uniform field, potential, the capacitor; semiconductors with the solar cell, electrical safety, an applied electric-car chapter.
Scope notes: Capacitor charging and discharging only qualitatively (no exponential function); no capacitor connections (LOPS täsmennys). Semiconductors as circuit components, not materials physics.
Scope notes: FY6 builds on FY2 (energy, power, kWh) and FY4 (force, energy) without re-teaching them; vectors with an overline (\overline{E}, \overline{F}); force and field arrows in different colours, velocity, acceleration and force always in different colours (force red, velocity blue, acceleration orange as in FY4). Conventional current direction from + to −; electron flow named separately where it matters.
Scope notes: Circuit diagrams use the IEC symbols of Finnish textbooks (resistor a rectangle); every label in them LaTeX. Division written with a colon in prose (U : I), \frac in display formulas.
Chapters (link targets, by id): fy6-1 Virtapiiri, sähkövirta ja jännite; fy6-2 Mittaukset virtapiirissä; fy6-3 Resistanssi ja Ohmin laki; fy6-4 Vastusten sarja- ja rinnankytkennät; fy6-5 Kirchhoffin lait ja potentiaali virtapiirissä; fy6-6 Sähköteho ja vastuksen lämpeneminen; fy6-7 Sähköenergia kotona; fy6-8 Lähdejännite ja sisäinen resistanssi; fy6-9 Akut ja latauspiiri; fy6-10 Sähkövaraus ja Coulombin laki; fy6-11 Homogeeninen sähkökenttä; fy6-12 Potentiaalienergia ja potentiaali sähkökentässä; fy6-13 Kondensaattori ja sen energia; fy6-14 Puolijohteet, diodi, LED ja aurinkokenno; fy6-15 Sähköturvallisuus kotona ja työssä; fy6-16 Soveltava luku: sähköauto ja kodin sähköjärjestelmä

## Framework (competencies.json, NOTES.md §9)
- concept: conceptual understanding: recognise phenomena, explain principles and relationships, correct misconceptions (Käsitteellinen ymmärrys)
- math: mathematical problem-solving: formulate and manipulate equations, units, precision, reasonableness (Matemaattinen ratkaisu)
- graph: graphical and numerical analysis: build a graph from data, axes and units, points, choose a fit, read quantities, model validity, interpolate and extrapolate, scatter (Kuvaajat ja aineiston analyysi)
- experiment: experimental reasoning: design, variables and controls, methods, systematic and random errors, reliability, shortcomings of a report (Kokeellinen päättely)
- communication: scientific communication: clear explanations, justified assumptions and models, complete solutions, interpreted results (Fysikaalinen selittäminen)
- transfer: independent transfer: unfamiliar context, relevant information, choose the model and strategy without being told the formula (Mallin valinta ja soveltaminen)

## Shared criteria (lang "criteria"; use the key, add `detail` for the task's specifics)
- graph_axes [graph]: Akseleilla ovat oikeat suureet ja yksiköt, ja asteikot ovat tasavälisiä.
- graph_points [graph]: Jokainen mittaus on merkitty erillisenä pisteenä oikealle paikalleen.
- graph_fit [graph]: Malli on sovitettu niihin pisteisiin, joihin se sopii, eikä pisteitä ole yhdistetty murtoviivaksi.
- graph_read [graph]: Kulmakerroin tai muu suure on luettu kuvaajalta näkyvästi, kahdesta kaukana toisistaan olevasta suoran pisteestä.
- equation [math]: Lähtöyhtälö on oikea, ja kysytty suure on ratkaistu siitä ennen lukuarvojen sijoittamista.
- calculation [math]: Lukuarvot on sijoitettu yksiköineen, ja lasku on oikein.
- units_precision [math]: Vastauksessa on oikea yksikkö ja lähtötietoja vastaava tarkkuus.
- reasonableness [math]: Tuloksen järkevyys on arvioitu.
- uncertainty [experiment]: Mittauksen epävarmuus on arvioitu.
- error_sources [experiment]: Tärkeimmät virhelähteet on nimetty ja kerrottu, miten ne vaikuttavat tulokseen.
- assumptions [transfer]: Oletus on nimetty, ja sen vaikutus tulokseen on perusteltu.
- conclusion [communication]: Johtopäätös vastaa kysymykseen ja perustuu aineistoon.
- fbd_object [concept]: Kappale on valittu selvästi, ja kuvioon on piirretty vain siihen kohdistuvat voimat.
- fbd_forces [concept]: Kaikki kappaleeseen vaikuttavat voimat ovat mukana, eikä kuviossa ole keksittyjä voimia.
- fbd_directions [concept]: Jokainen voima osoittaa fysikaalisesti oikeaan suuntaan.
- fbd_representation [communication]: Voimanuolet lähtevät kappaleesta järkevästä kohdasta, ja jokaisella voimalla on oma yksiselitteinen nimi.
- fbd_magnitudes [concept]: Nuolten pituudet ovat oikeassa suhteessa, kun suuruudet tiedetään, eikä voimia ole sekoitettu komponentteihin, nopeuteen tai kiihtyvyyteen.
- fbd_equations [math]: Liikeyhtälöt on muodostettu voimakuviosta: akselit ja positiivinen suunta on valittu, ja etumerkit ovat oikein.

## Deterministic checks
content/fi/FY6/sovella/tasks.json: [Errno 2] No such file or directory: '/home/user/hellsla.github.io/fysiikkalabra/content/fi/FY6/sovella/tasks.json'

## answers.py output
lessons/FY6/sovella/answers.py missing

## Your job
Write or fix tasks.json, solutions.md, answers.py and figures.py (schema and rules: README "Sovella itsenäisesti", NOTES.md §9). Run `python scripts/practice.py figures FY6` and `python scripts/practice.py check FY6` until OK, then `python scripts/build.py FY6-sovella` and `python scripts/check_layout.py FY6-sovella --width 360` (and 768, 1280).
