## fy6-2-L1-01
**Annettu:** lukema $U = 12{,}46\,\text{V}$ alueella $20\,\text{V}$, resoluutio $r = 0{,}01\,\text{V}$, virheraja $\pm(0{,}5\,\% + 2\ \text{numeroa})$
**Kysytty:** lukeman virheraja $\Delta U$ voltteina
**Periaate:** Valmistajan ilmoittama virheraja koostuu kahdesta osasta: osuudesta lukemasta ja muutamasta viimeisen numeron askeleesta. Yksi ”numero” tarkoittaa alueen resoluutiota eli pienintä askelta, jonka näyttö voi ottaa, tässä $0{,}01\,\text{V}$.
**Kaava:** $\Delta U = p \cdot U + n \cdot r$
**Muunnokset:** $p = 0{,}5\,\% = 0{,}005$; muita muunnoksia ei tarvita, koska lukema ja resoluutio ovat voltteina.
**Sijoitus:** $\Delta U = 0{,}005 \cdot 12{,}46\,\text{V} + 2 \cdot 0{,}01\,\text{V} = 0{,}0623\,\text{V} + 0{,}02\,\text{V} = 0{,}0823\,\text{V}$
**Vastaus:** $0{,}08\,\text{V}$, yksi merkitsevä numero, koska virheraja pyöristetään kuten virhe-arvio (laskimen arvo $0{,}0823\,\text{V}$).
**Järkevyys:** Prosenttiosa on noin puolet sadasosasta $12\,\text{V}$:sta eli noin $0{,}06\,\text{V}$, ja kaksi askelta lisää $0{,}02\,\text{V}$: yhteensä noin $0{,}08\,\text{V}$. Virheraja on alle prosentti lukemasta, mikä sopii hyvään mittariin.

## fy6-2-L1-02
**Annettu:** lukema $I = 146{,}3\,\text{mA}$ alueella $200\,\text{mA}$, resoluutio $r = 0{,}1\,\text{mA}$, virheraja $\pm(1{,}0\,\% + 2\ \text{numeroa})$
**Kysytty:** lukeman virheraja $\Delta I$ milliampeereina
**Periaate:** Virheraja on prosenttiosuus lukemasta lisättynä kahdella viimeisen numeron askeleella. Alueella $200\,\text{mA}$ viimeinen numero on milliampeerin kymmenesosa, joten yksi askel on $0{,}1\,\text{mA}$.
**Kaava:** $\Delta I = p \cdot I + n \cdot r$
**Muunnokset:** $p = 1{,}0\,\% = 0{,}010$; lukema ja resoluutio ovat jo milliampeereina.
**Sijoitus:** $\Delta I = 0{,}010 \cdot 146{,}3\,\text{mA} + 2 \cdot 0{,}1\,\text{mA} = 1{,}463\,\text{mA} + 0{,}2\,\text{mA} = 1{,}663\,\text{mA}$
**Vastaus:** $1{,}7\,\text{mA}$, kaksi merkitsevää numeroa, koska virherajan ensimmäinen numero on 1.
**Järkevyys:** Prosentti $146\,\text{mA}$:sta on noin $1{,}5\,\text{mA}$, ja numeroiden osuus $0{,}2\,\text{mA}$ on sitä pienempi, koska lukema on lähellä alueen ylärajaa. Tulos on vähän yli prosentin lukemasta.

## fy6-2-L1-03
**Annettu:** lukema $U = 8{,}00\,\text{V}$, virheraja $\Delta U = 0{,}06\,\text{V}$
**Kysytty:** suhteellinen virheraja $s$ prosentteina
**Periaate:** Suhteellinen virheraja kertoo, kuinka suuri osa lukemasta virheraja on. Se tekee eri suuruisten mittausten tarkkuuden vertailukelpoiseksi.
**Kaava:** $s = \dfrac{\Delta U}{U}$
**Muunnokset:** Ei tarvita: kummatkin ovat voltteina, ja yksikkö supistuu. Tulos kerrotaan sadalla, jotta se saadaan prosentteina.
**Sijoitus:** $s = \dfrac{0{,}06\,\text{V}}{8{,}00\,\text{V}} = 0{,}0075 = 0{,}75\,\%$
**Vastaus:** $0{,}8\,\%$, yksi merkitsevä numero kuten virherajassa $0{,}06\,\text{V}$.
**Järkevyys:** Prosentti $8\,\text{V}$:sta olisi $0{,}08\,\text{V}$; virheraja $0{,}06\,\text{V}$ on vähän pienempi, joten tuloksen on oltava vähän alle $1\,\%$, ja $0{,}8\,\%$ on.

## fy6-2-L1-04
**Annettu:** haaraton piiri, jossa paristo, lamppu ja vastus ovat peräkkäin; virta pariston ja lampun välissä $I = 0{,}180\,\text{A}$
**Kysytty:** virtamittarin lukema lampun ja vastuksen välissä ampeereina
**Periaate:** Haarattomassa piirissä virta on joka kohdassa sama: varausta ei katoa eikä kerry mihinkään, joten jokaisen poikkileikkauksen läpi kulkee sekunnissa yhtä paljon varausta. Lamppu muuttaa sähköenergiaa valoksi ja hehkulangan sisäenergiaksi, mutta se ei kuluta virtaa.
**Kaava:** $I_\text{jälkeen} = I_\text{ennen}$
**Muunnokset:** Ei tarvita: virta on ampeereina.
**Sijoitus:** $I_\text{jälkeen} = 0{,}180\,\text{A}$
**Vastaus:** $0{,}180\,\text{A}$, kolme merkitsevää numeroa kuten mittarin lukema.
**Järkevyys:** Jos lampun jälkeen kulkisi pienempi virta, varausta kertyisi lamppuun koko ajan lisää, eikä sellaista havaita. Simulaatiossa virtamittari näytti molemmissa kohdissa saman lukeman.

