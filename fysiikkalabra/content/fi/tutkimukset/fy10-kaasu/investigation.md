# Kaasun tilanyhtälön kokeellinen tutkiminen

> **Tutkimuskysymys:** Miten suljetun kaasun paine riippuu sen tilavuudesta ja lämpötilasta, ja kuinka hyvin mittaukset noudattavat ideaalikaasun mallia?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratorion työpöydällä on vasemmalla mäntäruisku, joka on liitetty lyhyellä letkulla paineanturiin. Keskellä lasikolvi on upotettu vesihauteeseen, ja sen tulpasta lähtee letku toiseen paineanturiin hauteen ulkopuolella. Hauteessa on myös lämpötila-anturi. Oikealla on astia jäävettä ja vedenkeitin. Taaempana on kannettava tietokone, johon anturit on kytketty johdoilla." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy10kh-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#dfe9ef"/></linearGradient><linearGradient id="fy10kh-desk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><linearGradient id="fy10kh-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy10kh-wall)"/>
  <rect x="0" y="470" width="1200" height="130" fill="url(#fy10kh-desk)"/>
  <line x1="0" y1="492" x2="1200" y2="488" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="514" x2="1200" y2="510" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="536" x2="1200" y2="532" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="558" x2="1200" y2="554" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="580" x2="1200" y2="576" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="470" x2="1200" y2="470" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <path d="M470,300 L760,300 L780,330 L450,330 Z" fill="#6c757d" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="490" y="130" width="250" height="170" rx="8" fill="#1f2933" stroke="#1f2933" stroke-width="3"/>
  <rect x="504" y="144" width="222" height="142" fill="#ffffff"/>
  <line x1="514" y1="166" x2="716" y2="166" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="514" y1="186" x2="716" y2="186" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="514" y1="206" x2="716" y2="206" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="514" y1="226" x2="716" y2="226" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="514" y1="246" x2="716" y2="246" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="514" y1="266" x2="716" y2="266" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <line x1="615" y1="152" x2="615" y2="278" stroke="#c9c2b2" stroke-width="2" stroke-linecap="butt"/>
  <rect x="230" y="413" width="97" height="34" fill="#eef5f9"/>
  <rect x="120" y="410" width="210" height="40" rx="4" fill="none" stroke="#1f2933" stroke-width="3"/>
  <rect x="330" y="424" width="22" height="12" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="218" y="413" width="12" height="34" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="50" y="425" width="168" height="10" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="38" y="408" width="12" height="44" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="114" y="398" width="6" height="64" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <line x1="140" y1="410" x2="140" y2="417" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="160" y1="410" x2="160" y2="417" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="180" y1="410" x2="180" y2="417" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="200" y1="410" x2="200" y2="417" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="220" y1="410" x2="220" y2="422" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="410" x2="240" y2="417" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="260" y1="410" x2="260" y2="417" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="280" y1="410" x2="280" y2="417" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="300" y1="410" x2="300" y2="417" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M352,430 C380,430 380,440 400,440" fill="none" stroke="#1f2933" stroke-width="7" stroke-linejoin="round"/>
  <rect x="400" y="418" width="96" height="46" rx="8" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="412" y="430" width="72" height="22" rx="3" fill="#ffffff" stroke="#8a96a3" stroke-width="1.5"/>
  <path d="M496,440 C530,440 520,380 560,340 L560,330" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M600,300 V460 Q600,470 610,470 H820 Q830,470 830,460 V300" fill="#eef5f9" stroke-linejoin="round"/>
  <path d="M603,330 H827 V460 Q827,467 820,467 H610 Q603,467 603,460 Z" fill="url(#fy10kh-water)" stroke-linejoin="round"/>
  <path d="M600,300 V460 Q600,470 610,470 H820 Q830,470 830,460 V300" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="679" y="300" width="22" height="68" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <circle cx="690" cy="410" r="48" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <rect x="681" y="358" width="18" height="12" fill="#eef5f9"/>
  <rect x="675" y="284" width="30" height="20" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M690,284 V252 Q690,232 710,232 H830 Q846,232 846,252 V447 H852" fill="none" stroke="#1f2933" stroke-width="7" stroke-linejoin="round"/>
  <rect x="852" y="424" width="96" height="46" rx="8" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="864" y="436" width="72" height="22" rx="3" fill="#ffffff" stroke="#8a96a3" stroke-width="1.5"/>
  <path d="M900,424 C900,360 800,340 765,318" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="781" y="290" width="10" height="160" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="776" y="270" width="20" height="26" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M786,270 C786,230 760,250 740,300" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M970,340 V460 Q970,470 980,470 H1080 Q1090,470 1090,460 V340" fill="#eef5f9" stroke-linejoin="round"/>
  <path d="M973,370 H1087 V460 Q1087,467 1080,467 H980 Q973,467 973,460 Z" fill="url(#fy10kh-water)" stroke-linejoin="round"/>
  <path d="M970,340 V460 Q970,470 980,470 H1080 Q1090,470 1090,460 V340" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="970" y="372" width="32" height="28" rx="5" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2"/>
  <rect x="1006" y="366" width="32" height="28" rx="5" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2"/>
  <rect x="1042" y="374" width="32" height="28" rx="5" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2"/>
  <rect x="988" y="404" width="32" height="28" rx="5" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2"/>
  <rect x="1026" y="410" width="32" height="28" rx="5" fill="#a5d8ff" stroke="#4f8fbf" stroke-width="2"/>
  <path d="M1150,392 Q1180,392 1180,420 Q1180,452 1162,456" fill="none" stroke="#1f2933" stroke-width="8" stroke-linejoin="round"/>
  <path d="M1100,470 L1108,384 Q1112,364 1132,364 H1140 Q1158,364 1160,384 L1166,470 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M1104,420 L1090,404" fill="none" stroke="#1f2933" stroke-width="6" stroke-linejoin="round"/>
  <rect x="1118" y="354" width="34" height="12" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <g transform="translate(150,530) rotate(-5)"><rect x="-90" y="-36" width="210" height="68" rx="4" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/><line x1="-74" y1="-20" x2="104" y2="-20" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/><line x1="-74" y1="-8" x2="104" y2="-8" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/><line x1="-74" y1="4" x2="104" y2="4" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/><line x1="-74" y1="16" x2="104" y2="16" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/><line x1="-74" y1="28" x2="104" y2="28" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/></g>
