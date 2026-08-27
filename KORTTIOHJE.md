# Käsitetakomo – miten teet omat kortit

Sovellus: **kasitetakomo.html**
Valmis sisältö: **kasitetakomo-data.js**

Kortteja voi lisätä kahdella tavalla.

---

## Tapa 1 – Tekstitiedosto sivustolle

1. Tee tekstitiedosto alla olevassa muodossa ja tallenna se samaan kansioon,
   esim. `kortit-fy9.txt`.
2. Lisää tiedoston nimi `kasitetakomo.html`-tiedoston alussa olevaan listaan:

```js
const LISATIEDOSTOT = [
  "kortit-fy9.txt"
];
```

Sivusto lataa tiedoston automaattisesti ja kortit näkyvät kaikille. (Toimii
verkossa, ei paikallisesti `file://`-osoitteesta avattuna.)

## Tapa 2 – Suoraan sisältötiedostoon

Lisää kurssi `kasitetakomo-data.js`-tiedostoon samassa muodossa kuin FY1–FY8.
Näin on tehty kaikki nykyiset kurssit.

---

## Tekstimuoto (tämä kannattaa pyytää ChatGPT:ltä)

```
# FY9 | Kurssin nimi
## Aiheen nimi
Käsite :: Määritelmä yhdellä lauseella.
Toinen käsite :: Toinen määritelmä.

## Toinen aihe
Kolmas käsite :: Kolmas määritelmä.
```

Säännöt:

| Merkintä | Tarkoitus |
|---|---|
| `# KOODI \| Nimi` | Kurssi. Koodi näkyy isolla ruudukossa, nimi pienellä. |
| `## Nimi` | Aihe. Yksi kurssi voi sisältää monta aihetta. |
| `Käsite :: Määritelmä` | Yksi kortti. Erottimena `::` |
| tyhjä rivi / `// kommentti` | Ohitetaan. |

Erottimena käy myös sarkain, `|` tai `;`, jos `::` puuttuu – näin taulukosta
kopioitu sisältö toimii sellaisenaan. Tiedostomuoto: `.txt`, `.md`, `.csv`, `.tsv`
tai `.json`. Tallenna **UTF-8**-muodossa, jotta ä ja ö näkyvät oikein.

### JSON-muoto (vaihtoehto)

```json
[
  {
    "id": "FY9",
    "nimi": "Kurssin nimi",
    "aiheet": [
      {
        "nimi": "Aiheen nimi",
        "kortit": [
          ["Käsite", "Määritelmä"]
        ]
      }
    ]
  }
]
```

---

## Valmis ChatGPT-kehote

Kopioi tämä ChatGPT:lle ja vaihda hakasulkeiden sisällöt:

> Tee minulle kertauskortteja lukion kurssista **[FY9 – kurssin nimi]**, aiheista
> **[aihe 1, aihe 2, aihe 3]**. Tee **[20]** korttia.
>
> Palauta pelkkä tekstitiedoston sisältö täsmälleen tässä muodossa, ilman muuta selitystä:
>
> ```
> # [FY9] | [Kurssin nimi]
> ## [Aiheen nimi]
> Käsite :: Määritelmä
> ```
>
> Säännöt:
> - Yksi kortti per rivi, erottimena `::`.
> - Käsite on 1–3 sanaa, ei lauseita, ei kysymysmuotoa.
> - Määritelmä on **yksi lause, enintään noin 20 sanaa**, ja se on ymmärrettävä
>   ilman että käsitettä toistetaan sanasta sanaan.
> - Kaavan saa mainita määritelmän lopussa, esim. `Q = cmΔT`.
> - Käytä kirjoitettuja yksikköjä ja Unicode-merkkejä (·, ², ⁻, Δ, λ, °C), ei LaTeXia.
> - Ryhmittele kortit aiheiden alle `##`-otsikoilla, 5–12 korttia per aihe.
> - Kirjoita suomeksi lukiotasolla, älä käytä lihavointia tai luettelomerkkejä.
> - Ei kaksoiskappaleita.

Tallenna vastaus tiedostoksi `kortit-[kurssi].txt` (UTF-8) ja lisää se yllä
kuvatulla tavalla.

---

## Hyvän kortin mitta

- Käsite edestä, määritelmä takaa – tai toisin päin, sen valitsee opiskelija.
- Yksi kortti = yksi asia. Jos määritelmässä on "ja", harkitse kahta korttia.
- Määritelmä ei saa alkaa samalla sanalla kuin käsite ("Lämpötila on lämpötila…").
- Pituus enintään noin 20 sanaa, muuten kortti ei toimi kertauksessa.

---

## Kuvat kortteihin

Kuva on kortin **valinnainen kolmas kenttä**. Se näkyy vastauspuolella,
määritelmän yläpuolella. Kortti ilman kuvaa toimii kuten ennenkin, ja jos
kuvatiedosto puuttuu, kortti näyttää pelkän tekstin — mikään ei hajoa.

Sisältötiedostossa:

```js
["Kalteva taso","Tilanne helpottuu valitsemalla koordinaatisto tason suuntaiseksi ja jakamalla voimat komponentteihin.","kuvat/fy4-kalteva-taso.svg"]
```

