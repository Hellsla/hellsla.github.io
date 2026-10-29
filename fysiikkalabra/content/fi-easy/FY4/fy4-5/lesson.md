# Voimakuvio ja voimien yhteisvaikutus

> **Miksi** pulkka voi painaa lunta eri tavalla, kun sitä vedetään narusta vinosti ylöspäin, kuin silloin, kun se vain seisoo paikallaan?

## Ydinajatus
Kappaleeseen vaikuttaa yleensä monta voimaa yhtä aikaa. Voima on veto tai työntö. Maa vetää kappaletta alaspäin. Alusta tukee sitä. Naru vetää sitä. Pinta jarruttaa sitä. Jokainen voima syntyy kappaleen ja jonkin toisen kappaleen välillä.

Liikkeen ratkaisee kaikkien voimien **yhteisvaikutus**. Sitä sanotaan myös **kokonaisvoimaksi**, ja sen merkki on $\Sigma\mathbf{F}$. Kokonaisvoima on voimien vektorisumma. Vektorisumma tarkoittaa, että voimat lasketaan yhteen suunnat huomioiden. Luvussa *Newtonin toinen laki* opit, että kokonaisvoima määrää kiihtyvyyden: $\Sigma\mathbf{F} = m\mathbf{a}$.

Voimat piirretään ensin **voimakuvioon**. Silloin kaikki voimat tulevat mukaan, eikä laskuun eksy ylimääräisiä voimia. Voimakuvio on eri kuva kuin **tilannekuva**. Tilannekuvassa näkyy koko tilanne: alusta, naru, vetäjä ja liikkeen suunta. Voimakuviossa on vain yksi valittu kappale. Se piirretään yksinkertaisena suorakulmiona. Siihen vaikuttavat voimat on piirretty nuolina. Nuolen suunta on voiman suunta. Pidempi nuoli tarkoittaa suurempaa voimaa.

<svg data-fig="tilanne" viewBox="0 0 600 340" role="img" aria-label="Kaksi kuvaa samasta tilanteesta. Vasemmalla on tilannekuva. Laatikkoa vedetään lattiaa pitkin narulla. Naru nousee vinosti ylöspäin. Laatikon yllä ohut sininen nuoli näyttää nopeuden oikealle. Oikealla on voimakuvio. Siinä on vain laatikko suorakulmiona ja siihen vaikuttavat voimat punaisina nuolina. Paino G osoittaa keskipisteestä suoraan alas. Lattian tukivoima N osoittaa alapinnasta suoraan ylös. Se on lyhyempi kuin paino. Narun jännitysvoima T lähtee narun kiinnityskohdasta vinosti ylös oikealle. Lattian kitkavoima lähtee alapinnan takakulmasta vasemmalle. Nopeutta ei piirretä voimakuvioon." style="max-width:100%;font-size:24px">
  <foreignObject x="77.5" y="7.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <line x1="20" y1="200" x2="280" y2="200" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="20" y1="200" x2="10" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="36" y1="200" x2="26" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="52" y1="200" x2="42" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="68" y1="200" x2="58" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="200" x2="74" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="200" x2="90" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="116" y1="200" x2="106" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="132" y1="200" x2="122" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="148" y1="200" x2="138" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="164" y1="200" x2="154" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="180" y1="200" x2="170" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="196" y1="200" x2="186" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="212" y1="200" x2="202" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="228" y1="200" x2="218" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="244" y1="200" x2="234" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="260" y1="200" x2="250" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="276" y1="200" x2="266" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="80" y="140" width="80" height="60" rx="3" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5"/>
  <line x1="160" y1="160" x2="246.5" y2="110" stroke="#a97a35" stroke-width="3" stroke-linecap="round"/>
  <circle cx="246.5" cy="110" r="8" fill="#6b7480"/>
  <line x1="90" y1="110" x2="158" y2="110" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M147,116.5 L160,110 L147,103.5" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="172" y="91.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\mathbf{v}$</div></foreignObject>
  <line x1="300" y1="20" x2="300" y2="320" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="383.5" y="7.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio}$</div></foreignObject>
  <rect x="400" y="140" width="80" height="60" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="440" y1="170" x2="440" y2="266" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,283 L432,265 L448,265 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="450" y="264.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{G}$</div></foreignObject>
  <line x1="460" y1="200" x2="460" y2="133" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M460,116 L468,134 L452,134 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="470" y="105.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{N}$</div></foreignObject>
  <line x1="480" y1="160" x2="515" y2="140" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M530,131 L518.5,147.5 L510,133 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="540.5" y="105" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{T}$</div></foreignObject>
  <line x1="400" y1="200" x2="382.5" y2="200" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M365.5,200 L383.5,192 L383.5,208 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="335" y="167.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{F}_{\mu}$</div></foreignObject>
