# Resistanssi ja Ohmin laki

> **Miksi** leivänpaahtimen lämmityslanka tehdään ohuesta erikoismetallista, mutta jatkojohdon johtimet ovat paksua kuparia?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: keittiön työtaso. Leivänpaahdin on päällä. Sen leipäaukoista hohtaa oranssi valo, kun ohuet lämmityslangat hehkuvat. Paahtimen johto on kytketty paksuun jatkojohtoon, joka menee pistorasiaan. Jatkojohto ei hehku." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-3-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Resistanssi kertoo, kuinka paljon komponentti vastustaa virtaa
Kun komponentin napojen välille kytketään jännite, komponentin läpi kulkee sähkövirta. Sama jännite antaa eri komponenteissa eri suuren virran. Lyhyessä paksussa kuparijohdossa virta on suuri. Ohuessa pitkässä lämmityslangassa virta on pieni. Komponentin **resistanssi** $R$ kertoo, kuinka paljon komponentti vastustaa sähkövirtaa. Resistanssi lasketaan jakamalla jännite virralla: $R = U : I$. Mitä suurempi resistanssi on, sitä pienemmän virran sama jännite antaa. Resistanssin yksikkö on ohmi, $1\,\Omega = 1\,\text{V/A}$. Komponentin resistanssi on yksi ohmi, kun yhden voltin jännite saa sen läpi yhden ampeerin virran.

Komponentti, joka on tehty tietyn suuruiseksi resistanssiksi, on **vastus**. Sen piirrosmerkki on suorakulmio. Resistanssi saadaan selville mittaamalla yhtä aikaa komponentin jännite ja komponentin läpi kulkeva virta. Virtamittari kytketään sarjaan komponentin kanssa. Silloin sama virta kulkee molempien läpi. Jännitemittari kytketään rinnan komponentin kanssa, komponentin napoihin. Kun mittaus tehdään usealla jännitteellä, nähdään, pysyykö suhde $U : I$ samana.

<svg data-fig="measure-circuit" viewBox="0 0 600 350" role="img" aria-label="Kytkentäkaavio resistanssin mittaamiseen, periaatekuva. Paristo, virtamittari ja vastus R ovat samassa virtapiirissä peräkkäin eli sarjassa. Virtamittarin läpi kulkee siis sama virta I kuin vastuksen läpi. Jännitemittari on kytketty vastuksen napoihin eli rinnan vastuksen kanssa. Se mittaa vastuksen jännitteen U. Violetit nuolet näyttävät virran suunnan pariston plusnavasta piirin kautta miinusnapaan." style="max-width:100%;font-size:24px">
  <path d="M90,162 L90,90 L223,90" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="245" cy="90" r="22" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="230" y="75.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <path d="M267,90 L400,90 L400,135" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="387" y="135" width="26" height="70" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M400,205 L400,250 L90,250 L90,178" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="68" y="158" width="44" height="4" fill="#1f2933"/>
  <rect x="79" y="172" width="22" height="6" fill="#1f2933"/>
  <foreignObject x="36" y="137.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="36" y="173.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$-$</div></foreignObject>
  <circle cx="400" cy="115" r="5" fill="#1f2933"/>
  <circle cx="400" cy="225" r="5" fill="#1f2933"/>
  <path d="M400,115 L500,115 L500,148" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M400,225 L500,225 L500,192" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="500" cy="170" r="22" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="485" y="155.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <foreignObject x="348" y="155.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$R$</div></foreignObject>
  <foreignObject x="532" y="155.5" width="26" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U$</div></foreignObject>
  <path d="M159,90 L141,98 L141,82 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M349,90 L331,98 L331,82 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M236,250 L254,242 L254,258 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="138" y="49.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="233" y="261.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="166" y="35.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{virtamittari}$</div></foreignObject>
  <foreignObject x="408.5" y="247.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{jännitemittari}$</div></foreignObject>
  <line x1="12" y1="296" x2="588" y2="296" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="90" y="309.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I = \text{virta},\ U = \text{jännite},\ R = \text{resistanssi}$</div></foreignObject>
</svg>

```pysahdy
Kahden komponentin yli on sama jännite. Toisen läpi kulkee suurempi virta kuin toisen. Kummalla on suurempi resistanssi?
---
Sillä, jonka läpi kulkee pienempi virta. Kun $U$ on sama, $R = U : I$ on sitä suurempi, mitä pienempi $I$ on.
```

