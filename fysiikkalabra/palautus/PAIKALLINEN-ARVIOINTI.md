# Arviointi ilman Apps Scriptiä: paikallinen arviointisivu (yksi tiedosto periodia kohti)

Eduespoossa Apps Script on estetty (Google Admin: *you do not have access to this service*, 5.11.2026). Siksi
arviointi tehdään erillisellä HTML-tiedostolla, yksi kuluvaa periodia kohti: **`arviointi-2026-27-p1.html`**. Siinä ovat
kaikki periodin kurssit, eli ne, joille `palautukset.json` antaa lomakkeen (6.11.2026). Uusi periodi saa uuden tiedoston, kun
`palautukset.json` päivitetään. Opettaja avaa sen omalla koneellaan
selaimessa (Chrome tai Edge). Tiedosto ei kuulu RuukkiLabraan eikä julkiseen sivustoon. Sivu ei käytä verkkoa eikä
Googlen tai Microsoftin palveluja. Se lukee Drivesta ladatut palautukset ja tallentaa ne ja pisteet vain tämän selaimen
muistiin.

Sivulla on periodin jokaisen kurssin kaikki luvut opetusjärjestyksessä ja niiden tehtävät. Jokaisessa FY1–FY8-luvussa on Tehtävät-otsikon rivillä painike **Lataa kaikki ratkaisut**. Painike lataa luvun tiedoston
`fy3-<n>.ratkaisut.json`. Painike on myös englanniksi (*Download all solutions*) ja selkosuomeksi. Tiedosto on
samanlainen, joten kaikki kielet arvioidaan samalla sivulla.

## Käyttöönotto

1. **Yksi Forms-lomake ryhmää kohti**, eduespoo-tilillä, kuten KAYTTOONOTTO.md:n kohdassa 1. Nimeä lomakkeet
   ryhmittäin, nimi **alkaa ryhmällä**: *FY3.2 lv 2026-27 Palauta ratkaisut*. Arviointisivu tunnistaa ryhmän ja kurssin
   nimen alusta. Tiedostokysymys *Palauta vastaukset*, enintään 10 Mt.
   Opiskelija palauttaa samalla lomakkeella jokaisen luvun erikseen, kun luku on tehty. Uusi palautus on uusi
   lomakevastaus. Sheetsiin linkittämistä ja Apps Scriptiä ei tarvita. Palautuskansio ja lomakkeen vastaukset vain
   nimetyille opettajille (KAYTTOONOTTO.md, kohta 5).
2. **Tallenna arviointisivu** kerran periodissa omalle koneelle: `fysiikkalabra/palautus/arviointi-2026-27-p1.html`
   (repossa, myös projektin tiedostoissa). Avaa se kaksoisnapsauttamalla. Sivu toimii ilman verkkoa.
3. **Lomakelinkit Ruukkilabraan**: lisää ryhmän lomakkeen vastaajalinkki (Lähetä → linkki, `forms.gle/…`) tiedostoon
   `fysiikkalabra/palautukset.json` (myös periodi ja lukuvuosi). Ruukkilabraan tulee sivu *Palautukset* (esim.
   *Palautukset · 1. periodi · lv 2026-27*, englanniksi *Submissions*), jossa on kaikki kurssit ja nappi jokaiselle ryhmälle. FY3-lukujen Tehtävät-rivillä on
   Lataa kaikki ratkaisut -napin vieressä nappi **Palauta**, joka vie tälle sivulle. Periodin vaihtuessa vaihda otsikko
   ja linkit. Sivu vain linkittää lomakkeisiin, se ei lataa mitään Googlelta.

## Arviointi

1. Drivessa: napsauta ryhmän lomakkeen kansiota **<lomakkeen nimi> (File responses)** hiiren oikealla → **Lataa**.
   Drive tekee zip-tiedoston (suurista kansioista useamman).
2. Arviointisivulla: **Tuo tiedosto** → valitse zip (tai kaikkien ryhmien zipit kerralla). Ryhmä tunnistetaan zipin
   ylimmästä kansiosta eli lomakkeen nimestä, ja uusi ryhmä syntyy itse. Kun ryhmiä on useampi, **Ryhmä**-valinnasta
   vaihdetaan näkyvää ryhmää. Sivu tarkistaa tiedostot ja näyttää käsittelytilan: hyväksytty, kaksoiskappale, tarkistettava
   (sama palautustunniste kahdella opiskelijalla), virheellinen (syy näkyy). Tarkistettavan voi hyväksyä ja hyväksytyn
   hylätä rivin painikkeella.
3. **Ryhmät pysyvät erillään.** Ryhmä muistaa, miltä lomakkeelta sen palautukset tulivat (zipin ylin kansio). Toisen
   lomakkeen zipiä se ei lue samaan ryhmään. Toisen kurssin (jota ei ole tämän periodin sivulla) zipiä ei lueta. Jokaisella ryhmällä on omat opiskelijat, pisteet,
   CSV ja varmuuskopio.
