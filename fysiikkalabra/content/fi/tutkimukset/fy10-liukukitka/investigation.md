# Liukukitkakertoimen määrittäminen

> **Tutkimuskysymys:** Miten jarruttavan vaunun pysähtymismatka riippuu sen alkunopeudesta, ja kuinka suuri on jarrun ja radan välinen liukukitkakerroin?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratorion työpöydällä on pitkä vaakasuora vaunurata. Radan vasemmassa päässä on liikeanturi. Vaunu liukuu radalla oikealle jarru radan pintaa vasten, ja sen paikka on piirretty tasaisin aikavälein: välit lyhenevät tasaisesti, kunnes vaunu pysähtyy ennen radan päätä. Pöydällä olevan kannettavan tietokoneen näytöllä on laskeva suora." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy10lh-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#dfe9ef"/></linearGradient><linearGradient id="fy10lh-desk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy10lh-wall)"/>
  <rect x="0" y="440" width="1200" height="160" fill="url(#fy10lh-desk)"/>
  <line x1="0" y1="462" x2="1200" y2="458" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="484" x2="1200" y2="480" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="506" x2="1200" y2="502" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="528" x2="1200" y2="524" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="550" x2="1200" y2="546" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="572" x2="1200" y2="568" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="440" x2="1200" y2="440" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="102" y="408" width="16" height="32" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="92" y="432" width="36" height="8" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="1072" y="408" width="16" height="32" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="1062" y="432" width="36" height="8" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="60" y="392" width="1080" height="16" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="64" y1="400" x2="1136" y2="400" stroke="#8a96a3" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="1120" y="358" width="14" height="34" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="70" y="327" width="53" height="65" rx="5" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="121" cy="359.5" r="18" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="121" cy="359.5" r="8.4" fill="#1f2933"/>
  <g opacity="0.28"><rect x="220" y="324" width="110" height="46" rx="6" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/><rect x="232" y="334" width="86" height="24" rx="3" fill="#ffffff" stroke="#1971c2" stroke-width="1.5" opacity="0.7"/><rect x="261" y="368" width="28" height="24" rx="2" fill="#495057" stroke="#1f2933" stroke-width="1.5"/><circle cx="242" cy="379" r="13" fill="#1f2933"/><circle cx="242" cy="379" r="6" fill="#c4ccd4"/><circle cx="308" cy="379" r="13" fill="#1f2933"/><circle cx="308" cy="379" r="6" fill="#c4ccd4"/></g>
  <g opacity="0.28"><rect x="390" y="324" width="110" height="46" rx="6" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/><rect x="402" y="334" width="86" height="24" rx="3" fill="#ffffff" stroke="#1971c2" stroke-width="1.5" opacity="0.7"/><rect x="431" y="368" width="28" height="24" rx="2" fill="#495057" stroke="#1f2933" stroke-width="1.5"/><circle cx="412" cy="379" r="13" fill="#1f2933"/><circle cx="412" cy="379" r="6" fill="#c4ccd4"/><circle cx="478" cy="379" r="13" fill="#1f2933"/><circle cx="478" cy="379" r="6" fill="#c4ccd4"/></g>
  <g opacity="0.28"><rect x="533.5" y="324" width="110" height="46" rx="6" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/><rect x="545.5" y="334" width="86" height="24" rx="3" fill="#ffffff" stroke="#1971c2" stroke-width="1.5" opacity="0.7"/><rect x="574.5" y="368" width="28" height="24" rx="2" fill="#495057" stroke="#1f2933" stroke-width="1.5"/><circle cx="555.5" cy="379" r="13" fill="#1f2933"/><circle cx="555.5" cy="379" r="6" fill="#c4ccd4"/><circle cx="621.5" cy="379" r="13" fill="#1f2933"/><circle cx="621.5" cy="379" r="6" fill="#c4ccd4"/></g>
  <g opacity="0.28"><rect x="651" y="324" width="110" height="46" rx="6" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/><rect x="663" y="334" width="86" height="24" rx="3" fill="#ffffff" stroke="#1971c2" stroke-width="1.5" opacity="0.7"/><rect x="692" y="368" width="28" height="24" rx="2" fill="#495057" stroke="#1f2933" stroke-width="1.5"/><circle cx="673" cy="379" r="13" fill="#1f2933"/><circle cx="673" cy="379" r="6" fill="#c4ccd4"/><circle cx="739" cy="379" r="13" fill="#1f2933"/><circle cx="739" cy="379" r="6" fill="#c4ccd4"/></g>
  <g opacity="0.28"><rect x="742.5" y="324" width="110" height="46" rx="6" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/><rect x="754.5" y="334" width="86" height="24" rx="3" fill="#ffffff" stroke="#1971c2" stroke-width="1.5" opacity="0.7"/><rect x="783.5" y="368" width="28" height="24" rx="2" fill="#495057" stroke="#1f2933" stroke-width="1.5"/><circle cx="764.5" cy="379" r="13" fill="#1f2933"/><circle cx="764.5" cy="379" r="6" fill="#c4ccd4"/><circle cx="830.5" cy="379" r="13" fill="#1f2933"/><circle cx="830.5" cy="379" r="6" fill="#c4ccd4"/></g>
  <g opacity="0.28"><rect x="808" y="324" width="110" height="46" rx="6" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/><rect x="820" y="334" width="86" height="24" rx="3" fill="#ffffff" stroke="#1971c2" stroke-width="1.5" opacity="0.7"/><rect x="849" y="368" width="28" height="24" rx="2" fill="#495057" stroke="#1f2933" stroke-width="1.5"/><circle cx="830" cy="379" r="13" fill="#1f2933"/><circle cx="830" cy="379" r="6" fill="#c4ccd4"/><circle cx="896" cy="379" r="13" fill="#1f2933"/><circle cx="896" cy="379" r="6" fill="#c4ccd4"/></g>
  <g opacity="0.28"><rect x="847" y="324" width="110" height="46" rx="6" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/><rect x="859" y="334" width="86" height="24" rx="3" fill="#ffffff" stroke="#1971c2" stroke-width="1.5" opacity="0.7"/><rect x="888" y="368" width="28" height="24" rx="2" fill="#495057" stroke="#1f2933" stroke-width="1.5"/><circle cx="869" cy="379" r="13" fill="#1f2933"/><circle cx="869" cy="379" r="6" fill="#c4ccd4"/><circle cx="935" cy="379" r="13" fill="#1f2933"/><circle cx="935" cy="379" r="6" fill="#c4ccd4"/></g>
  <g opacity="1.0"><rect x="860" y="324" width="110" height="46" rx="6" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/><rect x="872" y="334" width="86" height="24" rx="3" fill="#ffffff" stroke="#1971c2" stroke-width="1.5" opacity="0.7"/><rect x="901" y="368" width="28" height="24" rx="2" fill="#495057" stroke="#1f2933" stroke-width="1.5"/><circle cx="882" cy="379" r="13" fill="#1f2933"/><circle cx="882" cy="379" r="6" fill="#c4ccd4"/><circle cx="948" cy="379" r="13" fill="#1f2933"/><circle cx="948" cy="379" r="6" fill="#c4ccd4"/></g>
  <path d="M840,560 L1100,560 L1130,586 L810,586 Z" fill="#6c757d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="860" y="452" width="220" height="108" rx="6" fill="#1f2933" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="872" y="462" width="196" height="88" fill="#ffffff"/>
  <line x1="886" y1="540" x2="1056" y2="540" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="886" y1="540" x2="886" y2="470" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="886" y1="540" x2="904" y2="486" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <line x1="904" y1="486" x2="1014" y2="540" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <line x1="1014" y1="540" x2="1056" y2="540" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
