VERDICT: PASS
CONTENT-HASH: b33472b62ddc7aeb
## Blocking

## Polish
- content/fi/FY4/fy4-6/exercises/exercises.json (L2-09 text) — uusi aloitus sanoo pelkän "kitkavoima mitattiin", vaikka aiempi teksti ja ratkaisu puhuvat liikekitkasta. Koska "puupalikkaa vedettiin", lukija voi päätellä liikkeen, mutta "liikekitka mitattiin, kun palikkaa vedettiin tasaisella nopeudella" sanoisi mallin ehdon suoraan. Tehtäväteksti puhuu nyt kokeesta, kun taas ratkaisu ja kuvan kuvaus käyttävät sanaa "esimerkkiaineisto". Lisää "(esimerkkiaineisto)" myös tehtävätekstiin, kuten L2-03 tekee.
- lessons/FY4/fy4-6/answers.py (L2-09) — kulmakerroin 0,2145 on kirjoitettu käsin eikä laskettu `MITTAUS`-pisteistä. Huomio on siirtynyt edelliseltä kierrokselta.

## Checked
- Muutos koskee vain L2-09:n aloituslausetta. Luvut, massa, ehdot ("vain paino, tukivoima ja kitka") ja kysymys ovat ennallaan, ja kysymys on yhä viimeinen lause.
- Uusi kehys (palikkaa vedettiin pöydällä ja kitkavoima mitattiin eri tukivoimilla) vastaa kuvaa, jossa $F_\mu$ on piirretty $N$:n funktiona. Se on myös sama malli kuin ratkaisussa ($F_\mu = \mu N$, suora kulkee origon kautta).
- Laskin vastauksen uudelleen samassa skriptissä. Origon kautta sovitettu PNS-kulmakerroin on 0,21455, jolloin $F_\mu(7{,}848\,\text{N}) = 1{,}684\,\text{N}$ ja $a = 2{,}105\,\text{m/s}^2$. exercises.json antaa 2.1 ja toleranssin 0,05, joten arvo on sama.
- Hash b33472b62ddc7aeb sekä alussa että lopussa.
