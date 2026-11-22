# Valon heijastuminen ja taittuminen

> **Miksi** vesilasiin pantu pilli näyttää katkeavan juuri vedenpinnan kohdalla?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: keittiön pöydällä on vesilasi, jossa on raidallinen pilli. Pillin vedessä oleva osa näyttää siirtyneen sivuun, joten pilli näyttää katkeavan vedenpinnan kohdalla. Takana ikkuna, josta aurinko paistaa." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-10-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Valo etenee säteinä
Valo on sähkömagneettista aaltoliikettä (luku *Sähkömagneettinen säteily ja mustan kappaleen spektri*). Tasalaatuisessa aineessa, kuten ilmassa, vedessä tai lasissa, valo etenee suoraviivaisesti. Valon kulkua kuvataan **säteillä**: säde on viiva, joka näyttää valon etenemissuunnan. Kun valo kohtaa kahden aineen rajapinnan, osa siitä **heijastuu** takaisin samaan aineeseen ja osa jatkaa toiseen aineeseen. Rajapinnan läpi menevä valo yleensä muuttaa suuntaansa: se **taittuu**. Kulmat mitataan aina rajapinnan **normaalista** eli suorasta, joka on kohtisuorassa rajapintaa vastaan säteen osumiskohdassa. Tulevan säteen ja normaalin välinen kulma on tulokulma $\alpha_1$, heijastuneen säteen kulma heijastuskulma $\beta$ ja taittuneen säteen kulma taitekulma $\alpha_2$.

<svg data-fig="interface" viewBox="0 0 600 360" role="img" aria-label="Kaavakuva, kulmat mittakaavassa: valonsäde tulee ilmasta vedenpintaan. Pinnan osumiskohtaan on piirretty harmaa katkoviiva, normaali, joka on kohtisuorassa pintaa vastaan. Tuleva säde tulee vasemmalta ylhäältä normaalin kanssa kulmassa alfa 1, joka on 50 astetta. Ohuempi heijastunut säde lähtee oikealle ylös yhtä suuressa kulmassa beeta. Taittunut säde jatkuu veteen oikealle alas kulmassa alfa 2, joka on 35 astetta, eli se on taittunut kohti normaalia." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-10-interface.webp" x="1.2" y="1.2" width="597" height="368.2" preserveAspectRatio="none"/>
  <foreignObject x="246.5" y="77.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha_1$</div></foreignObject>
  <foreignObject x="327" y="77.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\beta$</div></foreignObject>
  <foreignObject x="313" y="259" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\alpha_2$</div></foreignObject>
  <foreignObject x="77" y="38" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#e64980">$\text{tuleva}$</div></foreignObject>
  <foreignObject x="367.5" y="38" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e64980">$\text{heijastunut}$</div></foreignObject>
  <foreignObject x="398.5" y="288" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e64980">$\text{taittunut}$</div></foreignObject>
  <foreignObject x="182" y="315.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{normaali}$</div></foreignObject>
  <foreignObject x="28" y="135.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ilma},\ n_1$</div></foreignObject>
  <foreignObject x="28" y="189.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{vesi},\ n_2$</div></foreignObject>
</svg>

### Heijastuslaki
Valo heijastuu samalla tavalla kuin mekaaniset aallot luvussa *Aalto kohtaa esteen tai raon*: heijastuskulma on yhtä suuri kuin tulokulma, ja tuleva säde, heijastunut säde ja normaali ovat samassa tasossa. Sileä pinta, kuten peili tai tyyni vedenpinta, heijastaa yhdensuuntaiset säteet yhdensuuntaisina, joten siitä näkyy kuva. Karhealla pinnalla, kuten paperilla, normaali osoittaa joka kohdassa eri suuntaan. Siksi pinta heijastaa valoa kaikkiin suuntiin, ja paperin näkee mistä suunnasta tahansa. Heijastuslaki pätee silloinkin jokaisessa pinnan pienessä kohdassa.

