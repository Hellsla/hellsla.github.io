# Sovella itsenäisesti FY6 (fi): pedagogy packet

Course: FY6 Sähkö, 2 op. Content hash now: b1e8c35e57ad6a01 (python scripts/practice.py hash FY6). Reports: science=stale, pedagogy=stale, visual=stale

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
practice.py check: OK

## answers.py output
{"fy6-s1-fit-slope": -1.1943, "fy6-s1-fit-icpt": 4.598, "fy6-s1-slope": -1.2, "fy6-s1-b-E": 4.6, "fy6-s1-b-Rs": 1.2, "fy6-s1-Ik": 3.833, "fy6-s1-c-P": 2.0, "fy6-s1-c-I": 0.5, "fy6-s1-c-Pbatt": 0.3, "fy6-s1-c-osuus": 13.04, "fy6-s1-c-U": 4.0, "fy6-s1-d-dRs": 0.08, "fy6-s1-d-maxres": 0.02, "fy6-s2-RA": 6.0, "fy6-s2-RB": 12.0, "fy6-s2-Rp": 4.0, "fy6-s2-Rtot": 4.8, "fy6-s2-a": 2.5, "fy6-s2-a-UL": 10.0, "fy6-s2-b": 16.667, "fy6-s2-b-PB": 8.333, "fy6-s2-b-Pc": 5.0, "fy6-s2-b-Pbatt": 30.0, "fy6-s2-b-eff": 0.8333, "fy6-s2-c-I": 1.7647, "fy6-s2-c-UA": 10.5882, "fy6-s2-c-PA": 18.685, "fy6-s2-c-Pc": 2.491, "fy6-s2-c-Ucable": 1.412, "fy6-s2-c-Ucable0": 2.0, "fy6-s2-RC": 4.0, "fy6-s2-d-Rp": 2.0, "fy6-s2-d": 4.2857, "fy6-s2-d-UL": 8.571, "fy6-s2-d-PC": 18.367, "fy6-s2-d-Pc": 14.694, "fy6-s3-a-E": 300000, "fy6-s3-a": 1.8e-07, "fy6-s3-a-G": 3.924e-09, "fy6-s3-a-ratio": 45.87, "fy6-s3-a-Eair": 0.1, "fy6-s3-a-acc": 450.0, "fy6-s3-b": 13.416, "fy6-s3-b-W": 3.6e-08, "fy6-s3-b-Wg": 7.848e-10, "fy6-s3-c-Ek": 5e-09, "fy6-s3-c-share": 0.1389, "fy6-s3-c-rest": 3.1e-08, "fy6-s3-d": 3.2356799999999993e-09, "fy6-s3-d-vsF": 0.018, "fy6-s3-d-vsG": 0.825, "fy6-s4-a": 14.85, "fy6-s4-b": 6.864, "fy6-s4-b-Eb": 7.986, "fy6-s4-b-share": 0.4622, "fy6-s4-c": 26.4, "fy6-s4-c-dQ": 26.4, "fy6-s4-c-P": 6864.0, "fy6-s4-Qa": 0.099, "fy6-s4-d-I": 0.3, "fy6-s4-d-Ires": 30.0}

## Your job
Judge the files below as the pedagogy reviewer (.claude/agents/pedagogy-reviewer.md, "Sovella itsenäisesti"). Write content/fi/FY6/sovella/review/pedagogy.md: line 1 `VERDICT: PASS|FAIL`, line 2 `CONTENT-HASH: b1e8c35e57ad6a01`, then Blocking, Polish, Checked (under 400 words).