</svg>

Kuvassa laatikkoa vedetään narulla vinosti ylöspäin. Narun voima osoittaa eteenpäin ja ylöspäin. Ylöspäin osoittava osa auttaa kannattelemaan laatikkoa. Siksi lattian ei tarvitse tukea laatikkoa yhtä paljon kuin silloin, kun laatikko seisoo paikallaan. Tukivoima $N$ on tässä pienempi kuin paino $G$. Tukivoima on pinnan voima, joka työntää kappaletta pois pinnasta. Nopeutta ei piirretä voimakuvioon. Nopeus ei ole voima.

## Voimakuvion piirtäminen
Voimakuvio piirretään aina samoilla kahdeksalla vaiheella. Käy ne läpi joka kerta. Tee niin myös silloin, kun tilanne näyttää helpolta.

1. **Valitse kappale.** Päätä, minkä kappaleen voimat piirrät. Voimakuvioon tulevat vain voimat, jotka vaikuttavat **tähän kappaleeseen**. Voimat, joilla kappale itse vaikuttaa muihin, eivät kuulu kuvioon.
2. **Etsi vuorovaikutukset.** Luettele kaikki, mikä vaikuttaa kappaleeseen. Maa aiheuttaa painon. Jokainen pinta, jota kappale koskettaa, aiheuttaa tukivoiman ja kitkan. Jokainen naru aiheuttaa jännitysvoiman. Työntö tai veto on voima. Ilma tai vesi aiheuttaa vastuksen ja nosteen. Jokaisella voimalla on aiheuttaja kappaleen ulkopuolella. Pelkkä liike ei aiheuta voimaa.
3. **Piirrä kappale ja voimat.** Piirrä kappale yksinkertaisena suorakulmiona. Piirrä yksi nuoli kutakin voimaa kohti. Nuoli lähtee siitä kohdasta, johon voima vaikuttaa. Työntävän voiman nuoli voi myös päättyä siihen kohtaan.
   - Paino $\mathbf{G}$ osoittaa suoraan alas.
   - Tukivoima $\mathbf{N}$ on kohtisuorassa kosketuspintaa vastaan. Kohtisuorassa tarkoittaa suorassa kulmassa. Tukivoima työntää kappaletta pois pinnasta. Se ei aina osoita ylös. Katto työntää alas ja seinä sivulle.
   - Kitkavoima $\mathbf{F}_\mu$ on kosketuspinnan suuntainen. Se vastustaa liukumista pinnan suhteen. Sen suunta tulee siitä, mihin kappale liukuu tai yrittää liukua pinnan suhteen. Kitka ei aina osoita nopeutta vastaan. Kitkan nuoli alkaa kosketuspinnan kulmasta kappaleen ulkopuolelle tai päättyy siihen. Älä piirrä sitä kappaleen sivua pitkin sivun keskeltä.
   - Jännitysvoima $\mathbf{T}$ vaikuttaa narun suuntaisesti. Se vetää kappaletta narua kohti.
   - Ilmanvastus piirretään vain, jos tilanne ja sen oletukset vaativat sen.
4. **Nimeä voimat.** Anna jokaiselle voimalle oma tunnus. Kaksi samanlaista voimaa erotetaan alaindekseillä, esimerkiksi $\mathbf{T}_1$ ja $\mathbf{T}_2$.
5. **Mieti suuruudet.** Levossa ja tasaisessa liikkeessä kokonaisvoima on nolla. Silloin nuolet kumoavat toisensa. Kiihtyvässä liikkeessä kokonaisvoima osoittaa kiihtyvyyden suuntaan. Kiihtyvyyden suunta ei aina ole nopeuden suunta. Älä keksi tarkkoja pituuksia, jos tiedot eivät määrää niitä.
6. **Vain voimat.** Nopeus, kiihtyvyys ja siirtymä eivät ole voimia. Jos niitä tarvitaan, piirrä ne kappaleen viereen ohuina nuolina ja eri värein. Tässä kurssissa voimat ovat punaisia, nopeus on sininen ja kiihtyvyys oranssi. Kokonaisvoima ei ole yksi voima lisää.
7. **Komponentit eivät ole uusia voimia.** Komponentti on voiman osa jonkin akselin suunnassa. Kun voima jaetaan komponentteihin, komponentit korvaavat voiman laskussa. Piirrä ne katkoviivalla. Silloin niitä ei sekoiteta voimiin.
8. **Liikeyhtälö.** Vasta nyt valitaan akselit. Sitten kirjoitetaan Newtonin toinen laki komponenteittain. Käytä kuvion voimia ja etumerkkejä.

