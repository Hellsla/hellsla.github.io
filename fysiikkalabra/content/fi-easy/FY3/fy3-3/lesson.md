# Termodynaaminen systeemi, tilanmuuttujat ja lämpötila

> **Miksi** pyörän rengas tuntuu kovemmalta kuumana kesäpäivänä kuin pakkasella, vaikka renkaaseen ei pumpata lisää ilmaa?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: polkupyörä seisoo kuumalla asfaltilla. On helteinen kesäpäivä. Aurinko paistaa, ja kuumuus väreilee asfaltin yllä. Tolpassa on lämpömittari, ja sen punainen pylväs on korkealla." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-3-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Kun tutkit ilmiötä, rajaat tutkittavan osan erilleen muusta maailmasta. Rajattu osa on termodynaaminen systeemi. Kaikki sen ulkopuolella on ympäristö. Pyörän renkaan ilma on esimerkki systeemistä. Jos systeemistä ei pääse ainetta ulos eikä sisään, systeemi on suljettu. Systeemin tilaa kuvataan tilanmuuttujilla. Tilanmuuttujia ovat lämpötila, paine ja tilavuus sekä aineen määrä. Paine on voima pinta-alaa kohti. Paineen yksikkö on pascal (Pa), ja $1\,\text{kPa} = 1000\,\text{Pa}$. Paineeseen tutustutaan tarkemmin myöhemmin. Kun muutat kaasusysteemissä yhtä tilanmuuttujaa, vähintään yksi muista muuttuu myös.

```pysahdy
Pyörän renkaan ilma on systeemi. Mikä on silloin ympäristö?
---
Ympäristö on kaikki systeemin ulkopuolella. Esimerkiksi rengas, vanne ja ulkoilma.
```

<svg data-fig="system" viewBox="0 0 600 340" role="img" aria-label="Periaatekuva, ei mittakaavassa. Kaasu on sylinterissä. Sylinterin yläpään sulkee mäntä, joka voi liikkua. Kaasu on termodynaaminen systeemi. Systeemin rajapinta on piirretty katkoviivalla kaasun ympärille. Sylinterin seinät, mäntä ja koko muu maailma ovat ympäristöä. Systeemin tilaa kuvaavat tilanmuuttujat: paine p, tilavuus V ja lämpötila T." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-3-system.webp" x="0" y="0" width="600" height="351.2" preserveAspectRatio="none"/>
  <foreignObject x="180" y="175.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T$</div></foreignObject>
  <foreignObject x="224" y="154.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$p$</div></foreignObject>
  <foreignObject x="72" y="205.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$V$</div></foreignObject>
  <foreignObject x="412" y="220.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{systeemi}$</div></foreignObject>
  <foreignObject x="412" y="175.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{rajapinta}$</div></foreignObject>
  <foreignObject x="412" y="105.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ympäristö}$</div></foreignObject>
</svg>

Miksi näin käy? Sen selittää aineen mikromalli. Kaasu koostuu hiukkasista. Hiukkaset liikkuvat jatkuvasti joka suuntaan. Ne törmäilevät toisiinsa ja astian seinämiin. Kaasun lämpötila kertoo hiukkasten keskimääräisestä liike-energiasta. Mitä kuumempaa kaasu on, sitä nopeammin hiukkaset liikkuvat keskimäärin. Paine syntyy, kun hiukkaset törmäävät seinämään. Jokainen törmäys työntää seinää hieman. Oletetaan, että tilavuus pienenee ja lämpötila pysyy samana. Silloin hiukkasilla on vähemmän tilaa, ja ne osuvat seinään useammin. Siksi paine kasvaa, mutta yksittäinen törmäys ei muutu kovemmaksi. Oletetaan sitten, että lämpötila nousee mutta tilavuus pysyy samana. Silloin hiukkaset osuvat seinään sekä useammin että kovempaa. Siksi paine kasvaa. Tästä syystä rengas tuntuu kesällä kovemmalta.

```pysahdy
Miksi kaasun paine kasvaa, kun tilavuutta pienennetään ja lämpötila pysyy samana?
---
Hiukkasilla on vähemmän tilaa. Ne osuvat seinään useammin. Yksittäinen törmäys ei muutu kovemmaksi.
```