## content/fi/FY6/sovella/tasks.json
```
{
  "intro": "Neljä tehtävää kokoaa moduulin: pariston mittauksen, virtapiirin, sähkökentän ja kondensaattorin. Jokaisessa päätät itse, mitkä mallit tilanteeseen sopivat, ja perustelet valintasi.",
  "tasks": [
    {
      "id": "fy6-s1",
      "title": "Taskulampun paristo",
      "source": "example",
      "source_note": "Mittaustulokset on laadittu tehtävää varten, mutta ne ovat samaa suuruusluokkaa kuin uuden litteän taskulamppupariston mittauksessa.",
      "text": "Oppilas tutkii uutta litteää taskulamppuparistoa, jonka kyljessä lukee $4{,}5\\,\\text{V}$. Hän kytkee paristoon säädettävän vastuksen ja ampeerimittarin sekä jännitemittarin suoraan pariston napoihin (kuva). Hän säätää vastuksesta virran ja lukee sitä vastaavan napajännitteen $U$. Mittarit näyttävät virran $0{,}01\\,\\text{A}$:n ja jännitteen $0{,}01\\,\\text{V}$:n tarkkuudella. Oppilas mittasi virran kasvavassa järjestyksessä, ja piiri oli kytkettynä kunkin lukeman ajan noin minuutin. Paristo lämpeni mittausten aikana hieman, ja jännite näytti laskevan hitaasti myös silloin, kun virtaa ei muutettu. Sarjan jälkeen oppilas mittasi jännitteen vielä kerran virralla $0{,}10\\,\\text{A}$: lukema oli $4{,}45\\,\\text{V}$ eli $0{,}03\\,\\text{V}$ pienempi kuin sarjan alussa.\n\nMittaustulokset (virta $I$, napajännite $U$):\n\n- $I = 0{,}10\\,\\text{A}$, $U = 4{,}48\\,\\text{V}$\n- $I = 0{,}20\\,\\text{A}$, $U = 4{,}37\\,\\text{V}$\n- $I = 0{,}30\\,\\text{A}$, $U = 4{,}22\\,\\text{V}$\n- $I = 0{,}40\\,\\text{A}$, $U = 4{,}13\\,\\text{V}$\n- $I = 0{,}50\\,\\text{A}$, $U = 3{,}99\\,\\text{V}$\n- $I = 0{,}60\\,\\text{A}$, $U = 3{,}89\\,\\text{V}$",
      "figure": "fy6-sovella/fy6-s1-circuit",
      "parts": [
        {
          "id": "a",
          "kind": "graph",
          "points": 4,
          "text": "Oppilas haluaa selvittää, millaisena jännitelähteenä paristo toimii. Mallinna paristoa ja muodosta aineistosta kuvaaja, jonka pisteisiin mallin mukaan sopii suora.",
          "criteria": [
            {
              "text": "Mallintaa pariston ideaaliseksi jännitelähteeksi ja sen kanssa sarjassa olevaksi sisäiseksi resistanssiksi, jolloin napajännite on $U = E - R_\\text{s} I$, ja valitsee kuvaajan suureiksi $I$ ja $U$.",
              "tag": "transfer",
              "points": 1
            },
            {
              "key": "graph_axes",
              "points": 1,
              "detail": "$I\\ (\\text{A})$ vaaka-akselilla ja $U\\ (\\text{V})$ pystyakselilla; pystyakselin ei tarvitse alkaa nollasta, jos asteikko on merkitty."
            },
            {
              "key": "graph_points",
              "points": 1
            },
            {
              "key": "graph_fit",
              "points": 1,
              "detail": "Suora kulkee pisteiden lomitse ja sitä on jatkettu pystyakselille asti."
            }
          ]
        },
        {
          "id": "b",
          "kind": "calc",
          "points": 4,
          "text": "Määritä kuvaajasta pariston lähdejännite $E$ ja sisäinen resistanssi $R_\\text{s}$.",
          "answer": [
            {
              "name": "E",
              "value": 4.6,
              "unit": "V",
              "tolerance": 0.03
            },
            {
              "name": "Rs",
              "value": 1.2,
              "unit": "Ω",
              "tolerance": 0.09
            }
          ],
          "criteria": [
            {
              "key": "graph_read",
              "points": 1,
              "detail": "Kulmakerroin $\\dfrac{\\Delta U}{\\Delta I} \\approx -1{,}2\\,\\text{V/A}$ on luettu piirretyn suoran kahdesta kaukana toisistaan olevasta pisteestä, esimerkiksi $(0{,}10\\,\\text{A};\\ 4{,}48\\,\\text{V})$ ja $(0{,}60\\,\\text{A};\\ 3{,}88\\,\\text{V})$, ei vierekkäisistä mittauspisteistä."
            },
            {
              "key": "equation",
              "points": 1,
              "detail": "$U = E - R_\\text{s} I$: $E$ on suoran ja pystyakselin leikkauskohta ($I = 0$) ja $R_\\text{s}$ kulmakertoimen vastaluku."
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "$R_\\text{s} = \\dfrac{0{,}60\\,\\text{V}}{0{,}50\\,\\text{A}}$ ja $E = 4{,}48\\,\\text{V} + R_\\text{s} \\cdot 0{,}10\\,\\text{A}$ tai leikkauskohta luettuna suoralta."
            },
            {
              "key": "units_precision",
              "points": 1,
              "detail": "$E \\approx 4{,}6\\,\\text{V}$ ja $R_\\text{s} \\approx 1{,}2\\,\\Omega$"
            }
          ]
        },
        {
          "id": "c",
          "kind": "calc",
          "points": 3,
          "text": "Paristoon kytketään $8{,}0\\,\\Omega$:n vastus. Kuinka suuri teho vastukseen siirtyy, ja kuinka suuri osa pariston koko sähkötehosta siirtyy lämpönä pariston sisäisessä resistanssissa?",
          "answer": [
            {
              "name": "P",
              "value": 2.0,
              "unit": "W",
              "tolerance": 0.03
            },
            {
              "name": "osuus",
              "value": 13,
              "unit": "%",
              "tolerance": 0.05
            }
          ],
          "criteria": [
            {
              "key": "equation",
              "points": 1,
              "detail": "$I = \\dfrac{E}{R + R_\\text{s}}$, vastuksen teho $P = R I^2$ ja pariston sisällä $P_\\text{s} = R_\\text{s} I^2$; osuus on $\\dfrac{P_\\text{s}}{P + P_\\text{s}}$."
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "$I = 0{,}50\\,\\text{A}$, $P = 2{,}0\\,\\text{W}$ ja $P_\\text{s} = 0{,}30\\,\\text{W}$."
            },
            {
              "key": "units_precision",
              "points": 1,
              "detail": "$P \\approx 2{,}0\\,\\text{W}$ ja osuus noin $13\\,\\%$"
            }
          ]
        },
        {
          "id": "d",
          "kind": "word",
          "points": 4,
          "text": "Arvioi, miten pariston purkautuminen ja lämpeneminen vaikuttavat b-kohdan tulokseen. Arvioi myös, kuinka paljon pisteiden hajonta jättää $R_\\text{s}$:n arvoon epävarmuutta (pisteet poikkeavat sovitetusta suorasta enintään $0{,}02\\,\\text{V}$), ja ehdota mittaukseen parannus.",
          "criteria": [
            {
              "key": "error_sources",
              "points": 1,
              "detail": "Pariston purkautuminen laskee jännitettä sarjan aikana, joten myöhemmin mitatut jännitteet (suuremmat virrat) ovat liian pieniä: suora on liian jyrkkä ja $R_\\text{s}$ tulee liian suureksi (systemaattinen virhe). Koska virtaa kasvatettiin vain yhteen suuntaan, ajan vaikutus sekoittuu kulmakertoimeen. Lämpeneminen muuttaa myös $R_\\text{s}$:ää mittauksen aikana (yleensä pienentää sitä), joten sen suunta on epävarma."
            },
            {
              "key": "uncertainty",
              "points": 1,
              "detail": "Ääriviivojen kulmakertoimet poikkeavat toisistaan $\\dfrac{2 \\cdot 0{,}02\\,\\text{V}}{0{,}50\\,\\text{A}} = 0{,}08\\,\\Omega$, joten $R_\\text{s} = (1{,}20 \\pm 0{,}08)\\,\\Omega$ pelkän hajonnan perusteella."
            },
            {
              "text": "Ehdottaa parannuksen, joka vähentää purkautumisen vaikutusta: virrat satunnaisessa järjestyksessä, piiri kytkettynä vain lukeman ajan tai sarja toistettuna käänteisessä järjestyksessä ja tulosten vertailu.",
              "tag": "experiment",
              "points": 1
            },
            {
              "key": "conclusion",
              "points": 1,
              "detail": "Arvioi ajautuman vaikutuksen: jännite laski sarjan aikana noin $0{,}03\\,\\text{V}$, joten kulmakerroin on enintään noin $\\dfrac{0{,}03\\,\\text{V}}{0{,}50\\,\\text{A}} = 0{,}06\\,\\Omega$ liian suuri. Se on samaa suuruusluokkaa kuin hajonnan $0{,}08\\,\\Omega$, joten $R_\\text{s}$ on noin $1{,}1\\ldots1{,}2\\,\\Omega$ ja arvo $1{,}2\\,\\Omega$ on pikemmin yläraja."
            }
          ]
        }
      ],
      "links": {
        "transfer": "fy6-8",
        "math": "fy6-8",
        "graph": "fy6-8",
        "experiment": "fy6-2",
        "communication": "fy6-8"
      }
    },
    {
      "id": "fy6-s2",
      "title": "Mökin pihavalot",
      "source": "example",
      "source_note": "Kaapelin resistanssi ja lamppujen tiedot ovat keksittyjä, mutta samaa suuruusluokkaa kuin 12 voltin mökkisähköjärjestelmässä.",
      "text": "Mökin pihavalot saavat sähkönsä $12{,}0\\,\\text{V}$:n akustosta. Akustolta lamppuihin johtaa pitkä kaapeli, jonka molempien johtimien yhteinen resistanssi on $0{,}80\\,\\Omega$. Piirissä on akuston jälkeen sulake. Kaapelin päässä on kaksi rinnan kytkettyä lamppua (kuva). Lamppu A on merkitty $12\\,\\text{V},\\ 24\\,\\text{W}$ ja lamppu B $12\\,\\text{V},\\ 12\\,\\text{W}$: merkintä kertoo tehon, kun lamppuun kytketään nimellisjännite. Oleta lamppujen resistanssit vakioiksi. Akuston sisäinen resistanssi on niin pieni, että sen voi jättää huomiotta.\n\nMuita tietoja:\n\n- sulakkeen nimellisvirta on $3{,}15\\,\\text{A}$\n- kaapeli kestää pitkäaikaisesti enintään $4{,}0\\,\\text{A}$ virran",
      "figure": "fy6-sovella/fy6-s2-circuit",
      "parts": [
        {
          "id": "a",
          "kind": "calc",
          "points": 4,
          "text": "Kuinka suuri virta kulkee akustosta, kun molemmat lamput palavat?",
          "answer": {
            "value": 2.5,
            "unit": "A",
            "tolerance": 0.03
          },
          "criteria": [
            {
              "text": "Hahmottaa piirin: kaapeli on sarjassa rinnankytkettyjen lamppujen kanssa, ja laskee lamppujen resistanssit nimellisarvoista, esimerkiksi $R = \\dfrac{U^2}{P}$: $R_\\text{A} = 6{,}0\\,\\Omega$ ja $R_\\text{B} = 12\\,\\Omega$.",
              "tag": "transfer",
              "points": 1
            },
            {
              "key": "equation",
              "points": 1,
              "detail": "$\\dfrac{1}{R_\\text{r}} = \\dfrac{1}{R_\\text{A}} + \\dfrac{1}{R_\\text{B}}$, $R = R_\\text{k} + R_\\text{r}$ ja $I = \\dfrac{E}{R}$ ratkaistuna ennen lukuarvoja."
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "$R_\\text{r} = 4{,}0\\,\\Omega$ ja $R = 4{,}8\\,\\Omega$."
            },
            {
              "key": "units_precision",
              "points": 1,
              "detail": "$I = 2{,}5\\,\\text{A}$"
            }
          ]
        },
        {
          "id": "b",
          "kind": "calc",
          "points": 3,
          "text": "Kuinka suuri teho lamppuun A todellisuudessa siirtyy? Vertaa tulosta lampun nimellistehoon.",
          "answer": {
            "value": 16.7,
            "unit": "W",
            "tolerance": 0.03
          },
          "criteria": [
            {
              "key": "equation",
              "points": 1,
              "detail": "Silmukkasääntö $E - R_\\text{k} I - U_\\text{L} = 0$ antaa lamppujen jännitteen $U_\\text{L} = E - R_\\text{k} I$; lampun teho $P = \\dfrac{U_\\text{L}^2}{R_\\text{A}}$."
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "$U_\\text{L} = 12{,}0\\,\\text{V} - 0{,}80\\,\\Omega \\cdot 2{,}5\\,\\text{A} = 10{,}0\\,\\text{V}$ ja $P_\\text{A} = \\dfrac{(10{,}0\\,\\text{V})^2}{6{,}0\\,\\Omega} = 16{,}7\\,\\text{W}$."
            },
            {
              "key": "reasonableness",
              "points": 1,
              "detail": "$17\\,\\text{W}$ on vähemmän kuin nimellinen $24\\,\\text{W}$, koska kaapelin jännitehäviö jättää lampulle alle $12\\,\\text{V}$. Tarkistus: akuston teho $30\\,\\text{W}$ on $16{,}7\\,\\text{W} + 8{,}3\\,\\text{W} + 5{,}0\\,\\text{W}$."
            }
          ]
        },
        {
          "id": "c",
          "kind": "word",
          "points": 4,
          "text": "Lamppu B palaa loppuun, eikä se enää johda virtaa. Miten lampun A kirkkaus, akuston virta ja kaapelin lämpeneminen muuttuvat? Perustele, ja tarkista perustelusi laskemalla lampun A teho.",
          "criteria": [
            {
              "text": "Päättelee, että kokonaisresistanssi kasvaa, kun toinen rinnakkainen haara poistuu, joten akuston virta pienenee: $I = \\dfrac{12{,}0\\,\\text{V}}{6{,}8\\,\\Omega} \\approx 1{,}8\\,\\text{A}$.",
              "tag": "concept",
              "points": 1
            },
            {
              "text": "Perustelee, että pienempi virta pienentää jännitehäviötä kaapelissa ($R_\\text{k} I$ pienenee), jolloin lampulle A jää suurempi jännite ja se palaa kirkkaammin, ja että kaapeliin siirtyvä teho $R_\\text{k} I^2$ pienenee noin $5{,}0\\,\\text{W}$:sta $2{,}5\\,\\text{W}$:iin, joten kaapeli lämpenee vähemmän.",
              "tag": "concept",
              "points": 1
            },
            {
              "text": "Laskee lampun A tehon: $U_\\text{A} \\approx 10{,}6\\,\\text{V}$ ja $P_\\text{A} \\approx 18{,}7\\,\\text{W}$, aiemmin $16{,}7\\,\\text{W}$.",
              "tag": "math",
              "points": 1
            },
            {
              "key": "conclusion",
              "points": 1,
              "detail": "Toteaa, että rinnankytketyt lamput eivät ole täysin toisistaan riippumattomia, kun kaapelilla on resistanssi: jos kaapelin resistanssi olisi nolla, lampun A kirkkaus ei muuttuisi."
            }
          ]
        },
        {
          "id": "d",
          "kind": "calc",
          "points": 4,
          "text": "Omistaja lisää piiriin rinnan kolmannen lampun C, joka on merkitty $12\\,\\text{V},\\ 36\\,\\text{W}$. Kuinka suuri virta akustosta tulee nyt kulkemaan? Mitä sulakkeelle tapahtuu, ja miksi sulakkeen nimellisvirta on valittu kaapelin mukaan? Laske myös lamppujen jännite.",
          "answer": {
            "value": 4.3,
            "unit": "A",
            "tolerance": 0.03
          },
          "criteria": [
            {
              "key": "equation",
              "points": 1,
              "detail": "Kolme rinnakkaista lamppua: $\\dfrac{1}{R_\\text{r}} = \\dfrac{1}{R_\\text{A}} + \\dfrac{1}{R_\\text{B}} + \\dfrac{1}{R_\\text{C}}$ ja $I = \\dfrac{E}{R_\\text{k} + R_\\text{r}}$."
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "$R_\\text{C} = \\dfrac{(12\\,\\text{V})^2}{36\\,\\text{W}} = 4{,}0\\,\\Omega$, $R_\\text{r} = 2{,}0\\,\\Omega$ ja $I = \\dfrac{12{,}0\\,\\text{V}}{2{,}8\\,\\Omega} = 4{,}3\\,\\text{A}$."
            },
            {
              "key": "conclusion",
              "points": 1,
              "detail": "Virta $4{,}3\\,\\text{A}$ ylittää sulakkeen $3{,}15\\,\\text{A}$ ja kaapelin sallitun $4{,}0\\,\\text{A}$, joten sulake todennäköisesti palaa ylivirran jatkuessa ja katkaisee piirin; sulakkeen toiminta-aika on yksinkertaistettu, sillä pieni ylivirta voi kestää hetken. Sulake mitoitetaan suojaamaan heikointa osaa eli kaapelia, joten sen nimellisvirta on kaapelin sallittua virtaa pienempi."
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "Lamppujen jännite on $R_\\text{r} I = 2{,}0\\,\\Omega \\cdot 4{,}3\\,\\text{A} \\approx 8{,}6\\,\\text{V}$, joten lamput palavat himmeämmin kuin $10{,}0\\,\\text{V}$:n jännitteellä."
            }
          ]
        }
      ],
      "links": {
        "transfer": "fy6-4",
        "math": "fy6-5",
        "concept": "fy6-6",
        "communication": "fy6-5"
      }
    },
    {
      "id": "fy6-s3",
      "title": "Ruiskumaalaus",
      "source": "example",
      "source_note": "Suuruusluokat ovat samaa luokkaa kuin teollisessa sähköstaattisessa ruiskumaalauksessa, mutta tehtävän arvot on pyöristetty ja yksinkertaistettu.",
      "text": "Autonosa maalataan sähköstaattisella ruiskulla. Suutinlevyn potentiaali on $+60\\,\\text{kV}$ ja maadoitettu työkappale on $20\\,\\text{cm}$:n päässä. Suuttimesta lähtevät maalipisarat saavat positiivisen varauksen, ja ne kulkevat työkappaletta kohti. Oletetaan, että suutinlevyn ja työkappaleen välinen sähkökenttä on homogeeninen (kuva).\n\nYksi maalipisara:\n\n- massa $4{,}0 \\cdot 10^{-10}\\,\\text{kg}$\n- varaus $q = +6{,}0 \\cdot 10^{-13}\\,\\text{C}$\n- lähtee levossa suutinlevyltä\n\nMuita tietoja: ilman läpilyöntilujuus on noin $3\\,\\text{MV/m}$, putoamiskiihtyvyys $9{,}81\\,\\text{m/s}^2$ ja Coulombin lain vakio $k = 8{,}988 \\cdot 10^{9}\\,\\tfrac{\\text{N}\\cdot\\text{m}^2}{\\text{C}^2}$.",
      "figure": "fy6-sovella/fy6-s3-field",
      "parts": [
        {
          "id": "a",
          "kind": "calc",
          "points": 4,
          "text": "Kuinka suuri sähkövoima pisaraan vaikuttaa? Onko pisaran painon huomiotta jättäminen perusteltua, ja syntyykö kenttään kipinöintiä?",
          "answer": {
            "value": 1.8e-07,
            "unit": "N",
            "tolerance": 0.03
          },
          "criteria": [
            {
              "key": "equation",
              "points": 1,
              "detail": "Homogeenisessa kentässä $E = \\dfrac{U}{d}$ ja pisaraan vaikuttaa voima $F = qE$."
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "$E = \\dfrac{60\\,000\\,\\text{V}}{0{,}20\\,\\text{m}} = 3{,}0 \\cdot 10^{5}\\,\\text{V/m}$"
            },
            {
              "key": "units_precision",
              "points": 1,
              "detail": "$F \\approx 1{,}8 \\cdot 10^{-7}\\,\\text{N}$"
            },
            {
              "key": "reasonableness",
              "points": 1,
              "detail": "Paino $mg \\approx 3{,}9 \\cdot 10^{-9}\\,\\text{N}$ on vain noin $2\\,\\%$ sähkövoimasta, joten sen voi jättää huomiotta. Kenttä on noin kymmenesosa ilman läpilyöntilujuudesta, joten kipinöintiä ei synny."
            }
          ]
        },
        {
          "id": "b",
          "kind": "calc",
          "points": 4,
          "text": "Kuinka suurella nopeudella pisara osuu työkappaleeseen, kun ilmanvastusta ei oteta huomioon?",
          "answer": {
            "value": 13.4,
            "unit": "m/s",
            "tolerance": 0.03
          },
          "criteria": [
            {
              "text": "Valitsee energiaperiaatteen: sähkökentän tekemä työ $qU$ kasvattaa pisaran liike-energiaa, kun paino ja ilmanvastus jätetään pois; kentän voimakkuutta tai kiihtyvyyttä ei tarvita.",
              "tag": "transfer",
              "points": 1
            },
            {
              "key": "equation",
              "points": 1,
              "detail": "$q U = \\dfrac{1}{2} m v^2$, josta $v = \\sqrt{\\dfrac{2 q U}{m}}$; $U$ on suutinlevyn ja työkappaleen potentiaaliero."
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "$qU = 6{,}0 \\cdot 10^{-13}\\,\\text{C} \\cdot 6{,}0 \\cdot 10^{4}\\,\\text{V} = 3{,}6 \\cdot 10^{-8}\\,\\text{J}$ ja $v = \\sqrt{\\dfrac{2 \\cdot 3{,}6 \\cdot 10^{-8}\\,\\text{J}}{4{,}0 \\cdot 10^{-10}\\,\\text{kg}}}$."
            },
            {
              "key": "units_precision",
              "points": 1,
              "detail": "$v \\approx 13\\,\\text{m/s}$"
            }
          ]
        },
        {
          "id": "c",
          "kind": "word",
          "points": 4,
          "text": "Mittauksessa pisaroiden osumanopeudeksi saadaan noin $5{,}0\\,\\text{m/s}$. Selitä, miksi se on paljon pienempi kuin b-kohdan tulos, ja päättele, minne sähkökentän tekemä työ jää.",
          "criteria": [
            {
              "text": "Tunnistaa, että b-kohdan malli jätti ilmanvastuksen pois: ilma vastustaa pisaran liikettä, ja nopeuden kasvaessa ilmanvastus kasvaa, kunnes se on likimain yhtä suuri kuin sähkövoima.",
              "tag": "concept",
              "points": 1
            },
            {
              "text": "Laskee todellisen liike-energian $\\dfrac{1}{2} m v^2 = 5{,}0 \\cdot 10^{-9}\\,\\text{J}$ ja vertaa sitä kentän tekemään työhön $3{,}6 \\cdot 10^{-8}\\,\\text{J}$: se on vain noin $14\\,\\%$.",
              "tag": "math",
              "points": 1
            },
            {
              "text": "Päättelee, että loput noin $3{,}1 \\cdot 10^{-8}\\,\\text{J}$ siirtyy ilmaan: ilman sisäenergia kasvaa ja energia siirtyy edelleen lämpönä ympäristöön. Energia ei häviä.",
              "tag": "concept",
              "points": 1
            },
            {
              "key": "conclusion",
              "points": 1,
              "detail": "Päättelee, että b-kohdan tulos on ilmanvastuksen puuttuessa suurin mahdollinen nopeus (yläraja) ja että energia ei häviä vaan siirtyy ilmaan."
            }
          ]
        },
        {
          "id": "d",
          "kind": "calc",
          "points": 4,
          "text": "Kaksi vierekkäistä pisaraa on $1{,}0\\,\\text{mm}$:n päässä toisistaan, ja kummankin varaus on $+6{,}0 \\cdot 10^{-13}\\,\\text{C}$. Kuinka suuri voima pisaroiden välillä on? Mitä tulos kertoo pisarapilven käyttäytymisestä?",
          "answer": {
            "value": 3.2e-09,
            "unit": "N",
            "tolerance": 0.03
          },
          "criteria": [
            {
              "key": "equation",
              "points": 1,
              "detail": "Coulombin laki pistemäisille varauksille: $F = k\\dfrac{q_1 q_2}{r^2}$."
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "Muunnos $1{,}0\\,\\text{mm} = 1{,}0 \\cdot 10^{-3}\\,\\text{m}$; $F = 8{,}988 \\cdot 10^{9}\\,\\tfrac{\\text{N}\\cdot\\text{m}^2}{\\text{C}^2} \\cdot \\dfrac{(6{,}0 \\cdot 10^{-13}\\,\\text{C})^2}{(1{,}0 \\cdot 10^{-3}\\,\\text{m})^2}$."
            },
            {
              "key": "units_precision",
              "points": 1,
              "detail": "$F \\approx 3{,}2 \\cdot 10^{-9}\\,\\text{N}$"
            },
            {
              "key": "conclusion",
              "points": 1,
              "detail": "Samanmerkkiset varaukset hylkivät toisiaan, joten pisarapilvi levenee sivusuunnassa. Voima on noin $2\\,\\%$ kentän voimasta mutta lähes saman suuruinen kuin pisaran paino ($0{,}8$-kertainen), joten pisarat kulkevat silti kohti työkappaletta mutta leviävät."
            }
          ]
        }
      ],
      "links": {
        "transfer": "fy6-12",
        "math": "fy6-11",
        "concept": "fy6-11",
        "communication": "fy6-10"
      }
    },
    {
      "id": "fy6-s4",
      "title": "Kameran salama",
      "source": "example",
      "source_note": "Kondensaattorin arvot ovat samaa suuruusluokkaa kuin kameran salamalaitteessa, mutta ne on valittu tehtävää varten.",
      "text": "Kameran salamalaitteessa pieni paristo lataa kondensaattorin jännitettä nostavan piirin avulla jännitteeseen $300\\,\\text{V}$. Kondensaattorin kapasitanssi on $330\\,\\mu\\text{F}$. Kun salama välähtää, kondensaattori purkautuu salamaputken kautta noin $1{,}0\\,\\text{ms}$:ssa, ja sen jännite laskee arvoon $220\\,\\text{V}$. Salamaan siirtynyt energia lähtee laitteesta valona ja lämpönä.",
      "parts": [
        {
          "id": "a",
          "kind": "calc",
          "points": 3,
          "text": "Kuinka suuri energia on varastoituneena kondensaattoriin ennen salamaa?",
          "answer": {
            "value": 14.85,
            "unit": "J",
            "tolerance": 0.02
          },
          "criteria": [
            {
              "key": "equation",
              "points": 1,
              "detail": "Kondensaattorin energia $E = \\dfrac{1}{2} C U^2$."
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "Muunnos $330\\,\\mu\\text{F} = 330 \\cdot 10^{-6}\\,\\text{F}$; $E = \\dfrac{1}{2} \\cdot 330 \\cdot 10^{-6}\\,\\text{F} \\cdot (300\\,\\text{V})^2$."
            },
            {
              "key": "units_precision",
              "points": 1,
              "detail": "$E \\approx 15\\,\\text{J}$"
            }
          ]
        },
        {
          "id": "b",
          "kind": "calc",
          "points": 4,
          "text": "Kuinka suuri energia siirtyi salamaan? Kuinka suuri osa varastoidusta energiasta tämä on, ja miksi osuus on suurempi kuin jännitteen pieneneminen?",
          "answer": {
            "value": 6.86,
            "unit": "J",
            "tolerance": 0.03
          },
          "criteria": [
            {
              "text": "Päättelee, että salamaan siirtynyt energia on kondensaattorin energian muutos: energiat lasketaan erikseen ennen ja jälkeen eikä jännitteen muutoksella $\\Delta U$ yksin.",
              "tag": "transfer",
              "points": 1
            },
            {
              "key": "equation",
              "points": 1,
              "detail": "$\\Delta E = \\dfrac{1}{2} C U_1^2 - \\dfrac{1}{2} C U_2^2$"
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "$E_2 = \\dfrac{1}{2} \\cdot 330 \\cdot 10^{-6}\\,\\text{F} \\cdot (220\\,\\text{V})^2 = 7{,}99\\,\\text{J}$ ja $\\Delta E = 14{,}85\\,\\text{J} - 7{,}99\\,\\text{J} = 6{,}9\\,\\text{J}$."
            },
            {
              "key": "reasonableness",
              "points": 1,
              "detail": "Osuus on noin $46\\,\\%$, vaikka jännite pieneni vain noin $27\\,\\%$, koska energia riippuu jännitteen neliöstä: $1 - \\left(\\dfrac{220}{300}\\right)^2 \\approx 0{,}46$."
            }
          ]
        },
        {
          "id": "c",
          "kind": "calc",
          "points": 3,
          "text": "Kuinka suuri on kondensaattorista salaman aikana kulkenut keskimääräinen virta?",
          "answer": {
            "value": 26.4,
            "unit": "A",
            "tolerance": 0.03
          },
          "criteria": [
            {
              "key": "equation",
              "points": 1,
              "detail": "$I = \\dfrac{\\Delta Q}{\\Delta t}$, missä siirtynyt varaus $\\Delta Q = C\\,\\Delta U$."
            },
            {
              "key": "calculation",
              "points": 1,
              "detail": "$\\Delta Q = 330 \\cdot 10^{-6}\\,\\text{F} \\cdot 80\\,\\text{V} = 0{,}0264\\,\\text{C}$ ja $\\Delta t = 1{,}0 \\cdot 10^{-3}\\,\\text{s}$."
            },
            {
              "key": "reasonableness",
              "points": 1,
              "detail": "$I \\approx 26\\,\\text{A}$ ja keskiteho $\\dfrac{6{,}9\\,\\text{J}}{1{,}0\\,\\text{ms}} \\approx 6{,}9\\,\\text{kW}$ ovat paljon suurempia kuin pieni paristo voisi antaa näin lyhyessä pulssissa; siksi energia varastoidaan ensin kondensaattoriin."
            }
          ]
        },
        {
          "id": "d",
          "kind": "word",
          "points": 4,
          "text": "Korjaaja irrottaa salamalaitteesta pariston ja avaa laitteen heti sen jälkeen. Arvioi, onko kondensaattorissa vaaraa, ja kuvaile, miten kondensaattori puretaan turvallisesti. Arvioi vaaraa myös laskemalla virta, jos ihmisen kehon resistanssi on noin $1{,}0\\,\\text{k}\\Omega$.",
          "criteria": [
            {
              "text": "Tietää, että kondensaattori säilyttää varauksensa ja energiansa, kun paristo irrotetaan: se on edelleen $300\\,\\text{V}$:ssa ja siinä on noin $15\\,\\text{J}$, vaikka laitetta syöttää pieni paristo.",
              "tag": "concept",
              "points": 1
            },
            {
              "text": "Laskee virran kehon läpi: $I = \\dfrac{U}{R} = \\dfrac{300\\,\\text{V}}{1{,}0 \\cdot 10^{3}\\,\\Omega} = 0{,}30\\,\\text{A}$, mikä on moninkertainen verrattuna muutamaan kymmeneen milliampeeriin, jotka voivat jo olla vaarallisia.",
              "tag": "math",
              "points": 1
            },
            {
              "text": "Kuvaa turvallisen purkamisen: napojen väliin kytketään eristetyillä työkaluilla sopiva vastus, esimerkiksi $10\\,\\text{k}\\Omega$, jolloin energia siirtyy vastuksen sisäenergiaksi ja edelleen lämpönä ympäristöön; alkuvirta on $\\dfrac{300\\,\\text{V}}{10\\,\\text{k}\\Omega} = 30\\,\\text{mA}$. Napoja ei oikosulkuteta, ja jännite varmistetaan mittarilla. Vastuksen on kestettävä alussa noin $\\dfrac{(300\\,\\text{V})^2}{10\\,\\text{k}\\Omega} = 9\\,\\text{W}$, joten sen tehonkesto on valittava sen mukaan. Kuvaus on tarkoitettu ymmärtämiseen: älä yritä purkaa itse.",
              "tag": "concept",
              "points": 1
            },
            {
              "key": "conclusion",
              "points": 1,
              "detail": "Päättelee, että laitetta ei saa avata heti: vaara johtuu varastoituneesta energiasta ja jännitteestä eikä pariston koosta. Kehon resistanssi vaihtelee (esimerkiksi kostea iho), joten arvio on suuruusluokka."
            }
          ]
        }
      ],
      "links": {
        "transfer": "fy6-13",
        "math": "fy6-13",
        "concept": "fy6-15",
        "communication": "fy6-15"
      }
    }
  ]
}
```