### Valo hidastuu aineessa
Tyhjiössä valo etenee nopeudella $c = 3{,}00 \cdot 10^{8}\,\text{m/s}$. Aineessa valo etenee hitaammin. Aineen **taitekerroin** $n$ kertoo, kuinka monta kertaa hitaammin: vedessä valon nopeus on noin $2{,}26 \cdot 10^{8}\,\text{m/s}$, joten veden taitekerroin on $1{,}33$. Ilman taitekerroin on $1{,}0003$, joten ilmassa valo etenee lähes yhtä nopeasti kuin tyhjiössä. Aine, jonka taitekerroin on suurempi, on **optisesti tiheämpi**. Kun valo siirtyy aineesta toiseen, sen taajuus ei muutu, koska taajuuden määrää valonlähde. Nopeus kuitenkin muuttuu, joten myös aallonpituus muuttuu yhtälön $v = f \lambda$ mukaan: vedessä aallonpituus on $1{,}33$ kertaa lyhyempi kuin ilmassa.

```pysahdy
Valo siirtyy ilmasta veteen. Muuttuuko sen taajuus ja muuttuuko sen aallonpituus?
---
Taajuus ei muutu, koska sen määrää valonlähde. Aallonpituus lyhenee: vedessä se on $1{,}33$ kertaa lyhyempi kuin ilmassa, koska nopeus pienenee ja $v = f \lambda$.
```

### Miksi valo taittuu
Taittuminen johtuu nopeuden muutoksesta. Kuvassa vinosti rajapintaan tulevan aallon aaltorintamat ovat yhdensuuntaisia viivoja, ja säde on kohtisuorassa niitä vastaan. Rintaman vasen pää saapuu veteen ensin ja hidastuu, kun oikea pää kulkee vielä ilmassa nopeammin. Siksi rintama kääntyy, ja vedessä aalto etenee uuteen suuntaan, lähempänä normaalia. Vedessä rintamat ovat myös tiheämmässä, koska aallonpituus on lyhyempi. Kun valo tulee kohtisuoraan rajapintaan, $\alpha_1 = 0^\circ$, rintaman kaikki kohdat hidastuvat yhtä aikaa, eikä suunta muutu.

<svg data-fig="wavefronts" viewBox="0 0 600 360" role="img" aria-label="Kaavakuva, mittakaavassa veden taitekertoimella 1,33: valoaalto tulee ilmasta vinosti vedenpintaan. Aaltorintamat ovat yhdensuuntaisia viivoja, jotka ovat kohtisuorassa sädettä vastaan. Ilmassa rintamien väli on aallonpituus lambda 1. Rintaman vasen pää on jo vedessä, kun oikea pää on vielä ilmassa. Vedessä rintamat ovat lähempänä toisiaan, aallonpituus lambda 2 on lyhyempi, ja rintamat ovat kääntyneet niin, että säde etenee lähempänä normaalia." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-10-wavefronts.webp" x="2.5" y="2.5" width="594.1" height="365.1" preserveAspectRatio="none"/>
  <foreignObject x="309.5" y="31" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda_1$</div></foreignObject>
  <foreignObject x="219.5" y="292.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda_2$</div></foreignObject>
  <foreignObject x="28" y="31.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ilma}$</div></foreignObject>
  <foreignObject x="28" y="307.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{vesi}$</div></foreignObject>
</svg>

### Kohti normaalia tai siitä poispäin
Kun valo siirtyy optisesti tiheämpään aineeseen, esimerkiksi ilmasta veteen, se taittuu **kohti normaalia**: taitekulma on pienempi kuin tulokulma. Kun valo siirtyy optisesti harvempaan aineeseen, esimerkiksi vedestä ilmaan, se taittuu **normaalista poispäin**. Valon kulku on käännettävissä: jos säde kulkee ilmasta veteen tiettyä reittiä, vedestä ilmaan tuleva säde voi kulkea saman reitin takaisin. Mitä suurempi on taitekertoimien ero, sitä enemmän säde taittuu samalla tulokulmalla. Siksi timantti, jonka taitekerroin on $2{,}42$, taittaa valoa paljon enemmän kuin vesi.

