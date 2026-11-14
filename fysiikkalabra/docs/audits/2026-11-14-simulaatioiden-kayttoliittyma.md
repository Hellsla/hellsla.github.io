# Simulaatioiden käyttöliittymä: mittaus ja suunnitelma

Opettajan linjaus 14.11.2026. Muistio jatkaa vaiheiden käyttöliittymän muistiota
(`2026-11-10-vaiheiden-kayttoliittyma.md`, Tutki-vaihe ja kohta 3 "Tarttuva simulaatiokuva puhelimella"). Se kuvaa,
miten simulaatiokortit nyt toimivat eri näytöillä, mitkä ongelmat ovat jaettuja ja mitkä yksittäisten simulaatioiden,
sekä missä järjestyksessä ne korjataan. Mitään tässä ei ole vielä toteutettu; jokainen kohta on oma pull request
(kohta 6), ja jaettujen tiedostojen muutokset tehdään yksin ja yhdistetään ensin.

Mittaus 14.11.2026: 96 julkaistua suomenkielistä simulaatiosivua Chromiumilla leveyksillä 360, 390, 768, 1280 ja
1920 px sekä matalan kannettavan ikkunoilla (alla). Opiskelijoilla ei ole testattu mitään.

## 1. Yhteenveto

| Havainto | Laajuus | Syy | Korjaus |
|---|---|---|---|
| Kuvan tekstit noin 7 px matalalla kannettavalla | 87/96 alle 11 px | kuvan kavennus ja tekstikoko #sim-rootin leveydestä | PR 1 ja PR 2 |
| Kortti ei mahdu ikkunaan 1280×720 | 77/96 | lukemat ja selitteet kuvan ja säätimien jälkeen, 25 rem:n varaus | PR 2 ja PR 3 |
| Puhelimella kuva vierii pois, kun säätimiä käytetään | kaikki | mikään ei tartu | PR 4 |
| Canvasilla ei nimeä eikä kuvausta, valintaruutu alle 40 px | kaikki / 10 | – | PR 5 |
| Korkeat monipaneeliset kuvat | 6 (tyyppi D) | sim.js | myöhemmin |
| Saman toiminnon eri nimet, toistuvat seliterivit | kymmeniä | sim.js ja lang | myöhemmin, sisältömuutoksen yhteydessä |

Rakenne on yhtenäinen ja kevyt: vaakavieritystä ei ole millään leveydellä, ja säätimiä on vähän. Ongelmat ovat
tilankäytössä (matala näyttö, puhelin), eivät simulaatioiden määrässä tai fysiikassa.

## 2. Mittaus

### Rakenne
- 87/96 simulaatiossa järjestys on kuva > säätimet > lukemat > selite > kolme suljettua laatikkoa (Käyttöohje, Mallin
  oletukset, Laskennan selitys).
- Säätimiä on mediaanina 5; 90 simulaatiossa enintään 7. Poikkeus on fy1-2: 17 säädintä, joista 14 painiketta.
- Vaakavieritystä ei millään mitatulla leveydellä.

### Matala kannettava (ikkunan korkeus noin 650–730 px)
Esimerkiksi 1366×650, 1280×720 ja 1536×730: kuva kapenee 384 px:iin, vaikka kortti on 640 px leveä, ja kuvan tekstit
ovat noin 7 px. 87/96 simulaatiossa tekstit jäävät alle 11 px:n.

| Ikkuna | Kuvan leveys | Kuvan tekstit |
|---|---|---|
| 1366×650, 1280×720, 1536×730 | 384 px | noin 7 px |
| 1280×800 | 492 px | 9 px |
| 1440×900 | 600 px | 11 px |

**Syy 1.** `site.css`: `.lab-side .sim-canvas{max-width:calc((100vh - var(--sticky-top) - 25rem) * var(--sim-ar,1.5))}`.
Kuva kapenee ikkunan korkeuden mukaan, jotta kortti mahtuisi ruutuun, ja 25 rem:n varaus on suurempi kuin kuvan alle
nyt tarvitaan.

**Syy 2.** Simulaatiot suurentavat tekstinsä `#sim-root`in `clientWidth`in mukaan (esimerkiksi fy4-1:n sim.js:
`k = max(1, 600 / clientWidth)`), eivät kuvan todellisen leveyden mukaan. Kun kuva kapenee mutta `#sim-root` ei,
`k` on 1 eikä tekstiä suurenneta. `sim-embed.js`:n `p.text`-kääreen 10 px:n alaraja ei auta, koska koko sisältää jo
`p.scale(s)`:n ja `k` on 1.

**CI ei näe tätä.** `check_layout.py` käyttää korkeutta 800 px, `test_sims.py` ja `test_inquiry.py` 900 px.

### Kortin korkeus
- 1280×720: kortin mediaani 684 px (kuva 256 px, sen alla noin 430 px). Kortti mahtuu ikkunaan 19/96 simulaatiossa.

### Puhelin
- Kortin mediaani 1051 px (360 px leveä) ja 1022 px (390 px). Mikään osa ei tartu, joten kuva vierii pois, kun
  opiskelija käyttää säätimiä tai lukee lukemia.
- 360×740: kuva ja säätimet mahtuvat samaan ruutuun 66/96 simulaatiossa; kuva, säätimet ja lukemat 39/96:ssa.

### Korkeat monipaneeliset kuvat
fy6-5, fy6-6, fy6-9, fy6-12, fy6-13 ja fy6-14: kortti 950–1170 px myös työpöydällä.

