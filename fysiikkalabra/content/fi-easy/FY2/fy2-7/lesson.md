# Energian siirtäminen: sähkö ja lämpö

> **Miksi** voimalinjojen jännite on satoja kilovoltteja, vaikka pistorasiasta saa vain $230\,\text{V}$? Miksi kaukolämpöputket kääritään paksuun eristeeseen?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: maisemassa on korkeita voimalinjan pylväitä. Niiden johdot kulkevat kauas. Etualalla näkyy maan sisään: maan alla on kaukolämpöputket. Putkien ympärillä on paksu eristekerros. Putket vievät lämpöä talolle." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-7-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

Energiaa tuotetaan usein kaukana siitä, missä sitä käytetään. Voimalaitos on kaupungin ulkopuolella, mutta lämmitin ja pistorasia ovat kotona. Siksi energia täytyy siirtää käyttäjälle. Energiaa voi siirtää paikasta toiseen monella tavalla. Tässä luvussa tutkitaan kahta tapaa, jotka ovat tärkeitä yhteiskunnan energiaverkoille. Sähköverkossa siirtyy **sähköenergiaa**. Kaukolämpöverkon vesiputkissa siirtyy **lämpöenergiaa**.

### Sähköverkko

**Sähköverkko** vie sähköenergian voimalaitokselta kotiin. Pitkät matkat kulkevat kantaverkon voimalinjoissa. Niiden jännite on $110\text{–}400\,\text{kV}$. Lähempänä käyttäjää jännite lasketaan ensin arvoon $20\,\text{kV}$. Lopuksi se lasketaan pienjänniteverkon arvoon $0{,}4\,\text{kV}$. Siitä kodin pistorasiat saavat $230\,\text{V}$. Jännitettä muutetaan muuntajissa.

<svg data-fig="grid" viewBox="0 0 600 332" role="img" aria-label="Kaavakuva siitä, miten sähkö kulkee voimalaitokselta kotiin. Vasemmalta oikealle: voimalaitos ja sen muuntaja, kantaverkon voimalinja (jännite 110 kV:sta 400 kV:iin), sähköasema, jakeluverkon pylväät (20 kV) ja koti (0,4 kV, pistorasiassa 230 V). Alla oranssi nuoli näyttää, miten energia kulkee voimalaitokselta kotiin. Kuva ei ole mittakaavassa." style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-7-grid.webp" x="0" y="-1.2" width="600" height="338.8" preserveAspectRatio="none"/>
  <foreignObject x="160" y="47.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$110\text{–}400\,\text{kV}$</div></foreignObject>
  <foreignObject x="426" y="101.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$20\,\text{kV}$</div></foreignObject>
  <foreignObject x="506" y="47.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$0{,}4\,\text{kV}$</div></foreignObject>
  <foreignObject x="85" y="86" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{muuntaja}$</div></foreignObject>
  <foreignObject x="18" y="247.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{voimalaitos}$</div></foreignObject>
  <foreignObject x="175" y="247.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kantaverkko}$</div></foreignObject>
  <foreignObject x="325" y="281.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sähköasema}$</div></foreignObject>
  <foreignObject x="450" y="247.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{jakeluverkko}$</div></foreignObject>
</svg>

### Miksi pitkä matka siirretään korkealla jännitteellä

Saman tehon voi siirtää kahdella tavalla. Voi käyttää pientä jännitettä ja suurta sähkövirtaa. Voi myös käyttää suurta jännitettä ja pientä sähkövirtaa. Mitä suurempi virta johtimessa kulkee, sitä enemmän johdin lämpenee. Lämmitykseen menevä energia on häviötä. Siksi pitkä matka siirretään suurella jännitteellä. Silloin virta ja häviö jäävät pieniksi. Jännitteen, virran ja häviön tarkka yhteys kuuluu myöhempiin sähkökursseihin.

Muuntaja nostaa jännitteen voimalaitoksella. Se laskee jännitteen takaisin käyttäjän lähellä. Hyvässä muuntajassa häviö on hyvin pieni.