<svg data-fig="micro-model" viewBox="0 0 600 300" role="img" aria-label="Kaaviokuva kaasun mikromallista. Kuvassa on kaksi suljettua astiaa. Astiat ovat yhtä suuret, ja niissä on yhtä monta hiukkasta. Nuolet kuvaavat hiukkasten nopeutta. Kylmässä kaasussa nuolet ovat lyhyitä. Kuumassa kaasussa nuolet ovat pitkiä. Kuuman kaasun paine p2 on suurempi kuin kylmän kaasun paine p1." class="fig-anim" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-3-micro-model.webp" x="4.9" y="8.6" width="591.1" height="306.7" preserveAspectRatio="none"/>
  <foreignObject x="88.5" y="25.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kylmä kaasu}$</div></foreignObject>
  <foreignObject x="378.5" y="25.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kuuma kaasu}$</div></foreignObject>
  <foreignObject x="138.5" y="257.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$p_1$</div></foreignObject>
  <foreignObject x="380" y="257.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$p_2 \gt p_1$</div></foreignObject>
</svg>

Kuva on kaaviokuva: nuolen pituus kuvaa hiukkasen nopeutta. Astiat ovat yhtä suuret, ja niissä on yhtä monta hiukkasta.

Lämpötilaa mitataan celsiusasteikolla ja kelvinasteikolla. Celsiusasteikolla $0\,{}^\circ\text{C}$ on veden jäätymispiste ja $100\,{}^\circ\text{C}$ on veden kiehumispiste normaalipaineessa. Kelvinasteikon nollapiste on absoluuttinen nollapiste. Se on alin mahdollinen lämpötila. Siinä hiukkasten keskimääräinen liike-energia on pienimmillään, eikä kylmempää voi olla. Celsiusaste ja kelvin ovat yhtä suuria. Siksi lämpötilaero on sama kelvineinä ja celsiusasteina. Oletetaan, että tilavuus ja kaasun määrä pysyvät samoina. Oletetaan myös, että kaasu on harvaa eli kaukana nesteytymisestä. Silloin kaasun paine on suoraan verrannollinen kelvinlämpötilaan. Myös harvan kaasun hiukkasten keskimääräinen liike-energia on suoraan verrannollinen kelvinlämpötilaan. Siksi lämpötilojen suhteita verrataan kelvineinä. Paineen, tilavuuden ja lämpötilan yhteyttä tutkitaan tarkemmin luvussa *Kaasujen tilanmuutokset ja Boylen laki*.

<figure class="unit-photo"><img src="pics/fy3/liquid-thermometer.webp" alt="Lasinen lämpömittari sinisellä taustalla."><figcaption>Lämpömittari näyttää oman lämpötilansa. Siksi mittarin ja kohteen lämpötilan on ensin tasaannuttava. Vasta sitten lukema kertoo kohteen lämpötilan.</figcaption></figure>

<figure class="unit-photo"><img src="pics/fy3/liquid-nitrogen.webp" alt="Käsi pitää lasimaljaa. Maljan ympärillä on valkoista sumua."><figcaption>Nestemäistä typpeä tiedetapahtumassa Puolassa. Typpi kiehuu hyvin kylmässä. Valkoinen sumu on pieniä vesipisaroita. Ne syntyvät kylmässä ilman vesihöyrystä.</figcaption></figure>

### Mallin rajat
Lause ”lämpötila kertoo hiukkasten keskimääräisestä liike-energiasta” on sellaisenaan totta vain harvalle kaasulle. Harvassa kaasussa hiukkaset vaikuttavat toisiinsa vain törmätessään. Silloin lämpötila on verrannollinen hiukkasten etenemisliikkeen keskimääräiseen liike-energiaan. Nesteessä ja kiinteässä aineessa hiukkaset ovat lähellä toisiaan. Ne värähtelevät, ja naapurit vetävät niitä. Lämpötila kuvaa niissäkin hiukkasten lämpöliikkeen voimakkuutta. Aineen energiaan kuuluu kuitenkin myös hiukkasten välisten vuorovaikutusten energia. Siksi lämpötila ei ole sama asia kuin aineen energia. Jäällä ja vedellä voi olla sama lämpötila $0\,{}^\circ\text{C}$, mutta samamassaisessa vedessä on enemmän sisäenergiaa kuin jäässä (luvut *Sisäenergia, lämpömäärä ja energian säilyminen* ja *Olomuodon muutokset*). Absoluuttisessa nollapisteessäkään kaikki hiukkasten liike ei lakkaa. Sen energia on kuitenkin pienin mahdollinen.

