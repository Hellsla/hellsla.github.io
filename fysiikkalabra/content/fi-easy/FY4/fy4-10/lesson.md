# Liikemäärän säilyminen ja yksiulotteiset törmäykset

> **Miksi** biljardin lyöntipallo voi pysähtyä paikalleen, kun se osuu suoraan levossa olevaan palloon? Toinen pallo jatkaa silloin matkaa lähes samalla nopeudella.

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: biljardipöytä läheltä nähtynä. Pöydän yllä roikkuu lamppu, ja sen valo osuu pöytään. Vasemmalta alhaalta osoittaa biljardikeppi, jolla valkoista lyöntipalloa on juuri lyöty. Lyöntipallo on osunut suoraan punaiseen palloon. Hetki törmäyksen jälkeen lyöntipallo on pysähtynyt pöydän keskelle, ja sen takana näkyy haalea jälki kuljetusta matkasta. Punainen pallo kiitää eteenpäin kohti pöydän oikeaa reunaa, ja sen takana on liikeviivoja. Pöydän takaosassa on kolme muuta palloa." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-10-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Systeemi ja sen kokonaisliikemäärä
Luvussa *Liikemäärä ja impulssi* opit, että kappaleen liikemäärä on $\overline{p} = m\overline{v}$. Opit myös, että vakiosuuruisen kokonaisvoiman impulssi muuttaa liikemäärää: $\Delta\overline{p} = \Sigma\overline{F}\,\Delta t$. Törmäyksessä on kuitenkin kaksi kappaletta, jotka vaikuttavat toisiinsa. Siksi tarkastellaan niitä yhdessä **systeeminä**. Systeemi on kappaleiden joukko, jota tutkitaan yhtenä kokonaisuutena. Systeemin **kokonaisliikemäärä** on sen kappaleiden liikemäärien vektorisumma, $\overline{p}_\text{kok} = \overline{p}_1 + \overline{p}_2$.

Systeemin kappaleet vaikuttavat toisiinsa **sisäisillä voimilla**. Esimerkki ovat vaunujen puskurien voimat toisiinsa törmäyksessä. Voimat, jotka tulevat systeemin ulkopuolelta, ovat **ulkoisia voimia**. Esimerkkejä ovat vaunujen paino, radan tukivoima ja kitka.

### Miksi kokonaisliikemäärä säilyy
Vaunu 1 työntää vaunua 2 voimalla $\overline{F}$. Newtonin kolmannen lain mukaan vaunu 2 työntää silloin vaunua 1 yhtä suurella voimalla $-\overline{F}$ vastakkaiseen suuntaan. Voimat alkavat ja loppuvat samalla hetkellä, joten ne vaikuttavat saman ajan $\Delta t$. Oletetaan, että voima on vakio. Silloin vaunun 2 liikemäärä muuttuu impulssin $\overline{F}\,\Delta t$ verran. Vaunun 1 liikemäärä muuttuu yhtä paljon vastakkaiseen suuntaan. Toinen vaunu saa liikemäärää täsmälleen sen verran kuin toinen menettää. Kokonaisliikemäärä ei muutu. Sama pätee, vaikka voima muuttuisi törmäyksen aikana. Voimat ovat nimittäin joka hetki yhtä suuret ja vastakkaissuuntaiset.