</svg>

Polkupyörän pumpun mäntä käy yhä raskaammaksi, kun suuaukkoa pitää sormella kiinni, ja auton renkaiden paine on pakkasaamuna eri kuin helteellä. Kaasun paine, tilavuus ja lämpötila riippuvat siis toisistaan. Tässä tutkimuksessa selvität mittaamalla, millaisia riippuvuudet ovat, ja testaat, kuvaako ideaalikaasun malli niitä. Mittaa, piirrä ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** ainakin kahdella mittaussarjalla, miten suljetun ilmamäärän paine riippuu tilavuudesta, kun lämpötila pysyy samana, ja miten paine riippuu lämpötilasta, kun tilavuus pysyy samana. Etsi kummallekin riippuvuudelle kuvaajasta sopiva malli, ilmoita mallin vakiot epävarmuuksineen ja arvioi, kuinka hyvin tulokset sopivat ideaalikaasun malliin.

**Päätät itse:** mittausjärjestelyt, sen, miten pidät kummassakin sarjassa yhden suureen ja kaasun määrän vakiona, mittausalueet ja mittauspisteiden määrän, sen, kuinka kauan odotat ennen lukemaa, kuvaajien akselit perusteluineen sekä tavan, jolla arvioit tulosten epävarmuuden. Osittain ohjatussa työtavassa sivu antaa valmiiksi mittausjärjestelyt, mallit ja kuvaajien akselit sekä ehdottaa tapoja arvioida epävarmuus; päätät silloin itse mittausalueet, mittauspisteiden määrän, odotusajan ja sen, miten varmistat, että vakioksi tarkoitettu suure ja kaasun määrä pysyvät vakioina. Itsenäisessä työtavassa teet kaikki luetellut valinnat ja perustelet mallit itse.

::: tuki I
**Itsenäinen työtapa.** Laajennus, sarjojen yhdistäminen tilanyhtälöksi, kuuluu työhösi.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Ruiskuun suljetun ilman tilavuus puolitetaan hitaasti. Mitä paineelle tapahtuu? Muuttuuko tulos, jos männän painaa sisään hyvin nopeasti ja luet paineen heti?
2. Suljetun lasiastian ilma lämpenee $20\,{}^\circ\text{C}$:sta $40\,{}^\circ\text{C}$:seen, ja astian tilavuus pysyy samana. Kaksinkertaistuuko paine? Perustele.
3. Millainen on paineen ja tilavuuden välinen kuvaaja? Millainen riippuvuus paineen ja tilavuuden välillä mielestäsi on, ja voiko sen nähdä suoraan tästä kuvaajasta?
4. Mikä mittausjärjestelyssä voisi saada tulokset poikkeamaan mallista, ja mihin suuntaan?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Tutkimuskysymyksestä mitattaviksi suureiksi