</svg>

Kun auton kuljettaja jarruttaa lukkojarruin, auto liukuu vielä matkan ennen kuin pysähtyy, ja matka on sitä pidempi, mitä suurempi vauhti oli. Tässä tutkimuksessa jarrutat vaunua radalla eri alkunopeuksilla, mittaat liikeanturilla, kuinka pitkälle se liukuu, ja määrität mittauksistasi liukukitkakertoimen. Mittaa, piirrä ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** miten pysähtymismatka riippuu alkunopeudesta ja kuinka suuri on jarrun ja radan välinen liukukitkakerroin eli liikekitkakerroin epävarmuuksineen. Kerroin määritetään graafisesti, energiaperiaatteen avulla.

**Päätät itse:** mitkä suureet mittaat ja miten luet ne liikeanturin tuloksista, alkunopeudet ja niiden määrän, toistojen määrän, kuvaajan akselit perusteluineen sekä tavan, jolla arvioit tuloksen epävarmuuden. Ohjatussa ja osittain ohjatussa työtavassa sivu antaa näihin tukea, itsenäisessä työtavassa perustelet valintasi itse.

::: tuki I
**Itsenäinen työtapa.** Laajennus, kitkakertoimen määrittäminen nopeuden kuvaajasta, kuuluu työhösi: vertaa lopuksi kahdella menetelmällä saatuja tuloksia.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Jos vaunun alkunopeus kaksinkertaistuu, kuinka monikertaiseksi arvelet pysähtymismatkan kasvavan?
2. Mihin vaunun liike-energia joutuu jarrutuksen aikana?
3. Muuttuuko pysähtymismatka, jos vaunuun lisätään kuormaa mutta alkunopeus pysyy samana?
4. Mikä voisi vääristää tulosta niin, että kaikki mittaukset virheellisesti antavat liian suuren tai liian pienen kitkakertoimen?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Tutkimuskysymyksestä mitattaviksi suureiksi