## content/fi/FY6/sovella/solutions.md
```
## fy6-s1

### a)
**Kysytty:** kuvaaja, jonka pisteisiin pariston mallin mukaan sopii suora
**Kuvaaja:** Paristo mallinnetaan ideaaliseksi jännitelähteeksi, jonka lähdejännite on $E$, ja sen kanssa sarjassa olevaksi sisäiseksi resistanssiksi $R_\text{s}$. Kun paristosta kulkee virta $I$, sisäisen resistanssin yli on jännite $R_\text{s} I$, ja napajännite on $U = E - R_\text{s} I$. Tämä on suoran yhtälö: kun virta $I$ on vaaka-akselilla ja napajännite $U$ pystyakselilla, suora leikkaa pystyakselin kohdassa $E$ ja sen kulmakerroin on $-R_\text{s}$. Mittaukset viedään siis kuvaajaan sellaisinaan.

| $I\ (\text{A})$ | $U\ (\text{V})$ |
|---|---|
| $0{,}10$ | $4{,}48$ |
| $0{,}20$ | $4{,}37$ |
| $0{,}30$ | $4{,}22$ |
| $0{,}40$ | $4{,}13$ |
| $0{,}50$ | $3{,}99$ |
| $0{,}60$ | $3{,}89$ |

Pystyakselin asteikko alkaa arvosta $3{,}6\,\text{V}$, jotta pisteiden vähäinen lasku erottuu, ja alku on merkitty kuvaan.

<svg …figure from figures.py…>

**Mallivastaus:** Kuusi pistettä asettuu lähes samalle suoralle, joten malli $U = E - R_\text{s} I$ kuvaa pariston käyttäytymistä mittausalueella hyvin: napajännite pienenee tasaisesti virran kasvaessa. Suora on sovitettu pisteiden lomitse eikä pisteitä ole yhdistetty murtoviivaksi. Suoraa on jatkettu katkoviivana pystyakselille, jotta lähdejännitteen kohta $I = 0$ näkyy.

### b)
**Annettu:** a-kohdan suora, jolta luetaan pisteet $(0{,}10\,\text{A};\ 4{,}48\,\text{V})$ ja $(0{,}60\,\text{A};\ 3{,}88\,\text{V})$
**Kysytty:** lähdejännite $E$ ja sisäinen resistanssi $R_\text{s}$
**Periaate:** Mallin mukaan napajännite on $U = E - R_\text{s} I$. Suoran leikkauskohta pystyakselilla on virran arvolla nolla, jolloin pariston sisällä ei synny jännitehäviötä, joten leikkauskohta on $E$. Kulmakerroin kertoo, kuinka paljon napajännite laskee virran kasvaessa, joten se on $-R_\text{s}$.
**Kuvaajan lukeminen:** Kulmakerroin luetaan piirretyn suoran kahdesta kaukana toisistaan olevasta pisteestä eikä vierekkäisistä mittauspisteistä: $(0{,}10\,\text{A};\ 4{,}48\,\text{V})$ ja $(0{,}60\,\text{A};\ 3{,}88\,\text{V})$. Niiden välillä $\Delta I = 0{,}50\,\text{A}$ ja $\Delta U = -0{,}60\,\text{V}$ (kuvaajan kulmakertoimen kolmio). Suora leikkaa pystyakselin kohdassa $4{,}60\,\text{V}$.
**Kaava:** $R_\text{s} = -\dfrac{\Delta U}{\Delta I}$ ja $E = U + R_\text{s} I$ mistä tahansa suoran pisteestä.
**Muunnokset:** Ei tarvita: jännite on voltteina ja virta ampeereina, ja $1\,\text{V/A} = 1\,\Omega$.
**Sijoitus:** $R_\text{s} = -\dfrac{-0{,}60\,\text{V}}{0{,}50\,\text{A}} = 1{,}2\,\Omega$ ja $E = 4{,}48\,\text{V} + 1{,}2\,\Omega \cdot 0{,}10\,\text{A} = 4{,}48\,\text{V} + 0{,}12\,\text{V} = 4{,}60\,\text{V}$
**Vastaus:** $E \approx 4{,}6\,\text{V}$ ja $R_\text{s} \approx 1{,}2\,\Omega$, kaksi merkitsevää numeroa, koska kulmakerroin luetaan kuvaajalta eikä sitä voi lukea tarkemmin kuin kahden numeron tarkkuudella.
**Järkevyys:** Lähdejännite on hieman pariston nimellisjännitettä $4{,}5\,\text{V}$ suurempi, mikä sopii uudelle paristolle. Sisäinen resistanssi on ohmin luokkaa, kuten litteillä taskulamppuparistoilla. Oikosulkuvirta olisi $\dfrac{E}{R_\text{s}} \approx 3{,}8\,\text{A}$.

### c)
**Annettu:** $E = 4{,}60\,\text{V}$, $R_\text{s} = 1{,}2\,\Omega$ ja ulkoinen vastus $R = 8{,}0\,\Omega$
**Kysytty:** vastukseen siirtyvä teho $P$ ja pariston sisäisessä resistanssissa lämpönä siirtyvän tehon osuus pariston koko sähkötehosta
**Periaate:** Virtapiirissä paristo, sisäinen resistanssi ja vastus ovat sarjassa, joten kaikkien läpi kulkee sama virta. Silmukkasäännön mukaan lähdejännite jakautuu sisäisen resistanssin ja vastuksen yli: $E - R_\text{s} I - R I = 0$. Sähkötehosta siirtyy lämpönä sekä vastuksessa että pariston sisällä, ja pariston koko teho on näiden summa $E I$.
**Kaava:** $I = \dfrac{E}{R + R_\text{s}}$, $P = R I^2$, $P_\text{s} = R_\text{s} I^2$ ja osuus $\dfrac{P_\text{s}}{P + P_\text{s}} = \dfrac{R_\text{s}}{R + R_\text{s}}$
**Muunnokset:** Ei tarvita, kaikki suureet ovat perusyksiköissä.
**Sijoitus:** $I = \dfrac{4{,}60\,\text{V}}{8{,}0\,\Omega + 1{,}2\,\Omega} = \dfrac{4{,}60\,\text{V}}{9{,}2\,\Omega} = 0{,}50\,\text{A}$, $P = 8{,}0\,\Omega \cdot (0{,}50\,\text{A})^2 = 2{,}0\,\text{W}$ ja $P_\text{s} = 1{,}2\,\Omega \cdot (0{,}50\,\text{A})^2 = 0{,}30\,\text{W}$. Osuus on $\dfrac{0{,}30\,\text{W}}{2{,}0\,\text{W} + 0{,}30\,\text{W}} = 0{,}13$.
**Vastaus:** Vastukseen siirtyy teho $P \approx 2{,}0\,\text{W}$, ja noin $13\,\%$ pariston sähkötehosta siirtyy lämpönä pariston sisällä. Tulos on annettu kahden merkitsevän numeron tarkkuudella kuten lähtötiedot.
**Järkevyys:** Napajännite on $R I = 4{,}0\,\text{V}$, mikä on sama kuin $E - R_\text{s} I = 4{,}60\,\text{V} - 0{,}60\,\text{V}$, ja kuvaajalla virran $0{,}50\,\text{A}$ kohdalla jännite on noin $4{,}0\,\text{V}$. Koska ulkoinen vastus on yli seitsemän kertaa sisäistä resistanssia suurempi, vain pieni osa tehosta jää pariston sisälle.

### d)
**Kysytty:** purkautumisen ja lämpenemisen vaikutus lähdejännitteen ja sisäisen resistanssin tulokseen, hajonnan aiheuttama epävarmuus $R_\text{s}$:ssä ja mittauksen parannus
**Periaate:** Malli $U = E - R_\text{s} I$ olettaa, että $E$ ja $R_\text{s}$ pysyvät vakioina koko mittauksen ajan. Jos paristo purkautuu tai lämpenee, ne muuttuvat mittauksen aikana, ja kuvaajan suora kuvaa jonkinlaista keskiarvoa. Hajonta kertoo satunnaisista virheistä eli siitä, kuinka paljon sovitettu suora voisi kääntyä.
**Mallivastaus:** *Systemaattinen virhe.* Virtaa kasvatettiin koko ajan samaan suuntaan, ja jokaista lukemaa varten piiri oli kytkettynä noin minuutin. Pariston purkautuminen laskee jännitettä ajan myötä, joten myöhemmin mitatut jännitteet eli suurimpia virtoja vastaavat jännitteet ovat liian pieniä. Koska aika ja virta kasvavat yhtä aikaa, ajan vaikutus sekoittuu kulmakertoimeen: suora laskee liian jyrkästi ja $R_\text{s}$ tulee liian suureksi. Lämpeneminen muuttaa myös $R_\text{s}$:ää mittauksen aikana (yleensä pienentää sitä), joten sen vaikutuksen suunta on epävarma. Lähdejännitteeseen vaikutus on pieni, koska pienimmällä virralla mitattiin ensin tuoreella paristolla.

*Ajautuman suuruus.* Uusi mittaus virralla $0{,}10\,\text{A}$ antoi $4{,}45\,\text{V}$ eli $0{,}03\,\text{V}$ vähemmän kuin sarjan alussa. Pahimmillaan viimeinen piste on siis noin $0{,}03\,\text{V}$ liian alhaalla, ja kulmakerroin on liian suuri enintään $\dfrac{0{,}03\,\text{V}}{0{,}50\,\text{A}} = 0{,}06\,\Omega$.

*Epävarmuus.* Pisteet poikkeavat sovitetusta suorasta enintään $0{,}02\,\text{V}$. Jos suoran toinen pää nousee ja toinen laskee tämän verran, kulmakerroin muuttuu $\dfrac{2 \cdot 0{,}02\,\text{V}}{0{,}50\,\text{A}} = 0{,}08\,\Omega$ eli $R_\text{s} = (1{,}20 \pm 0{,}08)\,\Omega$. Epävarmuus on pyöristetty yhteen merkitsevään numeroon.

*Parannus.* Virrat mitataan satunnaisessa järjestyksessä tai sarja toistetaan käänteisessä järjestyksessä, ja piiri kytketään päälle vain lukeman ajaksi. Jos tulokset eroavat toisistaan, ero kertoo purkautumisen vaikutuksen suuruuden.

*Johtopäätös.* Ajautuman vaikutus ($0{,}06\,\Omega$) on samaa suuruusluokkaa kuin hajonnan ($0{,}08\,\Omega$), joten $R_\text{s}$ on noin $1{,}1\ldots1{,}2\,\Omega$. Arvo $1{,}2\,\Omega$ on pikemmin yläraja, koska systemaattinen virhe kasvattaa sitä.

### Hyväksytään myös
- a-kohdassa kuvaajan pystyakseli voi alkaa nollasta, kunhan pisteet ja $E$ erottuvat; silloin suora voidaan jatkaa myös vaaka-akselille, jossa $I_\text{k} = \dfrac{E}{R_\text{s}} \approx 3{,}8\,\text{A}$.
- b-kohdassa kulmakertoimen lukema $-1{,}1\ldots-1{,}3\,\text{V/A}$ (vastaus $R_\text{s}$ noin $1{,}1\ldots1{,}3\,\Omega$) ja lähdejännite $4{,}5\ldots4{,}7\,\text{V}$ hyväksytään. Myös laskimen tai taulukkolaskennan sovitus hyväksytään.
- d-kohdassa epävarmuuden saa arvioida myös sovittamalla ääriviivat ja lukemalla niiden kulmakertoimet.

### Yleisiä virheitä
- Pisteet yhdistetään murtoviivaksi tai suora pakotetaan kulkemaan origon kautta, vaikka $U$ ei ole nolla virran ollessa nolla.
- Kulmakerroin luetaan kahdesta peräkkäisestä mittauspisteestä eikä kaukana toisistaan olevista suoran pisteistä.
- Kulmakertoimen etumerkki jätetään huomiotta, tai $R_\text{s}$ laskee $U : I$ yksittäisestä mittauksesta, jolloin saadaan ulkoisen vastuksen arvo, ei sisäistä resistanssia.
- c-kohdassa vastuksen jännitteeksi otetaan koko lähdejännite $E$ ja unohdetaan sisäisen resistanssin jännitehäviö.
- Epävarmuudeksi kirjoitetaan mittarin lukematarkkuus $0{,}01\,\text{V}$ sellaisenaan eikä oteta huomioon pisteiden hajontaa eikä systemaattista virhettä.

## fy6-s2

### a)
**Annettu:** lähdejännite $E = 12{,}0\,\text{V}$, kaapelin resistanssi $R_\text{k} = 0{,}80\,\Omega$, lamppu A $12\,\text{V},\ 24\,\text{W}$ ja lamppu B $12\,\text{V},\ 12\,\text{W}$
**Kysytty:** akustosta kulkeva virta $I$, kun molemmat lamput palavat
**Periaate:** Lamppu käsitellään vakioresistanssina, jonka arvo saadaan nimellisarvoista: nimellisjännitteellä teho on $P = \dfrac{U^2}{R}$. Lamput A ja B ovat rinnan, joten niillä on sama jännite, ja kaapeli on niiden kanssa sarjassa, joten koko virta kulkee kaapelin kautta. Silloin kokonaisresistanssi on kaapelin resistanssin ja rinnankytkennän korvaavan resistanssin summa.
**Kaava:** $R_\text{A} = \dfrac{U_\text{n}^2}{P_\text{A}}$, $R_\text{B} = \dfrac{U_\text{n}^2}{P_\text{B}}$, $\dfrac{1}{R_\text{r}} = \dfrac{1}{R_\text{A}} + \dfrac{1}{R_\text{B}}$, $R = R_\text{k} + R_\text{r}$ ja $I = \dfrac{E}{R}$
**Muunnokset:** Ei tarvita: $1\,\text{V}^2/\text{W} = 1\,\Omega$.
**Sijoitus:** $R_\text{A} = \dfrac{(12\,\text{V})^2}{24\,\text{W}} = 6{,}0\,\Omega$ ja $R_\text{B} = \dfrac{(12\,\text{V})^2}{12\,\text{W}} = 12\,\Omega$. Rinnankytkentä: $\dfrac{1}{R_\text{r}} = \dfrac{1}{6{,}0\,\Omega} + \dfrac{1}{12\,\Omega} = \dfrac{3}{12\,\Omega}$, joten $R_\text{r} = 4{,}0\,\Omega$. Kokonaisresistanssi on $R = 0{,}80\,\Omega + 4{,}0\,\Omega = 4{,}8\,\Omega$ ja virta $I = \dfrac{12{,}0\,\text{V}}{4{,}8\,\Omega} = 2{,}5\,\text{A}$.
**Vastaus:** $I = 2{,}5\,\text{A}$, kaksi merkitsevää numeroa kuten lähtötiedoissa.
**Järkevyys:** Jos lamput saisivat nimellisjännitteen, niiden virrat olisivat $2{,}0\,\text{A}$ ja $1{,}0\,\text{A}$ eli yhteensä $3{,}0\,\text{A}$. Kaapeli ottaa osan jännitteestä, joten virta jää tätä pienemmäksi. Virta on myös sulakkeen $3{,}15\,\text{A}$ ja kaapelin $4{,}0\,\text{A}$ rajojen alapuolella.

### b)
**Annettu:** $E = 12{,}0\,\text{V}$, $R_\text{k} = 0{,}80\,\Omega$, $R_\text{A} = 6{,}0\,\Omega$ ja a-kohdan virta $I = 2{,}5\,\text{A}$
**Kysytty:** lampun A todellinen teho $P_\text{A}$ ja sen vertailu nimellistehoon $24\,\text{W}$
**Periaate:** Silmukkasäännön mukaan akun jännite jakautuu kaapelin jännitehäviön ja lamppujen jännitteen kesken: $E - R_\text{k} I - U_\text{L} = 0$. Lamppujen jännite jää siksi nimellisjännitettä pienemmäksi, ja teho lasketaan tästä todellisesta jännitteestä.
**Kaava:** $U_\text{L} = E - R_\text{k} I$ ja $P_\text{A} = \dfrac{U_\text{L}^2}{R_\text{A}}$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $U_\text{L} = 12{,}0\,\text{V} - 0{,}80\,\Omega \cdot 2{,}5\,\text{A} = 12{,}0\,\text{V} - 2{,}0\,\text{V} = 10{,}0\,\text{V}$ ja $P_\text{A} = \dfrac{(10{,}0\,\text{V})^2}{6{,}0\,\Omega} = 16{,}7\,\text{W}$
**Vastaus:** $P_\text{A} \approx 17\,\text{W}$, noin $70\,\%$ nimellisarvosta $24\,\text{W}$, kaksi merkitsevää numeroa kuten lähtötiedoissa ($0{,}80\,\Omega$, $24\,\text{W}$, $12\,\text{V}$).
**Järkevyys:** Lamppu palaa himmeämmin kuin nimellisjännitteellä, koska sen jännite on vain $10{,}0\,\text{V}$. Tarkistus: lampun B teho on $\dfrac{(10{,}0\,\text{V})^2}{12\,\Omega} = 8{,}3\,\text{W}$ ja kaapeliin siirtyy lämpönä $0{,}80\,\Omega \cdot (2{,}5\,\text{A})^2 = 5{,}0\,\text{W}$. Summa $16{,}7\,\text{W} + 8{,}3\,\text{W} + 5{,}0\,\text{W} = 30\,\text{W}$ on yhtä suuri kuin akuston teho $12{,}0\,\text{V} \cdot 2{,}5\,\text{A} = 30\,\text{W}$.

### c)
**Kysytty:** miten lampun A kirkkaus, akuston virta ja kaapelin lämpeneminen muuttuvat, kun lamppu B poistuu piiristä, sekä lampun A tehon tarkistus laskemalla
**Periaate:** Akusto antaa piiriin vakiojännitteen $12{,}0\,\text{V}$. Kun toinen rinnakkainen haara poistuu, rinnankytkennän korvaava resistanssi kasvaa ja kokonaisresistanssi kasvaa, joten virta pienenee. Kaapeli on sarjassa lampun A kanssa, joten sen jännitehäviö riippuu koko virrasta.
**Mallivastaus:** *Virta.* Kokonaisresistanssi on nyt $R = 0{,}80\,\Omega + 6{,}0\,\Omega = 6{,}8\,\Omega$ ja virta $I = \dfrac{12{,}0\,\text{V}}{6{,}8\,\Omega} \approx 1{,}8\,\text{A}$, aiemmin $2{,}5\,\text{A}$.

*Kirkkaus.* Pienempi virta pienentää kaapelin jännitehäviötä: $0{,}80\,\Omega \cdot 1{,}76\,\text{A} \approx 1{,}4\,\text{V}$, aiemmin $2{,}0\,\text{V}$. Lampulle A jää siksi suurempi jännite $U_\text{A} \approx 10{,}6\,\text{V}$, ja sen teho on $\dfrac{(10{,}6\,\text{V})^2}{6{,}0\,\Omega} \approx 18{,}7\,\text{W}$, aiemmin $16{,}7\,\text{W}$. Lamppu A siis palaa kirkkaammin, vaikka sen omassa haarassa ei muuttunut mikään.

*Kaapeli.* Kaapeliin siirtyy lämpönä teho $R_\text{k} I^2 = 0{,}80\,\Omega \cdot (1{,}76\,\text{A})^2 \approx 2{,}5\,\text{W}$, aiemmin $5{,}0\,\text{W}$. Kaapeli lämpenee siis vähemmän, koska teho riippuu virran neliöstä.

*Johtopäätös.* Rinnankytketyt lamput ovat toisistaan riippumattomia vain, jos jännite niiden yli pysyy vakiona. Kaapelin resistanssi tekee lampuista hieman riippuvaisia toisistaan: jos kaapelin resistanssi olisi nolla, lampun A kirkkaus ei muuttuisi lainkaan.

### d)
**Annettu:** $E = 12{,}0\,\text{V}$, $R_\text{k} = 0{,}80\,\Omega$, $R_\text{A} = 6{,}0\,\Omega$, $R_\text{B} = 12\,\Omega$, uusi lamppu C $12\,\text{V},\ 36\,\text{W}$, sulake $3{,}15\,\text{A}$ ja kaapelin raja $4{,}0\,\text{A}$
**Kysytty:** akuston virta $I$ kolmella lampulla ja sulakkeen toiminta
**Periaate:** Lamput ovat edelleen rinnan, joten niillä on yhteinen jännite ja resistanssit lasketaan yhteen käänteislukuina. Kaapeli on sarjassa kaikkien kanssa. Sulake on virtapiirin suojalaite: se palaa ja katkaisee piirin, jos virta ylittää sen nimellisvirran liian pitkään.
**Kaava:** $R_\text{C} = \dfrac{U_\text{n}^2}{P_\text{C}}$, $\dfrac{1}{R_\text{r}} = \dfrac{1}{R_\text{A}} + \dfrac{1}{R_\text{B}} + \dfrac{1}{R_\text{C}}$ ja $I = \dfrac{E}{R_\text{k} + R_\text{r}}$
**Muunnokset:** Ei tarvita.
**Sijoitus:** $R_\text{C} = \dfrac{(12\,\text{V})^2}{36\,\text{W}} = 4{,}0\,\Omega$ ja $\dfrac{1}{R_\text{r}} = \dfrac{1}{6{,}0\,\Omega} + \dfrac{1}{12\,\Omega} + \dfrac{1}{4{,}0\,\Omega} = \dfrac{2 + 1 + 3}{12\,\Omega} = \dfrac{1}{2{,}0\,\Omega}$, joten $R_\text{r} = 2{,}0\,\Omega$. Virta on $I = \dfrac{12{,}0\,\text{V}}{0{,}80\,\Omega + 2{,}0\,\Omega} = \dfrac{12{,}0\,\text{V}}{2{,}8\,\Omega} = 4{,}3\,\text{A}$.
**Vastaus:** $I \approx 4{,}3\,\text{A}$. Virta ylittää sekä sulakkeen nimellisvirran $3{,}15\,\text{A}$ että kaapelin sallitun virran $4{,}0\,\text{A}$, joten sulake todennäköisesti palaa ylivirran jatkuessa ja katkaisee piirin (todellinen toiminta-aika riippuu sulakkeen tyypistä, joten tämä on yksinkertaistus). Lamppujen jännite on $R_\text{r} I = 2{,}0\,\Omega \cdot 4{,}3\,\text{A} \approx 8{,}6\,\text{V}$, joten ne palavat himmeämmin kuin aiemmin. Sulake mitoitetaan suojaamaan piirin heikointa osaa eli kaapelia: sen nimellisvirta on kaapelin sallittua virtaa pienempi, jotta kaapeli ei lämpene vaarallisesti ennen kuin piiri katkeaa.
**Järkevyys:** Kolmas lamppu pienentää rinnankytkennän resistanssin $4{,}0\,\Omega$:sta $2{,}0\,\Omega$:iin, joten virran täytyy kasvaa $2{,}5\,\text{A}$:sta. Jos sulaketta ei olisi, kaapeliin siirtyisi lämpönä $0{,}80\,\Omega \cdot (4{,}3\,\text{A})^2 \approx 15\,\text{W}$, melkein kolminkertainen teho aiempaan $5{,}0\,\text{W}$:iin verrattuna. Lamppujen resistanssit on laskettu nimellisarvoista, joten tulos on arvio.

### Hyväksytään myös
- a-kohdan voi laskea lampun nimellisvirroista $I = \dfrac{P}{U}$ ja resistansseista $R = \dfrac{U}{I}$, kunhan tulokset ovat samat: $2{,}0\,\text{A}$ ja $1{,}0\,\text{A}$, $6{,}0\,\Omega$ ja $12\,\Omega$.
- b-kohdassa lampun jännitteen saa laskea myös suoraan $U_\text{L} = R_\text{r} I = 4{,}0\,\Omega \cdot 2{,}5\,\text{A}$.
- d-kohdassa lamppujen jännitteen ($8{,}6\,\text{V}$) voi lisäksi laskea ja todeta, että lamput palavat himmeämmin kuin aiemmin.

### Yleisiä virheitä
- Lamppujen resistanssit lasketaan kaavalla $R = \dfrac{P}{U}$ tai $R = \dfrac{U}{P}$.
- Rinnankytkennän resistanssi lasketaan summana $6{,}0\,\Omega + 12\,\Omega$ tai korvaavaksi resistanssiksi saadaan käänteisluku, jota ei muuteta takaisin ($\tfrac{1}{4{,}0\,\Omega} = 0{,}25\,\text{S}$ kirjoitetaan resistanssiksi $0{,}25\,\Omega$).
- Lamppujen jännitteeksi otetaan koko akuston jännite $12{,}0\,\text{V}$, ja kaapelin jännitehäviö unohdetaan.
- c-kohdassa päätellään, että lamppu A ei muutu lainkaan, koska se on rinnan: unohdetaan, että kaapeli on sarjassa.
- d-kohdassa sulakkeen ylittyminen todetaan, mutta sulakkeen tarkoitusta kaapelin suojaajana ei selitetä.

## fy6-s3

### a)
**Annettu:** potentiaaliero $U = 60\,\text{kV} = 6{,}0 \cdot 10^{4}\,\text{V}$, etäisyys $d = 20\,\text{cm}$, varaus $q = 6{,}0 \cdot 10^{-13}\,\text{C}$ ja massa $m = 4{,}0 \cdot 10^{-10}\,\text{kg}$
**Kysytty:** pisaraan vaikuttava sähkövoima $F$, painon merkitys ja kipinöinnin mahdollisuus
**Periaate:** Levyjen välissä on homogeeninen sähkökenttä, jonka voimakkuus on potentiaaliero jaettuna etäisyydellä. Positiivisesti varautuneeseen pisaraan vaikuttaa kentän suuntainen voima, joten pisara kulkee kohti pienempää potentiaalia eli maadoitettua työkappaletta. Painon merkitys arvioidaan vertaamalla sitä sähkövoimaan, ja kipinöinti kentän voimakkuutta ilman läpilyöntilujuuteen.
**Kaava:** $E = \dfrac{U}{d}$ ja $F = qE$
**Muunnokset:** $20\,\text{cm} = 0{,}20\,\text{m}$ ja $60\,\text{kV} = 60 \cdot 1000\,\text{V} = 6{,}0 \cdot 10^{4}\,\text{V}$.
**Sijoitus:** $E = \dfrac{6{,}0 \cdot 10^{4}\,\text{V}}{0{,}20\,\text{m}} = 3{,}0 \cdot 10^{5}\,\text{V/m}$ ja $F = 6{,}0 \cdot 10^{-13}\,\text{C} \cdot 3{,}0 \cdot 10^{5}\,\text{V/m} = 1{,}8 \cdot 10^{-7}\,\text{N}$
**Vastaus:** $F \approx 1{,}8 \cdot 10^{-7}\,\text{N}$ kentän suuntaan kohti työkappaletta, kaksi merkitsevää numeroa kuten lähtötiedoissa.
**Järkevyys:** Pisaran paino on $mg = 4{,}0 \cdot 10^{-10}\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 = 3{,}9 \cdot 10^{-9}\,\text{N}$, eli vain noin $2\,\%$ sähkövoimasta, joten painon voi jättää huomiotta. Kentän voimakkuus $3{,}0 \cdot 10^{5}\,\text{V/m} = 0{,}30\,\text{MV/m}$ on noin kymmenesosa ilman läpilyöntilujuudesta $3\,\text{MV/m}$, joten kipinöintiä ei synny.

### b)
**Annettu:** $q = 6{,}0 \cdot 10^{-13}\,\text{C}$, $U = 6{,}0 \cdot 10^{4}\,\text{V}$, $m = 4{,}0 \cdot 10^{-10}\,\text{kg}$ ja pisara lähtee levosta
**Kysytty:** pisaran nopeus $v$ osuessaan työkappaleeseen, kun ilmanvastusta ei oteta huomioon
**Periaate:** Sähkökentän pisaraan tekemä työ on varaus kertaa potentiaaliero, $W = qU$, ja se kasvattaa pisaran liike-energiaa. Paino ja ilmanvastus jätetään pois, joten muita voimia ei ole. Tällä tavalla riittää tietää potentiaaliero, eikä kentän voimakkuutta tai kiihtyvyyttä tarvita.
**Kaava:** $q U = \dfrac{1}{2} m v^2$, josta $v = \sqrt{\dfrac{2 q U}{m}}$
**Muunnokset:** Ei tarvita, kaikki suureet ovat perusyksiköissä; $1\,\text{C} \cdot 1\,\text{V} = 1\,\text{J}$.
**Sijoitus:** $qU = 6{,}0 \cdot 10^{-13}\,\text{C} \cdot 6{,}0 \cdot 10^{4}\,\text{V} = 3{,}6 \cdot 10^{-8}\,\text{J}$ ja $v = \sqrt{\dfrac{2 \cdot 3{,}6 \cdot 10^{-8}\,\text{J}}{4{,}0 \cdot 10^{-10}\,\text{kg}}} = \sqrt{180\,\text{m}^2/\text{s}^2} = 13{,}4\,\text{m/s}$
**Vastaus:** $v \approx 13\,\text{m/s}$, kaksi merkitsevää numeroa kuten lähtötiedoissa.
**Järkevyys:** Kiihtyvyys on $\dfrac{F}{m} = \dfrac{1{,}8 \cdot 10^{-7}\,\text{N}}{4{,}0 \cdot 10^{-10}\,\text{kg}} = 450\,\text{m/s}^2$, joten $0{,}20\,\text{m}$:n matkalla nopeus olisi $\sqrt{2 \cdot 450\,\text{m/s}^2 \cdot 0{,}20\,\text{m}} = 13{,}4\,\text{m/s}$, mikä vahvistaa tuloksen. Painon työ koko matkalla olisi vain $7{,}8 \cdot 10^{-10}\,\text{J}$ eli noin $2\,\%$ sähkökentän työstä.

### c)
**Kysytty:** miksi mitattu osumanopeus $5{,}0\,\text{m/s}$ on paljon pienempi kuin b-kohdan tulos ja minne sähkökentän tekemä työ jää
**Periaate:** B-kohdan malli jätti ilmanvastuksen pois. Ilmanvastus vaikuttaa pisaran liikkeen suuntaa vastaan, ja sen tekemä työ on negatiivista. Kun pisaran nopeus kasvaa, ilmanvastus kasvaa, ja pisara etenee nopeudella, jolla ilmanvastus ja sähkövoima ovat likimain yhtä suuret. Energian säilymisen mukaan sähkökentän tekemä työ ei häviä, vaan se siirtyy muualle.
**Mallivastaus:** *Selitys.* B-kohdan nopeus $13\,\text{m/s}$ olisi mahdollinen vain tyhjiössä. Ilmassa ilmanvastus rajoittaa nopeuden paljon pienemmäksi, joten b-kohdan tulos on pisaran suurin mahdollinen nopeus eli yläraja.

*Laskenta.* Pisaran todellinen liike-energia on $\dfrac{1}{2} m v^2 = \dfrac{1}{2} \cdot 4{,}0 \cdot 10^{-10}\,\text{kg} \cdot (5{,}0\,\text{m/s})^2 = 5{,}0 \cdot 10^{-9}\,\text{J}$. Sähkökentän tekemä työ on $3{,}6 \cdot 10^{-8}\,\text{J}$, joten liike-energiaksi päätyy vain $\dfrac{5{,}0 \cdot 10^{-9}\,\text{J}}{3{,}6 \cdot 10^{-8}\,\text{J}} \approx 14\,\%$.

*Energian kohtalo.* Loput $3{,}6 \cdot 10^{-8}\,\text{J} - 5{,}0 \cdot 10^{-9}\,\text{J} = 3{,}1 \cdot 10^{-8}\,\text{J}$ siirtyy ilmaan. Ilman sisäenergia kasvaa, ja energia siirtyy edelleen lämpönä ympäristöön. Energia ei siis häviä.

*Johtopäätös.* B-kohdan oletus (ei ilmanvastusta) tekee nopeudesta liian suuren, joten tulos on suurin mahdollinen nopeus. Energia ei häviä, vaan se siirtyy ilmaan.

### d)
**Annettu:** $q_1 = q_2 = 6{,}0 \cdot 10^{-13}\,\text{C}$, $r = 1{,}0\,\text{mm}$ ja $k = 8{,}988 \cdot 10^{9}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{C}^2}$
**Kysytty:** pisaroiden välinen voima $F$ ja sen merkitys pisarapilven käyttäytymiselle
**Periaate:** Pisarat ovat paljon pienempiä kuin niiden etäisyys, joten ne voi käsitellä pistemäisinä varauksina. Niiden välinen voima noudattaa Coulombin lakia: samanmerkkiset varaukset hylkivät toisiaan.
**Kaava:** $F = k\dfrac{q_1 q_2}{r^2}$
**Muunnokset:** $1{,}0\,\text{mm} = 1{,}0 \cdot 10^{-3}\,\text{m}$
**Sijoitus:** $F = 8{,}988 \cdot 10^{9}\,\tfrac{\text{N}\cdot\text{m}^2}{\text{C}^2} \cdot \dfrac{(6{,}0 \cdot 10^{-13}\,\text{C})^2}{(1{,}0 \cdot 10^{-3}\,\text{m})^2} = 8{,}988 \cdot 10^{9} \cdot \dfrac{3{,}6 \cdot 10^{-25}}{1{,}0 \cdot 10^{-6}}\,\text{N} = 3{,}2 \cdot 10^{-9}\,\text{N}$
**Vastaus:** $F \approx 3{,}2 \cdot 10^{-9}\,\text{N}$, hylkivä, kaksi merkitsevää numeroa kuten lähtötiedoissa.
**Järkevyys:** Voima on noin $1{,}8\,\%$ kentän voimasta $1{,}8 \cdot 10^{-7}\,\text{N}$ mutta $0{,}8$-kertainen pisaran painoon $3{,}9 \cdot 10^{-9}\,\text{N}$ verrattuna. Hylkimisvoima on siis pieni verrattuna sähkökentän voimaan, joten pisarat kulkevat edelleen kohti työkappaletta, mutta hylkiminen levittää pisarapilveä sivusuunnassa. Tämä on osa sitä, miksi suihku leviää suuttimen jälkeen.

### Hyväksytään myös
- a-kohdassa kentän voimakkuuden saa ilmoittaa yksikössä $\text{kV/m}$: $300\,\text{kV/m}$.
- b-kohdan voi ratkaista myös kiihtyvyydestä: $a = \dfrac{F}{m} = 450\,\text{m/s}^2$ ja $v = \sqrt{2 a d}$, kunhan ratkaisu perustuu a-kohdan voimaan ja matkaan $0{,}20\,\text{m}$.

### Yleisiä virheitä
- Potentiaaliero $60\,\text{kV}$ sijoitetaan kilovoltteina, jolloin kenttä saadaan väärin tuhatkertaisena tai tuhannesosana.
- Voimaksi lasketaan $U : d$, jolloin kentän voimakkuus sekoitetaan voimaan.
- b-kohdassa käytetään kaavaa $v = \sqrt{2 a d}$ kiihtyvyydellä $g$ tai lasketaan työ painosta.
- Pisaran energian ilmoitetaan "muuttuvan lämmöksi" tai "hukkuvan"; energia siirtyy ilmaan ja sieltä lämpönä.
- d-kohdassa etäisyys sijoitetaan millimetreinä, tai unohdetaan neliöinti.

## fy6-s4

### a)
**Annettu:** $C = 330\,\mu\text{F}$ ja $U = 300\,\text{V}$
**Kysytty:** kondensaattoriin varastoitunut energia $E$ ennen salamaa
**Periaate:** Ladattuun kondensaattoriin on varastoitunut energiaa, koska varaus on siirretty sen levyille jännitettä vastaan. Energia riippuu kapasitanssista ja jännitteen neliöstä.
**Kaava:** $E = \dfrac{1}{2} C U^2$
**Muunnokset:** $330\,\mu\text{F} = 330 \cdot 10^{-6}\,\text{F}$
**Sijoitus:** $E = \dfrac{1}{2} \cdot 330 \cdot 10^{-6}\,\text{F} \cdot (300\,\text{V})^2 = \dfrac{1}{2} \cdot 330 \cdot 10^{-6}\,\text{F} \cdot 90\,000\,\text{V}^2 = 14{,}85\,\text{J}$
**Vastaus:** $E \approx 15\,\text{J}$ ($14{,}85\,\text{J}$), kaksi merkitsevää numeroa, koska jännitteen $300\,\text{V}$ ja kapasitanssin $330\,\mu\text{F}$ tarkkuus on enintään kaksi tai kolme numeroa.
**Järkevyys:** Energia on joulen luokkaa, kuten pienen salamalaitteen kondensaattorissa. Jos tämä energia siirtyisi nostamaan kilon painoista kappaletta, se nousisi noin $1{,}5\,\text{m}$.

### b)
**Annettu:** $C = 330\,\mu\text{F}$, jännite ennen salamaa $U_1 = 300\,\text{V}$ ja sen jälkeen $U_2 = 220\,\text{V}$
**Kysytty:** salamaan siirtynyt energia $\Delta E$, sen osuus varastoidusta energiasta ja osuuden suuruuden syy
**Periaate:** Salamaan siirtynyt energia on kondensaattorin energian muutos: se on energia ennen salamaa vähennettynä energialla salaman jälkeen. Jännite on energiakaavassa neliönä, joten kumpikin energia lasketaan erikseen; pelkkä jännitteen muutos $\Delta U$ ei riitä.
**Kaava:** $\Delta E = \dfrac{1}{2} C U_1^2 - \dfrac{1}{2} C U_2^2$
**Muunnokset:** $330\,\mu\text{F} = 330 \cdot 10^{-6}\,\text{F}$
**Sijoitus:** $E_1 = 14{,}85\,\text{J}$ ja $E_2 = \dfrac{1}{2} \cdot 330 \cdot 10^{-6}\,\text{F} \cdot (220\,\text{V})^2 = \dfrac{1}{2} \cdot 330 \cdot 10^{-6}\,\text{F} \cdot 48\,400\,\text{V}^2 = 7{,}99\,\text{J}$, joten $\Delta E = 14{,}85\,\text{J} - 7{,}99\,\text{J} = 6{,}86\,\text{J}$. Osuus on $\dfrac{6{,}86\,\text{J}}{14{,}85\,\text{J}} = 0{,}46$.
**Vastaus:** Salamaan siirtyi $\Delta E \approx 6{,}9\,\text{J}$, noin $46\,\%$ varastoidusta energiasta, kaksi merkitsevää numeroa kuten a-kohdassa.
**Järkevyys:** Jännite pieneni vain $\dfrac{80\,\text{V}}{300\,\text{V}} \approx 27\,\%$, mutta energiaa siirtyi $46\,\%$, koska energia on verrannollinen jännitteen neliöön: $1 - \left(\dfrac{220}{300}\right)^2 = 0{,}46$. Siirtynyt energia on pienempi kuin alkuenergia, kuten pitääkin.

### c)
**Annettu:** $C = 330\,\mu\text{F}$, jännitteen muutos $\Delta U = 300\,\text{V} - 220\,\text{V} = 80\,\text{V}$ ja kesto $\Delta t = 1{,}0\,\text{ms}$
**Kysytty:** keskimääräinen virta $I$ salaman aikana
**Periaate:** Virta on varauksen siirtymisnopeus. Kondensaattorin varaus on $Q = C U$, joten jännitteen pienentyessä $80\,\text{V}$ kondensaattorilta on lähtenyt varausta $\Delta Q = C\,\Delta U$ salamaputken kautta.
**Kaava:** $I = \dfrac{\Delta Q}{\Delta t}$ ja $\Delta Q = C\,\Delta U$
**Muunnokset:** $330\,\mu\text{F} = 330 \cdot 10^{-6}\,\text{F}$ ja $1{,}0\,\text{ms} = 1{,}0 \cdot 10^{-3}\,\text{s}$
**Sijoitus:** $\Delta Q = 330 \cdot 10^{-6}\,\text{F} \cdot 80\,\text{V} = 0{,}0264\,\text{C}$ ja $I = \dfrac{0{,}0264\,\text{C}}{1{,}0 \cdot 10^{-3}\,\text{s}} = 26{,}4\,\text{A}$
**Vastaus:** $I \approx 26\,\text{A}$, kaksi merkitsevää numeroa kuten keston $1{,}0\,\text{ms}$ tarkkuus.
**Järkevyys:** Keskiteho on $\dfrac{6{,}86\,\text{J}}{1{,}0 \cdot 10^{-3}\,\text{s}} \approx 6{,}9\,\text{kW}$ ja virta $26\,\text{A}$: nämä ovat paljon suurempia kuin pieni paristo voisi antaa näin lyhyessä pulssissa. Siksi energia varastoidaan ensin kondensaattoriin, joka luovuttaa sen nopeasti.

### d)
**Kysytty:** onko kondensaattorissa vaaraa pariston irrottamisen jälkeen, miten se puretaan turvallisesti ja kuinka suuri virta kulkisi kehon läpi
**Periaate:** Kondensaattori varastoi varauksen ja energian levyilleen eikä sen jännite katoa, kun lataava paristo irrotetaan. Vaara riippuu varastoituneesta energiasta ja jännitteestä, ei paristosta. Virran suuruus kehon läpi saadaan jännitteestä ja resistanssista.
**Mallivastaus:** *Vaara.* Kondensaattori on pariston irrottamisen jälkeen edelleen $300\,\text{V}$:ssa, ja siinä on noin $15\,\text{J}$. Laite ei saa jännitettä pienestä paristosta, vaan kondensaattorista, joka voi purkautua korjaajan kehon kautta.

*Virta.* Jos kehon resistanssi on $1{,}0\,\text{k}\Omega$, virta olisi aluksi $I = \dfrac{U}{R} = \dfrac{300\,\text{V}}{1{,}0 \cdot 10^{3}\,\Omega} = 0{,}30\,\text{A}$. Se on moninkertainen verrattuna muutamaan kymmeneen milliampeeriin, jotka voivat jo olla vaarallisia. Virta pienenee kondensaattorin purkautuessa, mutta alun virta riittää vaaralliseen sähköiskuun.

*Turvallinen purku* (vain ymmärtämiseksi: älä yritä purkaa kondensaattoria itse). Kondensaattorin napojen väliin kytketään eristetyillä työkaluilla sopiva vastus, esimerkiksi $10\,\text{k}\Omega$. Alkuvirta on silloin $\dfrac{300\,\text{V}}{10\,\text{k}\Omega} = 30\,\text{mA}$, ja kondensaattorin energia siirtyy vastuksen sisäenergiaksi ja siitä lämpönä ympäristöön. Vastuksen teho on aluksi $\dfrac{(300\,\text{V})^2}{10\,\text{k}\Omega} = 9\,\text{W}$, joten vastuksen tehonkeston on oltava sen mukainen. Napoja ei oikosulkuteta ruuvimeisselillä, koska silloin virta on hyvin suuri ja syntyy kipinä. Lopuksi jännite varmistetaan mittarilla.

*Johtopäätös.* Laitetta ei saa avata heti. Vaara johtuu kondensaattorin varastoimasta energiasta ja jännitteestä eikä pariston koosta. Kehon resistanssi vaihtelee esimerkiksi ihon kosteuden mukaan, joten laskettu virta on suuruusluokka-arvio.

### Hyväksytään myös
- a-kohdassa energian saa laskea myös kaavalla $E = \dfrac{1}{2} Q U$, missä $Q = C U = 0{,}099\,\text{C}$.
- b-kohdassa osuuden saa laskea suoraan jännitteiden suhteesta $1 - \left(\dfrac{U_2}{U_1}\right)^2$.
- c-kohdassa tuloksen saa laskea myös varauksen ja ajan suhteena ilman erillistä $\Delta Q$:n laskua: $I = \dfrac{C\,\Delta U}{\Delta t}$.

### Yleisiä virheitä
- Kapasitanssi sijoitetaan mikrofaradeina kertomatta sitä luvulla $10^{-6}$.
- Energian laskemisessa unohdetaan jännitteen neliöinti, tai salamaan siirtynyt energia lasketaan kaavasta $\tfrac{1}{2} C (\Delta U)^2$.
- Virta lasketaan jakamalla energia ajalla, jolloin saadaan teho.
- Todetaan, että kondensaattori on vaaraton, koska laitteessa on vain pieni paristo.
- Kondensaattori puretaan oikosulkemalla se metallityökalulla.
```

