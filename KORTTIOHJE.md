# Käsitekortit – miten teet omat kortit

Käsitekortit ovat osa Ruukkilabraa. Kortit näkyvät luvun Teoriatiivistelmässä
(lihavoidut käsitteet ja käsitesirut), luvun lopussa ("Kertaa luvun käsitteet"),
moduulisivun kertauspakassa, Sovella itsenäisesti -sivulla ja koko kokoelmana
sivulla `fysiikkalabra/site/kasitteet.html`. Vanhat osoitteet `kasitetakomo.html`
ja `kasitekortit.html` ohjaavat sinne parametreineen.

## Missä kortit ovat

| Tiedosto | Sisältö |
|---|---|
| `fysiikkalabra/kortit/fy4.json` | Moduulin suomenkieliset kortit (myös selkosuomen sivut käyttävät näitä) |
| `fysiikkalabra/kortit/en/fy4.json` | Englanninkieliset kortit samoilla tunnisteilla |
| `fysiikkalabra/kortit/kuvat/` | Korttien kuvat |

Kortit muokataan näihin tiedostoihin, minkä jälkeen ajetaan
`python3 scripts/concept_cards.py check` ja `python3 scripts/build.py`. Build kopioi tiedostot
sivustolle (`site/kortit/`). Komennot ajetaan kansiossa `fysiikkalabra/`;
yhteenveto luvuittain: `python3 scripts/concept_cards.py stats`.

## Tiedoston muoto

```json
{
 "moduuli": "FY4",
 "nimi": "Voima ja liike",
 "aiheet": [ { "id": "fy4-newtonin-lait", "nimi": "Newtonin lait" } ],
 "kortit": [
  {
   "id": "fy4-newtonin-toinen-laki",
   "moduuli": "FY4",
   "luku": "fy4-4",
   "aihe": "fy4-newtonin-lait",
   "kasite": "Newtonin toinen laki",
   "maaritelma": "Kokonaisvoima aiheuttaa kappaleelle kiihtyvyyden; dynamiikan peruslaki.",
   "kaava": "\\Sigma\\overline{F} = m\\overline{a}",
   "kaava_puhe": "voimien summa on m kertaa a"
  }
 ]
}
```

| Kenttä | Pakollinen | Tarkoitus |
|---|---|---|
| `id` | kyllä | Pysyvä tunniste, alkaa moduulin koodilla (`fy4-…`). Opiskelijan kertauspakka tallentuu tällä tunnisteella, joten **älä muuta tai poista olemassa olevaa tunnistetta**. |
| `luku` | ei | Luku, jonka Teoriatiivistelmään ja loppuun kortti kuuluu. `null` = kortti näkyy vain kokoelmassa. |
| `aihe` | kyllä | Aiheen `id` tiedoston `aiheet`-listasta. Aiheita voi yhdistää kertauksessa. |
| `kasite` | kyllä | Kortin etupuoli. Teoriatiivistelmän samanniminen lihavointi (myös taivutettuna, esim. *tehoksi*) saa korttipopoverin. Jos lihavointia ei ole, build alleviivaa luvun kortin käsitteen sen ensimmäisessä esiintymässä teoriatekstissä (ei otsikoissa, kuvissa eikä kaavoissa). |
| `maaritelma` | kyllä | Takapuoli, yksi lause. Matematiikka LaTeXina `$…$`, esim. `$k$`. |
| `kaava` | ei | Kaava LaTeXina ilman `$`-merkkejä. Vektorit `\overline{F}`, kertomerkki `\cdot`, suomeksi desimaalipilkku `{,}`. |
| `kaava_puhe` | jos `kaava` | Kaava luettavassa muodossa ruudunlukijalle. |
| `kuva` | ei | Kuvan polku kansiosta `kortit/`, esim. `kuvat/fy4-kalteva-taso.svg`. |

Moduuli, jonka tiedostossa on `"kesken": true`, ei näy vielä sivustolla.
Englanninkielinen kortti saa saman `id`:n, `luku`:n ja `aihe`en kuin suomenkielinen;
jos moduulilla ei ole englanninkielistä tiedostoa, englanninkieliset sivut jättävät
käsiteosion pois.