Kitkakerrointa ei voi lukea mittarista. Ennen kuin luet eteenpäin, kirjaa:

1. Mitkä suureet sinun on mitattava jokaisesta jarrutuksesta, jotta voit laskea kitkavoiman tekemän työn ja vaunun liike-energian muutoksen?
2. Mistä hetkestä alkaen jarrutus lasketaan, kun vaunu lähtee liikkeelle käden työnnöstä?
3. Mitä muutat, mitä mittaat ja mitä pidät vakiona?

## Teoriaa lyhyesti

Kun vaunu liukuu vaakasuoralla radalla jarru radan pintaa vasten, siihen vaikuttavat paino $\overline{G}$, radan tukivoima $\overline{N}$ ja liikettä vastustava liikekitka $\overline{F}_\mu$. Vaakasuoralla radalla pystysuorat voimat kumoavat toisensa, joten tukivoima on yhtä suuri kuin paino, $N = G = mg$. Liikekitkan suuruus on

```latex
F_\mu = \mu N
```

missä $\mu$ on liikekitkakerroin, jota tässä työssä kutsutaan myös liukukitkakertoimeksi. Kerroin on yksikötön. Malli olettaa, että jarru painuu rataa vasten koko vaunun painolla. Jos pyörät kantavat osan painosta ja jarrua painaa esimerkiksi jousi, mittaamasi luku on kitkavoiman ja painon suhde, joka kuvaa koko vaunun jarrutusta, eikä pelkästään jarrun ja radan pintojen kitkakerroin. [[apua:fy4-6|Kitka ja kitkakerroin]]

<svg data-fig="forces" viewBox="0 0 600 330" role="img" aria-label="Voimakuvio: radalla oikealle liukuva ja hidastuva vaunu suorakulmiona. Paino G osoittaa keskipisteestä alas. Radan tukivoima N osoittaa alapinnasta ylös, ja se on yhtä pitkä kuin paino. Liikekitka F myy osoittaa alapinnan takakulmasta vasemmalle eli liikettä vastaan, ja se on paljon lyhyempi kuin paino. Kappaleen yläpuolella sininen nopeusnuoli v osoittaa oikealle ja oranssi kiihtyvyysnuoli a vasemmalle." style="max-width:100%;font-size:24px">
  <line x1="150" y1="192" x2="510" y2="192" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <rect x="265" y="128" width="130" height="64" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="330" y1="160" x2="330" y2="246" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M330,263 L322,245 L338,245 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="337.5" y="242.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="364" y1="192" x2="364" y2="106" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M364,89 L372,107 L356,107 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="371.5" y="82.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="265" y1="192" x2="251" y2="192" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M234,192 L252,184 L252,200 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="205.5" y="199.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <line x1="417" y1="124" x2="485" y2="124" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M474,130.5 L487,124 L474,117.5" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="492.5" y="105.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="243" y1="124" x2="195" y2="124" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M206,117.5 L193,124 L206,130.5" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="154.5" y="105.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
