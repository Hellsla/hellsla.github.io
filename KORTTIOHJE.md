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
