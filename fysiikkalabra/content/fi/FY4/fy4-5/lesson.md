# Voimakuvio ja voimien yhteisvaikutus

> **Miksi** pulkka voi painaa lunta eri tavalla, kun sitä vedetään narusta vinosti ylöspäin, kuin silloin, kun se vain seisoo paikallaan?

## Ydinajatus
Kappaleeseen vaikuttaa yleensä monta voimaa yhtä aikaa. Maa vetää sitä alaspäin, alusta tukee, naru vetää ja pinta jarruttaa. Jokainen voima kertoo yhdestä vuorovaikutuksesta kappaleen ja jonkin toisen kappaleen välillä. Liikkeen ratkaisee näiden voimien **yhteisvaikutus** eli **kokonaisvoima** $\Sigma\mathbf{F}$, joka on voimien vektorisumma. Luvussa *Newtonin toinen laki* opit, että kokonaisvoima määrää kiihtyvyyden: $\Sigma\mathbf{F} = m\mathbf{a}$.

Jotta kaikki voimat tulevat mukaan eikä mitään ylimääräistä eksy laskuun, voimat piirretään ensin **voimakuvioon**. Se on eri kuva kuin **tilannekuva**. Tilannekuvassa näkyy koko tilanne: alusta, naru, vetäjä ja liikkeen suunta. Voimakuviossa on vain valittu kappale ja siihen vaikuttavat voimat nuolina. Nuolen suunta on voiman suunta, ja nuolten pituudet kertovat, mikä voima on suurempi.

<svg data-fig="tilanne" viewBox="0 0 600 340" role="img" aria-label="Kaksi kuvaa samasta tilanteesta. Vasemmalla tilannekuva: laatikkoa vedetään lattiaa pitkin narulla, joka nousee vinosti ylöspäin, ja laatikon yllä ohut sininen nuoli näyttää nopeuden oikealle. Oikealla voimakuvio: vain laatikko ja siihen vaikuttavat voimat punaisina nuolina. Paino G osoittaa keskipisteestä suoraan alas, lattian tukivoima N alapinnasta suoraan ylös ja on lyhyempi kuin paino, narun jännitysvoima T lähtee narun kiinnityskohdasta vinosti ylös oikealle ja lattian kitkavoima alapinnasta vasemmalle. Nopeutta ei piirretä voimakuvioon." style="max-width:100%;font-size:24px">
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
  <rect x="400" y="140" width="80" height="60" rx="3" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5"/>
  <line x1="440" y1="170" x2="440" y2="266" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M440,283 L432,265 L448,265 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="450" y="264.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{G}$</div></foreignObject>
  <line x1="460" y1="200" x2="460" y2="133" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M460,116 L468,134 L452,134 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="470" y="105.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{N}$</div></foreignObject>
  <line x1="480" y1="160" x2="515" y2="140" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M530,131 L518.5,147.5 L510,133 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="540.5" y="105" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{T}$</div></foreignObject>
  <line x1="418" y1="200" x2="400.5" y2="200" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M383.5,200 L401.5,192 L401.5,208 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="353" y="169.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{F}_{\mu}$</div></foreignObject>
</svg>

Kuvan laatikkoa vedetään narulla vinosti ylöspäin. Narun voima osoittaa sekä eteenpäin että ylöspäin. Ylöspäin osoittava osa kannattelee laatikkoa, joten lattian ei tarvitse tukea sitä yhtä paljon kuin paikallaan seistessä. Siksi tukivoima $N$ on pienempi kuin paino $G$. Nopeutta ei piirretä voimakuvioon, koska nopeus ei ole voima.

## Voimakuvion piirtäminen
Voimakuvio piirretään aina samoilla kahdeksalla vaiheella. Ne kannattaa käydä läpi joka kerta, myös silloin, kun tilanne näyttää helpolta.

