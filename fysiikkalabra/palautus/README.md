# Palautus- ja arviointikokeilu (FY3–1, suomi)

Opettajan pyyntö 5.11.2026. Opiskelija tekee tehtävät RuukkiLabrassa, painaa **Lataa ratkaisut** ja palauttaa
tiedoston koulun Google Forms -lomakkeella. Opettaja tuo palautukset Sheetsiin sidotulla Apps Scriptillä ja
arvioi tehtävän kerrallaan, opiskelija kerrallaan, nuolinäppäimillä. Sanallinen palaute annetaan Wilmassa.

Tämä kansio ei kuulu julkaistuun sivustoon (`site/`).

| Tiedosto | Sisältö |
|---|---|
| [KAYTTOONOTTO.md](KAYTTOONOTTO.md) | Forms-, Sheets- ja Apps Script -käyttöönotto, oikeudet, käyttöoikeuksien tarkistus, eduespoon asetukset, säilytysaika, omistajuus |
| [TESTAUS.md](TESTAUS.md) | testaus koulutileillä keksityillä vastauksilla |
| [TIEDOSTOMUOTO.md](TIEDOSTOMUOTO.md) | palautustiedoston rakenne, versiointi ja rajat |
| `apps-script/Code.gs` | tuonti, tarkistus ja arviointinäkymän palvelinfunktiot (asetukset alussa: `RL_CONFIG`) |
| `apps-script/Review.html` | arviointinäkymä |
| `apps-script/Tehtavat.gs` | FY3–1:n tehtävänannot, **generoitu**: `python scripts/palautus_tasks.py` |
| `apps-script/appsscript.json` | manifesti: aikavyöhyke, V8 ja kolme oikeutta |
| `test/gas-mock.js` | testien korvikkeet Sheets-, Drive- ja google.script.run-palveluille |

RuukkiLabran puolella: `templates/palautus.js` (paneeli, tiedoston muodostus, *Lisää kuva*), kaksi koukkua
`templates/lesson.js`:ssä (`window.flPads.flush`, tapahtuma `fl:pad-ready`), `build.py`:n `SUBMISSION_PAGES` (vain
`fi`/`fy3-1`) ja tyylit `site.css`:ssä (`.palautus`). Muiden lukujen toiminta ei muutu.

## Testit
`python scripts/test_palautus.py [site]` (CI:ssä) ja `python scripts/palautus_tasks.py --check`.
Asetuksella `PALAUTUS_SHOTS=<kansio>` testi tallentaa kuvakaappaukset paneelista ja arviointinäkymästä.

**Testattu oikeasti:** opiskelijan vienti oikealla FY3–1-sivulla Chromiumissa. Apps Scriptin koodi (tuonti,
tarkistus, kaksoiskappaleet, versiot, virheelliset ja haitalliset tiedostot, uudelleenajo, lukitus,
kaavainjektion esto, arviointinäkymä nuolinäppäimineen, tallennusvirhe ja nopeat painallukset) on ajettu
Chromiumissa jäljiteltyjä Google-palveluja vasten.

**Ei testattu, varmistettava eduespoossa (TESTAUS.md):** oikea Forms (JSON-tiedoston lähetys, vahvistettu
sähköposti, sarakeotsikot), Drive-palautuskansion rakenne, Apps Scriptin oikeuksien hyväksyntä kaupungin
hallinnassa, arviointi-ikkunan koko ja MathML-kaavojen näkyminen opettajan selaimessa, sekä se, että opettaja
pääsee arvioimaan, opiskelija voi palauttaa ja opiskelija tai ulkopuolinen ei pääse kansioon, taulukkoon eikä
arviointinäkymään.
