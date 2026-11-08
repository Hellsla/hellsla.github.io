# Palautustiedosto `<luku>.ratkaisut.json` (ruukkilabra-palautus, versiot 1–3)

RuukkiLabran `templates/palautus.js` tekee tiedoston opiskelijan selaimessa, ja Apps Scriptin `Code.gs`
(`rlValidate_`) tarkistaa sen. Rajat ovat molemmissa samat (`LIMITS` / `RL_LIMITS`).

```json
{
  "format": "ruukkilabra-palautus",
  "version": 1,
  "chapter": "fy3-1",
  "lang": "fi",
  "submission_id": "32 heksamerkkiä, satunnainen",
  "exported": "2026-11-05T18:32:05.211Z",
  "includes": "solution-editor",
  "content_sha256": "64 heksamerkkiä",
  "answers": [
    { "task": "fy3-1-L1-01", "status": "answered", "content": [
        { "type": "text", "text": "Paino on " },
        { "type": "math", "latex": "G=mg", "png": "<base64>", "w": 58, "h": 15 },
        { "type": "text", "text": "\nkuva:" },
        { "type": "image", "mime": "image/png", "data": "<base64>", "w": 640, "h": 320 } ] },
    { "task": "fy3-1-L1-02", "status": "empty", "content": [] }
  ]
}
```

- Opiskelija näkee vain painikkeen *Lataa kaikki ratkaisut* (ei pitkää ohjetta, opettaja 5.11.2026). Opettaja kertoo
  opiskelijoille tarvittaessa itse, mitä tiedostossa on. Versioissa 1 ja 2 mukana oli vain luvun tehtävien *Kirjoita ratkaisu*
  -editorien sisältö. Versiosta 3 alkaen mukana ovat myös numerovastaukset, valinnat ja tekstivastaukset (ks. alla). Ei nimeä,
  sähköpostia eikä muiden lukujen ratkaisuja.
- `lang`: sivun kieli, `fi` (myös selkosuomi) tai `en` (6.11.2026). Luvut ja tehtävätunnisteet ovat kaikilla kielillä samat,
  joten arviointi on sama.
- `answers`: jokainen luvun tehtävä kerran sivun järjestyksessä. Tyhjä editori on `"empty"` ilman sisältöä.
  Puuttuva tehtävä tai rikkinäinen tiedosto on tuonnissa *Virheellinen*, joten opettaja erottaa vastaamattoman
  tehtävän puuttuvasta tai virheellisestä palautuksesta.
- `content`: osat ratkaisun järjestyksessä. Teksti rivinvaihtoineen (`\n`). Kaava on LaTeX ja sen kuva PNG:nä
  (`png`, piirretty 3-kertaisena; `w`, `h` = näyttökoko pikseleinä; jos selain ei piirrä kuvaa, vain LaTeX).
  Kuva on PNG- tai JPEG-data base64-muodossa ilman `data:`-alkua. SVG- tai HTML-sisältöä ei hyväksytä.
  `w`, `h` = kuvan oma koko pikseleinä. Jos opiskelija on pienentänyt kuvaa editorissa (6.11.2026), `dw` on sen
  näyttöleveys CSS-pikseleinä (kokonaisluku, pienempi kuin `w`); arviointisivu näyttää kuvan siinä koossa, ja
  napsautus avaa sen täysikokoisena. Ilman `dw`:tä kuva näytetään omassa koossaan.
  Selaimen tilapäiset `blob:`-osoitteet muunnetaan dataksi. Verkko-osoitteesta liitetty kuva estää latauksen.
- `content_sha256` = SHA-256 (UTF-8) merkkijonosta `JSON.stringify(answers)`, jossa kaavoista on jätetty vain
  `type` ja `latex`. Samat ratkaisut pitävät saman `submission_id`:n (selaimen localStorage
  `ruukkilabra:palautus:<luku>`). Muuttunut teksti, kaava tai kuva (lisätty, vaihdettu, poistettu) antaa uuden.
  Tuonti laskee summan uudelleen, joten jälkikäteen muutettu tiedosto on *Virheellinen*.
- Tunniste ei todista tekijää. Palauttaja on Formsin vahvistettu sähköposti, ja järjestys on Formsin palautusaika
  (ei `exported`).

## Rajat

| | raja | peruste |
|---|---|---|
| tiedosto | 9 Mt | Formsin tiedostorajaksi asetetaan 10 Mt; Apps Script lukee tiedoston kerralla |
| kuva | 2 Mt, enintään 5000 px sivu | koko näytön kuvakaappaus mahtuu; arviointinäkymä hakee yhden tehtävän kerrallaan |
| kuvia | 40 / tiedosto | |
| teksti | 20 000 merkkiä / tehtävä | |
| kaava | 4000 merkkiä LaTeXia, kaavakuva 200 kt | |
| osia | 400 / tehtävä | |