```pysahdy
Kaksi voimalinjaa siirtää saman tehon. Toisessa jännite on suuri ja toisessa pieni. Kummassa linjassa johtimet lämpenevät enemmän?
---
Pienemmän jännitteen linjassa. Siellä virta on suurempi. Suuri virta lämmittää johdinta enemmän.
```

<figure class="unit-photo"><img src="pics/fy2/muurame-transformer.webp" alt="Iso muuntaja sähköasemalla aidan takana."><figcaption>Sähköaseman muuntaja Muuramessa. Muuntaja laskee voimajohdon korkean jännitteen pienemmäksi.</figcaption></figure>

### Kaukolämpö

**Kaukolämpö** siirtää energian kuumana vetenä. Lämpölaitoksessa vesi lämmitetään. Lämmin vesi virtaa menoputkessa rakennuksiin. Siellä se luovuttaa lämpöä rakennuksen lämmitysjärjestelmälle. Jäähtynyt vesi palaa paluuputkessa takaisin lämmitettäväksi. Putket ovat maan alla paksussa eristeessä. Eristeen tehtävä on pitää lämpö putkessa, jotta ympäröivään maahan menisi mahdollisimman vähän lämpöä.

<svg data-fig="district" viewBox="0 0 600 320" role="img" aria-label="Kaavakuva kaukolämmön kierrosta. Vasemmalla on lämpölaitos ja oikealla koti. Punainen menoputki vie kuumaa vettä kotiin. Sininen paluuputki tuo jäähtyneen veden takaisin. Putket ovat yhteisen eristeen sisällä maan alla. Oranssit nuolet näyttävät, että eristeenkin läpi pääsee vähän lämpöä maahan. Kuva ei ole mittakaavassa." style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-7-district.webp" x="2.5" y="5" width="597" height="325.9" preserveAspectRatio="none"/>
  <foreignObject x="444" y="209.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{häviö}$</div></foreignObject>
  <foreignObject x="170" y="79.5" width="160" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{menovesi}$</div></foreignObject>
  <foreignObject x="165" y="253.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{paluuvesi}$</div></foreignObject>
  <foreignObject x="331" y="79.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{eriste}$</div></foreignObject>
  <foreignObject x="16" y="247.5" width="146" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{lämpölaitos}$</div></foreignObject>
  <foreignObject x="505" y="247.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{koti}$</div></foreignObject>
</svg>

### Siirtohäviö

Sähköverkossa osa sähköenergiasta muuttuu johtimissa ja muissa laitteissa sisäenergiaksi. Sisäenergia on aineen hiukkasten liikkeen ja niiden välisten vuorovaikutusten energiaa. Sen kasvu näkyy johtimen lämpenemisenä. Tämä energia siirtyy lämpönä ympäristöön. Kaukolämpöverkossa kuumasta vedestä siirtyy energiaa lämpönä putkien ja eristeiden läpi ympäristöön. Kummassakin verkossa käyttäjä saa vähemmän energiaa kuin verkkoon syötetään. Sitä kutsutaan **siirtohäviöksi**. Energia ei katoa (luku *Energialajit ja energian säilyminen*). Häviö on kuitenkin käyttäjälle hyödytöntä.

Suomessa sähköverkon häviöt olivat vuonna 2024 noin $4\,\%$ sähkön kulutuksesta. Kulutus oli noin $83\,\text{TWh}$ (Energiateollisuus, Sähkövuosi 2024). Tässä luvussa kulutusta käytetään sähköverkon lähtevänä energiana. Siksi $4\,\%$ on osuus siitä. Kaukolämmön verkkoon hankittiin vuonna 2024 noin $36\,\text{TWh}$. Asiakkaille käytettiin noin $32{,}7\,\text{TWh}$. Siis noin $9\,\%$ jäi matkalle (Energiateollisuus, Kaukolämpötilasto 2024). Osuus on laskettu erotuksesta, joten se on arvio. Kaukolämmön häviö on suhteessa suurempi, koska kuuma vesi on ympäristöä selvästi lämpimämpää. Mitä suurempi lämpötilaero ympäristöön on, sitä enemmän lämpöä karkaa. Lämpöä pääsee eristeen läpi koko putkiston pituudella.

