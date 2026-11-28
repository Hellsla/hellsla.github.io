# Pedagoginen viitekehys tekijöille

Sisäinen dokumentti Ruukkilabran tekijöille ja katselmoijille (työjono 38; opettaja 2026-11-28: "Add theoretical framework",
paikka "Internal doc for authors", lähteistä "Yes, checked sources"). Se ei ole sivuston sisältöä eikä uusi sääntö: se kertoo,
mihin tutkimukseen talon säännöt nojaavat tai muistuttavat. Säännöt ovat `CLAUDE.md`:ssä, `docs/inquiry-spec.md`:ssä ja
`NOTES.md`:ssä; jos tämä dokumentti ja sääntö ovat ristiriidassa, sääntö on voimassa.

## Lue ensin: kuinka vahva yhteys on

Repo ei aiemmin nimennyt viitekehyksiä. Säännöt syntyivät opettajan päätöksinä (`docs/decisions/`, `NOTES.md`), ja tämä
kartoitus on tehty jälkikäteen. Siksi jokaisella rivillä on merkintä:

- **Johdettu**: sääntö otettiin käyttöön nimenomaan tämän tutkimuksen takia (vain jos repo itse sen sanoo).
- **Vastaa**: sääntö toteuttaa tutkimuksen ajatusta, mutta sen yksityiskohdat (määrät, päivät, vaiheiden lukumäärä) ovat talon omia valintoja.
- **Muistuttaa**: sääntö on lähellä tutkimusta, mutta tutkimus ei tue sitä sellaisenaan.

Yksikään rivi ei ole "johdettu": tutkimusta ei ole kirjattu minkään säännön perusteeksi. Älä siis kirjoita sivustolle tai
katselmointiin, että jokin sääntö "perustuu tutkimukseen"; sano, mihin se vastaa tai muistuttaa. Tuloksia tai efektikokoja
ei toisteta tässä; ne pitää lukea alkuperäisistä lähteistä. Lähteiden tarkistuksen laajuus on kohdassa "Tarkistus".

## 1. Seitsemän vaihetta: tutkiva oppiminen, POE ja 5E
- **Sääntö**: Pohdinta → Ennusta → Tutki → Teoria → Esimerkit → Tehtävät → Testaa ja arvioi, ei kiinteää mallipohjaa (`CLAUDE.md` "Lesson form" 5; `inquiry-spec.md`; `NOTES.md` §5). **Vastaa.**
- **Idea**: tutkiva oppiminen etenee orientaatiosta käsitteellistämiseen, tutkimiseen, johtopäätöksiin ja keskusteluun. Predict–Observe–Explain pyytää ennustamaan ja perustelemaan ennen havaintoa ja selittämään sen jälkeen. 5E-malli (engage, explore, explain, elaborate, evaluate) on sama kaari opetusmallina. Vaiheiden vastaavuus 5E:hen (Pohdinta ≈ engage, Ennusta ja Tutki ≈ explore, Teoria ≈ explain, Esimerkit ja Tehtävät ≈ elaborate, Testaa ja arvioi ≈ evaluate) on tämän dokumentin tulkinta, ei lähteiden.
- **Lähteet**: Pedaste ym. 2015; White & Gunstone 1992; Bybee ym. 2006.

## 2. Sitoutuva ennuste ja käsitteellinen muutos
- **Sääntö**: ennuste sitoudutaan ennen todistusaineistoa; palaute riippuu sitoutumisesta, ei pääsystä; vastausta ei paljasteta ennen kuin opiskelija on toiminut (`CLAUDE.md` "Lesson form" 5; "Ennusta shows its first prediction at once"). **Vastaa.**
- **Idea**: käsitys vaihtuu todennäköisemmin, kun opiskelija huomaa vanhan käsityksensä riittämättömäksi ja uusi on ymmärrettävä, uskottava ja hedelmällinen. Ennuste tekee vanhan käsityksen näkyväksi ennen kuin havainto haastaa sen.
- **Lähteet**: Posner ym. 1982; White & Gunstone 1992.

## 3. Virhekäsityksiin perustuvat vaihtoehdot
- **Sääntö**: monivalintojen väärät vaihtoehdot ja palaute rakennetaan tunnetuista virhekäsityksistä; "Yleinen virhekäsitys" on suljettu laatikko (`inquiry-spec.md` "Multiple choice with misconception-specific feedback"; `NOTES.md` §5, §9; `CLAUDE.md` "Lesson page"). **Vastaa.**
- **Idea**: fysiikan diagnostinen testi (Force Concept Inventory) rakennetaan siten, että väärät vaihtoehdot ovat opiskelijoiden yleisiä arkikäsityksiä, jolloin valinta kertoo, mikä käsitys on kyseessä. Talo ei käytä FCI:n kysymyksiä (`CLAUDE.md` "Never": ei kopioida), vain periaatetta.
- **Lähteet**: Hestenes ym. 1992.