<svg data-fig="vuorovaikutus" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva, ei mittakaavassa. Kuvassa on kaksi ilmatyynyradan vaunua törmäyksen aikana. Vaunujen väliin jäävä jousipuskuri on puristunut. Ylhäällä ovat punaiset voimanuolet. Vaunu 1 työntää vaunua 2 oikealle voimalla F. Vaunu 2 työntää vaunua 1 vasemmalle yhtä suurella voimalla vastakkaiseen suuntaan, −F. Molemmat voimat vaikuttavat saman ajan Δt. Alhaalla violetit nuolet ovat liikemäärien muutokset. Vaunun 1 muutos Δp1 = −FΔt osoittaa vasemmalle. Vaunun 2 muutos Δp2 = FΔt osoittaa oikealle. Nuolet ovat yhtä pitkät. Niiden summa on nolla." class="fig-anim" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-10-vuorovaikutus.webp" x="1.2" y="1.2" width="597" height="348.3" preserveAspectRatio="none"/>
  <foreignObject x="240" y="89.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="350" y="89.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="488.5" y="45.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="72.5" y="45.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$-\overline{F}$</div></foreignObject>
  <foreignObject x="283.5" y="25.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta t$</div></foreignObject>
  <foreignObject x="87.5" y="257.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$\Delta\overline{p}_1 = -\overline{F}\,\Delta t$</div></foreignObject>
  <foreignObject x="373.5" y="257.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$\Delta\overline{p}_2 = \overline{F}\,\Delta t$</div></foreignObject>
  <foreignObject x="221" y="299.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta\overline{p}_1 + \Delta\overline{p}_2 = \overline{0}$</div></foreignObject>
</svg>

Tämä päättely toimii vain, jos ulkoiset voimat eivät muuta liikemäärää. Vaakasuoralla ilmatyynyradalla paino ja tukivoima kumoavat toisensa. Kitka on hyvin pieni. Törmäävät autot taas kokevat tien kitkan. Törmäys kestää kuitenkin vain sekunnin murto-osan. Silloin puskurien voimat ovat paljon suurempia kuin kitka. Kitkan impulssi jää siksi törmäyksen aikana niin pieneksi, ettei sillä ole merkitystä. Tästä saadaan **liikemäärän säilymislaki**: kun systeemiin vaikuttavien ulkoisten voimien summa on nolla tai niiden impulssi on törmäyksen aikana merkityksettömän pieni, systeemin kokonaisliikemäärä säilyy.

```pysahdy
Auton törmäyksessä tien kitka vaikuttaa autoihin. Miksi kokonaisliikemäärää voi silti pitää säilyvänä?
---
Törmäys kestää vain sekunnin murto-osan. Puskurien voimat ovat paljon suurempia kuin kitka. Kitkan impulssi on siksi hyvin pieni.
```

### Törmäysten lajit
Liikemäärä säilyy jokaisessa törmäyksessä, kun säilymislain ehto täyttyy. Liike-energia ei säily aina. Törmäys on **kimmoisa**, jos kappaleiden yhteinen liike-energia on törmäyksen jälkeen yhtä suuri kuin ennen sitä. Teräskuulat, biljardipallot ja jousipuskurilla varustetut vaunut törmäävät lähes kimmoisasti. Törmäys on **kimmoton**, jos osa liike-energiasta muuttuu muiksi energiamuodoiksi. Kappaleet muuttavat silloin muotoaan. Liike-energiaa muuttuu niiden sisäenergiaksi ja ääneksi. Joskus kappaleet jäävät kiinni toisiinsa ja jatkavat yhdessä. Silloin törmäys on **täysin kimmoton**, ja liike-energia pienenee mahdollisimman paljon. Silloin mahdollisimman suuri osa siitä muuttuu muiksi energiamuodoiksi.

<svg data-fig="tarra" viewBox="0 0 600 360" role="img" aria-label="Kaavakuva mittakaavassa. Kuvassa on kaksi samanmassaista vaunua ilmatyynyradalla: ylhäällä ennen törmäystä ja alhaalla sen jälkeen. Ennen törmäystä vaunu 1 liikkuu oikealle nopeudella v. Sen liikemäärä p on violetti nuoli. Vaunu 2 on levossa. Vaunujen päissä on tarranauhat. Törmäyksen jälkeen vaunut ovat tarttuneet yhteen ja liikkuvat yhdessä puolella alkuperäisestä nopeudesta. Sininen nopeusnuoli on puolet lyhyempi. Yhteisen liikemäärän violetti nuoli on yhtä pitkä kuin vaunun 1 liikemäärä ennen törmäystä." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-10-tarra.webp" x="0" y="0" width="600" height="371.2" preserveAspectRatio="none"/>
  <foreignObject x="36" y="7.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ennen}$</div></foreignObject>
  <foreignObject x="36" y="185.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{jälkeen}$</div></foreignObject>
  <foreignObject x="160" y="109.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="390" y="109.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="260" y="69.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="260" y="37.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$\overline{p}$</div></foreignObject>
  <foreignObject x="358.5" y="65.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\overline{v}_2 = \overline{0}$</div></foreignObject>
  <foreignObject x="240" y="277.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="340" y="277.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="274" y="237.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\tfrac{1}{2}\overline{v}$</div></foreignObject>
  <foreignObject x="340" y="205.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$\overline{p}$</div></foreignObject>