```pysahdy
Verkkoon syötetään $100\,\text{GWh}$ energiaa. Käyttäjille tulee $91\,\text{GWh}$. Kuinka suuri siirtohäviö on? Katosiko häviöön mennyt energia?
---
Häviö on $9\,\text{GWh}$, eli $9\,\%$ syötetystä energiasta. Energia ei kadonnut. Se siirtyi lämpönä ympäristöön.
```

### Energian siirtäminen ajassa: varastointi

Energiaa siirretään myös ajassa. Tuulivoimaa ja aurinkosähköä syntyy silloin, kun tuulee tai paistaa. Sähköä tarvitaan kuitenkin muulloinkin. Varasto ottaa energiaa vastaan silloin, kun sitä on liikaa. Se luovuttaa energian myöhemmin.

<svg data-fig="storage" viewBox="0 0 600 300" role="img" aria-label="Kaavakuva kolmesta energiavarastosta. Vasemmalla on akku, jossa energia on kemiallista. Keskellä on pumppuvoimala: ylempi allas, alempi allas ja putki, jossa vesi virtaa alas. Oikealla on lämpövarasto. Se on eristetty säiliö, joka on täynnä kuumaa vettä. Kuva ei ole mittakaavassa." style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-7-storage.webp" x="6" y="0" width="579.7" height="298.3" preserveAspectRatio="none"/>
  <foreignObject x="55" y="252.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{akku}$</div></foreignObject>
  <foreignObject x="192" y="252.5" width="180" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{pumppuvoimala}$</div></foreignObject>
  <foreignObject x="375" y="252.5" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lämpövarasto}$</div></foreignObject>
  <foreignObject x="25" y="25.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kemiallinen}$</div></foreignObject>
  <foreignObject x="188" y="14" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{potentiaali-}$</div></foreignObject>
  <foreignObject x="188" y="42" width="190" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{energia}$</div></foreignObject>
  <foreignObject x="420" y="25.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lämpö}$</div></foreignObject>
  <foreignObject x="196" y="78" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{yläallas}$</div></foreignObject>
  <foreignObject x="176" y="210" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{alaallas}$</div></foreignObject>
</svg>

Akkuun energia varastoituu kemialliseksi energiaksi. Pumppuvoimalassa vettä pumpataan ylempään altaaseen. Alas valuva vesi pyörittää voimalaitoksen koneita. Lämpövarastossa kuuma vesi säilyy eristetyssä säiliössä. Sitä käytetään esimerkiksi kaukolämpöverkossa. Sähköä ei varastoida suuria määriä sellaisenaan. Sähkö muutetaan toiseksi energialajiksi ja takaisin. Jokaisessa muunnoksessa osa energiasta muuttuu lämmöksi.

```pysahdy
Pumppuvoimalassa vesi pumpataan ylemmäs altaaseen. Myöhemmin vesi päästetään virtaamaan alas. Missä muodossa energia on varastossa? Saadaanko kaikki energia takaisin sähköksi?
---
Energia on varastossa ylemmän altaan veden potentiaalienergiana. Kaikkea ei saada takaisin. Jokaisessa muunnoksessa osa energiasta muuttuu lämmöksi.
```

## Kaava: Siirtohäviö

Häviö on verkkoon lähtevän ja perille tulevan energian erotus. Siirron hyötysuhde (luku *Hyötysuhde*) on perille tulevan energian osuus lähtevästä energiasta:

```latex
\begin{aligned}
E_\text{häviö} &= E_\text{lähtö} - E_\text{perille} \\
\eta &= \frac{E_\text{perille}}{E_\text{lähtö}}
\end{aligned}
```

Kaavassa $E_\text{lähtö}$ on verkkoon syötetty energia ja $E_\text{perille}$ on käyttäjälle asti tullut energia. Symboli $E_\text{häviö}$ on energia, joka on siirtynyt matkalla lämpönä ympäristöön. Symboli $\eta$ on siirron hyötysuhde. Hyötysuhde annetaan prosentteina tai desimaalilukuna.

