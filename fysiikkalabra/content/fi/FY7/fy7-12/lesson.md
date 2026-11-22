# Kokonais­heijastuminen ja valokuitu

> **Miksi** valo kulkee lasikuidussa Itämeren pohjaa pitkin Helsingistä Saksaan pääsemättä välillä ulos, vaikka lasi on läpinäkyvää?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: meren poikkileikkaus. Vasemmalla ja oikealla rannalla on kaupungit, ja meren pohjassa kulkee merikaapeli rannalta toiselle. Keskellä suurennuslasin kaltaisessa ympyrässä näkyy kaapelin sisällä oleva lasikuitu, jonka ytimessä valonsäde etenee siksakkia heijastuen kuidun reunoilta." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-12-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Valo optisesti harvempaan aineeseen
Luvussa *Valon heijastuminen ja taittuminen* nähtiin, että valo taittuu kahden aineen rajapinnassa taittumislain $n_1 \sin\alpha_1 = n_2 \sin\alpha_2$ mukaan ja että osa valosta heijastuu. Kun valo tulee suuremman taitekertoimen aineesta pienemmän taitekertoimen aineeseen, esimerkiksi vedestä ilmaan, se taittuu normaalista poispäin: taitekulma on suurempi kuin tulokulma. Vedestä $30^\circ$:n tulokulmassa tuleva säde jatkaa ilmassa $41{,}7^\circ$:n kulmassa normaaliin nähden. Kun tulokulmaa kasvatetaan, taitekulma kasvaa vielä nopeammin ja lähestyy $90^\circ$:ta. Samalla heijastuvan valon osuus kasvaa.

### Rajakulma ja kokonaisheijastuminen
Tulokulmaa, jolla taitekulma on $90^\circ$, sanotaan **rajakulmaksi** $\alpha_\text{r}$. Rajakulmassa taittunut säde kulkee pitkin rajapintaa. Kun tulokulma on suurempi kuin rajakulma, taittumislaista ei saada taitekulmaa, koska sen sinin pitäisi olla suurempi kuin yksi. Silloin toiseen aineeseen ei synny etenevää taittunutta valonsädettä, vaan valo heijastuu takaisin heijastumislain mukaan. Tämä on **kokonaisheijastuminen**. Ideaalisessa, häviöttömässä rajapinnassa koko tuleva valoteho heijastuu takaisin, eikä energiaa siirry toiseen aineeseen. Rajapinnan läheisyyteen syntyy kuitenkin hyvin nopeasti vaimeneva sähkömagneettinen kenttä.

Veden ja ilman rajapinnassa rajakulma on $48{,}8^\circ$. Siksi sukeltaja näkee vedenpinnan vinosti alhaalta katsottuna peilinä, josta näkyy pohja.

<svg data-fig="water" viewBox="0 0 600 360" role="img" aria-label="Periaatekuva: veden pohjalla oleva lamppu lähettää kolme valonsädettä vedenpintaan eri tulokulmissa. Jokaiseen osumakohtaan on piirretty pinnan normaali katkoviivana. Vasemmalla tulokulma 30 astetta on pienempi kuin rajakulma: säde taittuu ilmaan normaalista poispäin, ja heikko osa heijastuu takaisin veteen. Keskellä tulokulma on rajakulma 48,8 astetta: taittunut säde kulkee pitkin pintaa. Oikealla tulokulma 65 astetta on suurempi kuin rajakulma: ilmaan ei pääse valoa, vaan koko säde heijastuu takaisin veteen, eli tapahtuu kokonaisheijastuminen." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-12-water.webp" x="0" y="0" width="600" height="367.5" preserveAspectRatio="none"/>
  <foreignObject x="87" y="21.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha < \alpha_\text{r}$</div></foreignObject>
  <foreignObject x="216.5" y="21.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha = \alpha_\text{r}$</div></foreignObject>
  <foreignObject x="361" y="21.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha > \alpha_\text{r}$</div></foreignObject>
  <foreignObject x="526" y="85.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{ilma}$</div></foreignObject>
  <foreignObject x="297" y="231.5" width="270" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#ffffff">$\text{kokonaisheijastuminen}$</div></foreignObject>
  <foreignObject x="418" y="291.5" width="149" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#ffffff">$\text{vesi},\ n = 1{,}33$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/tir-wine-glass.webp" alt="Käsi pitää viinilasia jalasta mustaa taustaa vasten; vihreä lasersäde tulee alhaalta ja kulkee mutkitellen lasin jalassa ja pohjassa."><figcaption>Vihreä lasersäde viinilasin jalassa. Säde osuu lasin pintaan rajakulmaa suuremmassa kulmassa, joten se kokonaisheijastuu takaisin lasiin eikä pääse ilmaan.</figcaption></figure>

