# Termodynaaminen systeemi, tilanmuuttujat ja lämpötila

> **Miksi** pyörän rengas tuntuu kovemmalta kuumana kesäpäivänä kuin pakkasella, vaikka renkaaseen ei pumpata lisää ilmaa?

## Ydinajatus
Kun tutkitaan ilmiötä, tarkasteltava osa maailmasta rajataan erilleen muusta. Rajattu osa on termodynaaminen systeemi ja kaikki sen ulkopuolella oleva on ympäristö. Pyörän renkaan ilma on esimerkki systeemistä. Jos systeemistä ei pääse ainetta ulos eikä sisään, systeemi on suljettu. Systeemin tilaa kuvataan tilanmuuttujilla, joita ovat lämpötila, paine ja tilavuus sekä aineen määrä. Paine on voima pinta-alaa kohti; sen yksikkö on pascal (Pa), ja 1 kPa = 1000 Pa. Paineeseen paneudutaan tarkemmin myöhemmin. Kun kaasusysteemissä muutetaan yhtä tilanmuuttujaa, vähintään yksi muista muuttuu myös.

<svg data-fig="system" viewBox="0 0 600 340" role="img" aria-label="Periaatekuva, ei mittakaavassa: kaasua sylinterissä, jonka yläpäätä sulkee liikkuva mäntä. Kaasu on termodynaaminen systeemi; sen rajapinta on piirretty katkoviivalla kaasun ympärille. Sylinterin seinät, mäntä ja koko muu maailma ovat ympäristöä. Systeemin tilaa kuvaavat tilanmuuttujat: paine p, tilavuus V ja lämpötila T." style="max-width:100%;font-size:24px">
  <rect x="138" y="150" width="204" height="140" fill="#eef5f9"/>
  <path d="M126,110 V302 H354 V110 H342 V290 H138 V110 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="138" y="128" width="204" height="22" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="234" y="74" width="12" height="54" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="206" y="60" width="68" height="14" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="226" cy="212" r="5.5" fill="#2f74b5" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="282" cy="184" r="5.5" fill="#2f74b5" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="322" cy="200" r="5.5" fill="#2f74b5" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="256" cy="232" r="5.5" fill="#2f74b5" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="306" cy="238" r="5.5" fill="#2f74b5" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="212" cy="262" r="5.5" fill="#2f74b5" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="270" cy="268" r="5.5" fill="#2f74b5" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="322" cy="270" r="5.5" fill="#2f74b5" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="300" cy="208" r="5.5" fill="#2f74b5" stroke="#ffffff" stroke-width="1.5"/>
  <rect x="143" y="155" width="194" height="130" rx="4" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-dasharray="10 6"/>
  <rect x="158" y="168" width="8" height="90" rx="4" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="160" y="206" width="4" height="54" fill="#c92a2a"/>
  <circle cx="162" cy="268" r="9" fill="#c92a2a" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="180" y="175.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T$</div></foreignObject>
  <line x1="262" y1="176" x2="262" y2="168" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M262,158 L267,169 L257,169 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="302" y1="176" x2="302" y2="168" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M302,158 L307,169 L297,169 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="224" y="154.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$p$</div></foreignObject>
  <line x1="104" y1="150" x2="142" y2="150" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="104" y1="290" x2="142" y2="290" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="110" y1="220" x2="110" y2="161" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M110,151 L115,162 L105,162 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="110" y1="220" x2="110" y2="279" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M110,289 L105,278 L115,278 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="72" y="205.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$V$</div></foreignObject>
  <line x1="402" y1="235" x2="318" y2="235" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="318" cy="235" r="3" fill="#6b7480"/>
  <foreignObject x="412" y="220.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{systeemi}$</div></foreignObject>
  <line x1="402" y1="190" x2="338" y2="190" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="338" cy="190" r="3" fill="#6b7480"/>
  <foreignObject x="412" y="175.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{rajapinta}$</div></foreignObject>
  <line x1="402" y1="120" x2="350" y2="120" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <circle cx="350" cy="120" r="3" fill="#6b7480"/>
  <foreignObject x="412" y="105.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ympäristö}$</div></foreignObject>
</svg>