### Mistä resistanssi tulee
Metallissa on positiivisia ioneja. Ne ovat säännöllisessä hilassa, eli kiinteissä paikoissa rivissä. Ionien välissä liikkuu vapaita elektroneja. Kun johtimen päiden välillä on jännite, elektronit etenevät johtimessa. Ne törmäilevät koko ajan ioneihin, jotka värähtelevät paikallaan. Törmäykset hidastavat elektroneja. Tämä on resistanssin syy. Törmäyksissä sähköenergiaa muuttuu johtimen sisäenergiaksi, ja siksi johdin lämpenee. Pitkässä johtimessa elektroni törmää matkallaan useammin, joten resistanssi on suurempi. Paksussa johtimessa elektroneja kulkee rinnakkain enemmän, joten resistanssi on pienempi. Kun metalli kuumenee, ionit värähtelevät voimakkaammin ja törmäyksiä on enemmän. Siksi metallijohtimen resistanssi kasvaa, kun lämpötila nousee.

<svg data-fig="micro" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva metallilangan sisältä, ei mittakaavassa. Positiiviset metalli-ionit ovat säännöllisessä hilassa. Vapaat elektronit kulkevat ionien välissä vasemmalle, kun sovittu virran suunta on oikealle. Vasemmassa kuvassa lanka on huoneenlämpöinen. Ionit värähtelevät vähän, ja elektroni törmää harvoin. Oikeassa kuvassa lanka on kuuma. Ionit värähtelevät voimakkaasti, mitä kuvaavat leveämmät renkaat. Elektronin reitti katkeaa useammin törmäyksiin. Kuuman langan resistanssi on suurempi." style="max-width:100%;font-size:24px">
  <image href="pics/fy6/fy6-3-micro.webp" x="0" y="0" width="600" height="342.5" preserveAspectRatio="none"/>
  <foreignObject x="46" y="11.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{huoneenlämpöinen}$</div></foreignObject>
  <foreignObject x="146" y="237.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\text{elektronit}$</div></foreignObject>
  <foreignObject x="116" y="271.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="383.5" y="11.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kuuma lanka}$</div></foreignObject>
  <foreignObject x="446" y="237.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\text{elektronit}$</div></foreignObject>
  <foreignObject x="416" y="271.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy6/filament-bulb.webp" alt="Hehkulamppu läheltä. Ohut lanka hehkuu oranssina."><figcaption>Hehkulampun ohut volframilanka hehkuu, kun sen läpi kulkee virta. Elektronit törmäävät metallin ioneihin. Silloin sähköenergiaa muuttuu langan sisäenergiaksi, ja lanka kuumenee.</figcaption></figure>

## Kaava: Ohmin laki ja resistiivisyys
Resistanssi on komponentin jännitteen ja komponentin läpi kulkevan virran suhde:
```latex
R = \frac{U}{I}
```
Tässä $R$ on resistanssi ($\Omega$), $U$ on komponentin jännite ($\text{V}$) ja $I$ on komponentin läpi kulkeva virta ($\text{A}$).

**Ohmin laki:** metallijohtimen läpi kulkeva virta on suoraan verrannollinen jännitteeseen, kun johtimen lämpötila pysyy samana. Suoraan verrannollinen tarkoittaa tässä, että kun jännite kaksinkertaistuu, myös virta kaksinkertaistuu. Silloin resistanssi on vakio, ja
```kaavat
jännitehäviö johtimessa :: U = R I
```
Ohmin laki ei ole yleinen luonnonlaki. Se on monen johdinaineen ominaisuus. Laki pätee metalleille ja vastuksille, kun lämpötila pysyy samana. Se ei päde esimerkiksi hehkulampulle, jonka lanka kuumenee. Se ei päde myöskään diodille.

```pysahdy
Metallijohtimen jännite kasvaa arvosta $2{,}0\,\text{V}$ arvoon $6{,}0\,\text{V}$. Lämpötila pysyy samana. Miten virta ja resistanssi muuttuvat?
---
Jännite kolminkertaistuu, joten Ohmin lain mukaan virtakin kolminkertaistuu. Resistanssi $R = U : I$ pysyy samana.
```

