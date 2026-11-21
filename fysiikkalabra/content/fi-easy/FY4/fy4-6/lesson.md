# Paino, kitka ja kalteva taso

> **Miksi** muuttolaatikko pysyy paikallaan vinolla lastaussillalla, mutta lähtee liukumaan, kun siltaa jyrkennetään vähän lisää?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: muuttopäivä kerrostalon pihalla. Pakettiauton takaovet ovat auki. Auton lattialta laskeutuu puinen lastaussilta vinosti maahan. Sillan keskellä on pahvinen muuttolaatikko, joka pysyy paikallaan. Auton sisällä on lisää laatikoita. Muuttaja kantaa yhtä laatikkoa sillan vieressä." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-6-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Paino
Kappaleen **paino** $\overline{G}$ on voima, jolla Maa vetää kappaletta. Paino osoittaa aina suoraan alas, myös rinteellä. Voimakuviossa paino piirretään kappaleen keskipisteestä. Painon suuruus on massan ja putoamiskiihtyvyyden tulo $mg$.

Massa kertoo, kuinka vaikea kappaleen liiketilaa on muuttaa. Massa on sama kaikkialla. Paino taas riippuu paikasta. Kuun pinnalla $g = 1{,}62\,\text{m/s}^2$. Siksi $60\,\text{kg}$:n ihmisen paino on Kuussa noin $97\,\text{N}$, mutta Maassa noin $590\,\text{N}$.

```pysahdy
Astronautin massa on $80\,\text{kg}$. Hän menee Kuuhun. Muuttuuko hänen massansa, painonsa vai molemmat?
---
Massa ei muutu. Paino pienenee, koska Kuu vetää vähemmän kuin Maa.
```

### Lepokitka ja liukukitka
Kun kaksi pintaa koskettaa toisiaan, ne vastustavat liukumista toistensa suhteen. Tämä pinnan suuntainen voima on **kitka** $\overline{F}_\mu$. Pinnat eivät ole täysin sileitä. Pienet epätasaisuudet tarttuvat toisiinsa, ja pintojen hiukkasten välillä on vetovoimia. Mitä lujemmin pinnat painuvat toisiaan vasten, sitä suurempi kitka voi olla. Pintojen painamista toisiaan vasten kuvaa tukivoima $N$.

Kun laatikkoa vedetään lattialla heikosti, se ei liiku. Silloin laatikkoon vaikuttaa **lepokitka**. Lepokitka on yhtä suuri kuin veto ja vastakkaissuuntainen, joten kokonaisvoima on nolla. Lepokitka ei siis ole vakio, vaan se mukautuu tilanteeseen. Sillä on kuitenkin yläraja.

Kun veto ylittää ylärajan, laatikko lähtee liukumaan. Silloin kitka vaihtuu **liukukitkaksi**. Liukukitka on yleensä pienempi kuin lepokitkan suurin arvo. Lepokitkan suurinta arvoa sanotaan täysin kehittyneeksi lepokitkaksi eli lähtökitkaksi. Tavallisilla nopeuksilla liukukitka on likimain vakio.

