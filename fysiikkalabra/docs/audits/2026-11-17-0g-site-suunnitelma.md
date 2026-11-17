# Työjono 0g: `site/` pois sisältö-PR:istä — suunnitelma

Tila: **vain suunnitelma, ei koodia. Odottaa opettajan hyväksyntää.** Mitään ei toteuteta ennen sitä; toteutus omina PR:inään (osa 7).
Laatija: worker-istunto, 2026-11-17. Mittaukset ovat `origin/main`ista 5aaa798.

## 0. Nykytila (mitattu)

- `site/`: 246 Mt, 1282 seurattua tiedostoa; niistä 814 HTML-sivua (148 Mt), `en/` 49 Mt, `fi-easy/` 46 Mt, `pics/` 23 Mt. Repon pack 609 MiB.
- 10.–17.11. `site/`-polkuun koski 175 committia; mainiin yhdistettiin 81 PR:ää. Jokainen yhdistys vanhentaa jokaisen avoimen PR:n `site/`-kopion.
- Syy, miksi ristiriita on lähes varma: **jokaiseen sivuun** (814 kpl) kirjoitetaan `?v=<hash>` jaetuista tiedostoista (`build.py` rivit 1607–1613), joten yksi muutos `templates/`- tai `site.css`-tiedostoon muuttaa kaikkia sivuja; lisäksi kurssi- ja moduulisivut, navigointi ja `index.html` muuttuvat jokaisesta julkaistavasta luvusta.
- Mihin committoitu `site/` nyt on sidottu:
  1. `fysiikkalabra-ci.yml` checks-3: "committed site/ is exactly a fresh render" (`build.py` + `git status site/`).
  2. `layout`-työ ei rakenna: se avaa committoidun `site/`:n (`check_layout.py --site`, `ci_parallel.py` rivi 76–80). `check_a11y.py site`, `svgids.py site`, `test_chapter_nav.py site`, `deploy_site.py` lukevat samaa.
  3. `ci_scope.py`: `site/<id>.html`-diff nimeää sivut, joita lähde-diff ei nimeä (julkaisun alkaminen/loppuminen, naapurin Edellinen/Seuraava, moduulisivut), ja `version_only` suodattaa `?v=`-muutokset.
  4. `ruukkilabra-deploy.yml`: julkaisee commitin committoidun `fysiikkalabra/site/`:n; "fresh"-vaihe vertaa mainin `site/`:a.
  5. `build.py` `LIVE = site/`: varoitus "on live-sivustolla, mutta katselmoinnit eivät ole ajan tasalla; tämä rakennus poistaa sen" (rivit 1233, 1259, 1334, 1362, 1580–1595) ja `site.old`-vaihto.
  6. Työkalut: `round.py --finish` ajaa `build.py --all` ja `build.py`; `screenshot.py` varapolku `site/`; juuren `CLAUDE.md` sääntö 4.
  7. **Vanhat osoitteet:** `hellsla.github.io/fysiikkalabra/site/…` on yhä Pagesissa (juuren `index.html`, `sitemap.xml`, `kasitetakomo.html`, `kasitekortit.html` linkittävät sinne). Julkaisusääntö: julkinen osoite on `ruukkilab.fi`.

## 1. Tavoite ja suositus

Sisältö-PR ei sisällä `site/`-muutoksia. `site/` ei ole enää repossa; CI rakentaa sen jokaisella ajolla (git-ignoroituun `site/`-kansioon, kuten nyt `build.py` tekee), ja `ruukkilabra-deploy` julkaisee **saman CI-ajon rakentaman** version. Julkaisusääntö ei muutu: sivulle pääsee vain katselmoitu sisältö (`reviews.py`), ja yhdistäminen on opettajan julkaisupäätös.

**Suositus (vaihtoehto A):** `site/` poistuu kokonaan (`git rm`, `.gitignore`). Vaihtoehto B (CI kirjoittaa `site/`:n botti-commitina mainiin) pitäisi repon kasvun (~600 Mt, +~175 committia/viikko) ja vaatisi botille ohitusoikeuden suojattuun mainiin; PR:t eivät kuitenkaan koskisi `site/`:hen, joten ristiriita poistuisi myös siinä. A on yksinkertaisempi eikä riko sääntöä "ei pushata mainiin". Historia ei pienene (historian uudelleenkirjoitus on kielletty).

## 2. Miten `site/` rakennetaan vain CI:ssä ja deploy-työssä

**PR:n CI.** `plan` ja jokainen selaintyö rakentavat jo nyt (`build.py --all`); `layout`-työ ei, joten se saa `fetch-depth: 0` + rakennuksen (build lukee tehtävien katselmoidun version historiasta) ennen `check_layout.py --site`. checks-3:n "committed site/ is a fresh render" korvataan kahdella tarkistuksella (osa 4). Artefaktit: `site-preview` (osa 5).

