# Lenzin laki ja pyörrevirrat

> **Miksi** voimakas magneetti putoaa kupariputken läpi monta sekuntia? Kupari ei ole magneettista, ja tavallinen kappale putoaa saman matkan alle sekunnissa.

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratorion pöydällä on telineessä pystysuora kupariputki. Sen vieressä on läpinäkyvä muoviputki. Kupariputken alapäästä on juuri tulossa ulos pieni magneetti pehmeän alustan yläpuolella. Pöydällä on sekuntikello, joka näyttää, että on kulunut useita sekunteja." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-6-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Induktiovirta vastustaa muutosta
Luvussa *Sähkömagneettinen induktio* suljettuun johdinsilmukkaan syntyi induktiovirta. Se syntyi aina, kun silmukan läpi kulkeva magneettivuo muuttui. Magneettivuo kertoo, kuinka paljon magneettikenttää kulkee silmukan läpi.

Virran suunta noudattaa yhtä sääntöä. Sääntö on **Lenzin laki**: *induktiovirran suunta on aina sellainen, että sen oma magneettikenttä vastustaa sitä muutosta, joka induktiovirran synnyttää.*

Työnnä magneetin N-napa kohti kuparirengasta. Renkaan läpi kulkeva vuo kasvaa. Renkaassa kulkee induktiovirta, ja se tekee renkaasta pienen magneetin. Renkaan magneetin puoleinen sivu on N-napa. Samannimiset navat hylkivät toisiaan, joten rengas hylkii lähestyvää magneettia.

Vedä sitten magneetti pois. Nyt vuo pienenee. Virta kiertää toiseen suuntaan, ja renkaan magneetin puoleinen sivu on S-napa. Eri nimiset navat vetävät toisiaan puoleensa, joten rengas vetää magneettia takaisin. Kummassakin tapauksessa renkaan voima vastustaa magneetin liikettä.

<svg data-fig="ring" viewBox="0 0 600 360" role="img" aria-label="Kaksi periaatekuvaa, ei mittakaavassa. Kuparirengas on leikattu paperin tasossa, joten näkyvät renkaan ylä- ja alareunan poikkileikkaukset. Vasemmalla magneetti liikkuu N-napa edellä kohti rengasta. Renkaan induktiovirta kulkee yläreunassa paperiin päin ja alareunassa paperista ulos. Virran magneettikenttä osoittaa renkaan keskellä vasemmalle, kohti magneettia. Renkaan magneetin puoleinen sivu on siis N-napa, ja rengas hylkii magneettia. Voima magneettiin osoittaa vasemmalle, liikettä vastaan. Oikealla magneetti loittonee renkaasta. Virta kulkee vastakkaiseen suuntaan. Renkaan kenttä osoittaa oikealle, ja magneetin puoleinen sivu on S-napa. Rengas vetää magneettia takaisin. Voima osoittaa oikealle, taas liikettä vastaan." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-6-ring.webp" x="0" y="0" width="600" height="368.8" preserveAspectRatio="none"/>
  <foreignObject x="30" y="13.5" width="240" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{magneetti lähestyy}$</div></foreignObject>
  <foreignObject x="330" y="13.5" width="240" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{magneetti loittonee}$</div></foreignObject>
  <foreignObject x="44" y="167.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="100" y="167.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="240" y="71.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="145" y="197.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}_\text{ind}$</div></foreignObject>
  <foreignObject x="172" y="137.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="124" y="125.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="82" y="227.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="65" y="315.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{rengas hylkii}$</div></foreignObject>
  <foreignObject x="344" y="167.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="400" y="167.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="540" y="71.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="445" y="197.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}_\text{ind}$</div></foreignObject>
  <foreignObject x="472" y="137.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="414" y="125.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="343" y="227.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="365" y="315.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{rengas vetää}$</div></foreignObject>
</svg>

```pysahdy
Magneetin S-napaa työnnetään kohti kuparirengasta. Millainen on renkaan magneetin puoleinen sivu? Miksi?
---
Se on S-napa. Renkaan läpi menevä vuo kasvaa. Induktiovirran kenttä vastustaa kasvua. Siksi rengas työntää magneettia pois.
```

