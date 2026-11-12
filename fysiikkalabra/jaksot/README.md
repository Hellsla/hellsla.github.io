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
| lisätä suunnitteilla olevan jakson etusivulle | teen kansion ja `jakso.json`-tiedoston, jossa on otsake (`"status": "planned"`) ja `"front": {"icon", "title", "text"}`; koodia ei tarvita (malli: `droonilab/`) |
| julkaista uuden jakson ilman omaa koodia | kirjoitan sivut lohkoina kohtaan `"pages"` ja vaihdan tilaksi `"live"` (malli: `tests/jaksot/koejakso/`) |

Ikonin koodi on `scripts/module_icons.py`:n listalta; uusi ikoni on SVG kansiossa `assets/shared/module-icons/`.

## Sivut lohkoina (jakso ilman omaa koodia)

```json
"title": "Droonilab",
"front": {"icon": "DROONILAB", "title": "Droonilab", "text": "Rakenna, ohjelmoi ja lennätä drooni."},
"pages": [
  {"file": "droonilab.html", "title": "Droonilab", "nav": "Aloitus", "lead": "…",
   "blocks": [
     {"type": "teksti", "id": "mika", "title": "Mikä Droonilab on", "text": ["kappale", "kappale"]},
     {"type": "lista", "id": "alkuun", "title": "Näin pääset alkuun", "ordered": true, "items": ["…", "…"]},
     {"type": "kortit", "id": "tyopajat", "title": "Työpajat", "from": "kohteet"},
     {"type": "linkit", "id": "lisaa", "title": "Lisää", "links": [{"title": "…", "href": "droonilab-turvallisuus.html"}, {"title": "…", "url": "https://…"}]}
   ]}
]
```

- Ensimmäisen sivun tiedosto on `<id>.html`, muiden `<id>-<nimi>.html`.
- `kortit` näyttää joko annetut kortit (`"cards": [{"title", "text", "href"}]`) tai yhden kortin jokaisesta `kohteet/`-tiedostosta: `{"id", "title", "text", "status": "valmis" | "idea" | "luonnos", "order"}`. Muu kuin valmis kohde näyttää tilansa sanana.
- Sivut käyttävät samoja osia kuin Kilparobotiikan sivut, jakson omassa teemassa.

## Jaksot, joilla on oma sivukoodi

Ahjolla, Kilparobotiikalla ja LUMA-tutorilla on sisältöä, jota yleiset lohkot eivät kata (oppitunnit, lomakepohjat, kausikalenteri). Niiden `jakso.json` on sama tiedosto kuin ennen (`ahjo.json`, `kilparobo.json`, `lumatutor.json`), ja sivut tekee `scripts/ahjo.py`, `scripts/kilparobo.py` tai `scripts/lumatutor.py`. Tiedostojen paikat ja kielten varajärjestyksen tietää vain `scripts/jaksot.py`.

## Tarkistus

```bash
python scripts/jaksot.py
```

listaa jaksot ja tarkistaa otsakkeet, sivut, kohteet ja käännökset. `scripts/build.py` ajaa saman, ja `scripts/test_jaksot.py` testaa rakenteen.
