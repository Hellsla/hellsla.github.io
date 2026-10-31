Työselostuksen lukija näkee mittauksesi vain taulukoista, kuvaajista ja tuloksesta. Tässä ohjeessa kokoat ne niin, että toinen voi tarkistaa työsi ja ymmärtää, miten tulokseen päädyit.

## Mihin tarvitset tätä

Kaikista FY10:n tutkimuksista kirjoitetaan työselostus työselostuspohjalla. Esimerkiksi tutkimuksissa *Jousivakion määrittäminen* ja *Putoamiskiihtyvyyden määrittäminen heilurin avulla* selostuksen ydin on kuvaaja, josta tulos saadaan kulmakertoimena. Tässä ohjeessa käsitellään pohjan osat Mittaustulokset, Tulosten käsittely ja graafinen analyysi sekä Tulos.

## Työvaiheet

1. **Kokoa mittaustaulukko osaan Mittaustulokset.** Jokaisen sarakkeen otsikossa on suure ja yksikkö, esimerkiksi $l\ (\text{m})$. Alkuperäiset mittaukset ovat vasemmalla, ja niistä johdetut suureet, kuten $T^2\ (\text{s}^2)$, ovat omissa sarakkeissaan oikealla. Numeroi taulukko ja kirjoita sen yläpuolelle otsikko, esimerkiksi "Taulukko 1. Heilurin pituus ja jaksonaika".

2. **Ilmoita lukuarvot johdonmukaisesti.** Kirjoita saman sarakkeen luvut samalla tarkkuudella, joka vastaa mittauksen tarkkuutta. Jos luit pituuden millimetrin tarkkuudella, kirjoita $0{,}450\,\text{m}$ eikä $0{,}45\,\text{m}$. Johdettuihin suureisiin voit jättää yhden numeron enemmän kuin lopputulokseen ja pyöristää vasta lopussa.

3. **Tee kuvaaja osaan Tulosten käsittely ja graafinen analyysi.** Piirrä kuvaaja ja sovita suora Graphical Analysis Prossa ([[ohje:tvt-kuvaaja|Mittauspisteiden kuvaaja]], [[ohje:tvt-suoran-sovitus|Suoran sovittaminen mittauspisteisiin]]). Tarkista ennen vientiä, että kuvaajassa ovat otsikko, akselien suureet ja yksiköt, mittauspisteet, tarvittaessa epävarmuusjanat sekä sovitettu suora ja sen tulosruutu. Vie kuvaaja kuvaksi ohjelman vientitoiminnolla (englanninkielisessä versiossa **Export graph as png**) ja liitä kuva selostukseen.

4. **Kirjoita suoran yhtälö suureilla ja yksiköillä.** Sovituksen tulosruudun yhtälö y = mx + b ei kerro suureita, ja ohjelma kirjoittaa kertoimet desimaalipisteellä. Ohjelman m on kulmakerroin ja b vakiotermi. Jos keksityillä esimerkkiarvoilla tulosruudussa on m: 4.05 ja b: 0.02, eli $y = 4{,}05x + 0{,}02$, kirjoita yhtälö muotoon $T^2 = 4{,}05\,\text{s}^2/\text{m} \cdot l + 0{,}02\,\text{s}^2$, desimaalipilkuin.

5. **Lisää kuvateksti ja viittaa kuvaan.** Numeroi kuva ja kirjoita sen alle kuvateksti, esimerkiksi "Kuva 1. Heilurin jaksonajan neliö pituuden funktiona ja mittauspisteisiin sovitettu suora." Viittaa kuvaan tekstissä: "Kuvasta 1 nähdään, että pisteet asettuvat suoralle, joka kulkee lähes origon kautta." Lukijan ei pidä joutua arvaamaan, miksi kuva on mukana.

6. **Näytä mallilasku.** Kirjoita, miten tulos saadaan kulmakertoimesta, ensin kirjaimin ja sitten lukuarvoin yksiköineen, esimerkiksi $g = \tfrac{4\pi^2}{k}$. Jos laskit saman kaavan monelle riville, näytä yksi rivi esimerkkinä.