## Suorat linkit

| Osoite | Mitä avautuu |
|---|---|
| `kasitteet.html` | Moduulivalikko |
| `kasitteet.html?moduuli=FY4` | FY4:n aihevalikko |
| `kasitteet.html?moduuli=FY4&aihe=fy4-newtonin-lait` | Aiheen kertaus alkaa heti |
| `kasitteet.html?moduuli=FY4&aihe=fy4-newtonin-lait,fy4-kiihtyva-liike` | Kahden aiheen yhdistetty kertaus |
| `kasitteet.html?moduuli=FY4&luku=fy4-4` | Yhden luvun kortit |
| `kasitteet.html?moduuli=FY4&pakka=oma` | Opiskelijan oma kertauspakka |

Tuntematon moduuli tai aihe palauttaa valikkoon.

## Kertauspakka

Kortin kääntämisen jälkeen opiskelija valitsee "Osasin" tai "Kertaa myöhemmin".
Tila tallentuu selaimen localStorageen avaimeen `ruukkilabra:kortit`
(`{ id: { tila, osasinPutki, muokattu } }`). "Kertaa myöhemmin" lisää kortin
pakkaan, ja kolme peräkkäistä "Osasin" poistaa sen. Mitään ei lähetetä palvelimelle.

---

## Valmis ChatGPT-kehote

Kopioi tämä ChatGPT:lle ja vaihda hakasulkeiden sisällöt:

> Tee minulle kertauskortteja lukion fysiikan moduulista **[FY9 – moduulin nimi]**,
> aiheista **[aihe 1, aihe 2, aihe 3]**. Tee **[20]** korttia.
>
> Palauta pelkkä JSON-lista, ilman muuta selitystä, jossa jokainen kortti on muotoa
> `{"kasite": "…", "maaritelma": "…", "aihe": "[aiheen nimi]", "kaava": "…"}`.
>
> Säännöt:
> - Käsite on 1–3 sanaa, ei lauseita, ei kysymysmuotoa.
> - Määritelmä on **yksi lause, enintään noin 20 sanaa**, ja se on ymmärrettävä
>   ilman että käsitettä toistetaan sanasta sanaan.
> - Kaava vain jos käsitteellä on kaava, LaTeXina ilman dollareita; vektorit
>   `\overline{F}`, kertomerkki `\cdot`, desimaalipilkku `{,}`.
> - Suureet määritelmässä LaTeXina `$…$`.
> - 5–12 korttia per aihe, suomeksi lukiotasolla, ei kaksoiskappaleita.

Lisää kortit tiedostoon ja täydennä `id`, `moduuli`, `luku`, `aihe`-tunniste ja
`kaava_puhe`. Tarkistus (`concept_cards.py check`) kertoo, jos jotain puuttuu.

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

Kortin kentässä `kuva`:

```json
"kuva": "kuvat/fy4-kalteva-taso.svg"
```

Kuvat tallennetaan kansioon `fysiikkalabra/kortit/kuvat/`. Tiedostonimi ilman ääkkösiä ja
välilyöntejä, kurssitunnus alkuun: `fy4-kalteva-taso.svg`, `fy3-faasikaavio.svg`.

### Kaksi kuvatyyppiä – valitse tilanteen mukaan

**1. Kaaviot ja piirrokset → pyydä ChatGPT:ltä SVG-koodia, älä kuvaa.**
Tämä on tärkein neuvo. Kuvageneraattori kirjoittaa kaavioihin sekaisia
kirjaimia, keksii nuolia ja vääriä merkintöjä — juuri se osa, jonka pitäisi olla
täsmällinen, menee pieleen. SVG tulee tekstinä, jolloin näet mitä siinä lukee,
voit korjata yhden luvun editorissa, tiedosto on muutaman kilotavun kokoinen ja
pysyy terävänä joka näytöllä. Näin on tehty `kortit/kuvat/fy4-kalteva-taso.svg`.

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

Tallenna vastaus tiedostoksi `fysiikkalabra/kortit/kuvat/[kurssi]-[käsite].svg` ja **katso se läpi** —
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