Kolme suuretta muuttuu yhtä aikaa, mutta riippuvuuden voi nähdä luotettavasti vain, kun yksi niistä pysyy vakiona. Ennen kuin luet eteenpäin, kirjaa kummastakin mittaussarjasta:

1. Mikä tilanmuuttuja pysyy vakiona, ja miten varmistat sen? Miten varmistat, ettei kaasun määrä muutu?
2. Mitä muutat ja mitä mittaat, ja millä välineellä luet kunkin suureen?
3. Millaisen kuvaajan avulla voit päätellä, onko riippuvuus suoraa verrannollisuutta, kääntäistä verrannollisuutta vai jotain muuta?

## Teoriaa lyhyesti

Suljetun kaasumäärän tilaa kuvaavat paine $p$, tilavuus $V$ ja lämpötila $T$. Kun kaasua ei pääse vuotamaan pois eikä tulemaan lisää, kaasun ainemäärä $n$ pysyy samana. Mikromallin mukaan paine syntyy kaasun hiukkasten törmäyksistä astian seinämiin: paine kasvaa, kun hiukkaset osuvat seinämiin useammin tai suuremmalla nopeudella. Pienemmässä tilavuudessa samat hiukkaset osuvat seinämiin useammin, ja lämpimässä kaasussa hiukkaset liikkuvat keskimäärin nopeammin. [[apua:fy3-9|Kaasujen tilanmuutokset]]

**Ideaalikaasun mallissa** hiukkasten väliset vuorovaikutukset jätetään huomiotta. Malli kuvaa ilmaa hyvin tavallisissa paineissa ja lämpötiloissa, mutta se alkaa pettää suurissa paineissa ja matalissa lämpötiloissa. Kaasun malleissa lämpötila ilmoitetaan kelvineinä: $T = \theta + 273{,}15\,\text{K}$, missä $\theta$ on celsiuslämpötilan lukuarvo. Paineena käytetään kaasun kokonaispainetta, ei ylipainetta ilmanpaineeseen nähden. [[apua:fy3-10|Ideaalikaasun tilanyhtälö]]

Riippuvuuden muodon näkee luotettavimmin kuvaajasta, jossa mallin mukaiset pisteet asettuvat suoralle. Suoraa verrannollisuutta vastaa origon kautta kulkeva suora. Kaarevasta kuvaajasta on vaikea päätellä, mikä riippuvuus on kyseessä, joten akseleille kannattaa silloin valita mitatuista suureista laskettuja suureita.

::: tuki OO
**Tarkista kirjauksesi tästä.** Kun lämpötila ja kaasun määrä pysyvät vakioina (**isoterminen** tilanmuutos), ideaalikaasun mallin mukaan paineen ja tilavuuden tulo on vakio (Boylen laki):

```latex
\begin{aligned}
pV &= \text{vakio} \\
p &= \text{vakio} \cdot \frac{1}{V}
\end{aligned}
```

missä vakio on tulo $pV$. Paine on siis kääntäen verrannollinen tilavuuteen. $(V, p)$-kuvaaja on laskeva kaari, mutta paine tilavuuden käänteisluvun $\dfrac{1}{V}$ funktiona on origon kautta kulkeva suora, jonka kulmakerroin on tulo $pV$. Tilavuus $V$ on koko suljetun kaasun tilavuus, myös letkussa ja anturissa oleva osa.

<svg data-fig="boyle" viewBox="0 0 600 330" role="img" aria-label="Kuvaaja: paine p tilavuuden käänteisluvun yksi per V funktiona ideaalikaasun mallin mukaan, kun lämpötila ja kaasun määrä pysyvät samoina. Kuvaaja on origon kautta kulkeva suora, jonka kulmakerroin on tulo p kertaa V. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="280" x2="484" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,280 L483,286 L483,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="281" x2="90" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,24 L96,37 L84,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="60" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="251" width="20" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\dfrac{1}{V}$</div></foreignObject>
  <foreignObject x="80" y="-6.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p$</div></foreignObject>
  <polyline points="90,280 451,83.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="127.5" y="104.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kulmakerroin } pV$</div></foreignObject>