## Kaava: Kelvinasteikko
Celsiuslämpötila $\theta$ ja kelvinlämpötila $T$ liittyvät toisiinsa. Niiden lukuarvoille pätee yhtälö
```latex
\frac{T}{\text{K}} = \frac{\theta}{{}^\circ\text{C}} + 273{,}15
```
Esimerkiksi $20\,{}^\circ\text{C}$ on sama lämpötila kuin $293{,}15\,\text{K}$. Lämpötilaero on kelvineinä ja celsiusasteina sama luku. Kun lämpötila nousee $20\,{}^\circ\text{C}$:sta $30\,{}^\circ\text{C}$:seen, nousu on $10\,\text{K}$. Käytännössä riittää usein luku 273. Kelvineille ei käytetä sanaa aste. Sanotaan ”300 kelviniä”, ei ”300 kelvinastetta”.

Absoluuttinen nollapiste on siis $0\,\text{K}$ = $-273{,}15\,{}^\circ\text{C}$. Kelvinlämpötila ei voi olla negatiivinen. Celsiuslämpötila voi olla negatiivinen.

```pysahdy
Lämpötila on $250\,\text{K}$. Mikä se on celsiusasteina?
---
$\theta = 250 - 273{,}15 = -23{,}15$, eli $-23{,}15\,{}^\circ\text{C}$.
```

<svg data-fig="kelvin-scale" viewBox="0 0 600 250" role="img" aria-label="Kelvinasteikko ja celsiusasteikko rinnakkain mittakaavassa. 0 K on −273,15 °C (absoluuttinen nollapiste). 273,15 K on 0 °C (vesi jäätyy). 373,15 K on 100 °C (vesi kiehuu). Asteikkojen välit ovat yhtä suuret. Kelvinlukema saadaan, kun celsiuslukemaan lisätään 273,15." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-3-kelvin-scale.webp" x="0" y="12.5" width="600" height="260" preserveAspectRatio="none"/>
  <foreignObject x="62" y="61.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$0\,\text{K}$</div></foreignObject>
  <foreignObject x="346" y="61.5" width="104" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$273{,}15\,\text{K}$</div></foreignObject>
  <foreignObject x="466" y="61.5" width="104" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$373{,}15\,\text{K}$</div></foreignObject>
  <foreignObject x="62" y="203.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-273{,}15\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="358" y="203.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="473" y="203.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="62" y="15.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{absoluuttinen nollapiste}$</div></foreignObject>
  <foreignObject x="332" y="15.5" width="118" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{vesi jäätyy}$</div></foreignObject>
  <foreignObject x="472" y="15.5" width="118" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{vesi kiehuu}$</div></foreignObject>
  <foreignObject x="72" y="132.5" width="300" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T/\text{K} = \theta/{}^\circ\text{C} + 273{,}15$</div></foreignObject>
  <foreignObject x="553" y="97.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T$</div></foreignObject>
  <foreignObject x="553" y="167.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\theta$</div></foreignObject>
</svg>

Kuva on piirretty mittakaavassa. Yläasteikko on kelvinasteikko ja ala-asteikko celsiusasteikko. Väli $0\,{}^\circ\text{C}$:sta $100\,{}^\circ\text{C}$:een on yhtä pitkä kuin väli $273{,}15\,\text{K}$:sta $373{,}15\,\text{K}$:iin.

## Esimerkki
Suljetussa jäykässä astiassa on kaasua. Siksi sen tilavuus ja aineen määrä pysyvät samoina. Kaasun paine mitataan eri lämpötiloissa:

| $\theta$ (°C) | 0 | 20 | 40 | 60 | 80 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| $p$ (kPa) | 100 | 107 | 115 | 122 | 129 | 137 |

Määritä ekstrapoloimalla lämpötila, jossa kaasun paine olisi nolla.

<!-- vaihe -->

**Tunnetut ja kysytty.** Taulukossa on kuusi mittapistettä $(\theta,\, p)$. Paine on $p_0 = 100\,\text{kPa}$ lämpötilassa $0\,{}^\circ\text{C}$.

Kysytään lämpötilaa $\theta_0$, jossa paine olisi nolla.

Pisteet ovat kuvaajassa suoralla. Paine kasvaa jokaista $20\,{}^\circ\text{C}$ kohti $7$–$8\,\text{kPa}$. Suoraa jatketaan vasemmalle, mittausalueen ulkopuolelle. Tätä sanotaan ekstrapoloinniksi.

