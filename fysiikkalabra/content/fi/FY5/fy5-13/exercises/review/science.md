VERDICT: PASS
CONTENT-HASH: 0babe27b05324bcf
SCOPE: delta added-exercise from c716085d5bc703dc base 81db4a6fd727

## Blocking

## Polish
- exercises.json (L2-09 ja L2-04) — L2-09 on L2-04 käänteisenä samassa kuvassa. Kuvasta luetaan sama tieto (L = 1,20 m, n = 4) ja aallonpituus on sama λ = 0,60 m, mutta kysytään f eikä v. Tehtävä ei paljasta L2-04:n vastausta, mutta tuo vähän uutta. Ehdotus: kysy seuraavan moodin taajuutta (n = 5) tai sitä, mikä taajuus antaa kolme silmukkaa.

## Checked
- Hash oli sama alussa ja lopussa. Arvioin vain tehtävät L1-09 ja L2-09.
- Kierroksen 1 korjaukset on tehty. L1-09:n järkevyystarkastelussa todetaan nyt oikein, että äänihuulten perustaajuus ei juuri muutu ja että ääniväylän resonanssitaajuudet nousevat. Nopeuksien suhde on 2,93, mikä on noin 1,55 oktaavia, eli "noin puolitoista oktaavia" pitää paikkansa. L2-09:ssä on nyt v = 75,0 m/s, joten vastaus 125 Hz on kolmen merkitsevän numeron tarkkuudella, ja toleranssi 2 % sopii.
- Laskin uudelleen. L1-09: Δf = (971 − 331,5)/(2·0,50) = 639,5 Hz. L2-09: f = nv/(2L) = 4·75,0/2,40 = 125 Hz. Molemmat vastaavat answers.py:tä ja exercises.json:ia.
- Kuvaa kuvio-tehtava käytetään vain tehtävissä, ei inquiry.json:ssa. Kuvassa on neljä silmukkaa ja viisi solmua, ja viivain kulkee 0–1,20 m. Alt-teksti vastaa kuvaa.
- MAFY-arvot ovat samat kuin kierroksella 1. Kummankin kaasun lämpötila on 0 °C, ja ±4 %:n toleranssi on mainittu.