</svg>

Kuvassa samanmassaiset vaunut tarttuvat yhteen tarranauhalla. Kokonaisliikemäärä on sama ennen ja jälkeen. Nyt sama liikemäärä jakautuu kaksinkertaiselle massalle, joten yhteinen nopeus on puolet alkuperäisestä. Liike-energia $\tfrac12 mv^2$ ei säily: kaksinkertainen massa ja puolet nopeudesta antavat puolet alkuperäisestä liike-energiasta. Toinen puoli muuttuu tarranauhan ja vaunujen sisäenergiaksi.

```pysahdy
Vaunut tarttuvat yhteen. Minne liike-energia menee, kun se pienenee?
---
Se ei katoa. Se muuttuu tarranauhan ja vaunujen sisäenergiaksi. Kokonaisenergia säilyy.
```

### Räjähdys
**Räjähdyksessä** levossa oleva tai yhdessä liikkuva systeemi hajoaa osiin sisäisten voimien vaikutuksesta. Esimerkkejä ovat jousi, joka laukeaa vaunujen välissä, luistelijat, jotka työntävät toisiaan, ja ruuti, joka työntää luotia ja kivääriä. Jos systeemi on aluksi levossa, sen kokonaisliikemäärä on nolla ja pysyy nollana. Kun levossa oleva systeemi hajoaa kahdeksi osaksi, osat saavat yhtä suuret liikemäärät vastakkaisiin suuntiin. Kevyempi osa saa suuremman nopeuden. Siksi kivääri potkaisee taaksepäin, kun luoti lähtee eteenpäin. Jos osia on useampia, niiden liikemäärien vektorisumma on nolla. Yksittäisten osien liikemäärät voivat silloin olla erisuuruisia. Räjähdyksessä liike-energia kasvaa, koska jousen, lihasten tai ruudin energiaa muuttuu liike-energiaksi.

```pysahdy
Luistelija seisoo jäällä ja heittää raskaan pallon eteenpäin. Miksi hän liukuu itse taaksepäin?
---
Pallo saa liikemäärän eteenpäin. Kokonaisliikemäärä pysyy nollana. Siksi luistelija saa yhtä suuren liikemäärän taaksepäin.
```

### Vastaus alun kysymykseen
Biljardipallot ovat yhtä raskaita, ja niiden törmäys on lähes kimmoisa. Lyöntipallon nopeus on $v$. Liikemäärän säilymisestä seuraa, että pallojen nopeuksien summa pysyy samana: $v_1' + v_2' = v$. Liike-energian säilymisestä seuraa, että nopeuksien neliöiden summa pysyy samana: $v_1'^2 + v_2'^2 = v^2$. Korotetaan ensimmäinen ehto toiseen potenssiin ja vähennetään siitä toinen ehto. Saadaan $2 v_1' v_2' = 0$, joten toinen palloista on törmäyksen jälkeen levossa. Lyöntipallo ei voi kulkea toisen pallon läpi, joten se pysähtyy. Toinen pallo jatkaa nopeudella $v$. Oikeassa pelissä pallot myös pyörivät, eikä törmäys ole täysin kimmoisa. Siksi lyöntipallo voi jäädä hiukan liikkeeseen.

<figure class="unit-photo"><img src="pics/fy4/newtons-cradle.webp" alt="Newtonin kehto: rivi riippuvia teräskuulia."><figcaption>Newtonin kehto. Vasemmalta tuleva kuula osuu muihin kuuliin. Liikkuva kuula näkyy kuvassa epäselvänä.</figcaption></figure>

## Kaava: Liikemäärän säilymislaki