Miksi näin käy, selittää aineen mikromalli. Kaasu koostuu hiukkasista, jotka liikkuvat jatkuvasti joka suuntaan ja törmäilevät toisiinsa ja astian seinämiin. Lämpötila kertoo hiukkasten keskimääräisestä liike-energiasta: mitä kuumempaa kaasu on, sitä nopeammin hiukkaset keskimäärin liikkuvat. Paine syntyy, kun hiukkaset törmäävät seinämään ja jokainen törmäys työntää seinää hieman. Kun tilavuus pienenee ja lämpötila pysyy samana, hiukkasilla on vähemmän tilaa ja ne osuvat seinään useammin, joten paine kasvaa, mutta yksittäinen törmäys ei muutu kovemmaksi. Kun lämpötila nousee mutta tilavuus pysyy samana, hiukkaset osuvat seinään sekä useammin että kovempaa, joten paine kasvaa. Tästä syystä rengas tuntuu kesällä kovemmalta.

<svg data-fig="micro-model" viewBox="0 0 600 300" role="img" aria-label="Kaaviokuva kaasun mikromallista: kaksi samankokoista suljettua astiaa, joissa on yhtä monta hiukkasta. Kylmässä kaasussa nopeutta kuvaavat nuolet ovat lyhyitä, kuumassa pitkiä, ja kuuman kaasun paine p2 on suurempi kuin kylmän kaasun paine p1." style="max-width:100%;font-size:24px">
  <foreignObject x="88.5" y="25.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kylmä kaasu}$</div></foreignObject>
  <rect x="40" y="62" width="230" height="180" rx="6" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="378.5" y="25.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kuuma kaasu}$</div></foreignObject>
  <rect x="330" y="62" width="230" height="180" rx="6" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <line x1="95" y1="105" x2="104.5" y2="114.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M111,121 L100.5,117 L107,110.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="95" cy="105" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="210" y1="100" x2="199" y2="106.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M191,111 L197.5,102 L202,110 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="210" cy="100" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="155" y1="155" x2="168" y2="155" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M177,155 L167,159.5 L167,150.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="155" cy="155" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="85" y1="190" x2="94.5" y2="180.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M101,174 L97,184.5 L90.5,178 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="85" cy="190" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="215" y1="200" x2="202.5" y2="195" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M194,192 L205,191.5 L201.5,200 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="215" cy="200" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="140" y1="215" x2="153" y2="217.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M162,219 L151.5,221.5 L153,213 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="140" cy="215" r="7" fill="#1971c2" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="385" y1="105" x2="409.5" y2="129.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M416,136 L405.5,132 L412,125.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="385" cy="105" r="7" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="500" y1="100" x2="470" y2="117.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M462,122 L468.5,113 L473,121 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="500" cy="100" r="7" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="445" y1="155" x2="480" y2="155" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M489,155 L479,159.5 L479,150.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="445" cy="155" r="7" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="375" y1="190" x2="399.5" y2="165.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M406,159 L402,169.5 L395.5,163 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="375" cy="190" r="7" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="505" y1="200" x2="472.5" y2="188" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M464,185 L475,184 L472,192.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="505" cy="200" r="7" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="430" y1="215" x2="464" y2="221.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M473,223 L462.5,225.5 L464,216.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="430" cy="215" r="7" fill="#c92a2a" stroke="#ffffff" stroke-width="1.5"/>
  <foreignObject x="138.5" y="257.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$p_1$</div></foreignObject>
  <foreignObject x="380" y="257.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$p_2 \gt p_1$</div></foreignObject>
</svg>

Kuva on kaaviokuva: nuolen pituus kuvaa hiukkasen nopeutta. Astiat ovat yhtä suuret, ja niissä on yhtä monta hiukkasta.

Lämpötilaa mitataan celsiusasteikolla, jossa 0 °C on veden jäätymispiste ja 100 °C veden kiehumispiste normaalipaineessa, ja kelvinasteikolla. Kelvinasteikon nollapiste on absoluuttinen nollapiste, alin mahdollinen lämpötila. Siinä hiukkasten keskimääräinen liike-energia on pienimmillään, eikä kylmempää voi olla. Celsiusasteen ja kelvinin suuruus on sama, joten lämpötilaero on sama kelvineinä ja celsiusasteina. Kun tilavuus ja kaasun määrä pysyvät samoina, kaasun paine on suoraan verrannollinen kelvinlämpötilaan. Myös hiukkasten keskimääräinen liike-energia on suoraan verrannollinen kelvinlämpötilaan, joten lämpötilojen suhteita verrataan kelvineinä. Paineen, tilavuuden ja lämpötilan yhteyttä tutkitaan tarkemmin luvussa *Kaasujen tilanmuutokset ja Boylen laki*.