### Ominaiskäyrä
Komponentin **ominaiskäyrä** on kuvaaja, joka näyttää, miten komponentin jännite ja virta riippuvat toisistaan. Virta $I$ on vaaka-akselilla ja jännite $U$ pystyakselilla. Silloin vastuksen ominaiskäyrä on suora, joka kulkee origon kautta. Vastuksen pitää noudattaa Ohmin lakia. Suoran kulmakerroin on resistanssi $R$. Hehkulampun ominaiskäyrä on kaareva. Lampun volframilanka kuumenee sitä enemmän, mitä suurempi virta sen läpi kulkee. Kuuman langan resistanssi on suurempi. Käyrän jokaisessa pisteessä resistanssi on silti suhde $U : I$. Se on origosta pisteeseen piirretyn suoran kulmakerroin. Se ei ole käyrän jyrkkyys siinä kohdassa.

<svg data-fig="curves" viewBox="0 0 600 360" role="img" aria-label="Kuvaaja mittakaavassa: jännite U voltteina virran I funktiona ampeereina. Vastuksen ominaiskäyrä on suora, joka kulkee origon ja pisteen (0,30 A; 3,0 V) kautta. Sen resistanssi on siis 10 ohmia joka kohdassa. Hehkulampun ominaiskäyrä on kaareva. Pienillä jännitteillä se nousee loivasti ja suurilla jyrkästi. Jännitteellä 3,0 V lampun virta on 0,25 A. Katkoviiva origosta lampun pisteeseen kuvaa lampun resistanssia U : I = 12 ohmia tällä jännitteellä. Ruudukon väli on 0,05 A ja 0,5 V." style="max-width:100%;font-size:24px">
  <line x1="148.5" y1="306" x2="148.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="201" y1="306" x2="201" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="253.5" y1="306" x2="253.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="306.5" y1="306" x2="306.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="359" y1="306" x2="359" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="411.5" y1="306" x2="411.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="464" y1="306" x2="464" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="270.5" x2="464" y2="270.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="234.5" x2="464" y2="234.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="199" x2="464" y2="199" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="163" x2="464" y2="163" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="127.5" x2="464" y2="127.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="91.5" x2="464" y2="91.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="56" x2="464" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="306" x2="478" y2="306" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M490,306 L477,312 L477,300 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="307" x2="96" y2="42" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,30 L102,43 L90,43 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="148.5" y1="306" x2="148.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="201" y1="306" x2="201" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="178.5" y="315.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}1$</div></foreignObject>
  <line x1="253.5" y1="306" x2="253.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="306.5" y1="306" x2="306.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="284" y="315.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}2$</div></foreignObject>
  <line x1="359" y1="306" x2="359" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="411.5" y1="306" x2="411.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="389" y="315.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}3$</div></foreignObject>
  <line x1="464" y1="306" x2="464" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="270.5" x2="96" y2="270.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="234.5" x2="96" y2="234.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="220" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="89" y1="199" x2="96" y2="199" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="163" x2="96" y2="163" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="148.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="89" y1="127.5" x2="96" y2="127.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="89" y1="91.5" x2="96" y2="91.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="77" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="89" y1="56" x2="96" y2="56" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="66" y="311.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="496" y="291.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I\ (\text{A})$</div></foreignObject>
  <foreignObject x="86" y="-0.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U\ (\text{V})$</div></foreignObject>
  <polyline points="96,306 437.5,74" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,306 112,304 123,302.5 132,300.5 139.5,299 146,297 152,295.5 157.5,293.5 162.5,291.5 167,290 171.5,288 176,286.5 180,284.5 183.5,283 187.5,281 191,279 194,277.5 197.5,275.5 200.5,274 203.5,272 206.5,270.5 209.5,268.5 212,266.5 215,265 217.5,263 220,261.5 222.5,259.5 225,258 227.5,256 230,254 232,252.5 234.5,250.5 236.5,249 239,247 241,245.5 243,243.5 245,241.5 247.5,240 249.5,238 251,236.5 253,234.5 255,233 257,231 259,229 260.5,227.5 262.5,225.5 264,224 266,222 267.5,220.5 269.5,218.5 271,216.5 273,215 274.5,213 276,211.5 277.5,209.5 279.5,208 281,206 282.5,204 284,202.5 285.5,200.5 287,199 288.5,197 290,195.5 291.5,193.5 293,191.5 294.5,190 296,188 297,186.5 298.5,184.5 300,183 301.5,181 302.5,179 304,177.5 305.5,175.5 306.5,174 308,172 309.5,170.5 310.5,168.5 312,166.5 313,165 314.5,163 315.5,161.5 317,159.5 318,158 319.5,156 320.5,154 322,152.5 323,150.5 324.5,149 325.5,147 326.5,145.5 328,143.5 329,141.5 330,140 331.5,138 332.5,136.5 333.5,134.5 334.5,133 336,131 337,129 338,127.5 339,125.5 340,124 341.5,122 342.5,120.5 343.5,118.5 344.5,116.5 345.5,115 346.5,113 347.5,111.5 348.5,109.5 350,108 351,106 352,104 353,102.5 354,100.5 355,99 356,97 357,95.5 358,93.5 359,91.5" fill="none" stroke="#e8590c" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="96,306 359,91.5" fill="none" stroke="#6b7480" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 5"/>
  <circle cx="359" cy="91.5" r="6.5" fill="#e8590c" stroke="#ffffff" stroke-width="2"/>
  <circle cx="411.5" cy="91.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="445.5" y="59.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{vastus}$</div></foreignObject>
  <foreignObject x="200" y="67" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e8590c">$\text{hehkulamppu}$</div></foreignObject>