</svg>

Paino ja tukivoima ovat kohtisuorassa liikettä vastaan, joten ne eivät tee työtä. Kitka vastustaa liikettä ja tekee negatiivista työtä, joka pienentää vaunun liike-energiaa, kunnes vaunu pysähtyy. Energiaperiaatteen mukaan kitkan tekemä työ on yhtä suuri kuin liike-energian muutos. [[apua:fy4-8|Työ ja energiaperiaate]]

::: tuki O OO
Tarkista kirjauksesi tästä. Jarrutus alkaa hetkestä, jolloin käsi on irronnut vaunusta. Silloin vaunun nopeus on **alkunopeus** $v_0$, ja siitä kohdasta pysähtymiskohtaan vaunu kulkee **pysähtymismatkan** $s$. Molemmat luetaan liikeanturin tuloksista: $v_0$ nopeuden kuvaajasta ja $s$ paikan kuvaajasta, aina vaunun samasta kohdasta mitattuna.

<svg data-fig="setup" viewBox="0 0 600 320" role="img" aria-label="Kaaviokuva. Vaakasuoran vaunuradan vasemmassa päässä on liikeanturi. Vaunu on piirretty kahteen kohtaan. Vasemmalla, himmeämpänä, vaunu on kohdassa, jossa työntö on loppunut ja vaunun nopeus on alkunopeus v nolla, oikealle. Oikealla vaunu on pysähtynyt. Kohtien välinen matka, mitattuna vaunun samasta kohdasta, on pysähtymismatka s. Vaunun jarru painuu radan pintaa vasten." style="max-width:100%;font-size:24px">
  <rect x="20" y="210" width="560" height="12" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="26" y="161.5" width="39.5" height="48.5" rx="5" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="63.5" cy="185.5" r="13.5" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <circle cx="63.5" cy="185.5" r="6.3" fill="#1f2933"/>
  <foreignObject x="22" y="237.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{liikeanturi}$</div></foreignObject>
  <g opacity="0.45"><rect x="130" y="142" width="110" height="46" rx="6" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/><rect x="142" y="152" width="86" height="24" rx="3" fill="#ffffff" stroke="#1971c2" stroke-width="1.5" opacity="0.7"/><rect x="171" y="186" width="28" height="24" rx="2" fill="#495057" stroke="#1f2933" stroke-width="1.5"/><circle cx="152" cy="197" r="13" fill="#1f2933"/><circle cx="152" cy="197" r="6" fill="#c4ccd4"/><circle cx="218" cy="197" r="13" fill="#1f2933"/><circle cx="218" cy="197" r="6" fill="#c4ccd4"/></g>
  <g opacity="1.0"><rect x="400" y="142" width="110" height="46" rx="6" fill="#d0e6fb" stroke="#1f2933" stroke-width="2.5"/><rect x="412" y="152" width="86" height="24" rx="3" fill="#ffffff" stroke="#1971c2" stroke-width="1.5" opacity="0.7"/><rect x="441" y="186" width="28" height="24" rx="2" fill="#495057" stroke="#1f2933" stroke-width="1.5"/><circle cx="422" cy="197" r="13" fill="#1f2933"/><circle cx="422" cy="197" r="6" fill="#c4ccd4"/><circle cx="488" cy="197" r="13" fill="#1f2933"/><circle cx="488" cy="197" r="6" fill="#c4ccd4"/></g>
  <line x1="150" y1="110" x2="228" y2="110" stroke="#1971c2" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M217,116.5 L230,110 L217,103.5" fill="none" stroke="#1971c2" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="229.5" y="95.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}_0$</div></foreignObject>
  <foreignObject x="432.5" y="95.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$v = 0$</div></foreignObject>
  <line x1="240" y1="146" x2="240" y2="282" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="510" y1="146" x2="510" y2="282" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="240" y1="276" x2="510" y2="276" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="240" y1="266" x2="240" y2="286" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="510" y1="266" x2="510" y2="286" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="365" y="283.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$s$</div></foreignObject>
  <foreignObject x="420" y="229.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{jarru}$</div></foreignObject>
  <line x1="455" y1="232" x2="455" y2="223" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
