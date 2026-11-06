# Arviointi ilman Apps Scriptiä: paikallinen arviointisivu (FY1–FY8)

Eduespoossa Apps Script on estetty (Google Admin: *you do not have access to this service*, 5.11.2026). Siksi
arviointi tehdään erillisellä HTML-tiedostolla, yksi jokaiselle kurssille: **`arviointi-fy1.html`** … **`arviointi-fy8.html`**
(6.11.2026 alkaen kaikki kurssit; ohjeen esimerkit ovat FY3:sta, muut toimivat samoin). Opettaja avaa sen omalla koneellaan
selaimessa (Chrome tai Edge). Tiedosto ei kuulu RuukkiLabraan eikä julkiseen sivustoon. Sivu ei käytä verkkoa eikä
Googlen tai Microsoftin palveluja. Se lukee Drivesta ladatut palautukset ja tallentaa pisteet vain tämän selaimen
muistiin.

Sivulla on koko FY3: kaikki 16 lukua opetusjärjestyksessä (sama kuin FY3-moduulisivulla), ja niiden tehtävät. Jokaisessa
FY3-luvussa on Tehtävät-otsikon rivillä painike **Lataa kaikki ratkaisut**. Painike lataa luvun tiedoston
`fy3-<n>.ratkaisut.json`. Painike on myös englanninkielisessä (*Download all solutions*) ja selkosuomen FY3:ssa. Tiedosto on
samanlainen, joten kaikki kielet arvioidaan samalla sivulla.

## Käyttöönotto

1. **Yksi Forms-lomake ryhmää kohti**, eduespoo-tilillä, kuten KAYTTOONOTTO.md:n kohdassa 1. Nimeä lomakkeet
   ryhmittäin, esim. *FY3.1 palautukset* ja *FY3.2 palautukset*. Tiedostokysymys *Palauta vastaukset*, enintään 10 Mt.
   Opiskelija palauttaa samalla lomakkeella jokaisen luvun erikseen, kun luku on tehty. Uusi palautus on uusi
   lomakevastaus. Sheetsiin linkittämistä ja Apps Scriptiä ei tarvita. Palautuskansio ja lomakkeen vastaukset vain
   nimetyille opettajille (KAYTTOONOTTO.md, kohta 5).
2. **Tallenna arviointisivu** kerran omalle koneelle, opettamasi kurssin sivu, esim. `fysiikkalabra/palautus/arviointi-fy3.html` (repossa, myös
   projektin tiedostoissa). Avaa se kaksoisnapsauttamalla. Sivu toimii ilman verkkoa.
3. **Lisää ryhmät** sivulla: kirjoita nimi (esim. FY3.1) ja paina **Lisää ryhmä**. Yksi ryhmä jokaista lomaketta kohti.
4. **Lomakelinkit Ruukkilabraan**: lisää ryhmän lomakkeen vastaajalinkki (Lähetä → linkki, `forms.gle/…`) tiedostoon
   `fysiikkalabra/palautukset.json` (myös periodi ja lukuvuosi). Ruukkilabraan tulee sivu *Palautukset* (esim.
   *Palautukset · 1. periodi · lv 2026-27*, englanniksi *Submissions*), jossa on kaikki kurssit ja nappi jokaiselle ryhmälle. FY3-lukujen Tehtävät-rivillä on
   Lataa kaikki ratkaisut -napin vieressä nappi **Palauta**, joka vie tälle sivulle. Periodin vaihtuessa vaihda otsikko
   ja linkit. Sivu vain linkittää lomakkeisiin, se ei lataa mitään Googlelta.

## Arviointi

1. Drivessa: napsauta ryhmän lomakkeen kansiota **<lomakkeen nimi> (File responses)** hiiren oikealla → **Lataa**.
   Drive tekee zip-tiedoston (suurista kansioista useamman).
2. Arviointisivulla: valitse **Ryhmä**, sitten **Palautukset (zip)** → valitse zip (tai kaikki
   zipit kerralla). Sivu tarkistaa tiedostot ja näyttää käsittelytilan: hyväksytty, kaksoiskappale, tarkistettava
   (sama palautustunniste kahdella opiskelijalla), virheellinen (syy näkyy). Tarkistettavan voi hyväksyä ja hyväksytyn
   hylätä rivin painikkeella.
3. **Ryhmät pysyvät erillään.** Ryhmä muistaa, miltä lomakkeelta sen palautukset tulivat (zipin ylin kansio). Toisen
   lomakkeen zipiä se ei lue, vaan kertoo, että valittu ryhmä on väärä. Jokaisella ryhmällä on omat opiskelijat, pisteet,
   CSV ja varmuuskopio.
4. **Kooste** (ylhäällä): opiskelijat aakkosjärjestyksessä ja sarakkeet **Tehty** (tehtäviä, joihin on ratkaisu / tehtäviä),
   **Tarkistamatta** (tehtyjä ilman pisteitä) ja **Pisteet** (summa / enimmäispisteet). Valinnasta saa kaikki palautetut
   luvut yhdessä tai yhden luvun. Sarakkeen otsikko järjestää taulukon (uusi napsautus kääntää järjestyksen). Luvut
   lasketaan opiskelijan uusimmasta hyväksytystä palautuksesta.