## Kaava: Kelvinasteikko
Celsiuslämpötilan $\theta$ muunnos kelvineiksi on:
```latex
T = \theta + 273{,}15
```
missä $T$ on lämpötila kelvineinä (K) ja $\theta$ lämpötila celsiusasteina (°C). Käytännössä riittää usein luku 273. Kelvineissä ei käytetä sanaa aste: sanotaan ”300 kelviniä”, ei ”300 kelvinastetta”.

Absoluuttinen nollapiste on siis 0 K = −273,15 °C. Kelvinlämpötila ei voi olla negatiivinen, mutta celsiuslämpötila voi.

<svg data-fig="kelvin-scale" viewBox="0 0 600 250" role="img" aria-label="Kelvinasteikko ja celsiusasteikko rinnakkain mittakaavassa: 0 K on −273,15 °C (absoluuttinen nollapiste), 273,15 K on 0 °C (vesi jäätyy) ja 373,15 K on 100 °C (vesi kiehuu). Asteikkojen välit ovat yhtä suuret, ja kelvinlukema saadaan lisäämällä celsiuslukemaan 273,15." style="max-width:100%;font-size:24px">
  <line x1="58" y1="112" x2="533" y2="112" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M545,112 L532,118 L532,106 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="58" y1="182" x2="533" y2="182" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M545,182 L532,188 L532,176 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="70" y1="112" x2="70" y2="182" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <line x1="70" y1="104" x2="70" y2="120" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="70" y1="174" x2="70" y2="190" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="398" y1="112" x2="398" y2="182" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <line x1="398" y1="104" x2="398" y2="120" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="398" y1="174" x2="398" y2="190" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="518" y1="112" x2="518" y2="182" stroke="#c92a2a" stroke-width="3" stroke-linecap="butt"/>
  <line x1="518" y1="104" x2="518" y2="120" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="518" y1="174" x2="518" y2="190" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="62" y="61.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$0\,\text{K}$</div></foreignObject>
  <foreignObject x="346" y="61.5" width="104" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$273{,}15\,\text{K}$</div></foreignObject>
  <foreignObject x="466" y="61.5" width="104" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$373{,}15\,\text{K}$</div></foreignObject>
  <foreignObject x="62" y="203.5" width="130" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-273{,}15\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="358" y="203.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="473" y="203.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100\,{}^\circ\text{C}$</div></foreignObject>
  <foreignObject x="62" y="15.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{absoluuttinen nollapiste}$</div></foreignObject>
  <foreignObject x="332" y="15.5" width="118" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{vesi jäätyy}$</div></foreignObject>
  <foreignObject x="472" y="15.5" width="118" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{vesi kiehuu}$</div></foreignObject>
  <foreignObject x="107" y="132.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$T = \theta + 273{,}15$</span></div></foreignObject>
  <foreignObject x="553" y="97.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T$</div></foreignObject>
  <foreignObject x="553" y="167.5" width="30" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\theta$</div></foreignObject>
</svg>

Kuva on piirretty mittakaavassa. Yläasteikko on kelvinasteikko ja alaasteikko celsiusasteikko; väli 0 °C:sta 100 °C:een on yhtä pitkä kuin väli 273,15 K:sta 373,15 K:iin.

## Esimerkki
Suljetussa jäykässä astiassa on kaasua, joten sen tilavuus ja aineen määrä pysyvät samoina. Kaasun paine mitataan eri lämpötiloissa:

| $\theta$ (°C) | 0 | 20 | 40 | 60 | 80 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| $p$ (kPa) | 100 | 107 | 115 | 122 | 129 | 137 |

Määritä ekstrapoloimalla lämpötila, jossa kaasun paine olisi nolla.

<!-- vaihe -->