</svg>

### Resistiivisyys
Tasapaksun johtimen resistanssi on suoraan verrannollinen johtimen pituuteen $l$. Se on kääntäen verrannollinen poikkipinta-alaan $A$. Johtimen pitää olla samaa ainetta koko matkalta.
```kaavat
johtimen resistanssi :: R = \rho \frac{l}{A}
```
Tässä $R$ on johtimen resistanssi ($\Omega$), $l$ on pituus ($\text{m}$), $A$ on poikkipinta-ala ($\text{m}^2$) ja $\rho$ on aineen **resistiivisyys** ($\Omega\cdot\text{m}$). Kaksi kertaa pidempi lanka on kuin kaksi lankaa peräkkäin, joten resistanssi kaksinkertaistuu. Lanka, jonka poikkipinta-ala on kaksinkertainen, on kuin kaksi lankaa rinnakkain. Virta pääsee kulkemaan kahta reittiä, joten resistanssi puolittuu. Poikkipinta-ala ilmoitetaan usein neliömillimetreinä, ja $1\,\text{mm}^2 = (10^{-3}\,\text{m})^2 = 10^{-6}\,\text{m}^2$.

<svg data-fig="wire" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva kolmesta saman aineen langasta, pituudet mittakaavassa. Ylinnä on lanka, jonka pituus on l ja poikkipinta-ala A. Sen resistanssi on R. Keskellä on kaksi kertaa pidempi lanka, jonka poikkipinta-ala on sama. Sen resistanssi on 2R. Alinna on yhtä pitkä lanka, jonka poikkipinta-ala on kaksinkertainen. Sen resistanssi on puolet eli R jaettuna kahdella. Poikkipinta on korostettu oranssilla langan vasemmassa päässä." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy63-cu" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc078"/><stop offset="0.4" stop-color="#b8622d"/><stop offset="1" stop-color="#b8622d"/></linearGradient></defs>
  <rect x="96" y="50" width="190" height="24" fill="url(#fy63-cu)"/>
  <line x1="96" y1="50" x2="286" y2="50" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="96" y1="74" x2="286" y2="74" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="286" cy="62" rx="5" ry="12" fill="#b8622d" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="96" cy="62" rx="5" ry="12" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="38" y="47.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$A$</div></foreignObject>
  <line x1="96" y1="85" x2="96" y2="99" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="286" y1="85" x2="286" y2="99" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="171" y1="92" x2="107" y2="92" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M98,92 L108,87.5 L108,96.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="211" y1="92" x2="275" y2="92" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M284,92 L274,96.5 L274,87.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="173" y="77.5" width="36" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$l$</span></div></foreignObject>
  <foreignObject x="308" y="47.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R$</div></foreignObject>
  <rect x="96" y="154" width="380" height="24" fill="url(#fy63-cu)"/>
  <line x1="96" y1="154" x2="476" y2="154" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="96" y1="178" x2="476" y2="178" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="476" cy="166" rx="5" ry="12" fill="#b8622d" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="96" cy="166" rx="5" ry="12" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="38" y="151.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$A$</div></foreignObject>
  <line x1="96" y1="189" x2="96" y2="203" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="476" y1="189" x2="476" y2="203" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="266" y1="196" x2="107" y2="196" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M98,196 L108,191.5 L108,200.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="306" y1="196" x2="465" y2="196" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M474,196 L464,200.5 L464,191.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="268" y="181.5" width="36" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$2l$</span></div></foreignObject>
  <foreignObject x="498" y="151.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$2R$</div></foreignObject>
  <rect x="96" y="255" width="190" height="34" fill="url(#fy63-cu)"/>
  <line x1="96" y1="255" x2="286" y2="255" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="96" y1="289" x2="286" y2="289" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <ellipse cx="286" cy="272" rx="7" ry="17" fill="#b8622d" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="96" cy="272" rx="7" ry="17" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="38" y="257.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2A$</div></foreignObject>
  <line x1="96" y1="300" x2="96" y2="314" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="286" y1="300" x2="286" y2="314" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="171" y1="307" x2="107" y2="307" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M98,307 L108,302.5 L108,311.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="211" y1="307" x2="275" y2="307" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M284,307 L274,311.5 L274,302.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="173" y="292.5" width="36" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$l$</span></div></foreignObject>
  <foreignObject x="308" y="243" width="60" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\dfrac{R}{2}$</div></foreignObject>