<svg data-fig="extrapolation" viewBox="0 0 600 350" role="img" aria-label="Kuvaaja näyttää, miten kaasun paine riippuu lämpötilasta suljetussa astiassa. Mittapisteet ovat lämpötila-alueella 0–100 °C, ja ne ovat suoralla. Suoraa on jatkettu eli ekstrapoloitu. Jatkettu suora kohtaa nollapaineen noin −270 °C:ssa. Pystyakseli on kuvan vasemmassa reunassa kohdassa −300 °C." style="max-width:100%;font-size:24px">
  <line x1="120.5" y1="290" x2="120.5" y2="84" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="186.5" y1="290" x2="186.5" y2="84" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="281" y1="290" x2="281" y2="84" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="375.5" y1="290" x2="375.5" y2="84" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="290" x2="470" y2="84" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="255.5" x2="470" y2="255.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="221.5" x2="470" y2="221.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="187" x2="470" y2="187" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="152.5" x2="470" y2="152.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="118.5" x2="470" y2="118.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="291" x2="92" y2="70" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,58 L98,71 L86,71 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="120.5" y1="290" x2="120.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="91.5" y="299.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-270$</div></foreignObject>
  <line x1="186.5" y1="290" x2="186.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="157.5" y="299.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-200$</div></foreignObject>
  <line x1="281" y1="290" x2="281" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="252" y="299.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-100$</div></foreignObject>
  <line x1="375.5" y1="290" x2="375.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="365.5" y="299.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="470" y1="290" x2="470" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="447.5" y="299.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="85" y1="255.5" x2="92" y2="255.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="241" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$25$</div></foreignObject>
  <line x1="85" y1="221.5" x2="92" y2="221.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="207" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="85" y1="187" x2="92" y2="187" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="172.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$75$</div></foreignObject>
  <line x1="85" y1="152.5" x2="92" y2="152.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="138" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="85" y1="118.5" x2="92" y2="118.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="35" y="104" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$125$</div></foreignObject>
  <foreignObject x="502" y="275.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\theta\ (^\circ\text{C})$</div></foreignObject>
  <foreignObject x="82" y="27.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p\ (\text{kPa})$</div></foreignObject>
  <foreignObject x="60" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <polyline points="120,290 375.5,152.5" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="9 7"/>
  <polyline points="375.5,152.5 470,102" fill="none" stroke="#1f2933" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="375.5" cy="152.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="394.5" cy="143" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="413.5" cy="132" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="432" cy="122.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="451" cy="113" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="470" cy="102" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="120" cy="290" r="7" fill="#ffffff" stroke="#1971c2" stroke-width="3"/>
  <foreignObject x="124" y="235.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$p = 0$</div></foreignObject>
  <foreignObject x="224.5" y="251" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{ekstrapolointi}$</span></div></foreignObject>
  <foreignObject x="413.5" y="152" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{mittaukset}$</span></div></foreignObject>
</svg>

Pystyakseli on piirretty kuvan vasempaan reunaan, noin $-300\,{}^\circ\text{C}$:n kohdalle, eikä kohtaan $\theta = 0$. Yhtenäinen suora on mittausalue ja katkoviiva on ekstrapolointi.

<!-- vaihe -->

**Periaate.** Astia on suljettu ja jäykkä. Siksi kaasun määrä ja tilavuus pysyvät samoina, ja paine riippuu vain lämpötilasta. Mittapisteet ovat suoralla, joten paine muuttuu lämpötilan mukana tasaisesti. Suoran yhtälö antaa arvion paineesta myös mittausalueen ulkopuolella. Arvio pätee, jos oletetaan, että riippuvuus pysyy samanlaisena. Nollapaine on kohdassa, jossa suora leikkaa lämpötila-akselin.

<!-- vaihe -->