### Säilymislaki vektoreina ja yhdessä ulottuvuudessa
Oletetaan, että systeemiin vaikuttavien ulkoisten voimien summa on nolla tai niiden impulssi on törmäyksen tai räjähdyksen aikana merkityksettömän pieni. Silloin kokonaisliikemäärä on sama ennen ja jälkeen:
```latex
\overline{p}_1 + \overline{p}_2 = \overline{p}_1' + \overline{p}_2'
```
missä $\overline{p}_1$ ja $\overline{p}_2$ ovat kappaleiden liikemäärät ennen, ja $\overline{p}_1'$ ja $\overline{p}_2'$ ovat liikemäärät jälkeen ($\text{kg}\cdot\text{m/s}$).

Yksiulotteisessa törmäyksessä kaikki nopeudet ovat samalla suoralla. Valitaan positiivinen suunta. Silloin jokainen nopeus on luku, jolla on etumerkki. Vastakkaiseen suuntaan liikkuvan kappaleen nopeus on negatiivinen. Säilymislaki tulee muotoon
```latex
\begin{aligned}
&m_1 v_1 + m_2 v_2 \\
&\quad = m_1 v_1' + m_2 v_2'
\end{aligned}
```
missä $m_1$ ja $m_2$ ovat kappaleiden massat ($\text{kg}$), $v_1$ ja $v_2$ ovat niiden nopeudet ennen, ja $v_1'$ ja $v_2'$ ovat nopeudet jälkeen ($\text{m/s}$).

### Täysin kimmoton törmäys
Joskus kappaleet jäävät kiinni toisiinsa. Silloin niillä on törmäyksen jälkeen yhteinen nopeus $v'$:
```latex
\begin{aligned}
&m_1 v_1 + m_2 v_2 \\
&\quad = (m_1 + m_2)\,v'
\end{aligned}
```
missä $v'$ on nopeus, jolla kappaleet liikkuvat yhdessä törmäyksen jälkeen ($\text{m/s}$). Esimerkki: $0{,}40\,\text{kg}$:n vaunu liikkuu nopeudella $0{,}60\,\text{m/s}$ ja tarttuu levossa olevaan samanlaiseen vaunuun. Yhteinen nopeus on $0{,}30\,\text{m/s}$. Liike-energia pienenee $0{,}072\,\text{J}$:sta $0{,}036\,\text{J}$:iin.

### Kimmoisa törmäys
Kimmoisassa törmäyksessä säilyy liikemäärä. Lisäksi säilyy kappaleiden yhteinen liike-energia:
```latex
\begin{aligned}
&E_{\text{k},1} + E_{\text{k},2} \\
&\quad = E_{\text{k},1}' + E_{\text{k},2}'
\end{aligned}
```
missä $E_\text{k} = \tfrac12 mv^2$ on kappaleen liike-energia ennen törmäystä ja $E_\text{k}'$ sen liike-energia törmäyksen jälkeen ($\text{J}$). Kun tunnetaan toisen kappaleen nopeus törmäyksen jälkeen, toinen nopeus saadaan liikemäärän säilymislaista. Vertaamalla liike-energioita nähdään, oliko törmäys kimmoisa. Ajatellaan, että kappale osuu suoraan samanmassaiseen kappaleeseen, joka on levossa, ja törmäys on kimmoisa. Silloin kappaleet vaihtavat nopeuksia.

