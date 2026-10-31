# Lämmön johtuminen lämpökameralla

> **Tutkimuskysymys:** Mikä tutkittavista materiaaleista johtaa lämpöä tehokkaimmin, ja miten sen voi päätellä lämpökameralla mitatuista lämpötiloista?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: pöydällä on kattila kuumaa vettä, ja sen päällä on lämpöä eristävä kansi. Kannen läpi nousee viisi samanmuotoista sauvaa, jotka on päällystetty samanlaisella tummalla mattapintaisella teipillä; sauvojen yläpäistä näkyy, että ne ovat eri materiaaleista: kuparia, alumiinia, terästä, puuta ja muovia. Kattilan reunalta nousee höyryä. Kolmijalan päällä oleva lämpökamera kuvaa sauvoja sivulta, ja pöydällä on sekuntikello." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy10lh-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#dfe9ef"/></linearGradient><linearGradient id="fy10lh-table" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy10lh-pot" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8a96a3"/><stop offset="0.3" stop-color="#ffffff"/><stop offset="0.65" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy10lh-wall)"/>
  <rect x="0" y="470" width="1200" height="130" fill="url(#fy10lh-table)"/>
  <line x1="0" y1="492" x2="1200" y2="488" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="516" x2="1200" y2="512" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="540" x2="1200" y2="536" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="564" x2="1200" y2="560" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="470" x2="1200" y2="470" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="330" y="330" width="380" height="140" rx="8" fill="url(#fy10lh-pot)" stroke="#1f2933" stroke-width="3"/>
  <rect x="312" y="352" width="22" height="14" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="706" y="352" width="22" height="14" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="318" y="312" width="404" height="26" rx="6" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <circle cx="340" cy="325" r="2.2" fill="#c9c2b2"/>
  <circle cx="385" cy="325" r="2.2" fill="#c9c2b2"/>
  <circle cx="430" cy="325" r="2.2" fill="#c9c2b2"/>
  <circle cx="475" cy="325" r="2.2" fill="#c9c2b2"/>
  <circle cx="520" cy="325" r="2.2" fill="#c9c2b2"/>
  <circle cx="565" cy="325" r="2.2" fill="#c9c2b2"/>
  <circle cx="610" cy="325" r="2.2" fill="#c9c2b2"/>
  <circle cx="655" cy="325" r="2.2" fill="#c9c2b2"/>
  <circle cx="700" cy="325" r="2.2" fill="#c9c2b2"/>
  <path d="M336,306 q-12,-13.5 0,-26.5 t0,-26.5 t0,-26.5" fill="none" stroke="#ffc078" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <path d="M704,306 q-12,-13.5 0,-26.5 t0,-26.5 t0,-26.5" fill="none" stroke="#ffc078" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" stroke-opacity="0.75"/>
  <rect x="371" y="110" width="22" height="204" rx="3" fill="#3b4148" stroke="#1f2933" stroke-width="3"/>
  <rect x="371" y="96" width="22" height="22" rx="3" fill="#b8622d" stroke="#1f2933" stroke-width="3"/>
  <rect x="440" y="110" width="22" height="204" rx="3" fill="#3b4148" stroke="#1f2933" stroke-width="3"/>
  <rect x="440" y="96" width="22" height="22" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <rect x="509" y="110" width="22" height="204" rx="3" fill="#3b4148" stroke="#1f2933" stroke-width="3"/>
  <rect x="509" y="96" width="22" height="22" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="578" y="110" width="22" height="204" rx="3" fill="#3b4148" stroke="#1f2933" stroke-width="3"/>
  <rect x="578" y="96" width="22" height="22" rx="3" fill="#d9b26a" stroke="#1f2933" stroke-width="3"/>
  <line x1="585" y1="100" x2="587" y2="116" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="593" y1="99" x2="594" y2="115" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="647" y="110" width="22" height="204" rx="3" fill="#3b4148" stroke="#1f2933" stroke-width="3"/>
  <rect x="647" y="96" width="22" height="22" rx="3" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="163.5" y="365" width="13" height="9.5" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="167" y="374" width="5.5" height="5.5" fill="#6c757d"/>
  <circle cx="170" cy="418" r="40" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <circle cx="170" cy="418" r="32.8" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="170" y1="391" x2="170" y2="387" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="183.5" y1="394.5" x2="185.5" y2="391" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="193.5" y1="404.5" x2="197" y2="402.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="197" y1="418" x2="201" y2="418" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="193.5" y1="431.5" x2="197" y2="433.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="183.5" y1="441.5" x2="185.5" y2="445" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="170" y1="445" x2="170" y2="449" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="156.5" y1="441.5" x2="154.5" y2="445" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="146.5" y1="431.5" x2="143" y2="433.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="143" y1="418" x2="139" y2="418" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="146.5" y1="404.5" x2="143" y2="402.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="156.5" y1="394.5" x2="154.5" y2="391" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="170" y1="418" x2="195" y2="410" stroke="#c92a2a" stroke-width="2.8" stroke-linecap="round"/>
  <circle cx="170" cy="418" r="3.2" fill="#1f2933"/>
  <line x1="990" y1="330" x2="948" y2="470" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <line x1="990" y1="330" x2="1032" y2="470" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <line x1="990" y1="330" x2="1004" y2="470" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <line x1="990" y1="330" x2="990" y2="286" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <rect x="935" y="183" width="110" height="62" rx="10" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="921" y="192" width="14" height="44" rx="3" fill="#1f2933" stroke="#1f2933" stroke-width="2"/>
  <rect x="974" y="243" width="32" height="56" rx="6" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="1035" y="196" width="8" height="36" fill="#8a96a3"/>