### Nimet
- Toistonopeus: "Nopeus" 58 simulaatiossa, "Nopeus (toisto)" 5, "Animaation nopeus" 3, "Toistonopeus" 1, "Animaatio" 1.
  Nopeusvalinta on 69 simulaatiossa.
- Tauko 23 / Pysäytä 12; Alusta 28 / Alkuun 3 / Nollaa 3.

### Toisto
- fy4-1:n seliterivi toistuu Käyttöohjeessa.
- Kortin alin kuvausteksti (`.sim-lead`) toistaa koekortin.
- Aika t näkyy sekä liu'un nimiössä että lukemassa.

### Saavutettavuus
- Canvasilla ei ole nimeä eikä kuvausta, ja `.sim-tex-layer` on `aria-hidden`.
- Neljässä simulaatiossa kuvassa raahataan; vain kahdessa on näppäinkäsittelijä.
- Alle 40 px:n kohde (valintaruutu): fy1-4, fy3-4, fy3-9, fy4-5, fy4-6, fy5-1, fy5-3, fy5-11, fy5-12 ja fy7-1. Muut
  kohteet ovat vähintään 40 px.

## 3. Simulaatiotyypit

| Tyyppi | Kuvaus | Määrä | Missä | Korjataan |
|---|---|---|---|---|
| A | aikaohjattu ajo ja kuvaaja | noin 29 | FY4, FY1, osa FY5 | jaetuissa tiedostoissa |
| B | jatkuva animaatio ilman käynnistystä | noin 40 | FY3, FY5, osa FY7 ja FY8 | jaetuissa tiedostoissa |
| C | staattinen parametritutkimus | 25 | `sim-embed.js` `STATIC` | jaetuissa tiedostoissa |
| D | korkea monipaneelinen | 6 | kohta 2 | sim.js |
| E | poikkeavat | – | fy1-2, fy1-4, taulukollinen, 4 raahattavaa | sim.js |

Tyypit A–C korjataan jaetuissa tiedostoissa (`templates/sim-embed.js`, `templates/site.css`), eikä yksikään
katselmointi vanhene. Tyypit D ja E vaativat sim.js-muutoksen, joka vanhentaa luvun katselmoinnit, joten ne tehdään
kurssi kerrallaan.

## 4. Päätökset (opettaja 14.11.2026)

- Ei Lisäasetukset-painiketta eikä uutta yleiskomponenttia. Toistonopeus pysyy näkyvissä tiiviinä valintana
  toistorivin päässä.
- Lukemat siirtyvät kuvan alle, ennen säätimiä.
- Kolme suljettua laatikkoa säilyvät nykyisellään.
- Kuvausteksti (`.sim-lead`) pois kortin alta, kun simulaatio on kokeiden vieressä.
- Puhelimella kuva tarttuu vaihepalkin alle; pilotti ensin (sama kuin 10.11. muistion kohta 3).
- Nimien yhtenäistäminen (Toisto / Tauko / Alusta) ja toistuvien seliterivien poisto tehdään vasta kunkin luvun
  seuraavan sisältömuutoksen yhteydessä, koska ne vanhentavat katselmoinnit.

## 5. Mitä ei muuteta

- Simulaatioiden fysiikka, `simState`, `defineSimAdapter`, kokeiden lukitus- ja mittauslogiikka.
- Fysiikan säätimien ja hetki-liu'un näkyvyys.
- Kolmen laatikon nimet ja rivi.
- Työpöydän rinnakkaisasettelu ja sääntö, ettei kortti vieri itsensä sisällä.
- Suurenna-tila.
- LaTeX-nimiöt ja 17 px:n pohjafontti.
- `STATIC`-luettelo ja 5.–12.11. suorituskykykorjaukset.
- Nopeusvalinnan olemassaolo.
- Tehtävät, tallennusavaimet ja palautus.

## 6. Toteutusjärjestys

Jokainen rivi on oma pull request. PR 1–PR 4 muuttavat jaettuja tiedostoja: ne tehdään yksin ja yhdistetään ennen
sisältömuutoksia (repon juuren `CLAUDE.md`, sääntö 3).

| # | Muutos | Tiedostot | Riski | Testi |
|---|---|---|---|---|
| PR 1 | Kuvan todellinen leveys tekstikoon perustaksi | `sim-embed.js`, selaintesti | pieni | uusi testi 1366×650: kuvan tekstit vähintään 10 px |
| PR 2 | Pilotti fy4-1: lukemat kuvan alle, toistorivi yhdelle riville, 25 rem:n varaus pienemmäksi, kuvausteksti pois | `site.css`, `sim-embed.js` | keskisuuri | fy4-1 kaikilla leveyksillä ja 1366×650 |
| PR 3 | Sama asettelu tyypeille A–C | `site.css`, `sim-embed.js` | keskisuuri | kaikki simulaatiosivut paikallisesti |
| PR 4 | Tarttuva kuva puhelimella, pilotti fy4-1 ja yksi tyypin C simulaatio | `site.css`, `lesson.js` | keskisuuri | 360×740 ja 390×844 |
| PR 5 | Canvasin nimi ja kuvaus, valintaruudut 40 px:n kohteiksi | `sim-embed.js`, `site.css` | pieni | saavutettavuus ja `check_layout.py` |

Myöhemmin kurssi kerrallaan, kunkin luvun sisältömuutoksen yhteydessä ja katselmointien kanssa: tyyppi D, fy1-2:n
säätimien ryhmittely, näppäinvaihtoehto raahaukselle, nimien yhtenäistäminen ja toistuvien seliterivien poisto.