<svg data-fig="kitka" viewBox="0 0 600 360" role="img" aria-label="Kuvaaja mittakaavassa. Vaaka-akselilla on laatikkoa vetävä vaakasuora voima F newtoneina nollasta 80:een. Pystyakselilla on lattian kitkavoima newtoneina nollasta 60:een. Tukivoima, joka painaa laatikkoa lattiaa vasten, on 100 newtonia. Aluksi kitkavoima kasvaa yhtä suureksi kuin veto. Suora nousee origosta pisteeseen, jossa veto ja kitka ovat 50 newtonia. Se on lepokitkan suurin arvo eli lähtökitka, myy nolla kertaa N. Siinä laatikko lähtee liikkeelle. Kitkavoima putoaa katkoviivaa pitkin 35 newtoniin, myy kertaa N, ja pysyy siinä vedon kasvaessa." style="max-width:100%;font-size:24px">
  <line x1="193" y1="300" x2="193" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="294" y1="300" x2="294" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="395" y1="300" x2="395" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="496" y1="300" x2="496" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="261.5" x2="496" y2="261.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="223.5" x2="496" y2="223.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="185" x2="496" y2="185" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="146.5" x2="496" y2="146.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="108.5" x2="496" y2="108.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="70" x2="496" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="300" x2="510" y2="300" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M522,300 L509,306 L509,294 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="301" x2="92" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,44 L98,57 L86,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="193" y1="300" x2="193" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="176.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="294" y1="300" x2="294" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="277.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="395" y1="300" x2="395" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="378.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="496" y1="300" x2="496" y2="307" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="479.5" y="309.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$80$</div></foreignObject>
  <line x1="85" y1="261.5" x2="92" y2="261.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="247" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$10$</div></foreignObject>
  <line x1="85" y1="223.5" x2="92" y2="223.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="209" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$20$</div></foreignObject>
  <line x1="85" y1="185" x2="92" y2="185" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="170.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="85" y1="146.5" x2="92" y2="146.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="132" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$40$</div></foreignObject>
  <line x1="85" y1="108.5" x2="92" y2="108.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="94" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="85" y1="70" x2="92" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="55.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <foreignObject x="62" y="305.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="528" y="285.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F\ (\text{N})$</div></foreignObject>
  <foreignObject x="82" y="13.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$F_\mu\ (\text{N})$</div></foreignObject>
  <polyline points="92,300 344.5,108.5" fill="none" stroke="#c92a2a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="344.5" y1="108.5" x2="344.5" y2="166" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <polyline points="344.5,166 496,166" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="344.5" cy="108.5" r="6.5" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="107" y="170.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\text{lepokitka}$</div></foreignObject>
  <foreignObject x="370" y="124.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\text{liukukitka}$</div></foreignObject>
  <foreignObject x="279.5" y="71" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\mu_0 N$</div></foreignObject>
  <foreignObject x="419" y="174.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\mu N$</div></foreignObject>
</svg>

Kuvaajassa lattian tukivoima on $100\,\text{N}$. Lepokitka kasvaa vedon mukana $50\,\text{N}$:iin asti. Siinä laatikko lähtee liikkeelle. Liukuvaan laatikkoon vaikuttaa $35\,\text{N}$:n liukukitka, vaikka vetoa lisättäisiin. Siksi raskas kaappi on vaikeinta saada liikkeelle. Kun kaappi liikkuu, sitä on helpompi työntää.

```pysahdy
Vedät laatikkoa vähän, mutta se ei liiku. Kuinka suuri lepokitka on?
---
Se on yhtä suuri kuin voima, jolla vedät, mutta osoittaa vastakkaiseen suuntaan. Siksi voimat kumoavat toisensa ja laatikko pysyy paikallaan.
```

### Kalteva taso
Kalteva taso on vino pinta eli rinne. Rinteellä paino osoittaa yhä suoraan alas, mutta pinta on vinossa. Tukivoima on kohtisuorassa pintaa vastaan, ja kitka on pinnan suuntainen.

Laskua varten paino jaetaan kahteen **komponenttiin**. Komponentti on voiman osa tietyssä suunnassa. Rinteen suuntainen komponentti pyrkii viemään kappaletta rinnettä alas. Pintaa vastaan kohtisuora komponentti painaa kappaletta pintaa vasten. Komponentit eivät ole uusia voimia. Ne korvaavat painon laskussa. Voimakuviossa ne piirretään katkoviivoin.

