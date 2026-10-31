VERDICT: PASS
CONTENT-HASH: 47b36b1d0f3d0d64

## Blocking

(none)

## Polish

- inquiry.json exp-3 (rivi ~507) — kokeella 3 ei ole `question`-kenttää, vaikka intro kysyy "Miten impulssi riippuu massasta?"; opiskelija ei saa vastausta eikä palautetta (koe on valinnainen) — lisää lyhyt valintakysymys ($I$ on suoraan verrannollinen massaan, $F_\text{max}$ samoin).
- inquiry.json exp-1/exp-2 "Vakiona/Muutetaan"-rivi (kuvakaappaus lab-1280-1) — lauseessa "Vakiona: massa $m$ , alkunopeus $v_0$, törmäys." jää tyhjä väli ennen pilkkua ja arvot puuttuvat; rivi näyttää keskeneräiseltä — tarkista, että nimet renderöityvät ilman ylimääräistä väliä.
- inquiry.json simulaatio `model` — kappale on pitkä ja sisältää useita yksityiskohtia (sinipulssi, 0,64 F_max, jäykkyyssuhde 16); 17-vuotiaalle riittäisi kolme virkettä, loput `calc`-laatikkoon.
- lesson.md "Vastaus alun kysymykseen" — kappale on tiivis; väite "painuu kymmenien senttimetrien matkalta" kannattaisi tukea yhdellä luvulla (esim. 30 cm vs. 3 cm), niin aikasuhde tulee konkreettiseksi.

## Checked

- Polku: kertaus (F=ma) → ennusteet → simulaatio → kokeet → teoria → esimerkki → siirto; vain liikemäärä ja impulssi, ei törmäysten säilymislakia. Alun kysymys vastataan vasta teoriassa, kun opiskelija on sitoutunut.
- Ennusteet 1 ja 2 ovat kumottavissa kokeiden 1 ja 2 mittauksilla; väärien vaihtoehtojen palaute korjaa väärinkäsityksen (impulssi pienenee, kimpoamisessa ei impulssia).
- Simulaatio on mielekäs: kova/pehmeä puskuri, pysähtyminen/kimpoaminen; impulssi (pinta-ala) ja Δp (nopeuksista) lasketaan erikseen, joten yhtäsuuruus on todiste, ei laskennan toisto. Mallin oletukset ilmoitettu.
- Kuvat (fig-3, fig-6, hero) luettavissa 390 px:ssä; väri ei yksin kanna merkitystä (kova/pehmeä nimetty, katkoviiva); fig-3:n teksti ei paljasta impulssin arvoa ennen ennustetta teoriavaiheessa.
- Check-2:n kuva on välttämätön vastaamiseen (huippuarvo ja kesto vain kuvaajassa); vihjeet etenevät kolmeen vaiheeseen; mistakes-arvot (24, 5,4, 12000) vastaavat todellisia virheitä.
- Esimerkki: yksi vaihe kerrallaan, etumerkkivalinta perusteltu, järkevyystarkistus (paino ≈ 0,57 N, virheellinen 145 N); laskut tarkistettu (870 N).
- Siirto (80 N) ja ratkaisu seurattavissa; paino ei vaikuta vaakasuuntaan perusteltu.
- Check-1 vastavaihtoehdot ovat käsitepohjaisia; check-3:n kriteerit ovat havaittavia ja vastaavat kysymystä.
- Suomi: "80 N:n" -taivutus, termit (liikemäärä, impulssi, impulssiperiaate) sanaston mukaisia; ei virheitä löytynyt.
- Puhelin 390 px: simulaation ohjaimet ja lukemat ymmärrettävät; 1280 px:n asettelu selkeä.
