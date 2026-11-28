# Pedagoginen auditointi: arviointikyky, oma yritys, itsearviointi ja dialogisuus (2026-11-28)

Opettajan kaksi toimeksiantoa 2026-11-28: (A) "Kolme pedagogista kehityskohdetta tekoälyn aikakaudella" (Leung, BNU
28.11.2026) ja (B) "Dialogic Education" (Wegerif, BNU). Kumpikin pyytää ensin nykytilan auditoinnin ja kieltää
muutokset muutosten vuoksi. Tämä raportti on se auditointi, muutoslista ja FY4:n ja FY6:n pilottiehdotus. Raportti on pelkkä pohdinta:
sivustoon, sisältöön tai työjonoon ei ole tehty muutoksia.

**Menetelmä ja sen rajat.** Luvut on laskettu koneellisesti suomenkielisestä lähteestä (`content/fi/FY*/`: 113 lukua,
2 612 tehtävää, 2 203 tutkimuspolun aktiviteettia, `itsearvio/fi.json`, `lang/fi.json`); kertaluonteisella skriptillä. Laadullisesti luettu kokonaan vain fy4-3, fy4-4, fy6-1 ja fy6-4 sekä Näin opiskelet -sivu. FY9:n yksiköt,
FY10, FY14 ja Ahjo on katsottu vain rakenteen tasolla: niiden lukukohtainen arvio puuttuu. Vihjeiden laatua ei ole
arvioitu luku luvulta, vain otoksesta.

## 1. Yhteenveto

Suurin osa molempien toimeksiantojen tavoitteista toteutuu jo jokaisessa FY1–FY8-luvussa, koska ne on rakennettu
tutkimuspolkuun (`docs/inquiry-spec.md`) ja tehtäväpankkiin (`docs/exercise-types.md`). Uusia osioita, laatikoita tai
tehtävämäärän kasvua ei tarvita. Todellisia aukkoja on viisi, ja ne ovat pieniä:

| # | Aukko | Laajuus | Tila |
|---|---|---|---|
| 1 | Näin opiskelet -sivulla ei ole mitään tekoälyn käytöstä | 1 sivu, 3 kieltä | Ehdotus |
| 2 | Itsearvion loppuväittämistä 107/384 alkaa "Ymmärrän / Tiedän / Hahmotan": ne eivät nimeä näyttöä | FY1–FY9 | Ehdotus, pilotti FY4 + FY6 (29 väittämää) |
| 3 | Parin kanssa tehtävä perustelu on yhdessä luvussa (fy2-8), vaikka kenttä `pair` on valmiina | 112 lukua ilman | Ehdotus, pilotti 2 lukua |
| 4 | "Palaa ennusteisiisi" kysyy muutosta, mutta ei näyttöä, joka muutti käsityksen | 112 lukua, sanamuoto | Ehdotus, pilotti 4 lukua |
| 5 | Yhtään tehtävää, jossa arvioidaan tekoälyn tuottamaa ratkaisua tai verrataan kahta selitystä, ei ole | koko aineisto | Ehdotus, pilotti 2–3 tehtävää, olemassa olevia muokaten |

## 2. Mikä toteutuu jo (ei muuteta)