</svg>

Lämpökamera näyttää kappaleiden lämpötilat kuvana, joten sillä voi seurata, miten lämpö etenee kappaleessa ajan kuluessa. Tässä tutkimuksessa lämmität samanmuotoisten eri materiaaleista tehtyjen kappaleiden toista päätä samalla tavalla ja päättelet mittauksista, missä materiaalissa lämpö etenee tehokkaimmin. Lämpökamera on kuitenkin mittalaite, jonka lukemaan vaikuttaa muukin kuin lämpötila, joten selvität myös, milloin sen lukemaan voi luottaa. Mittaa, piirrä ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** missä järjestyksessä lämpö etenee tutkittavissa materiaaleissa tehokkaimmasta heikoimpaan, mihin mitattuun suureeseen vertailu perustuu ja kuinka varmasti järjestys erottuu mittausepävarmuuden rajoissa.

**Päätät itse:** suureen, jonka avulla vertailet materiaaleja, tavan, jolla lämmität kappaleita samalla tavalla, kohdat, joista luet lämpötilat, mittausten ajankohdat ja kokonaiskeston, toistot, kuvaajan sekä tavan, jolla arvioit epävarmuuden. Ohjatussa ja osittain ohjatussa työtavassa sivu antaa näihin tukea, itsenäisessä työtavassa perustelet valintasi itse.

::: tuki I
**Itsenäinen työtapa.** Laajennus, lämpötila kappaleen eri kohdissa ja tasapainotila, kuuluu työhösi: vertaa, saatko sen avulla saman materiaalien järjestyksen kuin päämittauksesta.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Missä järjestyksessä arvelet lämmön etenevän tutkittavissa materiaaleissa nopeimmasta hitaimpaan? Erottuvatko eri metallit toisistaan selvästi?
2. Kaksi yhtä lämmintä kappaletta kuvataan lämpökameralla. Toinen on kiiltävää metallia, toinen on päällystetty mattapintaisella teipillä. Näyttääkö kamera molemmille saman lämpötilan?
3. Mitä arvelet tapahtuvan kappaleen lämpötilalle kaukana lämmitetystä päästä, jos lämmitystä jatketaan hyvin pitkään? Nouseeko se lopulta lämmönlähteen lämpötilaan?
4. Mikä on todennäköisesti vaikeinta pitää samana kaikille kappaleille?

Perustele ennusteesi fysiikan avulla. Palaat niihin johtopäätöksissä. Ennusteen 2 testaat mittauksen yhteydessä ja ennusteen 3 laajennuksessa.

## Tutkimuskysymyksestä mitattaviksi suureiksi

Tutkimuskysymyksessä kysytään, mikä materiaali johtaa lämpöä tehokkaimmin, mutta johtumista ei voi lukea suoraan mittarista: lämpökamera näyttää vain lämpötiloja. Ennen kuin luet eteenpäin, kirjaa:

1. Mikä mitattava suure kertoo, kuinka tehokkaasti lämpö etenee kappaleessa? Keksi ainakin kaksi vaihtoehtoa ja valitse niistä yksi perustellen.
2. Mitä muutat, mitä mittaat ja mitä pidät vakiona?
3. Mistä kohdasta kappaletta ja mihin aikaan luet lämpötilan, jotta vertailu on reilu?

## Teoriaa lyhyesti

Kun kappaleen toista päätä lämmitetään, energiaa siirtyy johtumalla kappaleen läpi lämpimästä päästä kohti kylmää päätä [[apua:fy3-12|Lämmön siirtymisen tavat]]. Mitä tehokkaammin aine johtaa lämpöä, sitä nopeammin lämpö etenee kauemmas lämmitetystä päästä. Kappaleen kohdan lämpötilan nousuun vaikuttaa kuitenkin johtumisen lisäksi kaksi muuta asiaa: aineen lämpeneminen vaatii energiaa, ja tarvittava energia riippuu aineen ominaislämpökapasiteetista ja massasta [[apua:fy3-6|Aineen lämpeneminen]], ja kappaleen pinnasta siirtyy lämpöä ympäröivään ilmaan. Siksi vertailu on mielekäs vain, kun kappaleet ovat samanmuotoisia ja samankokoisia, niitä lämmitetään samalla tavalla ja niiden pinnat ovat samanlaiset. Silloinkin vertailu kertoo, kuinka nopeasti lämpö etenee kussakin materiaalissa, mikä riippuu sekä aineen lämmönjohtavuudesta että sen lämpökapasiteetista.