### Lenzin laki on energian säilymistä
Miksi induktiovirta ei voisi auttaa muutosta? Kuvitellaan, että se auttaisi. Silloin lähestyvä magneetti vetäisi rengasta puoleensa. Magneetti kiihtyisi kohti rengasta, ja vuo muuttuisi yhä nopeammin. Induktiovirta kasvaisi, ja veto voimistuisi.

Magneetin liike-energia ja renkaan sähköenergia kasvaisivat, vaikka kukaan ei tekisi työtä. Energiaa syntyisi tyhjästä. Tällainen kone olisi ikiliikkuja. Energian säilyminen kieltää sen.

Siksi magneettia täytyy liikuttaa voimalla, joka tekee työtä renkaan vastustavaa voimaa vastaan. Juuri tämä työ muuttuu induktiovirran sähköenergiaksi. Virta lämmittää johdinta, joten energia päätyy lopulta johtimen sisäenergiaksi.

### Pyörrevirrat
Induktiovirta ei tarvitse erillistä johdinsilmukkaa. Metallikappaleessa, esimerkiksi levyssä tai putken seinässä, virta voi kiertää suljettuna silmukkana. Kun magneettivuo muuttuu tällaisessa kappaleessa, metalliin syntyy suljettuja virtasilmukoita. Niitä sanotaan **pyörrevirroiksi**.

Magneetti putoaa kupariputkessa. Magneetin alapuolella putken seinän läpi kulkeva vuo kasvaa, ja yläpuolella vuo pienenee. Lenzin lain mukaan alapuolinen pyörrevirta hylkii magneettia ja yläpuolinen vetää sitä. Molemmat jarruttavat putoamista.

Pyörrevirrat ovat sitä suurempia, mitä nopeammin magneetti liikkuu. Siksi myös jarruttava voima kasvaa vauhdin mukana. Lopulta jarruttava voima on yhtä suuri kuin magneetin paino. Silloin voimien summa on nolla, ja magneetti putoaa tasaisella vauhdilla.

Muoviputkessa ei synny virtoja, koska muovi ei johda sähköä. Kupariputki ei jarruta myöskään magnetoimatonta teräskappaletta. Teräskappaleen liike ei muuta putken läpi kulkevaa vuota.

<svg data-fig="tube" viewBox="0 0 600 380" role="img" aria-label="Periaatekuva, ei mittakaavassa. Vasemmalla on pystysuora kupariputki leikattuna pituussuunnassa. Sen sisällä putoaa magneetti, jonka N-napa on alaspäin. Magneetin alapuolella putken seinässä kiertää pyörrevirta. Se kulkee oikeassa seinässä paperiin päin ja vasemmassa paperista ulos. Sen kenttä osoittaa ylöspäin, kohti magneettia. Magneetin yläpuolella pyörrevirta kiertää vastakkaiseen suuntaan, ja sen kenttä osoittaa alaspäin. Magneettiin vaikuttavat paino alaspäin ja yhtä pitkä jarruttava voima ylöspäin. Magneetin nopeus osoittaa alaspäin. Oikealla on alempi pyörrevirtarengas ylhäältä katsottuna. Virta kiertää vastapäivään. Kenttä osoittaa renkaan keskellä kohti katsojaa eli ylöspäin." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-6-tube.webp" x="0" y="0" width="600" height="388.8" preserveAspectRatio="none"/>
  <foreignObject x="140" y="156.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{S}$</div></foreignObject>
  <foreignObject x="140" y="194.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{N}$</div></foreignObject>
  <foreignObject x="70" y="257.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="70" y="93.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="12" y="287.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}_\text{ind}$</div></foreignObject>
  <foreignObject x="232" y="241.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{G}$</div></foreignObject>
  <foreignObject x="232" y="109.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\text{j}$</div></foreignObject>
  <foreignObject x="296" y="197.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="544" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I$</div></foreignObject>
  <foreignObject x="436" y="217.5" width="60" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}_\text{ind}$</div></foreignObject>
  <foreignObject x="341" y="31.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{alempi rengas ylhäältä}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy7/eddy-current-brake.webp" alt="Harmaa akseli ja iso pyöreä metallilevy. Levyn vieressä on jarrulaite, jossa on johtoja."><figcaption>Junan pyörrevirtajarru. Metallilevy pyörii akselin mukana. Levyn vieressä on sähkömagneetteja. Kun jarrutetaan, levyyn syntyy pyörrevirtoja. Ne vastustavat levyn pyörimistä. Liike-energia muuttuu levyn sisäenergiaksi.</figcaption></figure>

