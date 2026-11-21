# Liikemäärän säilyminen ja yksiulotteiset törmäykset

> **Miksi** biljardin lyöntipallo voi pysähtyä paikalleen, kun se osuu suoraan levossa olevaan palloon, ja toinen pallo jatkaa matkaa lähes samalla nopeudella?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: biljardipöytä läheltä nähtynä pöydän yllä roikkuvan lampun valossa. Vasemmalta alhaalta pöydälle osoittaa biljardikeppi, jolla valkoista lyöntipalloa on juuri lyöty. Lyöntipallo on osunut suoraan punaiseen palloon, ja hetki törmäyksen jälkeen se on pysähtynyt pöydän keskelle; sen takana näkyy haalea jälki kuljetusta matkasta. Punainen pallo kiitää eteenpäin kohti pöydän oikeaa reunaa, ja sen takana on liikeviivoja. Pöydän takaosassa on kolme muuta palloa." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-10-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Systeemi ja sen kokonaisliikemäärä
Luvussa *Liikemäärä ja impulssi* opit, että kappaleen liikemäärä on $\overline{p} = m\overline{v}$ ja että vakiosuuruisen kokonaisvoiman impulssi muuttaa sitä: $\Delta\overline{p} = \Sigma\overline{F}\,\Delta t$. Törmäyksessä on kuitenkin kaksi kappaletta, jotka vaikuttavat toisiinsa. Siksi tarkastellaan niitä yhdessä **systeeminä**. Systeemin **kokonaisliikemäärä** on sen kappaleiden liikemäärien vektorisumma, $\overline{p}_\text{kok} = \overline{p}_1 + \overline{p}_2$.

Systeemin kappaleiden toisiinsa kohdistamat voimat ovat **sisäisiä voimia**, esimerkiksi vaunujen puskurien voimat toisiinsa törmäyksessä. Systeemin ulkopuolelta tulevat voimat ovat **ulkoisia voimia**, esimerkiksi vaunujen paino, radan tukivoima ja kitka.

### Miksi kokonaisliikemäärä säilyy
Kun vaunu 1 työntää vaunua 2 voimalla $\overline{F}$, Newtonin kolmannen lain mukaan vaunu 2 työntää vaunua 1 yhtä suurella vastakkaissuuntaisella voimalla $-\overline{F}$. Voimat alkavat ja loppuvat samalla hetkellä, joten ne vaikuttavat saman ajan $\Delta t$. Jos voima on vakio, vaunun 2 liikemäärä muuttuu impulssin $\overline{F}\,\Delta t$ verran ja vaunun 1 liikemäärä yhtä paljon vastakkaiseen suuntaan. Se, minkä toinen vaunu saa liikemäärää, on täsmälleen se, minkä toinen menettää. Kokonaisliikemäärä ei muutu. Sama pätee, vaikka voima muuttuisi törmäyksen aikana, koska voimat ovat joka hetki yhtä suuret ja vastakkaissuuntaiset.

<svg data-fig="vuorovaikutus" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva, ei mittakaavassa: kaksi ilmatyynyradan vaunua törmäyksen aikana. Vaunujen väliin jäävä jousipuskuri on puristunut. Ylhäällä punaiset voimanuolet: vaunu 1 työntää vaunua 2 oikealle voimalla F, ja vaunu 2 työntää vaunua 1 vasemmalle yhtä suurella vastakkaissuuntaisella voimalla −F. Molemmat voimat vaikuttavat saman ajan Δt. Alhaalla violetit nuolet ovat liikemäärien muutokset: vaunun 1 muutos Δp1 = −FΔt osoittaa vasemmalle ja vaunun 2 muutos Δp2 = FΔt oikealle, yhtä pitkinä. Niiden summa on nolla." class="fig-anim" style="max-width:100%;font-size:24px">
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

Päättely toimii vain, kun ulkoiset voimat eivät muuta liikemäärää. Vaakasuoralla ilmatyynyradalla paino ja tukivoima kumoavat toisensa, ja kitka on hyvin pieni. Törmäävät autot taas kokevat tien kitkan, mutta törmäys kestää vain sekunnin murto-osan. Puskurien voimat ovat silloin paljon suurempia kuin kitka, joten kitkan impulssi jää törmäyksen aikana merkityksettömän pieneksi. Tästä saadaan **liikemäärän säilymislaki**: kun systeemiin vaikuttavien ulkoisten voimien summa on nolla tai niiden impulssi on törmäyksen aikana merkityksettömän pieni, systeemin kokonaisliikemäärä säilyy.