## 4. Vaiheittaiset esimerkit
- **Sääntö**: mallitehtävä on seitsemässä vaiheessa, jotka sivu paljastaa yksi kerrallaan; ratkaise ensin symbolisesti; täydellinen mallivastaus joka tehtävälle (`CLAUDE.md` "Lesson form" 2, 4, 7). **Vastaa.**
- **Idea**: kognitiivisen kuormituksen teoriassa työn alla olevan tiedon määrä rajoittuu; aloittelijalle valmiiksi ratkaistu esimerkki voi opettaa tehokkaammin kuin hakuun perustuva ratkaisuyritys. Vaiheiden lukumäärä (7) ja yksi kerrallaan paljastaminen ovat talon valintoja, eivät tutkimuksen tuloksia.
- **Lähteet**: Sweller 1988; Sweller & Cooper 1985.

## 5. Yritä ensin ja vihjeportaat
- **Sääntö**: numeerinen tehtävä on lukittu yhteen yritykseen asti; vihjeet ovat aina auki; mallivastaus aukeaa "Olen tehnyt ratkaisun" -painikkeen jälkeen; kolme asteittaista vihjettä ja yleisten virheiden palaute (`CLAUDE.md` "Lesson page" Yritä ensin; `NOTES.md` §5; `inquiry-spec.md` "progressive optional hints"). **Vastaa osittain, muistuttaa osittain.**
- **Idea**: itse tuotettu vastaus muistetaan paremmin kuin luettu (generation effect). Vaikea ensimmäinen yritys voi valmistaa oppimista, kun ohjaus tulee sen jälkeen (productive failure). Tukirakenteet (scaffolding) vähentävät tukea sitä mukaa kuin osaaminen kasvaa. Huom.: tutkimukset koskevat sanojen tuottamista ja pidempää omaa ratkaisemista; talon yksi yritys ja vihjeportaat ovat näitä pienempi ja ohjatumpi ratkaisu.
- **Lähteet**: Slamecka & Graf 1978; Kapur 2008; Wood, Bruner & Ross 1976.

## 6. Pohdinnan kertaus ja konseptikortit 5/10/20 vrk
- **Sääntö**: Pohdinnan kertaustehtävä ("Kertaa yläkoulusta"); konseptikortti palaa pakasta 5, 10 ja 20 vrk:n kuluttua (`CLAUDE.md` "Lesson page", "Parts specified in `docs/decisions/oppituntisivun-osat.md`"; `docs/decisions/oppituntisivun-osat.md`). **Vastaa.** Päivämäärät 5/10/20 ovat talon valinta; repo ei perusta niitä tutkimukseen.
- **Idea**: muistista palauttaminen (retrieval practice) vahvistaa pitkäaikaista muistia enemmän kuin uudelleen lukeminen, ja toistojen hajauttaminen ajassa (spacing) auttaa; sopiva väli riippuu siitä, kuinka pitkään asia halutaan muistaa.
- **Lähteet**: Roediger & Karpicke 2006; Cepeda ym. 2006.

## 7. Kuva tekstin vieressä
- **Sääntö**: jokaisessa Ydinajatuksessa ja Kaavassa vähintään yksi kuva heti selittämänsä kappaleen jälkeen; kuvat ja pienet taulukot selitettävän vieressä leveällä näytöllä; ei kuvaa kaukana selityksestä; kuvan tekstit LaTeXina (`CLAUDE.md` "Lesson form" 1; "Figures"; `NOTES.md` §3, §8). **Vastaa.**
- **Idea**: multimedian periaatteissa kuva ja siihen liittyvä teksti ovat lähellä toisiaan (spatial contiguity) ja turhat lisät jätetään pois (coherence). Talon "ei mitään, mitä lukija ei tarvitse" -sääntö muistuttaa jälkimmäistä.
- **Lähteet**: Mayer 2009.

## 8. Itsearvio kriteereihin
- **Sääntö**: ei luvun tasoista "Osaan / Tarvitsen vielä harjoitusta" -listaa; kirjoitettu vastaus arvioidaan mallivastauksen havaittavia kriteerejä vasten; varmuus ei ole näyttö (`CLAUDE.md` "Exercise levels…" Self-assessment; `NOTES.md` §9, §11). **Vastaa.**
- **Idea**: formatiivinen arviointi tuottaa tietoa, jota käytetään opetuksen tai opiskelun suuntaamiseen; kriteerit ja palaute auttavat opiskelijaa näkemään, mitä vielä puuttuu.
- **Lähteet**: Black & Wiliam 1998.

