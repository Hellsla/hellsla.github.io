# Palautustiedosto `<luku>.ratkaisut.json` (ruukkilabra-palautus, versio 1)

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
  opiskelijoille tarvittaessa itse, mitä tiedostossa on: **mukana on vain** luvun tehtävien *Kirjoita ratkaisu* -editorien sisältö, tälle laitteelle tallennettuna.
  Tarkista-kenttien luvut ja valintatehtävien valinnat eivät tule mukaan, koska niitä ei tallenneta. Ei nimeä,
  sähköpostia eikä muiden lukujen ratkaisuja.
- `answers`: jokainen luvun tehtävä kerran sivun järjestyksessä. Tyhjä editori on `"empty"` ilman sisältöä.
  Puuttuva tehtävä tai rikkinäinen tiedosto on tuonnissa *Virheellinen*, joten opettaja erottaa vastaamattoman
  tehtävän puuttuvasta tai virheellisestä palautuksesta.
- `content`: osat ratkaisun järjestyksessä. Teksti rivinvaihtoineen (`\n`). Kaava on LaTeX ja sen kuva PNG:nä
  (`png`, piirretty 3-kertaisena; `w`, `h` = näyttökoko pikseleinä; jos selain ei piirrä kuvaa, vain LaTeX).
  Kuva on PNG- tai JPEG-data base64-muodossa ilman `data:`-alkua. SVG- tai HTML-sisältöä ei hyväksytä.
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

## Uusi versio
Muutos, jota versio 1 ei ymmärrä, nostaa `version`-numeroa. Skripti hylkää tuntemattoman uudemman version
syyllä *uudempi kuin tämä skripti tuntee*, eikä lue sitä puoliksi.