Rajan ylitys näytetään opiskelijalle virheenä painikkeen alla (mikä tehtävä ja mikä raja), eikä tiedostoa ladata.
Kuvia ei pudoteta hiljaisesti. Kuvakaappaus liitetään editoriin Ctrl+V:llä; erillistä kuvapainiketta ei ole.

## Versio 2: itsearvio (6.11.2026)

Luvun sivulla, jonka *Tarkista osaamisesi* -osiossa on ohjattu itsearvio (`build.py` `SELF_ASSESS_COURSES`, aluksi FY3),
tiedoston `version` on 2 ja siinä on lisäksi

```json
"selfassessment": { "items": [
  { "id": "check-1", "level": "b", "history": [["d", "2026-11-06T15:21:44.750Z"], ["b", "2026-11-07T08:02:10.112Z"]] },
  { "id": "tavoite-1", "level": "c", "history": [["c", "2026-11-06T15:22:01.004Z"]] } ] }
```

- Kohteet ovat sivun järjestyksessä, ja mukana ovat vain arvioidut. `id` on Tarkista-osion tehtävän tunniste tai
  `tavoite-<n>` (luvun tavoite tai inquiry.json `self_extra` -väittämä). Kohteiden nimet ovat arviointisivun
  `Tehtavat.gs`:ssä (`self`), eivät tiedostossa.
- `level`: `a` (osaan niin hyvin, että voisin opettaa kaverille, tummanvihreä), `b` (koen oivaltaneeni, vihreä),
  `c` (osaan osittain, keltainen), `d` (tarvitsen vielä harjoitusta, punertava), `x` (ei vielä harjoiteltu, harmaa).
  Opiskelija näkee vain väriasteikon, ei kirjaimia.
- `history`: jokainen tason muutos aikaleimoineen (UTC), enintään 50 uusinta.
- `content_sha256` lasketaan versiossa 2 merkkijonosta `JSON.stringify({answers: <kuten yllä>, selfassessment: <items>})`,
  joten muuttunut itsearvio antaa uuden palautuksen.
- Tuonti hyväksyy versiot 1 ja 2. Arviointisivun *Osaamisen sormenjälki* näyttää ryhmän uusimpien palautusten tasot väreinä: rivit kohteita luvuittain, sarakkeissa opiskelijat, valkoinen = ei vastattu, harmaa = en ole vielä harjoitellut.

## Versio 3: kaikki vastaukset ja tavoitearvioiden kooste (6.11.2026)

Nykyinen `palautus.js` tekee aina version 3. Erot versioon 2:

```json
"includes": "answers",
"answers": [
  { "task": "fy3-1-L1-02", "status": "answered", "content": [],
    "responses": [ { "type": "number", "value": "6,0", "unit": "cm" } ] },
  { "task": "fy3-1:reflect", "status": "answered", "content": [],
    "responses": [ { "type": "choice", "question": "…", "answer": "Kyllä", "option": 0 },
                   { "type": "text", "label": "…", "text": "Ennustin väärin, koska …" } ] }
],
"selfassessment": { "goals": [
  { "id": "tavoite-1", "text": "Ymmärrän, mitä massa tarkoittaa.", "level": "a" },
  { "id": "tavoite-2", "text": "Osaan …", "level": null } ] }
```

- `answers` sisältää ensin luvun Tehtävät-osion tehtävät (tunniste kuten ennen) ja sitten oppitunnin tehtävät, joissa
  on vastauskenttä (ennusteet, kokeen taulukko, johtopäätös, Itsearvion tehtävät …). Oppitunnin tehtävän tunniste on
  `<luku>:<aktiviteetin id>`, koska samat id:t toistuvat luvuissa. Arviointisivu näyttää oppitunnin tehtävät mutta
  ei pisteytä niitä, joten pistemaksimit pysyvät ennallaan.
- `responses` on jokaisessa tehtävässä (tyhjä lista, jos ei vastauksia). Tyypit: `number` (`value` kirjoitettuna,
  `unit` jos kentässä on yksikkö), `choice` (`question`, `answer`, `option` = valinnan järjestysnumero), `text`
  (`label`, `text`), `truefalse` (`items`: `text`, `value` true/false/null), `order` (`items`: `text`, `rank` tai null),
  `table` (`head`, `rows`). Kysymys- ja vaihtoehtotekstit ovat pelkkää tekstiä, kaavat `$LaTeX$`-muodossa.
- `status` on `"answered"`, jos editorissa tai yhdessäkin vastauksessa on jotain. Pelkkä numero tyhjällä editorilla on siis vastaus.
- `selfassessment.goals`: luvun tavoitteet sivun järjestyksessä, kaikki mukana. `level` on opiskelijan viimeisin
  valinta: `a`–`d`, `x` = *En ole vielä harjoitellut*, `null` = ei vastattu. Tehtäväkohtaiset itsearviot ja
  muutoshistoria eivät tule tiedostoon; ne jäävät opiskelijan selaimeen.