<svg data-fig="kalteva-ydin" viewBox="0 0 600 380" role="img" aria-label="Kaksi kuvaa. Vasemmalla on tilannekuva. Laatikko on paikallaan puisella lankulla. Lankku nousee oikealle kulmassa alfa vaakatasoon nähden. Oikealla on laatikon voimakuvio. Laatikko on piirretty kallistettuna suorakulmiona, kuten lankulla. Paino G lähtee keskipisteestä suoraan alas. Tukivoima N lähtee alapinnasta kohtisuoraan pintaa vastaan ulospäin. Lepokitka lähtee alapinnan ylemmästä kulmasta pinnan suuntaisesti ylös rinnettä. Painon komponentit on piirretty katkoviivoin keskipisteestä: G x rinnettä alas ja G y kohtisuoraan pintaa kohti. Painon ja komponentin G y välinen kulma on alfa. Komponentti G y on yhtä pitkä kuin tukivoima. Komponentti G x on yhtä pitkä kuin kitkavoima." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-6-kalteva-ydin.webp" x="1.2" y="0" width="597" height="388.1" preserveAspectRatio="none"/>
  <foreignObject x="57.5" y="7.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <foreignObject x="81.5" y="260" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="373.5" y="7.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio}$</div></foreignObject>
  <foreignObject x="399.5" y="303.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="374" y="78" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="547" y="99.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <foreignObject x="321.5" y="213" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{x}$</div></foreignObject>
  <foreignObject x="497.5" y="234" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{y}$</div></foreignObject>
  <foreignObject x="440" y="208" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
</svg>

Mitä jyrkempi rinne on, sitä suurempi on rinteen suuntainen komponentti. Samalla kohtisuora komponentti pienenee.

Oletetaan, että pintaa vastaan kohtisuorassa vaikuttavat vain paino ja tukivoima. Oletetaan myös, että kappale ei kiihdy siinä suunnassa. Silloin tukivoima pienenee kohtisuoran komponentin mukana. Samalla pienenee lepokitkan yläraja.

Siksi laatikko lähtee jyrkässä rinteessä liukumaan. Rinnettä alas vievä komponentti kasvaa suuremmaksi kuin lähtökitka, jonka pinta pystyy aiheuttamaan.

```pysahdy
Miksi laatikko lähtee liukumaan, kun rinne on tarpeeksi jyrkkä?
---
Kun rinne jyrkkenee, rinnettä alas vievä osa painosta kasvaa ja tukivoima ja lähtökitka pienenevät. Kun alas vievä osa ylittää lähtökitkan, laatikko lähtee liikkeelle.
```

### Kitka ei aina vastusta liikettä
Kitka vastustaa pintojen liukumista **toistensa suhteen**. Se ei välttämättä vastusta kappaleen liikettä.

Esimerkiksi avolava-auto lähtee kiihtyen liikkeelle. Lavalla oleva laatikko kiihtyy mukana. Ilmanvastus jätetään huomiotta. Silloin ainoa vaakasuora voima laatikkoon on lavan kitka. Kitkan täytyy siis osoittaa eteenpäin, liikkeen suuntaan. Lava pyrkii liukumaan eteenpäin laatikon alta, ja lepokitka estää sen.

Samoin kävellessä jalka työntää maata taaksepäin, ja maan lepokitka työntää jalkaa eteenpäin. Peilijäällä kitkaa on hyvin vähän. Siksi liikkeelle lähteminen on siellä vaikeaa.

<svg data-fig="kuorma" viewBox="0 0 600 360" role="img" aria-label="Kaksi kuvaa. Vasemmalla on tilannekuva. Avolava-auto lähtee liikkeelle oikealle ja kiihtyy. Auton lavalla on laatikko, joka ei liu&#x27;u lavalla. Laatikon yllä ohut oranssi nuoli a osoittaa oikealle. Oikealla on laatikon voimakuvio suorakulmiona. Paino G lähtee keskipisteestä alas. Lavan tukivoima N lähtee alapinnasta ylös, ja se on yhtä pitkä kuin paino. Lavan kitkavoima lähtee alapinnan etukulmasta oikealle eli liikkeen suuntaan. Kitkavoima on paljon lyhyempi kuin paino." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-6-kuorma.webp" x="0" y="0" width="600" height="371.2" preserveAspectRatio="none"/>
  <foreignObject x="77.5" y="7.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <foreignObject x="159.5" y="93.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <foreignObject x="383.5" y="7.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio}$</div></foreignObject>
  <foreignObject x="415.5" y="309" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="349.5" y="68" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="465.5" y="225.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <foreignObject x="554.5" y="137.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
</svg>