**Miten lämpökamera mittaa.** Kaikki kappaleet lähettävät lämpösäteilyä, ja mitä kuumempi pinta on, sitä enemmän se säteilee. Lämpökamera ei kosketa kappaletta, vaan mittaa pinnasta tulevaa infrapunasäteilyä ja laskee siitä lämpötilan. Laskussa kamera olettaa, kuinka hyvin pinta säteilee. Tätä pinnan ominaisuutta sanotaan **emissiivisyydeksi**: se on luku nollan ja yhden väliltä, ja se kertoo, kuinka paljon pinta säteilee verrattuna ihanteelliseen säteilijään samassa lämpötilassa. Mattapintainen teippi, maali, puu ja useimmat muovit säteilevät hyvin, ja niiden emissiivisyys on lähellä yhtä. Kiiltävä metallipinta säteilee huonosti ja heijastaa sen sijaan ympäristöstä tulevaa säteilyä, esimerkiksi kuvaajan oman kehon säteilyä. Kiiltävän metallin kohdalla kamera voi siksi näyttää lämpötilan, joka on paljon lähempänä ympäristön lämpötilaa kuin metallin todellinen lämpötila. Kamera mittaa myös vain pinnan lämpötilaa: se ei näe esimerkiksi lasin läpi, koska lasi ei päästä kameran mittaamaa infrapunasäteilyä läpi.

<svg data-fig="emission" viewBox="0 0 600 345" role="img" aria-label="Kaaviokuva. Vasemmalla on metallikappale, jonka koko kappale on samassa lämpötilassa. Sen yläosa on paljasta kiiltävää metallia ja alaosa on päällystetty mattapintaisella teipillä. Teipatusta osasta lähtee lämpökameraa kohti voimakas lämpösäteily, kiiltävästä osasta vain heikko oma säteily. Kiiltävä pinta heijastaa lisäksi kameraan ympäristöstä tulevaa säteilyä. Oikealla on lämpökamera." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy10le-steel" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8a96a3"/><stop offset="0.3" stop-color="#ffffff"/><stop offset="0.65" stop-color="#c4ccd4"/><stop offset="1" stop-color="#8a96a3"/></linearGradient></defs>
  <rect x="120" y="70" width="80" height="110" rx="3" fill="url(#fy10le-steel)" stroke="#1f2933" stroke-width="3"/>
  <rect x="120" y="180" width="80" height="110" rx="3" fill="#3b4148" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="19" y="113" width="91" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:20px">$\text{kiiltävä}$</div></foreignObject>
  <foreignObject x="50" y="223" width="60" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:20px">$\text{matta}$</div></foreignObject>
  <path d="M210,235 L213,239.5 L216,242 L219,241 L222,236.5 L225,231.5 L228,228.5 L231,228.5 L234,231.5 L237,236.5 L240,241 L243,242 L246,239.5 L249,235 L252,230.5 L255,228 L258,229 L261,233.5 L264,238.5 L267,241.5 L270,241.5 L273,238.5 L276,233.5 L279,229 L282,228 L285,230.5 L288,235 L291,239.5 L294,242 L297,241 L300,236.5 L303,231.5 L306,228.5 L309,228.5 L312,231.5 L315,236.5 L318,241 L321,242 L324,239.5 L327,235 L330,230.5 L333,228 L336,229 L339,233.5 L342,238.5 L345,241.5 L348,241.5 L351,238.5 L354,233.5 L357,229 L360,228 L363,230.5 L366,235 L369,239.5 L372,242 L375,241 L378,236.5 L381,231.5 L384,228.5 L387,228.5 L390,231.5 L393,236.5 L396,241 L399,242 L402,239.5 L405,235 L408,230.5 L411,228 L414,229 L417,233.5 L420,238.5 L423,241.5 L426,241.5" fill="none" stroke="#e8590c" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M440,235 L426,242 L426,228 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M210,120 L212,124 L214.5,126.5 L217.5,126 L221.5,124 L225,121.5 L228.5,120 L231.5,121 L234,124 L236,128.5 L238,132 L241,133 L244.5,132 L248,129.5 L252,127 L255,126.5 L258,128.5 L260,132.5 L262,136.5 L264.5,139 L267.5,139.5 L271,138 L275,135 L278.5,133.5 L281.5,133.5 L284,136.5 L286,140.5 L288,144.5 L290.5,146 L294,145.5 L297.5,143.5 L301.5,140.5 L305,139.5 L307.5,141 L310,144.5 L312,148.5 L314,152 L317,153 L320.5,151.5 L324.5,148.5 L328,146.5 L331,146.5 L333.5,149 L336,153 L338,157 L340.5,159 L343.5,159 L347,157 L351,154.5 L354.5,153 L357.5,153.5 L359.5,157 L361.5,161 L364,164.5 L366.5,166 L370,165 L374,162.5 L377.5,160 L381,159.5 L383.5,161.5 L385.5,165 L387.5,169 L390,172 L393,172.5 L396.5,170.5 L400.5,168 L404,166 L407,166.5 L409.5,169 L411.5,173.5 L414,177 L416.5,179 L419.5,178.5 L423.5,176 L427,173.5" fill="none" stroke="#e8590c" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M440,180 L424.5,183 L428,169.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M300,18 L295.5,17 L292,18 L290.5,20.5 L290,25 L289.5,29.5 L288.5,33 L286,35 L281.5,34.5 L277,33.5 L273,33.5 L270.5,35 L269.5,39 L269.5,43.5 L268.5,48 L267,50.5 L263.5,51 L258.5,50 L254.5,49.5 L251,50 L249.5,53 L249,57.5 L248.5,62 L247.5,65.5 L244.5,67 L240.5,66.5 L236,65.5 L232,65.5 L229.5,67.5 L228.5,71.5 L228.5,76 L228,80.5 L225.5,82.5 L222,83 L217.5,82 L213,81.5" fill="none" stroke="#ffc078" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M206,92 L211.5,80 L219,89.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M206,98 L208,102 L211,104 L214,104 L217.5,101.5 L221,99 L224.5,97.5 L227.5,98 L230,101 L232,105 L234.5,108.5 L237,110 L240.5,109 L244,106.5 L248,104 L251,103 L254,104.5 L256,108 L258.5,112 L261,115 L264,115.5 L267,114 L271,111 L274.5,109 L277.5,109 L280,111.5 L282.5,115.5 L284.5,119 L287,121 L290.5,121 L294,118.5 L297.5,115.5 L301,114 L304,115 L306.5,118.5 L308.5,122.5 L311,125.5 L313.5,127 L317,125.5 L320.5,123 L324.5,120.5 L327.5,120 L330,121.5 L332.5,125.5 L334.5,129.5 L337,132 L340,132.5 L343.5,130.5 L347.5,127.5 L351,125.5 L354,126 L356.5,128.5 L358.5,132.5 L361,136.5 L363.5,138 L367,137.5 L370.5,135 L374,132.5 L377.5,131 L380.5,132 L382.5,135.5 L385,139.5 L387,143 L390,144 L393.5,142.5 L397,139.5 L400.5,137.5 L404,137 L406.5,139 L409,142.5 L411,146.5 L413.5,149 L416.5,149 L420,147 L424,144.5 L427.5,142.5" fill="none" stroke="#ffc078" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M440,150 L425,154 L428,140 Z" fill="#ffc078" stroke-linejoin="round"/>
  <foreignObject x="312" y="8" width="133" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#6b7480">$\text{ympäristöstä}$</div></foreignObject>
  <foreignObject x="120" y="310" width="299" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#6b7480">$\text{sama lämpötila koko kappaleessa}$</div></foreignObject>
  <rect x="470.5" y="162" width="99" height="56" rx="9" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="458" y="170" width="12.5" height="39.5" rx="3" fill="#1f2933" stroke="#1f2933" stroke-width="2"/>
  <rect x="505.5" y="216" width="29" height="50.5" rx="5.4" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="560.5" y="174" width="7" height="32.5" fill="#8a96a3"/>
  <foreignObject x="459" y="278" width="122" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\text{lämpökamera}$</div></foreignObject>