| Tavoite toimeksiannoissa | Nykytila | Kattavuus |
|---|---|---|
| Ennusta – havainnoi – selitä – arvioi uudelleen | Ennusta-vaiheen sitoutuva ennuste (`justify`), koe tai aineisto, Johtopäätös kriteereineen, "Palaa ennusteisiisi" | 113/113 lukua; 247 ennustetta, kaikissa perustelu |
| Virhekäsitysten haastaminen | Ennusteiden väärät vaihtoehdot ovat virhekäsityksiä palautteineen; "Etsi virhe"; suljettu Yleinen virhekäsitys -laatikko | laatikko 113/113; Etsi virhe 110/113 (ei fy4-4, fy4-14, fy4-16, joissa on tehtävätyyppi `error`) |
| Virheen tunnistaminen ja korjaaminen | tehtävätyyppi `error` | 110/113 lukua (ei fy1-6, fy4-3, fy8-12, joissa on Etsi virhe); jokaisessa luvussa siis vähintään yksi |
| Mallin oletukset ja soveltuvuus | tehtävätyyppi `model` | 113/113 (1–7 per luku) |
| Aineisto, kuvaaja, luotettavuus | `data`, `graph`, `experiment` | `data` 113/113 |
| Perusteltu päättely | `reasoning`, kaksivaiheinen perustelumonivalinta | 113/113 |
| Tuloksen mielekkyys | jokaisen malliratkaisun 7. vaihe Järkevyys; suuruusluokkatehtävätyyppi | kaikki ratkaisut (`check_solutions.py`) |
| Perustelu näkyy malliratkaisussa | seitsemän vaiheen ratkaisu, Periaate ja miksi se sopii | kaikki tehtävät |
| Yritä itse → vihje → jatka → malliratkaisu | Yritä ensin -lukko, kolme porrastettua vihjettä siirtotehtävässä, yleisen virheen palaute, mallivastaus vasta "Olen tehnyt ratkaisun" jälkeen | siirtotehtävän vihjeet 112/113 (fy8-9 eri rakenne) |
| Näyttö ennen itsearviota | Testaa ja arvioi: Pohdintatehtävä, kolme tarkistusta (käsite, lasku, selitys), kirjallinen vastaus arvioidaan kriteereihin, vasta sitten loppuväittämät | 113/113 |
| Soveltaminen uuteen tilanteeseen | "Sovella uuteen tilanteeseen" joka luvussa; moduulin Sovella itsenäisesti; 45 aineistotehtävää | kaikki kurssit |
| Tiede keskusteluna | historia ja mallien kehitys tekstissä | FY8 10/16 lukua; FY1–FY7 yhteensä 8 lukua |

Perustehtävät ovat tallessa: 1 551 tehtävää 2 612:sta on tyypittömiä lasku- ja käsitetehtäviä (12–17 per luku).
Arvioivia tehtäviä ei siis pidä lisätä; vaihtelua on jo (virhe 5 %, malli 10 %, aineisto 19 %, päättely 17 %).

Toimeksiannon B esimerkkiväitteistä on jo katettu: liike vaatii jatkuvan voiman (fy4-3), raskaampi putoaa nopeammin
(fy1-6), virta kuluu vastuksessa (fy6-1, fy6-3…5), muuntaja ja teho (fy7-8, fy7-16), metalli kylmempää kuin puu
(fy3-16). Kattamatta haun perusteella: puoliintumisaika ja vaarallisuus (FY8), uusiutuvien ympäristövaikutukset (FY2),
teoria ja laki (FY1). Nämä kannattaa tarkistaa käsin ennen kuin niistä kirjoitetaan mitään.

## 3. Aukot ja ehdotukset

### 3.1 Tekoälyohje Näin opiskelet -sivulle
Sivulla ei ole sanaakaan tekoälystä. Ehdotus: "Kun tehtävä ei etene" -listan alle samalla komponentilla ja olemassa
olevilla kuvakkeilla viiden kohdan lista (esim. otsikolla **Jos käytät tekoälyä**; fi, fi-easy, en): toimeksiannon A
viisi periaatetta sellaisinaan. Ei linkkiä mihinkään palveluun, ei uutta komponenttia. Tekstit olisivat uutta
käyttöliittymätekstiä ja tarvitsevat opettajan hyväksynnän. Mitään ei ole toteutettu.

### 3.2 Itsearvion väittämät näytön kautta
"Ymmärrän, miksi sähkövirta ei kulu lampussa" ei erota malliratkaisun ymmärtämistä itsenäisestä osaamisesta: opiskelija
voi rastia sen luettuaan vastauksen. Ehdotus: väittämä nimeää teon, jonka luvun tarkistus juuri mittasi.

| Nyt | Ehdotus |
|---|---|
| Ymmärrän, miksi sähkövirta ei kulu lampussa. | Osaan selittää omin sanoin, miksi sähkövirta ei kulu lampussa. |
| Ymmärrän, miten virta ja jännite jakautuvat sarja- ja rinnankytkennässä. | Osaan ennustaa, miten virta ja jännite jakautuvat, kun kytkentää muutetaan. |
| Ymmärrän, miksi liike jatkuu ilman eteenpäin vievää voimaa. | Osaan selittää Newtonin ensimmäisellä lailla, miksi liike jatkuu ilman eteenpäin vievää voimaa. |