Kitkan lisäksi kappaleeseen voi vaikuttaa muitakin kosketusvoimia. **Noste** on voima, jolla neste tai kaasu työntää siihen uponnutta kappaletta ylöspäin. **Väliaineen vastusvoima** on voima, jolla ilma tai vesi vastustaa kappaleen liikettä. Ilmanvastusta käsitellään tarkemmin luvussa *Ilmanvastus ja putoaminen ilmassa*. Tässä luvussa ilmanvastus ja noste jätetään huomiotta.

```pysahdy
Kävelet eteenpäin. Mihin suuntaan maan kitka vaikuttaa jalkaasi?
---
Eteenpäin, samaan suuntaan kuin kävelet. Jalkasi työntää maata taaksepäin, ja maan kitka työntää jalkaa eteenpäin.
```

## Kaava: Kitkavoima ja kalteva taso
Painon suuruus on
```kaavat
kappaleeseen vaikuttava painovoima Maan pinnalla :: G = mg
```
missä $G$ on paino (N), $m$ massa (kg) ja $g$ putoamiskiihtyvyys, Maan pinnalla $9{,}81\,\text{m/s}^2$.

Liukukitka on verrannollinen tukivoimaan:
```kaavat
liukukitka :: F_\mu = \mu N
```
missä $F_\mu$ on liukukitkan suuruus (N), $\mu$ **liukukitkakerroin** (ei yksikköä) ja $N$ tukivoiman suuruus (N). Lepokitka on enintään tukivoiman ja **lepokitkakertoimen** $\mu_0$ tulo:
```latex
F_{\mu 0} \le \mu_0 N
```
missä $F_{\mu 0}$ on lepokitkan suuruus (N). Lepokitka on suurimmillaan juuri ennen kuin kappale lähtee liukumaan. Tätä lepokitkan suurinta arvoa sanotaan **täysin kehittyneeksi lepokitkaksi eli lähtökitkaksi**:
```kaavat
lähtökitka, eli täysin kehittynyt lepokitka :: F_{\mu 0} = \mu_0 N
```

Kitkakertoimet riippuvat pintojen aineista ja kunnosta. Yleensä $\mu < \mu_0$. Kaavat ovat kokeellisia malleja, jotka kuvaavat kuivia pintoja hyvin. Niissä kitka ei riipu kosketuspinnan alasta eikä liukumisnopeudesta.

Kaltevalla tasolla kaltevuuskulma on $\alpha$. Valitaan $x$-akseli rinteen suuntaiseksi ja $y$-akseli kohtisuoraan pintaa vastaan. Painon komponentit ovat
```latex
\begin{aligned}
G_x &= G\sin\alpha \\
G_y &= G\cos\alpha
\end{aligned}
```
missä $G_x$ on rinteen suuntainen komponentti (N) ja $G_y$ pintaa vastaan kohtisuora komponentti (N).

Painon ja komponentin $G_y$ välinen kulma on sama $\alpha$ kuin rinteen kaltevuuskulma. Syy on tämä: paino on kohtisuorassa vaakatasoa vastaan ja $G_y$ on kohtisuorassa rinnettä vastaan.

<svg data-fig="kalteva" viewBox="0 0 600 380" role="img" aria-label="Kaksi kuvaa. Vasemmalla on tilannekuva. Laatikko on paikallaan puisella lankulla. Lankku nousee oikealle kulmassa alfa vaakatasoon nähden. Oikealla on laatikon voimakuvio. Laatikko on piirretty kallistettuna suorakulmiona, kuten lankulla. Paino G lähtee keskipisteestä suoraan alas. Tukivoima N lähtee alapinnasta kohtisuoraan pintaa vastaan ulospäin. Lepokitka lähtee alapinnan ylemmästä kulmasta pinnan suuntaisesti ylös rinnettä. Painon komponentit on piirretty katkoviivoin keskipisteestä: G x rinnettä alas ja G y kohtisuoraan pintaa kohti. Painon ja komponentin G y välinen kulma on alfa. Komponentti G y on yhtä pitkä kuin tukivoima. Komponentti G x on yhtä pitkä kuin kitkavoima." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-6-kalteva.webp" x="0" y="0" width="600" height="386.2" preserveAspectRatio="none"/>
  <foreignObject x="57.5" y="7.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{tilannekuva}$</div></foreignObject>
  <foreignObject x="83.5" y="266.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
  <foreignObject x="373.5" y="7.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{voimakuvio}$</div></foreignObject>
  <foreignObject x="399.5" y="303.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="379" y="62.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="539.5" y="130.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <foreignObject x="329" y="192" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{x}$</div></foreignObject>
  <foreignObject x="490" y="255" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{y}$</div></foreignObject>
  <foreignObject x="435" y="209.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha$</div></foreignObject>