### Osittainen heijastuminen
Tavallisesti kahden läpinäkyvän aineen rajapinnassa osa valosta heijastuu ja osa läpäisee rajapinnan. Tähän on kuitenkin poikkeuksia: kokonaisheijastumisessa toiseen aineeseen ei etene taittunutta valonsädettä (luku *Kokonaisheijastuminen ja valokuitu*), ja Brewsterin kulmassa tietty valon polarisaatiosuunta ei heijastu (luku *Valon polarisaatio*). Kun valo tulee kohtisuoraan ilmasta lasiin, lasin kummastakin pinnasta heijastuu noin $4\,\%$ valosta ja vedenpinnasta noin $2\,\%$. Mitä suurempi tulokulma on eli mitä enemmän valo tulee pintaa hipoen, sitä suurempi osa heijastuu. Siksi järven pinta peilaa iltaisin rannan puut, vaikka pohja näkyy, kun katsoo suoraan alas. Ikkunasta näkee illalla oman huoneensa heijasteen, koska ulkoa tulee vähän valoa ja huoneesta lasiin osuva valo heijastuu osittain takaisin. Heijastunut ja läpi mennyt osa ovat yhteensä yhtä paljon kuin tuleva valo, kun aine ei absorboi valoa.

### Näennäinen syvyys
Kun katsot uima-altaan pohjassa olevaa kolikkoa, kolikosta lähtevät säteet taittuvat vedenpinnassa normaalista poispäin. Silmä ja aivot tulkitsevat, että valo on tullut suoraan viivaa pitkin. Kun silmään tulevat säteet jatketaan taaksepäin veteen, ne näyttävät lähtevän kohdasta, joka on ylempänä kuin kolikko. Siksi allas näyttää matalammalta kuin se on, ja kolikko näyttää olevan lähempänä pintaa. Samasta syystä pillin vedessä oleva osa näyttää nousseen ylemmäs, kun lasia katsotaan vinosti ylhäältä vedenpinnan läpi, ja pilli näyttää katkeavan vedenpinnan kohdalla. Koska katsot vinosti, ylemmäs nostettu osa näkyy samalla sivuun siirtyneenä.

<svg data-fig="depth" viewBox="0 0 600 360" role="img" aria-label="Kaavakuva, kulmat veden taitekertoimella 1,33: uima-altaan poikkileikkaus. Altaan pohjalla vasemmalla on kolikko. Siitä lähtee kaksi sädettä vinosti ylös oikealle. Vedenpinnassa säteet taittuvat normaalista poispäin ja jatkuvat oikealla ylhäällä olevaan silmään. Säteiden jatkeet on piirretty harmaina katkoviivoina takaisin veteen: ne kohtaavat kolikon yläpuolella, ja siinä kohdassa silmä näkee kolikon. Kolikko näyttää olevan lähempänä pintaa kuin todellisuudessa." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-10-depth.webp" x="1.2" y="1.2" width="597" height="368.2" preserveAspectRatio="none"/>
  <foreignObject x="133" y="289.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{kolikko}$</div></foreignObject>
  <foreignObject x="55" y="179" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{näennäinen paikka}$</div></foreignObject>
  <foreignObject x="28" y="77.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ilma}$</div></foreignObject>
  <foreignObject x="514" y="281.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{vesi}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/pencil-in-water.webp" alt="Sininen lyijykynä vinossa vesilasissa harmaata seinää vasten; vedenpinnan kohdalla kynä näyttää katkeavan ja siirtyvän sivuun."><figcaption>Lyijykynä vesilasissa näyttää katkenneelta. Veden alla olevasta kynän osasta lähtevä valo taittuu, kun se tulee vedestä lasin läpi ilmaan, joten näemme kynän eri paikassa kuin se on.</figcaption></figure>