</svg>

::: tuki O OO
Tarkista kirjauksesi tästä. Lämmön etenemistä voi vertailla esimerkiksi näillä suureilla:

- **Lämpötilan nousu tietyssä kohdassa tiettynä hetkenä:** lue kunkin kappaleen lämpötila $T$ samalta etäisyydeltä $x$ lämmitetystä päästä, kun lämmitys on kestänyt saman ajan, ja vertaa nousua $T - T_0$, missä $T_0$ on kappaleen lämpötila ennen lämmitystä.
- **Aika tiettyyn lämpötilan nousuun:** mittaa, kuinka kauan kestää, että kohta etäisyydellä $x$ lämpenee esimerkiksi viisi astetta alkulämpötilaa lämpimämmäksi.
- **Lämpötila ajan funktiona:** lue kunkin kappaleen lämpötila samasta kohdasta tasaisin väliajoin ja piirrä kaikki samaan kuvaajaan.

Muutettava tekijä on materiaali. Vakiona pidetään kappaleiden muoto ja koko, lämmitystapa ja lämmönlähteen lämpötila, kuinka syvällä lämmönlähteessä kappaleet ovat, kappaleiden pinta ja kameran paikka. Etäisyys $x$ mitataan kohdasta, jossa kappale tulee ulos lämmönlähteestä, esimerkiksi eristävän kannen yläpinnasta.