</svg>

Resistiivisyys on aineen ominaisuus. Se kertoo, kuinka huonosti aine johtaa sähköä. Metallien resistiivisyys kasvaa, kun lämpötila nousee. Konstantaanin resistiivisyys muuttuu lämpötilan mukana hyvin vähän. Siksi konstantaanista tehdään tarkkoja vastuksia. Lämmityslangat tehdään kromnikkelistä, koska sen resistiivisyys on suuri. Taulukon arvot ovat yksikössä $\Omega\cdot\text{m}$ huoneenlämmössä ($20\,{}^\circ\text{C}$).

| aine | resistiivisyys $\rho$ |
|---|---|
| hopea | $1{,}6 \cdot 10^{-8}$ |
| kupari | $1{,}7 \cdot 10^{-8}$ |
| alumiini | $2{,}7 \cdot 10^{-8}$ |
| rauta | $1{,}0 \cdot 10^{-7}$ |
| konstantaani | $5{,}0 \cdot 10^{-7}$ |
| kromnikkeli | $1{,}1 \cdot 10^{-6}$ |

Kuparin resistiivisyys on pieni. Siksi paksut kuparijohtimet päästävät virran läpi lähes ilman jännitehäviötä. Jännitehäviö tarkoittaa, että jännitettä jää johtoon eikä se ehdi laitteelle. Leivänpaahtimen lanka on kromnikkeliä, ja sen resistiivisyys on yli 60-kertainen kupariin verrattuna. Lisäksi lanka on ohut. Siksi sen resistanssi on suuri, ja juuri lanka lämpenee.

```pysahdy
Lanka korvataan samaa ainetta olevalla langalla. Uuden langan pituus ja poikkipinta-ala ovat kumpikin kaksinkertaiset. Miten resistanssi muuttuu?
---
Se ei muutu. Kaavassa $R = \rho \tfrac{l}{A}$ sekä $l$ että $A$ kaksinkertaistuvat. Siksi suhde $\tfrac{l}{A}$ pysyy samana.
```

## Esimerkki
Konstantaanilangasta halutaan tehdä vastus, jonka resistanssi on $12\,\Omega$. Langan poikkipinta-ala on $0{,}20\,\text{mm}^2$. Kuinka pitkä lanka tarvitaan? Konstantaanin resistiivisyys on $5{,}0 \cdot 10^{-7}\,\Omega\cdot\text{m}$.

<!-- vaihe -->

**Tunnetut ja kysytty.** $R = 12\,\Omega$, $A = 0{,}20\,\text{mm}^2$ ja $\rho = 5{,}0 \cdot 10^{-7}\,\Omega\cdot\text{m}$.

Kysytään langan pituutta $l$.

<!-- vaihe -->