1. **Valitse kappale.** Päätä, minkä kappaleen voimat piirrät. Voimakuvioon tulevat vain voimat, jotka vaikuttavat **tähän kappaleeseen**. Voimat, joilla kappale itse vaikuttaa muihin, eivät kuulu siihen.
2. **Etsi vuorovaikutukset.** Luettele kaikki, mikä vaikuttaa kappaleeseen: Maa (paino), jokainen pinta, jota kappale koskettaa (tukivoima ja kitka), jokainen naru (jännitysvoima), työntö tai veto sekä ilma tai vesi (vastus ja noste). Jokaisella voimalla on aiheuttaja kappaleen ulkopuolella. Pelkkä liike ei aiheuta voimaa.
3. **Piirrä voimat.** Yksi nuoli kutakin voimaa kohti, ja nuoli lähtee kappaleesta.
   - Paino $\mathbf{G}$ osoittaa suoraan alas.
   - Tukivoima $\mathbf{N}$ on kohtisuorassa kosketuspintaa vastaan ja työntää kappaletta poispäin pinnasta. Se ei aina osoita ylös: katto työntää alas ja seinä sivulle.
   - Kitkavoima $\mathbf{F}_\mu$ on kosketuspinnan suuntainen. Sen suunta tulee siitä, mihin suuntaan kappale liukuu tai pyrkii liukumaan pinnan suhteen. Se ei aina ole nopeutta vastaan.
   - Jännitysvoima $\mathbf{T}$ vaikuttaa narun suuntaisesti ja vetää kappaletta narua kohti.
   - Ilmanvastus piirretään vain, kun tilanne ja sen oletukset sitä vaativat.
4. **Nimeä voimat.** Anna jokaiselle voimalle oma tunnus. Kaksi samanlaista voimaa erotetaan indekseillä, esimerkiksi $\mathbf{T}_1$ ja $\mathbf{T}_2$.
5. **Mieti suuruudet.** Levossa ja tasaisessa liikkeessä kokonaisvoima on nolla, joten nuolet kumoavat toisensa. Kiihtyvässä liikkeessä kokonaisvoima osoittaa kiihtyvyyden suuntaan, joka ei aina ole nopeuden suunta. Älä keksi tarkkoja pituuksia, jos tiedot eivät niitä määrää.
6. **Vain voimat.** Nopeus, kiihtyvyys ja siirtymä eivät ole voimia. Jos niitä tarvitaan, ne piirretään kappaleen viereen eri tyylillä. Kokonaisvoima ei ole yksi voima lisää.
7. **Komponentit eivät ole uusia voimia.** Kun voima jaetaan komponentteihin, komponentit yhdessä korvaavat voiman laskussa. Ne piirretään katkoviivalla, jotta niitä ei sekoiteta voimiin.
8. **Liikeyhtälö.** Vasta nyt valitaan akselit ja kirjoitetaan Newtonin toinen laki komponenteittain kuvion voimista ja etumerkeistä.