**`ci_scope.py` ilman `site/`-diffiä (kysymys 1).** Lähdesäännöt (`content/`, `lessons/`, `assets/`, `lang/`, `tests/`) säilyvät. `site/`-rivit korvataan **kahden rakennuksen vertailulla**: `plan`-työ rakentaa base-commitin (`git worktree` + `build.py`, `SITE_OUT`-ympäristömuuttuja) ja headin, vertaa HTML-tiedostot (`filecmp`, `?v=`-tokenit normalisoituna pois, joten `version_only` poistuu) ja antaa muuttuneet sivut samalla muodolla kuin nyt. Se on tarkempi kuin nykyinen: julkaisun alku/loppu, naapurit ja moduulisivut nimeytyvät automaattisesti, eikä `NOTHING`-taulukon "ei mitään"-rivejä (courses.json, kortit) tarvitse arvata. Jaettujen tiedostojen sääntö (SMOKE-otos) ei muutu.
Hinta: yksi lisärakennus `plan`-työssä. **Rakennusaikaa ei ole mitattu**; mittaus on toteutus-PR 1:n ensimmäinen tehtävä, ja jos se on yli ~5 min, base-rakennus välimuistitetaan (`actions/cache`, avain base-sha).

**`build.py` `LIVE`.** "Poistuu live-sivustolta" -varoitus verrataan base-rakennukseen (`LIVE` = ympäristömuuttuja `BUILD_LIVE_DIR`, oletus ei mitään → ei varoituksia). Deploy-työssä `LIVE` = julkaistu `Hellsla/ruukkilabra`-checkout, jolloin varoitus kertoo, mitä julkaisu todella poistaa. `site.tmp`→`site`-vaihto säilyy (rakennus ei jää puolitiehen).

**Deploy (`ruukkilabra-deploy.yml`).** `fysiikkalabra-ci` main-ajolla lataa `site`-artefaktin (rakennettu ja testattu; pakattu koko mitataan, odotus ≪ 246 Mt). Deploy lataa saman ajon artefaktin (`workflow_run.id`), ajaa `deploy_site.py`:n (yksityisyys- ja linkkiportit ennallaan) ja pushaa. Näin julkaistaan täsmälleen se, mikä testattiin. Manuaalinen ajo ("now" tai uusin vihreä) rakentaa itse samasta commitista. "Fresh"-vaihe korvataan: julkaistun repon `.source-sha`-tiedosto; ei julkaista, jos julkaistu sha on tämän jälkeläinen. `concurrency` ennallaan.

## 3. Mitkä tarkistukset ja työkalut muuttuvat

| Kohde | Muutos |
|---|---|
| `fysiikkalabra-ci.yml` | checks-3 "fresh render" → (a) `git ls-files site` on tyhjä, (b) build onnistuu ja `deploy_site.py` PASS; `layout`-työ rakentaa; `plan` kahden rakennuksen diff; artefaktit. |
| `ci_scope.py`, `ci_parallel.py` | skope kahden rakennuksen diffistä (osa 2); `ci_parallel` lukee valmiin rakennuksen (`site/` rakennuksen jäljiltä, ei committoitu); `test_ci_parallel.py`, uusi skooppitesti. |
| `build.py` | `LIVE` ympäristömuuttujasta; muuten ei muutosta (`?v=` ja `site.tmp` säilyvät). |
| `check_lesson.py` | ei muutosta (rakentaa `preview/`:hen). |
| `screenshot.py` | rakentaa jo itse `preview/`:hen; `site/`-varapolku pois (kuollutta koodia). |
| `round.py` | `--finish` ei ajaa `build.py --all` eikä `build.py`:tä (säästää täyden rakennuksen ja poistaa `site/`-diffin commitista); `test_round.py` päivitetään. Vaihe 1 (catalog/assessment/coverage) ennallaan. |
| `reviews.py impact` | `site/`-polku pois tooling-listasta; muuten ennallaan. `verify` ei muutu. |
| `deploy_site.py` | lukee rakennuksen (`--site`, oletus `site/`); ei muutosta logiikkaan. |
| Ohjeet | juuren `CLAUDE.md` sääntö 4 ("rakenna `site/` uudelleen") poistuu; `fysiikkalabra/CLAUDE.md` rivit 8 ja 97; `docs/QUALITY.md`, `lesson.md`, README, deploy-työn ja CI:n otsikkokommentit. |

## 4. "Committoitu `site/` vastaa tuoretta rakennusta" -tarkistuksen korvaaja (kysymys 2)