7. **Ilmoita tulos osassa Tulos.** Kirjoita päätulos epävarmuuksineen ja yksikköineen, esimerkiksi $g = (9{,}7 \pm 0{,}4)\,\text{m/s}^2$, ja vertaa sitä vertailuarvoon ([[ohje:tvt-epavarmuus|Kulmakertoimen epävarmuus]]).

    Kuvassa on työselostuksen sivu, jossa nämä kolme osaa ovat peräkkäin. Harmaat palkit ovat omaa tekstiäsi ja omia lukujasi.

    <svg data-fig="page" viewBox="0 0 600 730" role="img" aria-label="Kaaviokuva työselostuksen sivusta ilman lukuarvoja; harmaat palkit ovat oppilaan omaa tekstiä ja lukuja. Osassa 4, Mittaustulokset, on taulukko 1, jonka sarakkeiden otsikoissa on suure ja yksikkö: l metreinä, T sekunteina ja T toiseen sekunnin neliöinä. Osassa 5, Tulosten käsittely ja graafinen analyysi, on kuvaaja, jonka akseleilla on suureet ja yksiköt, mittauspisteet ja sovitettu suora, jonka yhtälö T toiseen on k kertaa l on kirjoitettu kuvaajan viereen. Kuvaajan alla on kuvateksti Kuva 1 ja sen alla tekstissä viittaus: Kuvasta 1 nähdään, että. Osassa 6, Tulos, on tulos muodossa g on sulkeissa lukuarvo plus miinus epävarmuus, molemmat harmaina palkkeina, ja yksikkö metriä per sekunti toiseen." style="max-width:100%;font-size:24px">
  <rect x="36" y="18" width="528" height="694" rx="6" fill="#fdfcf8" stroke="#c9c2b2" stroke-width="2"/>
  <foreignObject x="66" y="41.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$4$</div></foreignObject>
  <foreignObject x="96" y="41.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Mittaustulokset}$</div></foreignObject>
  <foreignObject x="66" y="81.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{Taulukko 1.}$</div></foreignObject>
  <rect x="210" y="92" width="230" height="8" rx="4" fill="#e3dccb"/>
  <rect x="66" y="116" width="450" height="36" fill="#e3dccb"/>
  <line x1="66" y1="116" x2="516" y2="116" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="66" y1="152" x2="516" y2="152" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="66" y1="188" x2="516" y2="188" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="66" y1="224" x2="516" y2="224" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="66" y1="116" x2="66" y2="224" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="216" y1="116" x2="216" y2="224" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="366" y1="116" x2="366" y2="224" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="516" y1="116" x2="516" y2="224" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="110" y="119.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$l\ (\text{m})$</div></foreignObject>
  <foreignObject x="260" y="119.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T\ (\text{s})$</div></foreignObject>
  <foreignObject x="397.5" y="119.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$T^2\ (\text{s}^2)$</div></foreignObject>
  <rect x="136" y="166" width="66" height="8" rx="4" fill="#e3dccb"/>
  <rect x="286" y="166" width="66" height="8" rx="4" fill="#e3dccb"/>
  <rect x="436" y="166" width="66" height="8" rx="4" fill="#e3dccb"/>
  <rect x="136" y="202" width="66" height="8" rx="4" fill="#e3dccb"/>
  <rect x="286" y="202" width="66" height="8" rx="4" fill="#e3dccb"/>
  <rect x="436" y="202" width="66" height="8" rx="4" fill="#e3dccb"/>
  <foreignObject x="66" y="249.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$5$</div></foreignObject>
  <foreignObject x="96" y="249.5" width="245" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Tulosten käsittely ja}$</div></foreignObject>
  <foreignObject x="96" y="283.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{graafinen analyysi}$</div></foreignObject>
  <line x1="109" y1="506" x2="344" y2="506" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M356,506 L343,512 L343,500 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="110" y1="507" x2="110" y2="366" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M110,354 L116,367 L104,367 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="362" y="491.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$l\ (\text{m})$</div></foreignObject>
  <foreignObject x="100" y="323.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T^2\ (\text{s}^2)$</div></foreignObject>
  <polyline points="110,506 319,386.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="143" cy="484" r="5.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="176" cy="470.5" r="5.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="209" cy="446" r="5.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="242" cy="432.5" r="5.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="275" cy="409.5" r="5.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="308" cy="394.5" r="5.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="372" y="403.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T^2 = k \cdot l$</div></foreignObject>
  <foreignObject x="66" y="531.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{Kuva 1.}$</div></foreignObject>
  <rect x="166" y="542" width="274" height="8" rx="4" fill="#e3dccb"/>
  <foreignObject x="66" y="567.5" width="258" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{Kuvasta 1 nähdään, että}$</div></foreignObject>
  <rect x="380" y="578" width="120" height="8" rx="4" fill="#e3dccb"/>
  <foreignObject x="66" y="615.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$6$</div></foreignObject>
  <foreignObject x="96" y="615.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Tulos}$</div></foreignObject>
  <foreignObject x="96" y="659.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$g = ($</div></foreignObject>
  <rect x="150" y="670" width="76" height="8" rx="4" fill="#e3dccb"/>
  <foreignObject x="234" y="659.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\pm$</div></foreignObject>
  <rect x="262" y="670" width="56" height="8" rx="4" fill="#e3dccb"/>
  <foreignObject x="326" y="659.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$)\,\text{m/s}^2$</div></foreignObject>