</svg>

Oletetaan, että pintaa vastaan kohtisuorassa vaikuttavat vain paino ja tukivoima. Oletetaan myös, että kappale ei kiihdy siinä suunnassa. Silloin tukivoima on yhtä suuri kuin $G_y$: $N = mg\cos\alpha$. Tukivoima on painoa pienempi. (Pintaa vasten tai siitä poispäin suuntautuva vetävä tai työntävä voima muuttaisi tukivoimaa.)

Levossa olevaan kappaleeseen vaikuttava lepokitka on yhtä suuri kuin $G_x$. Kappale pysyy paikallaan niin kauan kuin $mg\sin\alpha \le \mu_0\,mg\cos\alpha$ eli $\tan\alpha \le \mu_0$. Massa supistuu. Tämän mallin mukaan raskas ja kevyt laatikko lähtevät samalta pinnalta liukumaan samalla kulmalla.

<figure class="unit-photo"><img src="pics/fy4/snow-sledding.webp" alt="Lapsi laskee keltaisella liukurilla lumista mäkeä alas."><figcaption>Lapsi laskee mäkeä alas muovisella liukurilla.</figcaption></figure>

### Kitkakertoimen määrittäminen
Kuvioissa ja simulaatiossa levossa olevaan kappaleeseen vaikuttavaa lepokitkaa merkitään $\overline{F}_\mu$. Sen suuruus on $F_{\mu 0} \le \mu_0 N$. Liukuessa $F_\mu = \mu N$.

Lepokitkakerroin saadaan kokeesta, jossa lautaa kallistetaan hitaasti, kunnes kappale lähtee liukumaan. Tällä rajakulmalla $\alpha_0$ lepokitka on suurimmillaan, joten $\mu_0 = \tan\alpha_0$.

Liukukitkakerroin saadaan esimerkiksi vetämällä kappaletta vaakasuoralla pöydällä jousivaa'alla. Veto on vaakasuora ja nopeus tasainen. Silloin veto on yhtä suuri kuin liukukitka ja tukivoima yhtä suuri kuin paino, joten $\mu = F : mg$. Kun mittaus toistetaan eri massoilla, kitkakerroin on $(N, F_\mu)$-kuvaajaan sovitetun suoran kulmakerroin. Suora kulkee origon kautta.

## Esimerkki
Muuttolaatikon massa on $18\,\text{kg}$. Laatikko liukuu lastaussiltaa alas. Silta on $25^\circ$:n kulmassa vaakatasoon nähden, ja laatikon ja sillan välinen liukukitkakerroin on $0{,}30$. Kuinka suuri on laatikon kiihtyvyys, ja kuinka suuri on kitkavoima? Ilmanvastus jätetään huomiotta.

<!-- vaihe -->

**Tunnetut ja kysytty.** $m = 18\,\text{kg}$, $\alpha = 25^\circ$, $\mu = 0{,}30$ ja $g = 9{,}81\,\text{m/s}^2$.

Kysytään kiihtyvyyttä $a$ ja kitkavoimaa $F_\mu$.

<!-- vaihe -->

**Periaate.** Valitaan kappaleeksi laatikko. Siihen vaikuttavat Maa (paino) ja silta (tukivoima ja liukukitka). Laatikko liukuu alas, joten liukukitka osoittaa rinnettä ylös. Newtonin toinen laki kirjoitetaan kahteen suuntaan. Rinteen suunnassa laatikko kiihtyy. Kohtisuoraan pintaa vastaan se ei kiihdy: $a_y = 0$.