</svg>

Kitkavoima on vakio ja liikettä vastaan, joten se tekee matkalla $s$ työn $W = -F_\mu s = -\mu m g s$. Liike-energia muuttuu arvosta $\tfrac{1}{2}mv_0^2$ nollaan. Energiaperiaatteesta saadaan

```latex
\begin{aligned}
-\mu m g s &= 0 - \tfrac{1}{2} m v_0^2 \\
\tfrac{1}{2} v_0^2 &= \mu g \cdot s
\end{aligned}
```

Massa supistuu pois. Malli ennustaa, että puolet alkunopeuden neliöstä on suoraan verrannollinen pysähtymismatkaan, joten kuvaaja $\tfrac{1}{2}v_0^2$ pysähtymismatkan $s$ funktiona on origon kautta kulkeva suora, jonka kulmakerroin on $\mu g$. Kitkakerroin saadaan kulmakertoimesta $k$: $\mu = \dfrac{k}{g}$. Pätevätkö malli ja sen oletukset, selviää vasta mittaamalla: jos kitka riippuu vauhdista, pisteet poikkeavat suoralta. Radan tasainen kallistus sen sijaan muuttaa vain hidastuvuutta ja siis kulmakerrointa: suora kulkee yhä origon kautta, joten kallistusta ei näe kuvaajasta. Se on tarkistettava vesivaa'alla tai jarruttamalla vaunua radalla kumpaankin suuntaan.

<svg data-fig="model" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja: puolet alkunopeuden neliöstä pysähtymismatkan s funktiona mallin mukaan. Kuvaaja on origon kautta kulkeva suora. Suoralle on merkitty kaksi pistettä ja niiden välinen muutos vaakasuunnassa delta s ja pystysuunnassa. Kulmakerroin on myy kertaa g. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="99" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="291" x2="100" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,44 L106,57 L94,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="70" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$s$</div></foreignObject>
  <foreignObject x="90" y="13.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\tfrac{1}{2}v_0^2$</div></foreignObject>
  <polyline points="100,290 451.5,102" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="211" y1="230.5" x2="396" y2="230.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="396" y1="230.5" x2="396" y2="131.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="287" y="236" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\Delta s$</div></foreignObject>
  <foreignObject x="406" y="166.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\Delta\!\left(\tfrac{1}{2}v_0^2\right)$</div></foreignObject>
  <foreignObject x="122" y="86.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kulmakerroin } \mu g$</div></foreignObject>
</svg>
:::

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, mitä muutat, mitä mittaat ja mitä pidät vakiona.

::: tuki O
**Ohjattu.** Muutat vaunun alkunopeutta $v_0$ työntämällä vaunua eri voimakkuudella. Mittaat liikeanturilla jokaisesta jarrutuksesta alkunopeuden $v_0$ ja pysähtymismatkan $s$. Vakiona pidät vaunun, sen kuorman, jarrun säädön ja radan. Tee ainakin kuusi jarrutusta niin, että alkunopeudet jakautuvat tasaisesti pienimmästä suurimpaan.
:::

::: tuki OO
**Osittain ohjattu.** Muuttuja on alkunopeus. Päätä tarkemmin, kuinka monta jarrutusta teet, millä alkunopeuksilla ja miten luet alkunopeuden ja pysähtymismatkan anturin tuloksista. Kirjaa päätöksesi perusteluineen.
:::

