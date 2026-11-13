VERDICT: PASS
CONTENT-HASH: 0e1ca561eb3c7a3f
SCOPE: delta added-exercise from 2af3ee47b4394d1d base 81db4a6fd727
## Blocking

## Polish
- content/fi/FY4/fy4-4/exercises/solutions.md (L1-09) — Periaate mainitsee voimakuvion, mutta ratkaisussa ei ole kuviota. Lohko ```voimakuvio```, jossa $\overline{F}$ osoittaa ylös ja $\overline{G}$ alas, noudattaisi luvun ohjetta "Ensin voimat, sitten yhtälö". Huomio on siirtynyt edelliseltä kierrokselta.
- solutions.md (L2-09) — kärryn A massa on nyt sama kuin L1-10:n vastaus $0{,}50\,\text{kg}$, joten L2-09 on L1-10 ja yksi askel lisää. Fysiikassa tässä ei ole virhettä. Väriä kutsutaan L1-10:ssä "tumma" ja L2-09:ssä "tummanharmaa". Yksi ja sama sana olisi selkeämpi.

## Checked
- L2-09 käyttää nyt kärryä A. Kuvasta luetaan piste $(3{,}0\,\text{N};\, 6{,}0\,\text{m/s}^2)$, josta $m_\text{A} = 0{,}50\,\text{kg}$. Silloin $a = 2{,}4\,\text{N} : 0{,}50\,\text{kg} = 4{,}8\,\text{m/s}^2$. Järkevyystarkistus pitää paikkansa: kohdassa $2{,}4\,\text{N}$ A:n suora on välillä $4$–$6\,\text{m/s}^2$, ja tulos on pienempi kuin $6{,}0\,\text{m/s}^2$.
- Laskin vastaukset uudelleen yhdessä skriptissä `python -I answers.py`:n rinnalla. L1-09 antaa $31{,}83\,\text{kN}$, L1-10 $0{,}50\,\text{kg}$ ja L2-09 $4{,}8\,\text{m/s}^2$. Kaikki kolme täsmäävät exercises.json:n kanssa.
- L1-09: $F - mg = ma$, kun ylöspäin on positiivinen, joten $F = m(g + a)$. Kuun $g = 1{,}622\,\text{m/s}^2$ on MAFY-taulukon arvo. Vastaus $32\,\text{kN}$ eroaa tarkasta arvosta 0,5 %, joten se mahtuu toleranssiin.
- Kuvan $(\Sigma F, a)$-suorat kulkevat origon kautta, ja kaikki pisteet ovat ruudukon risteyksissä. Kuvaus ei anna massoja.
- Merkinnät ovat samat kuin luvussa ($\Sigma F$, $m$, $a$ ja yläviivalliset vektorit), ja sisältö pysyy FY4:n alueella.
- Hash 0e1ca561eb3c7a3f sekä alussa että lopussa.