</svg>

Kun tilavuus ja kaasun määrä pysyvät vakioina (**isokoorinen** tilanmuutos), mallin mukaan paine on suoraan verrannollinen kelvinlämpötilaan:

```latex
\begin{aligned}
\frac{p}{T} &= \text{vakio} \\
p &= \text{vakio} \cdot T
\end{aligned}
```

missä vakio on suhde $\dfrac{p}{T}$ ja $T$ kelvinlämpötila. Paine kelvinlämpötilan funktiona on siis origon kautta kulkeva suora. Mittaukset tehdään vain lämpötiloissa, joissa vesihaude on nestettä, joten origoon päästään vain jatkamalla suoraa mittausalueen ulkopuolelle. Jos lämpötila merkitään celsiusasteina, suora ei kulje origon kautta, vaan sen jatke leikkaa vaaka-akselin lämpötilassa, jossa paine olisi mallin mukaan nolla. Mallia sovellettaessa oletetaan lisäksi, että koko kaasu on hauteen lämpötilassa ja että astiassa on vain kaasua: jos astiassa on vettä, se höyrystyy lämmetessään, ja vesihöyry kasvattaa painetta.

<svg data-fig="isokoori" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja: paine p kelvinlämpötilan T funktiona ideaalikaasun mallin mukaan, kun tilavuus ja kaasun määrä pysyvät samoina. Kuvaaja on suora, joka kulkee origon kautta. Yhtenäinen osa suorasta on alueella, jolla vesihaude on nestettä, noin 273 kelvinistä 373 kelviniin. Katkoviivalla piirretty jatke ulottuu origoon eli nollaan kelviniin. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="270" x2="484" y2="270" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,270 L483,276 L483,264 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="271" x2="90" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,24 L96,37 L84,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="349.5" y1="270" x2="349.5" y2="277" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="327" y="279.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$273$</div></foreignObject>
  <line x1="444.5" y1="270" x2="444.5" y2="277" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="422" y="279.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$373$</div></foreignObject>
  <foreignObject x="502" y="255.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T\ (\text{K})$</div></foreignObject>
  <foreignObject x="80" y="-6.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p$</div></foreignObject>
  <foreignObject x="80" y="279.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <polyline points="90,270 349.5,137.5" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="10 8"/>
  <polyline points="349.5,137.5 444.5,89" fill="none" stroke="#1f2933" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="349.5" y1="137.5" x2="349.5" y2="270" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="444.5" y1="89" x2="444.5" y2="270" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="324.5" y="309.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{mittausalue}$</div></foreignObject>
  <foreignObject x="178.5" y="162.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{jatke}$</div></foreignObject>
</svg>

Molemmat riippuvuudet seuraavat ideaalikaasun tilanyhtälöstä $pV = nRT$, kun kaasun määrä $n$ ja lisäksi joko $T$ tai $V$ pysyvät vakioina.
:::

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös kummastakin sarjasta, mitä muutat, mitä mittaat ja mitä pidät vakiona, sekä mittausalue ja mittauspisteiden määrä. Mittauspisteitä tarvitaan niin monta ja niin laajalta alueelta, että riippuvuuden muodon voi päätellä kuvaajasta.

**Selvitä ensin paineanturin tyyppi.** Avaa anturin letku huoneilmaan ja lue anturin lukema. Jos lukema on noin $100\,\text{kPa}$, anturi näyttää kokonaispaineen. Jos lukema on lähellä nollaa, anturi näyttää ylipaineen ilmanpaineeseen nähden, ja kokonaispaine saadaan lisäämällä lukemaan ilmanpaine. Ilmanpaineen saat koulun ilmanpuntarista (barometrista) tai lähimmän sääaseman tiedoista. Sääpalvelut ilmoittavat yleensä merenpinnan tasolle muunnetun paineen; jos koulu on selvästi merenpintaa korkeammalla, paikallinen ilmanpaine on hieman pienempi. Kirjaa anturin tyyppi ja käyttämäsi ilmanpaine.