<svg data-fig="suunnat" viewBox="0 0 600 620" role="img" aria-label="Neljä tilannetta. Jokaisessa on vasemmalla pieni tilannekuva. Oikealla on kappaleen voimakuvio, jossa kappale on suorakulmio eikä pintoja piirretä. Vasemmalla ylhäällä laatikko lepää vaakasuoralla lattialla. Paino G osoittaa keskipisteestä alas. Yhtä pitkä tukivoima N osoittaa alapinnasta ylös. Oikealla ylhäällä laatikko on paikallaan kaltevalla rinteellä. Voimakuviossa suorakulmio on kallellaan kuten rinteellä. Paino G osoittaa suoraan alas. Tukivoima N on kohtisuorassa alapintaa vastaan. Kitkavoima lähtee alapinnan ylemmästä kulmasta ja osoittaa rinteen suuntaisesti ylös. Vasemmalla alhaalla lamppu roikkuu johdon varassa. Paino G osoittaa alas. Johdon jännitysvoima T osoittaa yläpinnasta ylös. Oikealla alhaalla heliumilmapallo painuu kattoa vasten ja on paikallaan. Noste osoittaa keskipisteestä ylös. Paino osoittaa keskipisteestä alas. Katon tukivoima N painaa yläpintaa alaspäin, pois katon pinnasta. Nosteen nuoli on yhtä pitkä kuin painon ja tukivoiman nuolet yhteensä." style="max-width:100%;font-size:24px">
  <line x1="300" y1="10" x2="300" y2="610" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="10" y1="310" x2="590" y2="310" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="108.5" y="9.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{lattia}$</div></foreignObject>
  <line x1="20" y1="190" x2="120" y2="190" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="20" y1="190" x2="10" y2="202" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="36" y1="190" x2="26" y2="202" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="52" y1="190" x2="42" y2="202" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="68" y1="190" x2="58" y2="202" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84" y1="190" x2="74" y2="202" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="190" x2="90" y2="202" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="116" y1="190" x2="106" y2="202" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="42" y="146" width="56" height="44" rx="3" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5"/>
  <rect x="185" y="138" width="60" height="44" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="215" y1="160" x2="215" y2="231" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M215,248 L207,230 L223,230 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="225" y="229.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{G}$</div></foreignObject>
  <line x1="230" y1="182" x2="230" y2="111" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M230,94 L238,112 L222,112 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="240" y="83.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{N}$</div></foreignObject>
  <foreignObject x="415" y="9.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{rinne}$</div></foreignObject>
  <line x1="312" y1="230" x2="421" y2="179.5" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="312" y1="230" x2="302" y2="242" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="326.5" y1="223" x2="316.5" y2="235" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="341" y1="216.5" x2="331" y2="228.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="355.5" y1="209.5" x2="345.5" y2="221.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="370" y1="203" x2="360" y2="215" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="384.5" y1="196" x2="374.5" y2="208" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="399" y1="189.5" x2="389" y2="201.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="413.5" y1="182.5" x2="403.5" y2="194.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M350.1,212.3 L389.9,193.7 L375.6,162.8 L335.7,181.4 Z" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="462" y="128" width="60" height="44" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5" transform="rotate(-25 492 150)"/>
  <line x1="492" y1="150" x2="492" y2="221" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M492,238 L484,220 L500,220 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="502" y="227.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{G}$</div></foreignObject>
  <line x1="490.5" y1="175" x2="464" y2="118" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M456.5,102.5 L471.5,115.5 L457,122.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="430.5" y="82" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{N}$</div></foreignObject>
  <line x1="528.5" y1="157.5" x2="547" y2="148.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M562,141.5 L549.5,156.5 L542.5,142 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="545.5" y="151" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{F}_{\mu}$</div></foreignObject>
  <foreignObject x="108.5" y="319.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{lamppu}$</div></foreignObject>
  <line x1="30" y1="360" x2="110" y2="360" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="30" y1="360" x2="20" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="46" y1="360" x2="36" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="62" y1="360" x2="52" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="78" y1="360" x2="68" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="94" y1="360" x2="84" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="70" y1="360" x2="70" y2="440" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M48,470 L92,470 L81,440 L59,440 Z" fill="#e9c98a" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="190" y="452" width="50" height="36" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="215" y1="470" x2="215" y2="530" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M215,547 L207,529 L223,529 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="227" y="528.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{G}$</div></foreignObject>
  <line x1="215" y1="452" x2="215" y2="392" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M215,375 L223,393 L207,393 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="227" y="380.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{T}$</div></foreignObject>
  <foreignObject x="377.5" y="319.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{heliumpallo}$</div></foreignObject>
  <line x1="316" y1="360" x2="430" y2="360" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="316" y1="360" x2="306" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="332" y1="360" x2="322" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="348" y1="360" x2="338" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="364" y1="360" x2="354" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="360" x2="370" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="396" y1="360" x2="386" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="412" y1="360" x2="402" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="372" cy="402" r="40" fill="#f2a69c" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="372" y1="442" x2="368" y2="520" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="480" y="470" width="70" height="40" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="515" y1="490" x2="515" y2="407" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M515,390 L523,408 L507,408 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="513.5" y="387.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{F}_\text{noste}$</div></foreignObject>
  <line x1="515" y1="490" x2="515" y2="513" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M515,530 L507,512 L523,512 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="523" y="519.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{G}$</div></foreignObject>
  <line x1="495" y1="410" x2="495" y2="453" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M495,470 L487,452 L503,452 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="465" y="389.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{N}$</div></foreignObject>
