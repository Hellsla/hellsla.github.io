# Voimakuvio ja voimien yhteisvaikutus

> **Miksi** pulkka voi painaa alustaansa eri tavalla, kun sitä vedetään narusta vinosti ylöspäin, kuin silloin, kun se vain seisoo paikallaan?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: talvinen piha. Vasemmalla pulkka seisoo paikallaan ja on painunut syvälle lumeen. Oikealla lapsi vetää samanlaista pulkkaa narusta vinosti ylöspäin, ja sen jättämä jälki lumessa on matalampi." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-5-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Kappaleeseen vaikuttaa yleensä monta voimaa yhtä aikaa. Maa vetää sitä alaspäin, alusta tukee, naru vetää ja pinta jarruttaa. Jokainen voima kertoo yhdestä vuorovaikutuksesta kappaleen ja jonkin toisen kappaleen välillä. Liikkeen ratkaisee näiden voimien **yhteisvaikutus** eli **kokonaisvoima** $\Sigma\overline{F}$, joka on voimien vektorisumma. Luvussa *Newtonin toinen laki* opit, että kokonaisvoima määrää kiihtyvyyden: $\Sigma\overline{F} = m\overline{a}$.

Jotta kaikki voimat tulevat mukaan eikä mitään ylimääräistä eksy laskuun, voimat piirretään ensin **voimakuvioon**. Se on eri kuva kuin **tilannekuva**. Tilannekuvassa näkyy koko tilanne: alusta, naru, vetäjä ja liikkeen suunta. Voimakuviossa on vain valittu kappale pelkistettynä suorakulmiona ja siihen vaikuttavat voimat nuolina. Nuolen suunta on voiman suunta, ja nuolten pituudet kertovat, mikä voima on suurempi.

<svg data-fig="tilanne" viewBox="0 0 600 340" role="img" aria-label="Kaksi kuvaa samasta tilanteesta. Vasemmalla tilannekuva: laatikkoa vedetään lattiaa pitkin narulla, joka nousee vinosti ylöspäin, ja laatikon yllä ohut sininen nuoli näyttää nopeuden oikealle. Oikealla voimakuvio: vain laatikko suorakulmiona ja siihen vaikuttavat voimat punaisina nuolina. Paino G osoittaa keskipisteestä suoraan alas, lattian tukivoima N alapinnasta suoraan ylös ja on lyhyempi kuin paino, narun jännitysvoima T lähtee narun kiinnityskohdasta vinosti ylös oikealle ja lattian kitkavoima lähtee alapinnan takakulmasta vasemmalle. Nopeutta ei piirretä voimakuvioon." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-5-tilanne.webp" x="0" y="0" width="600" height="350" preserveAspectRatio="none"/>
  <foreignObject x="77.5" y="7.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <foreignObject x="165.5" y="91.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="383.5" y="7.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio}$</div></foreignObject>
  <foreignObject x="443.5" y="264.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="463.5" y="105.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="534" y="105" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <foreignObject x="329" y="167.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
</svg>

Kuvan laatikkoa vedetään narulla vinosti ylöspäin. Narun voima osoittaa sekä eteenpäin että ylöspäin. Ylöspäin osoittava osa kannattelee laatikkoa, joten lattian ei tarvitse tukea sitä yhtä paljon kuin paikallaan seistessä. Siksi tukivoima $N$ on pienempi kuin paino $G$. Nopeutta ei piirretä voimakuvioon, koska nopeus ei ole voima.

```pysahdy
Jääkiekko liukuu jäällä tasaisesti oikealle. Piirrätkö sen voimakuvioon voiman liikkeen suuntaan?
---
Et. Nopeus ei ole voima, eikä mikään toinen kappale työnnä kiekkoa eteenpäin. Voimakuvioon tulevat vain voimat, joilla muut kappaleet vaikuttavat kiekkoon.
```

## Voimakuvion piirtäminen
Voimakuvio piirretään aina samoilla kahdeksalla vaiheella. Ne kannattaa käydä läpi joka kerta, myös silloin, kun tilanne näyttää helpolta.