::: tuki OO
**Osittain ohjattu.** Ensimmäisessä sarjassa ruiskuun suljetaan ilmaa, ja ruisku liitetään paineanturiin. Muutat tilavuutta $V$ männällä ja luet jokaisella tilavuudella paineen $p$. Toisessa sarjassa suljettu, kuiva lasiastia on liitetty paineanturiin, ja astia upotetaan vuorotellen eri lämpötilaisiin vesihauteisiin. Luet hauteen lämpötilan $\theta$ lämpötila-anturista ja paineen $p$ paineanturista.

<svg data-fig="setup" viewBox="0 0 600 470" role="img" aria-label="Kaaviokuva kahdesta mittausjärjestelystä. Ylhäällä mäntäruisku, jonka tilavuus V luetaan ruiskun asteikolta, on liitetty lyhyellä letkulla paineanturiin, joka mittaa paineen p. Alhaalla lasikolvi on upotettu vesihauteeseen. Kolvin tulpasta lähtee lyhyt letku hauteen ulkopuolella olevaan paineanturiin, joka mittaa paineen p. Hauteessa kolvin vieressä on lämpötila-anturi, joka mittaa hauteen lämpötilan theta." style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy10ks-water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient></defs>
  <rect x="230" y="71" width="127" height="38" fill="#eef5f9"/>
  <rect x="150" y="68" width="210" height="44" rx="4" fill="none" stroke="#1f2933" stroke-width="3"/>
  <rect x="360" y="84" width="22" height="12" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="218" y="71" width="12" height="38" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="80" y="85" width="138" height="10" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="68" y="66" width="12" height="48" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="144" y="56" width="6" height="68" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <line x1="170" y1="68" x2="170" y2="75" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="190" y1="68" x2="190" y2="75" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="210" y1="68" x2="210" y2="75" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="230" y1="68" x2="230" y2="75" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="250" y1="68" x2="250" y2="80" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="270" y1="68" x2="270" y2="75" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="290" y1="68" x2="290" y2="75" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="310" y1="68" x2="310" y2="75" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="330" y1="68" x2="330" y2="75" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="230" y1="46" x2="382" y2="46" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="230" y1="38" x2="230" y2="54" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="382" y1="38" x2="382" y2="54" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="296" y="9.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$V$</div></foreignObject>
  <path d="M382,90 H440" fill="none" stroke="#1f2933" stroke-width="7" stroke-linejoin="round"/>
  <rect x="440" y="67" width="96" height="46" rx="8" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="452" y="79" width="72" height="22" rx="3" fill="#ffffff" stroke="#8a96a3" stroke-width="1.5"/>
  <foreignObject x="415.5" y="121.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{paineanturi}$</div></foreignObject>
  <foreignObject x="552" y="75.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p$</div></foreignObject>
  <foreignObject x="213.5" y="125.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{ruisku}$</div></foreignObject>
  <line x1="20" y1="176" x2="580" y2="176" stroke="#e3dccb" stroke-width="2" stroke-linecap="butt"/>
  <path d="M70,250 V440 Q70,450 80,450 H340 Q350,450 350,440 V250" fill="#eef5f9" stroke-linejoin="round"/>
  <path d="M73,280 H347 V440 Q347,447 340,447 H80 Q73,447 73,440 Z" fill="url(#fy10ks-water)" stroke-linejoin="round"/>
  <path d="M70,250 V440 Q70,450 80,450 H340 Q350,450 350,440 V250" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="169" y="240" width="22" height="78" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <circle cx="180" cy="370" r="58" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <rect x="171" y="308" width="18" height="12" fill="#eef5f9"/>
  <rect x="165" y="224" width="30" height="20" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M180,224 V212 Q180,200 192,200 H478 Q498,200 498,220 V226" fill="none" stroke="#1f2933" stroke-width="7" stroke-linejoin="round"/>
  <rect x="450" y="226" width="96" height="46" rx="8" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="462" y="238" width="72" height="22" rx="3" fill="#ffffff" stroke="#8a96a3" stroke-width="1.5"/>
  <foreignObject x="558" y="234.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p$</div></foreignObject>
  <foreignObject x="425.5" y="281.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{paineanturi}$</div></foreignObject>
  <rect x="296" y="260" width="10" height="160" rx="4" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="291" y="236" width="20" height="28" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="306" y1="380" x2="366" y2="380" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="372" y="347.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\theta$</div></foreignObject>
  <foreignObject x="372" y="381.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{lämpötila-anturi}$</div></foreignObject>
  <foreignObject x="150" y="417.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#ffffff">$\text{vesihaude}$</div></foreignObject>
</svg>