Tarkistuksen tarkoitus oli (i) ettei sivustolla ole katselmoimatonta sisältöä, (ii) että testattu sivu = julkaistu sivu. (i): `build.py` rakentaa vain katselmoidut luvut, ja `reviews.py verify` pysyy. (ii): julkaistaan CI:n artefakti (osa 2), joten erillistä vastaavuutta ei voi rikkoutua. Lisäksi **determinismitesti**: CI rakentaa kahdesti (plan-työn head-rakennus ja checks-3:n) ja vertaa tiedostoittain; ero = punainen. Siirtymässä vastaavuus todistetaan kerran: PR 2:n main-ajossa artefakti verrataan committoituun `site/`:iin (osa 7).

## 5. Opettajan näkymä PR:n vaikutukseen ennen yhdistämistä (kysymys 3)

1. `reviews.py impact` -tuloste on jo PR:n yhteenvedossa (checks-3).
2. Uusi: step summary listaa **muuttuneet sivut** kahden rakennuksen diffistä (sama lista kuin skooppi, plus lisätyt/poistuvat sivut).
3. Artefakti `site-preview` (koko rakennus, 14 pv; pakattu koko mitataan). Opettaja lataa sen ja avaa sivut paikallisesti; suhteelliset linkit toimivat. Nykyisin sama näkyy PR:n tiedostodiffissä (HTML), joka on epäluettava, joten tämä ei heikennä.
4. Vaihtoehto, joka tarvitsee opettajan päätöksen: julkinen esikatselusivusto (esim. erillinen yksityinen repo/Pages). Ei suositella ilman erillistä päätöstä, koska se on julkaisun lähellä.

## 6. Julkaisun palautus (kysymys 5)

- Julkaistu repo `Hellsla/ruukkilabra` on versiohistoria: palautus = `git revert` siellä tai deploy-työn manuaaliajo, johon lisätään syöte `sha` (rakentaa ja julkaisee vanhemman main-commitin; rakennus on deterministinen lähteistä ja historiasta).
- "now"-vipu ennallaan. Julkaistun repon `.source-sha` kertoo, mikä commit on livenä.
- Artefaktin vanheneminen (14 pv) ei estä palautusta, koska vanha commit rakennetaan uudelleen.

## 7. Siirtymäjärjestys ja avoimet PR:t (kysymys 6)

Kaikki jaettuja tiedostoja → yksi kerrallaan, yksin, yhdistetään ennen sisältö-PR:iä (kohdan 0 sääntö).

- **PR 1 (varjo, ei käytösmuutosta):** `BUILD_LIVE_DIR`, kahden rakennuksen skooppi uutena tilana `ci_scope.py --built`, mittaukset (rakennusaika, artefaktin koko, determinismi), CI:n `plan`-työ ajaa uuden skoopin **rinnalla** ja kirjaa eron vanhaan yhteenvetoon. Ei vielä vaikuta mihinkään. Pidetään päällä muutama yhdistys; ero oltava nolla tai selitetty.
- **PR 2 (kytkentä):** `layout` rakentaa; skooppi vaihtuu uuteen; checks-3 "fresh render" poistuu; `site-preview`/`site`-artefaktit; deploy julkaisee artefaktin; `round.py`/`screenshot.py`/ohjeet. Tästä hetkestä **kukaan ei rakenna `site/`:a PR:ään**; PR:iden vanhat `site/`-muutokset ovat harmittomia (CI ei lue niitä). PR 2:n main-ajossa artefakti verrataan committoituun `site/`:iin: pitää olla identtinen, ennen kuin PR 3 tehdään.
- **PR 3 (poisto):** `git rm -r fysiikkalabra/site`, `.gitignore`, "ei seurattua `site/`" -tarkistus, vanhojen `hellsla.github.io/fysiikkalabra/site/`-osoitteiden korvaus (osa 8). Tämä on se hetki, jolloin avoimet PR:t kohtaavat modify/delete-ristiriidan. Koordinaattori ilmoittaa ikkunan; ennen sitä mahdollisimman moni PR yhdistetään. Jokaiselle avoimelle PR:lle yksi komento (skripti `scripts/site_migrate.sh`, PR 3:ssa): `git merge origin/main; git rm -rq --ignore-unmatch site; git commit` — hyväksytään poisto, PR:n omat `site/`-muutokset heitetään pois. Ei uudelleenrakennusta, ei uutta katselmointia (`site/` ei kuulu sisältöhashiin).
- **PR 4:** ohjeiden viimeistely, tyojono-loki, mitattu säästö (kohdan 0 vaatimus).

## 8. Riskit

