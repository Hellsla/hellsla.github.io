# Energian siirtäminen: sähkö ja lämpö

> **Miksi** voimalinjojen jännite on satoja kilovoltteja, vaikka pistorasiasta saa vain $230\,\text{V}$, ja miksi kaukolämpöputket kääritään paksuun eristeeseen?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: maisemassa korkeat voimalinjapylväät, joiden johdot kulkevat kauas. Etualalla maan läpi leikattu näkymä: kaukolämpöputket, joiden ympärillä on paksu eristekerros, vievät lämpöä talolle." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-7-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

Energiaa tuotetaan usein kaukana siitä, missä sitä käytetään: voimalaitos on kaupungin ulkopuolella, mutta lämmitin ja pistorasia ovat kotona. Energia täytyy siis siirtää käyttäjälle. Energiaa voidaan siirtää paikasta toiseen monella tavalla. Tässä luvussa tarkastellaan kahta yhteiskunnan energiaverkkojen kannalta tärkeää tapaa: **sähköenergian** siirtämistä sähköverkossa ja **lämpöenergian** siirtämistä kaukolämpöverkon vesiputkissa.

### Sähköverkko

**Sähköverkko** vie sähköenergian voimalaitokselta kotiin. Pitkät matkat kulkevat kantaverkon voimalinjoissa, joiden jännite on $110\text{–}400\,\text{kV}$. Lähempänä käyttäjää jännite lasketaan ensin $20\,\text{kV}$:iin ja lopuksi pienjänniteverkon $0{,}4\,\text{kV}$:iin, josta kodin pistorasiat saavat $230\,\text{V}$. Jännitteen muuttaminen tapahtuu muuntajissa.

<svg data-fig="grid" viewBox="0 0 600 332" role="img" aria-label="Kaavakuva sähköverkon reitistä voimalaitokselta kotiin. Vasemmalta oikealle: voimalaitos ja sen muuntaja, kantaverkon voimalinja (jännite 110 kV:sta 400 kV:iin), sähköasema, jakeluverkon pylväät (20 kV) ja koti (0,4 kV, pistorasiassa 230 V). Alla oranssi nuoli kuvaa energian kulkua voimalaitokselta kotiin. Kuva ei ole mittakaavassa." style="max-width:100%;font-size:24px">
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

Saman tehon voi siirtää kahdella tavalla: pienellä jännitteellä ja suurella sähkövirralla tai suurella jännitteellä ja pienellä sähkövirralla. Johdin lämpenee sitä enemmän, mitä suurempi virta siinä kulkee, ja lämmitykseen menevä energia on häviötä. Siksi pitkä matka siirretään suurella jännitteellä, jolloin virta ja häviö jäävät pieniksi. Jännitteen, virran ja häviön tarkka yhteys kuuluu myöhempiin sähkökursseihin.

Muuntaja nostaa jännitteen voimalaitoksella ja laskee sen takaisin käyttäjän lähellä. Hyvässä muuntajassa häviö on hyvin pieni.

```pysahdy
Kaksi voimalinjaa siirtää saman tehon, toisessa jännite on suuri ja toisessa pieni. Kummassa linjassa johtimet lämpenevät enemmän?
---
Pienemmän jännitteen linjassa. Siellä virta on suurempi, ja suuri virta lämmittää johdinta enemmän.
```

<figure class="unit-photo"><img src="pics/fy2/muurame-transformer.webp" alt="Suuri vihreänharmaa muuntaja eristimineen ja tuulettimineen aidatulla sähköasemalla koivujen keskellä."><figcaption>Sähköaseman muuntaja Muuramessa. Sähköasemalla muuntaja laskee voimajohdon korkean jännitteen jakeluverkon jännitteeksi.</figcaption></figure>

### Kaukolämpö

**Kaukolämpö** siirtää energian kuumana vetenä. Lämpölaitoksessa lämmitetty vesi virtaa menoputkessa rakennuksiin ja luovuttaa lämpöä rakennuksen lämmitysjärjestelmälle. Jäähtynyt vesi palaa paluuputkessa takaisin lämmitettäväksi. Putket ovat maan alla paksussa eristeessä, jotta lämpöä menisi ympäröivään maahan mahdollisimman vähän.