## fy6-2-L1-05
**Annettu:** lukema $U = 1{,}587\,\text{V}$ alueella $2\,\text{V}$, resoluutio $r = 0{,}001\,\text{V}$, virheraja $\pm(0{,}5\,\% + 2\ \text{numeroa})$
**Kysytty:** lukeman virheraja $\Delta U$ voltteina
**Periaate:** Valmistajan virheraja on osuus lukemasta lisättynä kahdella viimeisen numeron askeleella. Alueella $2\,\text{V}$ näytössä on kolme desimaalia, joten askel on $0{,}001\,\text{V}$.
**Kaava:** $\Delta U = p \cdot U + n \cdot r$
**Muunnokset:** $p = 0{,}5\,\% = 0{,}005$; lukema ja resoluutio ovat voltteina.
**Sijoitus:** $\Delta U = 0{,}005 \cdot 1{,}587\,\text{V} + 2 \cdot 0{,}001\,\text{V} = 0{,}007935\,\text{V} + 0{,}002\,\text{V} = 0{,}009935\,\text{V}$
**Vastaus:** $0{,}010\,\text{V}$ eli $10\,\text{mV}$: laskimen arvo $0{,}009935\,\text{V}$ pyöristyy yhteen merkitsevään numeroon $0{,}01\,\text{V}$, ja koska ensimmäinen numero on 1, virheraja ilmoitetaan kahdella numerolla.
**Järkevyys:** Puoli prosenttia $1{,}6\,\text{V}$:sta on noin $8\,\text{mV}$, ja kaksi askelta lisää $2\,\text{mV}$: yhteensä noin $10\,\text{mV}$. Alueella $20\,\text{V}$ numeroiden osuus olisi yksinään $20\,\text{mV}$, joten pieni alue on tässä selvästi tarkempi.

## fy6-2-L2-01
**Annettu:** lukema $I = 0{,}35\,\text{A}$ alueella $10\,\text{A}$, resoluutio $r = 0{,}01\,\text{A}$, virheraja $\pm(2{,}0\,\% + 3\ \text{numeroa})$
**Kysytty:** suhteellinen virheraja $\dfrac{\Delta I}{I}$ prosentteina
**Periaate:** Ensin lasketaan virheraja valmistajan ilmoituksesta: osuus lukemasta ja kolme viimeisen numeron askelta. Sitten virherajaa verrataan lukemaan. Kun lukema on pieni verrattuna alueeseen, numeroiden osuus on suuri.
**Kaava:** $\Delta I = p \cdot I + n \cdot r$, joten $\dfrac{\Delta I}{I} = \dfrac{p \cdot I + n \cdot r}{I}$
**Muunnokset:** $p = 2{,}0\,\% = 0{,}020$; kaikki virrat ovat ampeereina.
**Sijoitus:** $\Delta I = 0{,}020 \cdot 0{,}35\,\text{A} + 3 \cdot 0{,}01\,\text{A} = 0{,}007\,\text{A} + 0{,}03\,\text{A} = 0{,}037\,\text{A}$, joten $\dfrac{\Delta I}{I} = \dfrac{0{,}037\,\text{A}}{0{,}35\,\text{A}} = 0{,}106 = 10{,}6\,\%$
**Vastaus:** noin $11\,\%$, kaksi merkitsevää numeroa, koska ensimmäinen numero on 1.
**Järkevyys:** Kolme askelta eli $0{,}03\,\text{A}$ on jo lähes kymmenesosa lukemasta $0{,}35\,\text{A}$, ja prosenttiosa lisää vähän. Virta $0{,}35\,\text{A}$ ei mahdu alueelle $200\,\text{mA}$, joten $10\,\text{A}$ on tässä pienin sopiva alue; virheraja on silti lähes $11\,\%$, koska lukema on pieni alueeseen nähden, ja tarkempi suuren virran alue auttaisi.

## fy6-2-L2-02
**Annettu:** lukema $I = 0{,}0875\,\text{A}$ alueella $200\,\text{mA}$, resoluutio $r = 0{,}1\,\text{mA}$, virheraja $\pm(1{,}0\,\% + 2\ \text{numeroa})$
**Kysytty:** lukeman virheraja $\Delta I$ ampeereina
**Periaate:** Virheraja on osuus lukemasta lisättynä kahdella viimeisen numeron askeleella. Lukema ja resoluutio on ilmoitettu eri yksiköissä, joten ne muutetaan samaan yksikköön ennen yhteenlaskua.
**Kaava:** $\Delta I = p \cdot I + n \cdot r$
**Muunnokset:** $p = 1{,}0\,\% = 0{,}010$ ja $r = 0{,}1\,\text{mA} = 0{,}1 \cdot 0{,}001\,\text{A} = 0{,}0001\,\text{A}$
**Sijoitus:** $\Delta I = 0{,}010 \cdot 0{,}0875\,\text{A} + 2 \cdot 0{,}0001\,\text{A} = 0{,}000875\,\text{A} + 0{,}0002\,\text{A} = 0{,}001075\,\text{A}$
**Vastaus:** $0{,}0011\,\text{A}$ eli noin $1{,}1\,\text{mA}$, kaksi merkitsevää numeroa, koska virherajan ensimmäinen numero on 1.
**Järkevyys:** Näyttö näyttää $87{,}5\,\text{mA}$; prosentti siitä on noin $0{,}9\,\text{mA}$ ja kaksi askelta $0{,}2\,\text{mA}$, yhteensä noin $1{,}1\,\text{mA}$. Jos resoluutiota ei muuntaisi ampeereiksi, saisi järjettömän tuloksen $0{,}2\,\text{A}$, joka on suurempi kuin itse virta.