<svg data-fig="suunnat" viewBox="0 0 600 620" role="img" aria-label="Neljä pientä voimakuviota. Vasemmalla ylhäällä laatikko lepää vaakasuoralla lattialla: paino G keskipisteestä alas ja yhtä pitkä tukivoima N alapinnasta ylös. Oikealla ylhäällä laatikko on paikallaan kaltevalla rinteellä: paino G suoraan alas, tukivoima N kohtisuoraan rinnettä vastaan ja kitkavoima rinteen suuntaisesti ylös. Vasemmalla alhaalla lamppu roikkuu johdon varassa: paino G alas ja johdon jännitysvoima T johtoa pitkin ylös. Oikealla alhaalla heliumilmapallo painuu kattoa vasten ja on paikallaan. Sen vieressä pallon voimakuvio pisteenä: noste ylös, paino alas ja sen vieressä katon tukivoima N alas, pois katon pinnasta. Nosteen nuoli on yhtä pitkä kuin painon ja tukivoiman nuolet yhteensä." style="max-width:100%;font-size:24px">
  <line x1="300" y1="10" x2="300" y2="610" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <line x1="10" y1="310" x2="590" y2="310" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 6"/>
  <foreignObject x="108.5" y="9.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{lattia}$</div></foreignObject>
  <line x1="40" y1="200" x2="260" y2="200" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="40" y1="200" x2="30" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="56" y1="200" x2="46" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="72" y1="200" x2="62" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="88" y1="200" x2="78" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="104" y1="200" x2="94" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="120" y1="200" x2="110" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="136" y1="200" x2="126" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="152" y1="200" x2="142" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="168" y1="200" x2="158" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="184" y1="200" x2="174" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200" y1="200" x2="190" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="216" y1="200" x2="206" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="232" y1="200" x2="222" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="248" y1="200" x2="238" y2="212" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="112" y="140" width="76" height="60" rx="3" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5"/>
  <line x1="150" y1="170" x2="150" y2="252" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M150,269 L142,251 L158,251 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="160" y="250.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{G}$</div></foreignObject>
  <line x1="168" y1="200" x2="168" y2="118" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M168,101 L176,119 L160,119 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="178" y="90.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{N}$</div></foreignObject>
  <foreignObject x="415" y="9.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{rinne}$</div></foreignObject>
  <line x1="316" y1="262" x2="559" y2="148.5" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="316" y1="262" x2="306" y2="274" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="330.5" y1="255" x2="320.5" y2="267" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="345" y1="248.5" x2="335" y2="260.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="359.5" y1="241.5" x2="349.5" y2="253.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="374" y1="235" x2="364" y2="247" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="388.5" y1="228" x2="378.5" y2="240" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="403" y1="221.5" x2="393" y2="233.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="417.5" y1="214.5" x2="407.5" y2="226.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="432" y1="208" x2="422" y2="220" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="446.5" y1="201" x2="436.5" y2="213" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="461" y1="194.5" x2="451" y2="206.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="475.5" y1="187.5" x2="465.5" y2="199.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="490" y1="181" x2="480" y2="193" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="504.5" y1="174" x2="494.5" y2="186" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="519" y1="167.5" x2="509" y2="179.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="533.5" y1="160.5" x2="523.5" y2="172.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="548" y1="154" x2="538" y2="166" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M401.2,222.3 L466.4,191.8 L441.1,137.5 L375.8,167.9 Z" fill="#f1dfb5" stroke="#a97a35" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="421" y1="180" x2="421" y2="262" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M421,279 L413,261 L429,261 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="431" y="268.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{G}$</div></foreignObject>
  <line x1="421" y1="213" x2="390.5" y2="147" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M383,131.5 L398,144.5 L383.5,151.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="357" y="111" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{N}$</div></foreignObject>
  <line x1="448.5" y1="200.5" x2="471" y2="190" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M486,182.5 L473.5,197.5 L466.5,183 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="473.5" y="190" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{F}_{\mu}$</div></foreignObject>
  <foreignObject x="108.5" y="319.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{lamppu}$</div></foreignObject>
  <line x1="70" y1="360" x2="230" y2="360" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <line x1="70" y1="360" x2="60" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="86" y1="360" x2="76" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="102" y1="360" x2="92" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="118" y1="360" x2="108" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="134" y1="360" x2="124" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="150" y1="360" x2="140" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="166" y1="360" x2="156" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="182" y1="360" x2="172" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="198" y1="360" x2="188" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="214" y1="360" x2="204" y2="348" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="150" y1="360" x2="150" y2="450" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M124,480 L176,480 L163,450 L137,450 Z" fill="#e9c98a" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="150" y1="468" x2="150" y2="539" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M150,556 L142,538 L158,538 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="162" y="537.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{G}$</div></foreignObject>
  <line x1="150" y1="450" x2="150" y2="379" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M150,362 L158,380 L142,380 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="162" y="367.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{T}$</div></foreignObject>
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
  <circle cx="505" cy="495" r="6" fill="#1f2933"/>
  <line x1="505" y1="495" x2="505" y2="412" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M505,395 L513,413 L497,413 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="503.5" y="392.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{F}_\text{noste}$</div></foreignObject>
  <line x1="513" y1="495" x2="513" y2="518" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M513,535 L505,517 L521,517 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="521" y="518.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{G}$</div></foreignObject>
  <line x1="497" y1="495" x2="497" y2="538" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M497,555 L489,537 L505,537 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="467" y="532.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{N}$</div></foreignObject>
