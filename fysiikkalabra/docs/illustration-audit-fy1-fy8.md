# Ruukkilabran kuvituksen laatuauditointi FY1-FY8

Päivitetty: 2026-11-09. Tämä dokumentti erottaa **todetun rakenteellisen inventaarion** ja **vielä vahvistettavan visuaalisen/fysikaalisen arvioinnin**.

## Tilannekuva lähdekoodista

Käytiin läpi suomenkielisten oppituntien `content/fi/FY1...FY8/<lesson>/lesson.md` -tiedostot. Alla on teoriaosuuksissa olevien inline-SVG- ja img-elementtien määrä; mukana ei ole tehtäväpankin kuvaviittauksia eikä simulaatioiden piirroksia.

| Moduuli | Oppitunteja | Teorian SVG-kuvat | Teorian img-kuvat |
|---|---:|---:|---:|
| FY1 | 8 | 35 | 8 |
| FY2 | 8 | 30 | 10 |
| FY3 | 16 | 78 | 17 |
| FY4 | 16 | 79 | 13 |
| FY5 | 17 | 99 | 12 |
| FY6 | 16 | 86 | 21 |
| FY7 | 16 | 100 | 27 |
| FY8 | 16 | 90 | 28 |
| **Yhteensä** | **113** | **597** | **136** |

Jokaisella 113 oppitunnilla on erillinen `data-fig="hero"` -aloituskuva. Kuvien määrä ei osoita, että kuvat olisivat automaattisesti laadukkaita tai oikein.

### Säilytettävä nykyinen arkkitehtuuri

- `scripts/figlib.py`: skaalautuva, yhtenäinen SVG- ja KaTeX-kuvituskirjasto.
- `scripts/herolib.py`: arkielämän ilmiökuvat (ei korvata geneerisillä rasterikuvilla).
- `scripts/fbd.py`: voimakuvioiden fysikaaliset tarkistukset, voimien vaikutuspisteet ja merkitysvärit.
- `scripts/figures.py` ja oppituntikohtainen `lessons/FY*/fy*-*/figures.py`: lähdekuvat `data-fig`-elementeille.
- `scripts/figcat.py` ja `docs/figures/catalog.json`: kuvien uudelleenkäytön ja tehtäväkuvien inventaario. Älä kopioi tehtäviin vastausta paljastavaa teoriakuvaa.
- `scripts/check_layout.py`, `scripts/check_a11y.py`, `scripts/test_fbd.py`: nykyiset testit; uutta tarkistusta käytetään niiden rinnalla.
- `NOTES.md`, kohta 3: olemassa olevat tyylisäännöt ovat määrääviä, ei rinnakkaista värijärjestelmää.

## Kuvitusjärjestelmä: voimassa olevat yhteiset periaatteet

Vältä uusia ristiriitaisia värisääntöjä. Käytä olemassa olevia `figlib`-vakioita. Voimakuvioissa voima on punainen yhtenäinen nuoli, sen komponentti samanvärinen katkoviivainen nuoli, nopeus sininen, kiihtyvyys oranssi, resultantti vihreä. Aaltorintamissa voi käyttää vesiväriä, kun suureiden merkitykset ovat muuten yksiselitteisiä.

- Mallikuva: 600 SVG-yksikön levyinen, merkinnät KaTeXilla ja `foreignObject`-rakenteella.
- Aloituskuva: 1200 × 600, nykyinen flat-vector-tyyli, tekstittömyys ja mobiilin keskikolmannekseen painottuva kohde.
- Tunnistettava tilannekuva ja idealisoitu mallikuva erotetaan toisistaan.
- Akselit, mittayksiköt ja mittauspisteet esitetään oppikirjan käytäntöjen mukaan. Älä vääristä asteikkoa.
- Älä lisää kuvaa vain kuvamäärän kasvattamiseksi. Kuva pitää sijoittaa juuri sitä selittävän tekstin yhteyteen.
- Alt-teksti kertoo tarvittaessa myös kuvan sisällön kannalta välttämättömät suhteet ja suunnat; kuvan näkyvä teksti ei ole ainoa tapa välittää asiaa.
- Testaa 360, 390, 768 ja 1280 px sekä vaalea/tumma teema, kun teemat ovat käytössä; lopullinen selainarvio tarvitaan myös staattisille piirroksille.