```pysahdy
Kahden auton törmäyksessä tien kitka vaikuttaa autoihin. Miksi kokonaisliikemäärää voi silti pitää säilyvänä?
---
Törmäys kestää vain sekunnin murto-osan, ja puskurien voimat ovat paljon suurempia kuin kitka. Kitkan impulssi jää silloin merkityksettömän pieneksi.
```

### Törmäysten lajit
Liikemäärä säilyy jokaisessa törmäyksessä, kun säilymislain ehto täyttyy. Liike-energia ei säily aina. Törmäys on **kimmoisa**, jos kappaleiden yhteinen liike-energia on törmäyksen jälkeen yhtä suuri kuin ennen sitä. Teräskuulat, biljardipallot ja jousipuskurilla varustetut vaunut törmäävät lähes kimmoisasti. Törmäys on **kimmoton**, jos osa liike-energiasta muuttuu muiksi energiamuodoiksi. Kappaleet muuttavat silloin muotoaan, ja liike-energiaa muuttuu niiden sisäenergiaksi ja ääneksi. Kun kappaleet jäävät kiinni toisiinsa ja jatkavat yhdessä, törmäys on **täysin kimmoton**, ja liike-energia pienenee eniten: suurin mahdollinen osa siitä muuttuu muiksi energiamuodoiksi.

<svg data-fig="tarra" viewBox="0 0 600 360" role="img" aria-label="Kaavakuva mittakaavassa: kaksi samanmassaista vaunua ilmatyynyradalla, ylhäällä ennen törmäystä ja alhaalla sen jälkeen. Ennen törmäystä vaunu 1 liikkuu oikealle nopeudella v, ja sen liikemäärä p on violetti nuoli; vaunu 2 on levossa. Vaunujen päissä on tarranauhat. Törmäyksen jälkeen vaunut ovat tarttuneet yhteen ja liikkuvat yhdessä puolella alkuperäisestä nopeudesta, sininen nuoli on puolet lyhyempi. Yhteisen liikemäärän violetti nuoli on yhtä pitkä kuin vaunun 1 liikemäärä ennen törmäystä." style="max-width:100%;font-size:24px">
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

Kuvassa samanmassaiset vaunut tarttuvat yhteen tarranauhalla. Kokonaisliikemäärä on sama ennen ja jälkeen, mutta nyt sama liikemäärä jakautuu kaksinkertaiselle massalle, joten yhteinen nopeus on puolet alkuperäisestä. Liike-energia $\tfrac12 mv^2$ ei säily: kaksinkertainen massa ja puolet nopeudesta antavat puolet alkuperäisestä liike-energiasta. Toinen puoli muuttuu tarranauhan ja vaunujen sisäenergiaksi.

```pysahdy
Kimmoton törmäys: vaunut tarttuvat yhteen. Mihin liike-energia, joka "katoaa", joutuu?
---
Se ei katoa vaan muuttuu tarranauhan ja vaunujen sisäenergiaksi. Kokonaisenergia säilyy, vaikka liike-energia pienenee.
```

### Räjähdys
**Räjähdyksessä** levossa oleva tai yhdessä liikkuva systeemi hajoaa osiin sisäisten voimien vaikutuksesta: jousi laukeaa vaunujen välissä, luistelijat työntävät toisiaan tai ruuti työntää luotia ja kivääriä. Jos systeemi on aluksi levossa, sen kokonaisliikemäärä on nolla ja pysyy nollana. Kun levossa oleva systeemi hajoaa kahdeksi osaksi, osat saavat yhtä suuret ja vastakkaissuuntaiset liikemäärät, ja kevyempi osa saa suuremman nopeuden. Siksi kivääri potkaisee taaksepäin, kun luoti lähtee eteenpäin. Jos osia on useampia, niiden liikemäärien vektorisumma on nolla, mutta yksittäisten osien liikemäärät voivat olla erisuuruisia. Liike-energia kasvaa räjähdyksessä, koska jousen, lihasten tai ruudin energiaa muuttuu liike-energiaksi.