## fy6-2-L2-03
**Annettu:** alueella $2\,\text{V}$ lukema $U_2 = 1{,}234\,\text{V}$ ja resoluutio $r_2 = 0{,}001\,\text{V}$; alueella $20\,\text{V}$ lukema $U_{20} = 1{,}23\,\text{V}$ ja resoluutio $r_{20} = 0{,}01\,\text{V}$; kummallakin virheraja $\pm(0{,}5\,\% + 2\ \text{numeroa})$
**Kysytty:** virherajojen suhde $\dfrac{\Delta U_{20}}{\Delta U_2}$ paljaana lukuna
**Periaate:** Prosenttiosa on molemmilla alueilla lähes sama, koska lukema on sama. Ero syntyy numeroiden osuudesta: suuremmalla alueella viimeinen numero on kymmenen kertaa karkeampi.
**Kaava:** $\Delta U = p \cdot U + n \cdot r$, joten $\dfrac{\Delta U_{20}}{\Delta U_2} = \dfrac{p \cdot U_{20} + n \cdot r_{20}}{p \cdot U_2 + n \cdot r_2}$
**Muunnokset:** $p = 0{,}5\,\% = 0{,}005$; jännitteet ovat voltteina.
**Sijoitus:** $\Delta U_2 = 0{,}005 \cdot 1{,}234\,\text{V} + 2 \cdot 0{,}001\,\text{V} = 0{,}00817\,\text{V}$ ja $\Delta U_{20} = 0{,}005 \cdot 1{,}23\,\text{V} + 2 \cdot 0{,}01\,\text{V} = 0{,}02615\,\text{V}$, joten $\dfrac{\Delta U_{20}}{\Delta U_2} = \dfrac{0{,}02615\,\text{V}}{0{,}00817\,\text{V}} = 3{,}20$
**Vastaus:** $3{,}2$; suhde lasketaan pyöristämättömistä virherajoista, ja koska ne ovat arvioita, kaksi numeroa riittää: alueen $20\,\text{V}$ virheraja on noin kolminkertainen.
**Järkevyys:** Jos virheraja koostuisi pelkistä numeroista, suhde olisi $10$; jos pelkästä prosenttiosasta, se olisi $1$. Tulos on näiden välissä, lähempänä pientä päätä, koska prosenttiosa $0{,}006\,\text{V}$ on alueella $2\,\text{V}$ suurempi kuin numeroiden osuus $0{,}002\,\text{V}$.

## fy6-2-L2-04
**Annettu:** pariston jännite $9{,}0\,\text{V}$; jännitemittari sarjassa lampun kanssa; mittarin resistanssi on hyvin suuri lampun resistanssiin verrattuna; lamppu sammuu
**Kysytty:** jännitemittarin lukema $U_\text{m}$ voltteina
**Periaate:** Jännitemittari päästää läpi vain hyvin pienen virran, joten sarjaan kytkettynä se pienentää koko piirin virran lähes nollaan. Silloin lampun yli ei juuri jää jännitettä, koska lampun jännite on sen resistanssi kertaa lähes nolla oleva virta, ja pariston koko jännite jää mittarin napojen välille.
**Kaava:** $U_\text{m} + U_\text{lamppu} = U_\text{paristo}$ ja $U_\text{lamppu} \approx 0$, joten $U_\text{m} \approx U_\text{paristo}$
**Muunnokset:** Ei tarvita: jännite on voltteina.
**Sijoitus:** $U_\text{m} \approx 9{,}0\,\text{V}$
**Vastaus:** noin $9{,}0\,\text{V}$, kaksi merkitsevää numeroa kuten pariston jännite.
**Järkevyys:** Simulaatiossa sarjaan kytketty jännitemittari näytti pariston jännitteen $4{,}50\,\text{V}$, ja lamppu sammui. Lukema ei voi olla pariston jännitettä suurempi, ja koska virta on lähes nolla, se ei ole juuri sitä pienempikään.

## fy6-2-L3-01
**Annettu:** mittarin yli jäävä jännite $1{,}0\,\text{mV}$ milliampeeria kohti alueella $200\,\text{mA}$, mittarin lukema $I = 97{,}8\,\text{mA}$, paristojen jännite $U_0 = 4{,}5\,\text{V}$, ihanteellinen paristo
**Kysytty:** mittarin yli jäävän jännitteen osuus $\dfrac{U_\text{m}}{U_0}$ prosentteina
**Periaate:** Todellisen virtamittarin resistanssi ei ole nolla, joten mittarin yli jää pieni jännite. Käyttöohjeen mukaan se kasvaa samassa suhteessa kuin mittarin läpi kulkeva virta. Tämä jännite on poissa lampulta ja vastukselta, joten mittari pienentää piirin virtaa hieman.
**Kaava:** $U_\text{m} = k \cdot I$, missä $k = 1{,}0\,\tfrac{\text{mV}}{\text{mA}}$, joten $\dfrac{U_\text{m}}{U_0} = \dfrac{k \cdot I}{U_0}$
**Muunnokset:** $U_0 = 4{,}5\,\text{V} = 4{,}5 \cdot 1000\,\text{mV} = 4500\,\text{mV}$
**Sijoitus:** $U_\text{m} = 1{,}0\,\tfrac{\text{mV}}{\text{mA}} \cdot 97{,}8\,\text{mA} = 97{,}8\,\text{mV}$, joten $\dfrac{U_\text{m}}{U_0} = \dfrac{97{,}8\,\text{mV}}{4500\,\text{mV}} = 0{,}0217 = 2{,}17\,\%$
**Vastaus:** $2{,}2\,\%$, kaksi merkitsevää numeroa kuten jännitehäviö $1{,}0\,\text{mV}$ milliampeeria kohti ja paristojen jännite $4{,}5\,\text{V}$.
**Järkevyys:** Noin $100\,\text{mA}$ antaa noin $100\,\text{mV}$ eli $0{,}1\,\text{V}$, ja $0{,}1\,\text{V} : 4{,}5\,\text{V} \approx 0{,}022$. Mittari vie piiristä muutaman prosentin jännitteen, joten se pienentää virtaa saman verran: ilman mittaria virta olisi noin $100\,\text{mA}$, mikä sopii simulaation lukemiin $97{,}8\,\text{mA}$ ja $0{,}10\,\text{A}$.