**Kuvaaja.** Pisteet asettuvat suoralle. Jatketaan suoraa vasemmalle mittausalueen ulkopuolelle eli ekstrapoloidaan: sovitettua suoraa jatketaan mitattujen pisteiden yli, vaikka siellä ei ole mittauksia.

<svg data-fig="extrapolation" viewBox="0 0 600 350" role="img" aria-label="Kaasun paine lämpötilan funktiona suljetussa astiassa: mittapisteet lämpötila-alueella 0–100 °C asettuvat suoralle, ja ekstrapoloitu suora kohtaa nollapaineen lämpötilassa noin −270 °C. Pystyakseli on kuvan vasemmassa reunassa kohdassa −300 °C." style="max-width:100%;font-size:24px">
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

Pystyakseli on piirretty kuvan vasempaan reunaan, noin −300 °C:n kohdalle, eikä kohtaan $\theta = 0$. Yhtenäinen suora on mittausalue ja katkoviiva ekstrapolointi.

<!-- vaihe -->

**Kulmakerroin.** Suoran kulmakerroin lasketaan mittausalueen päätepisteistä:
```latex
\begin{aligned}
&k = \frac{\Delta p}{\Delta \theta} \\
&= \frac{(137 - 100)\,\text{kPa}}{(100 - 0)\,\text{°C}} \\
&= 0{,}37\,\text{kPa/°C}
\end{aligned}
```

<!-- vaihe -->

**Kaava ratkaistuna.** Suoran yhtälö on ylärivillä, missä $p_0$ on paine lämpötilassa 0 °C. Nollapaine saavutetaan, kun $p = 0$, ja siitä ratkaistaan lämpötila:
```latex
\begin{aligned}
&p = p_0 + k\theta \\
&0 = p_0 + k\theta \\
&\theta = -\frac{p_0}{k}
\end{aligned}
```

<!-- vaihe -->

**Sijoitus.** Tässä $p_0 = 100\,\text{kPa}$, joten
```latex
\begin{aligned}
&\theta = -\frac{p_0}{k} \\
&= -\frac{100\,\text{kPa}}{0{,}37\,\text{kPa/°C}} \\
&\approx -270\,\text{°C}
\end{aligned}
```

<!-- vaihe -->

**Järkevyys.** Tulos on lähellä absoluuttista nollapistettä −273 °C. Mikromallin mukaan tässä lämpötilassa hiukkasten liike olisi niin vähäistä, ettei paine enää syntyisi. Näin absoluuttinen nollapiste voidaan määrittää kokeellisesti. Todelliset kaasut nesteytyvät jo ennen tätä lämpötilaa, joten suoran jatke on vain malli ja kuvaa raja-arvoa.

## Yleinen virhekäsitys
Moni ajattelee, että lämpötila kaksinkertaistuu, kun se nousee 10 °C:sta 20 °C:een. Fysikaalisesti oikea vertailu tehdään kelvineinä: 283 K:sta 293 K:iin. Lämpötilojen suhde on 293/283 ≈ 1,035, eli nousu on noin 3,5 %. Siksi hiukkasten keskimääräinen liike-energia ei kaksinkertaistu. Toinen virhe on pitää 0 °C:ta alimpana mahdollisena lämpötilana. Se on vain veden jäätymispiste, ja alin mahdollinen lämpötila on 0 K.

## Tiivistelmä
- Termodynaaminen systeemi on rajattu osa maailmaa. Sen tilaa kuvaavat tilanmuuttujat: lämpötila, paine, tilavuus ja aineen määrä.
- Kaasusysteemissä lämpötila, paine ja tilavuus riippuvat toisistaan: jos yhtä muutetaan, vähintään yksi muista muuttuu myös.
- Mikromalli: lämpötila kertoo hiukkasten keskimääräisestä liike-energiasta, ja paine syntyy hiukkasten törmäyksistä seinämään.
- Kun tilavuus ja aineen määrä pysyvät samoina, paine on suoraan verrannollinen kelvinlämpötilaan. Mittapisteiden suoran jatkaminen eli ekstrapolointi antaa absoluuttisen nollapisteen.
- Muunnos on $T = \theta + 273{,}15$. Absoluuttinen nollapiste on 0 K = −273,15 °C.