## 9. Tasot: perus → soveltava → haastava → Sovella itsenäisesti
- **Sääntö**: tehtävätasot 1 perus, 2 soveltava, 3 haastava; moduulin lopussa Sovella itsenäisesti; tutkiva ydin pysyy perustana, yo-tyyliset kysymykset eivät leviä joka vaiheeseen (`CLAUDE.md` "Exercise levels…"; `NOTES.md` §9). **Muistuttaa.**
- **Idea**: tuki vähenee vähitellen (scaffolding) ja esimerkkien jälkeen siirrytään itsenäiseen ratkaisemiseen; sama kaari kuin kohdissa 4 ja 5. Tasojen rajat (yksi vaihe, kaksi vaihetta, päättely) ovat talon omia.
- **Lähteet**: Wood, Bruner & Ross 1976; Sweller & Cooper 1985.

## 10. Selkeä suomi ja saavutettavuus
- **Sääntö**: `content/fi-easy/` S2-opiskelijoille: vaikeat sanat selitetään ensimmäisellä kerralla, 3–5 *Luvun tärkeää käsitettä*; yksi lukupalsta, ei vierekkäisiä tehtäviä; ääneenluku (`CLAUDE.md` "Selkeä suomi", "Lesson page"; `NOTES.md` §8, §12). **Muistuttaa.**
- **Idea**: selkokieli on sisällöltään, sanastoltaan ja rakenteeltaan tavallista helpompaa suomea; WCAG on verkkosisällön saavutettavuuden kansainvälinen suositus. Talon fi-easy ei ole virallinen selkokieli eikä sivusto väitä täyttävänsä WCAG-tasoa, ellei erikseen todeta.
- **Lähteet**: Selkokeskus; W3C 2023 (WCAG 2.2).

## 11. FY9-valmentaja: mastery learning
- **Sääntö**: valmentaja suosittelee seuraavan tehtävän tämän laitteen tallenteen perusteella; lähtötasotesti ja kertaus moduuleittain; ei seurantaa, kirjautumista eikä tietojen keruuta (`CLAUDE.md` "FY9 coach"; `docs/FY9_ADAPTIVE_PLAN.md`; työjono 33). **Muistuttaa.**
- **Idea**: mastery learning etenee yksiköissä, joissa osaaminen todetaan ennen seuraavaa, ja puutteisiin annetaan korjaavaa harjoitusta. FY9 ei kuitenkaan estä etenemistä eikä "hyväksy" yksikköä, joten kyseessä on vain sukua oleva ajatus.
- **Lähteet**: Kulik, Kulik & Bangert-Drowns 1990.

## 12. LOPS 2019 -painotukset
Lukion opetussuunnitelman perusteet 2019 on ohjaava määräys; `docs/lops2019/` sisältää MAOL:n ja OPH:n tukimateriaalit (FY1–FY8; FY9 on kertauskurssi). Näistä kolme painotusta näkyy talon säännöissä:
- **Tutkimuksellisuus.** Fysiikka on tutkimuksellinen oppiaine; tutkimuksellisuus voi olla myös videoita, demonstraatioita tai simulaatioita, ei aina varsinaista koetyötä. → kohta 1; "simulaatio on mukana sen opettavuuden takia" (`CLAUDE.md` "Lesson form" 5).
- **Fysiikan luku- ja kirjoitustaidot.** Opiskelija tulkitsee kuva- ja mittausaineistoa, kuvaa ilmiön, määrittelee käsitteen ja perustelee kirjallisesti. → kohdat 7, 8 ja kirjoitetut vastaukset itsearvioon.
- **Laaja-alainen osaaminen ja ehjä käsiterakenne.** Perusteissa sisältöjä on kevennetty, jotta jää aikaa pohdintaan, kokeellisuuteen ja laaja-alaisen osaamisen tavoitteille; moduulien sisällöt ovat minimivaatimuksia ja käsiterakenteen tulee pysyä ehjänä. → kohdat 1–2; `curriculum.json` kantaa moduulien tavoitteet.

