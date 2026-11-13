VERDICT: PASS
CONTENT-HASH: 682917e1074659db
SCOPE: delta added-exercise from 23f25874b515562a base 81db4a6fd727

## Blocking

## Polish

## Checked
- Hash oli sama alussa ja lopussa. Arvioin vain tehtävän L1-10 (kierros 3).
- Laskin uudelleen figures.py:n datasta: P on 4 ruutua oikealla ja 3 ylempänä, joten OP = √(4² + 3²) = 5 ruutua = 0,50 m. Sauvaa vastaan kohtisuoran voiman varsi on koko sauva, joten M = 30 N · 0,50 m = 15 Nm. Tulos on sama kuin answers.py:ssä ja exercises.json:ssa.
- Toistoa ei ole: L1-04 lukee samasta kuvasta vaakavoiman varren (3 ruutua). L1-10 lukee sauvan pituuden (5 ruutua) ja käyttää uutta voiman suuntaa. Edellisen kierroksen huoli on siis poistunut.
- Merkitsevät numerot: 30 N:ssa on kaksi merkitsevää numeroa ja vastauksessa 15 Nm samoin. Ruudukosta luettu pituus on tarkka, ja toleranssi 2 % sopii.
- Ratkaisussa on kaikki seitsemän osaa, ja r = OP perustellaan symbolisesti ennen sijoitusta. Järkevyystarkistus vertaa kuvan vaakavoimaan (0,30 m, 9,0 Nm), ja tarkistus on oikein.
- Kuva ja sen kuvaus antavat tiedot, jotka tehtävä tarvitsee, eivätkä ne paljasta vastausta.