</svg>

Kuvassa on neljä tilannetta, joissa voimien suunnat yllättävät usein. Rinteellä tukivoima on kohtisuorassa rinnettä vastaan eikä pystysuora, ja kitka pitää laatikkoa paikallaan rinteen suuntaisesti. Kattoa vasten painuvaan heliumpalloon katto vaikuttaa alaspäin.

Voimakuvion voi piirtää kahdella tavalla, ja molemmat ovat oikein. **Kappalemallissa** kappale piirretään muotoineen, ja jokainen voima lähtee vaikutuskohdastaan: paino keskipisteestä, tukivoima ja kitka kosketuspinnasta ja jännitysvoima narun kiinnityskohdasta. **Pistemallissa** kappale on piste, ja kaikki voimat lähtevät siitä. Pistemalli riittää, kun kappaleen pyöriminen ei ole tärkeää. Noudata tehtävän mallia.

<svg data-fig="malli" viewBox="0 0 600 320" role="img" aria-label="Pistemallin voimakuvio samasta laatikosta kuin edellä: kaikki neljä voimaa lähtevät yhdestä pisteestä. Paino G alas, tukivoima N ylös ja painoa lyhyempi, narun jännitysvoima T vinosti ylös oikealle ja kitkavoima vasemmalle. Nurkassa koordinaattiakselit: x oikealle ja y ylös." style="max-width:100%;font-size:24px">
  <circle cx="300" cy="150" r="7" fill="#1f2933"/>
  <line x1="300" y1="150" x2="300" y2="246" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M300,263 L292,245 L308,245 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="310" y="244.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{G}$</div></foreignObject>
  <line x1="300" y1="150" x2="300" y2="83" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M300,66 L308,84 L292,84 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="310" y="55.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{N}$</div></foreignObject>
  <line x1="300" y1="150" x2="335" y2="130" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M350,121 L338.5,137.5 L330,123 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="360.5" y="95" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{T}$</div></foreignObject>
  <line x1="300" y1="150" x2="282.5" y2="150" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M265.5,150 L283.5,142 L283.5,158 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="233" y="121.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{F}_{\mu}$</div></foreignObject>
  <line x1="80" y1="270" x2="117" y2="270" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M126,270 L116,274.5 L116,265.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="80" y1="270" x2="80" y2="233" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M80,224 L84.5,234 L75.5,234 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="128" y="255.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$x$</div></foreignObject>
  <foreignObject x="70" y="197.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$y$</div></foreignObject>
</svg>

Ylioppilaskokeiden arviointiohjeissa voimakuviolle on annettu tehtäväkohtaiset pisteet. Esimerkiksi kevään 2025 heliumpallotehtävässä puuttuva, ylimääräinen tai väärään suuntaan piirretty voima vei kaikki voimakuvion pisteet, ja nopeuden tai kiihtyvyyden piirtäminen pallon voimaksi samoin. Syksyn 2025 kokeessa puuttuvasta nimestä vähennettiin piste. Tarkka pisteytys vaihtelee tehtävästä toiseen, mutta joka kokeessa vaaditaan samaa: kaikki voimat, ei keksittyjä voimia, oikeat suunnat ja yksiselitteiset nimet.