1. **Valitse kappale.** Päätä, minkä kappaleen voimat piirrät. Voimakuvioon tulevat vain voimat, jotka vaikuttavat **tähän kappaleeseen**. Voimat, joilla kappale itse vaikuttaa muihin, eivät kuulu siihen.
2. **Etsi vuorovaikutukset.** Luettele kaikki, mikä vaikuttaa kappaleeseen: Maa (paino), jokainen pinta, jota kappale koskettaa (tukivoima ja kitka), jokainen naru (jännitysvoima), työntö tai veto sekä ilma tai vesi (vastus ja noste). Jokaisella voimalla on aiheuttaja kappaleen ulkopuolella. Pelkkä liike ei aiheuta voimaa.
3. **Piirrä kappale ja voimat.** Piirrä kappale pelkistettynä suorakulmiona. Piirrä kullekin voimalle yksi nuoli, joka lähtee voiman vaikutuskohdasta. Työntävän voiman nuoli voi myös päättyä vaikutuskohtaan.
    - Paino $\overline{G}$ osoittaa suoraan alas.
    - Tukivoima $\overline{N}$ on kohtisuorassa kosketuspintaa vastaan ja työntää kappaletta poispäin pinnasta. Se ei aina osoita ylös: katto työntää alas ja seinä sivulle.
    - Kitkavoima $\overline{F}_\mu$ on kosketuspinnan suuntainen. Sen suunta tulee siitä, mihin suuntaan kappale liukuu tai pyrkii liukumaan pinnan suhteen. Se ei aina ole nopeutta vastaan. Kitkan nuoli alkaa kosketuspinnan kulmasta kappaleen ulkopuolelle tai päättyy siihen. Sitä ei piirretä kappaleen sivua pitkin sivun keskeltä.
    - Jännitysvoima $\overline{T}$ vaikuttaa narun suuntaisesti ja vetää kappaletta narua kohti.
    - Ilmanvastus piirretään vain, kun tilanne ja sen oletukset sitä vaativat.
4. **Nimeä voimat.** Anna jokaiselle voimalle oma tunnus. Kaksi samanlaista voimaa erotetaan indekseillä, esimerkiksi $\overline{T}_1$ ja $\overline{T}_2$.
5. **Mieti suuruudet.** Levossa ja tasaisessa liikkeessä kokonaisvoima on nolla, joten nuolet kumoavat toisensa. Kiihtyvässä liikkeessä kokonaisvoima osoittaa kiihtyvyyden suuntaan, joka ei aina ole nopeuden suunta. Älä keksi tarkkoja pituuksia, jos tiedot eivät niitä määrää.
6. **Vain voimat.** Nopeus, kiihtyvyys ja siirtymä eivät ole voimia. Jos niitä tarvitaan, ne piirretään kappaleen viereen ohuina nuolina ja eri värein: tässä kurssissa voimat ovat punaisia, nopeus sininen ja kiihtyvyys oranssi. Kokonaisvoima ei ole yksi voima lisää.
7. **Komponentit eivät ole uusia voimia.** Kun voima jaetaan komponentteihin, komponentit yhdessä korvaavat voiman laskussa. Ne piirretään katkoviivalla, jotta niitä ei sekoiteta voimiin.
8. **Liikeyhtälö.** Vasta nyt valitaan akselit ja kirjoitetaan Newtonin toinen laki komponenteittain kuvion voimista ja etumerkeistä.

<svg data-fig="suunnat" viewBox="0 0 600 620" role="img" aria-label="Neljä tilannetta. Kussakin on vasemmalla pieni tilannekuva ja oikealla kappaleen voimakuvio, jossa kappale on suorakulmio eikä pintoja piirretä. Vasemmalla ylhäällä laatikko lepää vaakasuoralla lattialla: paino G keskipisteestä alas ja yhtä pitkä tukivoima N alapinnasta ylös. Oikealla ylhäällä laatikko on paikallaan kaltevalla rinteellä: voimakuviossa suorakulmio on kallellaan kuten rinteellä, paino G suoraan alas, tukivoima N kohtisuoraan alapintaa vastaan ja kitkavoima alapinnan ylemmästä kulmasta rinteen suuntaisesti ylös. Vasemmalla alhaalla lamppu roikkuu johdon varassa: paino G alas ja johdon jännitysvoima T yläpinnasta ylös. Oikealla alhaalla heliumilmapallo painuu kattoa vasten ja on paikallaan: noste keskipisteestä ylös, paino keskipisteestä alas ja katon tukivoima N, joka painaa yläpintaa alaspäin, pois katon pinnasta. Nosteen nuoli on yhtä pitkä kuin painon ja tukivoiman nuolet yhteensä." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-5-suunnat.webp" x="0" y="0" width="600" height="620" preserveAspectRatio="none"/>
  <foreignObject x="108.5" y="9.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{lattia}$</div></foreignObject>
  <foreignObject x="218.5" y="229.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="233.5" y="83.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="415" y="9.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{rinne}$</div></foreignObject>
  <foreignObject x="495.5" y="227.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="446" y="72" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="539.5" y="151" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <foreignObject x="108.5" y="319.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{lamppu}$</div></foreignObject>
  <foreignObject x="220.5" y="528.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="220.5" y="380.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <foreignObject x="377.5" y="319.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{heliumpallo}$</div></foreignObject>
  <foreignObject x="507.5" y="387.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{noste}$</div></foreignObject>
  <foreignObject x="516.5" y="519.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="458.5" y="389.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