**Kaava ratkaistuna.** Kulmakerroin $k$ lasketaan kahdesta kaukana toisistaan olevasta suoran pisteestä. Tässä mittapisteet ovat lukutarkkuuden rajoissa suoralla. Siksi mittausalueen päätepisteet ovat myös suoran pisteitä. Suoran yhtälössä $p_0$ on paine lämpötilassa $0\,{}^\circ\text{C}$. Asetetaan $p = 0$ ja ratkaistaan $\theta_0$:
```latex
\begin{aligned}
&k = \frac{\Delta p}{\Delta \theta} \\[4pt]
&p = p_0 + k\theta \\
&0 = p_0 + k\theta_0 \\
&\theta_0 = -\frac{p_0}{k}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Muunnoksia ei tarvita. Paineet ovat jo kilopascaleina. Lämpötilaero $\Delta\theta$ on sama celsiusasteina ja kelvineinä. Siksi kulmakertoimen yksikkö $\tfrac{\text{kPa}}{{}^\circ\text{C}}$ on myös $\tfrac{\text{kPa}}{\text{K}}$. Tulos saadaan suoraan celsiusasteina, koska taulukon lämpötilat ovat celsiusasteina.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin kulmakerroin ja sitten nollakohta:
```latex
\begin{aligned}
&k = \frac{\Delta p}{\Delta \theta} \\
&= \frac{(137 - 100)\,\text{kPa}}{(100 - 0)\,{}^\circ\text{C}} \\
&= 0{,}37\,\tfrac{\text{kPa}}{{}^\circ\text{C}} \\[6pt]
&\theta_0 = -\frac{p_0}{k} \\
&= -\frac{100\,\text{kPa}}{0{,}37\,\tfrac{\text{kPa}}{{}^\circ\text{C}}} \\
&= -270{,}27\,{}^\circ\text{C}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Nollapaineen lämpötila on noin $-270\,{}^\circ\text{C}$. Tulos ilmoitetaan kahdella merkitsevällä numerolla. Syy on se, että kulmakerroin $0{,}37\,\tfrac{\text{kPa}}{{}^\circ\text{C}}$ tunnetaan vain kahden numeron tarkkuudella.

<!-- vaihe -->

**Järkevyys.** Tulos on lähellä absoluuttista nollapistettä $-273{,}15\,{}^\circ\text{C}$. Ero on vain noin $3\,{}^\circ\text{C}$ eli yksi prosentti.

Tehdään vielä riippumaton tarkistus. Jos paine on verrannollinen kelvinlämpötilaan, $p = 100\,\text{kPa}$ vastaa lämpötilaa $273{,}15\,\text{K}$. Silloin paine lämpötilassa $100\,{}^\circ\text{C}$ olisi $100\,\text{kPa} \cdot \tfrac{373{,}15}{273{,}15} = 136{,}6\,\text{kPa}$. Mitattu arvo on $137\,\text{kPa}$.

Mikromallin mukaan nollapaineessa hiukkasten liike olisi niin vähäistä, ettei paine enää syntyisi. Todelliset kaasut nesteytyvät jo ennen tätä lämpötilaa. Siksi suoran jatke on vain malli, ja se kuvaa raja-arvoa.

## Yleinen virhekäsitys
Moni ajattelee, että lämpötila kaksinkertaistuu, kun se nousee $10\,{}^\circ\text{C}$:sta $20\,{}^\circ\text{C}$:een. Fysikaalisesti oikea vertailu tehdään kelvineinä: $283\,\text{K}$:sta $293\,\text{K}$:iin. Lämpötilojen suhde on 293/283 ≈ 1,035, eli nousu on noin $3{,}5\,\%$. Siksi hiukkasten keskimääräinen liike-energia ei kaksinkertaistu. Toinen virhe on pitää $0\,{}^\circ\text{C}$:ta alimpana mahdollisena lämpötilana. Se on vain veden jäätymispiste. Alin mahdollinen lämpötila on $0\,\text{K}$.

## Tiivistelmä
- Termodynaaminen systeemi on rajattu osa maailmaa. Sen tilaa kuvaavat tilanmuuttujat: lämpötila, paine, tilavuus ja aineen määrä.
- Kaasusysteemissä lämpötila, paine ja tilavuus riippuvat toisistaan. Jos yhtä muutetaan, vähintään yksi muista muuttuu myös.
- Kaasun mikromalli: lämpötila kertoo hiukkasten keskimääräisestä liike-energiasta. Paine syntyy hiukkasten törmäyksistä seinämään. Nesteessä ja kiinteässä aineessa energiaan kuuluu myös hiukkasten välisten vuorovaikutusten energia. Siksi lämpötila ei ole sama asia kuin aineen energia.
- Kun tilavuus ja aineen määrä pysyvät samoina, harvan kaasun paine on suoraan verrannollinen kelvinlämpötilaan. Mittapisteiden suoran jatkaminen eli ekstrapolointi antaa arvion absoluuttisesta nollapisteestä.
- Muunnos on $\tfrac{T}{\text{K}} = \tfrac{\theta}{{}^\circ\text{C}} + 273{,}15$. Absoluuttinen nollapiste on $0\,\text{K}$ = $-273{,}15\,{}^\circ\text{C}$.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: sama polkupyörä on ulkona lumisena pakkasaamuna. Maassa ja satulalla on lunta. Tolpan lämpömittarin pylväs on matalalla." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-3-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
