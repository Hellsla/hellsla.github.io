# Palautus- ja arviointikokeilu (FY3, suomi)

Opettajan pyyntö 5.11.2026: ensin FY3–1, samana iltana kaikki FY3:n luvut ja arviointi ryhmittäin. Opiskelija tekee
luvun tehtävät RuukkiLabrassa, painaa **Lataa kaikki ratkaisut** (Tehtävät-otsikon rivillä) ja palauttaa tiedoston
ryhmän Google Forms -lomakkeella. Opettaja tuo palautukset Sheetsiin sidotulla Apps Scriptillä ja
arvioi tehtävän kerrallaan, opiskelija kerrallaan, nuolinäppäimillä. Sanallinen palaute annetaan Wilmassa.

Tämä kansio ei kuulu julkaistuun sivustoon (`site/`).

**Eduespoossa Apps Script on estetty (5.11.2026).** Arviointi tehdään siksi erillisellä paikallisella sivulla
[`arviointi-fy3.html`](arviointi-fy3.html) (koko FY3, ryhmät erikseen, pisteet luvuittain ja yhteensä): ohje [PAIKALLINEN-ARVIOINTI.md](PAIKALLINEN-ARVIOINTI.md). Sivu käyttää
samaa tarkistus- ja arviointikoodia (Code.gs, Review.html) selaimessa, palautukset Drivesta ladattuna zipinä.
Apps Script -versio jää valmiiksi siltä varalta, että kaupunki sallii sen.

| Tiedosto | Sisältö |
|---|---|
| [KAYTTOONOTTO.md](KAYTTOONOTTO.md) | Forms-, Sheets- ja Apps Script -käyttöönotto, oikeudet, käyttöoikeuksien tarkistus, eduespoon asetukset, säilytysaika, omistajuus |
| [TESTAUS.md](TESTAUS.md) | testaus koulutileillä keksityillä vastauksilla |
| [TIEDOSTOMUOTO.md](TIEDOSTOMUOTO.md) | palautustiedoston rakenne, versiointi ja rajat |
| `apps-script/Code.gs` | tuonti, tarkistus ja arviointinäkymän palvelinfunktiot (asetukset alussa: `RL_CONFIG`) |
| `apps-script/Review.html` | arviointinäkymä |
| `apps-script/Tehtavat.gs` | FY3:n luvut opetusjärjestyksessä ja niiden tehtävänannot (`RL_COURSE`), **generoitu**: `python scripts/palautus_tasks.py` |
| `apps-script/appsscript.json` | manifesti: aikavyöhyke, V8 ja kolme oikeutta |
| `arviointi-fy3.html` | paikallinen arviointisivu, **generoitu** samalla komennolla (`palautus_tasks.py`) |
| `paikallinen/local-backend.js` | paikallisen sivun korvikkeet Sheets-, Drive- ja google.script.run-palveluille, zipin luku, localStorage, CSV ja varmuuskopio |
| `test/gas-mock.js` | testien korvikkeet Sheets-, Drive- ja google.script.run-palveluille |

RuukkiLabran puolella: `templates/palautus.js` (painike *Lataa kaikki ratkaisut* ja tiedoston muodostus; ei pitkää ohjetta eikä
erillistä kuvapainiketta, kuvakaappaus liitetään editoriin Ctrl+V:llä, opettaja 5.11.2026), yksi koukku
`templates/lesson.js`:ssä (`window.flPads.flush`), `build.py`:n `SUBMISSION_COURSES` (suomenkieliset
`fy3-<n>`-luvut) ja tyylit `site.css`:ssä (`.palautus`). Muiden opintojaksojen
toiminta ei muutu.

## Testit
`python scripts/test_palautus.py [site]` (CI:ssä) ja `python scripts/palautus_tasks.py --check`.
Asetuksella `PALAUTUS_SHOTS=<kansio>` testi tallentaa kuvakaappaukset painikkeesta ja arviointinäkymästä.

**Testattu oikeasti:** opiskelijan vienti oikealla FY3–1-sivulla (painike kaikilla FY3-sivuilla) Chromiumissa. Apps Scriptin koodi (tuonti,
tarkistus, kaksoiskappaleet, versiot, virheelliset ja haitalliset tiedostot, uudelleenajo, lukitus,
kaavainjektion esto, arviointinäkymä nuolinäppäimineen, tallennusvirhe ja nopeat painallukset) on ajettu
Chromiumissa jäljiteltyjä Google-palveluja vasten.

**Ei testattu, varmistettava eduespoossa (TESTAUS.md):** oikea Forms (JSON-tiedoston lähetys, vahvistettu
sähköposti, sarakeotsikot), Drive-palautuskansion rakenne, Apps Scriptin oikeuksien hyväksyntä kaupungin
hallinnassa, arviointi-ikkunan koko ja MathML-kaavojen näkyminen opettajan selaimessa, sekä se, että opettaja
pääsee arvioimaan, opiskelija voi palauttaa ja opiskelija tai ulkopuolinen ei pääse kansioon, taulukkoon eikä
arviointinäkymään.