## Kaava: Heijastuslaki ja taittumislaki
Heijastuslaki: heijastuskulma on yhtä suuri kuin tulokulma,
```latex
\beta = \alpha_1
```
missä $\beta$ on heijastuskulma ja $\alpha_1$ tulokulma, molemmat mitattuina rajapinnan normaalista.

Aineen taitekerroin on valon nopeuden suhde tyhjiössä ja aineessa:
```kaavat
taitekerroin sähkömagneettiselle aaltoliikkeelle (valolle) :: n = \frac{c}{v}
```
missä $c = 3{,}00 \cdot 10^{8}\,\text{m/s}$ on valon nopeus tyhjiössä ja $v$ valon nopeus aineessa (m/s). Taitekerroin on yksikötön, ja näkyvälle valolle läpinäkyvissä aineissa se on aina suurempi kuin $1$.

```pysahdy
Valon nopeus tyhjiössä on $3{,}00 \cdot 10^{8}\,\text{m/s}$ ja timantin taitekerroin on $2{,}42$. Kuinka nopeasti valo etenee timantissa?
---
Nopeus on $v = c : n = 3{,}00 \cdot 10^{8}\,\text{m/s} : 2{,}42 \approx 1{,}24 \cdot 10^{8}\,\text{m/s}$.
```

### Taittumislaki eli Snellin laki
Kun valo siirtyy aineesta, jonka taitekerroin on $n_1$, aineeseen, jonka taitekerroin on $n_2$, tulokulma ja taitekulma toteuttavat yhtälön
```kaavat
taittumislaki (Snellin laki) :: n_1 \sin \alpha_1 = n_2 \sin \alpha_2
```
missä $\alpha_1$ on tulokulma ja $\alpha_2$ taitekulma normaalista mitattuina. Laki seuraa aaltorintamien kääntymisestä: kulmien sinien suhde on sama kuin nopeuksien suhde, $\sin\alpha_1 : \sin\alpha_2 = v_1 : v_2 = n_2 : n_1$. Laki koskee kulmien sinejä, ei kulmia: kun tulokulma kaksinkertaistuu, taitekulma ei kaksinkertaistu. Kuvaajassa taitekulma kasvaa tulokulman mukana, mutta yhä hitaammin.