<svg data-fig="setup" viewBox="0 0 600 400" role="img" aria-label="Kaaviokuva yhdestä mahdollisesta koejärjestelystä sivulta. Astiassa on kuumaa vettä ja sen päällä lämpöä eristävä kansi. Kannen läpi nousee neljä samanmuotoista sauvaa, jotka ulottuvat yhtä syvälle veteen; ne on teipattu vain vedenpinnan yläpuolelta. Ensimmäisen sauvan vierellä on merkitty mittauskohta, jonka korkeus kannen yläpinnasta on x. Oikealla jalustan päällä oleva lämpökamera kuvaa kaikkia sauvoja samasta kohdasta. Veteen on upotettu lämpömittari." style="max-width:100%;font-size:24px">
  <rect x="40" y="250" width="280" height="120" rx="6" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <rect x="43" y="268" width="274" height="99" fill="#a9d1f0"/>
  <line x1="43" y1="268" x2="317" y2="268" stroke="#2f74b5" stroke-width="2" stroke-linecap="butt"/>
  <rect x="30" y="236" width="300" height="16" rx="4" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="82" y="70" width="16" height="270" rx="2" fill="#b8622d" stroke="#1f2933" stroke-width="2"/>
  <rect x="82" y="70" width="16" height="198" rx="2" fill="#3b4148" stroke="#1f2933" stroke-width="2"/>
  <rect x="142" y="70" width="16" height="270" rx="2" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="142" y="70" width="16" height="198" rx="2" fill="#3b4148" stroke="#1f2933" stroke-width="2"/>
  <rect x="202" y="70" width="16" height="270" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="202" y="70" width="16" height="198" rx="2" fill="#3b4148" stroke="#1f2933" stroke-width="2"/>
  <rect x="262" y="70" width="16" height="270" rx="2" fill="#d9b26a" stroke="#1f2933" stroke-width="2"/>
  <rect x="262" y="70" width="16" height="198" rx="2" fill="#3b4148" stroke="#1f2933" stroke-width="2"/>
  <line x1="298" y1="196" x2="298" y2="350" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="298" cy="352" r="6" fill="#e8590c" stroke="#1f2933" stroke-width="2"/>
  <line x1="62" y1="150" x2="62" y2="236" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="54" y1="150" x2="70" y2="150" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="54" y1="236" x2="70" y2="236" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="30" y="178.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$x$</div></foreignObject>
  <circle cx="90" cy="150" r="5" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="90" y="28" width="154" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#6b7480">$\text{teipatut sauvat}$</div></foreignObject>
  <foreignObject x="336" y="308" width="102" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#6b7480">$\text{kuuma vesi}$</div></foreignObject>
  <foreignObject x="336" y="232" width="143" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#6b7480">$\text{eristävä kansi}$</div></foreignObject>
  <line x1="478" y1="140" x2="74" y2="62" stroke="#6b7480" stroke-width="1.2" stroke-linecap="butt" stroke-dasharray="4 5"/>
  <line x1="478" y1="140" x2="74" y2="236" stroke="#6b7480" stroke-width="1.2" stroke-linecap="butt" stroke-dasharray="4 5"/>
  <line x1="530" y1="370" x2="530" y2="180" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="500" y1="370" x2="560" y2="370" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="489" y="117" width="82.5" height="46.5" rx="7.5" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="478" y="123.5" width="10.5" height="33" rx="3" fill="#1f2933" stroke="#1f2933" stroke-width="2"/>
  <rect x="518" y="161" width="24" height="42" rx="4.5" fill="#6c757d" stroke="#1f2933" stroke-width="3"/>
  <rect x="564" y="126.5" width="6" height="27" fill="#8a96a3"/>
  <foreignObject x="469" y="70" width="122" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\text{lämpökamera}$</div></foreignObject>
</svg>

Kuvaaja esittää mallin muotoa, ei mittaustuloksia: samassa kohdassa lämpötila alkaa nousta vasta viiveellä, koska lämmön täytyy ensin edetä kohtaan asti. Mitä nopeammin lämpö etenee materiaalissa, sitä aikaisemmin ja nopeammin lämpötila nousee.