```pysahdy
Luistelija seisoo levossa jäällä ja heittää raskaan pallon eteenpäin. Miksi hän liukuu itse taaksepäin?
---
Pallo saa eteenpäin suuntautuvan liikemäärän, ja systeemin kokonaisliikemäärä pysyy nollana. Siksi luistelija saa yhtä suuren liikemäärän taaksepäin.
```

### Vastaus alun kysymykseen
Biljardipallot ovat yhtä raskaita, ja niiden törmäys on lähes kimmoisa. Kun lyöntipallon nopeus on $v$, liikemäärän säilymisestä seuraa, että pallojen nopeuksien summa pysyy samana: $v_1' + v_2' = v$. Liike-energian säilymisestä seuraa, että nopeuksien neliöiden summa pysyy samana: $v_1'^2 + v_2'^2 = v^2$. Korottamalla ensimmäinen ehto toiseen potenssiin ja vähentämällä toinen ehto saadaan $2 v_1' v_2' = 0$, joten toinen palloista on törmäyksen jälkeen levossa. Lyöntipallo ei voi kulkea toisen läpi, joten se pysähtyy, ja toinen pallo jatkaa nopeudella $v$. Todellisuudessa pallot myös pyörivät ja törmäys ei ole täysin kimmoisa, joten lyöntipallo voi jäädä hiukan liikkeeseen.

<figure class="unit-photo"><img src="pics/fy4/newtons-cradle.webp" alt="Newtonin kehto: rivi riippuvia teräskuulia, joista vasemmanpuoleinen on liikkeessä ja siksi epäterävä."><figcaption>Newtonin kehdossa vasemmalta heilahtava kuula osuu paikallaan oleviin kuuliin. Liikkuva kuula näkyy kuvassa epäterävänä.</figcaption></figure>

## Kaava: Liikemäärän säilymislaki

### Säilymislaki vektoreina ja yhdessä ulottuvuudessa
Kun systeemiin vaikuttavien ulkoisten voimien summa on nolla tai niiden impulssi on törmäyksen tai räjähdyksen aikana merkityksettömän pieni, kokonaisliikemäärä on sama ennen ja jälkeen:
```latex
\overline{p}_1 + \overline{p}_2 = \overline{p}_1' + \overline{p}_2'
```
missä $\overline{p}_1$ ja $\overline{p}_2$ ovat kappaleiden liikemäärät ennen ja $\overline{p}_1'$ ja $\overline{p}_2'$ niiden liikemäärät jälkeen ($\text{kg}\cdot\text{m/s}$).

Yksiulotteisessa törmäyksessä kaikki nopeudet ovat samalla suoralla. Valitaan positiivinen suunta, jolloin jokainen nopeus on etumerkillinen luku: vastakkaiseen suuntaan liikkuvan kappaleen nopeus on negatiivinen. Säilymislaki tulee muotoon
```latex
\begin{aligned}
&m_1 v_1 + m_2 v_2 \\
&\quad = m_1 v_1' + m_2 v_2'
\end{aligned}
```
missä $m_1$ ja $m_2$ ovat kappaleiden massat ($\text{kg}$), $v_1$ ja $v_2$ niiden nopeudet ennen ja $v_1'$ ja $v_2'$ nopeudet jälkeen ($\text{m/s}$).

### Täysin kimmoton törmäys
Kun kappaleet jäävät kiinni toisiinsa, niillä on törmäyksen jälkeen yhteinen nopeus $v'$:
```latex
\begin{aligned}
&m_1 v_1 + m_2 v_2 \\
&\quad = (m_1 + m_2)\,v'
\end{aligned}
```
missä $v'$ on kappaleiden yhteinen nopeus törmäyksen jälkeen ($\text{m/s}$). Esimerkiksi kun $0{,}40\,\text{kg}$:n vaunu nopeudella $0{,}60\,\text{m/s}$ tarttuu levossa olevaan samanlaiseen vaunuun, yhteinen nopeus on $0{,}30\,\text{m/s}$, ja liike-energia pienenee $0{,}072\,\text{J}$:sta $0{,}036\,\text{J}$:iin.