<svg data-fig="sankey" viewBox="0 0 600 330" role="img" aria-label="Energiavirtakuva mittakaavassa. Ylhäällä on sähköverkko: lähtevästä energiasta 96 % tulee perille ja 4 % häviää. Alhaalla on kaukolämpöverkko: 91 % tulee perille ja 9 % häviää. Virran leveys kertoo energian määrän. Lähtevän energian virta on molemmissa yhtä leveä." style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-7-sankey.webp" x="11.1" y="2.5" width="591.1" height="332.5" preserveAspectRatio="none"/>
  <foreignObject x="12" y="17.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{sähkö}$</div></foreignObject>
  <foreignObject x="50" y="77.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100\,\%$</div></foreignObject>
  <foreignObject x="510" y="76" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$96\,\%$</div></foreignObject>
  <foreignObject x="510" y="142" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$4\,\%$</div></foreignObject>
  <foreignObject x="12" y="175.5" width="200" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kaukolämpö}$</div></foreignObject>
  <foreignObject x="50" y="235.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100\,\%$</div></foreignObject>
  <foreignObject x="510" y="232" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$91\,\%$</div></foreignObject>
  <foreignObject x="510" y="298" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$9\,\%$</div></foreignObject>
</svg>

Kuvassa virran leveys kuvaa energian määrää. Sähköverkossa $4\,\%$ lähtevästä energiasta (kulutuksesta) häviää ja $96\,\%$ tulee perille. Kaukolämmössä luvut ovat $9\,\%$ ja $91\,\%$.

### Laskeminen häviöprosentista

Häviöprosentti kerrotaan aina lähtevästä energiasta. Jos häviö on $9{,}0\,\%$, perille tulee $100\,\% - 9{,}0\,\% = 91{,}0\,\%$ lähtevästä. Lisäksi $91{,}0\,\% = 91{,}0 : 100 = 0{,}910$. Tarvittava energia ratkaistaan kaavasta: $E_\text{perille} = \eta\, E_\text{lähtö}$ ja $E_\text{lähtö} = E_\text{perille} : \eta$.

Sama koskee tehoa. Perille tuleva teho on $\eta$ kertaa lähtevä teho. Energia ja teho liittyvät toisiinsa kaavalla $P = \tfrac{E}{t}$ (luku *Teho*). Jos häviöteho $P_\text{häviö}$ on tasainen, energiaa häviää ajassa $t$ määrä $E_\text{häviö} = P_\text{häviö} \cdot t$.

## Esimerkki

Kaukolämpöverkko siirtää lämpölaitokselta kaupunginosaan $245\,\text{MWh}$ lämpöenergiaa viikossa (esimerkkitilanne). Verkon häviö on $9{,}0\,\%$ lähtevästä energiasta. Kuinka paljon energiaa tulee perille ja kuinka paljon sitä häviää?

<!-- vaihe -->

**Tunnetut ja kysytty.**

- $E_\text{lähtö} = 245\,\text{MWh}$ ja
- häviö on $9{,}0\,\%$ lähtevästä energiasta.

Kysytään perille tulevaa energiaa $E_\text{perille}$ ja häviötä $E_\text{häviö}$.

<!-- vaihe -->

**Periaate.** Energia ei katoa. Siksi lähtevä energia on yhtä suuri kuin perille tuleva ja häviävä energia yhteensä. Kun $9{,}0\,\%$ häviää, loput $91{,}0\,\%$ tulee perille. Hyötysuhde on siis $\eta = 0{,}910$.

<!-- vaihe -->

**Kaava ratkaistuna.**