## fy6-2-L3-02
**Annettu:** mittari A: lukema $U_\text{A} = 5{,}02\,\text{V}$, virheraja $\pm(0{,}5\,\% + 2\ \text{numeroa})$; mittari B: lukema $U_\text{B} = 5{,}14\,\text{V}$, virheraja $\pm(1{,}5\,\% + 3\ \text{numeroa})$; molemmilla resoluutio $r = 0{,}01\,\text{V}$; lukemien ero $0{,}12\,\text{V}$
**Kysytty:** virherajojen summa $\Delta U_\text{A} + \Delta U_\text{B}$ voltteina ja voidaanko eroa pitää todisteena viasta
**Periaate:** Kummankin lukeman todellinen arvo on valmistajan mukaan oman virherajansa sisällä. Lukemat ovat sopusoinnussa, jos niiden välit menevät päällekkäin eli jos ero on pienempi kuin virherajojen summa. Silloin eroa ei voi osoittaa mittareiden vikaan liittyväksi.
**Kaava:** $\Delta U = p \cdot U + n \cdot r$, joten $\Delta U_\text{A} + \Delta U_\text{B} = p_\text{A} \cdot U_\text{A} + n_\text{A} \cdot r + p_\text{B} \cdot U_\text{B} + n_\text{B} \cdot r$
**Muunnokset:** $p_\text{A} = 0{,}5\,\% = 0{,}005$ ja $p_\text{B} = 1{,}5\,\% = 0{,}015$; jännitteet ovat voltteina.
**Sijoitus:** $\Delta U_\text{A} = 0{,}005 \cdot 5{,}02\,\text{V} + 2 \cdot 0{,}01\,\text{V} = 0{,}0451\,\text{V}$ ja $\Delta U_\text{B} = 0{,}015 \cdot 5{,}14\,\text{V} + 3 \cdot 0{,}01\,\text{V} = 0{,}1071\,\text{V}$, joten $\Delta U_\text{A} + \Delta U_\text{B} = 0{,}0451\,\text{V} + 0{,}1071\,\text{V} = 0{,}1522\,\text{V}$
**Vastaus:** $0{,}15\,\text{V}$, kaksi merkitsevää numeroa, koska virherajojen summan ensimmäinen numero on 1. Lukemien ero $0{,}12\,\text{V}$ on pienempi kuin $0{,}15\,\text{V}$, joten välit $4{,}97$–$5{,}07\,\text{V}$ ja $5{,}03$–$5{,}25\,\text{V}$ menevät päällekkäin: eron perusteella kumpaakaan mittaria ei voi sanoa vialliseksi. Se ei kuitenkaan todista, että mittarit näyttäisivät aina saman.
**Järkevyys:** Halvemman mittarin virheraja on yli kaksinkertainen, kuten sen suurempi prosentti ja numeromäärä antavat odottaa. Ero $0{,}12\,\text{V}$ on noin $2\,\%$ lukemasta, mikä on samaa suuruusluokkaa kuin mittari B:n virheraja.

## fy6-2-L3-03
**Kysytty:** mitä piirissä tapahtui, miksi lamppu sammui vain hetkeksi ja näyttö jäi nollaan, ja miten lampun virta olisi pitänyt mitata
**Periaate:** Virta-alueella yleismittarin resistanssi on hyvin pieni, jotta mittari ei muuttaisi sarjaan kytkettynä piirin virtaa. Mittarin sisällä on sulake, joka palaa ja katkaisee mittarin virtatien, kun mittarin läpi kulkee liian suuri virta.
**Mallivastaus:** Opiskelija kytki virtamittarin lampun rinnalle, vaikka virtamittari kytketään sarjaan. Lampun napojen välille tuli rinnakkainen tie, jonka resistanssi on hyvin pieni, joten lähes koko virta kulki lampun ohi mittarin kautta. Lamppu sammui, koska sen läpi ei enää kulkenut virtaa. Koska tiellä paristosta mittarin kautta takaisin paristoon ei ollut juuri mitään virtaa rajoittavaa, virta kasvoi paljon suuremmaksi kuin mittausalue $200\,\text{mA}$, ja mittarin sulake paloi. Palanut sulake katkaisi virran mittarin läpi, joten mittari jäi pois piiristä: paristo ja lamppu muodostivat taas pelkän suljetun piirin, ja lamppu syttyi uudelleen. Näyttö jäi nollaan, koska mittarin läpi ei enää kulje virtaa, ennen kuin sulake vaihdetaan. Oikein mitattuna piiri avataan esimerkiksi pariston ja lampun välistä ja virtamittari asetetaan aukkoon, jolloin sama virta kulkee pariston, mittarin ja lampun läpi. Jos virran suuruutta ei tiedetä, aloitetaan alueelta $10\,\text{A}$ ja punainen johto siirretään sille kuuluvaan liittimeen.

**Itsearviointi:** Vastauksessani

- sanon, että virtamittari kytkettiin lampun rinnalle, vaikka se kuuluu kytkeä sarjaan
- selitän, että mittarin pieni resistanssi ohjasi virran lampun ohi, minkä vuoksi lamppu sammui
- selitän, että virta kasvoi niin suureksi, että mittarin sulake paloi, minkä jälkeen mittari oli poissa piiristä, lamppu syttyi uudelleen ja näyttö jäi nollaan
- kerron, että piiri avataan ja mittari asetetaan aukkoon, jotta sama virta kulkee mittarin ja lampun läpi.