</svg>

Kuvassa on neljä tilannetta. Niissä voimien suunnat yllättävät usein. Rinteellä tukivoima on kohtisuorassa rinnettä vastaan. Se ei ole pystysuora. Kitka pitää laatikkoa paikallaan rinteen suuntaisesti. Heliumpallo painuu kattoa vasten. Katto vaikuttaa palloon alaspäin.

Voimakuviossa kappale on aina yksinkertainen suorakulmio. Jokainen voima lähtee omasta vaikutuskohdastaan. Paino lähtee keskipisteestä. Tukivoima ja kitka lähtevät kosketuspinnasta. Jännitysvoima lähtee narun kiinnityskohdasta. Työntävän voiman nuoli voi myös päättyä siihen kohtaan, johon työntö kohdistuu. Tilannekuvassa kappaleet piirretään sellaisina kuin ne näyttävät. Voimakuvioon piirretään vain suorakulmio ja voimat.

Ylioppilaskokeiden arviointiohjeissa voimakuviosta saa tehtäväkohtaisia pisteitä. Kevään 2025 heliumpallotehtävässä puuttuva, ylimääräinen tai väärään suuntaan piirretty voima vei kaikki voimakuvion pisteet. Samoin kävi, jos pallon voimaksi piirrettiin nopeus tai kiihtyvyys. Syksyn 2025 kokeessa puuttuvasta nimestä vähennettiin piste. Tarkka pisteytys vaihtelee tehtävästä toiseen. Joka kokeessa vaaditaan samaa: kaikki voimat, ei keksittyjä voimia, oikeat suunnat ja yksiselitteiset nimet.

## Kaava: Liikeyhtälö komponenteittain
Newtonin toinen laki koskee kokonaisvoimaa:
```latex
\Sigma\mathbf{F} = m\mathbf{a}
```
missä $\Sigma\mathbf{F}$ on kappaleeseen vaikuttavien voimien vektorisumma (N), $m$ kappaleen massa (kg) ja $\mathbf{a}$ sen kiihtyvyys (m/s²). Joskus voimat eivät ole samalla suoralla. Silloin valitaan kaksi kohtisuoraa akselia. Laki kirjoitetaan erikseen kummankin akselin suuntaan:
```latex
\begin{aligned}
\Sigma F_x &= m a_x \\
\Sigma F_y &= m a_y
\end{aligned}
```
missä $\Sigma F_x$ ja $\Sigma F_y$ ovat voimien komponenttien summat (N) ja $a_x$ ja $a_y$ kiihtyvyyden komponentit (m/s²). Komponentti on positiivinen, kun se osoittaa akselin suuntaan. Se on negatiivinen, kun se osoittaa vastakkaiseen suuntaan. Valitse akselit niin, että toinen osoittaa kiihtyvyyden suuntaan.

