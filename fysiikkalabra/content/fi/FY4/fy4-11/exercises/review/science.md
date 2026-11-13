VERDICT: PASS
CONTENT-HASH: 2f7544a1c68c1bc4
SCOPE: delta added-exercise from 3a2e90bccdbd2345 base 81db4a6fd727
## Blocking

## Polish
- content/fi/FY4/fy4-11/exercises/solutions.md (L1-09 Vastaus) — "kaksi merkitsevää numeroa nopeuden $80\,\text{km/h}$ tarkkuudella": tarkkuutta rajaa todellisuudessa taulukon $\mu = 0{,}8$, ja välin vaikutus selitetään heti perään. Lause "kaksi numeroa; kitkakertoimen väli vaikuttaa tulokseen enemmän kuin pyöristys" kattaisi molemmat.
- solutions.md (L3-06 Vastaus) — "kolmas numero säilytetään, ettei välitulosten pyöristys vääristä tulosta": $10{,}5\,\text{kN}$ on lopputulos eikä välitulos. Lisäksi "Massa" on kirjoitettu isolla pilkun jälkeen. Huomio on siirtynyt edelliseltä kierrokselta.
- exercises.json (L1-09) — tehtäväteksti käyttää jarrutusmatkasta tunnusta $s$, luku tunnusta $s_\text{j}$. Huomio on siirtynyt edelliseltä kierrokselta.

## Checked
- L1-09: väli on nyt kuvattu oikein. $\mu = 0{,}8$ antaa $a = 7{,}85\,\text{m/s}^2$ ja $s = 31{,}46\,\text{m} \approx 31\,\text{m}$, mikä on välin lyhyempi ääripää. $\mu = 0{,}5$ antaa $50{,}3\,\text{m}$, mikä on pidempi. Tehtävä pyytää välin suurinta arvoa, ja vastaus vastaa sitä. Toleranssi 0,05 hyväksyy arvot $30$–$33\,\text{m}$. Sana "liukukitkakerroin" on opettajan valinta.
- L1-09:n fysiikka: tie on vaakasuora, pyörät ovat lukossa ja ilmanvastus jätetään huomiotta, joten $N = mg$, $a = \mu g$ ja $s = v_0^2/(2\mu g)$. Vertailu ABS-jarrutukseen ($\mu \approx 0{,}9$, luvun $9{,}0\,\text{m/s}^2$) pitää paikkansa, koska liukuva rengas pitää huonommin.
- Laskin vastaukset uudelleen yhdessä skriptissä `python -I answers.py`:n rinnalla. L1-09 antaa $31{,}46\,\text{m}$, L2-09 $20 + 25 = 45\,\text{m}$ ja L3-06 $17{,}5 - 7{,}0 = 10{,}5\,\text{kN}$. Kaikki täsmäävät exercises.json:n kanssa.
- Kuvien arvot ovat ruudukon risteyksissä, ja kuvaukset antavat samat arvot.
- Hash 2f7544a1c68c1bc4 sekä alussa että lopussa.