<svg data-fig="district" viewBox="0 0 600 320" role="img" aria-label="Kaavakuva kaukolämmön kierrosta. Vasemmalla lämpölaitos, oikealla koti. Punainen menoputki vie kuumaa vettä kotiin ja sininen paluuputki tuo jäähtyneen veden takaisin. Putket ovat yhteisen eristeen sisällä maan alla. Oranssit nuolet osoittavat, että eristeestäkin pääsee vähän lämpöä maahan. Kuva ei ole mittakaavassa." style="max-width:100%;font-size:24px">
  <image href="pics/fy2/fy2-7-district.webp" x="2.5" y="5" width="597" height="325.9" preserveAspectRatio="none"/>
  <foreignObject x="444" y="209.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{häviö}$</div></foreignObject>
  <foreignObject x="170" y="79.5" width="160" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{menovesi}$</div></foreignObject>
  <foreignObject x="165" y="253.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{paluuvesi}$</div></foreignObject>
  <foreignObject x="331" y="79.5" width="90" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{eriste}$</div></foreignObject>
  <foreignObject x="16" y="247.5" width="146" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{lämpölaitos}$</div></foreignObject>
  <foreignObject x="505" y="247.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{koti}$</div></foreignObject>
</svg>

### Siirtohäviö

Sähköverkossa osa sähköenergiasta muuttuu johtimissa ja muissa laitteissa sisäenergiaksi, joka siirtyy lämpönä ympäristöön. Kaukolämpöverkossa puolestaan kuumasta vedestä siirtyy energiaa lämpönä putkiston ja eristeiden läpi ympäristöön. Molemmissa tapauksissa käyttäjälle saadaan vähemmän energiaa kuin verkkoon syötetään. Tätä kutsutaan **siirtohäviöksi**. Energia ei katoa (luku *Energialajit ja energian säilyminen*), mutta häviö on käyttäjälle hyödytöntä.

Suomessa sähköverkon häviöt olivat vuonna 2024 noin $4\,\%$ sähkön kulutuksesta, kun kulutus oli noin $83\,\text{TWh}$ (Energiateollisuus, Sähkövuosi 2024). Tässä luvussa kulutusta käytetään sähköverkon lähtevänä energiana, joten $4\,\%$ on osuus siitä. Kaukolämmön verkkoon hankittiin vuonna 2024 noin $36\,\text{TWh}$ ja asiakkaille käytettiin noin $32{,}7\,\text{TWh}$, joten noin $9\,\%$ jäi matkalle (Energiateollisuus, Kaukolämpötilasto 2024; osuus on laskettu erotuksesta, joten se on arvio). Kaukolämmön häviö on suhteessa suurempi, koska kuuma vesi on ympäristöä selvästi lämpimämpää: mitä suurempi lämpötilaero ympäristöön on, sitä enemmän lämpöä karkaa, ja lämpöä pääsee eristeen läpi koko putkiston pituudella.

```pysahdy
Verkkoon syötetään $100\,\text{GWh}$ ja käyttäjille tulee $91\,\text{GWh}$. Paljonko on siirtohäviö, ja katosiko häviöön mennyt energia?
---
Häviö on $9\,\text{GWh}$, eli $9\,\%$ syötetystä energiasta. Energia ei kadonnut vaan siirtyi lämpönä ympäristöön.
```

### Energian siirtäminen ajassa: varastointi

Energiaa siirretään myös ajassa. Tuulivoimaa ja aurinkosähköä syntyy silloin, kun tuulee tai paistaa, mutta sähköä tarvitaan muulloinkin. Varasto ottaa energiaa vastaan silloin, kun sitä on liikaa, ja luovuttaa sen myöhemmin.

<svg data-fig="storage" viewBox="0 0 600 300" role="img" aria-label="Kaavakuva kolmesta energiavarastosta. Vasemmalla akku, jossa energia on kemiallista. Keskellä pumppuvoimala: ylempi allas, alempi allas ja putki, jossa vesi virtaa alas. Oikealla lämpövarasto, eristetty säiliö täynnä kuumaa vettä. Kuva ei ole mittakaavassa." style="max-width:100%;font-size:24px">
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