Vinon voiman $F$ komponentit saadaan suorakulmaisesta kolmiosta. Kulma $\alpha$ on voiman ja $x$-akselin välinen kulma:
```latex
\begin{aligned}
F_x &= F\cos\alpha \\
F_y &= F\sin\alpha
\end{aligned}
```
missä $F$ on voiman suuruus (N), $F_x$ ja $F_y$ sen komponentit (N) ja $\alpha$ kulma. Komponentit eivät ole uusia voimia. Ne korvaavat voiman $F$ laskussa.

<svg data-fig="komponentit" viewBox="0 0 600 300" role="img" aria-label="Kappaleeseen vaikuttaa voima F. Se lähtee kappaleen oikeasta yläkulmasta vinosti ylös oikealle. Sen ja vaakasuoran välinen kulma on alfa. Komponentit on piirretty katkoviivoin, ja ne lähtevät samasta kulmasta. Vaakasuora F x on x-akselin suuntainen. Pystysuora F y on y-akselin suuntainen. Komponentit ja voima muodostavat suorakulmaisen kolmion. Sen pisin sivu eli hypotenuusa on F. Merkinnät: F x on F kertaa kosini alfa ja F y on F kertaa sini alfa." style="max-width:100%;font-size:24px">
  <rect x="30" y="230" width="80" height="56" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="110" y1="230" x2="260" y2="125" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M274,115.5 L263.5,132 L254.5,119 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="258" y="83" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{F}$</div></foreignObject>
  <line x1="110" y1="230" x2="272" y2="230" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M261,236.5 L274,230 L261,223.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="257.5" y="237.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{F}_{x}$</div></foreignObject>
  <line x1="110" y1="230" x2="110" y2="117.5" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M116.5,128.5 L110,115.5 L103.5,128.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="69.5" y="101" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{F}_{y}$</div></foreignObject>
  <line x1="274" y1="230" x2="274" y2="115.5" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="110" y1="115.5" x2="274" y2="115.5" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <path d="M162,230 A52,52 0 0 0 152.6,200.2" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="174" y="197.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="390" y="105.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F_x = F\cos\alpha$</div></foreignObject>
  <foreignObject x="390" y="155.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F_y = F\sin\alpha$</div></foreignObject>
</svg>

## Esimerkki
Pulkkaa, jonka massa on $12\,\text{kg}$, vedetään vaakasuoralla lumella narulla. Naru on $35^\circ$:n kulmassa vaakatasoon nähden. Narun jännitysvoima on $80\,\text{N}$ ja lumen kitkavoima $30\,\text{N}$. Kuinka suuri on pulkan kiihtyvyys, ja kuinka suuri on lumen tukivoima?

<!-- vaihe -->

**Tunnetut ja kysytty.** $m = 12\,\text{kg}$, $T = 80\,\text{N}$, $\alpha = 35^\circ$, $F_\mu = 30\,\text{N}$ ja $g = 9{,}81\,\text{m/s}^2$. Kysytään kiihtyvyyttä $a$ ja tukivoimaa $N$.

<!-- vaihe -->

**Periaate.** Valitaan kappaleeksi pulkka. Siihen vaikuttavat Maa (paino), lumi (tukivoima ja kitka) ja naru (jännitysvoima). Newtonin toinen laki kirjoitetaan kahteen suuntaan. Vaakasuunnassa pulkka kiihtyy. Pystysuunnassa pulkka pysyy lumen pinnalla, joten $a_y = 0$.

<!-- vaihe -->

**Voimakuvio.** Pulkka piirretään suorakulmiona. Voimat lähtevät vaikutuskohdistaan. Akselit valitaan niin, että $x$ osoittaa liikkeen suuntaan ja $y$ ylös. Narun voima jaetaan komponentteihin $T_x = T\cos\alpha$ ja $T_y = T\sin\alpha$. Ne on piirretty katkoviivalla.

