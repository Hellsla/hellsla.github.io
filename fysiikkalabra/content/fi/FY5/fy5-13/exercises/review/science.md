VERDICT: PASS
CONTENT-HASH: 1d5f9df3a4fed506
SCOPE: delta added-exercise from c716085d5bc703dc base 81db4a6fd727

## Blocking

## Polish
- exercises.json (L2-09 ja L2-04) — samassa kuvassa on L2-04:ssä f = 100 Hz ja v = 60 m/s, mutta L2-09:ssä v = 75,0 m/s. Ristiriitaa ei ole, koska kuvassa ei ole lukuja punnuksesta tai kireydestä. Sivulause "kun punnus on raskaampi" tekisi kuitenkin eron selväksi.

## Checked
- Hash oli sama alussa ja lopussa. Arvioin vain tehtävät L1-09 ja L2-09 (kierros 3).
- L2-09:ssä kysytään nyt taajuuden nousua seuraavaan silmukkamäärään. Kuvasta luetaan L = 1,20 m ja n = 4, joten f₄ = 125 Hz ja f₅ = 156,25 Hz, ja nousu on v/(2L) = 31,25 Hz. Tulos on sama kuin answers.py:ssä. Ratkaisussa erotus muodostetaan symbolisesti ennen sijoitusta.
- Toistoa ei ole: L2-04 kysyy samasta kuvasta aallon nopeutta. L3-02 päättelee perustaajuuden kahdesta annetusta taajuudesta, eikä siinä lueta kuvaa. Kuvaa ei käytetä inquiry.json:ssa.
- Merkitsevät numerot: vastaus 31,3 Hz on kolmen numeron tarkkuudella kuten 75,0 m/s ja 1,20 m. Arvo on 0,2 %:n päässä tarkasta arvosta 31,25, joten se on toleranssin 2 % sisällä.
- L1-09: (971 − 331,5)/1,00 = 639,5 Hz. MAFY-arvot (helium 971 m/s, ilma 0 °C 331,5 m/s) ovat VERIFIED-riveiltä, ja toleranssi on 4 %.
- Järkevyystarkistukset ovat oikein: peräkkäisten ominaistaajuuksien erotus on f₁. Heliumin ääni on 2,93-kertainen, eli noin 1,55 oktaavia.