::: tuki O OO
Mieti ainakin näitä:

- Miten tarkistat, että rata on vaakasuorassa? Mitä tulokselle tapahtuisi, jos rata olisi hieman kallellaan liikkeen suuntaan tai sitä vastaan?
- Kuinka suurilla nopeuksilla vaunu pysähtyy vielä radalle, ja kuinka lähelle anturia se saa tulla, jotta anturi mittaa luotettavasti? Tarkista anturin lähin mittausetäisyys sen ohjeesta.
- Miten varmistat, että luet alkunopeuden vasta, kun käsi on irronnut vaunusta?
:::

::: tuki O
**Vihje lukemiseen.** Nopeuden kuvaajassa työntö näkyy nousevana osana ja jarrutus sen jälkeen laskevana osana. Huippu voi vielä sisältää työnnön tai olla yksittäinen kohinapiikki, joten älä lue alkunopeutta suoraan huipusta. Valitse hetki heti huipun jälkeen, kun laskeva osa on jo suora, ja lue siltä hetkeltä sekä alkunopeus $v_0$ että vaunun paikka $x_0$. Tasoita nopeus ohjelmassa tai laske muutaman lukeman keskiarvo valitun hetken ympäriltä. Lue sitten paikka, jossa vaunu on pysähtynyt. Pysähtymismatka on näiden paikkojen erotus.
:::

## Mittaa

Kirjaa jokaisesta jarrutuksesta alkuperäiset lukemat taulukkoon heti mittauksen aikana. Laskemasi suureet saavat omat sarakkeensa luettujen oikealle puolelle. Tallenna myös anturin mittaussarjat, jotta voit tarkistaa lukemasi myöhemmin.

::: tuki O
Voit käyttää esimerkiksi tällaista taulukkoa:

| $v_0\ (\text{m/s})$ | $x_0\ (\text{m})$ | $x_1\ (\text{m})$ | $s = x_1 - x_0\ (\text{m})$ | $\tfrac{1}{2}v_0^2\ (\text{m}^2/\text{s}^2)$ |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

Tässä $x_0$ on vaunun paikka jarrutuksen alkaessa ja $x_1$ paikka, jossa vaunu on pysähtynyt. Tee jarrutukset satunnaisessa järjestyksessä, ettei jarrun vähittäinen lämpeneminen tai kuluminen näy kuvaajassa järjestelmällisenä vinoumana.
:::

Muista mittausepävarmuus: arvioi, kuinka tarkasti pystyt lukemaan alkunopeuden ja pysähtymismatkan, ja kirjaa arviot ylös. Anturin nopeuslukemissa on kohinaa, joka näkyy kuvaajan värinänä. [[apua:fy1-3|Mittausepävarmuuden arvioiminen]]

## Käsittele tulokset

Piirrä mittaustuloksista kuvaaja, josta liukukitkakerroin saadaan kulmakertoimen avulla. Merkitse akseleille suureet ja yksiköt. Piirrä mittauspisteet, älä yhdistä niitä murtoviivalla, ja sovita pisteisiin suora. [[apua:fy1-4|Suoran sovittaminen ja kulmakertoimen tulkinta]]

::: tuki O
Valitse pystyakselille $\tfrac{1}{2}v_0^2$ ja vaaka-akselille pysähtymismatka $s$.
:::

Kirjoita sovitetun suoran yhtälö ja vastaa:

1. Ovatko pisteet suoralla? Jos eivät, millä alkunopeuksilla ne poikkeavat, ja mihin suuntaan?
2. Miten saat kulmakertoimesta $\mu$:n?
3. Kulkeeko suora origon kautta? Jos ei, mistä vakiotermi voi johtua?

