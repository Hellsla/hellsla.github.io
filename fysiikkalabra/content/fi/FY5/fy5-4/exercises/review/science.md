VERDICT: PASS
CONTENT-HASH: 70d174f2f9293390
SCOPE: delta added-exercise from a6b9feb8d21605fb base 8f23aa7ae3bd

## Blocking

## Polish

## Checked
- Hash oli sama alussa ja lopussa. Arvioin vain tehtävät L2-09 ja L3-06 (kierros 3).
- L2-09:n uusi piste: kuvaaja-a:n käyrä on v²/75, ja piste (15 m/s; 3,0 m/s²) on käyrällä. Siitä r = v²/a_n = 225/3,0 = 75 m, sama kuin answers.py:ssä. L1-01:ssä luvut ovat 20 m/s, 5,0 m/s² ja 80 m, joten L2-09 ei enää toista sitä.
- Kuvaaja-b mahtuu nyt kuvaan: käyrä päättyy kohtaan 24 m/s, jossa arvo on 11,52 kN eli alle y-akselin ylärajan 12 kN. Kuvaaja-a:n suurin arvo on 11,2 alle rajan 12.
- L3-06: 1,2·20²/60 = 8,0 kN, ja μ0 = 8000/(1200·9,81) = 0,6796 ≈ 0,68. Malli on oikea: kitka on ainoa vaakasuora voima, N = mg ja rajatapaus F = μ0N. Tehtävä kertoo nämä oletukset.
- Lukeminen: piste 15 on numeroidulla apuviivalla. Arvo 3 on apuviivalla numeroiden 2 ja 4 välissä, ja pisteeseen on piirretty apuviivat. Kahden merkitsevän numeron vastaukset 75 m ja 0,68 pysyvät toleranssin 2 % sisällä.
- Järkevyystarkistukset ovat oikein: 3,0/9,81 ≈ 0,3 g, ja nopeudella 10 m/s a_n = 1,33 m/s². L3-06:ssa vertailu kuivaan ja märkään asfalttiin on oikein.
- Alt-tekstit antavat samat pisteet kuin kuvat. Säde ei näy kummassakaan kuvassa.