5. **Tehtävät**: jokainen luku on oma laatikkonsa, ja ne luvut, joista on palautuksia, ovat auki. Valitse tehtävä ja
   arvioi sen kaikki palautukset peräkkäin. Jonossa ovat vain ne opiskelijat, jotka ovat palauttaneet kyseisen luvun.

   | Näppäin | Toiminto |
   |---|---|
   | ↓ / ↑ | seuraava / edellinen opiskelija (pisteet tallentuvat ennen siirtymistä) |
   | → / ← | +1 p / −1 p, rajat 0 ja 1, tallentuu heti; tyhjästä → antaa 1 ja ← antaa 0 |
   | 0, 1 | pisteet suoraan, tallentuu heti |
   | Backspace | tyhjä = arvioimaton |
   | , | siirtyy pistekenttään desimaalia varten (esim. 0,5) |
   | kentässä Enter, ↓, ↑ | tallentaa, siirtyy ja poistuu kentästä, jolloin nuolet toimivat taas |

   Pisteet tehtävää kohti 0–1, enintään kaksi desimaalia (0,5 tai 0,25). Tyhjä = arvioimaton, 0 = annettu nolla.
   Viimeisellä opiskelijalla ↓ tallentaa ja kertoo, että tehtävä on käyty läpi. Jos tallennus epäonnistuu, siirtymistä
   ei tapahdu.
6. **Vie pisteet (CSV)** lataa tiedoston `FY3-<ryhmä>-pisteet.csv`: opiskelija, pisteet luvuittain (tyhjä, jos lukua ei
   ole palautettu), yhteensä, palautettujen lukujen määrä, Tehty ja Tarkistamatta. Desimaalierotin on pilkku. Avaa
   tiedosto Sheetsissä (Tiedosto → Tuo) tai Excelissä. Kaavoiksi tulkittavat merkit on suojattu.
7. **Varmuuskopio** lataa ryhmän tuonnin tilan ja pisteet JSON-tiedostona. Säilytä se koulun Drivessa, ei julkisesti.
   **Palauta varmuuskopio** tuo sen takaisin valittuun ryhmään (esim. toisella koneella). **Poista ryhmä** poistaa
   ryhmän ja sen arvioinnin tästä selaimesta.
8. Kun uusia palautuksia tulee, lataa kansio uudelleen ja valitse uusi zip samaan ryhmään. Jo luetut ohitetaan ja uudet
   lisätään. Korjattu palautus on opiskelijan uusi versio samasta luvusta, ja vanhan pisteet säilyvät vanhalla
   versiolla.

Sivu ei säilytä palautustiedostoja. Kun avaat sivun seuraavan kerran, ryhmät, pisteet ja tilat ovat tallessa, mutta
vastausten näyttämistä varten valitse ryhmän zip uudelleen.

## Tunniste ja aika

- **Opiskelija** tunnistetaan nimestä, jonka Forms lisää palautetun tiedoston nimeen:
  `fy3-4.ratkaisut - Etunimi Sukunimi.json`. Nimi tulee opiskelijan kirjautuneesta eduespoo-tilistä.
  Vahvistettu sähköposti näkyy tarvittaessa lomakkeen vastauksissa.
- **Luku** luetaan tiedoston sisällöstä, ei tiedoston nimestä.
- **Palautusaika** on tiedoston aika Driven zipissä. Järjestys ei perustu opiskelijan tiedoston omaan aikaleimaan.
- Nimi, aika ja zipin kansiorakenne on varmistettava ensimmäisessä kokeessa (alla).

## Tietoturva

- Zip sisältää opiskelijoiden töitä: pidä se koulun koneella ja poista Lataukset-kansiosta arvioinnin jälkeen.
- Sivu tallentaa selaimen muistiin (localStorage) ryhmittäin tuonnin tilan, opiskelijoiden nimet ja pisteet, ei
  vastauksia. Käytä omaa, henkilökohtaista koulun konetta, älä yhteiskäyttöistä. Kurssin jälkeen: **Poista ryhmä**.
- Sivu ei lataa mitään verkosta (Content-Security-Policy estää sen), ei suorita palautuksista koodia eikä näytä
  niistä HTML:ää. Kuvina näytetään vain tarkistetut PNG- ja JPEG-kuvat.

## Varmistettava ensimmäisessä kokeessa (keksityillä vastauksilla)

1. Kaksi opiskelijan testitiliä palauttavat lomakkeella kahden eri luvun tiedostot, ja toinen niistä palauttaa yhden
   luvun toisen kerran.
2. Lataa lomakkeen kansio zipinä ja valitse se sivulla. Tarkista, että **oikea nimi**, **oikea luku** ja **järkevä
   palautusaika** näkyvät (vertaa lomakkeen vastauksiin). Jos nimi puuttuu tai jokin on väärin, kerro, niin korjaan
   tunnistuksen.
3. Tee toinen lomake toiselle ryhmälle ja kokeile sen zipiä ensin väärään ryhmään (sivun pitää kieltäytyä) ja sitten
   oikeaan.
4. Arvioi muutama tehtävä, katso Pisteet luvuittain, vie CSV ja avaa se Sheetsissä.
5. Sulje ja avaa sivu ja valitse zip uudelleen. Pisteiden pitää olla tallessa, ja uusia rivejä pitää tulla 0.
6. Opiskelijan testitili ei pääse palautuskansioon eikä lomakkeen vastauksiin.

Sivu on testattu automaattisesti (`scripts/test_palautus.py`) itse tehdyillä zip-tiedostoilla, joiden kansiot ja
tiedostonimet ovat Formsin muotoa: kaksi ryhmää, kaksi lukua. Oikeaa Driven zipiä ei ole vielä testattu.