<svg data-fig="tyypit" viewBox="0 0 600 434" role="img" aria-label="Kaavakuva, liikemäärät mittakaavassa. Kuvassa on kolme tapahtumaa kahdelle samanmassaiselle vaunulle. Vasemmalla on tilanne ennen ja oikealla jälkeen. Ylimpänä on kimmoisa törmäys. Ennen vaunulla 1 on liikemäärä oikealle ja vaunu 2 on levossa. Jälkeen vaunu 1 on levossa ja vaunulla 2 on sama liikemäärä. Liike-energia säilyy. Keskellä on täysin kimmoton törmäys. Vaunut tarttuvat yhteen, ja yhteinen liikemäärä on yhtä suuri kuin ennen. Liike-energia pienenee. Alimpana on räjähdys. Ennen vaunut ovat yhdessä levossa, ja kokonaisliikemäärä on nolla. Jälkeen vaunuilla on yhtä suuret liikemäärät vastakkaisiin suuntiin. Liike-energia kasvaa." class="fig-anim" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-10-tyypit.webp" x="0" y="0" width="600" height="438.8" preserveAspectRatio="none"/>
  <foreignObject x="90" y="45.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kimmoisa: } E_\text{k}\ \text{säilyy}$</div></foreignObject>
  <foreignObject x="90" y="175.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{täysin kimmoton: } E_\text{k}\ \text{pienenee}$</div></foreignObject>
  <foreignObject x="90" y="305.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{räjähdys: } E_\text{k}\ \text{kasvaa}$</div></foreignObject>
  <foreignObject x="113.5" y="349.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$p_\text{kok} = 0$</div></foreignObject>
  <foreignObject x="120" y="3.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{ennen}$</div></foreignObject>
  <foreignObject x="397.5" y="3.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{jälkeen}$</div></foreignObject>
</svg>

Joskus ulkoiset voimat vaikuttavat. Silloin liikemäärän säilymislakia käytetään vain itse törmäyksen tai räjähdyksen yli, lyhyen ajan alusta loppuun. Ennen törmäystä ja sen jälkeen ulkoiset voimat, kuten kitka tai paino, voivat muuttaa kappaleiden liikettä. Silloin liikettä tarkastellaan muilla laeilla, esimerkiksi energiaperiaatteella.

## Esimerkki
Ratapihalla tavaravaunu A, jonka massa on $32\,000\,\text{kg}$, liikkuu nopeudella $1{,}5\,\text{m/s}$. Se saavuttaa samaan suuntaan nopeudella $0{,}50\,\text{m/s}$ liikkuvan vaunun B, jonka massa on $18\,000\,\text{kg}$. Vaunut kytkeytyvät yhteen ja jatkavat yhdessä. Kuinka suuri on vaunujen yhteinen nopeus heti kytkeytymisen jälkeen?

<!-- vaihe -->

**Tunnetut ja kysytty.** $m_\text{A} = 32\,000\,\text{kg}$, $v_\text{A} = 1{,}5\,\text{m/s}$, $m_\text{B} = 18\,000\,\text{kg}$ ja $v_\text{B} = 0{,}50\,\text{m/s}$.

Kysytään vaunujen yhteistä nopeutta $v'$ heti sen jälkeen, kun ne ovat kytkeytyneet.

<!-- vaihe -->

**Periaate.** Valitaan systeemiksi molemmat vaunut. Positiivinen suunta on vaunujen liikkeen suunta. Kytkeytyminen kestää hetken. Sen aikana kytkinten voimat ovat sisäisiä voimia. Paino ja kiskojen tukivoima kumoavat toisensa. Vierimisvastuksen impulssi on lyhyen kytkeytymisen aikana niin pieni, ettei sillä ole merkitystä. Siksi kokonaisliikemäärä säilyy. Vaunut jäävät kiinni toisiinsa, joten törmäys on täysin kimmoton.

<!-- vaihe -->

**Kaava ratkaistuna.** Vaunujen liikemäärä ennen kytkeytymistä on yhtä suuri kuin yhteen kytkeytyneiden vaunujen liikemäärä sen jälkeen:
```latex
\begin{aligned}
&m_\text{A} v_\text{A} + m_\text{B} v_\text{B} \\
&\quad = (m_\text{A} + m_\text{B})\,v' \\[6pt]
&v' = \frac{m_\text{A} v_\text{A} + m_\text{B} v_\text{B}}{m_\text{A} + m_\text{B}}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Muunnoksia ei tarvita, koska massat ovat kilogrammoina ja nopeudet yksikössä $\text{m/s}$.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin liikemäärät ennen kytkeytymistä. Sitten lasketaan yhteinen nopeus:
```latex
\begin{aligned}
&m_\text{A} v_\text{A} \\
&= 32\,000\,\text{kg} \cdot 1{,}5\,\tfrac{\text{m}}{\text{s}} \\
&= 48\,000\,\text{kg}\cdot\tfrac{\text{m}}{\text{s}} \\[6pt]
&m_\text{B} v_\text{B} \\
&= 18\,000\,\text{kg} \cdot 0{,}50\,\tfrac{\text{m}}{\text{s}} \\
&= 9000\,\text{kg}\cdot\tfrac{\text{m}}{\text{s}} \\[6pt]
&v' \\
&= \frac{48\,000 + 9000}{50\,000} \cdot \frac{\text{kg}\cdot\text{m/s}}{\text{kg}} \\
&= 1{,}14\,\tfrac{\text{m}}{\text{s}}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Vaunujen yhteinen nopeus on $v' \approx 1{,}1\,\text{m/s}$. Vaunut liikkuvat samaan suuntaan kuin ennen. Tulos ilmoitetaan kahdella merkitsevällä numerolla, koska nopeuksissa $1{,}5\,\text{m/s}$ ja $0{,}50\,\text{m/s}$ on kaksi merkitsevää numeroa.