```pysahdy
Kupariputkessa putoavan magneetin vauhti kasvaa. Mitä tapahtuu jarruttavalle voimalle? Miksi?
---
Jarruttava voima kasvaa. Kun vauhti on suurempi, pyörrevirrat ovat suurempia. Isot pyörrevirrat jarruttavat enemmän.
```

### Pyörrevirtajarru, induktioliesi ja metallinilmaisin
**Induktiojarrussa** eli pyörrevirtajarrussa metallilevy tai kisko liikkuu magneettikentässä. Pyörrevirrat jarruttavat liikettä. Vuoristoradan vaunun alle kiinnitetyt kupari- tai alumiinilevyt kulkevat radan vahvojen magneettien välistä. Junissa jarrun sähkömagneetit ovat lähellä kiskoa.

Jarru ei kulu, koska mikään ei hankaa. Se jarruttaa sitä voimakkaammin, mitä suurempi vauhti on. Pysähtymisen lähellä vauhti on pieni ja jarrutus heikkenee. Siksi lopullinen pysäytys tarvitsee tavallisen jarrun.

Induktioliedessä lasin alla on kela, jossa kulkee vaihtovirta. Vaihtovirran suunta vaihtuu koko ajan, joten kelan magneettikenttä muuttuu kymmeniätuhansia kertoja sekunnissa. Pyörrevirrat lämmittävät kattilan pohjaa. Lasi ei johda sähköä, joten se lämpenee vain kuuman kattilan vaikutuksesta.

Metallinilmaisimen kela synnyttää vaihtuvan magneettikentän. Maassa olevaan metalliin syntyy pyörrevirtoja. Niiden oma kenttä havaitaan ilmaisimen kelassa.

### Kun pyörrevirroista on haittaa
Pyörrevirrat muuttavat sähköenergiaa aina sisäenergiaksi. Muuntajan ja sähkömoottorin rautasydämessä magneettikenttä vaihtelee jatkuvasti. Umpinaisessa sydämessä kiertäisi suuria pyörrevirtoja. Ne kuumentaisivat sydäntä ja hukkaisivat energiaa.

Siksi sydän kootaan ohuista levyistä. Levyjen välissä on eristekerros, joka ei johda sähköä. Pyörrevirrat voivat kiertää vain kunkin kapean levyn sisällä, joten ne jäävät pieniksi. Muuntajasta kerrotaan lisää luvussa *Muuntaja ja sähköenergian siirto*.

Sama ajatus näkyy kupariputkessa, johon on sahattu pitkittäinen rako. Rako katkaisee putken ympäri kiertävät virrat, ja magneetti putoaa paljon nopeammin. Jarrutus ei kuitenkaan katoa kokonaan, koska pienemmät pyörrevirrat kiertävät yhä raon vieressä olevassa seinässä.