Päätä itse tilavuudet, lämpötilat ja mittauspisteiden määrä, mutta mieti ainakin näitä:

- **Ruiskun alkutilavuus.** Aseta mäntä haluamaasi alkutilavuuteen ennen kuin liität ruiskun anturiin, jolloin paine on aluksi ilmanpaine. Jos kaasu puristetaan puoleen tilavuudesta, paine kaksinkertaistuu suunnilleen: varmista, että suurin paine jää anturin sallitun alueen alapuolelle.
- **Lämpötila ruiskussa.** Puristaminen lämmittää ilmaa hetkeksi. Muuta tilavuutta rauhallisesti ja odota, että lukema asettuu. Pidä kiinni männän päästä, ei ruiskun säiliöstä, jotta käden lämpö ei lämmitä ilmaa.
- **Vuoto.** Miten huomaat, jos ilmaa pääsee vuotamaan? Voit palata mittaussarjan lopuksi alkutilavuuteen ja verrata painetta alkuarvoon.
- **Lasiastia.** Upota astia hauteeseen niin syvälle kuin mahdollista ja pidä letku lyhyenä, jotta mahdollisimman suuri osa kaasusta on hauteen lämpötilassa. Sekoita haudetta ja odota, että sekä lämpötila- että painelukema ovat asettuneet.
- **Lämpötila-alue.** Jäävesi, huoneenlämpöinen vesi ja kuuma vesi antavat laajan alueen. Välilämpötiloja saat sekoittamalla kylmää ja kuumaa vettä.
:::

## Mittaa

Kirjaa alkuperäiset mittaustulokset taulukkoon heti mittauksen aikana. Laskemasi suureet saavat omat sarakkeensa mitattujen oikealle puolelle.

::: tuki OO
Voit käyttää esimerkiksi tällaisia taulukoita:

| $V\ (\text{ml})$ | $p\ (\text{kPa})$ | $\dfrac{1}{V}\ \left(\dfrac{1}{\text{ml}}\right)$ | $pV\ (\text{kPa} \cdot \text{ml})$ |
|---|---|---|---|
| | | | |
| | | | |

| $\theta\ ({}^\circ\text{C})$ | $p\ (\text{kPa})$ | $T\ (\text{K})$ | $\dfrac{p}{T}\ \left(\dfrac{\text{kPa}}{\text{K}}\right)$ |
|---|---|---|---|
| | | | |
| | | | |

Kirjaa lisäksi ruiskun alkutilavuus ja alkupaine, huoneen lämpötila ruiskusarjan aikana sekä se, missä järjestyksessä hauteet mitattiin.
:::

Muista mittausepävarmuus: kirjaa, kuinka tarkasti luet tilavuuden ruiskun asteikolta, ja kuinka paljon paineen ja lämpötilan lukemat vaihtelevat, kun ne ovat asettuneet. [[apua:fy1-3|Mittausepävarmuuden arvioiminen]]

## Käsittele tulokset

Piirrä kummastakin mittaussarjasta kuvaaja, jossa mallin mukaiset pisteet asettuvat suoralle. Merkitse akseleille suureet ja yksiköt. Piirrä mittauspisteet, älä yhdistä niitä murtoviivalla, ja sovita pisteisiin suora. [[apua:fy1-4|Suoran sovittaminen ja kulmakertoimen tulkinta]]

Kirjoita kummankin sovitetun suoran yhtälö ja vastaa:

1. Ovatko pisteet suoralla? Jos eivät, millä alueella ne poikkeavat, ja mihin suuntaan?
2. Mitä suoran kulmakerroin kertoo kaasusta, ja mikä on sen yksikkö?
3. Kulkeeko suora origon kautta mittausepävarmuuden rajoissa? Jos ei, mistä vakiotermi voi johtua?

::: tuki OO
**Akselit.** Ruiskusarjassa valitse pystyakselille paine $p$ ja vaaka-akselille $\dfrac{1}{V}$. Kulmakerroin on tulo $pV$, jonka yksikkö on $\text{kPa} \cdot \text{ml}$, ja $1\,\text{kPa} \cdot \text{ml} = 1\,\text{mJ}$. Laske lisäksi tulo $pV$ jokaiselle mittaukselle: pysyykö se vakiona, vai muuttuuko se järjestelmällisesti tilavuuden mukana?

