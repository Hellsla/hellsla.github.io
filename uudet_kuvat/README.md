# Uudelleen piirretyt kuvat FY1–FY10 ja FY14

Opettajan 15.–17.11.2026 hyväksymät kuvat, jotka Codex piirsi uudelleen Ruukkilabran alkuperäisistä kuvista.
Tämä kansio on vain kuvien säilytystä ja lataamista varten. **Haaraa ei yhdistetä `main`iin**: zipit ovat yhteensä
noin 600 Mt ja jäisivät repositorion historiaan pysyvästi.

| Paketti | Kuvia | Niistä kaavioita merkintöineen |
|---|---|---|
| `FY1-hyvaksytyt-kuvat.zip` | 36 | 15 |
| `FY2-hyvaksytyt-kuvat.zip` | 20 | 12 |
| `FY3-hyvaksytyt-kuvat.zip` | 68 | 43 |
| `FY4-hyvaksytyt-kuvat.zip` | 75 | 60 |
| `FY5-hyvaksytyt-kuvat.zip` | 94 | 72 |
| `FY6-hyvaksytyt-kuvat.zip` | 79 | 58 |
| `FY7-hyvaksytyt-kuvat.zip` | 89 | 61 |
| `FY8-hyvaksytyt-kuvat.zip` | 55 | 39 |
| `FY9-hyvaksytyt-kuvat.zip` | 41 | 29 |
| `FY10-hyvaksytyt-kuvat.zip` | 62 | 39 |
| `FY14-hyvaksytyt-kuvat.zip` | 43 | 15 |

Jokaisessa zipissä:

- `kuvat/`: hyväksytyt kuvat sellaisinaan, ilman merkintöjä (nämä menevät sivustolle)
- `merkinnoin/`: kaaviot merkintöineen, sellaisina kuin opettaja ne hyväksyi (vertailua varten)
- `ASETTELU.tsv`: missä kohdassa kuva on alkuperäisen kuvan omissa yksiköissä ja mitä merkintöjä on siirretty
- `PAATOS.txt`: opettajan päätös, hyväksyttyihin kuviin liittyvät huomiot ja uudelleen piirtämättä jääneet kuvat

Kuvat eivät ole vielä sivustolla. Ne viedään Ruukkilabraan vasta, kun julkaisuputki osaa käyttää kuvatiedostoa
kuvan pohjana (jaettu muutos, oma työjonon kohtansa). Kuvaajia ei piirretty uudelleen.

## Vaihdettavuuden tarkistus (18.11.2026)

`VAIHDETTAVUUS.tsv`: jokainen 662 hyväksytystä kuvasta tarkistettu julkaistuilta sivuilta (suomi ja englanti;
selkosuomen kuvat ovat samat kuin suomen). Yhtään estettä vaihtamiselle ei löytynyt: yksikään kuva ei piirry selaimessa,
skripti ei muuta yhtäkään, eikä missään ole animaatiota, valittavia osia tai tekstiä, joka katoaisi.

Korjattu 18.11.2026 opettajan pyynnöstä, minkä jälkeen kaikki 662 kuvaa läpäisevät tarkistuksen ilman huomioita:

- FY8: kaikki 55 kuvaa suurennettu samaan pikselimäärään kuin muissa moduuleissa (noin 1,57 megapikseliä). Suurennus
  on tehty kuvankäsittelyllä, joten uutta yksityiskohtaa ei ole syntynyt: jos Codexin pienentämättömät versiot saadaan,
  ne korvaavat nämä.
- FY3: monivalinnan neljästä vaihtoehtokuvasta (`fy3-1/pick-*`) poistettu kehys, joka oli vain kolmessa.
- FY9: kuvat `fy9-voimat/nimeton-1`, `-3` ja `-9` täydennetty alkuperäiseen kuvasuhteeseen (kuvaa ei venytetty).

Korjaukset on kirjattu myös kyseisten pakettien `PAATOS.txt`-tiedostoihin.

Muut huomiot:

- 50 kuvaa on monivalintatehtävien vastausvaihtoehtoja (13 tehtävää). Jokaisessa tehtävässä kaikki vaihtoehdot vaihtuvat
  ja näyttävät keskenään samanlaisilta.
- Englanninkielisiä merkintöjä ei verrattu 91 kuvassa (FY10 ja kuvauksesta tunnistettavat kuvat), ja kuvissa
  `fy2-7/district`, `fy2-7/grid` ja `fy2-7/storage` englanninkielinen versio poikkeaa hieman suomenkielisestä.
- Opettajan yleisohje 17.11.2026: jos kuva on osa vuorovaikutteista elementtiä, sitä ei korvata.

Tarkistus on tekninen. Fysiikan sisältöä ja mittasuhteita koskevat huomiot ovat kunkin paketin `PAATOS.txt`-tiedostossa.