<!-- vaihe -->

**Voimakuvio.** Laatikko piirretään suorakulmiona rinteen suuntaisesti, ja voimat lähtevät vaikutuskohdistaan. Akseli $x$ osoittaa rinnettä alas eli kiihtyvyyden suuntaan. Akseli $y$ osoittaa kohtisuoraan pinnasta ulos. Paino jaetaan komponentteihin $G_x = mg\sin\alpha$ ja $G_y = mg\cos\alpha$. Ne on piirretty katkoviivalla.

<svg data-fig="esimerkki" viewBox="0 0 600 420" role="img" aria-label="Laatikon voimakuvio. Laatikko on suorakulmio, joka on kallistettu 25 asteen rinteen suuntaisesti. Paino G lähtee keskipisteestä suoraan alas. Tukivoima N lähtee alapinnasta kohtisuoraan pintaa vastaan ulospäin. Liukukitka lähtee alapinnan ylemmästä kulmasta rinnettä ylös, koska laatikko liukuu alas. Painon komponentit on piirretty katkoviivoin keskipisteestä: G x rinnettä alas ja G y kohtisuoraan pintaa kohti. G x on pidempi kuin kitkavoima. Erillään on ohut oranssi kiihtyvyysnuoli a rinnettä alas. Nurkassa ovat akselit: x rinnettä alas ja y kohtisuoraan pinnasta ulos." style="max-width:100%;font-size:24px">
  <rect x="235" y="132" width="130" height="76" fill="#f6f1e6" stroke="#1f2933" stroke-width="2.5" transform="rotate(-25 300 170)"/>
  <line x1="300" y1="170" x2="300" y2="321" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M300,338 L292,320 L308,320 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="267.5" y="341.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <line x1="332.5" y1="197" x2="275.5" y2="74.5" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M268,59 L283,72 L268.5,79 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="239.5" y="32.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <line x1="375" y1="177" x2="401" y2="165" stroke="#c92a2a" stroke-width="4" stroke-linecap="butt"/>
  <path d="M416.5,157.5 L403.5,172.5 L396.5,158 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <foreignObject x="412" y="151" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_{\mu}$</div></foreignObject>
  <line x1="300" y1="170" x2="237.5" y2="199" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M245,188.5 L235.5,200 L250.5,200.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="193" y="195.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{x}$</div></foreignObject>
  <line x1="300" y1="170" x2="363.5" y2="306" stroke="#c92a2a" stroke-width="2.5" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <path d="M353,299 L364.5,308 L364.5,293.5" fill="none" stroke="#c92a2a" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="370" y="295.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{G}_{y}$</div></foreignObject>
  <line x1="120" y1="120" x2="58.5" y2="148.5" stroke="#e8590c" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M65.5,138 L56.5,149.5 L71,150" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="20" y="140.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$\overline{a}$</div></foreignObject>
  <path d="M300,230 A60,60 0 0 0 325.5,224.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="295.5" y="237.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$25^\circ$</div></foreignObject>
  <line x1="520" y1="330" x2="486.5" y2="345.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M478.5,349.5 L485.5,341 L489.5,349.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <line x1="520" y1="330" x2="504.5" y2="296.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <path d="M500.5,288.5 L509,295.5 L500.5,299.5 Z" fill="#6b7480" stroke-linejoin="round"/>
  <foreignObject x="455.5" y="341" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$x$</div></foreignObject>
  <foreignObject x="484.5" y="261" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$y$</div></foreignObject>
</svg>

<!-- vaihe -->