```pysahdy
Valo tulee vedestä ilmaan $70^\circ$:n tulokulmalla. Veden ja ilman rajakulma on $48{,}8^\circ$. Pääseekö osa valosta ilmaan?
---
Ei pääse. Tulokulma $70^\circ$ on suurempi kuin rajakulma $48{,}8^\circ$, joten valo kokonaisheijastuu takaisin veteen.
```

### Vain suuremmasta taitekertoimesta pienempään
Kokonaisheijastuminen voi tapahtua vain, kun valo tulee suuremman taitekertoimen aineesta pienemmän taitekertoimen aineeseen. Kun valo tulee ilmasta veteen tai lasiin, se taittuu normaalia kohti, ja taittunut säde on olemassa jokaisella tulokulmalla. Silloin osa valosta pääsee aina toiseen aineeseen, vaikka heijastuva osuus kasvaa suurilla tulokulmilla. Kokonaisheijastumisessa valoa ei katoa: sileästä rajapinnasta heijastunut säde vie mukanaan koko tulevan säteen tehon, kun aine ei absorboi valoa. Siksi kokonaisheijastuminen on parempi peili kuin metallipinta, joka absorboi osan valosta.

### Valokuitu
**Valokuitu** on hiuksen paksuinen lasikuitu, jonka keskellä on ydin ja sen ympärillä kuori. Ytimen taitekerroin on hieman suurempi kuin kuoren, esimerkiksi $1{,}48$ ja $1{,}46$. Kuidun päähän lähes akselin suuntaisesti tuleva valo osuu ytimen ja kuoren rajapintaan hyvin loivasti eli suurella tulokulmalla, joka on suurempi kuin rajakulma. Valo kokonaisheijastuu joka kerta takaisin ytimeen ja etenee kuitua pitkin siksakkia myös silloin, kun kuitu kaartuu loivasti. Jos valo tulee kuidun päähän liian jyrkässä kulmassa, se osuu rajapintaan rajakulmaa pienemmällä tulokulmalla, ja jokaisessa osumassa osa siitä taittuu kuoreen ja katoaa ytimestä. Jyrkkä mutka pienentää tulokulmaa samalla tavalla, joten kuitua ei saa taittaa terävälle mutkalle.

<svg data-fig="fibre" viewBox="0 0 600 340" role="img" aria-label="Periaatekuva valokuidusta, ei mittakaavassa. Ylhäällä kuitu pituussuunnassa leikattuna: keskellä ydin, jonka taitekerroin on n1, sen ympärillä kuori, jonka taitekerroin n2 on vähän pienempi, ja uloimpana muovinen suojapäällyste. Valonsäde etenee ytimessä siksakkia: se osuu ytimen ja kuoren rajapintaan tulokulmassa, joka on suurempi kuin rajakulma, ja kokonaisheijastuu joka kerta takaisin ytimeen. Alhaalla oikealla sama kuitu poikkileikkauksena: ydin, kuori ja päällyste sisäkkäisinä ympyröinä." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-12-fibre.webp" x="-2.5" y="0" width="603" height="353" preserveAspectRatio="none"/>
  <foreignObject x="333.5" y="63.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="422.5" y="63.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\alpha > \alpha_\text{r}$</div></foreignObject>
  <foreignObject x="132" y="147.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kuori}\ n_2$</div></foreignObject>
  <foreignObject x="60" y="247.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ydin}\ n_1$</div></foreignObject>
  <foreignObject x="210" y="291.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{suojapäällyste}$</div></foreignObject>
  <foreignObject x="330" y="255.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$n_1 > n_2$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/optical-fibres.webp" alt="Kiepille kierretty läpikuultava valokaapeli mustalla pohjalla; kaapelin kummassakin päässä on liitin, josta loistaa punaista valoa."><figcaption>Muovisen valokaapelin toiseen päähän johdettu punainen valo tulee ulos toisesta päästä. Kokonaisheijastumisen ansiosta valo seuraa kuitua kiepin ympäri.</figcaption></figure>