::: tuki O OO
**Miksi juuri nämä akselit?** Malli $\tfrac{1}{2}v_0^2 = \mu g \cdot s$ on suoran yhtälö $y = kx$, kun pystyakselille valitaan $\tfrac{1}{2}v_0^2$ ja vaaka-akselille $s$. Kulmakertoimen yksikkö on $\text{m/s}^2$, ja kulmakerroin on $\mu g$. Jos pystyakselille valitaan $v_0^2$, kulmakerroin on $2\mu g$. Jos akselit vaihdetaan keskenään, kulmakerroin on käänteisluku. Pysähtymismatkan kuvaaja pelkän alkunopeuden $v_0$ funktiona ei ole suora vaan kaartuu ylöspäin. Siitä on vaikea nähdä, noudattavatko pisteet mallia, ja kitkakertoimen saaminen siitä on hankalaa. Jos suora ei kulje origon kautta, syynä voi olla esimerkiksi se, että alkunopeus on luettu ennen kuin työntö on loppunut tai eri hetkeltä kuin paikka $x_0$. Radan tasainen kallistus ei tee vakiotermiä: se muuttaa vain kulmakerrointa: mitattu kitkakerroin muuttuu noin $0{,}02$ asteen kallistusta kohti, joten sitä ei näe kuvaajasta.
:::

Kuvaajan sovitukseen käytä Graphical Analysis Pro -ohjelmaa. Ruukkilabran ohjeet: [[ohje:tvt-suoran-sovitus|Suoran sovittaminen]], [[ohje:tvt-kulmakerroin|Kulmakertoimen tulkinta]] ja [[ohje:tvt-taulukkolaskenta|Taulukko ja lasketut sarakkeet]].

## Epävarmuus ja luotettavuus

Ilmoita liukukitkakerroin muodossa $\mu \pm \Delta\mu$ ja perustele, miten arvioit epävarmuuden $\Delta\mu$.

::: tuki O OO
Kulmakertoimen epävarmuuden $\Delta k$ voit arvioida jommallakummalla tavalla:

- **Sovitusohjelman keskivirhe.** Monet ohjelmat ilmoittavat kulmakertoimen keskivirheen. Käytä sitä epävarmuutena $\Delta k$.
- **Jyrkin ja loivin suora.** Piirrä jyrkin ja loivin suora, jotka vielä sopivat pisteisiin niiden epävarmuuksien rajoissa. Määritä niiden kulmakertoimet $k_\text{max}$ ja $k_\text{min}$ ja arvioi epävarmuus vaihteluvälin puolikkaana: $\Delta k = \dfrac{k_\text{max} - k_\text{min}}{2}$.

Koska $\mu = \dfrac{k}{g}$ ja putoamiskiihtyvyys tunnetaan tarkasti, kitkakertoimen suhteellinen epävarmuus on sama kuin kulmakertoimen: $\dfrac{\Delta\mu}{\mu} = \dfrac{\Delta k}{k}$. Pyöristä $\Delta\mu$ yhteen merkitsevään numeroon ja $\mu$ samaan desimaaliin.

Huomaa, että nopeuden lukemisen epävarmuus kasvaa neliöön korotettaessa: jos nopeuden epävarmuus on $\Delta v_0$, suureen $\tfrac{1}{2}v_0^2$ epävarmuus on noin $v_0 \Delta v_0$, eli se on suurimmilla nopeuksilla suurin.
:::

Pohdi sitten luotettavuutta konkreettisesti: mitkä olivat suurimmat epävarmuuden lähteet, olivatko ne satunnaisia vai systemaattisia, ja mihin suuntaan systemaattiset virheet olisivat muuttaneet tulosta? Pohdi ainakin radan kallistusta, jarrun painumista radan pintaa vasten ja pyörien omaa vierimisvastusta. Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Miten pysähtymismatka riippuu alkunopeudesta, ja noudattavatko mittauksesi energiaperiaatteen mallia koko mittausalueella? Kuinka suuri liukukitkakerroin on, ja mihin vaunun liike-energia muuttui? Viittaa kuvaajaan, esimerkiksi "kuvaajasta 1 nähdään, että …". Vertaa tulosta ennusteeseesi: mikä osui oikeaan ja mikä ei?

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla ja käy läpi sen kaikki osat. Kuvaajien ja tulosten esittämisessä auttaa ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tausta ja teoria:** voimakuvio, kitkan tekemä työ ja energiaperiaate sekä miksi valitsit juuri nämä akselit.
- **Koejärjestely ja menetelmä:** miten varmistit radan vaakasuoruuden ja miten luit alkunopeuden ja pysähtymismatkan anturin tuloksista. Liitä esimerkki yhden jarrutuksen nopeuden kuvaajasta.
- **Mittaustulokset:** luetut suureet omissa sarakkeissaan ja johdetut suureet niiden oikealla puolella.
- **Tulos:** $\mu \pm \Delta\mu$ oikein pyöristettynä.
- **Luotettavuus:** konkreettiset epävarmuuden lähteet ja niiden vaikutuksen suunta.