**Kaava ratkaistuna.** Kuviosta luetaan liikeyhtälöt, ja niistä ratkaistaan kysytyt suureet:
```latex
\begin{aligned}
&x\text{:}\ \ mg\sin\alpha - \mu N = ma \\
&y\text{:}\ \ N - mg\cos\alpha = 0 \\
&F_\mu = \mu mg\cos\alpha \\
&a = g(\sin\alpha - \mu\cos\alpha)
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Muunnoksia ei tarvita. Kaikki suureet ovat SI-yksiköissä, ja kitkakerroin on yksikötön.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan lukuarvot yksiköineen:
```latex
\begin{aligned}
&F_\mu = \mu mg\cos\alpha \\
&\phantom{F_\mu} = 0{,}30\cdot 18\,\text{kg} \\
&\quad\ \cdot 9{,}81\,\text{m/s}^2\cdot\cos 25^\circ \\
&\phantom{F_\mu} \approx 48{,}0\,\text{N} \\[4pt]
&a = g(\sin\alpha - \mu\cos\alpha) \\
&\phantom{a} = 9{,}81\,\text{m/s}^2 \\
&\quad\ \cdot(\sin 25^\circ - 0{,}30\cdot\cos 25^\circ) \\
&\phantom{a} \approx 1{,}48\,\text{m/s}^2
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Laatikon kiihtyvyys on $a \approx 1{,}5\,\text{m/s}^2$ rinnettä alas. Kitkavoima on $F_\mu \approx 48\,\text{N}$. Tuloksissa on kaksi merkitsevää numeroa kuten lähtötiedoissa $\mu = 0{,}30$ ja $m = 18\,\text{kg}$.

<!-- vaihe -->

**Järkevyys.** Ilman kitkaa kiihtyvyys olisi $g\sin 25^\circ \approx 4{,}1\,\text{m/s}^2$. Kitka pienentää kiihtyvyyttä, kuten pitääkin. Kitkavoima $48\,\text{N}$ on pienempi kuin rinteen suuntainen komponentti $G_x \approx 75\,\text{N}$. Siksi kokonaisvoima osoittaa rinnettä alas ja laatikko kiihtyy alas. Massa ei vaikuta kiihtyvyyteen, koska sekä $G_x$ että $F_\mu$ ovat verrannollisia massaan.

## Yleinen virhekäsitys
Moni ajattelee, että kitkavoima on aina $\mu_0 N$ tai $\mu N$ ja aina liikettä vastaan. Lepokitka on kuitenkin vain niin suuri kuin tilanne vaatii. Jos laatikkoa työnnetään $20\,\text{N}$:n voimalla eikä se liiku, lepokitka on $20\,\text{N}$, vaikka sen yläraja olisi suurempi.

Kitka vastustaa pintojen liukumista toistensa suhteen. Siksi se voi osoittaa myös liikkeen suuntaan, kuten kiihtyvän auton lavalla.

Toinen yleinen virhe on pitää tukivoimaa aina painon suuruisena. Rinteellä $N = mg\cos\alpha$ on painoa pienempi. Tämä pätee, kun kohtisuorassa suunnassa vaikuttavat vain paino ja tukivoima eikä kappale kiihdy siinä suunnassa. Paino osoittaa silloinkin suoraan alas eikä kohtisuoraan rinnettä vastaan.

## Tiivistelmä
- Painon suuruus on $G = mg$, ja paino osoittaa aina suoraan alas. Massa on sama kaikkialla, mutta paino riippuu putoamiskiihtyvyydestä.
- Kitka on pinnan suuntainen. Se vastustaa pintojen liukumista toistensa suhteen, ei aina kappaleen liikettä.
- Lepokitka mukautuu tilanteeseen: $F_{\mu 0} \le \mu_0 N$. Liukuvaan kappaleeseen vaikuttaa liukukitka $F_\mu = \mu N$, ja yleensä $\mu < \mu_0$.
- Rinteellä paino jaetaan komponentteihin $G_x = mg\sin\alpha$ ja $G_y = mg\cos\alpha$. Tukivoima on $N = mg\cos\alpha$, kun pintaa vastaan kohtisuorassa vaikuttavat vain paino ja tukivoima eikä kappale kiihdy siinä suunnassa. Komponentit piirretään katkoviivoin, eivätkä ne ole uusia voimia.
- Lepokitkakerroin saadaan rajakulmasta, jolla kappale lähtee liukumaan: $\mu_0 = \tan\alpha_0$.