<!-- vaihe -->

**Järkevyys.** Yhteinen nopeus on vaunujen alkunopeuksien $0{,}50\,\text{m/s}$ ja $1{,}5\,\text{m/s}$ välissä. Se on lähempänä raskaamman vaunun A nopeutta, kuten pitääkin. Liike-energia pienenee $38{,}3\,\text{kJ}$:sta $32{,}5\,\text{kJ}$:iin eli noin $15\,\%$. Se sopii täysin kimmottomaan törmäykseen: liike-energiaa muuttuu kytkimien ja puskurien sisäenergiaksi ja ääneksi.

## Yleinen virhekäsitys
Moni ajattelee, että liike-energia säilyy törmäyksessä samalla tavalla kuin liikemäärä. Liikemäärä säilyy aina, kun ulkoisten voimien impulssi on niin pieni, ettei sillä ole merkitystä. Liike-energia säilyy vain kimmoisassa törmäyksessä. Jos yhteen tarttuvien vaunujen nopeus lasketaan liike-energian säilymisestä, tulos on liian suuri.

Toinen virhe on unohtaa etumerkit. Jos kappaleet liikkuvat toisiaan kohti, niiden liikemäärät ovat vastakkaissuuntaiset. Silloin toinen liikemääristä on negatiivinen. Kolmas virhe on ajatella, että liikemäärä katoaa, kun lattialle pudonnut savipallo pysähtyy. Pallon liikemäärä siirtyy Maahan. Pallo ja Maa muodostavat systeemin, ja sen kokonaisliikemäärä säilyy. Maan massa on kuitenkin niin suuri, ettei sen nopeuden muutosta huomaa.

## Tiivistelmä
- Systeemin kokonaisliikemäärä säilyy, kun ulkoisten voimien summa on nolla. Se säilyy myös, kun ulkoisten voimien impulssi on törmäyksen tai räjähdyksen aikana niin pieni, ettei sillä ole merkitystä: $\overline{p}_1 + \overline{p}_2 = \overline{p}_1' + \overline{p}_2'$.
- Säilyminen seuraa Newtonin kolmannesta laista. Törmäyksen sisäiset voimat ovat yhtä suuret ja vastakkaissuuntaiset, ja ne vaikuttavat saman ajan. Siksi kappaleiden liikemäärien muutokset kumoavat toisensa.
- Yhdessä ulottuvuudessa valitaan positiivinen suunta, ja nopeuksilla on etumerkit: $$\begin{aligned} &m_1 v_1 + m_2 v_2 \\ &= m_1 v_1' + m_2 v_2' \end{aligned}$$
- Kimmoisassa törmäyksessä myös liike-energia säilyy. Kimmottomassa törmäyksessä osa liike-energiasta muuttuu sisäenergiaksi. Täysin kimmottomassa törmäyksessä kappaleet jatkavat yhdessä yhteisellä nopeudella.
- Räjähdyksessä levossa olevan systeemin kokonaisliikemäärä pysyy nollana. Kun systeemi hajoaa kahdeksi osaksi, osat saavat yhtä suuret liikemäärät vastakkaisiin suuntiin. Liike-energia kasvaa.