## fy6-2-L1-06
**Kysytty:** miten virtamittari kytketään lampun läpi kulkevan virran mittaamiseksi.
**Periaate:** Virta on varauksen kulkua johtimen poikkileikkauksen läpi, joten virtamittarin läpi täytyy kulkea koko mitattava virta. Siksi virtamittari kytketään sarjaan: piiri avataan ja mittari asetetaan aukkoon. Virtamittarin resistanssi on hyvin pieni, joten rinnalle kytkettynä se ohjaisi virran komponentin ohi ja tekisi oikosulun.
**Mallivastaus:** Piiri avataan esimerkiksi pariston ja lampun välistä, ja virtamittari asetetaan aukkoon. Silloin sama virta kulkee pariston, mittarin ja lampun läpi, ja mittari näyttää lampun virran. Mittaria ei liitetä lampun napojen väliin, koska niin kytketään jännitemittari ja virtamittarin pieni resistanssi aiheuttaisi oikosulun. Sitä ei myöskään liitetä pariston napojen väliin eikä jätetä johdoitta lampun viereen, sillä mittari mittaa vain oman johtimensa läpi kulkevan virran.

## fy6-2-L1-07
**Kysytty:** miksi jännitemittarin resistanssin pitää olla hyvin suuri.
**Periaate:** Jännitemittari kytketään rinnalle, joten osa piirin virrasta kulkee mittarin kautta. Mittarin läpi kulkeva virta on sitä pienempi, mitä suurempi mittarin resistanssi on, ja virta pois komponentilta muuttaisi juuri sitä jännitettä, jota yritetään mitata.
**Mallivastaus:** Kun jännitemittarin resistanssi on hyvin suuri, mittarin läpi kulkee vain hyvin pieni virta. Silloin mittari ei vie virtaa mitattavalta komponentilta eikä muuta piiriä, ja lukema on lähellä jännitettä, joka komponentilla oli ennen mittaria. Suuri resistanssi ei vahvista jännitettä, ei kasvata mittarin läpi kulkevaa virtaa eikä liity johtojen kuumenemiseen. Samasta syystä virtamittarin resistanssin pitää olla päinvastoin hyvin pieni.

## fy6-2-L1-08
**Annettu:** lukema $U = 5{,}98\,\text{V}$ alueella $20\,\text{V}$, resoluutio $r = 0{,}01\,\text{V}$, virheraja $\pm(0{,}5\,\% + 2\ \text{numeroa})$
**Kysytty:** virheraja $\Delta U$ voltteina ja mittaustulos muodossa $U \pm \Delta U$
**Periaate:** Virheraja on prosenttiosuus lukemasta lisättynä kahdella viimeisen numeron askeleella. Mittaustulos ilmoitetaan lukemana ja virherajana, ja virheraja pyöristetään yhteen merkitsevään numeroon.
**Kaava:** $\Delta U = p \cdot U + n \cdot r$
**Muunnokset:** $p = 0{,}5\,\% = 0{,}005$; lukema ja resoluutio ovat jo voltteina.
**Sijoitus:** $\Delta U = 0{,}005 \cdot 5{,}98\,\text{V} + 2 \cdot 0{,}01\,\text{V} = 0{,}0299\,\text{V} + 0{,}02\,\text{V} = 0{,}0499\,\text{V}$
**Vastaus:** $\Delta U = 0{,}05\,\text{V}$, yksi merkitsevä numero, koska ensimmäinen numero on 4 (laskimen arvo $0{,}0499\,\text{V}$). Mittaustulos on $U = 5{,}98\,\text{V} \pm 0{,}05\,\text{V}$ eli väli $5{,}93$–$6{,}03\,\text{V}$. Lukema kirjoitetaan samalla desimaalien määrällä kuin virheraja.
**Järkevyys:** Virheraja $0{,}05\,\text{V}$ on alle prosentti lukemasta $5{,}98\,\text{V}$, koska lukema on noin kolmasosa alueesta $20\,\text{V}$ ($5{,}98 : 20 = 0{,}30$). Prosenttiosa $0{,}03\,\text{V}$ ja numeroiden osuus $0{,}02\,\text{V}$ ovat samaa suuruusluokkaa, joten molemmat vaikuttavat.