Akkuun energia varastoituu kemialliseksi energiaksi. Pumppuvoimalassa vettä pumpataan ylempään altaaseen, ja alas valuva vesi pyörittää voimalaitoksen koneita. Lämpövarastossa kuuma vesi säilyy eristetyssä säiliössä, ja sitä käytetään esimerkiksi kaukolämpöverkossa. Sähköä ei varastoida suuria määriä sellaisenaan vaan muuttamalla se toiseksi energialajiksi ja takaisin, ja jokaisessa muunnoksessa osa energiasta muuttuu lämmöksi.

```pysahdy
Pumppuvoimalassa vesi pumpataan ylemmäs altaaseen ja päästetään myöhemmin virtaamaan alas. Missä muodossa energia on varastossa, ja saadaanko se kaikki takaisin sähköksi?
---
Energia on varastossa ylemmän altaan veden potentiaalienergiana. Kaikkea ei saada takaisin, koska jokaisessa muunnoksessa osa energiasta muuttuu lämmöksi.
```

## Kaava: Siirtohäviö

Häviö on verkkoon lähtevän ja perille tulevan energian erotus. Siirron hyötysuhde (luku *Hyötysuhde*) on perille tulevan energian osuus lähtevästä energiasta:

```latex
\begin{aligned}
E_\text{häviö} &= E_\text{lähtö} - E_\text{perille} \\
\eta &= \frac{E_\text{perille}}{E_\text{lähtö}}
\end{aligned}
```

missä $E_\text{lähtö}$ on verkkoon syötetty energia, $E_\text{perille}$ käyttäjälle asti tullut energia, $E_\text{häviö}$ matkalla lämpönä ympäristöön siirtynyt energia ja $\eta$ siirron hyötysuhde. Hyötysuhde annetaan prosentteina tai desimaalilukuna.

<svg data-fig="sankey" viewBox="0 0 600 330" role="img" aria-label="Energiavirtakuva mittakaavassa. Ylhäällä sähköverkko: lähtevästä energiasta 96 % tulee perille ja 4 % häviää. Alhaalla kaukolämpöverkko: 91 % tulee perille ja 9 % häviää. Virran leveys on verrannollinen energiaan; lähtevän energian leveys on molemmissa sama." style="max-width:100%;font-size:24px">
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

Kuvassa virran leveys kuvaa energian määrää. Sähköverkossa $4\,\%$ lähtevästä energiasta (kulutuksesta) häviää ja $96\,\%$ tulee perille, kaukolämmössä $9\,\%$ ja $91\,\%$.

### Laskeminen häviöprosentista

Häviöprosentti kerrotaan aina lähtevästä energiasta. Jos häviö on $9{,}0\,\%$, perille tulee $100\,\% - 9{,}0\,\% = 91{,}0\,\%$ lähtevästä, ja $91{,}0\,\% = 91{,}0 : 100 = 0{,}910$. Kaavasta ratkaistaan tarvittava energia: $E_\text{perille} = \eta\, E_\text{lähtö}$ ja $E_\text{lähtö} = E_\text{perille} : \eta$.

Sama koskee tehoa: perille tuleva teho on $\eta$ kertaa lähtevä teho. Energia ja teho liittyvät toisiinsa kaavalla $P = \tfrac{E}{t}$ (luku *Teho*), joten tasaisella häviöteholla $P_\text{häviö}$ aikana $t$ häviää energiaa $E_\text{häviö} = P_\text{häviö} \cdot t$.

## Esimerkki

Kaukolämpöverkko siirtää lämpölaitokselta kaupunginosaan $245\,\text{MWh}$ lämpöenergiaa viikossa (esimerkkitilanne). Verkon häviö on $9{,}0\,\%$ lähtevästä energiasta. Kuinka paljon energiaa tulee perille ja kuinka paljon sitä häviää?

<!-- vaihe -->

**Tunnetut ja kysytty.**

- $E_\text{lähtö} = 245\,\text{MWh}$ ja
- häviö $9{,}0\,\%$ lähtevästä energiasta.

Kysytään perille tulevaa energiaa $E_\text{perille}$ ja häviötä $E_\text{häviö}$.

<!-- vaihe -->