```pysahdy
Mitä jos kuidun ytimen ja kuoren taitekertoimet ovat yhtä suuret, $n_1 = n_2$? Voisiko valo silti kokonaisheijastua ytimen ja kuoren rajapinnassa?
---
Ei voisi. Silloin $\sin\alpha_\text{r} = n_2 : n_1 = 1$ ja rajakulma olisi $90^\circ$. Tulokulma ei voi olla näin suuri, joten valo ei kokonaisheijastuisi vaan etenisi kuoreen ja vuotaisi ulos kuidusta.
```

### Miksi kuidussa on kuori
Paljas lasisauva pitää valon sisällään ilmassakin, ja vieläpä jyrkemmin tulevan valon, koska lasin ja ilman taitekertoimien ero on suuri ja rajakulma siksi pieni. Lasin pintaan tarttuva vesi, rasva tai toinen kuitu kuitenkin muuttaa rajapintaa, ja kosketuskohdasta valoa vuotaa ulos. Kuori pitää heijastavan rajapinnan puhtaana kuidun sisällä, ja muovinen suojapäällyste suojaa lasia naarmuilta. Kun ytimen ja kuoren taitekertoimien ero on pieni, kuidussa pysyvät vain lähes akselin suuntaiset säteet. Niiden kulkumatkat ovat lähes yhtä pitkät, joten lyhyet valopulssit venyvät matkalla vain vähän.

### Tietoa valopulsseina
Tietoliikenteessä tieto kulkee kuidussa lyhyinä valopulsseina. Valona käytetään yleensä infrapunavaloa, jonka aallonpituus on noin $1550\,\text{nm}$, koska kuidun kvartsilasi vaimentaa sitä vähiten. Valon teho pienenee kuidussa puoleen vasta noin $15\,\text{km}$:n matkalla, joten pitkillä yhteyksillä pulssit vahvistetaan vain noin $50$–$100\,\text{km}$:n välein. Esimerkiksi Cinian merikaapeli C-Lion1 kulkee Itämeren pohjassa Helsingistä Saksan Rostockiin, ja sen pituus on $1172\,\text{km}$ (Cinia, 2016). Valo etenee lasissa hitaammin kuin tyhjiössä, joten kuitu viivästyttää signaalia hieman enemmän kuin pelkkä matka antaisi odottaa.

### Tähystin
Perinteisessä kuitutähystimessä eli kuituendoskoopissa on kaksi kuitukimppua. Toinen tuo valaistusvalon kehon sisään, ja toinen välittää kuvan takaisin. Kuvakimpun tuhannet kuidut ovat kimpun kummassakin päässä samassa järjestyksessä, ja kukin kuitu kuljettaa yhden kuvapisteen valon. Kimppu taipuu, joten sillä nähdään mutkan taakse esimerkiksi mahalaukkuun. Nykyaikaisissa videotähystimissä kuva voidaan muodostaa myös laitteen kärjessä olevalla kamerakennolla, ja kuidut tuovat silloin vain valaistuksen.

### Timantin säihke
Timantin taitekerroin on $2{,}42$, joten sen rajakulma ilmaa vasten on vain $24{,}4^\circ$. Hiotun timantin alaviistopinnat on kallistettu niin, että yläpinnasta tuleva valo osuu niihin rajakulmaa suuremmalla tulokulmalla. Valo kokonaisheijastuu ja palaa ylöspäin katsojaa kohti. Samanmuotoisessa lasikivessä rajakulma on $41{,}8^\circ$, joten osa samasta valosta taittuu ulos kiven alapuolelta, ja lasi säihkyy vähemmän.