**Periaate.** Lanka on tasapaksu ja samaa ainetta. Sen resistanssi on verrannollinen pituuteen ja kääntäen verrannollinen poikkipinta-alaan. Konstantaanin resistiivisyys pysyy lähes samana, vaikka lanka lämpenisi käytössä. Siksi taulukon arvo kelpaa.

<!-- vaihe -->

**Kaava ratkaistuna.** Pituus ratkaistaan kertomalla yhtälö molemmilla puolilla $A$:lla ja jakamalla $\rho$:lla:
```latex
\begin{aligned}
R &= \rho \frac{l}{A} \\
l &= \frac{R A}{\rho}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Poikkipinta-ala muutetaan neliömetreiksi: $0{,}20\,\text{mm}^2 = 0{,}20 \cdot (10^{-3}\,\text{m})^2 = 0{,}20 \cdot 10^{-6}\,\text{m}^2$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
l &= \frac{R A}{\rho} \\
&= \frac{12\,\Omega \cdot 0{,}20 \cdot 10^{-6}\,\text{m}^2}{5{,}0 \cdot 10^{-7}\,\Omega\cdot\text{m}} \\
&= 4{,}8\,\text{m}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Lankaa tarvitaan $4{,}8\,\text{m}$. Tulos on annettu kahdella merkitsevällä numerolla. Resistanssi, poikkipinta-ala ja resistiivisyys on nimittäin annettu kahdella numerolla.

<!-- vaihe -->

**Järkevyys.** Yksi metri tätä lankaa on $$\begin{aligned} &5{,}0 \cdot 10^{-7}\,\Omega\cdot\text{m} \cdot 1{,}0\,\text{m} \\ &: (0{,}20 \cdot 10^{-6}\,\text{m}^2) \\ &= 2{,}5\,\Omega \end{aligned}$$. Siksi $12\,\Omega$ vaatii vajaat viisi metriä: $12\,\Omega : 2{,}5\,\Omega = 4{,}8$. Yksiköt menevät oikein: $\Omega \cdot \text{m}^2 : (\Omega\cdot\text{m}) = \text{m}$. Valmis vastus päästäisi jännitteellä $6{,}0\,\text{V}$ läpi virran $6{,}0\,\text{V} : 12\,\Omega = 0{,}50\,\text{A}$.

## Yleinen virhekäsitys
Moni päättelee kaavasta $R = U : I$, että resistanssi kasvaa, kun jännite kasvaa. Ohmin lakia noudattavan vastuksen resistanssi pysyy kuitenkin melkein samana, kun lämpötila ja muut olosuhteet pysyvät samoina. Silloin virta on suoraan verrannollinen jännitteeseen. Kun jännite kaksinkertaistuu, myös virta kaksinkertaistuu. Suhde pysyy samana. Resistanssi riippuu johtimen aineesta, pituudesta, paksuudesta ja lämpötilasta. Hehkulampun resistanssi kasvaa jännitteen mukana vain siksi, että suurempi virta kuumentaa lankaa.

Toinen virhekäsitys on, että virta kuluu vastuksessa. Vastuksen jälkeen virta on yhtä suuri kuin ennen vastusta, koska varaus ei katoa matkalla. Vastuksessa sähköenergiaa muuttuu sisäenergiaksi. Virta ei muutu miksikään.

## Tiivistelmä
- Resistanssi $R = U : I$ kertoo, kuinka paljon komponentti vastustaa sähkövirtaa. Yksikkö on ohmi, $1\,\Omega = 1\,\text{V/A}$.
- Resistanssi mitataan virtamittarilla, joka on sarjassa komponentin kanssa, ja jännitemittarilla, joka on rinnan komponentin kanssa.
- Ohmin laki: metallijohtimen virta on suoraan verrannollinen jännitteeseen, kun lämpötila pysyy samana, $U = RI$.
- Ominaiskäyrä näyttää komponentin jännitteen ja virran riippuvuuden. Vastuksen ominaiskäyrä on suora, joka kulkee origon kautta. Hehkulampun ominaiskäyrä on kaareva, koska kuuman langan resistanssi on suurempi.
- Johtimen resistanssi on $R = \rho l : A$. Se kasvaa pituuden mukana ja pienenee paksuuden mukana. Se riippuu myös aineen resistiivisyydestä $\rho$.