## Laajennus: kitkakerroin nopeuden kuvaajasta

Kitkakertoimen voi määrittää samoista mittauksista myös toisella tavalla. Jarrutuksen aikana vaunuun vaikuttava kokonaisvoima on kitka, joten Newtonin toisen lain mukaan $ma = \mu mg$ ja vaunun hidastuvuuden suuruus on

```latex
a = \mu g
```

Jos kitkavoima on vakio, hidastuvuuskin on vakio, ja nopeuden kuvaaja jarrutuksen aikana on laskeva suora, jonka kulmakerroin on $-\mu g$. [[apua:fy4-4|Newtonin toinen laki]] [[apua:fy4-2|Kiihtyvyys nopeuden kuvaajasta]]

<svg data-fig="velocity" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja: vaunun nopeus v ajan t funktiona jarrutuksen aikana mallin mukaan. Nopeus pienenee alkunopeudesta v nolla tasaisesti nollaan, joten kuvaaja on laskeva suora. Suoran kulmakerroin on miinus myy kertaa g, ja hidastuvuuden suuruus on a yhtä kuin myy kertaa g. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="99" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="291" x2="100" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,44 L106,57 L94,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="70" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="90" y="13.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v$</div></foreignObject>
  <polyline points="100,103 396,290" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="93" y1="103" x2="100" y2="103" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="88.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$v_0$</div></foreignObject>
  <foreignObject x="342" y="299.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{pysähtyy}$</div></foreignObject>
  <line x1="174" y1="150" x2="322" y2="150" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="322" y1="150" x2="322" y2="243" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="231.5" y="115" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\Delta t$</div></foreignObject>
  <foreignObject x="332" y="182" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\Delta v$</div></foreignObject>
  <foreignObject x="292.5" y="72" width="233" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kulmakerroin } \dfrac{\Delta v}{\Delta t} = -\mu g$</div></foreignObject>
</svg>

Sovita suora kunkin jarrutuksen nopeuden kuvaajan laskevaan osaan ja määritä siitä hidastuvuus ja kitkakerroin. Laske jarrutusten tuloksista keskiarvo ja arvioi sen epävarmuus. Onko hidastuvuus sama suurilla ja pienillä nopeuksilla? Vertaa tulosta päämenetelmän kitkakertoimeen epävarmuuksineen: mahtuvatko tulokset toistensa epävarmuusväleihin? Päällekkäiset välit tarkoittavat, että tulokset ovat sopusoinnussa, eivät sitä, että ne on todistettu samoiksi. Kumpi menetelmä vaikutti luotettavammalta, ja miksi?

::: tuki O OO
**Vihjeitä.** Valitse sovitusväliksi vain se osa kuvaajasta, jossa käsi on jo irronnut eikä vaunu ole vielä pysähtynyt. Aivan pysähtymisen lähellä anturin nopeuslukemat ovat usein epätarkkoja, joten jätä loppu pois, jos se poikkeaa suorasta. Jos laskeva osa kaartuu, kitka ei ole vakio, ja se kannattaa kertoa raportissa.
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi kuvaajaan ja mittaustuloksiin vai siihen, mitä odotit?
- Mitä tekisit toisin, jos aloittaisit alusta?