<svg data-fig="diamond" viewBox="0 0 600 310" role="img" aria-label="Periaatekuva, ei mittakaavassa: kaksi samanmuotoista hiottua kiveä poikkileikkauksena. Kummankin kiven yläpinnasta tulee pystysuoraan alas sama valonsäde, joka osuu alaviistopintaan 38 asteen tulokulmassa. Vasemmalla timantissa, jonka taitekerroin on 2,42 ja rajakulma 24,4 astetta, säde kokonaisheijastuu kahdesti ja palaa ylöspäin ulos kiven yläosasta. Oikealla lasissa, jonka taitekerroin on 1,50 ja rajakulma 41,8 astetta, tulokulma on pienempi kuin rajakulma: suurin osa valosta taittuu ulos kiven alapuolelta, ja vain heikko osa heijastuu." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-12-diamond.webp" x="13.2" y="1.2" width="576.9" height="308.9" preserveAspectRatio="none"/>
  <foreignObject x="137" y="118.5" width="50" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$38^\circ$</div></foreignObject>
  <foreignObject x="25" y="265.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{timantti},\ \alpha_\text{r} = 24{,}4^\circ$</div></foreignObject>
  <foreignObject x="426" y="118.5" width="50" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$38^\circ$</div></foreignObject>
  <foreignObject x="325" y="265.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lasi},\ \alpha_\text{r} = 41{,}8^\circ$</div></foreignObject>
</svg>

## Kaava: Rajakulma
Rajakulmassa taitekulma on $90^\circ$, ja $\sin 90^\circ = 1$. Kun taittumislakiin sijoitetaan tulokulmaksi rajakulma ja taitekulmaksi $90^\circ$, saadaan rajakulmalle
```latex
\begin{aligned}
&n_1 \sin\alpha_\text{r} = n_2 \sin 90^\circ \\[6pt]
&\sin\alpha_\text{r} = \frac{n_2}{n_1}
\end{aligned}
```
missä $\alpha_\text{r}$ on rajakulma rajapinnan normaalista mitattuna, $n_1$ sen aineen taitekerroin, josta valo tulee, ja $n_2$ sen aineen taitekerroin, johon valo on menossa. Rajakulma on olemassa vain, kun $n_1 > n_2$: muuten $n_2 : n_1 \ge 1$. Kun tulokulma on suurempi kuin rajakulma, valo kokonaisheijastuu. Mitä suurempi taitekertoimien ero on, sitä pienempi on rajakulma, kuten kuvaajasta näkyy.