<svg data-fig="graph" viewBox="0 0 600 360" role="img" aria-label="Kuvaaja mittakaavassa: taitekulma alfa 2 tulokulman alfa 1 funktiona, kun valo tulee ilmasta, jonka taitekerroin on 1,00, veteen (taitekerroin 1,33) ja timanttiin (2,42). Molemmat käyrät kulkevat suoran alfa 2 = alfa 1 alapuolella, joten säde taittuu kohti normaalia. Käyrät kaartuvat loivemmiksi: tulokulmalla 90 astetta taitekulma on vedessä 48,8 ja timantissa 24,4 astetta. Katkoviiva alfa 2 = alfa 1 kuvaa tilannetta, jossa aineilla on sama taitekerroin." style="max-width:100%;font-size:24px">
  <line x1="128.5" y1="306" x2="128.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="165" y1="306" x2="165" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="201.5" y1="306" x2="201.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="238" y1="306" x2="238" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="274" y1="306" x2="274" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="310.5" y1="306" x2="310.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="347" y1="306" x2="347" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="383.5" y1="306" x2="383.5" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="306" x2="420" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="278" x2="420" y2="278" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="250.5" x2="420" y2="250.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="222.5" x2="420" y2="222.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="195" x2="420" y2="195" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="167" x2="420" y2="167" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="139.5" x2="420" y2="139.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="111.5" x2="420" y2="111.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="84" x2="420" y2="84" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="92" y1="56" x2="420" y2="56" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="91" y1="306" x2="434" y2="306" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M446,306 L433,312 L433,300 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="92" y1="307" x2="92" y2="42" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M92,30 L98,43 L86,43 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="128.5" y1="306" x2="128.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="165" y1="306" x2="165" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="201.5" y1="306" x2="201.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="185" y="315.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="238" y1="306" x2="238" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="274" y1="306" x2="274" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="310.5" y1="306" x2="310.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="294" y="315.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="347" y1="306" x2="347" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="383.5" y1="306" x2="383.5" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="420" y1="306" x2="420" y2="313" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="403.5" y="315.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$90$</div></foreignObject>
  <line x1="85" y1="278" x2="92" y2="278" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="85" y1="250.5" x2="92" y2="250.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="85" y1="222.5" x2="92" y2="222.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="208" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$30$</div></foreignObject>
  <line x1="85" y1="195" x2="92" y2="195" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="85" y1="167" x2="92" y2="167" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="85" y1="139.5" x2="92" y2="139.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="125" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$60$</div></foreignObject>
  <line x1="85" y1="111.5" x2="92" y2="111.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="85" y1="84" x2="92" y2="84" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="85" y1="56" x2="92" y2="56" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="47" y="41.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$90$</div></foreignObject>
  <foreignObject x="62" y="311.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="452" y="291.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\alpha_1\ (^\circ)$</div></foreignObject>
  <foreignObject x="82" y="-0.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\alpha_2\ (^\circ)$</div></foreignObject>
  <polyline points="92,306 420,56" fill="none" stroke="#6b7480" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <polyline points="92,306 94.5,304.5 97.5,303 100,301.5 103,299.5 105.5,298 108.5,296.5 111,295 114,293.5 116.5,292 119.5,290.5 122,289 125,287 127.5,285.5 130.5,284 133,282.5 135.5,281 138.5,279.5 141,278 144,276.5 146.5,275 149.5,273.5 152,271.5 155,270 157.5,268.5 160.5,267 163,265.5 166,264 168.5,262.5 171.5,261 174,259.5 176.5,258 179.5,256.5 182,255 185,253.5 187.5,252 190.5,250.5 193,249 196,247.5 198.5,246 201.5,244.5 204,243 207,241.5 209.5,240.5 212.5,239 215,237.5 217.5,236 220.5,234.5 223,233 226,231.5 228.5,230.5 231.5,229 234,227.5 237,226 239.5,225 242.5,223.5 245,222 248,221 250.5,219.5 253.5,218 256,217 258.5,215.5 261.5,214 264,213 267,211.5 269.5,210.5 272.5,209 275,208 278,206.5 280.5,205.5 283.5,204.5 286,203 289,202 291.5,201 294.5,199.5 297,198.5 299.5,197.5 302.5,196.5 305,195 308,194 310.5,193 313.5,192 316,191 319,190 321.5,189 324.5,188 327,187.5 330,186.5 332.5,185.5 335.5,184.5 338,184 340.5,183 343.5,182 346,181.5 349,180.5 351.5,180 354.5,179 357,178.5 360,178 362.5,177 365.5,176.5 368,176 371,175.5 373.5,175 376.5,174.5 379,174 381.5,173.5 384.5,173 387,173 390,172.5 392.5,172 395.5,172 398,171.5 401,171.5 403.5,171 406.5,171 409,171 412,170.5 414.5,170.5 417.5,170.5 420,170.5" fill="none" stroke="#2f74b5" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="92,306 94.5,305 97.5,304.5 100,303.5 103,302.5 105.5,301.5 108.5,301 111,300 114,299 116.5,298.5 119.5,297.5 122,296.5 125,295.5 127.5,295 130.5,294 133,293 135.5,292.5 138.5,291.5 141,290.5 144,290 146.5,289 149.5,288 152,287.5 155,286.5 157.5,285.5 160.5,285 163,284 166,283 168.5,282.5 171.5,281.5 174,280.5 176.5,280 179.5,279 182,278.5 185,277.5 187.5,276.5 190.5,276 193,275 196,274.5 198.5,273.5 201.5,273 204,272 207,271.5 209.5,270.5 212.5,270 215,269 217.5,268.5 220.5,267.5 223,267 226,266 228.5,265.5 231.5,265 234,264 237,263.5 239.5,263 242.5,262 245,261.5 248,261 250.5,260 253.5,259.5 256,259 258.5,258 261.5,257.5 264,257 267,256.5 269.5,255.5 272.5,255 275,254.5 278,254 280.5,253.5 283.5,253 286,252.5 289,251.5 291.5,251 294.5,250.5 297,250 299.5,249.5 302.5,249 305,248.5 308,248 310.5,248 313.5,247.5 316,247 319,246.5 321.5,246 324.5,245.5 327,245 330,245 332.5,244.5 335.5,244 338,243.5 340.5,243.5 343.5,243 346,242.5 349,242.5 351.5,242 354.5,241.5 357,241.5 360,241 362.5,241 365.5,240.5 368,240.5 371,240 373.5,240 376.5,240 379,239.5 381.5,239.5 384.5,239 387,239 390,239 392.5,239 395.5,238.5 398,238.5 401,238.5 403.5,238.5 406.5,238.5 409,238.5 412,238.5 414.5,238 417.5,238 420,238" fill="none" stroke="#e64980" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="430" y="156" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2f74b5">$\text{vesi}$</div></foreignObject>
  <foreignObject x="430" y="223.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e64980">$\text{timantti}$</div></foreignObject>
  <foreignObject x="430" y="45.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\alpha_2 = \alpha_1$</div></foreignObject>
  <foreignObject x="106.5" y="69.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$n_1 = 1{,}00$</div></foreignObject>