<svg data-fig="core" viewBox="0 0 600 340" role="img" aria-label="Kaksi periaatekuvaa muuntajan rautasydämen poikkileikkauksesta, ei mittakaavassa. Vaihtuva magneettikenttä osoittaa sydämen pituussuunnassa paperiin päin. Sitä kuvaavat vihreät ristit. Vasemmalla on umpinainen rautasydän. Siinä kiertää yksi suuri pyörrevirtasilmukka koko poikkileikkauksen ympäri. Oikealla sydän on koottu ohuista levyistä, ja levyjen välissä on eristekerros. Pyörrevirrat kiertävät vain kunkin kapean levyn sisällä pieninä ja heikkoina silmukoina." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-6-core.webp" x="0" y="0" width="600" height="351.2" preserveAspectRatio="none"/>
  <foreignObject x="40" y="13.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{umpinainen sydän}$</div></foreignObject>
  <foreignObject x="325" y="13.5" width="250" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{levyistä koottu sydän}$</div></foreignObject>
  <foreignObject x="50" y="295.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{suuri pyörrevirta}$</div></foreignObject>
  <foreignObject x="355" y="295.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{eristetyt levyt}$</div></foreignObject>
  <foreignObject x="365" y="49.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\overline{B}\ \text{paperiin}$</div></foreignObject>
</svg>

## Kaava: Lenzin laki ja energia
Luvun *Sähkömagneettinen induktio* induktiolain miinusmerkki on Lenzin laki:
```kaavat
käämiin indusoituva jännite :: e_\text{ka} = -N \frac{\Delta \Phi}{\Delta t}
```
Kaavassa $e_\text{ka}$ on keskimääräinen induktiojännite (V) aikavälillä $\Delta t$, $N$ on silmukan kierrosten lukumäärä, $\Delta\Phi$ on magneettivuon muutos (Wb) ja $\Delta t$ on muutokseen kulunut aika (s). Kun vuo muuttuu tasaisesti, jännite on vakio. Silloin merkitään lyhyesti $e$. Miinusmerkki kertoo, että induktiovirran kenttä vastustaa vuon muutosta. Suuruus lasketaan ilman merkkiä. Suunta päätellään Lenzin laista.

Energian säilyminen kertoo, mihin putoavan magneetin energia menee. Kun magneetti putoaa korkeuden $h$, sen potentiaalienergia pienenee määrän $mgh$. Osa tästä energiasta muuttuu liike-energiaksi. Loput muuttuu pyörrevirtojen kautta putken sisäenergiaksi $Q$:
```latex
\begin{aligned}
&mgh = \tfrac{1}{2} m v^2 + Q \\
&Q = mgh - \tfrac{1}{2} m v^2
\end{aligned}
```
Kaavassa $m$ on magneetin massa (kg), $g = 9{,}81\,\text{m/s}^2$, $h$ on pudotuskorkeus (m), $v$ on vauhti lopussa (m/s) ja $Q$ on sisäenergiaksi muuttunut energia (J).

Kun magneetti putoaa tasaisella vauhdilla, jarruttava voima $F$ on yhtä suuri kuin paino $mg$. Ajassa $\Delta t$ magneetti liikkuu matkan $v \Delta t$. Jarruttava voima tekee tällä matkalla työn $F v \Delta t$. Siksi sisäenergia kasvaa teholla
```kaavat
hetkellinen teho :: P = F v
```
Kaavassa $P$ on teho (W), $F$ on jarruttava voima (N) ja $v$ on vauhti (m/s). Sama kaava pätee jokaiseen pyörrevirtajarruun. Jarruttava voima kertaa vauhti on teho, jolla liike-energia muuttuu sisäenergiaksi.