<svg data-fig="graph" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja mittakaavassa: rajakulma asteina aineen taitekertoimen n1 funktiona, kun toinen aine on ilmaa, jonka taitekerroin on 1,00. Käyrä laskee 90 asteesta, kun n1 on 1,00, ensin jyrkästi ja sitten loivemmin. Merkityt pisteet: vesi, n1 = 1,33, rajakulma 48,8 astetta; lasi, n1 = 1,50, 41,8 astetta; timantti, n1 = 2,42, 24,4 astetta." style="max-width:100%;font-size:24px">
  <line x1="149" y1="290" x2="149" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="202" y1="290" x2="202" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="255" y1="290" x2="255" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="308" y1="290" x2="308" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="361" y1="290" x2="361" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="414" y1="290" x2="414" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="467" y1="290" x2="467" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="520" y1="290" x2="520" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="254.5" x2="520" y2="254.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="218.5" x2="520" y2="218.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="183" x2="520" y2="183" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="147.5" x2="520" y2="147.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="111.5" x2="520" y2="111.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="76" x2="520" y2="76" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="290" x2="534" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M546,290 L533,296 L533,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="291" x2="96" y2="62" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,50 L102,63 L90,63 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="149" y1="290" x2="149" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="126.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}2$</div></foreignObject>
  <line x1="202" y1="290" x2="202" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="255" y1="290" x2="255" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="232.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}6$</div></foreignObject>
  <line x1="308" y1="290" x2="308" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="361" y1="290" x2="361" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="338.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}0$</div></foreignObject>
  <line x1="414" y1="290" x2="414" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="467" y1="290" x2="467" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="444.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2{,}4$</div></foreignObject>
  <line x1="520" y1="290" x2="520" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="254.5" x2="96" y2="254.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="218.5" x2="96" y2="218.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="204" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="89" y1="183" x2="96" y2="183" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="147.5" x2="96" y2="147.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="133" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="89" y1="111.5" x2="96" y2="111.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="76" x2="96" y2="76" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="51" y="61.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$90$</div></foreignObject>
  <foreignObject x="552" y="275.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$n_1$</div></foreignObject>
  <foreignObject x="86" y="19.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\alpha_\text{r}\ (^\circ)$</div></foreignObject>
  <foreignObject x="73.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1{,}0$</div></foreignObject>
  <foreignObject x="64" y="267.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <polyline points="96,76 99.5,98 103,107 106.5,114 110,119.5 113.5,124.5 117,129 120.5,132.5 124.5,136.5 128,139.5 131.5,143 135,145.5 138.5,148.5 142,151 145.5,153.5 149,156 152.5,158 156,160 159.5,162 163,164 166.5,166 170,168 173.5,169.5 177.5,171.5 181,173 184.5,174.5 188,176 191.5,177.5 195,179 198.5,180.5 202,181.5 205.5,183 209,184 212.5,185.5 216,186.5 219.5,188 223,189 226.5,190 230.5,191 234,192 237.5,193 241,194 244.5,195 248,196 251.5,197 255,198 258.5,199 262,200 265.5,200.5 269,201.5 272.5,202.5 276,203 279.5,204 283.5,204.5 287,205.5 290.5,206 294,207 297.5,207.5 301,208.5 304.5,209 308,210 311.5,210.5 315,211 318.5,211.5 322,212.5 325.5,213 329,213.5 332.5,214 336.5,215 340,215.5 343.5,216 347,216.5 350.5,217 354,217.5 357.5,218 361,218.5 364.5,219 368,219.5 371.5,220 375,220.5 378.5,221 382,221.5 385.5,222 389.5,222.5 393,223 396.5,223.5 400,224 403.5,224.5 407,225 410.5,225.5 414,225.5 417.5,226 421,226.5 424.5,227 428,227.5 431.5,228 435,228 438.5,228.5 442.5,229 446,229.5 449.5,229.5 453,230 456.5,230.5 460,230.5 463.5,231 467,231.5 470.5,232 474,232 477.5,232.5 481,233 484.5,233 488,233.5 491.5,234 495.5,234 499,234.5 502.5,234.5 506,235 509.5,235.5 513,235.5 516.5,236 520,236" fill="none" stroke="#e64980" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="183.5" cy="174" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="113.5" y="185.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{vesi}$</span></div></foreignObject>
  <circle cx="228.5" cy="190.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="240.5" y="154" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{lasi}$</span></div></foreignObject>
  <circle cx="472.5" cy="232" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="418.5" y="181.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{timantti}$</span></div></foreignObject>
  <foreignObject x="320" y="97.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$n_2 = 1{,}00\ (\text{ilma})$</span></div></foreignObject>
</svg>

```pysahdy
Aineen taitekerroin on $2{,}00$. Mikä on rajakulma tämän aineen ja ilman rajapinnassa?
---
Ilman taitekerroin on $1{,}00$, joten $\sin\alpha_\text{r} = 1{,}00 : 2{,}00 = 0{,}500$. Siis $\alpha_\text{r} = 30{,}0^\circ$.
```

### Valon kulkuaika kuidussa
Aineessa, jonka taitekerroin on $n$, valo etenee nopeudella $v = c : n$ (luku *Valon heijastuminen ja taittuminen*). Matkaan $s$ kuluu siksi aika
```latex
t = \frac{s}{v} = \frac{n s}{c}
```
missä $c = 3{,}00 \cdot 10^8\,\text{m/s}$ on valon nopeus tyhjiössä. Kuidun lasissa $n \approx 1{,}47$, joten valo etenee nopeudella noin $2{,}04 \cdot 10^8\,\text{m/s}$ eli noin kahdella kolmasosalla tyhjiön valonnopeudesta. Kaava antaa kuidun akselin suuntaisen säteen kulkuajan. Siksakkia etenevä säde kulkee hieman pidemmän matkan ja tulee perille hieman myöhemmin.

## Esimerkki
Valokuidun ytimen taitekerroin on $1{,}48$ ja kuoren $1{,}46$. Kuinka suuri on rajakulma ytimen ja kuoren rajapinnassa? Ytimessä etenevä säde osuu rajapintaan $83^\circ$:n tulokulmassa. Pysyykö se ytimessä?

<!-- vaihe -->