## fy6-2-L2-05
**Annettu:** esimerkkiaineisto: alueella $2\,\text{V}$ lukema $1{,}847\,\text{V}$ ja resoluutio $0{,}001\,\text{V}$, alueella $20\,\text{V}$ lukema $1{,}85\,\text{V}$ ja resoluutio $0{,}01\,\text{V}$, alueella $200\,\text{V}$ lukema $1{,}8\,\text{V}$ ja resoluutio $0{,}1\,\text{V}$; virheraja kaikilla alueilla $\pm(0{,}5\,\% + 2\ \text{numeroa})$
**Kysytty:** a) virheraja jokaisella alueella, b) paras alue ja perustelu; vastauslaatikkoon parhaan alueen virheraja millivoltteina
**Periaate:** Valmistajan virheraja on osuus lukemasta lisättynä kahdella viimeisen numeron askeleella. Lukema on kaikilla alueilla likimain sama, joten prosenttiosa on likimain sama ja ero syntyy numeroiden osuudesta. Mitä pienempi alue on, sitä pienempi resoluutio ja sitä pienempi virheraja on.
**Kaava:** $\Delta U = p \cdot U + n \cdot r$
**Muunnokset:** $p = 0{,}5\,\% = 0{,}005$; lukemat ja resoluutiot ovat voltteina. Tulos muutetaan lopuksi millivolteiksi: $1\,\text{V} = 1000\,\text{mV}$.
**Sijoitus:**
$\Delta U_2 = 0{,}005 \cdot 1{,}847\,\text{V} + 2 \cdot 0{,}001\,\text{V} = 0{,}009235\,\text{V} + 0{,}002\,\text{V} = 0{,}011235\,\text{V} = 11{,}235\,\text{mV}$
$\Delta U_{20} = 0{,}005 \cdot 1{,}85\,\text{V} + 2 \cdot 0{,}01\,\text{V} = 0{,}00925\,\text{V} + 0{,}02\,\text{V} = 0{,}02925\,\text{V} = 29{,}25\,\text{mV}$
$\Delta U_{200} = 0{,}005 \cdot 1{,}8\,\text{V} + 2 \cdot 0{,}1\,\text{V} = 0{,}009\,\text{V} + 0{,}2\,\text{V} = 0{,}209\,\text{V} = 209\,\text{mV}$
**Vastaus:** paras alue on $2\,\text{V}$, koska sen virheraja on pienin: $11\,\text{mV}$, kaksi merkitsevää numeroa, koska ensimmäinen numero on 1 (laskimen arvo $11{,}235\,\text{mV}$). Alueen $20\,\text{V}$ virheraja on $29\,\text{mV}$ ja alueen $200\,\text{V}$ virheraja $209\,\text{mV}$. Jännite mahtuu alueelle $2\,\text{V}$, joten pienin sopiva alue antaa tarkimman tuloksen.
**Järkevyys:** Prosenttiosa on kaikilla alueilla noin $9\,\text{mV}$, ja numeroiden osuus on $2\,\text{mV}$, $20\,\text{mV}$ ja $200\,\text{mV}$. Alueella $200\,\text{V}$ virheraja $209\,\text{mV}$ on yli $11$ prosenttia lukemasta $1{,}8\,\text{V}$, kun alueella $2\,\text{V}$ se on noin $0{,}6\,\%$.

## fy6-2-L2-06
**Kysytty:** mitä tehdään, kun virta-alueella $200\,\text{mA}$ mittarin näytössä lukee OL.
**Periaate:** OL tarkoittaa, että mitattava arvo on yli valitun mittausalueen. Se ei ole vikailmoitus eikä tarkoita nollaa. Kun suuruusluokkaa ei tiedetä, mittaus aloitetaan suurimmalta alueelta ja siirrytään pienimmälle alueelle, jolle lukema mahtuu.
**Mallivastaus:** Lampun virta on suurempi kuin $200\,\text{mA}$, joten valitaan suurempi virta-alue, virta katkaistaan tai piiri avataan, ja vasta sitten punainen johto siirretään suurille virroille tarkoitettuun liittimeen. Kun lukema saadaan, alue voidaan vaihtaa pienimmäksi alueeksi, jolle lukema mahtuu, jotta virheraja pienenee. Pienemmälle alueelle siirtyminen ei auttaisi, koska virta ylittää jo nykyisen alueen. Mittari ei ole rikki, koska OL on tavallinen ilmoitus alueen ylityksestä, eikä virta ole nolla, koska nolla näkyisi lukemana nolla.

## fy6-2-L2-07
**Annettu:** esimerkkiaineisto: lukemat $12{,}48\,\text{V}$, $12{,}52\,\text{V}$, $12{,}46\,\text{V}$, $12{,}50\,\text{V}$ ja $12{,}49\,\text{V}$ alueella $20\,\text{V}$, resoluutio $r = 0{,}01\,\text{V}$, virheraja $\pm(0{,}5\,\% + 2\ \text{numeroa})$, täyteen ladatun akun lepojännite $12{,}60\,\text{V}$
**Kysytty:** a) keskiarvo, b) hajonnan arvio puoleksi vaihteluvälistä, c) mittarin virheraja keskiarvolle, d) sopusointu lepojännitteen kanssa; vastauslaatikkoon c)-kohdan virheraja voltteina
**Periaate:** Toistomittaus kertoo, kuinka paljon lukemat hajoavat. Puolet vaihteluvälistä on yksinkertainen arvio hajonnasta, ei keskiarvon epävarmuus. Mittarin virheraja ei pienene toistamalla, koska se kuuluu mittariin. Tulos on sopusoinnussa vertailuarvon kanssa, jos arvojen ero on pienempi kuin virheraja.
**Kaava:** $U_\text{ka} = \dfrac{\text{lukemien summa}}{N}$, hajonnan arvio $\dfrac{U_\text{max} - U_\text{min}}{2}$ ja virheraja $\Delta U = p \cdot U_\text{ka} + n \cdot r$
**Muunnokset:** $p = 0{,}5\,\% = 0{,}005$; kaikki jännitteet ovat voltteina.
**Sijoitus:** a) Lukemien summa on $62{,}45\,\text{V}$ ja lukemia on $N = 5$, joten $U_\text{ka} = 62{,}45\,\text{V} : 5 = 12{,}49\,\text{V}$. b) Hajonnan arvio on $(12{,}52\,\text{V} - 12{,}46\,\text{V}) : 2 = 0{,}03\,\text{V}$. c) $\Delta U = 0{,}005 \cdot 12{,}49\,\text{V} + 2 \cdot 0{,}01\,\text{V} = 0{,}06245\,\text{V} + 0{,}02\,\text{V} = 0{,}08245\,\text{V}$
**Vastaus:** c)-kohdan virheraja on $0{,}08\,\text{V}$, yksi merkitsevä numero, koska ensimmäinen numero on 8 (laskimen arvo $0{,}08245\,\text{V}$). Keskiarvo on $12{,}49\,\text{V}$ ja hajonnan arvio $0{,}03\,\text{V}$. Lepojännitteen ja keskiarvon ero on $12{,}60\,\text{V} - 12{,}49\,\text{V} = 0{,}11\,\text{V}$, joka on suurempi kuin virheraja $0{,}08\,\text{V}$. Tulos $12{,}49\,\text{V} \pm 0{,}08\,\text{V}$ ei ole sopusoinnussa täyteen ladatun akun lepojännitteen kanssa: akku on todennäköisesti osittain purkautunut. Toistaminen ei auttaisi, koska hajonta $0{,}03\,\text{V}$ on jo pieni ja virheraja kuuluu mittariin.
**Järkevyys:** Tulosväli $12{,}41$–$12{,}57\,\text{V}$ ei sisällä arvoa $12{,}60\,\text{V}$, mutta se on lähellä, joten akku on vain vähän vajaa. Virheraja $0{,}08\,\text{V}$ on lähes kolminkertainen hajonnan arvioon $0{,}03\,\text{V}$ nähden, joten mittarin oma virheraja hallitsee tulosta eikä lukemien toistaminen pienennä sitä.