Määrät: FY1 3, FY2 6, FY3 12, FY4 12, FY5 15, FY6 17, FY7 17, FY8 19, FY9 6. Asteikko, käyttöliittymä, tunnisteet
(`tavoite-N`) ja palautustiedosto eivät muutu. Lisäksi yksi lause: `sa_goals_lead` voisi sanoa "Arvioi sen perusteella,
mitä osasit yllä olevissa tehtävissä ilman malliratkaisua" (nyt "tehtävistä saamasi palautteen ja oman käsityksesi
perusteella"). Ei ehdoteta: uutta väittämää joka lukuun (sovellan uudessa tilanteessa, arvioin mielekkyyttä); ne
kasvattaisivat rivimäärää, ja siirtotehtävä ja Järkevyys-vaihe antavat näytön jo.

Avoin kysymys opettajalle: väittämät hyväksyttiin 6.11.2026 ("monipuolisemmat kuin Opin …"). Muutetaanko niitä taas?

### 3.3 Keskustele ja perustele ilman uutta osiota
`explain`-aktiviteetin kenttä `pair` näyttää parikehotteen saman kortin sisällä (fy2-8). Ehdotus: lisätään se
yhteen olemassa olevaan Johtopäätös- tai Selitä-tehtävään niissä luvuissa, joissa ennusteet tyypillisesti jakautuvat.
Ei uutta otsikkoa "Keskustele ja perustele", ei uutta tehtävää; yksin opiskeleva ohittaa kehotteen. Kehote kysyy
näyttöä ("mikä mittaus tukee kumpaakin selitystä, mikä saisi sinut muuttamaan mieltäsi"), ei "keskustelkaa".

### 3.4 Palaa ennusteisiisi: mikä muutti käsitykseni
Nykyinen kehote ("Mikä ajatuksistasi piti paikkansa, ja minkä muuttaisit?") on jo hyvä. Pieni tarkennus pilotissa:
kehote pyytää nimeämään havainnon, joka muutti käsityksen, ja sen, mikä jäi epäselväksi. Tehtävä pysyy valinnaisena.

### 3.5 Arvioi ratkaisu, vertaa selityksiä
Aineistossa ei ole tehtävää, jossa lähteenä on tekoälyn tuottama ratkaisu, ja kahden selityksen vertailu on vain
ennusteiden vaihtoehdoissa. Ehdotus: pilotissa 2–3 olemassa olevaa `error`-tehtävää muotoillaan uudelleen (ei uusia
tehtäviä): yhdessä "opiskelija" → "tekoälyn tuottama ratkaisu, joka näyttää siistiltä" (virhe periaatteessa, ei
laskussa), yhdessä kaksi kilpailevaa selitystä ja kysymys, kumpaa aineisto tukee. Tunnisteet säilyvät.

### 3.6 Mitä ei ehdoteta
- **Uudet nimetyt osiot** (Haasta ajatteluasi, Tieteen vuoropuhelu, Sovella osaamistasi, Tekoäly keskustelukumppanina):
  sisältö on jo luvuissa toisella nimellä; uusi nimiö jokaisessa luvussa olisi juuri sitä laatikoiden kasvua, jonka
  toimeksianto B kieltää, ja rikkoisi yleislinjan (käyttöliittymään ei lisätä tekstiä).
- **Lisää lukkoja tai klikkauksia**: Yritä ensin riittää.
- **Vihjeet koko tehtäväpankkiin**: vihjeitä on 58 tehtävässä 2 612:sta (lähes kaikki tason 1). Kattava lisäys olisi
  noin 2 500 vihjesarjaa kolmella kielellä. Jos halutaan, järkevä rajaus on ydintehtävät (469), kurssi kerrallaan.
  Tämä on opettajan kustannuspäätös, ei pilotin osa.
- **Lukukohtaiset tekoälykehotteet sivuille**: yksi yleinen, kopioitava kehote Näin opiskelet -sivulla on harkittavissa
  pilotin jälkeen. Kouluun hyväksytty palvelu ja tietosuoja ovat koulun päätöksiä; sivu ei voi luvata niitä.