| Riski | Torjunta |
|---|---|
| Julkaistu ≠ testattu | Julkaistaan CI:n artefakti; determinismitesti; PR 2:n identtisyyskoe. |
| Opettajan tarkastus vaikeutuu | `site-preview` + muuttuneiden sivujen lista (osa 5); päätös esikatselusta opettajalle. |
| Rakennus on hidas / artefakti suuri | Mitataan PR 1:ssä; välimuisti base-rakennukselle; pakattu artefakti. |
| `layout`-työ rakentaa (+aika × 4–8 työtä) | Artefakti `plan`-työstä ladattavaksi rakentamisen sijaan (valinta mittausten mukaan). |
| Vanhat linkit `hellsla.github.io/fysiikkalabra/site/` katkeavat (`index.html`, `sitemap.xml`, `kasitetakomo.html`, `kasitekortit.html`) | **Opettajan päätös:** ohjauspysäkki-sivut tai linkkien vaihto `ruukkilab.fi`-osoitteisiin PR 3:ssa. Julkaistut sivut eivät saa nimetä hellsla.github.io:ta, joten korjaus tehdään juuren puolella, ei `site/`:ssä. |
| Hajonnut deploy mainin ajon jälkeen | Palautus osa 6; deploy ei pushaa, jos portit eivät mene läpi (ennallaan). |
| Vanha artefakti puuttuu (14 pv) manuaaliajossa | Manuaaliajo rakentaa itse. |
| Muu generoitu tiedosto samaa luokkaa | Katso osa 9. |

## 9. Rajaus: muut committoidut generoidut tiedostot (ei tässä kohdassa, ehdotus)

`docs/figures/catalog.json`, `docs/assessment/<COURSE>.md` ja `docs/coverage/<COURSE>.md` ovat samanlaisia (CI vertaa `--check`illä; `round.py` vaihe 1 uudistaa), ja niiden ristiriidat vaativat myös mainin yhdistämisen. Eivät kuulu kohtaan 0g, mutta jos `site/`-työ onnistuu, ehdotan erillistä 0h: CI generoi ne ja tarkistaa vain vastaavuuden, `figcat.py find` generoi katalogin tarvittaessa paikallisesti. Opettaja päättää, otetaanko jonoon.

## 10. Säästöarvio

Mitatut luvut: ~110 `site/`-uudelleenrakennusta ja ~140 mainin yhdistystä haaroihin 10.–17.11.; ~30 PR:ää yhdistettiin 17.11.; 1,6 rakennusta/haara.
- **Poistuu kokonaan:** `site/`-uudelleenrakennus (`build.py --all` + `build.py`) jokaisessa PR:ssä ja `round.py --finish`issä; mainin yhdistys, jonka ainoa syy on `site/` tai `?v=`/`catalog.json`-ristiriita (osa niistä; `catalog.json` jää kunnes 0h); sitä seuraava uusi CI-ajo (jokainen ylimääräinen push käynnistää `qa`:n; skooppi pienenee, kun `?v=`-kohina poistuu); 175 `site/`-committia viikossa, repon kasvu (~600 Mt:n pack) ja HTML-diffit PR:ssä.
- **Arvio (oletus, ei mitattu):** jos yksi rakenna-yhdistä-korjaa-kierros maksaa 10–20 k tokenia ja yhden ylimääräisen CI-ajon, 110 kierrosta viikossa on noin 1,1–2,2 M tokenia ja 110 tarpeetonta CI-ajoa; työntekijän vuoroista poistuu 1–2 per kierros. Todellinen luku mitataan PR 4:ssä `usage.py`:llä kohdan 0 mukaan (vuorot, tokenit, yhdistykset ennen/jälkeen).
- **Uusi kustannus:** yksi lisärakennus `plan`-työssä ja `layout`-töissä (osa 8); arvioidaan PR 1:ssä, ja nettohyöty raportoidaan.

## 11. Päätettävää opettajalle

1. Hyväksytäänkö A: `site/` poistuu repossa kokonaan (suositus), vai B: CI-botti kirjoittaa sen mainiin?
2. Vanhat `hellsla.github.io/fysiikkalabra/site/`-osoitteet: ohjauspysäkit vai linkkien vaihto `ruukkilab.fi`:hin?
3. Esikatselu: riittääkö CI-artefakti + muuttuneiden sivujen lista (suositus), vai halutaanko erillinen esikatselusivusto?
4. Otetaanko 0h (`catalog.json`, `assessment`, `coverage` CI:lle) jonoon?
5. Hyväksytäänkö siirtymäjärjestys PR 1 (varjo) → PR 2 (kytkentä) → PR 3 (poisto) → PR 4?