## Kaava: Liikeyhtälö komponenteittain
Newtonin toinen laki koskee kokonaisvoimaa:
```latex
\Sigma\mathbf{F} = m\mathbf{a}
```
missä $\Sigma\mathbf{F}$ on kappaleeseen vaikuttavien voimien vektorisumma (N), $m$ kappaleen massa (kg) ja $\mathbf{a}$ sen kiihtyvyys (m/s²). Kun voimat eivät ole samalla suoralla, valitaan kaksi kohtisuoraa akselia ja kirjoitetaan laki kummankin akselin suuntaan erikseen:
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

<svg data-fig="komponentit" viewBox="0 0 600 300" role="img" aria-label="Voima F lähtee pisteestä vinosti ylös oikealle kulmassa alfa vaakasuoraan nähden. Katkoviivoin piirretyt komponentit: vaakasuora F x pitkin x-akselia ja pystysuora F y pitkin y-akselia. Komponentit ja voima muodostavat suorakulmaisen kolmion, jonka hypotenuusa on F. Merkinnät: F x on F kertaa kosini alfa ja F y on F kertaa sini alfa." style="max-width:100%;font-size:24px">
  <line x1="110" y1="240" x2="260" y2="135" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M274,125.5 L263.5,142 L254.5,129 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="258" y="93" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{F}$</div></foreignObject>
  <line x1="110" y1="240" x2="272" y2="240" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M261,246.5 L274,240 L261,233.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="257.5" y="247.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{F}_{x}$</div></foreignObject>
  <line x1="110" y1="240" x2="110" y2="127.5" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M116.5,138.5 L110,125.5 L103.5,138.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="69.5" y="111" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{F}_{y}$</div></foreignObject>
  <line x1="274" y1="240" x2="274" y2="125.5" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="110" y1="125.5" x2="274" y2="125.5" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <path d="M162,240 A52,52 0 0 0 152.6,210.2" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="174" y="207.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="390" y="105.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F_x = F\cos\alpha$</div></foreignObject>
  <foreignObject x="390" y="155.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F_y = F\sin\alpha$</div></foreignObject>
</svg>

## Esimerkki
Pulkkaa, jonka massa on $12\,\text{kg}$, vedetään vaakasuoralla lumella narulla, joka on $35^\circ$:n kulmassa vaakatasoon nähden. Narun jännitysvoima on $80\,\text{N}$ ja lumen kitkavoima $30\,\text{N}$. Kuinka suuri on pulkan kiihtyvyys, ja kuinka suuri on lumen tukivoima?

<!-- vaihe -->

**Tunnetut ja kysytty.** $m = 12\,\text{kg}$, $T = 80\,\text{N}$, $\alpha = 35^\circ$, $F_\mu = 30\,\text{N}$ ja $g = 9{,}81\,\text{m/s}^2$. Kysytään kiihtyvyyttä $a$ ja tukivoimaa $N$.

<!-- vaihe -->

**Periaate.** Valitaan kappaleeksi pulkka. Siihen vaikuttavat Maa (paino), lumi (tukivoima ja kitka) ja naru (jännitysvoima). Newtonin toinen laki kirjoitetaan kahteen suuntaan: vaakasuunnassa pulkka kiihtyy, pystysuunnassa se pysyy lumen pinnalla, joten $a_y = 0$.

<!-- vaihe -->

**Voimakuvio.** Pulkka piirretään pisteenä. Akselit valitaan niin, että $x$ osoittaa liikkeen suuntaan ja $y$ ylös. Narun voima jaetaan komponentteihin $T_x = T\cos\alpha$ ja $T_y = T\sin\alpha$, jotka on piirretty katkoviivalla.