</svg>

Kuvassa on neljä tilannetta, joissa voimien suunnat yllättävät usein. Rinteellä tukivoima on kohtisuorassa rinnettä vastaan eikä pystysuora, ja kitka pitää laatikkoa paikallaan rinteen suuntaisesti. Kattoa vasten painuvaan heliumpalloon katto vaikuttaa alaspäin.

```pysahdy
Laatikko on paikallaan kaltevalla rinteellä. Osoittaako tukivoima pystysuoraan ylöspäin, ja mikä estää laatikkoa liukumasta alas?
---
Ei osoita. Tukivoima on kohtisuorassa rinnettä vastaan. Laatikon pitää paikallaan rinteen suuntaisesti ylöspäin osoittava kitkavoima.
```

Voimakuviossa kappale on aina pelkistetty suorakulmio, ja jokainen voima lähtee vaikutuskohdastaan: paino keskipisteestä, tukivoima ja kitka kosketuspinnasta ja jännitysvoima narun kiinnityskohdasta. Työntävän voiman nuoli voi myös päättyä kohtaan, johon työntö kohdistuu. Tilannekuvassa kappaleet piirretään sellaisina kuin ne näyttävät, mutta voimakuvioon piirretään vain suorakulmio ja voimat.

Ylioppilaskokeiden arviointiohjeissa voimakuviolle on annettu tehtäväkohtaiset pisteet. Esimerkiksi kevään 2025 heliumpallotehtävässä puuttuva, ylimääräinen tai väärään suuntaan piirretty voima vei kaikki voimakuvion pisteet, ja nopeuden tai kiihtyvyyden piirtäminen pallon voimaksi samoin. Syksyn 2025 kokeessa puuttuvasta nimestä vähennettiin piste. Tarkka pisteytys vaihtelee tehtävästä toiseen, mutta joka kokeessa vaaditaan samaa: kaikki voimat, ei keksittyjä voimia, oikeat suunnat ja yksiselitteiset nimet.

## Kaava: Liikeyhtälö komponenteittain
Newtonin toinen laki koskee kokonaisvoimaa:
```kaavat
Newtonin 2. laki (dynamiikan peruslaki) :: \Sigma\overline{F} = m\overline{a}
```
missä $\Sigma\overline{F}$ on kappaleeseen vaikuttavien voimien vektorisumma (N), $m$ kappaleen massa (kg) ja $\overline{a}$ sen kiihtyvyys (m/s²). Kun voimat eivät ole samalla suoralla, valitaan kaksi kohtisuoraa akselia ja kirjoitetaan laki kummankin akselin suuntaan erikseen:
```latex
\begin{aligned}
\Sigma F_x &= m a_x \\
\Sigma F_y &= m a_y
\end{aligned}
```
missä $\Sigma F_x$ ja $\Sigma F_y$ ovat voimien komponenttien summat (N) ja $a_x$ ja $a_y$ kiihtyvyyden komponentit (m/s²). Akselin suuntaan osoittava komponentti on positiivinen ja vastakkainen negatiivinen. Akselit kannattaa valita niin, että toinen osoittaa kiihtyvyyden suuntaan.

Vinon voiman $F$ komponentit saadaan suorakulmaisesta kolmiosta, kun $\alpha$ on voiman ja $x$-akselin välinen kulma:
```latex
\begin{aligned}
F_x &= F\cos\alpha \\
F_y &= F\sin\alpha
\end{aligned}
```
missä $F$ on voiman suuruus (N), $F_x$ ja $F_y$ sen komponentit (N) ja $\alpha$ kulma. Komponentit eivät ole uusia voimia, vaan ne korvaavat voiman $F$ laskussa.