## fy6-2-L3-04
**Annettu:** esimerkkitilanne: jännitelähde $U_0 = 12{,}0\,\text{V}$ (ihanteellinen), vastukset $R_1 = R_2 = 1{,}0\,\text{M}\Omega$ peräkkäin, mittarin resistanssi $R_\text{m} = 10\,\text{M}\Omega$ vastuksen $R_2$ rinnalla; mittarin alueen $20\,\text{V}$ virheraja $\pm(0{,}5\,\% + 2\ \text{numeroa})$, resoluutio $0{,}01\,\text{V}$
**Kysytty:** a) $R_2$:n jännite ilman mittaria, b) mittarin näyttämä jännite $U$, c) mittarin aiheuttama jännitteen pieneneminen prosentteina (vastauslaatikkoon), d) vertailu virherajaan ja luotettavampi mittaus
**Periaate:** Mittari on vastuksen $R_2$ rinnalla, joten ne ovat samassa jännitteessä $U$ ja mittarin läpi kulkeva virta on pois piirin muusta virrasta. Vastuksen $R_1$ läpi kulkeva virta on vastuksen $R_2$ ja mittarin virtojen summa. Jännitteet ovat samassa silmukassa: $U_1 + U = U_0$. Virta saadaan vastuksen jännitteestä ja resistanssista: $I = U : R$.
**Kaava:** $\dfrac{U_0 - U}{R_1} = \dfrac{U}{R_2} + \dfrac{U}{R_\text{m}}$, josta $U = \dfrac{U_0}{1 + \dfrac{R_1}{R_2} + \dfrac{R_1}{R_\text{m}}}$; pieneneminen $\dfrac{U_\text{ilman} - U}{U_\text{ilman}}$
**Muunnokset:** Vastusten suhteet ovat paljaita lukuja, joten megaohmeja ei tarvitse muuntaa: $\dfrac{R_1}{R_2} = 1{,}0$ ja $\dfrac{R_1}{R_\text{m}} = \dfrac{1{,}0\,\text{M}\Omega}{10\,\text{M}\Omega} = 0{,}10$.
**Sijoitus:** a) Ilman mittaria vastuksilla on sama virta ja sama resistanssi, joten jännite jakautuu tasan: $U_\text{ilman} = 12{,}0\,\text{V} : 2 = 6{,}00\,\text{V}$. b) Kerrotaan yhtälö $\dfrac{U_0 - U}{R_1} = \dfrac{U}{R_2} + \dfrac{U}{R_\text{m}}$ puolittain resistanssilla $R_1$: $U_0 - U = U \cdot \dfrac{R_1}{R_2} + U \cdot \dfrac{R_1}{R_\text{m}}$. Siirretään $U$ samalle puolelle: $U_0 = U \left(1 + \dfrac{R_1}{R_2} + \dfrac{R_1}{R_\text{m}}\right)$, ja jaetaan sulkeella. Silloin $U = \dfrac{12{,}0\,\text{V}}{1 + 1{,}0 + 0{,}10} = \dfrac{12{,}0\,\text{V}}{2{,}10} = 5{,}714\,\text{V}$. c) Pieneneminen on $6{,}00\,\text{V} - 5{,}714\,\text{V} = 0{,}286\,\text{V}$, joten $\dfrac{0{,}286\,\text{V}}{6{,}00\,\text{V}} = 0{,}0476 = 4{,}76\,\%$. d) Lukemalle $5{,}71\,\text{V}$ mittarin virheraja on $\Delta U = 0{,}005 \cdot 5{,}71\,\text{V} + 2 \cdot 0{,}01\,\text{V} = 0{,}0486\,\text{V}$.
**Vastaus:** c)-kohdan tulos on $4{,}8\,\%$, kaksi merkitsevää numeroa kuten annetut resistanssit (laskimen arvo $4{,}76\,\%$). Ilman mittaria jännite on $6{,}00\,\text{V}$ ja mittarin näyttämä jännite $5{,}71\,\text{V}$. Mittarin aiheuttama muutos $0{,}286\,\text{V}$ on noin $5{,}9$-kertainen virherajaan $0{,}0486\,\text{V}$ verrattuna. Virheraja kertoo vain mittarin sisäisen epätarkkuuden, ei mittarin vaikutusta piiriin, joten mittaustulos $5{,}71\,\text{V} \pm 0{,}05\,\text{V}$ ei ole luotettava: jännite ilman mittaria, $6{,}00\,\text{V}$, jää sen ulkopuolelle. Mittaus on luotettavampi, kun mittarin resistanssi on paljon suurempi kuin mitattavan komponentin tai kun vastukset ovat pienempiä. Jos vastukset olisivat $R_1 = R_2 = 10\,\text{k}\Omega$, mittarin vaikutus olisi vain $0{,}05\,\%$.
**Järkevyys:** Takaisinsijoitus: vastuksen $R_1$ läpi kulkee virta $(12{,}0 - 5{,}714)\,\text{V} : 1{,}0\,\text{M}\Omega = 6{,}29\,\mu\text{A}$, ja se on vastuksen $R_2$ virran ja mittarin virran summa: $5{,}714\,\mu\text{A} + 0{,}571\,\mu\text{A} = 6{,}29\,\mu\text{A}$. Mittari vie vastuksen $R_2$ virrasta lähes kymmenesosan, joten jännite pienenee noin $5\,\%$, mikä sopii tulokseen $4{,}8\,\%$. Pienempien vastusten tapauksessa $U = 12{,}0\,\text{V} : 2{,}001 = 5{,}997\,\text{V}$, mikä on lähes $6{,}00\,\text{V}$.