Tekstitiedostossa kolmas kenttä samalla erottimella:

```
Kalteva taso :: Tilanne helpottuu valitsemalla koordinaatisto tason suuntaiseksi. :: kuvat/fy4-kalteva-taso.svg
```

Kuvat tallennetaan kansioon `kuvat/`. Tiedostonimi ilman ääkkösiä ja
välilyöntejä, kurssitunnus alkuun: `fy4-kalteva-taso.svg`, `fy3-faasikaavio.svg`.

### Kaksi kuvatyyppiä – valitse tilanteen mukaan

**1. Kaaviot ja piirrokset → pyydä ChatGPT:ltä SVG-koodia, älä kuvaa.**
Tämä on tärkein neuvo. Kuvageneraattori kirjoittaa kaavioihin sekaisia
kirjaimia, keksii nuolia ja vääriä merkintöjä — juuri se osa, jonka pitäisi olla
täsmällinen, menee pieleen. SVG tulee tekstinä, jolloin näet mitä siinä lukee,
voit korjata yhden luvun editorissa, tiedosto on muutaman kilotavun kokoinen ja
pysyy terävänä joka näytöllä. Näin on tehty `kuvat/fy4-kalteva-taso.svg`.

**2. Havainnollistavat kuvat → kuvageneraattori käy.**
Tuulivoimala, revontulet, höyryturbiini, hehkulanka. Näissä ei ole merkintöjä,
joiden pitäisi olla oikein. Vaadi silti: **ei tekstiä kuvaan**.

### Kehote SVG-kaaviolle

> Piirrä SVG-kuva, joka havainnollistaa käsitteen **[kalteva taso]** lukion
> fysiikan kurssilla **[FY4]**. Palauta pelkkä SVG-koodi, ei selitystä.
>
> Vaatimukset:
> - `viewBox="0 0 400 250"`, ei kiinteää width/height-arvoa, tausta läpinäkyvä.
> - Värit vain tästä paletista: viivat ja tekstit `#012169`, korostus `#e8863a`,
>   toinen korostus `#5f7a52`, kappaleet `#fca5c7`, harmaa `#8f887a`.
> - Viivanpaksuus 3, `stroke-linecap="round"`, nuolenkärjet `<marker>`-elementillä.
> - Tekstiä vain suureiden tunnukset (G, N, F, α) — ei selittäviä lauseita,
>   `font-family="Karla, system-ui, sans-serif"`.
> - Ei gradientteja, ei varjoja, ei kehystä.
> - Fysiikan on oltava oikein: nuolten suunnat, kulmat ja mittasuhteet.
>
> Noudata suomalaisten oppimateriaalien merkintätapaa:
> - Jokainen voima piirretään vaikutuspisteestään.
> - **Paino** lähtee kappaleen massakeskipisteestä alaspäin.
> - **Tukivoima** lähtee kosketuskohdasta eli tason ja kappaleen välistä,
>   kohtisuoraan tasosta poispäin.
> - **Kitkavoima** piirretään tason suuntaisesti niin, että kärki päättyy
>   kappaleeseen.
> - Suureiden tunnukset kursiivilla (*G*, *N*, *F*, *v*), alaindeksit pienemmällä.
> - Yksiköt pystyllä kirjasimella, lukuarvon ja yksikön väliin välilyönti,
>   desimaalierottimena pilkku.
> - Kulma merkitään kaarella ja kreikkalaisella kirjaimella.
> - Kuvaajissa akselit merkitään suureen tunnuksella ja yksiköllä, esim. *p* (kPa).

Tallenna vastaus tiedostoksi `kuvat/[kurssi]-[käsite].svg` ja **katso se läpi** —
avaa selaimessa ja tarkista nuolten suunnat, vaikutuspisteet ja tunnusten kursivointi.
Kielimalli piirtää sujuvasti myös väärin päin olevan kitkavoiman.

### Kehote havainnollistavalle kuvalle

> Luo kuva aiheesta **[tuulivoimala talvisessa maisemassa]**. Litteä
> vektorimainen kuvitustyyli, rauhalliset murretut sävyt, tausta vaalea
> beige (#efe8da), pääväri tummansininen (#012169), korostus oranssi (#e8863a).
> Ei tekstiä, ei kirjaimia, ei numeroita kuvassa. Kuvasuhde 4:3. Yksinkertainen
> ja selkeä, ei yksityiskohtien tulvaa.

Tallenna **WebP**-muodossa noin 1200 px leveänä; pidä tiedosto alle 100 kt,
jotta kortit latautuvat nopeasti myös puhelimella.

### Kannattaa muistaa

- **Älä tee kuvaa joka korttiin.** 30–50 hyvin valittua kuvaa auttaa enemmän
  kuin 478 keskinkertaista. Aloita niistä, joissa kuva kertoo sen mitä teksti ei:
  faasikaavio, kalteva taso, aaltoliike, energiatasot, ydinreaktiot.
- **Kuva ei saa paljastaa vastausta etupuolella** — siksi se näkyy vain
  vastauspuolella.
- Kuvan `alt`-teksti on automaattisesti kortin käsite, joten ruudunlukija
  kertoo mistä kuva on.