## Moduulikohtaiset korkeimman riskin kuvaryhmät

Alla olevat ovat **tarkistusjonoja**, eivät lähdekoodissa todettuja virheitä.

| Moduuli | Ensimmäisenä tarkastettavat kuvaryhmät | Perustelu |
|---|---|---|
| FY1 | fy1-3 mittaus, fy1-4 kuvaajat, fy1-5 liikkeen kuvaajat | tarkkuus, asteikot, data ja tulkinta |
| FY2 | fy2-4 hyötysuhde, fy2-6 energian tuotantotavat, fy2-7 energiansiirto | energian virrat ja häviöiden merkitys |
| FY3 | fy3-4 paine, fy3-9 ja fy3-10 kaasulait, fy3-11 lämpövoimakone | hiukkasmallit ja pV-kuvaajien oikeellisuus |
| FY4 | fy4-5 voimakuvat, fy4-6 kalteva taso, fy4-10 törmäykset | nuolien suunnat, vaikutuspisteet, fysikaaliset oletukset |
| FY5 | fy5-9 värähtely, fy5-11 taipuminen, fy5-12 interferenssi, fy5-13 seisova aalto | vaiheistus, aaltorintamat ja solmut |
| FY6 | fy6-4 rinnankytkennät, fy6-10 Coulombin laki, fy6-11 sähkökenttä | sähkötekninen ja kenttämallien oikeellisuus |
| FY7 | fy7-5 induktio, fy7-7 generaattori, fy7-13 interferenssi | suunta-, napaisuus- ja vaihevirheet |
| FY8 | fy8-1 valosähköilmiö, fy8-3 energiatilat, fy8-11 fissio/fuusio | tapahtumajärjestys, mallit ja energiatasot |

### Tarkastetut lähdekoodiesimerkit

- **FY4-5**: erillinen `tilanne()` ja voimakuvio samasta tilanteesta. Koodissa käytetään `FBD`-kirjastoa. Älä korvaa tätä yleisellä nuolikaaviolla.
- **FY5-11**: `diffraction()` vertaa raon leveyttä `b≈4λ` ja `b<λ`. Tarkista leveän raon kuva aaltorintamien näkökulmasta renderöitynä; ratkaise ensin, tarvitaanko korjausta.
- **FY5-13**: `superposition()`, `nodes()`, `string_modes()` ja `pipes()` havainnollistavat eri näkökulmia. Tarkista myös, ettei kielten ja ilmapatsaiden siirtymä- ja paineaaltomalleja sekoiteta.
- **FY4-6**: kitka ja kalteva taso; tarkista erityisesti, vastaavatko kitkan nuolet tekstissä ilmoitettua liiketilaa.
  
## Käytännön kuvakohtainen laadunvarmistus

1. Avaa `docs/figures/catalog.json` / `python scripts/figcat.py show <id>`, älä kopioi valmista SVG:ta.
2. Nimeä opittava asia ja kuvan tyyppi: ilmiö, malli, kuvaaja, toimintaperiaate tai vaiheistus.
3. Tarkista fysiikka kirjoitetulla perustelulla: malli, oletukset, suunnat, suurten ja pienten suureiden suhteet, yksiköt.
4. Aja kyseisen luvun `scripts/figures.py` ja nykyiset `check_layout.py`, `check_latex.py` ja `check_a11y.py`.
5. Tarkista selainrenderöinti läppärin ja puhelimen mitoissa sekä kuvatekstit ja alt-tekstit.
6. Kuva merkitään valmiiksi vasta hyväksytyn fysiikka- ja visuaalitarkistuksen jälkeen.

Automaattinen rakenteellinen inventointi: `python scripts/check_illustrations.py --report docs/illustration-inventory.md`.

## Rehellinen rajaus

Tämä kierros **ei** tarkoita, että kaikki 597 teoriakuvaa tai tehtävien ja simulaatioiden kuvat olisi jo yksitellen katsottu ja korjattu visuaalisesti. Tätä ei voi todeta ilman selainrenderöintiä ja asiantuntijatarkistusta. Dokumentin tarkoitus on varmistaa, että myöhempi kuvakohtainen työ kohdistuu todellisiin puutteisiin eikä tuota päällekkäisiä kuvia.