## fy6-2-L3-05
**Annettu:** esimerkkiaineisto: jännitemittarin resistanssi $10\,\text{M}\Omega$, jännite $U = 4{,}52\,\text{V}$ alueella $20\,\text{V}$ ($r = 0{,}01\,\text{V}$, virheraja $\pm(0{,}5\,\% + 2\ \text{numeroa})$), virta $I = 38{,}4\,\text{mA}$ alueella $200\,\text{mA}$ ($r = 0{,}1\,\text{mA}$, virheraja $\pm(1{,}0\,\% + 2\ \text{numeroa})$); opiskelijan väite: $R = 117{,}71\,\Omega$, joten vastus ei ole $120\,\Omega$ vaan viallinen
**Kysytty:** a) $R = U : I$, b) suhteelliset virherajat, c) resistanssin virheraja $\Delta R$ ohmeina (vastauslaatikkoon), d) päätelmän arviointi ja oikea tulos
**Periaate:** Resistanssi lasketaan mittaustuloksista osamääränä $R = U : I$, ja sen virheraja saadaan osamäärän sääntöstä: suhteellinen virheraja on jännitteen ja virran suhteellisten virherajojen summa. Tulos on sopusoinnussa nimellisarvon kanssa, jos nimellisarvo mahtuu tulosväliin. Pelkkä ero lasketusta arvosta ei osoita vikaa.
**Kaava:** $R = \dfrac{U}{I}$, $\Delta U = p_U \cdot U + n_U \cdot r_U$, $\Delta I = p_I \cdot I + n_I \cdot r_I$ ja $\dfrac{\Delta R}{R} = \dfrac{\Delta U}{U} + \dfrac{\Delta I}{I}$
**Muunnokset:** $p_U = 0{,}5\,\% = 0{,}005$ ja $p_I = 1{,}0\,\% = 0{,}010$; virta muutetaan ampeereiksi: $I = 38{,}4\,\text{mA} = 0{,}0384\,\text{A}$.
**Sijoitus:** a) $R = \dfrac{4{,}52\,\text{V}}{0{,}0384\,\text{A}} = 117{,}71\,\Omega$. b) $\Delta U = 0{,}005 \cdot 4{,}52\,\text{V} + 2 \cdot 0{,}01\,\text{V} = 0{,}0426\,\text{V}$, joten $\dfrac{\Delta U}{U} = \dfrac{0{,}0426\,\text{V}}{4{,}52\,\text{V}} = 0{,}00942 = 0{,}94\,\%$. Lisäksi $\Delta I = 0{,}010 \cdot 38{,}4\,\text{mA} + 2 \cdot 0{,}1\,\text{mA} = 0{,}584\,\text{mA}$, joten $\dfrac{\Delta I}{I} = \dfrac{0{,}584\,\text{mA}}{38{,}4\,\text{mA}} = 0{,}0152 = 1{,}5\,\%$. c) Suhteellinen virheraja on $0{,}00942 + 0{,}0152 = 0{,}0246 = 2{,}5\,\%$, joten $\Delta R = 0{,}0246 \cdot 117{,}71\,\Omega = 2{,}90\,\Omega$.
**Vastaus:** c)-kohdan virheraja on $\Delta R = 3\,\Omega$, yksi merkitsevä numero (laskimen arvo $2{,}90\,\Omega$). Mittaustulos on $R = 118\,\Omega \pm 3\,\Omega$ eli väli $115$–$121\,\Omega$, ja nimellisarvo $120\,\Omega$ mahtuu tähän väliin. Opiskelijan päätelmä on väärä: ero nimellisarvoon on $2{,}3\,\Omega$, mikä on pienempi kuin virheraja, joten mittaus ei osoita vastusta vialliseksi. Raportissa pitää antaa tulos virherajoineen ja pyöristää tulos virherajan mukaan, eikä kirjoittaa neljää merkitsevää numeroa ilman virherajaa. Jännitemittarin virta on $4{,}52\,\text{V} : 10\,\text{M}\Omega = 0{,}45\,\mu\text{A}$, mikä on vain $0{,}001\,\%$ virrasta $38{,}4\,\text{mA}$, joten sen voi jättää huomiotta (suuri mittarin resistanssi verrattuna vastukseen $118\,\Omega$).
**Järkevyys:** Jännitteen ja virran suhteelliset virherajat ovat noin yksi ja puolitoista prosenttia, joten niiden summa on noin kaksi ja puoli prosenttia, ja $2{,}5\,\%$ luvusta $118\,\Omega$ on noin $3\,\Omega$. Nimellisarvo $120\,\Omega$ poikkeaa mittaustuloksesta noin $2\,\%$ ($2{,}29\,\Omega : 117{,}71\,\Omega = 1{,}95\,\%$), mikä on pienempi kuin $2{,}5\,\%$.