<svg data-fig="komponentit" viewBox="0 0 600 300" role="img" aria-label="Kappaleeseen vaikuttaa voima F, joka lähtee kappaleen oikeasta yläkulmasta vinosti ylös oikealle kulmassa alfa vaakasuoraan nähden. Katkoviivoin piirretyt komponentit lähtevät samasta kulmasta: vaakasuora F x pitkin x-akselia ja pystysuora F y pitkin y-akselia. Komponentit ja voima muodostavat suorakulmaisen kolmion, jonka hypotenuusa on F. Merkinnät: F x on F kertaa kosini alfa ja F y on F kertaa sini alfa." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-5-komponentit.webp" x="3.8" y="6.3" width="606.1" height="311.9" preserveAspectRatio="none"/>
  <foreignObject x="251.5" y="83" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="251.5" y="237.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{x}$</div></foreignObject>
  <foreignObject x="63.5" y="101" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{y}$</div></foreignObject>
  <foreignObject x="174" y="197.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="390" y="105.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F_x = F\cos\alpha$</div></foreignObject>
  <foreignObject x="390" y="155.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F_y = F\sin\alpha$</div></foreignObject>
</svg>

## Esimerkki
Pulkkaa, jonka massa on $12\,\text{kg}$, vedetään vaakasuoralla lumella narulla, joka on $35^\circ$:n kulmassa vaakatasoon nähden. Narun jännitysvoima on $80\,\text{N}$ ja lumen kitkavoima $30\,\text{N}$. Kuinka suuri on pulkan kiihtyvyys, ja kuinka suuri on lumen tukivoima?

<!-- vaihe -->

**Tunnetut ja kysytty.** $m = 12\,\text{kg}$, $T = 80\,\text{N}$, $\alpha = 35^\circ$, $F_\mu = 30\,\text{N}$ ja $g = 9{,}81\,\text{m/s}^2$.

Kysytään kiihtyvyyttä $a$ ja tukivoimaa $N$.

<!-- vaihe -->

**Periaate.** Valitaan kappaleeksi pulkka. Siihen vaikuttavat Maa (paino), lumi (tukivoima ja kitka) ja naru (jännitysvoima). Newtonin toinen laki kirjoitetaan kahteen suuntaan: vaakasuunnassa pulkka kiihtyy, pystysuunnassa se pysyy lumen pinnalla, joten $a_y = 0$.

<!-- vaihe -->

**Voimakuvio.** Pulkka piirretään suorakulmiona, ja voimat lähtevät vaikutuskohdistaan. Akselit valitaan niin, että $x$ osoittaa liikkeen suuntaan ja $y$ ylös. Narun voima jaetaan komponentteihin $T_x = T\cos\alpha$ ja $T_y = T\sin\alpha$, jotka on piirretty katkoviivalla.

<svg data-fig="esimerkki" viewBox="0 0 600 360" role="img" aria-label="Pulkan voimakuvio, pulkka suorakulmiona. Paino G keskipisteestä alas, lumen tukivoima N alapinnasta ylös ja painoa lyhyempi, narun jännitysvoima T etuyläkulmasta vinosti ylös oikealle kulmassa 35 astetta, sen komponentit katkoviivoin, ja lumen kitkavoima alapinnan takakulmasta vasemmalle. Nurkassa akselit: x oikealle eli liikkeen suuntaan ja y ylös." style="max-width:100%;font-size:24px">
  <rect x="210" y="163" width="120" height="44" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="270" y1="185" x2="270" y2="303.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M270,320.5 L262,302.5 L278,302.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="273.5" y="302" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="290" y1="207" x2="290" y2="141.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M290,124.5 L298,142.5 L282,142.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="243.5" y="116" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="330" y1="163" x2="391.5" y2="120" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M405.5,110 L395.5,127 L386,114 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="405" y="85.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}$</div></foreignObject>
  <line x1="210" y1="207" x2="192.5" y2="207" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M175.5,207 L193.5,199 L193.5,215 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="143" y="176.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <line x1="330" y1="163" x2="403.5" y2="163" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M392.5,169.5 L405.5,163 L392.5,156.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="383" y="172.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{x}$</div></foreignObject>
  <line x1="330" y1="163" x2="330" y2="112" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M336.5,123 L330,110 L323.5,123" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="303.5" y="79.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{T}_{y}$</div></foreignObject>
  <path d="M370.0,163.0 A40,40 0 0 0 362.8,140.1" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="378" y="134.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$35^\circ$</div></foreignObject>
  <line x1="70" y1="320" x2="107" y2="320" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M116,320 L106,324.5 L106,315.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="70" y1="320" x2="70" y2="283" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M70,274 L74.5,284 L65.5,284 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="118" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$x$</div></foreignObject>
  <foreignObject x="60" y="247.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$y$</div></foreignObject>