</svg>

```pysahdy
Valonsäde tulee ilmasta ($n = 1{,}00$) ikkunalasiin ($n = 1{,}52$) tulokulmalla $40^\circ$. Mikä on taitekulma ja taittuuko säde kohti normaalia vai siitä poispäin?
---
Snellin laista $\sin\alpha_2 = 1{,}00 \cdot \sin 40^\circ : 1{,}52 = 0{,}423$, joten $\alpha_2 \approx 25^\circ$. Lasi on optisesti tiheämpi, joten säde taittuu kohti normaalia.
```

### Taitekertoimia
Taitekerroin riippuu hieman valon aallonpituudesta (luku *Dispersio: prisma ja sateenkaari*). Taulukon arvot ovat keltaiselle valolle, jonka aallonpituus on $589\,\text{nm}$, ja huoneenlämpöiselle aineelle. Lasin ja akryylin taitekertoimet vaihtelevat laadun mukaan.

| aine | $n$ |
| --- | --- |
| ilma | $1{,}0003$ |
| vesi | $1{,}33$ |
| etanoli | $1{,}36$ |
| akryyli | $1{,}49$ |
| ikkunalasi | $1{,}52$ |
| timantti | $2{,}42$ |

Lähde: *CRC Handbook of Chemistry and Physics*, 97. painos, 2016; lasin ja akryylin arvot ovat tyypillisiä arvoja. Laskuissa ilman taitekertoimena käytetään arvoa $1{,}00$.

## Esimerkki
Laserin säde tulee ilmasta altaan vedenpintaan tulokulmassa $55{,}0^\circ$. Kuinka suuri on taitekulma vedessä, ja kuinka suurella nopeudella valo etenee vedessä? Ilman taitekerroin on $1{,}00$ ja veden $1{,}33$.

<!-- vaihe -->

**Tunnetut ja kysytty.** Tulokulma $\alpha_1 = 55{,}0^\circ$, ilman taitekerroin $n_1 = 1{,}00$, veden taitekerroin $n_2 = 1{,}33$ ja valon nopeus tyhjiössä $c = 3{,}00 \cdot 10^{8}\,\text{m/s}$.

Kysytään taitekulmaa $\alpha_2$ ja valon nopeutta vedessä $v$.

<!-- vaihe -->

