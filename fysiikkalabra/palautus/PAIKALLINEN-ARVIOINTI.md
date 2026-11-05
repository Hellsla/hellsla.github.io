# Arviointi ilman Apps Scriptiä: paikallinen arviointisivu

Eduespoossa Apps Script on estetty (Google Admin: *you do not have access to this service*, 5.11.2026). Siksi
arviointi tehdään tiedostolla **`arviointi-fy3-1.html`**, jonka opettaja avaa omalla koneellaan selaimessa
(Chrome tai Edge). Sivu ei käytä verkkoa eikä Googlen tai Microsoftin palveluja. Se lukee Drivesta ladatut
palautukset ja tallentaa pisteet vain tämän selaimen muistiin. Arviointinäkymä on sama kuin Apps Script -versiossa.

## Käyttöönotto

1. **Lomake** tehdään kuten KAYTTOONOTTO.md:n kohdassa 1, eduespoo-tilillä. Sheetsiin linkittämistä ja Apps Scriptiä
   ei tarvita. Palautuskansio ja lomake vain nimetyille opettajille (KAYTTOONOTTO.md, kohta 5).
2. **Lataa arviointisivu** kerran omalle koneelle: `fysiikkalabra/palautus/arviointi-fy3-1.html` (repossa, myös
   projektin tiedostoissa). Avaa se kaksoisnapsauttamalla. Sivu toimii ilman verkkoa.

## Arviointi

1. Drivessa: napsauta kansiota **Palauta vastaukset (File responses)** hiiren oikealla → **Lataa**. Drive tekee
   zip-tiedoston (suurista kansioista useamman).
2. Arviointisivulla: **Palautukset: Valitse tiedostot** → valitse zip (tai kaikki zipit kerralla).
   Sivu tarkistaa tiedostot samoin kuin Apps Script -versio ja näyttää käsittelytilan: hyväksytty, kaksoiskappale,
   tarkistettava (sama palautustunniste kahdella opiskelijalla), virheellinen (syy näkyy). Tarkistettavan voi
   hyväksyä ja hyväksytyn hylätä rivin painikkeella.
3. Valitse tehtävä ja arvioi kuten ennenkin: yksi opiskelija kerrallaan, ↓/↑, numeronäppäin antaa pisteet, Enter
   tallentaa ja siirtyy. Pisteet 0–3, tyhjä = arvioimaton, 0 = annettu nolla.
4. **Vie pisteet (CSV)** lataa tiedoston `fy3-1-pisteet.csv`: opiskelija, palautusaika, tunniste, pisteet
   tehtävittäin, yhteensä. Avaa se Sheetsissä (Tiedosto → Tuo) tai Excelissä. Kaavoiksi tulkittavat merkit on suojattu.
5. **Varmuuskopioi arviointi** lataa tuonnin tilan ja pisteet JSON-tiedostona. Säilytä se koulun Drivessa,
   ei julkisesti. **Palauta varmuuskopio** tuo sen takaisin (esim. toisella koneella).
6. Uusia palautuksia tullessa lataa kansio uudelleen ja valitse uusi zip: jo luetut ohitetaan, uudet lisätään.
   Korjattu palautus on opiskelijan uusi versio, vanhan pisteet säilyvät vanhalla versiolla.

Palautustiedostoja ei säilytetä sivulla. Kun avaat sivun seuraavan kerran, pisteet ja tilat ovat tallessa, mutta
vastausten näyttämistä varten valitse zip uudelleen.

## Tunniste ja aika

- **Opiskelija** tunnistetaan nimestä, jonka Forms lisää palautetun tiedoston nimeen:
  `fy3-1.ratkaisut - Etunimi Sukunimi.json`. Nimi tulee opiskelijan kirjautuneesta eduespoo-tilistä.
  Vahvistettu sähköposti näkyy tarvittaessa lomakkeen vastauksissa.
- **Palautusaika** on tiedoston aika Driven zipissä. Järjestys ei perustu opiskelijan tiedoston omaan aikaleimaan.
- Molemmat on varmistettava ensimmäisessä kokeessa (alla).

## Tietoturva

- Zip sisältää opiskelijoiden töitä: pidä se koulun koneella ja poista Lataukset-kansiosta arvioinnin jälkeen.
- Sivu tallentaa selaimen muistiin (localStorage) tuonnin tilan, opiskelijoiden nimet ja pisteet, ei vastauksia.
  Käytä omaa, henkilökohtaista koulun konetta. Älä käytä yhteiskäyttöistä konetta. Kurssin jälkeen: **Tyhjennä arviointi**.
- Sivu ei lataa mitään verkosta (Content-Security-Policy estää sen), ei suorita palautuksista koodia eikä näytä
  niistä HTML:ää. Kuvina näytetään vain tarkistetut PNG- ja JPEG-kuvat.

## Varmistettava ensimmäisessä kokeessa (keksityillä vastauksilla)

1. Kaksi opiskelijan testitiliä palauttavat tiedoston lomakkeella (ja toinen niistä toisen kerran).
2. Lataa kansio zipinä, valitse se sivulla: näkyykö **oikea nimi** ja **järkevä palautusaika** (vertaa lomakkeen
   vastauksiin)? Jos nimi puuttuu tai on väärä, kerro, niin korjaan nimen tunnistuksen.
3. Arvioi muutama tehtävä, vie CSV ja avaa se Sheetsissä.
4. Sulje ja avaa sivu, valitse zip uudelleen: pisteet tallessa, uusia rivejä 0.
5. Opiskelijan testitili ei pääse palautuskansioon eikä lomakkeen vastauksiin.

Sivu on testattu automaattisesti (`scripts/test_palautus.py`) itse tehdyllä zip-tiedostolla, jonka tiedostonimet
ovat Formsin muotoa. Oikeaa Driven zipiä ei ole vielä testattu.