### Kimmoisa törmäys
Kimmoisassa törmäyksessä säilyy liikemäärän lisäksi kappaleiden yhteinen liike-energia:
```latex
\begin{aligned}
&E_{\text{k},1} + E_{\text{k},2} \\
&\quad = E_{\text{k},1}' + E_{\text{k},2}'
\end{aligned}
```
missä $E_\text{k} = \tfrac12 mv^2$ on kunkin kappaleen liike-energia ennen ja $E_\text{k}'$ jälkeen ($\text{J}$). Kun tunnetaan toisen kappaleen nopeus törmäyksen jälkeen, toinen saadaan liikemäärän säilymislaista, ja liike-energioita vertaamalla nähdään, oliko törmäys kimmoisa. Kun samanmassainen kappale osuu suoraan levossa olevaan kappaleeseen kimmoisasti, kappaleet vaihtavat nopeuksia.

<svg data-fig="tyypit" viewBox="0 0 600 434" role="img" aria-label="Kaavakuva, liikemäärät mittakaavassa: kolme tapahtumaa kahdelle samanmassaiselle vaunulle, vasemmalla ennen ja oikealla jälkeen. Ylimpänä kimmoisa törmäys: ennen vaunulla 1 on liikemäärä oikealle ja vaunu 2 on levossa, jälkeen vaunu 1 on levossa ja vaunulla 2 on sama liikemäärä; liike-energia säilyy. Keskellä täysin kimmoton törmäys: vaunut tarttuvat yhteen, ja yhteinen liikemäärä on yhtä suuri kuin ennen; liike-energia pienenee. Alimpana räjähdys: ennen vaunut ovat yhdessä levossa ja kokonaisliikemäärä on nolla, jälkeen vaunuilla on yhtä suuret vastakkaissuuntaiset liikemäärät; liike-energia kasvaa." class="fig-anim" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-10-tyypit.webp" x="0" y="0" width="600" height="438.8" preserveAspectRatio="none"/>
  <foreignObject x="90" y="45.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kimmoisa: } E_\text{k}\ \text{säilyy}$</div></foreignObject>
  <foreignObject x="90" y="175.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{täysin kimmoton: } E_\text{k}\ \text{pienenee}$</div></foreignObject>
  <foreignObject x="90" y="305.5" width="420" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{räjähdys: } E_\text{k}\ \text{kasvaa}$</div></foreignObject>
  <foreignObject x="113.5" y="349.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$p_\text{kok} = 0$</div></foreignObject>
  <foreignObject x="120" y="3.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{ennen}$</div></foreignObject>
  <foreignObject x="397.5" y="3.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{jälkeen}$</div></foreignObject>
</svg>

Kun ulkoiset voimat vaikuttavat, liikemäärän säilymislakia käytetään vain itse törmäyksen tai räjähdyksen yli, lyhyen ajan alusta loppuun. Ennen ja jälkeen ulkoiset voimat, kuten kitka tai paino, voivat muuttaa kappaleiden liikettä, ja silloin liikettä tarkastellaan muilla laeilla, esimerkiksi energiaperiaatteella.

## Esimerkki
Ratapihalla tavaravaunu A, jonka massa on $32\,000\,\text{kg}$, liikkuu nopeudella $1{,}5\,\text{m/s}$ ja saavuttaa samaan suuntaan nopeudella $0{,}50\,\text{m/s}$ liikkuvan vaunun B, jonka massa on $18\,000\,\text{kg}$. Vaunut kytkeytyvät yhteen ja jatkavat yhdessä. Kuinka suuri on vaunujen yhteinen nopeus heti kytkeytymisen jälkeen?

<!-- vaihe -->

**Tunnetut ja kysytty.** $m_\text{A} = 32\,000\,\text{kg}$, $v_\text{A} = 1{,}5\,\text{m/s}$, $m_\text{B} = 18\,000\,\text{kg}$ ja $v_\text{B} = 0{,}50\,\text{m/s}$.

Kysytään yhteistä nopeutta $v'$ heti kytkeytymisen jälkeen.

<!-- vaihe -->

**Periaate.** Valitaan systeemiksi molemmat vaunut ja positiiviseksi suunnaksi vaunujen liikkeen suunta. Kytkeytyminen kestää hetken, ja sen aikana kytkinten voimat ovat sisäisiä voimia. Paino ja kiskojen tukivoima kumoavat toisensa, ja vierimisvastuksen impulssi on lyhyen kytkeytymisen aikana merkityksettömän pieni, joten kokonaisliikemäärä säilyy. Vaunut jäävät kiinni toisiinsa, joten törmäys on täysin kimmoton.