- **Tieteen vuoropuhelu FY1–FY7:ään laajasti**: FY8 hoitaa tämän. FY4:ssä yksi luonteva kohta (Newtonin mekaniikan
  pätevyysalue) ja FY6:ssa ei tarvetta.

## 4. Kurssikohtainen muutoslista

| Kurssi | Arvioi ja perustele | Yritä itse | Itsearvio | Dialogisuus |
|---|---|---|---|---|
| FY1 | riittää (fy1-6: ei `error`-tehtävää, Etsi virhe on) | riittää | 3 väittämää | teoria ja laki: tarkista fy1-8 |
| FY2 | riittää | riittää | 6 | `pair` on fy2-8:ssa (malli muille) |
| FY3 | fy3-3: ydintehtävissä ei arvioivaa tyyppiä | riittää | 12 | – |
| FY4 | fy4-2…5 ja fy4-16: ydintehtävissä ei arvioivaa tyyppiä; fy4-4, -14, -16: ei Etsi virhe | riittää | 12 | pilotti |
| FY5 | riittää | riittää | 15 | – |
| FY6 | riittää | riittää | 17 | pilotti |
| FY7 | riittää | riittää | 17 | – |
| FY8 | riittää (fy8-12: ei `error`-tehtävää) | fy8-9: siirtotehtävän vihjeet tarkistettava | 19 | puoliintumisaika ja vaarallisuus: tarkista |
| FY9 | ei auditoitu luku luvulta | vihjeportaat tehty (11c) | 6 | ei auditoitu |
| FY10, FY14, Ahjo | ei auditoitu | – | – | luontevin paikka aidoille päätöstehtäville; oma auditointi |

"Ydintehtävissä ei arvioivaa tyyppiä" korjataan vaihtamalla ydinmerkintä (`core`) olemassa olevaan tason 2
arvioivaan tehtävään, ei kirjoittamalla uutta.

## 5. Pilotti: FY4 ja FY6

Kaksi PR:ää (kurssi kerrallaan), fi + fi-easy + en, normaalit kolme katselmointia. Ei jaettuja muutoksia, ei uusia
käyttöliittymätekstejä.

| Luku | Muutos | Rakenne, jota käytetään |
|---|---|---|
| fy4-3 Newtonin I ja III laki | parikehote ennusteen 2 (kumpi työntää lujemmin) johtopäätökseen; Palaa ennusteisiisi -tarkennus | `pair`, `reflect` |
| fy4-4 Newtonin II laki | yksi olemassa oleva `error`-tehtävä ydintehtäväksi; Palaa ennusteisiisi -tarkennus | `core`, `reflect` |
| fy4-16 | yksi `error`-tehtävä muotoon "tekoälyn tuottama ratkaisu" | `error` |
| FY4 kaikki | 12 itsearvioväittämää näytön kautta | `itsearvio/*.json` |
| fy6-1 Virta ja jännite | parikehote (mitä lampussa kuluu); Palaa ennusteisiisi -tarkennus | `pair`, `reflect` |
| fy6-4 Sarja- ja rinnankytkentä | yksi `error`-tehtävä kahden selityksen vertailuksi; Palaa ennusteisiisi -tarkennus | `error`, `reflect` |
| FY6 kaikki | 17 itsearvioväittämää näytön kautta | `itsearvio/*.json` |

Pilotin jälkeen opettaja päättää laajennuksesta. Arvio: 6 lukua × kolme katselmointia × kolme kieltä (delta).

## 6. Riskit
- Väittämien muutos kesken lukuvuoden: opiskelijan aiemmat arviot säilyvät, mutta väittämän teksti niiden vieressä
  vaihtuu. Palautustiedoston vaikutus tarkistettava pilotissa ennen muuta.
- "Tekoälyn tuottama ratkaisu" -tehtävä vanhenee, jos virhe on sellainen, jota nykyiset mallit eivät tee. Virheen
  pitää olla fysiikan periaatteessa (väärä systeemi, väärä malli), ei laskussa.
- Dialogisten tehtävien vaikuttavuudesta ei ole omaa näyttöä; toimeksiannon B lähteet ovat pääosin teoreettisia.
  Pilotin jälkeen kannattaa kysyä opiskelijoilta ennen laajennusta. Lähdeviitteitä ei lisätä sivustolle tarkistamatta.
