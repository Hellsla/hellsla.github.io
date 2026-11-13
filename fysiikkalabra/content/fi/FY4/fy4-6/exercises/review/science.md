VERDICT: PASS
CONTENT-HASH: c38d31b78cf4dc01
## Blocking

## Polish
- content/fi/FY4/fy4-6/exercises/exercises.json (L2-09 text) — "kitkavoima mitattiin" ei nimeä liikekitkaa, kuten ratkaisu tekee. Koska palikkaa "vedettiin", lukija voi päätellä liikkeen, mutta "liikekitka" sanoisi mallin ehdon suoraan.
- lessons/FY4/fy4-6/answers.py (L2-09) — kulmakerroin 0,2145 on kirjoitettu käsin eikä laskettu `MITTAUS`-pisteistä. Huomio on siirtynyt edelliseltä kierrokselta.

## Checked
- Muutos koskee vain L2-09:n aloitusta, johon on lisätty "(esimerkkiaineisto)". Tehtävä merkitsee nyt aineistonsa esimerkkiaineistoksi samoin kuin ratkaisu, kuvan kuvaus ja L2-03. Tämä noudattaa ohjeen sääntöä "kerro, onko luku mitattu, simuloitu vai laskettu".
- Luvut, massa $0{,}80\,\text{kg}$, ehdot ("vain paino, tukivoima ja kitka") ja kysymys ovat ennallaan, ja kysymys on yhä viimeinen lause.
- Laskin vastauksen uudelleen. Origon kautta sovitettu PNS-kulmakerroin on 0,21455, jolloin $F_\mu(7{,}848\,\text{N}) = 1{,}684\,\text{N}$ ja $a = 2{,}105\,\text{m/s}^2$. exercises.json antaa 2.1 ja toleranssin 0,05, joten arvo on sama.
- Hash c38d31b78cf4dc01 sekä alussa että lopussa.