Lasiastiasarjassa valitse pystyakselille paine $p$ ja vaaka-akselille kelvinlämpötila $T$, ja aloita vaaka-akseli nollasta, jotta näet, osuuko suoran jatke origoon. Saman voi tutkia celsiusasteikolla jatkamalla suoraa nollapaineeseen. Tapa on esitetty luvussa [[apua:fy3-13|Absoluuttisen nollapisteen määrittäminen]].

**Jos ruiskusarjan suora ei kulje origon kautta.** Syitä on kaksi tavallista, ja ne erottaa toisistaan vakiotermin etumerkistä.

- *Ylipaine.* Jos käytit ylipainetta näyttävän anturin lukemia lisäämättä niihin ilmanpainetta, pisteet ovat suoralla, mutta suoran vakiotermi on negatiivinen, suunnilleen $-p_\text{ilma}$, missä $p_\text{ilma}$ on ilmanpaine. Korjaus: lisää ilmanpaine jokaiseen lukemaan.
- *Letkun ja anturin tilavuus.* Jos vakiotermi on positiivinen ja pisteet kaartuvat hieman alaspäin suurimmilla $\dfrac{1}{V}$:n arvoilla, syy on todennäköisesti tämä.

Letkussa ja anturissa on ilmaa, jonka tilavuus $V_0$ ei näy ruiskun asteikolla, joten koko kaasun tilavuus on $V + V_0$. Mallin mukaan $(V + V_0)\,p = \text{vakio}$, josta saadaan

```latex
V = \text{vakio} \cdot \frac{1}{p} - V_0
```

Kun piirrät ruiskun lukeman $V$ paineen käänteisluvun $\dfrac{1}{p}$ funktiona, suoran vakiotermi on $-V_0$. Näin voit arvioida letkun ja anturin tilavuuden ja korjata sen tuloksiin.
:::

Kuvaajan sovitukseen ja laskettuihin sarakkeisiin voit käyttää esimerkiksi Graphical Analysis -ohjelmaa tai taulukkolaskentaa. Ruukkilabran ohjeet: [[ohje:tvt-suoran-sovitus|Suoran sovittaminen]], [[ohje:tvt-kulmakerroin|Kulmakertoimen tulkinta]] ja [[ohje:tvt-taulukkolaskenta|Taulukkolaskenta]].

## Epävarmuus ja luotettavuus

Ilmoita kummankin suoran kulmakerroin muodossa $a \pm \Delta a$ yksikköineen ja perustele, miten arvioit epävarmuuden. Ilmoita myös, osuuko paine–lämpötila-sarjan suoran jatke origoon epävarmuuden rajoissa, tai ilmoita lämpötila, jossa paine olisi mallin mukaan nolla, epävarmuuksineen.

::: tuki OO
Kulmakertoimen epävarmuuden voit arvioida jommallakummalla tavalla:

- **Sovitusohjelman keskivirhe.** Monet ohjelmat ilmoittavat kulmakertoimen ja vakiotermin keskivirheet. Käytä niitä epävarmuuksina.
- **Jyrkin ja loivin suora.** Piirrä jyrkin ja loivin suora, jotka vielä sopivat pisteisiin niiden epävarmuuksien rajoissa. Määritä niiden kulmakertoimet $a_\text{max}$ ja $a_\text{min}$ ja arvioi epävarmuus vaihteluvälin puolikkaana: $\Delta a = \dfrac{a_\text{max} - a_\text{min}}{2}$.

Laskettujen suureiden epävarmuudet: käänteisluvun $\dfrac{1}{V}$ suhteellinen epävarmuus on sama kuin tilavuuden suhteellinen epävarmuus $\dfrac{\Delta V}{V}$. Tulon $pV$ suhteellinen epävarmuus on paineen ja tilavuuden suhteellisten epävarmuuksien summa. Kelvinlämpötilan epävarmuus on sama kuin celsiuslämpötilan, $\Delta T = \Delta\theta$, koska lisätty $273{,}15$ on tarkka luku.

Pyöristä epävarmuus yhteen merkitsevään numeroon ja tulos samaan desimaaliin.

**Virheen suunta paine–lämpötila-sarjassa.** Letkussa ja anturissa oleva ilma pysyy suunnilleen huoneen lämpötilassa, vaikka haude lämpenee tai jäähtyy. Siksi paine muuttuu hauteen lämpötilan mukana vähemmän kuin mallin mukaan, suoran kulmakerroin jää liian pieneksi, ja suoran jatke osuu nollapaineeseen vasta alle $0\,\text{K}$:n lämpötilassa eli kylmemmässä kuin $-273{,}15\,{}^\circ\text{C}$. Mitä suurempi letkun osuus kaasun tilavuudesta on, sitä suurempi on poikkeama.
:::