## lessons/FY6/sovella/answers.py
```
"""FY6 Sovella itsenäisesti: every number of the worked solutions, recomputed from the task data.
Prints {"<task>-<part>": value} for the parts with an answer in tasks.json (and the intermediate values the solutions
quote); `python scripts/practice.py check FY6` compares them with tasks.json."""
import json, math

k_e = 8.988e9          # Coulomb constant, N·m²/C²
g = 9.81

out = {}


def fit(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    k = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    return k, my - k * mx


# fy6-s1: the battery measurement (simulated data: E = 4,60 V, R_s = 1,2 ohm, readings to 0,01 V and 0,01 A)
I1 = [0.10, 0.20, 0.30, 0.40, 0.50, 0.60]        # A
U1 = [4.48, 4.37, 4.22, 4.13, 3.99, 3.89]        # V
slope, icpt = fit(I1, U1)
# as read in the solution from two far-apart points of the drawn line: (0,10 A; 4,48 V) and (0,60 A; 3,88 V)
sl_read = (3.88 - 4.48) / (0.60 - 0.10)
Rs = -sl_read
E = 4.48 + Rs * 0.10
out.update({"fy6-s1-fit-slope": round(slope, 4), "fy6-s1-fit-icpt": round(icpt, 4), "fy6-s1-slope": round(sl_read, 3),
            "fy6-s1-b-E": round(E, 3), "fy6-s1-b-Rs": round(Rs, 3), "fy6-s1-Ik": round(E / Rs, 3)})
R = 8.0                                           # c) the load
I = E / (R + Rs)
P = R * I * I
P_batt = Rs * I * I
out.update({"fy6-s1-c-P": round(P, 3), "fy6-s1-c-I": round(I, 4), "fy6-s1-c-Pbatt": round(P_batt, 4),
            "fy6-s1-c-osuus": round(100 * P_batt / (P + P_batt), 2), "fy6-s1-c-U": round(R * I, 3)})
# d) the scatter of the points about the line is at most 0,02 V; extreme lines through the scatter's ends
dU = 0.02
dRs = 2 * dU / (0.60 - 0.10)
out.update({"fy6-s1-d-dRs": round(dRs, 3), "fy6-s1-d-maxres": round(max(abs(u - (icpt + slope * i)) for i, u in zip(I1, U1)), 3)})

# fy6-s2: cable and two lamps (12,0 V source, cable 0,80 ohm, lamps 12 V/24 W and 12 V/12 W, fuse 3,15 A, cable limit 4,0 A)
E2, Rc = 12.0, 0.80
RA, RB = 12.0 ** 2 / 24.0, 12.0 ** 2 / 12.0
Rp = 1 / (1 / RA + 1 / RB)
Rtot = Rc + Rp
Ia = E2 / Rtot
UL = Rp * Ia
PA, PB, Pc = UL ** 2 / RA, UL ** 2 / RB, Rc * Ia ** 2
out.update({"fy6-s2-RA": RA, "fy6-s2-RB": RB, "fy6-s2-Rp": round(Rp, 4), "fy6-s2-Rtot": round(Rtot, 4), "fy6-s2-a": round(Ia, 4),
            "fy6-s2-a-UL": round(UL, 4), "fy6-s2-b": round(PA, 3), "fy6-s2-b-PB": round(PB, 3), "fy6-s2-b-Pc": round(Pc, 3),
            "fy6-s2-b-Pbatt": round(E2 * Ia, 3), "fy6-s2-b-eff": round((PA + PB) / (E2 * Ia), 4)})
# c) lamp B removed
Ic = E2 / (Rc + RA)
UAc = RA * Ic
out.update({"fy6-s2-c-I": round(Ic, 4), "fy6-s2-c-UA": round(UAc, 4), "fy6-s2-c-PA": round(UAc ** 2 / RA, 3), "fy6-s2-c-Pc": round(Rc * Ic ** 2, 3),
            "fy6-s2-c-Ucable": round(Rc * Ic, 3), "fy6-s2-c-Ucable0": round(Rc * Ia, 3)})
# d) a third lamp 12 V/36 W in parallel
RC = 12.0 ** 2 / 36.0
Rp3 = 1 / (1 / RA + 1 / RB + 1 / RC)
Id = E2 / (Rc + Rp3)
out.update({"fy6-s2-RC": RC, "fy6-s2-d-Rp": round(Rp3, 4), "fy6-s2-d": round(Id, 4), "fy6-s2-d-UL": round(Rp3 * Id, 3),
            "fy6-s2-d-PC": round((Rp3 * Id) ** 2 / RC, 3), "fy6-s2-d-Pc": round(Rc * Id ** 2, 3)})

# fy6-s3: electrostatic spray painting (plates d = 0,20 m, U = 60 kV, droplet m = 4,0e-10 kg, q = 6,0e-13 C)
d3, U3, m3, q3 = 0.20, 60e3, 4.0e-10, 6.0e-13
E3 = U3 / d3
F3 = q3 * E3
G3 = m3 * g
out.update({"fy6-s3-a-E": round(E3), "fy6-s3-a": F3, "fy6-s3-a-G": G3, "fy6-s3-a-ratio": round(F3 / G3, 2),
            "fy6-s3-a-Eair": round(E3 / 3e6, 3), "fy6-s3-a-acc": round(F3 / m3, 1)})
W3 = q3 * U3
v3 = math.sqrt(2 * W3 / m3)
out.update({"fy6-s3-b": round(v3, 3), "fy6-s3-b-W": W3, "fy6-s3-b-Wg": G3 * d3})
v_meas = 5.0
Ek = 0.5 * m3 * v_meas ** 2
out.update({"fy6-s3-c-Ek": Ek, "fy6-s3-c-share": round(Ek / W3, 4), "fy6-s3-c-rest": W3 - Ek})
r3 = 1.0e-3
Fc = k_e * q3 ** 2 / r3 ** 2
out.update({"fy6-s3-d": Fc, "fy6-s3-d-vsF": round(Fc / F3, 4), "fy6-s3-d-vsG": round(Fc / G3, 3)})

# fy6-s4: camera flash (C = 330 uF, 300 V before, 220 V after, 1,0 ms)
C4, U4a, U4b, t4 = 330e-6, 300.0, 220.0, 1.0e-3
Ea, Eb = 0.5 * C4 * U4a ** 2, 0.5 * C4 * U4b ** 2
dE = Ea - Eb
dQ = C4 * (U4a - U4b)
out.update({"fy6-s4-a": round(Ea, 3), "fy6-s4-b": round(dE, 3), "fy6-s4-b-Eb": round(Eb, 3), "fy6-s4-b-share": round(dE / Ea, 4),
            "fy6-s4-c": round(dQ / t4, 3), "fy6-s4-c-dQ": round(dQ * 1e3, 3), "fy6-s4-c-P": round(dE / t4, 1),
            "fy6-s4-Qa": round(C4 * U4a, 4), "fy6-s4-d-I": round(U4a / 1000.0, 3), "fy6-s4-d-Ires": round(U4a / 10e3 * 1e3, 3)})
print(json.dumps(out))
```