**Periaate.** Energia ei katoa, joten lähtevä energia on yhtä suuri kuin perille tuleva ja häviävä energia yhteensä. Kun $9{,}0\,\%$ häviää, loput $91{,}0\,\%$ tulee perille, eli hyötysuhde on $\eta = 0{,}910$.

<!-- vaihe -->

**Kaava ratkaistuna.**

```latex
\begin{aligned}
&E_\text{perille} = \eta\, E_\text{lähtö} \\
&E_\text{häviö} = E_\text{lähtö} - E_\text{perille}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Hyötysuhde saadaan prosentista: $\eta = 100\,\% - 9{,}0\,\% = 91{,}0\,\% = 91{,}0 : 100 = 0{,}910$. Energiat ovat samassa yksikössä, megawattitunneissa, joten muuta muunnosta ei tarvita.

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

**Tulos.** Perille tulee noin $223\,\text{MWh}$ ja häviää noin $22\,\text{MWh}$. Perille tuleva energia ilmoitetaan kolmella merkitsevällä numerolla, koska hyötysuhde $0{,}910$ ja lähtöenergia $245\,\text{MWh}$ tunnetaan kolmen numeron tarkkuudella. Häviö ilmoitetaan kahdella merkitsevällä numerolla, koska häviöprosentti $9{,}0\,\%$ tunnetaan vain kahden numeron tarkkuudella.

<!-- vaihe -->

**Järkevyys.** Kymmenen prosenttia energiasta $245\,\text{MWh}$ olisi $24{,}5\,\text{MWh}$, ja $9{,}0\,\%$ on hieman vähemmän, joten häviö $22\,\text{MWh}$ on oikean suuruinen. Lisäksi $$
\begin{aligned}
&222{,}95\,\text{MWh} + 22{,}05\,\text{MWh} \\
&= 245\,\text{MWh}
\end{aligned}
$$, eli energia säilyy.

## Yleinen virhekäsitys

Moni ajattelee, että siirtohäviössä energia katoaa. Energia ei katoa. Sähköverkossa osa sähköenergiasta muuttuu johtimissa sisäenergiaksi, ja kaukolämpöverkossa kuumasta vedestä siirtyy energiaa putkien läpi. Kummassakin tapauksessa energia siirtyy lopulta lämpönä ympäristöön, eikä käyttäjä saa sitä hyötyyn.

Toinen virhe on laskea häviöprosentti perille tulevasta energiasta. Prosentti kuuluu laskea lähtevästä energiasta: jos häviö on $9{,}0\,\%$ ja perille tulee $245\,\text{MWh}$, lähtevä energia ei ole $245\,\text{MWh} + 0{,}090 \cdot 245\,\text{MWh}$ vaan $245\,\text{MWh} : 0{,}910$.

Kolmas virhe on ajatella, että häviö vähennetään yksikkönä prosentista: häviö $4\,\%$ ei tarkoita $4\,\text{MWh}$ vaan neljää sadasosaa lähtevästä energiasta.

## Tiivistelmä

- Sähköenergia siirretään sähköverkossa, pitkät matkat korkealla jännitteellä, koska silloin virta on pieni ja johtimien lämpenemisestä aiheutuva häviö vähäinen. Muuntajat nostavat ja laskevat jännitettä.
- Lämpöenergia siirretään kaukolämpöverkossa kuumana vetenä eristetyissä putkissa. Siirtohäviössä sähköenergiaa muuttuu johtimissa sisäenergiaksi, ja kuumasta vedestä siirtyy energiaa putkien läpi; molemmissa energia siirtyy lämpönä ympäristöön. Suomessa sähköverkon häviöt olivat noin $4\,\%$ ja kaukolämpöverkon noin $9\,\%$ (Energiateollisuus, 2024).
- Siirtohäviö $E_\text{häviö} = E_\text{lähtö} - E_\text{perille}$ ja siirron hyötysuhde $\eta = E_\text{perille} : E_\text{lähtö}$. Häviöprosentti lasketaan lähtevästä energiasta.
- Varastot (akku, pumppuvoimala, lämpövarasto) siirtävät energiaa ajassa, mutta niissäkin osa energiasta muuttuu lämmöksi.