</svg>

<!-- vaihe -->

**Kaava ratkaistuna.** Kuviosta luetaan liikeyhtälöt ja ratkaistaan kysytyt suureet:
```latex
\begin{aligned}
&x\text{:}\ \ T\cos\alpha - F_\mu = m a \\
&y\text{:}\ \ N + T\sin\alpha - mg = 0 \\
&a = \frac{T\cos\alpha - F_\mu}{m} \\
&N = mg - T\sin\alpha
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: kaikki suureet ovat SI-yksiköissä, ja $\tfrac{\text{N}}{\text{kg}} = \tfrac{\text{m}}{\text{s}^2}$.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan lukuarvot yksiköineen:
```latex
\begin{aligned}
&a = \frac{T\cos\alpha - F_\mu}{m} \\
&\phantom{a} = \frac{80\,\text{N}\cdot\cos 35^\circ - 30\,\text{N}}{12\,\text{kg}} \\
&\phantom{a} \approx 2{,}96\,\text{m/s}^2 \\[4pt]
&N = mg - T\sin\alpha \\
&\phantom{N} = 12\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 \\
&\quad\ - 80\,\text{N}\cdot\sin 35^\circ \\
&\phantom{N} \approx 71{,}8\,\text{N}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Kiihtyvyys on $a \approx 2{,}96\,\text{m/s}^2$ ja tukivoima $N \approx 71{,}8\,\text{N}$. Lähtötietojen kokonaisluvut $12\,\text{kg}$, $80\,\text{N}$, $30\,\text{N}$ ja $35^\circ$ tulkitaan tarkoiksi arvoiksi. Kiihtyvyys lasketaan pelkistä tarkoista arvoista, ja se annetaan kolmella merkitsevällä numerolla. Tukivoiman tarkkuuden rajaa putoamiskiihtyvyys $9{,}81\,\text{m/s}^2$, joten sekin annetaan kolmella merkitsevällä numerolla.

<!-- vaihe -->

**Järkevyys.** Pulkan paino on $mg \approx 118\,\text{N}$. Tukivoima $71{,}8\,\text{N}$ on sitä pienempi, koska narun pystykomponentti $T_y \approx 45{,}9\,\text{N}$ kannattelee osan painosta, ja $71{,}8\,\text{N} + 45{,}9\,\text{N} \approx 118\,\text{N}$. Ilman kitkaa kiihtyvyys olisi $65{,}5\,\text{N} : 12\,\text{kg} \approx 5{,}5\,\text{m/s}^2$, joten kitka pienentää sitä, kuten pitääkin.

## Yleinen virhekäsitys
Liikkuvaan kappaleeseen ei tarvitse vaikuttaa voimaa liikkeen suuntaan. Liukuvaan laatikkoon vaikuttavat vain paino, tukivoima ja kitka, eikä "liikkeen voimaa" ole: ei ole mitään kappaletta, joka sitä aiheuttaisi. Toinen yleinen virhe on pitää tukivoimaa aina yhtä suurena kuin paino. Tukivoima on juuri niin suuri, kuin tilanne vaatii: vinossa vedossa se on painoa pienempi, vinossa työnnössä suurempi ja ylöspäin kiihtyvässä hississä suurempi. Kolmas virhe on piirtää komponentit voimiksi voiman lisäksi, jolloin sama voima tulee laskuun kahteen kertaan.

## Tiivistelmä
- Voimakuviossa on vain valittu kappale suorakulmiona ja siihen vaikuttavat voimat. Tilannekuva ja voimakuvio ovat eri kuvia.
- Jokaisella voimalla on aiheuttaja: Maa, pinta, naru, työntäjä tai ilma. Nopeus ja kiihtyvyys eivät ole voimia, ja ne piirretään eri värein kuin voimat.
- Tukivoima on kohtisuorassa pintaa vastaan, kitka pinnan suuntainen ja jännitysvoima narun suuntainen.
- Kokonaisvoima on voimien vektorisumma, ja $\Sigma\overline{F} = m\overline{a}$ kirjoitetaan komponenteittain: $\Sigma F_x = m a_x$ ja $\Sigma F_y = m a_y$.
- Vinon voiman komponentit ovat $F\cos\alpha$ ja $F\sin\alpha$. Ne korvaavat voiman laskussa eivätkä ole uusia voimia.