<svg data-fig="energy" viewBox="0 0 600 360" role="img" aria-label="Pylväskuvaaja mittakaavassa: energiat, kun 20 gramman magneetti on pudonnut metrin pituisen putken läpi. Muoviputkessa potentiaalienergian väheneminen, 196 millijoulea, on kokonaan muuttunut liike-energiaksi. Sisäenergiaa ei synny. Kupariputkessa potentiaalienergia vähenee yhtä paljon. Liike-energiaa on kuitenkin vain 0,2 millijoulea, niin vähän ettei pylvästä näy. Lähes kaikki, 196 millijoulea, on muuttunut putken sisäenergiaksi." style="max-width:100%;font-size:24px">
  <line x1="100" y1="227.5" x2="560" y2="227.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="175" x2="560" y2="175" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="122.5" x2="560" y2="122.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="100" y1="70" x2="560" y2="70" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="280" x2="574" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M586,280 L573,286 L573,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="100" y1="281" x2="100" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M100,44 L106,57 L94,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="93" y1="227.5" x2="100" y2="227.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="55" y="213" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$50$</div></foreignObject>
  <line x1="93" y1="175" x2="100" y2="175" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="160.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <line x1="93" y1="122.5" x2="100" y2="122.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="108" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$150$</div></foreignObject>
  <line x1="93" y1="70" x2="100" y2="70" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="43" y="55.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$200$</div></foreignObject>
  <foreignObject x="70" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="90" y="13.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E\ (\text{mJ})$</div></foreignObject>
  <rect x="139.5" y="74" width="46" height="206" fill="#6b7480"/>
  <foreignObject x="140" y="287.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta E_\text{p}$</div></foreignObject>
  <rect x="198.5" y="74" width="46" height="206" fill="#1971c2"/>
  <foreignObject x="205" y="287.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$E_\text{k}$</div></foreignObject>
  <foreignObject x="270.5" y="287.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$Q$</div></foreignObject>
  <foreignObject x="146.5" y="327.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{muoviputki}$</div></foreignObject>
  <rect x="363" y="74" width="46" height="206" fill="#6b7480"/>
  <foreignObject x="363.5" y="287.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta E_\text{p}$</div></foreignObject>
  <foreignObject x="428.5" y="287.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$E_\text{k}$</div></foreignObject>
  <rect x="481" y="74" width="46" height="206" fill="#e8590c"/>
  <foreignObject x="494" y="287.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$Q$</div></foreignObject>
  <foreignObject x="370" y="327.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kupariputki}$</div></foreignObject>
  <line x1="445" y1="276" x2="445" y2="217" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <foreignObject x="403.5" y="192" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$0{,}2\,\text{mJ}$</span></div></foreignObject>
</svg>

```pysahdy
Magneetin massa on $20\,\text{g}$. Se putoaa kupariputkessa tasaisella vauhdilla $0{,}30\,\text{m/s}$. Millä teholla putken sisäenergia kasvaa?
---
Jarruttava voima on yhtä suuri kuin paino: $F = mg = 0{,}020\,\text{kg}\cdot 9{,}81\,\text{m/s}^2 \approx 0{,}196\,\text{N}$. Teho on $P = Fv \approx 0{,}196\,\text{N}\cdot 0{,}30\,\text{m/s} \approx 0{,}059\,\text{W}$.
```

## Esimerkki
Opiskelija pudottaa $25\,\text{g}$:n neodyymimagneetin $1{,}20\,\text{m}$:n pituiseen pystysuoraan kupariputkeen. Hän mittaa, että magneetti tulee putken alapäästä ulos $8{,}0\,\text{s}$:n kuluttua. Magneetti putoaa lähes koko matkan tasaisella vauhdilla. Kuinka paljon putken sisäenergia kasvaa putoamisen aikana?

<!-- vaihe -->

**Tunnetut ja kysytty.** Magneetin massa $m = 25\,\text{g}$, putken pituus eli pudotuskorkeus $h = 1{,}20\,\text{m}$, putoamisaika $t = 8{,}0\,\text{s}$ ja $g = 9{,}81\,\text{m/s}^2$.

Kysytään, kuinka paljon putken sisäenergia kasvaa. Merkitään sitä $Q$.

<!-- vaihe -->