Pohdi sitten luotettavuutta konkreettisesti: pysyikö vakioksi tarkoitettu suure todella vakiona, pysyikö kaasun määrä samana, ja oliko koko kaasu samassa lämpötilassa? Mitkä olivat suurimmat epävarmuuden lähteet? Olivatko ne satunnaisia vai systemaattisia, ja mihin suuntaan systemaattiset virheet olisivat muuttaneet tuloksia? Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Miten paine riippuu tilavuudesta ja miten lämpötilasta? Käyttäytyikö tutkittu kaasu ideaalikaasun mallin mukaisesti koko mittausalueella, ja mitä oletuksia mittauksiin liittyi? Viittaa kuvaajiin, esimerkiksi "kuvaajasta 1 nähdään, että …". Vertaa tuloksia ennusteeseesi: mikä osui oikeaan ja mikä ei?

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla (kuvaajista ja tuloksista ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]) ja käy läpi sen kaikki osat. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tausta ja teoria:** ideaalikaasun malli, miksi lämpötila ilmoitetaan kelvineinä ja miksi valitsit juuri nämä akselit.
- **Koejärjestely ja menetelmä:** kummankin sarjan vakiona pidetyt suureet ja miten varmistit ne, piirros järjestelyistä sekä työturvallisuus.
- **Mittaustulokset:** alkuperäiset lukemat omissa sarakkeissaan ja lasketut suureet niiden oikealla puolella.
- **Tulos:** kummankin suoran kulmakerroin epävarmuuksineen oikein pyöristettynä sekä tulos origon kohdalta.
- **Luotettavuus:** miten hyvin oletukset pitivät, konkreettiset epävarmuuden lähteet ja niiden vaikutuksen suunta.

## Laajennus: sarjojen yhdistäminen tilanyhtälöksi

Kumpikin mittaussarja tutki vain kahta tilanmuuttujaa kerrallaan. Ideaalikaasun mallissa kaikki kolme yhdistyvät: kun kaasun määrä pysyy samana, suure $\dfrac{pV}{T}$ on vakio, joka on tilanyhtälön mukaan $nR$.

Tee ruiskusarja uudelleen toisessa lämpötilassa, esimerkiksi niin, että ruiskun ilmaa sisältävä osa on lämpimässä vesihauteessa ja paineanturi pysyy kuivana. Vertaa kahden lämpötilan suorien kulmakertoimia: mitä mallin mukaan pitäisi tapahtua, ja tapahtuiko niin? Laske suure $\dfrac{pV}{T}$ kummankin sarjan mittauksille. Pysyykö se samana epävarmuuksien rajoissa? Päällekkäiset epävarmuusvälit tarkoittavat, että tulokset ovat sopusoinnussa, eivät sitä, että ne on todistettu samoiksi. Mikä mittausjärjestelyssäsi rajoittaa sitä, kuinka hyvin voit testata yhdistettyä mallia?

::: tuki OO
**Vihjeitä.** Mallin mukaan ruiskusarjan kulmakerroin on $pV = nRT$, joten se on suoraan verrannollinen kelvinlämpötilaan, kun kaasun määrä on sama. Jos täytät ruiskun uudelleen eri lämpötilassa, kaasun määrä voi muuttua. Jos käytät samaa ilmaa, liitä ruisku anturiin ennen lämmittämistä ja tarkista, ettei mikään vuoda. Anna ilman lämmetä hauteen lämpötilaan ennen ensimmäistä lukemaa. Letkussa ja anturissa oleva ilma ei ole hauteessa, joten pidä letku lyhyenä. Suhteen $\dfrac{pV}{T}$ suhteellinen epävarmuus on paineen, tilavuuden ja lämpötilan suhteellisten epävarmuuksien summa. Kun tunnet suureen $nR$, voit laskea myös ruiskuun suljetun ilman ainemäärän $n$, kun $R = 8{,}31\,\tfrac{\text{J}}{\text{mol} \cdot \text{K}}$.
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi kuvaajiin ja mittaustuloksiin vai siihen, mitä odotit?
- Mitä tekisit toisin, jos aloittaisit alusta?