## Lähteet (tarkistettu verkosta, katso "Tarkistus")
- Black, P. & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice* 5(1), 7–74.
- Bybee, R. W., Taylor, J. A., Gardner, A., Van Scotter, P. ym. (2006). *The BSCS 5E Instructional Model: Origins and Effectiveness*. BSCS; raportti NIH:n Office of Science Educationille. https://www.azed.gov/sites/default/files/media/BSCS_5E_Full_Report.pdf
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T. & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin* 132(3), 354–380. https://doi.org/10.1037/0033-2909.132.3.354
- Hestenes, D., Wells, M. & Swackhamer, G. (1992). Force Concept Inventory. *The Physics Teacher* 30(3), 141–158. https://doi.org/10.1119/1.2343497
- Kapur, M. (2008). Productive failure. *Cognition and Instruction* 26(3), 379–424.
- Kulik, C.-L. C., Kulik, J. A. & Bangert-Drowns, R. L. (1990). Effectiveness of mastery learning programs: A meta-analysis. *Review of Educational Research* 60(2), 265–299. https://doi.org/10.3102/00346543060002265
- Mayer, R. E. (2009). *Multimedia Learning* (2. painos). Cambridge University Press. https://doi.org/10.1017/CBO9780511811678
- Pedaste, M., Mäeots, M., Siiman, L. A., de Jong, T., van Riesen, S. A. N., Kamp, E. T., Manoli, C. C., Zacharia, Z. C. & Tsourlidaki, E. (2015). Phases of inquiry-based learning: Definitions and the inquiry cycle. *Educational Research Review* 14, 47–61. https://doi.org/10.1016/j.edurev.2015.02.003
- Posner, G. J., Strike, K. A., Hewson, P. W. & Gertzog, W. A. (1982). Accommodation of a scientific conception: Toward a theory of conceptual change. *Science Education* 66(2), 211–227. https://doi.org/10.1002/sce.3730660207
- Roediger, H. L. & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science* 17(3), 249–255. https://doi.org/10.1111/j.1467-9280.2006.01693.x
- Slamecka, N. J. & Graf, P. (1978). The generation effect: Delineation of a phenomenon. *Journal of Experimental Psychology: Human Learning and Memory* 4(6), 592–604.
- Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science* 12(2), 257–285.
- Sweller, J. & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction* 2(1), 59–89.
- White, R. & Gunstone, R. (1992). *Probing Understanding*. London: Falmer Press. (ISBN 9780750700481)
- Wood, D., Bruner, J. S. & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry* 17(2), 89–100. https://doi.org/10.1111/j.1469-7610.1976.tb00381.x
- Selkokeskus: selkokielen esittely. https://selkokeskus.fi/in-english/easy-finnish/
- W3C (2023). *Web Content Accessibility Guidelines (WCAG) 2.2*. W3C Recommendation 5.10.2023. https://www.w3.org/TR/WCAG22/
- Opetushallitus (2019). *Lukion opetussuunnitelman perusteet 2019*. Määräykset ja ohjeet 2019:2a. https://www.oph.fi/fi/tilastot-ja-julkaisut/julkaisut/lukion-opetussuunnitelman-perusteet-2019 ; MAOL & OPH: fysiikan tukimateriaalit https://www.oph.fi/fi/koulutus-ja-tutkinnot/fysiikan-ja-kemian-lops-tukimateriaalit

## Tarkistus (2026-11-28)
Jokaisen yllä olevan lähteen tekijät, vuosi, nimi ja julkaisija tai lehti on varmistettu verkkohaulla (kustantajan, PubMedin,
yliopistotietokannan tai kirjastoluettelon tiedoista). Alkuperäisiä artikkeleita ei ole luettu kokonaan: tässä esitetyt
tutkimusten ideat ovat yleisiä, hakutulosten tiivistelmien tukemia kuvauksia, eivät tarkkoja tuloksia.

**Tarkistamatta (ei kirjattu tai kirjattu ilman):**
- DOI puuttuu tarkoituksella, koska sitä ei saatu varmistettua: Black & Wiliam 1998, Kapur 2008, Slamecka & Graf 1978, Sweller 1988 (hakutulokset antavat kaksi eri DOI:ta), Sweller & Cooper 1985; White & Gunstone 1992 on kirja ilman DOI:ta.
- Bybee ym. 2006: koko tekijälistaa ei varmistettu (kirjattu "ym."); raportin pysyvää linkkiä ei löytynyt, linkki on yhden kopion osoite.
- Selkokeskus-linkki on englanninkielinen esittelysivu; selkokielen periaatteiden täydellistä luetteloa ei saatu luettua.
- Lukion opetussuunnitelman perusteiden asiakirjanumero "2019:2a" on peräisin yhden PDF-kopion kansilehdeltä; ePerusteet-palvelun nykyistä versiota ei tarkistettu.
- Jätetty pois kokonaan: ei tutkimusta, jota ei olisi saatu tarkistettua. Muita lähteitä (esim. mastery learningin alkuperäinen lähde Bloom 1968; kognitiivisen kuormituksen kirjaversiot) ei tarkistettu eikä kirjattu.
