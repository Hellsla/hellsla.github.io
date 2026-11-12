# Jaksot: fysiikan moduulien ulkopuoliset opintojaksot

Jokainen jakso on yksi kansio. Rakenne on kaikissa sama, joten yhden jakson päivittäminen on samaa työtä kuin toisen.

```
jaksot/<id>/
  jakso.json        jakso suomeksi
  kohteet/          yksi tiedosto per kohde (ohje, työpaja, projekti)
  en/, fi-easy/     käännös: jakso.json ja kohteet/ samoilla nimillä; puuttuva tiedosto näytetään suomeksi
```

`jakso.json` alkaa aina samalla otsakkeella:

```json
"jakso": {"id": "<kansion nimi>", "status": "live" | "planned", "theme": "ahjo" | "kiviruukki" | "ruukkilabra"}
```

## Tavallisimmat päivitykset

| Haluan | Teen |
|---|---|
| korjata tekstiä | muokkaan riviä tiedostossa `jakso.json` (ja käännöksessä, jos sellainen on) |
| lisätä työpajan, ohjeen tai projektin | lisään tiedoston kansioon `kohteet/` |
| lisätä suunnitteilla olevan jakson etusivulle | teen kansion ja `jakso.json`-tiedoston, jossa on otsake (`"status": "planned"`) ja `"front": {"icon", "title", "text"}`; koodia ei tarvita (malli: `esimerkkijakso/`) |
| julkaista uuden jakson ilman omaa koodia | kirjoitan sivut lohkoina kohtaan `"pages"` ja vaihdan tilaksi `"live"` (mallit: `kilparobo/jakso.json` ja `tests/jaksot/koejakso/`) |
| muuttaa Kilparobotiikan tekstiä, korttia, vaihetta tai linkkiä | muokkaan tiedostoa `kilparobo/jakso.json` (ja `kilparobo/en/jakso.json`); koodiin ei kosketa |

Ikonin koodi on `scripts/module_icons.py`:n listalta; uusi ikoni on SVG kansiossa `assets/shared/module-icons/`.

## Sivut lohkoina (jakso ilman omaa koodia)

```json
"title": "Esimerkkijakso",
"front": {"icon": "DRONELABRA", "title": "Esimerkkijakso", "text": "Rakenna, ohjelmoi ja lennätä drooni."},
"pages": [
  {"file": "esimerkkijakso.html", "title": "Esimerkkijakso", "nav": "Aloitus", "lead": "…",
   "blocks": [
     {"type": "teksti", "id": "mika", "title": "Mikä Esimerkkijakso on", "text": ["kappale", "kappale"]},
     {"type": "lista", "id": "alkuun", "title": "Näin pääset alkuun", "ordered": true, "items": ["…", "…"]},
     {"type": "kortit", "id": "tyopajat", "title": "Työpajat", "from": "kohteet"},
     {"type": "linkit", "id": "lisaa", "title": "Lisää", "links": [{"title": "…", "href": "esimerkkijakso-turvallisuus.html"}, {"title": "…", "url": "https://…"}]}
   ]}
]
```

- Ensimmäisen sivun tiedosto on `<id>.html`, muiden `<id>-<nimi>.html`.
- `kortit` näyttää joko annetut kortit (`"cards": [{"title", "text", "href"}]`) tai yhden kortin jokaisesta `kohteet/`-tiedostosta: `{"id", "title", "text", "status": "valmis" | "idea" | "luonnos", "order"}`. Muu kuin valmis kohde näyttää tilansa sanana.
- Sivut käyttävät samoja osia kuin Kilparobotiikan sivut, jakson omassa teemassa.

## Lohkot

Yksinkertaisimmat lohkot ovat `teksti`, `lista`, `kortit` ja `linkit` (yllä). Loput ovat osia, joista Kilparobotiikan
sivut on rakennettu; mikä tahansa jakso voi käyttää niitä. Malli jokaisesta on tiedostossa `kilparobo/jakso.json`.

| Lohko | Mitä se näyttää |
|---|---|
| `pikavalikko` | numeroidut pikalinkit sivun alussa |
| `nyt` | mitä juuri nyt tehdään; tyhjä teksti sanoo, ettei uutta ole |
| `kokemukset` | aiemmat tapahtumat, opiskelijoiden kokemukset ja tulevat tapahtumat |
| `sarakkeet` | muutama rinnakkainen lista otsikoineen |
| `johdanto` | kappale ja huomiolaatikko linkkeineen, ilman otsikkoa |
| `polku` | vaiheet: tavoite, aiheet, harjoitus, mentorin vinkki, näyttö ja linkit |
| `ohjelinkit` | lista ulkoisia ohjeita selityksineen |
| `kausi` | kauden vaiheet kysymyksineen ja tuotoksineen |
| `paivakirja` | kysymykset ja kopioitava tai ladattava tekstipohja |
| `periaate` | yksi korostettu lause |
| `rinnakkain` | kaksi lohkoa vierekkäin |
| `kappale` | yksi kappale |
| `taidot` | taitokortit: mistä taidon tunnistaa ja mikä on näyttö |
| `varoitukset` | luonnosmerkintä ja pysäytysohje |
| `roolit` | mentorin ja opettajan vastuut erikseen |
| `turva-aiheet` | turvallisuusaiheet ikoneineen |
| `loppulinkit` | loppulause ja viralliset linkit |

Kenttien nimet ovat tiedoston `scripts/jaksot.py` kommentissa lohkokirjaston alussa. Ikonien nimet: `scripts/jaksot.py`
`ICONS`.

## Jakso, joka on myös rekisterin opintojakso

Kilparobotiikan etusivu on samalla opintojakson sivu (`local-courses.json`, koodi `KILPAROBO`). Silloin otsakkeessa on
`"course": "KILPAROBO"`, ensimmäinen sivu on `KILPAROBO.html`, ja sen otsikkolohko, kuvat ja opiskelijoiden kokemukset
tulevat rekisteristä. Etusivun rivi tulee myös sieltä.

## Jaksot, joilla on oma sivukoodi

Ahjolla ja LUMA-tutorilla on sisältöä, jota lohkot eivät vielä kata (oppitunnit, ohjeet kuvineen, lomakepohjat,
työpajakortit suodattimineen). Niiden sivut tekee `scripts/ahjo.py` ja `scripts/lumatutor.py`. Kilparobotiikan sivut
tehdään lohkoista; `scripts/kilparobo.py`:ssä on enää jakson omat säännöt (vain VEXin ja RECF:n viralliset linkit,
kahdeksan kausivaihetta, viisi polun vaihetta). Tiedostojen paikat ja kielten varajärjestyksen tietää vain
`scripts/jaksot.py`.

## Tarkistus

```bash
python scripts/jaksot.py
```

listaa jaksot ja tarkistaa otsakkeet, sivut, kohteet ja käännökset. `scripts/build.py` ajaa saman, ja `scripts/test_jaksot.py` testaa rakenteen.