<svg data-fig="esimerkki" viewBox="0 0 600 360" role="img" aria-label="Pulkan voimakuvio. Pulkka on piirretty suorakulmiona. Paino G osoittaa keskipisteestä alas. Lumen tukivoima N osoittaa alapinnasta ylös, ja se on painoa lyhyempi. Narun jännitysvoima T lähtee etuyläkulmasta vinosti ylös oikealle kulmassa 35 astetta. Sen komponentit on piirretty katkoviivoin. Lumen kitkavoima lähtee alapinnan takakulmasta vasemmalle. Nurkassa ovat akselit: x oikealle eli liikkeen suuntaan ja y ylös." style="max-width:100%;font-size:24px">
  <rect x="210" y="163" width="120" height="44" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="270" y1="185" x2="270" y2="303.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M270,320.5 L262,302.5 L278,302.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="280" y="302" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{G}$</div></foreignObject>
  <line x1="290" y1="207" x2="290" y2="141.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M290,124.5 L298,142.5 L282,142.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="260" y="116" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{N}$</div></foreignObject>
  <line x1="330" y1="163" x2="391.5" y2="120" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M405.5,110 L395.5,127 L386,114 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="411.5" y="85.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{T}$</div></foreignObject>
  <line x1="210" y1="207" x2="192.5" y2="207" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M175.5,207 L193.5,199 L193.5,215 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="149" y="176.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{F}_{\mu}$</div></foreignObject>
  <line x1="330" y1="163" x2="403.5" y2="163" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M392.5,169.5 L405.5,163 L392.5,156.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="389" y="172.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{T}_{x}$</div></foreignObject>
  <line x1="330" y1="163" x2="330" y2="112" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M336.5,123 L330,110 L323.5,123" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="285.5" y="99.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{T}_{y}$</div></foreignObject>
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

**Kaava ratkaistuna.** Kuviosta luetaan liikeyhtälöt. Niistä ratkaistaan kysytyt suureet:
```latex
\begin{aligned}
&x\text{:}\ \ T\cos\alpha - F_\mu = m a \\
&y\text{:}\ \ N + T\sin\alpha - mg = 0 \\
&a = \frac{T\cos\alpha - F_\mu}{m} \\
&N = mg - T\sin\alpha
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Muunnoksia ei tarvita. Kaikki suureet ovat SI-yksiköissä, ja $\tfrac{\text{N}}{\text{kg}} = \tfrac{\text{m}}{\text{s}^2}$.

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

**Tulos.** Kiihtyvyys on $a \approx 3{,}0\,\text{m/s}^2$ ja tukivoima $N \approx 72\,\text{N}$. Vastaukset annetaan kahdella merkitsevällä numerolla. Lähtötiedoissa $80\,\text{N}$, $30\,\text{N}$ ja $12\,\text{kg}$ on myös kaksi merkitsevää numeroa.

<!-- vaihe -->

**Järkevyys.** Pulkan paino on $mg \approx 118\,\text{N}$. Tukivoima $72\,\text{N}$ on sitä pienempi. Syy on, että narun pystykomponentti $T_y \approx 46\,\text{N}$ kannattelee osan painosta. Summa täsmää: $72\,\text{N} + 46\,\text{N} \approx 118\,\text{N}$. Ilman kitkaa kiihtyvyys olisi $65{,}5\,\text{N} : 12\,\text{kg} \approx 5{,}5\,\text{m/s}^2$. Kitka siis pienentää kiihtyvyyttä, kuten pitääkin.

## Yleinen virhekäsitys
Liikkuvaan kappaleeseen ei tarvitse vaikuttaa voimaa liikkeen suuntaan. Liukuvaan laatikkoon vaikuttavat vain paino, tukivoima ja kitka. "Liikkeen voimaa" ei ole, koska mikään kappale ei aiheuta sitä.

Toinen yleinen virhe on pitää tukivoimaa aina yhtä suurena kuin paino. Tukivoima on juuri niin suuri, kuin tilanne vaatii. Vinossa vedossa se on painoa pienempi. Vinossa työnnössä se on painoa suurempi. Ylöspäin kiihtyvässä hississä se on myös painoa suurempi.

Kolmas virhe on piirtää komponentit voimiksi voiman lisäksi. Silloin sama voima tulee laskuun kahteen kertaan.

## Tiivistelmä
- Voimakuviossa on vain valittu kappale suorakulmiona ja siihen vaikuttavat voimat. Tilannekuva ja voimakuvio ovat eri kuvia.
- Jokaisella voimalla on aiheuttaja: Maa, pinta, naru, työntäjä tai ilma. Nopeus ja kiihtyvyys eivät ole voimia. Ne piirretään eri värein kuin voimat.
- Tukivoima on kohtisuorassa pintaa vastaan. Kitka on pinnan suuntainen. Jännitysvoima on narun suuntainen.
- Kokonaisvoima on voimien vektorisumma. Laki $\Sigma\mathbf{F} = m\mathbf{a}$ kirjoitetaan komponenteittain: $\Sigma F_x = m a_x$ ja $\Sigma F_y = m a_y$.
- Vinon voiman komponentit ovat $F\cos\alpha$ ja $F\sin\alpha$. Ne korvaavat voiman laskussa. Ne eivät ole uusia voimia.