**Periaate.** Valo siirtyy ilmasta veteen, joten se taittuu rajapinnassa taittumislain mukaan. Vesi on optisesti tiheämpää, joten säde taittuu kohti normaalia. Valon nopeus vedessä saadaan taitekertoimen määritelmästä $n = c : v$.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&n_1 \sin\alpha_1 = n_2 \sin\alpha_2 \\
&\sin\alpha_2 = \frac{n_1 \sin\alpha_1}{n_2} \\[6pt]
&n_2 = \frac{c}{v} \;\Rightarrow\; v = \frac{c}{n_2}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: taitekertoimet ovat yksikköttömiä, ja kulma on asteina. Nopeus saadaan samassa yksikössä kuin $c$ eli metreinä sekunnissa.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&\sin\alpha_2 = \frac{n_1 \sin\alpha_1}{n_2} \\
&= \frac{1{,}00 \cdot \sin 55{,}0^\circ}{1{,}33} \\
&= 0{,}6159 \\
&\alpha_2 = 38{,}02^\circ \\[6pt]
&v = \frac{c}{n_2} \\
&= \frac{3{,}00 \cdot 10^{8}\,\text{m/s}}{1{,}33} \\
&= 2{,}256 \cdot 10^{8}\,\text{m/s}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Taitekulma on $\alpha_2 \approx 38{,}0^\circ$, ja valo etenee vedessä nopeudella $v \approx 2{,}26 \cdot 10^{8}\,\text{m/s}$. Tulokset ilmoitetaan kolmella merkitsevällä numerolla kuten tulokulma $55{,}0^\circ$ ja taitekertoimet.

<!-- vaihe -->

**Järkevyys.** Säde taittuu kohti normaalia, koska $38{,}0^\circ < 55{,}0^\circ$, kuten optisesti tiheämpään aineeseen siirtyessä pitääkin. Nopeus on pienempi kuin $c$, ja sinien suhde on sama kuin nopeuksien suhde: $\sin 55{,}0^\circ : \sin 38{,}0^\circ \approx 1{,}33$ ja $3{,}00 : 2{,}26 \approx 1{,}33$.

## Yleinen virhekäsitys
Moni mittaa tulokulman rajapinnasta eikä normaalista. Jos säde ja vedenpinta ovat $30^\circ$:n kulmassa, tulokulma on $90^\circ - 30^\circ = 60^\circ$. Toinen virhe on ajatella, että taitekulma on verrannollinen tulokulmaan. Taittumislaki koskee kulmien sinejä: ilmasta veteen tulokulmalla $30^\circ$ taitekulma on $22{,}1^\circ$, mutta tulokulmalla $60^\circ$ se on $40{,}6^\circ$ eikä $44{,}2^\circ$. Kolmas virhe on uskoa, että valo taittuu aina kohti normaalia. Suunta riippuu siitä, kumpi aine on optisesti tiheämpi: vedestä ilmaan tuleva säde taittuu normaalista poispäin. Neljäs virhe on luulla, että valo taittuu, koska se ”törmää” pintaan. Valo taittuu, koska sen nopeus muuttuu.

## Tiivistelmä
- Rajapinnassa osa valosta yleensä heijastuu ja osa taittuu. Kulmat mitataan rajapinnan normaalista.
- Heijastuslaki: $\beta = \alpha_1$, ja tuleva säde, heijastunut säde ja normaali ovat samassa tasossa.
- Taitekerroin $n = c : v$ kertoo, kuinka monta kertaa hitaammin valo etenee aineessa kuin tyhjiössä.
- Taittumislaki: $n_1 \sin\alpha_1 = n_2 \sin\alpha_2$. Optisesti tiheämpään aineeseen säde taittuu kohti normaalia, harvempaan normaalista poispäin.
- Vedessä olevat esineet näyttävät olevan lähempänä pintaa kuin ne ovat, koska niistä tulevat säteet taittuvat vedenpinnassa.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: tyyni järvi illalla. Vastarannan kuuset heijastuvat vedenpinnasta ylösalaisin. Etualalla rannan lähellä näkyy veden läpi kiviä pohjassa." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-10-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