```latex
\begin{aligned}
&E_\text{perille} = \eta\, E_\text{lähtö} \\
&E_\text{häviö} = E_\text{lähtö} - E_\text{perille}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Hyötysuhde saadaan prosentista: $\eta = 100\,\% - 9{,}0\,\% = 91{,}0\,\% = 91{,}0 : 100 = 0{,}910$. Energiat ovat samassa yksikössä, megawattitunneissa. Muuta muunnosta ei tarvita.

<!-- vaihe -->

**Sijoitus.**

```latex
\begin{aligned}
E_\text{perille} &= \eta\, E_\text{lähtö} \\
&= 0{,}910 \cdot 245\,\text{MWh} \\
&= 222{,}95\,\text{MWh} \\
E_\text{häviö} &= E_\text{lähtö} - E_\text{perille} \\
&= (245 - 222{,}95)\,\text{MWh} \\
&= 22{,}05\,\text{MWh}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Perille tulee noin $223\,\text{MWh}$ ja häviää noin $22\,\text{MWh}$. Perille tuleva energia ilmoitetaan kolmella merkitsevällä numerolla. Syy on, että hyötysuhde $0{,}910$ ja lähtöenergia $245\,\text{MWh}$ tunnetaan kolmen numeron tarkkuudella. Häviö ilmoitetaan kahdella merkitsevällä numerolla. Syy on, että häviöprosentti $9{,}0\,\%$ tunnetaan vain kahden numeron tarkkuudella.

<!-- vaihe -->

**Järkevyys.** Kymmenen prosenttia energiasta $245\,\text{MWh}$ olisi $24{,}5\,\text{MWh}$. Luku $9{,}0\,\%$ on hieman pienempi, joten häviö $22\,\text{MWh}$ on oikean suuruinen. Lisäksi $$
\begin{aligned}
&222{,}95\,\text{MWh} + 22{,}05\,\text{MWh} \\
&= 245\,\text{MWh}
\end{aligned}
$$, eli energia säilyy.

## Yleinen virhekäsitys

Moni ajattelee, että siirtohäviössä energia katoaa. Energia ei katoa. Sähköverkossa osa sähköenergiasta muuttuu johtimissa sisäenergiaksi. Kaukolämpöverkossa kuumasta vedestä siirtyy energiaa putkien läpi. Kummassakin energia siirtyy lopulta lämpönä ympäristöön. Käyttäjä ei saa tätä energiaa hyötyyn.

Toinen virhe on laskea häviöprosentti perille tulevasta energiasta. Prosentti pitää laskea lähtevästä energiasta. Oletetaan, että häviö on $9{,}0\,\%$ ja perille tulee $245\,\text{MWh}$. Silloin lähtevä energia ei ole $245\,\text{MWh} + 0{,}090 \cdot 245\,\text{MWh}$. Se on $245\,\text{MWh} : 0{,}910$.

Kolmas virhe on ajatella, että häviö vähennetään prosentista yksikkönä. Häviö $4\,\%$ ei tarkoita $4\,\text{MWh}$. Se tarkoittaa neljää sadasosaa lähtevästä energiasta.

## Tiivistelmä

- Sähköenergia siirretään sähköverkossa. Pitkät matkat siirretään korkealla jännitteellä, koska silloin virta on pieni ja johtimien lämpenemisestä aiheutuva häviö on vähäinen. Muuntajat nostavat ja laskevat jännitettä.
- Lämpöenergia siirretään kaukolämpöverkossa kuumana vetenä eristetyissä putkissa. Siirtohäviössä sähköenergiaa muuttuu johtimissa sisäenergiaksi, ja kuumasta vedestä siirtyy energiaa putkien läpi. Kummassakin energia siirtyy lämpönä ympäristöön. Suomessa sähköverkon häviöt olivat noin $4\,\%$ ja kaukolämpöverkon noin $9\,\%$ (Energiateollisuus, 2024).
- Siirtohäviö on $E_\text{häviö} = E_\text{lähtö} - E_\text{perille}$ ja siirron hyötysuhde on $\eta = E_\text{perille} : E_\text{lähtö}$. Häviöprosentti lasketaan lähtevästä energiasta.
- Varastot (akku, pumppuvoimala, lämpövarasto) siirtävät energiaa ajassa. Niissäkin osa energiasta muuttuu lämmöksi.