- `content_sha256` = SHA-256 merkkijonosta `JSON.stringify({answers: <answers ilman kaavakuvia, responses mukana>, selfassessment: <goals>})`.
- Tuonti hyväksyy versiot 1, 2 ja 3. Vanhoista tiedostoista ei vaadita oppitunnin tehtäviä, ja version 2
  tehtäväkohtaiset arviot ohitetaan (luetaan vain tarkistussummaa varten).

## Uusi versio
Muutos, jota versio 1 ei ymmärrä, nostaa `version`-numeroa. Skripti hylkää tuntemattoman uudemman version
syyllä *uudempi kuin tämä skripti tuntee*, eikä lue sitä puoliksi.

## Opintojakson työtiedosto `Ruukkilabra_<FY>_<pvm>_<aika>.json` (ruukkilabra-tyo, versio 1, 7.11.2026)

Moduuleissa FY1–FY8 opiskelijalla on yksi työ opintojaksoa kohti. Sama tiedosto on opiskelijan varmuuskopio ja
opettajalle palautettava työ. Sen tekevät kaikki tallennuspainikkeet samalla tavalla: luvun *Tallenna työ tiedostoon*
ja *Palauta*, moduulisivun *Tallenna työ tiedostoon* ja editorin *Tallennetut ratkaisut* -vienti. Moduulisivun
*Avaa tallennettu työ* ja editorin tuonti avaavat sen (`templates/palautus.js`, "Work file").

```json
{ "format": "ruukkilabra-tyo", "version": 1, "course": "FY3", "lang": "fi", "created": "2026-11-07T12:30:25.000Z",
  "submission_id": "32 heksamerkkiä", "content_sha256": "64 heksamerkkiä",
  "chapters": [ { "chapter": "fy3-1", "answers": [ { "task": "fy3-1-L1-06", "status": "answered",
       "content": [ { "type": "text", "text": "…" }, { "type": "math", "latex": "G=mg", "png": "…", "w": 58, "h": 15 },
                    { "type": "image", "mime": "image/png", "w": 640, "h": 320, "ref": 0 } ],
       "responses": [ { "type": "number", "value": "39" } ] } ],
     "selfassessment": { "goals": [ { "id": "tavoite-1", "text": "", "level": "b" } ] } } ],
  "progress": { "course": "FY3", "assigned": ["fy3-1-L1-06", "…"], "done": [["fy3-1-L1-06", "2026-11-05T10:12:00.000Z"]],
                "history": [["fy3-1-L1-06", "2026-11-05T10:12:00.000Z", 1]] },
  "store": { "local": { "<localStorage-avain>": "<arvo>" }, "solutions": [ { "id", "html", "page", "updated" } ] } }
```

- `created` ja tiedostonimi: tallennusaika, uusi jokaisella tallennuksella. `progress.done`: Tehty-merkinnät ja niiden
  valmistumisajat, jotka säilyvät tallennuksessa ja avauksessa; uusi merkintä saa uuden ajan. `history`: merkinnät (1)
  ja niiden poistot (0). Ne ovat opiskelijan omaa etenemisgraafia varten. `progress` on `null`, jos moduulissa ei ole
  annettuja tehtäviä.
- `store`: kaikki, mitä selain pitää tästä moduulista (ratkaisueditorin tietueet, joiden tunniste alkaa `fy3-`, ja
  moduulin sivujen localStorage-avaimet: vastaukset, valinnat, selitykset, taulukot, itsearviot). Avaus kirjoittaa ne
  takaisin. Ensin tarkistetaan tiedoston muoto, versio, moduuli, tarkistussumma ja jokainen tietue. Mitään ei kirjoiteta,
  jos jokin ei täsmää. Selaimesta puuttuvat tiedot lisätään. Jos sama kohta on molemmissa eri sisältöisenä, opiskelijalta
  kysytään kerran: tiedosto korvaa (OK) tai selaimen tiedot säilyvät ja vain puuttuvat lisätään (Peruuta). Kysymys
  kertoo, montako selaimen tiedoista on uudempia.
- `chapters`: opettajan näkymä. Mukana ovat vain luvut, joissa on jotakin. Kuvan data on vain `store.solutions`-tietueen
  HTML:ssä, ja kohteen `ref` kertoo, monesko PNG- tai JPEG-kuva se on. Opettajan skripti hakee kuvan sieltä.
- `content_sha256` = SHA-256 merkkijonosta `JSON.stringify({ chapters, progress, store })`.
- Arviointi (`Code.gs` `rlValidateWork_`): jokainen luku tarkistetaan kuten luvun palautus (versio 3) ja kirjataan
  omalle rivilleen (avain `<lomakkeen rivi>#<luku>`). Taulukkoon ja arviointinäkymään tulevat vain Tehty-merkinnät
  (`Eteneminen`: `<annettuja>|<tehtävä>,…`). Valmistumisaikoja ja etenemisgraafia ei näytetä eikä käytetä arviointiin.
  Vanhat luvun tiedostot (`ruukkilabra-palautus`, versiot 1–4) kelpaavat edelleen.