4. **Kooste** (ylhäällä): opiskelijat aakkosjärjestyksessä ja sarakkeet **Tehty** (tehtäviä, joihin on ratkaisu / tehtäviä),
   **Tarkistamatta** (tehtyjä ilman pisteitä), **Pisteet** (summa / enimmäispisteet) ja **Itsearvio** (keskiarvo,
   4 = osaan niin hyvin, että voisin opettaa kaverille … 1 = tarvitsen vielä harjoitusta; luvun tavoitearvioista,
   *En ole vielä harjoitellut* ei ole mukana). Ylhäällä oleva **Luvut**-valinta (mistä luvusta mihin) rajaa koosteen, tehtävät ja sormenjäljen.
   **Osaamisen sormenjälki** näyttää koko ryhmän tavoitearviot yhdessä taulukossa: rivit ovat luvun tavoitteet luvuittain, sarakkeissa
   opiskelijat. Valkoinen = ei vastattu, harmaa = en ole vielä harjoitellut. Koko teksti näkyy hiiren alla. Sarakkeen otsikko järjestää taulukon (uusi napsautus kääntää järjestyksen). Luvut
   lasketaan opiskelijan uusimmasta hyväksytystä palautuksesta. Palkit näyttävät tehdyt tehtävät ja pisteet suhteessa
   enimmäismäärään, opiskelijoittain ja koko ryhmälle (Kooste-otsikon alla).
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
   ei tapahdu. **Piilota nimet** (Kooste-rivillä) korvaa nimet numeroilla, kun näytät pisteitä luokalle.
6. **Muut toiminnot** (pieni linkki Tuo tiedosto -napin alla): **Vie pisteet (CSV)** lataa tiedoston `FY3-<ryhmä>-pisteet.csv`: opiskelija, pisteet luvuittain (tyhjä, jos lukua ei
   ole palautettu), yhteensä, palautettujen lukujen määrä, Tehty ja Tarkistamatta. Desimaalierotin on pilkku. Avaa
   tiedosto Sheetsissä (Tiedosto → Tuo) tai Excelissä. Kaavoiksi tulkittavat merkit on suojattu.
7. **Varmuuskopio** lataa ryhmän tuonnin tilan ja pisteet JSON-tiedostona. Säilytä se koulun Drivessa, ei julkisesti.
   **Palauta varmuuskopio** tuo sen takaisin valittuun ryhmään (esim. toisella koneella). **Poista ryhmä** poistaa
   ryhmän ja sen arvioinnin tästä selaimesta.
8. Kun uusia palautuksia tulee, lataa kansio uudelleen ja valitse uusi zip samaan ryhmään. Jo luetut ohitetaan ja uudet
   lisätään (Tuo tiedosto). Korjattu palautus on opiskelijan uusi versio samasta luvusta, ja sitä arvioidaan.
   **Pisteet siirtyvät:** jos tehtävän ratkaisu on uudessa versiossa täsmälleen sama kuin aiemmassa, arvioidussa
   versiossa, tehtävä saa vanhat pisteet (arviointinäkymässä *Pisteet versiosta 1 ✓ (sama ratkaisu)*). Vain uudet ja
   muuttuneet ratkaisut jäävät arvioitaviksi. Siirretyt pisteet voi muuttaa normaalisti.

Sivu säilyttää tuodut palautukset tämän selaimen muistissa. Kun avaat sivun seuraavan kerran, ryhmät, pisteet, tilat ja
vastaukset ovat tallessa, eikä zipiä tarvitse tuoda uudelleen. Uuden periodin sivu näkee saman selaimen ryhmät ja
pisteet. Varmuuskopio sisältää pisteet ja tilat mutta ei vastauksia: toisella koneella tuo myös ryhmän zip.

## Tunniste ja aika

- **Opiskelija** tunnistetaan nimestä, jonka Forms lisää palautetun tiedoston nimeen:
  `fy3-4.ratkaisut - Etunimi Sukunimi.json`. Nimi tulee opiskelijan kirjautuneesta eduespoo-tilistä.
  Vahvistettu sähköposti näkyy tarvittaessa lomakkeen vastauksissa.
- **Luku** luetaan tiedoston sisällöstä, ei tiedoston nimestä.
- **Palautusaika** on tiedoston aika Driven zipissä. Järjestys ei perustu opiskelijan tiedoston omaan aikaleimaan.
- Nimi, aika ja zipin kansiorakenne on varmistettava ensimmäisessä kokeessa (alla).

## Tietoturva

- Zip sisältää opiskelijoiden töitä: pidä se koulun koneella ja poista Lataukset-kansiosta arvioinnin jälkeen.
- Sivu tallentaa selaimen muistiin ryhmittäin tuonnin tilan, opiskelijoiden nimet ja pisteet (localStorage) sekä
  tuodut palautustiedostot eli vastaukset (IndexedDB). Käytä omaa, henkilökohtaista koulun konetta, älä
  yhteiskäyttöistä. Kurssin jälkeen: **Poista ryhmä**, joka poistaa myös ryhmän vastaukset.
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
5. Sulje ja avaa sivu. Vastausten ja pisteiden pitää olla tallessa ilman uutta tuontia. Valitse sama zip uudelleen: uusia rivejä pitää tulla 0.
6. Opiskelijan testitili ei pääse palautuskansioon eikä lomakkeen vastauksiin.

Sivu on testattu automaattisesti (`scripts/test_palautus.py`) itse tehdyillä zip-tiedostoilla, joiden kansiot ja
tiedostonimet ovat Formsin muotoa: kaksi ryhmää, kaksi lukua, uusi versio luvusta. Oikeaa Driven zipiä ei ole vielä testattu.