</svg>

8. **Tarkista, että kuva on luettava.** Kuvatiedosto on yleensä siistimpi kuin kuvakaappaus, koska siinä ei ole valikoita. Tarkista, että akselien tekstit ja luvut erottuvat selostuksessa, ja lisää puuttuvat akselien otsikot ja yksiköt ohjelmassa ennen vientiä. Mittaustaulukon voit kirjoittaa selostukseen taulukkona kopioimalla arvot ohjelman taulukosta, ja koko datan voit liittää CSV-tiedostona (englanninkielisessä versiossa **Export data as csv**).

## Tavallisimmat virheet

- **Taulukossa on vain lasketut suureet.** Lukija ei voi tarkistaa laskujasi. Pidä alkuperäiset mittaukset mukana omissa sarakkeissaan.
- **Saman sarakkeen luvut on kirjoitettu eri tarkkuudella**, esimerkiksi $0{,}45$, $0{,}453$ ja $0{,}5$. Kirjoita kaikki luvut mittauksen tarkkuudella.
- **Kuvaa ei mainita tekstissä.** Lukija ei tiedä, mitä kuvasta pitäisi nähdä. Kirjoita johtopäätös näkyviin ja viittaa kuvan numeroon.
- **Suoran yhtälössä on $x$ ja $y$ ilman yksiköitä.** Yhtälöstä ei näe, mikä luku on mikin suure. Kirjoita yhtälö suureilla ja yksiköillä.
- **Tuloksesta puuttuu epävarmuus tai yksikkö.** Pelkkä luku ei ole mittaustulos. Ilmoita tulos muodossa (arvo $\pm$ epävarmuus) yksikkö.
- **Kuva on lukukelvoton.** Teksti on liian pientä tai kuvaaja vaalea. Suurenna kuvaaja ohjelmassa ennen vientiä ja vie se kuvatiedostona kuvakaappauksen sijaan.

## Tarkista ennen kuin jatkat

- Taulukossa ovat alkuperäiset mittaukset ja johdetut suureet, ja jokaisen sarakkeen otsikossa on suure ja yksikkö.
- Kuvaajalla on numero ja kuvateksti, ja tekstissä viitataan siihen.
- Suoran yhtälö on kirjoitettu suureilla ja yksiköillä.
- Tulos on ilmoitettu epävarmuuksineen ja yksikköineen.