**Periaate.** Energia säilyy. Potentiaalienergia pienenee. Osa siitä jää magneetin liike-energiaksi, ja pyörrevirrat muuttavat loput putken sisäenergiaksi. Ilmanvastus on näin pienellä vauhdilla merkityksetön. Vauhti on lähes koko matkan sama, joten se saadaan matkasta ja ajasta.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&v = \frac{h}{t} \\
&Q = mgh - \tfrac{1}{2} m v^2
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Massa kilogrammoina: $m = 25\,\text{g} = 25 \cdot 0{,}001\,\text{kg} = 0{,}025\,\text{kg}$. Muut suureet ovat jo SI-yksiköissä.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin vauhti ja sitten energia.
```latex
\begin{aligned}
&v = \frac{h}{t} \\
&= \frac{1{,}20\,\text{m}}{8{,}0\,\text{s}} \\
&= 0{,}15\,\text{m/s} \\[6pt]
&Q = mgh - \tfrac{1}{2} m v^2 \\
&= 0{,}025\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \cdot 1{,}20\,\text{m} \\
&\quad - \tfrac{1}{2} \cdot 0{,}025\,\text{kg} \cdot (0{,}15\,\text{m/s})^2 \\
&= 0{,}29430\,\text{J} - 0{,}00028\,\text{J} \\
&= 0{,}29402\,\text{J}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Putken sisäenergia kasvaa noin $0{,}29\,\text{J}$. Tulos ilmoitetaan kahdella merkitsevällä numerolla, koska massa $25\,\text{g}$ ja aika $8{,}0\,\text{s}$ on annettu kahdella merkitsevällä numerolla.

<!-- vaihe -->

**Järkevyys.** Liike-energiaksi jää vain noin $0{,}1\,\%$ potentiaalienergian vähenemisestä. Lähes kaikki energia siis lämmittää putkea, kuten tasaisessa putoamisessa pitääkin. Oletetaan, että putken massa on $0{,}30\,\text{kg}$. Kuparin ominaislämpökapasiteetti on $385\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$, ja sen avulla lämpötilan nousuksi tulee vain noin $0{,}003\,\text{K}$. Siksi putki ei tunnu lämpenevän.

## Yleinen virhekäsitys
Moni ajattelee, että kupariputki hidastaa magneettia, koska magneetti tarttuu kupariin. Näin ei ole. Kupari ei ole ferromagneettinen aine, eli magneetti ei vedä sitä puoleensa. Levossa oleva magneetti ei tartu kupariputken seinään. Putki ei jarruta myöskään samanmuotoista magnetoimatonta teräskappaletta. Jarrutus syntyy vain liikkeestä, koska vain liikkuva magneetti muuttaa putken läpi kulkevaa vuota.

Toinen yleinen virhe on sanoa, että induktiovirran kenttä on aina magneetin kenttää vastaan. Lenzin laki ei vastusta kenttää vaan sen **muutosta**. Kun magneetti loittonee renkaasta, renkaan läpi kulkeva vuo pienenee. Induktiovirran kenttä osoittaa renkaan keskellä samaan suuntaan kuin magneetin kenttä. Silloin rengas vetää magneettia puoleensa.

## Tiivistelmä
- Lenzin laki: induktiovirran oma magneettikenttä vastustaa sitä muutosta, joka induktiovirran synnyttää. Rengas hylkii lähestyvää magneettia ja vetää loittonevaa.
- Lenzin laki seuraa energian säilymisestä. Työ, joka tehdään magneettia liikutettaessa, muuttuu induktiovirran sähköenergiaksi ja edelleen johtimen sisäenergiaksi: $Q = mgh - \tfrac{1}{2} m v^2$.
- Muuttuvassa magneettikentässä metallikappaleeseen syntyy pyörrevirtoja. Ne jarruttavat liikettä sitä voimakkaammin, mitä suurempi vauhti on. Jarrutuksen teho on $P = F v$.
- Pyörrevirtoja käytetään induktiojarrussa, induktioliedessä ja metallinilmaisimessa. Muuntajan ja moottorin rautasydän kootaan eristetyistä levyistä. Silloin pyörrevirrat ja niiden energiahäviö jäävät pieniksi.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: induktioliesi, jonka lasipinnalla on teräskattila. Kattilassa vesi kiehuu ja siitä nousee höyryä. Lasipinnan alla näkyy leikkauskuvana kuparinen kela. Liekkiä tai hehkuvaa levyä ei ole." style="max-width:100%;font-size:24px">
  <image href="pics/fy7/fy7-6-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