<svg data-fig="esimerkki" viewBox="0 0 600 360" role="img" aria-label="Pulkan voimakuvio pistemallina. Paino G alas, lumen tukivoima N ylös ja painoa lyhyempi, narun jännitysvoima T vinosti ylös oikealle kulmassa 35 astetta, sen komponentit katkoviivoin, ja lumen kitkavoima vasemmalle. Nurkassa akselit: x oikealle eli liikkeen suuntaan ja y ylös." style="max-width:100%;font-size:24px">
  <circle cx="290" cy="180" r="7" fill="#1f2933"/>
  <line x1="290" y1="180" x2="290" y2="298.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M290,315.5 L282,297.5 L298,297.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="300" y="297" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{G}$</div></foreignObject>
  <line x1="290" y1="180" x2="290" y2="114.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M290,97.5 L298,115.5 L282,115.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="302" y="89" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{N}$</div></foreignObject>
  <line x1="290" y1="180" x2="351.5" y2="137" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M365.5,127 L355.5,144 L346,131 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="371.5" y="102.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{T}$</div></foreignObject>
  <line x1="290" y1="180" x2="272.5" y2="180" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M255.5,180 L273.5,172 L273.5,188 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="223" y="149.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{F}_{\mu}$</div></foreignObject>
  <line x1="290" y1="180" x2="363.5" y2="180" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M352.5,186.5 L365.5,180 L352.5,173.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="349" y="189.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{T}_{x}$</div></foreignObject>
  <line x1="290" y1="180" x2="290" y2="129" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M296.5,140 L290,127 L283.5,140" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="245.5" y="116.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\mathbf{T}_{y}$</div></foreignObject>
  <path d="M330,180 A40,40 0 0 0 322.8,157.1" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round"/>
  <foreignObject x="338" y="151.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$35^\circ$</div></foreignObject>
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

**Tulos.** Kiihtyvyys on $a \approx 3{,}0\,\text{m/s}^2$ ja tukivoima $N \approx 72\,\text{N}$, kahden merkitsevän numeron tarkkuudella kuten lähtötiedot $80\,\text{N}$, $30\,\text{N}$ ja $12\,\text{kg}$.

<!-- vaihe -->

**Järkevyys.** Pulkan paino on $mg \approx 118\,\text{N}$. Tukivoima $72\,\text{N}$ on sitä pienempi, koska narun pystykomponentti $T_y \approx 46\,\text{N}$ kannattelee osan painosta, ja $72\,\text{N} + 46\,\text{N} \approx 118\,\text{N}$. Ilman kitkaa kiihtyvyys olisi $65{,}5\,\text{N} : 12\,\text{kg} \approx 5{,}5\,\text{m/s}^2$, joten kitka pienentää sitä, kuten pitääkin.

## Yleinen virhekäsitys
Liikkuvaan kappaleeseen ei tarvitse vaikuttaa voimaa liikkeen suuntaan. Liukuvaan laatikkoon vaikuttavat vain paino, tukivoima ja kitka, eikä "liikkeen voimaa" ole: ei ole mitään kappaletta, joka sitä aiheuttaisi. Toinen yleinen virhe on pitää tukivoimaa aina yhtä suurena kuin paino. Tukivoima on juuri niin suuri, kuin tilanne vaatii: vinossa vedossa se on painoa pienempi, vinossa työnnössä suurempi ja ylöspäin kiihtyvässä hississä suurempi. Kolmas virhe on piirtää komponentit voimiksi voiman lisäksi, jolloin sama voima tulee laskuun kahteen kertaan.

## Tiivistelmä
- Voimakuviossa on vain valittu kappale ja siihen vaikuttavat voimat. Tilannekuva ja voimakuvio ovat eri kuvia.
- Jokaisella voimalla on aiheuttaja: Maa, pinta, naru, työntäjä tai ilma. Nopeus ja kiihtyvyys eivät ole voimia.
- Tukivoima on kohtisuorassa pintaa vastaan, kitka pinnan suuntainen ja jännitysvoima narun suuntainen.
- Kokonaisvoima on voimien vektorisumma, ja $\Sigma\mathbf{F} = m\mathbf{a}$ kirjoitetaan komponenteittain: $\Sigma F_x = m a_x$ ja $\Sigma F_y = m a_y$.
- Vinon voiman komponentit ovat $F\cos\alpha$ ja $F\sin\alpha$. Ne korvaavat voiman laskussa eivätkä ole uusia voimia.