<svg data-fig="model" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja: lämpötila T ajan t funktiona samassa kohdassa kahdessa sauvassa mallin mukaan. Molemmat alkavat huoneen lämpötilasta T nolla. Sauvassa, jossa lämpö etenee nopeasti, lämpötila alkaa nousta lyhyen viiveen jälkeen ja nousee nopeammin; sauvassa, jossa lämpö etenee hitaasti, nousu alkaa myöhemmin ja on loivempi. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="291" x2="90" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,24 L96,37 L84,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="502" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="80" y="-6.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T$</div></foreignObject>
  <polyline points="90,263.5 470,263.5" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <foreignObject x="47" y="249" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$T_0$</div></foreignObject>
  <polyline points="90,263.5 93,263.5 96.5,263.5 99.5,263.5 102.5,263.5 106,263 109,263 112,262.5 115.5,262 118.5,261.5 121.5,260.5 125,259.5 128,258.5 131,257 134.5,255.5 137.5,254 140.5,252.5 144,251 147,249.5 150,248 153.5,246.5 156.5,244.5 159.5,243 163,241.5 166,240 169,238.5 172.5,237 175.5,235.5 178.5,234 182,232.5 185,231 188,229.5 191.5,228 194.5,226.5 197.5,225 201,224 204,222.5 207,221 210.5,220 213.5,218.5 216.5,217.5 220,216 223,215 226,214 229.5,212.5 232.5,211.5 235.5,210.5 239,209.5 242,208.5 245,207.5 248.5,206 251.5,205 254.5,204 258,203.5 261,202.5 264,201.5 267.5,200.5 270.5,199.5 273.5,198.5 277,197.5 280,197 283,196 286.5,195 289.5,194.5 292.5,193.5 296,192.5 299,192 302,191 305.5,190.5 308.5,189.5 311.5,189 315,188 318,187.5 321,187 324.5,186 327.5,185.5 330.5,184.5 334,184 337,183.5 340,182.5 343.5,182 346.5,181.5 349.5,181 353,180 356,179.5 359,179 362.5,178.5 365.5,178 368.5,177.5 372,176.5 375,176 378,175.5 381.5,175 384.5,174.5 387.5,174 391,173.5 394,173 397,172.5 400.5,172 403.5,171.5 406.5,171 410,170.5 413,170 416,169.5 419.5,169 422.5,168.5 425.5,168 429,167.5 432,167 435,166.5 438.5,166.5 441.5,166 444.5,165.5 448,165 451,164.5 454,164 457.5,164 460.5,163.5 463.5,163 467,162.5 470,162" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="90,263.5 93,263.5 96.5,263.5 99.5,263.5 102.5,263.5 106,263.5 109,263.5 112,263.5 115.5,263.5 118.5,263.5 121.5,263.5 125,263.5 128,263.5 131,263.5 134.5,263.5 137.5,263.5 140.5,263.5 144,263.5 147,263.5 150,263.5 153.5,263.5 156.5,263.5 159.5,263.5 163,263.5 166,263.5 169,263.5 172.5,263.5 175.5,263.5 178.5,263.5 182,263.5 185,263.5 188,263 191.5,263 194.5,263 197.5,263 201,263 204,263 207,263 210.5,263 213.5,263 216.5,263 220,263 223,263 226,262.5 229.5,262.5 232.5,262.5 235.5,262.5 239,262.5 242,262.5 245,262 248.5,262 251.5,262 254.5,262 258,262 261,261.5 264,261.5 267.5,261.5 270.5,261.5 273.5,261 277,261 280,261 283,261 286.5,260.5 289.5,260.5 292.5,260.5 296,260 299,260 302,260 305.5,259.5 308.5,259.5 311.5,259 315,259 318,259 321,258.5 324.5,258.5 327.5,258.5 330.5,258 334,258 337,257.5 340,257.5 343.5,257.5 346.5,257 349.5,257 353,256.5 356,256.5 359,256 362.5,256 365.5,255.5 368.5,255.5 372,255.5 375,255 378,255 381.5,254.5 384.5,254.5 387.5,254 391,254 394,253.5 397,253.5 400.5,253 403.5,253 406.5,252.5 410,252.5 413,252 416,252 419.5,251.5 422.5,251.5 425.5,251 429,251 432,250.5 435,250.5 438.5,250 441.5,250 444.5,249.5 448,249.5 451,249 454,249 457.5,248.5 460.5,248.5 463.5,248 467,248 470,247.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="9 6"/>
  <foreignObject x="256.5" y="120.5" width="206" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:20px">$\text{lämpö etenee nopeasti}$</div></foreignObject>
  <foreignObject x="256.5" y="211.5" width="206" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:20px">$\text{lämpö etenee hitaasti}$</div></foreignObject>
</svg>
:::

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, millä suureella vertailet materiaaleja, mitä pidät vakiona ja miten varmistat, että lämpökamera mittaa kaikkien kappaleiden lämpötilaa yhtä luotettavasti.

::: tuki O
**Ohjattu.** Käytä samankokoisia sauvoja tai liuskoja, esimerkiksi noin $15\ \text{cm}$ – $20\ \text{cm}$ pitkiä, ja päällystä niiden vedenpinnan yläpuoliset osat samanlaisella mattapintaisella teipillä. Työnnä kappaleet eristävän kannen reikien läpi niin, että ne ovat yhtä syvällä kuumassa vedessä eivätkä kosketa toisiaan. Kiinnitä lämpökamera jalustaan niin, että kaikki kappaleet näkyvät samassa kuvassa. Tutki ainakin kolmea materiaalia, esimerkiksi kuparia, terästä ja puuta, ja lue lämpötilat yhdestä mittauskohdasta kannen yläpuolelta, esimerkiksi $x = 3\ \text{cm}$. Jos aikaa jää, voit lisätä materiaaleja tai toisen mittauskohdan. Mittaa veden lämpötila lämpömittarilla mittauksen alussa ja lopussa.
:::

::: tuki OO
**Osittain ohjattu.** Vertailtava tekijä on materiaali. Päätä itse, millä suureella vertailet materiaaleja, mistä kohdista luet lämpötilat ja kuinka pitkään mittaat. Kirjaa päätöksesi perusteluineen.
:::

::: tuki O OO
Mieti ainakin näitä:

- Miten varmistat, että kaikkien kappaleiden pinnat säteilevät yhtä hyvin? Miksi pelkkä kiiltävän metallin kuvaaminen ei riitä?
- Miten tunnistat lämpökamerakuvasta kohdan, joka on etäisyydellä $x$? Voit käyttää mittakaavana esimerkiksi kappaleen tunnettua pituutta kuvassa.
- Veden lämpötila laskee mittauksen aikana. Miksi se ei haittaa vertailua, kun kaikki kappaleet ovat samassa astiassa, ja miten voit pienentää laskua?
- Kuinka kauan mittaus kestää, ja kuinka usein otat kuvan? Kokeile ennen varsinaista mittausta, kuinka nopeasti lämpö etenee nopeimmassa kappaleessa.
- Miksi lämpökameraa ei kannata pitää kädessä eikä kuvaajan pidä seistä kappaleiden takana?
- Näkyykö kappale kuvassa niin leveänä, että lukemasi kohta on kokonaan kappaleen päällä? Jos kappale on kuvassa vain muutaman kuvapisteen levyinen, lukemaan sekoittuu taustan lämpötila.
- Kannen yläpuolinen lämmin ilma voi lämmittää kappaleita myös ulkopuolelta. Miten erotat sen johtumisesta, esimerkiksi huonosti johtavan kappaleen lukemista?
:::

## Mittaa

Kirjaa alkuperäiset mittaustulokset taulukkoon heti mittauksen aikana tai tallenna lämpökamerakuvat ja lue lämpötilat niistä jälkikäteen. Merkitse jokaiseen kuvaan, kuinka kauan lämmitys oli kestänyt.

::: tuki O
Ota lämpökamerakuva heti, kun kappaleet on laskettu veteen, ja sen jälkeen minuutin välein noin kymmenen minuutin ajan. Voit käyttää esimerkiksi tällaista taulukkoa. Jos tutkit lisää materiaaleja, lisää niille omat sarakkeet.

| $t\ (\text{min})$ | $T_\text{kupari}\ ({}^\circ\text{C})$ | $T_\text{teräs}\ ({}^\circ\text{C})$ | $T_\text{puu}\ ({}^\circ\text{C})$ |
|---|---|---|---|
| $0$ | | | |
| $1$ | | | |
| $2$ | | | |
| … | | | |

Kun mittaus on valmis ja kappaleet ovat jäähtyneet huoneen lämpötilaan, toista mittaus niin, että kappaleiden järjestys astiassa on vaihdettu. Näin näet, johtuivatko erot materiaalista vai kappaleen paikasta astiassa tai kuvassa.
:::

**Testaa ennusteesi 2.** Jätä ennen mittausta yhteen metallisauvaan lyhyt kohta ilman teippiä, mittauskohtien ulkopuolelle. Kun sauva on lämmennyt, ota kuva, jossa näkyvät sekä paljas kohta että sen vieressä oleva teipattu kohta, ja vertaa niiden lukemia. Älä koske sauvaan.

Muista mittausepävarmuus: arvioi, kuinka tarkasti luet lämpötilan kuvasta, ja kirjaa arvio ylös. Selvitä kameran ohjeesta, kuinka tarkaksi valmistaja ilmoittaa kameran lukeman. [[apua:fy1-3|Mittaaminen ja mittauksen luotettavuus]]

## Käsittele tulokset

Esitä tulokset kuvaajana tai kuvaajina, joista materiaalien erot näkyvät selvästi. Merkitse akseleille suureet ja yksiköt ja kerro, mitä materiaalia kukin kuvaaja tai pisteistö esittää. [[apua:fy1-4|Graafinen esitys]]

::: tuki O
Piirrä kuvaaja: pystyakselille lämpötila $T$ ja vaaka-akselille aika $t$, ja kaikki materiaalit samaan kuvaajaan eri merkein. Yhdistä saman materiaalin pisteet ohuella viivalla, jotta käyrät erottuvat toisistaan. Lue kuvaajasta lisäksi kunkin materiaalin lämpötilan nousu $T - T_0$ samana valittuna hetkenä.
:::

Vastaa sitten:

1. Missä järjestyksessä materiaalit lämpenivät? Onko järjestys sama eri mittauskohdissa ja toistoissa?
2. Mitkä materiaalit erottuvat toisistaan selvästi ja mitkä eivät?
3. Näkyykö lämpökamerakuvassa kohtia, joiden lukemaan et luota? Mistä ne voisivat johtua?

Kuvaajan piirtämiseen voit käyttää esimerkiksi Graphical Analysis -ohjelmaa tai taulukkolaskentaa. Ruukkilabran ohjeet: [[ohje:tvt-kuvaaja|Mittauspisteiden kuvaaja]] ja [[ohje:tvt-taulukkolaskenta|Taulukkolaskenta]]. Lämpökameran käytössä noudata laitteen omaa käyttöohjetta.

## Epävarmuus ja luotettavuus

Arvioi, kuinka suuri on vertailemasi suureen epävarmuus, ja päättele sen avulla, mitkä materiaalien erot ovat todellisia.

::: tuki O OO
Lämpötilalukeman epävarmuuden $\Delta T$ voit arvioida esimerkiksi näin:

- **Lukeman vaihtelu.** Lue saman kohdan lämpötila samasta kuvasta muutaman kerran hieman eri pisteistä ja arvioi, kuinka paljon lukema vaihtelee.
- **Toisto.** Vertaa saman materiaalin tuloksia kahdessa toistossa. Ero kertoo, kuinka hyvin koko mittaus toistuu.

