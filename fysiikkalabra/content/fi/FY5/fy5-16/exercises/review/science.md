VERDICT: PASS
CONTENT-HASH: f7420c067b94a929
SCOPE: delta added-exercise from 9b2ee0bf44613b3e base 81db4a6fd727

## Blocking

## Polish
- exercises.json (L2-09 ja L2-07) — L2-09 (105 dB, vastaus minuutteina) on sama lasku kuin L2-07 (109 dB). Uutta on vain kuvan lukeminen. Tämä on hyväksyttävää.

## Checked
- Hash oli sama alussa ja lopussa. Arvioin vain tehtävät L1-09 ja L2-09.
- Kierroksen 1 korjaukset on tehty. Tehtävät käyttävät nyt kuvaa scale-tehtava, jossa jokaisen merkin taso on kirjoitettu näkyviin (90 dB ja 105 dB), joten lukeminen on tarkka ja toleranssi 2 % on mielekäs. L1-09:n järkevyystarkistus sanoo nyt oikein: 90 dB on lähempänä 91 dB:ä, ja 2,5 h on lähempänä 2 tuntia.
- Laskin uudelleen. L1-09: 8 h/2^(5/3) = 2,52 h, joten vastaus 2,5 h. L2-09: 480 min/2^(20/3) = 4,72 min, joten vastaus 4,7 min. Molemmat vastaavat answers.py:tä ja exercises.json:ia. L2-09:n tarkistus (20 dB on noin 100-kertainen intensiteetti, joten 4,8 min) on oikein.
- Malli on luvun mukainen: vertailuaika t_v = t_0/2ⁿ, missä n = (L − 85 dB)/3 dB. Vertailuaikaa ei kutsuta sallituksi eikä turvalliseksi ajaksi, kuten ohjeistus edellyttää.
- Kuvaa scale-tehtava käytetään vain tehtävissä, ei inquiry.json:ssa. figures.py:ssä merkit ovat tarkalleen kohdissa 90 ja 105 dB, ja alt-tekstissä on samat arvot.