<!-- vaihe -->

**Kaava ratkaistuna.** Liikemäärä ennen on yhtä suuri kuin yhteisen kappaleen liikemäärä jälkeen:
```latex
\begin{aligned}
&m_\text{A} v_\text{A} + m_\text{B} v_\text{B} \\
&\quad = (m_\text{A} + m_\text{B})\,v' \\[6pt]
&v' = \frac{m_\text{A} v_\text{A} + m_\text{B} v_\text{B}}{m_\text{A} + m_\text{B}}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: massat ovat kilogrammoina ja nopeudet yksikössä $\text{m/s}$.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin liikemäärät ennen kytkeytymistä ja sitten yhteinen nopeus:
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

**Tulos.** Vaunujen yhteinen nopeus on $v' \approx 1{,}1\,\text{m/s}$ vaunujen alkuperäiseen liikesuuntaan. Tulos ilmoitetaan kahdella merkitsevällä numerolla kuten nopeudet $1{,}5\,\text{m/s}$ ja $0{,}50\,\text{m/s}$.

<!-- vaihe -->

**Järkevyys.** Yhteinen nopeus on vaunujen alkunopeuksien $0{,}50\,\text{m/s}$ ja $1{,}5\,\text{m/s}$ välissä ja lähempänä raskaamman vaunun A nopeutta, kuten pitää. Liike-energia pienenee $38{,}3\,\text{kJ}$:sta $32{,}5\,\text{kJ}$:iin eli noin $15\,\%$, mikä sopii täysin kimmottomaan törmäykseen: liike-energiaa muuttuu kytkimien ja puskurien sisäenergiaksi ja ääneksi.

## Yleinen virhekäsitys
Moni ajattelee, että liike-energia säilyy törmäyksessä samalla tavalla kuin liikemäärä. Liikemäärä säilyy aina, kun ulkoisten voimien impulssi on merkityksettömän pieni, mutta liike-energia säilyy vain kimmoisassa törmäyksessä. Jos yhteen tarttuvien vaunujen nopeus lasketaan liike-energian säilymisestä, tulos on liian suuri.

Toinen virhe on unohtaa etumerkit. Kun kappaleet liikkuvat toisiaan kohti, niiden liikemäärät ovat vastakkaissuuntaiset, ja toinen niistä on negatiivinen. Kolmas virhe on ajatella, että liikemäärä katoaa, kun lattialle pudonnut savipallo pysähtyy. Pallon liikemäärä siirtyy Maahan: pallo ja Maa muodostavat systeemin, jonka kokonaisliikemäärä säilyy, mutta Maan massa on niin suuri, ettei sen nopeuden muutosta huomaa.

## Tiivistelmä
- Systeemin kokonaisliikemäärä säilyy, kun ulkoisten voimien summa on nolla tai niiden impulssi on törmäyksen tai räjähdyksen aikana merkityksettömän pieni: $\overline{p}_1 + \overline{p}_2 = \overline{p}_1' + \overline{p}_2'$.
- Säilyminen seuraa Newtonin kolmannesta laista: törmäyksen sisäiset voimat ovat yhtä suuret ja vastakkaissuuntaiset ja vaikuttavat saman ajan, joten kappaleiden liikemäärien muutokset kumoavat toisensa.
- Yhdessä ulottuvuudessa valitaan positiivinen suunta, ja nopeudet ovat etumerkillisiä: $$\begin{aligned} &m_1 v_1 + m_2 v_2 \\ &= m_1 v_1' + m_2 v_2' \end{aligned}$$
- Kimmoisassa törmäyksessä myös liike-energia säilyy. Kimmottomassa törmäyksessä osa liike-energiasta muuttuu sisäenergiaksi, ja täysin kimmottomassa kappaleet jatkavat yhdessä yhteisellä nopeudella.
- Räjähdyksessä levossa olevan systeemin kokonaisliikemäärä pysyy nollana: kahdeksi osaksi hajotessa osat saavat yhtä suuret vastakkaissuuntaiset liikemäärät, ja liike-energia kasvaa.