Kun vertaat lämpötilan nousua $T - T_0$, sen epävarmuus on lähtö- ja loppulukeman epävarmuuksien summa. Jos luet molemmat lukemat samasta kohdasta samalla kameralla, kameran tasovirhe eli kaikkiin lukemiin samansuuruisena vaikuttava poikkeama kumoutuu nousussa suurelta osin, joten lukeman vaihtelu on silloin tärkeämpi kuin kameran ilmoitettu tarkkuus. Kahden materiaalin tulokset eroavat selvästi, jos niiden ero on suurempi kuin niiden epävarmuuksien summa. Valmistajan ilmoittama kameran tarkkuus kuvaa lähinnä systemaattista virhettä, joka on samansuuntainen kaikilla samanlaisilla pinnoilla samassa kuvassa. Se vaikuttaa siksi enemmän yksittäisiin lämpötiloihin kuin materiaalien järjestykseen.
:::

Pohdi sitten luotettavuutta konkreettisesti: olivatko kappaleiden pinnat, lämmitys ja paikat todella samanlaiset? Miten kappaleen pinta ja ympäristöstä heijastuva säteily ovat voineet vaikuttaa lukemiin? Olivatko virheet satunnaisia vai systemaattisia, ja muuttivatko ne kaikkien materiaalien tuloksia samaan suuntaan? Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella: mikä materiaali johtaa lämpöä tehokkaimmin, ja kuinka varmasti järjestys erottui epävarmuuden rajoissa? Kerro, mihin suureeseen vertailu perustui ja mitä muuta kuin lämmönjohtavuutta se saattoi mitata. Viittaa kuvaajaan, esimerkiksi "kuvaajasta 1 nähdään, että …". Vertaa tulosta ennusteeseesi: mikä osui oikeaan ja mikä ei? Ennusteeseen 3 vastaat laajennuksen avulla. Jos et tee laajennusta, kerro, mitä kuvaajasi loppuosa kertoo siitä.

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla (kuvaajista ja tuloksista ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]) ja käy läpi sen kaikki osat. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tutkimuskysymys ja tausta:** mihin mitattavaan suureeseen materiaalien vertailu perustuu ja miksi.
- **Koejärjestely ja menetelmä:** mitä pidit vakiona ja miten varmistit, että lämpökamera mittasi kaikkia kappaleita yhtä luotettavasti.
- **Mittaustulokset:** taulukko tai tallennetut kuvat, joista lukemat on luettu, ja tieto siitä, milloin kukin kuva on otettu.
- **Tulos:** materiaalien järjestys ja kuvaaja, josta se näkyy.
- **Luotettavuus:** konkreettiset epävarmuuden lähteet, erityisesti pinnan vaikutus lämpökameran lukemaan, ja niiden vaikutuksen suunta.

## Laajennus: lämpötila kappaleen eri kohdissa ja tasapainotila

Lämpökamerakuvasta näet saman hetken lämpötilan kappaleen kaikissa kohdissa yhtä aikaa. Lue yhdestä kuvasta kunkin kappaleen lämpötila useassa kohdassa ja piirrä lämpötila etäisyyden $x$ funktiona kaikille materiaaleille samaan kuvaajaan. Jatka sitten lämmitystä niin kauan, että lämpötilat eivät enää muutu, ja piirrä sama kuvaaja uudelleen.

Kun lämpötilat eivät enää muutu, kappale on energiatasapainossa: kappaleeseen johtuu lämmönlähteestä yhtä suuri teho kuin sen pinnasta siirtyy ympäröivään ilmaan [[apua:fy3-12|Energiatasapaino]]. Silloin kappaleen lämpeneminen ei enää sido energiaa, joten aineen lämpökapasiteetti ei enää vaikuta lämpötiloihin. Kun kappaleiden muoto, koko ja pinta sekä lämmönlähteen ja ilman lämpötilat ovat samat, lämpötilat riippuvat vain siitä, kuinka hyvin aine johtaa lämpöä verrattuna siihen, kuinka paljon lämpöä pinnasta siirtyy ilmaan.

Vastaa: miten lämpötila muuttuu etäisyyden kasvaessa eri materiaaleissa? Saatko tasapainotilasta saman materiaalien järjestyksen kuin päämittauksesta? Miksi tasapainotilan vertailu kertoo lämmönjohtavuudesta suoremmin kuin vertailu lämmityksen alkuvaiheessa?

::: tuki O OO
**Vihjeitä.** Tasapainotilan saavuttaminen voi kestää kauan, joten pidä veden lämpötila mahdollisimman vakiona, esimerkiksi lisäämällä kuumaa vettä tai käyttämällä suurta vesimäärää. Tasapainotilan tunnistat siitä, että peräkkäisten kuvien lukemat eivät enää muutu enempää kuin lukeman epävarmuus.
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi kuvaajaan ja mittaustuloksiin vai siihen, mitä odotit?
- Mitä tekisit toisin, jos aloittaisit alusta?
