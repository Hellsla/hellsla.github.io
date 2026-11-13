VERDICT: PASS
CONTENT-HASH: 7c5b2c273c5f7baf
SCOPE: delta added-exercise from 6f0e928ad88d259e base 81db4a6fd727
## Blocking

## Polish
- solutions.md L2-09 ja L3-06 Kuvaajan lukeminen — kulmakerroin lasketaan raakapisteestä $(2{,}0\,\text{s};\, 3{,}9\,\text{m/s})$ ja origosta. Sano, että piste luetaan origon ja pisteiden kautta piirretyltä suoralta. Huomio on siirtynyt edelliseltä kierrokselta.

## Checked
- L3-06:n Vastaus a on nyt $m_1 \approx 1{,}2\,\text{kg}$, jossa on kaksi merkitsevää numeroa. Perusteluna mainitaan $0{,}30\,\text{kg}$ ja luettu kiihtyvyys, joten rivi on johdonmukainen. Toleranssi 4 % hyväksyy sekä arvon $1{,}2$ että $1{,}21$.
- Laskin vastaukset uudelleen yhdessä skriptissä `python -I answers.py`:n rinnalla. $a = 3{,}9/2{,}0 = 1{,}95\,\text{m/s}^2$. L2-09 antaa $T = 0{,}80 \cdot 1{,}95 = 1{,}56\,\text{N}$ (vastaus $1{,}6$, ero 2,5 %, toleranssi 4 %). L3-06 antaa $m_1 = 0{,}30\,(9{,}81/1{,}95 - 1) = 1{,}209\,\text{kg}$.
- L3-06 b: $T = 2{,}36\,\text{N} < m_2 g = 2{,}94\,\text{N}$, ja perustelu ($m_2 g - T = m_2 a > 0$) pitää paikkansa.
- Voimakuviot vastaavat liikettä: $G_1 = N$, $T_1 = T_2$, $T_2$ on lyhyempi kuin $G_2$ ja punnuksen $a$ osoittaa alas. Kolmannen lain pareja ei ole samassa kuviossa.
- Hash 7c5b2c273c5f7baf sekä alussa että lopussa.