**Tunnetut ja kysytty.** Ytimen taitekerroin $n_1 = 1{,}48$, kuoren taitekerroin $n_2 = 1{,}46$ ja säteen tulokulma $\alpha = 83^\circ$.

Kysytään rajakulmaa $\alpha_\text{r}$ ja sitä, kokonaisheijastuuko säde.

<!-- vaihe -->

**Periaate.** Valo tulee ytimestä kuoreen eli suuremman taitekertoimen aineesta pienemmän, joten rajakulma on olemassa. Rajakulmassa taitekulma olisi $90^\circ$, joten rajakulman sini saadaan taittumislaista. Jos tulokulma on suurempi kuin rajakulma, säde kokonaisheijastuu.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&n_1 \sin\alpha_\text{r} = n_2 \sin 90^\circ \\[6pt]
&\sin\alpha_\text{r} = \frac{n_2}{n_1} \\[6pt]
&\alpha_\text{r} = \sin^{-1}\frac{n_2}{n_1}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: taitekertoimet ovat yksiköttömiä lukuja, ja kulma saadaan asteina.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&\sin\alpha_\text{r} = \frac{1{,}46}{1{,}48} \\
&= 0{,}9865 \\[6pt]
&\alpha_\text{r} = \sin^{-1} 0{,}9865 \\
&= 80{,}57^\circ
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Rajakulma on $\alpha_\text{r} \approx 80{,}6^\circ$, kolmella merkitsevällä numerolla kuten taitekertoimet. Tulokulma $83^\circ$ on suurempi kuin rajakulma, joten säde kokonaisheijastuu ja pysyy ytimessä.

<!-- vaihe -->

**Järkevyys.** Taitekertoimet ovat lähes yhtä suuret, joten säde taittuu kuoreen vain vähän ja rajakulman pitää olla lähellä $90^\circ$:ta, kuten tuloksessa. Lasin ja ilman rajapinnassa ero on paljon suurempi, ja rajakulma on vain noin $42^\circ$. Tarkistus: $1{,}48 \cdot \sin 80{,}57^\circ = 1{,}48 \cdot 0{,}9865 = 1{,}46$.

## Yleinen virhekäsitys
Moni ajattelee, että valo voi kokonaisheijastua mistä tahansa rajapinnasta, kunhan tulokulma on tarpeeksi suuri, esimerkiksi myös silloin, kun valo tulee ilmasta veteen. Ilmasta veteen tuleva valo taittuu kuitenkin normaalia kohti, ja taittunut säde on olemassa kaikilla tulokulmilla, joten osa valosta pääsee aina veteen. Kokonaisheijastuminen vaatii, että valo tulee suuremman taitekertoimen aineesta pienemmän taitekertoimen aineeseen. Toinen virhe on luulla, että valokuidun sisäpinta on peilattu. Kuidussa ei ole peilipintaa: ydin ja kuori ovat kumpikin läpinäkyvää lasia, ja valo pysyy ytimessä, koska kuoren taitekerroin on pienempi ja tulokulma on suurempi kuin rajakulma.

## Tiivistelmä
- Kun valo tulee suuremman taitekertoimen aineesta pienemmän taitekertoimen aineeseen, se taittuu normaalista poispäin. Rajakulmassa $\alpha_\text{r}$ taitekulma on $90^\circ$.
- Rajakulma saadaan yhtälöstä $\sin\alpha_\text{r} = n_2 : n_1$, kun $n_1 > n_2$. Kun tulokulma on suurempi kuin rajakulma, kaikki valo heijastuu takaisin: tapahtuu kokonaisheijastuminen.
- Valokuidussa ytimen taitekerroin on hieman suurempi kuin kuoren, ja valo etenee ytimessä kokonaisheijastuen. Liian jyrkästi tuleva valo vuotaa ulos.
- Kuitua käytetään tiedonsiirrossa, tähystimissä ja valaisimissa. Kuidussa valo etenee nopeudella $v = c : n$, ja kulkuaika on $t = n s : c$.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: hyllyllä on kuitulamppu. Sen jalustasta nousee kimppu ohuita läpinäkyviä muovikuituja, jotka kaartuvat joka suuntaan. Kuidut eivät hehku sivuiltaan, mutta jokaisen kuidun pää loistaa kirkkaana pisteenä." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-12-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