## lessons/FY6/sovella/figures.py
```
"""Figures of FY6 Sovella itsenäisesti (scripts/figlib.py); `python scripts/practice.py figures FY6` writes them into
solutions.md. Three are task figures (the measuring circuit of s1, the lamp circuit of s2, the plates of s3) that carry
no answer; fy6-s1-graph is the model graph of s1 a. Circuit diagrams with IEC symbols: resistor a rectangle, cell a long
thin (+) and a short thick (-) plate, lamp a circle with a cross, meters circles with their letter, fuse a rectangle with
a line through it; conventional current + -> - in violet (#7048e8) as in the other FY6 chapters; field lines green."""
from figlib import Fig, Axes, fi, INK, MUTED, WHITE, RULE, HOT, HOT_LIGHT, COLD, GLASS, GOOD, n

CUR = "#7048e8"     # conventional current
POT = COLD          # voltages and potentials
FIELD = GOOD        # electric field lines and arrows (#2b8a3e)


def wire(f, *pts):
    f.add('<polyline points="' + " ".join(f"{n(x)},{n(y)}" for x, y in pts) + f'" fill="none" stroke="{INK}" '
          'stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>')


def resistor(f, x, y, vertical=False, length=64, width=24):
    w, h = (width, length) if vertical else (length, width)
    f.rect(x - w / 2, y - h / 2, w, h, WHITE, INK, 3)


def fuse(f, x, y, length=64, width=24):
    f.rect(x - length / 2, y - width / 2, length, width, WHITE, INK, 3)
    f.line(x - length / 2, y, x + length / 2, y, INK, 2)


def lamp(f, x, y, r=22):
    f.circle(x, y, r, WHITE, INK, 3)
    d = r * 0.7071
    f.line(x - d, y - d, x + d, y + d, INK, 3); f.line(x - d, y + d, x + d, y - d, INK, 3)


def cell(f, x, y, gap=16):
    """Plates of a source on a vertical wire at x, centred on y: long thin (+) above, short thick (-) below."""
    f.line(x - 26, y - gap / 2, x + 26, y - gap / 2, INK, 3)
    f.line(x - 13, y + gap / 2, x + 13, y + gap / 2, INK, 7)


def node(f, x, y):
    f.circle(x, y, 6, INK)


def meter(f, x, y, letter):
    f.circle(x, y, 20, WHITE, INK, 3)
    f.tex(x, y, r"\text{" + letter + "}", "middle", w=30)


def head(f, x, y, d, colour=CUR):
    s = 10
    pts = {"r": [(x + s, y), (x - s, y - s * 0.8), (x - s, y + s * 0.8)], "l": [(x - s, y), (x + s, y - s * 0.8), (x + s, y + s * 0.8)],
           "d": [(x, y + s), (x - s * 0.8, y - s), (x + s * 0.8, y - s)], "u": [(x, y - s), (x - s * 0.8, y + s), (x + s * 0.8, y + s)]}[d]
    f.path("M" + " L".join(f"{n(a)},{n(b)}" for a, b in pts) + " Z", colour)


def new(fid, h, label):
    f = Fig(fid, h, label)
    f.wcover = 10
    return f


# --- fy6-s1 task figure: the measuring circuit -------------------------------------------------------------------
def circuit1():
    f = new("fy6-s1-circuit", 310, "Kytkentäkaavio, ei mittakaavassa: pariston mittaus. Vasemmalla on tutkittava paristo, plusnapa ylhäällä. "
            "Plusnavalta johdin kulkee ylhäällä ampeerimittarin A kautta oikealle ja alas säädettävän vastuksen R kautta takaisin "
            "miinusnavalle. Jännitemittari V on kytketty suoraan pariston napojen väliin. Violetit nuolet näyttävät virran I "
            "suunnan plusnavalta kuorman kautta miinusnavalle.")
    xb, xv, xr, top, bot = 90, 200, 500, 70, 270
    wire(f, (xb, top), (xr, top), (xr, 135)); wire(f, (xr, 195), (xr, bot), (xb, bot), (xb, 160)); wire(f, (xb, top), (xb, 134))
    cell(f, xb, 147)
    f.tex(xb - 30, 128, "+", "end", w=24); f.tex(xb - 30, 166, "-", "end", w=24)
    node(f, xv, top); node(f, xv, bot)
    wire(f, (xv, top), (xv, 150)); wire(f, (xv, 190), (xv, bot))
    meter(f, xv, 170, "V")
    f.tex(xv + 30, 170, "U", "start", POT, w=30)
    meter(f, 340, top, "A")
    resistor(f, xr, 165, True, 60)
    f.arrow(xr - 30, 200, xr + 30, 130, INK, 2.5, 12)
    f.tex(xr + 40, 165, "R", "start", w=30)
    head(f, 270, top, "r"); f.tex(270, top - 24, "I", "middle", CUR, w=24)
    head(f, xr, 100, "d"); head(f, 340, bot, "l")
    return f.svg()


# --- fy6-s1 a: the model graph ------------------------------------------------------------------------------------
I1 = [0.10, 0.20, 0.30, 0.40, 0.50, 0.60]
U1 = [4.48, 4.37, 4.22, 4.13, 3.99, 3.89]


def graph1():
    f = new("fy6-s1-graph", 380, "Kuvaaja: pariston napajännite U voltteina virran I funktiona ampeereina. Kuusi mustaa pistettä "
            "virroilla 0,10–0,60 A; jännite pienenee arvosta 4,48 V arvoon 3,89 V. Pisteisiin on sovitettu suora, joka kulkee "
            "pisteiden lomitse, ja sitä on jatkettu katkoviivana pystyakselille kohtaan 4,60 V. Suoralta on merkitty pisteet "
            "(0,10 A; 4,48 V) ja (0,60 A; 3,88 V) sekä niiden väliin kulmakertoimen kolmio, jossa virran muutos on 0,50 A ja "
            "jännitteen muutos −0,60 V. Pystyakselin asteikko alkaa arvosta 3,6 V.")
    ax = Axes(f, (96, 320), (500, 66), x=(0, 0.8), y=(3.6, 4.8), xticks=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],
              yticks=[3.8, 4.0, 4.2, 4.4, 4.6, 4.8], xlabel=r"I\ (\text{A})", ylabel=r"U\ (\text{V})",
              xfmt=lambda v: fi(v, 1), yfmt=lambda v: fi(v, 1), origin_label=False)
    f.tex(ax.x0 - 12, ax.y0 - 4, "3{,}6", "end"); f.tex(ax.x0, ax.y0 + 24, "0", "middle")
    E, Rs = 4.60, 1.2
    ax.line([(0.06, E - Rs * 0.06), (0.77, E - Rs * 0.77)], INK, 2.5)
    ax.line([(0, E), (0.06, E - Rs * 0.06)], INK, 2.5, dash="8 6")
    for i, u in zip(I1, U1): ax.point(i, u)
    # slope triangle between the line's points at 0,10 A and 0,60 A
    ua, ub = 4.48, 3.88
    f.line(ax.X(0.10), ax.Y(ua), ax.X(0.60), ax.Y(ua), MUTED, 1.5, "6 5")
    f.line(ax.X(0.60), ax.Y(ua), ax.X(0.60), ax.Y(ub), MUTED, 1.5, "6 5")
    for i, u in ((0.10, ua), (0.60, ub)): f.circle(ax.X(i), ax.Y(u), 11, "none", INK, 1.5)
    f.tex((ax.X(0.10) + ax.X(0.60)) / 2, ax.Y(ua) + 24, r"\Delta I = 0{,}50\,\text{A}", "middle", w=150, bg=True)
    f.tex(ax.X(0.60) + 12, (ax.Y(ua) + ax.Y(ub)) / 2, r"\Delta U = -0{,}60\,\text{V}", "start", w=170, bg=True)
    f.circle(ax.X(0), ax.Y(E), 6.5, WHITE, INK, 2.5)
    f.tex(ax.X(0) + 16, ax.Y(E) - 22, r"E = 4{,}60\,\text{V}", "start", w=130)
    return f.svg()


# --- fy6-s2 task figure: cable, fuse and two lamps ---------------------------------------------------------------
def circuit2():
    f = new("fy6-s2-circuit", 310, "Kytkentäkaavio, ei mittakaavassa: mökin valaistus. Vasemmalla on 12 voltin akku, plusnapa ylhäällä. "
            "Plusnavalta johdin kulkee ylhäällä sulakkeen ja kaapelin resistanssin Rk kautta kahteen rinnan kytkettyyn lamppuun. "
            "Lamppu A on merkitty 12 V, 24 W ja lamppu B 12 V, 12 W. Alajohdin palaa lampuilta akun miinusnavalle. Violetit nuolet "
            "näyttävät virran suunnan.")
    xb, xa, xl, top, bot, yl = 80, 360, 480, 70, 270, 165
    wire(f, (xb, top), (xl, top), (xl, yl - 22)); wire(f, (xl, yl + 22), (xl, bot), (xb, bot), (xb, 160)); wire(f, (xb, top), (xb, 134))
    wire(f, (xa, top), (xa, yl - 22)); wire(f, (xa, yl + 22), (xa, bot))
    cell(f, xb, 147)
    f.tex(xb - 30, 128, "+", "end", w=24); f.tex(xb - 30, 166, "-", "end", w=24)
    f.tex(xb + 34, 147, r"E", "start", POT, w=30)
    fuse(f, 170, top, 60)
    f.tex(170, top - 30, r"\text{sulake}", "middle", w=90)
    resistor(f, 290, top, False, 64)
    f.tex(290, top - 30, r"R_\text{k}", "middle", w=44)
    node(f, xa, top); node(f, xa, bot)
    lamp(f, xa, yl); lamp(f, xl, yl)
    for x, name, v, w in ((xa, "A", r"12\,\text{V}", r"24\,\text{W}"), (xl, "B", r"12\,\text{V}", r"12\,\text{W}")):
        f.tex(x + 34, yl - 28, r"\text{" + name + "}", "start", INK, w=30)
        f.tex(x + 34, yl, v, "start", MUTED, 21, w=70)
        f.tex(x + 34, yl + 26, w, "start", MUTED, 21, w=70)
    head(f, 232, top, "r"); f.tex(232, top - 28, "I", "middle", CUR, w=24)
    head(f, 338, top, "r")
    head(f, 200, bot, "l")
    return f.svg()


# --- fy6-s3 task figure: the plates of the spray gun -------------------------------------------------------------
def field3():
    f = new("fy6-s3-field", 350, "Kaaviokuva, ei mittakaavassa: ruiskumaalauksen sähkökenttä. Ylhäällä on vaakasuora suutinlevy, jonka "
            "potentiaali on +60 kV, ja alhaalla maadoitettu työkappale. Levyjen etäisyys on d. Levyjen välissä homogeenisen "
            "sähkökentän kenttäviivat ovat vihreitä suoria viivoja ylhäältä alas, ja kenttä on merkitty E-vektorilla. Suutinlevyn "
            "vieressä on positiivisesti varautunut maalipisara varauksella q, joka lähtee levyltä.")
    xl, xr, yt, yb = 150, 500, 70, 290
    f.rect(xl, yt - 12, xr - xl, 12, "#adb5bd", INK, 2.5); f.rect(xl, yb, xr - xl, 12, "#adb5bd", INK, 2.5)
    for x in (200, 280, 360, 440):
        f.arrow(x, yt + 4, x, yb - 4, FIELD, 2.5, 13)
    f.tex(xl - 22, yt - 6, r"+60\,\text{kV}", "end", w=100); f.tex(xl - 22, yb + 6, r"0\,\text{V}", "end", w=70)
    f.tex(xl + 4, yt - 40, r"\text{suutinlevy}", "start", MUTED, w=120); f.tex(xl + 4, yb + 40, r"\text{työkappale}", "start", MUTED, w=130)
    f.tex(xr - 4, 180, r"\overline{E}", "end", FIELD, w=40)
    f.arrow(40, 180, 40, yt + 6, MUTED, 2, 11); f.arrow(40, 180, 40, yb - 6, MUTED, 2, 11)
    f.tex(54, 180, "d", "start", MUTED, w=24)
    f.circle(280, yt + 22, 16, HOT_LIGHT, INK, 2.5)
    f.tex(280, yt + 22, "+", "middle", w=24)
    f.tex(306, yt + 22, "q", "start", w=24)
    return f.svg()


FIGURES = {"fy6-s1-circuit": circuit1, "fy6-s1-graph": graph1, "fy6-s2-circuit": circuit2, "fy6-s3-field": field3}
REUSE = {
    "fy6-s1-circuit": "safe: the measuring circuit of the battery experiment (task fy6-s1)",
    "fy6-s1-graph": "reveals: the model graph, line and values of task fy6-s1 a and b (its solution)",
    "fy6-s2-circuit": "safe: the cable, fuse and two lamps with their ratings, no results (task fy6-s2)",
    "fy6-s3-field": "safe: the plates and the uniform field of the spray gun, symbols only (task fy6-s3)",
}
```
