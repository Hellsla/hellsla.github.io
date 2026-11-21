# Aalto kohtaa esteen tai raon

> **Miksi** aallot ylettyvät aallonmurtajan kapeasta aukosta myös sataman nurkkiin eivätkä kulje vain suoraan aukon kohdalle?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: satama ylhäältä viistosti katsottuna. Taustalla on avomeri, jolla aallonharjat kulkevat suorina riveinä kohti satamaa. Kivistä tehdyssä aallonmurtajassa on keskellä kapea aukko, jonka kummallakin puolella on pieni majakka. Aukon takana sataman altaassa aallonharjat leviävät puoliympyröinä koko altaan leveydelle, myös aallonmurtajan taakse altaan nurkkiin, joissa laiturin veneet keinuvat. Laitureilla on punaisia venevajoja ja kuusia, ja kaukana merellä purjevene." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-11-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Aaltorintama ja säde
Aaltoa on helpointa kuvata ylhäältä katsottuna. **Aaltorintama** on viiva, joka yhdistää aallon samassa vaiheessa olevat kohdat, esimerkiksi yhden aallonharjan. Kahden peräkkäisen harjan välinen etäisyys on aallonpituus $\lambda$ (luku *Aaltojen synty ja eteneminen*). **Säde** on nuoli, joka näyttää aallon etenemissuunnan, ja se on aina kohtisuorassa aaltorintamaa vastaan. Suoran rintaman aalto on tasoaalto, ja pistemäisestä lähteestä, kuten veteen pudonneesta kivestä, lähtee ympyräaalto, jonka säteet osoittavat lähteestä poispäin joka suuntaan.

<svg data-fig="rintamat" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva kahdesta aallosta ylhäältä katsottuna. Vasemmalla tasoaalto: aaltorintamat ovat yhdensuuntaisia suoria, joiden väli on aallonpituus lambda, ja säteet ovat niitä vastaan kohtisuoria nuolia. Oikealla pistemäisestä lähteestä lähtevä ympyräaalto: aaltorintamat ovat samankeskisiä ympyröitä ja säteet lähtevät lähteestä joka suuntaan, kohtisuoraan rintamia vastaan." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-11-rintamat.webp" x="0" y="0" width="600" height="351.2" preserveAspectRatio="none"/>
  <foreignObject x="90" y="7.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{tasoaalto}$</div></foreignObject>
  <foreignObject x="377.5" y="7.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ympyräaalto}$</div></foreignObject>
  <foreignObject x="90" y="301.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda$</div></foreignObject>
  <foreignObject x="126" y="301.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{aaltorintama}$</div></foreignObject>
  <foreignObject x="526" y="301.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{säde}$</div></foreignObject>
</svg>

```pysahdy
Veteen pudotetun kiven synnyttämän ympyräaallon rintama on ympyrä. Mihin suuntaan säteet osoittavat suhteessa tähän rintamaan?
---
Säteet osoittavat lähteestä poispäin ja ovat joka kohdassa kohtisuorassa rintamaa vastaan, koska säde on aallon etenemissuunta.
```

### Heijastuminen köyden päästä
Kun aalto saapuu väliaineen rajalle, se heijastuu eli osa siitä tai koko aalto palaa takaisin. Köydessä tämän näkee yhdestä pulssista. Jos köyden pää on kiinni seinässä, pää ei pääse liikkumaan. Ylöspäin suuntautuva pulssi vetää kiinnitystä ylöspäin, ja seinä vetää köyttä yhtä suurella voimalla alaspäin. Siksi **kiinteästä päästä heijastunut pulssi on kääntynyt**: se palaa alaspäin suuntautuvana. Jos köyden pää on rengas, joka liukuu kitkatta tankoa pitkin, pää heilahtaa pulssin mukana ylös, eikä mikään vedä sitä alas. **Vapaasta päästä heijastunut pulssi ei käänny**, vaan palaa samanmerkkisenä.

<svg data-fig="koysi" viewBox="0 0 600 380" role="img" aria-label="Kaavakuva, ei mittakaavassa: köyden pulssin heijastuminen kahdessa tapauksessa. Vasemmalla köyden pää on kiinnitetty seinään (kiinteä pää), oikealla pää on rengas, joka liukuu kitkatta pystysuoraa tankoa pitkin (vapaa pää). Ylärivillä ennen heijastumista ylöspäin suuntautunut pulssi etenee oikealle kohti päätä. Alarivillä heijastumisen jälkeen pulssi etenee vasemmalle: kiinteästä päästä heijastunut pulssi on kääntynyt alaspäin, vapaasta päästä heijastunut on yhä ylöspäin." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-11-koysi.webp" x="1.2" y="0" width="597" height="386.8" preserveAspectRatio="none"/>
  <foreignObject x="83.5" y="7.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kiinteä pää}$</div></foreignObject>
  <foreignObject x="396" y="7.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{vapaa pää}$</div></foreignObject>
  <foreignObject x="16" y="45.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{ennen}$</div></foreignObject>
  <foreignObject x="136" y="59.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <foreignObject x="16" y="211.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{jälkeen}$</div></foreignObject>
  <foreignObject x="120" y="219.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <foreignObject x="316" y="45.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{ennen}$</div></foreignObject>
  <foreignObject x="436" y="59.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
  <foreignObject x="316" y="211.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{jälkeen}$</div></foreignObject>
  <foreignObject x="420" y="219.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#1971c2">$v$</div></foreignObject>
</svg>

### Huygensin periaate
Hollantilainen Christiaan Huygens esitti 1600-luvulla periaatteen, jolla aallon etenemistä voi päätellä piirtämällä. **Huygensin periaatteen** mukaan aaltorintaman jokainen piste toimii uuden pienen ympyräaallon, alkeisaallon, lähteenä. Alkeisaallot etenevät samalla nopeudella kuin alkuperäinen aalto, ja hetken kuluttua uusi aaltorintama on viiva, joka sivuaa kaikkia alkeisaaltoja. Avoimessa vedessä alkeisaaltojen sivuaja on taas suora, joten tasoaalto jatkaa suoraan. Kun osa rintamasta pysähtyy esteeseen tai kimpoaa seinästä, jäljelle jääneet alkeisaallot kertovat, mihin aalto etenee.

```pysahdy
Aalto etenee nopeudella $0{,}30\,\text{m/s}$. Kuinka suuren ympyrän säteen alkeisaalto on piirtänyt $2{,}0\,\text{s}$ kuluttua?
---
Alkeisaalto etenee samalla nopeudella kuin alkuperäinen aalto, joten säde on $0{,}30\,\text{m/s} \cdot 2{,}0\,\text{s} = 0{,}60\,\text{m}$. Uusi rintama sivuaa kaikkia näitä ympyröitä.
```

### Diffraktio
Kun aalto kulkee raosta tai esteen ohi, se taipuu myös esteen taakse, alueelle, jonne suoraan etenevä säde ei osu. Tätä kutsutaan **diffraktioksi** eli taipumiseksi. Huygensin periaate selittää sen: raon kohdalla olevat rintaman pisteet ovat alkeisaaltojen lähteitä, ja reunimmaisten pisteiden alkeisaallot leviävät sivuille. Raon leveyttä merkitään $b$. Jos rako on monta aallonpituutta leveä, rintama jatkaa raon kohdalla lähes suorana ja kaartuu vain reunoilta. Kun rako on selvästi aallonpituutta kapeampi, eli $b < \lambda$, alkeisaaltoja on raon kohdalla kuin yhdestä pisteestä, ja aalto leviää puoliympyränä koko alueelle raon taakse. Jo silloin, kun rako on suunnilleen aallonpituuden levyinen, $b \approx \lambda$, aalto leviää paljon.

<svg data-fig="diffraktio" viewBox="0 0 600 360" role="img" aria-label="Kaavakuva, ei mittakaavassa: tasoaalto tulee vasemmalta esteeseen, jossa on rako, ylhäältä katsottuna. Vasemmalla rako on noin neljän aallonpituuden levyinen: raon kohdalla aaltorintamat jatkavat suorina, ja vain reunoilla ne kaartuvat hieman varjoon. Raon pisteisiin on piirretty pienet Huygensin alkeisaallot. Oikealla rako on aallonpituutta kapeampi: raon takana aaltorintamat ovat puoliympyröitä, ja aalto leviää koko alueelle raon taakse." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-11-diffraktio.webp" x="0" y="0" width="600" height="370" preserveAspectRatio="none"/>
  <foreignObject x="121" y="7.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$b \approx 4\lambda$</div></foreignObject>
  <foreignObject x="427.5" y="7.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$b < \lambda$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy5/ripple-model-single-slit.webp" alt="Laskettu kuva vedenpinnasta ylhäältä katsottuna. Vasemmalla on pystysuoria vaaleita ja tummia juovia. Keskellä on pystysuora este, jossa on kapea rako. Esteen oikealla puolella raosta lähtee puoliympyrän muotoisia renkaita, jotka täyttävät koko oikean puolen."><figcaption>Laskettu mallikuva aaltoaltaasta ylhäältä katsottuna: vaaleat juovat ovat aallonharjoja ja tummat aallonpohjia. Vasemmalta tuleva tasoaalto kulkee raosta, joka on aallonpituuden levyinen, ja raon takana aalto leviää puoliympyröinä koko alueelle. Todellisuudessa aalto on raon takana heikompi; kuvassa se näytetään selvyyden vuoksi samalla kontrastilla, eikä esteestä heijastuvaa aaltoa ole piirretty.</figcaption></figure>

Sama pätee esteeseen. Laituripaalun kaltainen este, joka on aallonpituutta kapeampi, ei juuri jätä taakseen varjoa, koska aalto taipuu sen ympäri. Aallonpituutta paljon leveämmän esteen taakse jää suojaisa alue. Diffraktio on siis voimakasta silloin, kun raon tai esteen leveys on aallonpituuden suuruusluokkaa tai pienempi. Ääni taipuu ovesta käytävään, koska puheäänen aallonpituus on noin metrin suuruusluokkaa, oviaukon levyinen.

```pysahdy
Meren aaltojen aallonpituus on $20\,\text{m}$, ja laituripaalun leveys on $0{,}50\,\text{m}$. Jääkö paalun taakse selvä tyven alue?
---
Ei jää. Paalu on paljon aallonpituutta kapeampi, joten aalto taipuu sen ympäri ja yhtyy sen takana.
```

## Kaava: Heijastuslaki
Kun aalto osuu tasaiseen pintaan, kuten seinään tai rantamuuriin, osumakohtaan piirretään pinnan **normaali** eli pintaa vastaan kohtisuora suora. Kulmat mitataan aina normaalista: tulokulma on tulevan säteen ja normaalin välinen kulma ja heijastuskulma heijastuneen säteen ja normaalin välinen kulma. Heijastuslaki on
```latex
\beta = \alpha
```
missä $\alpha$ on tulokulma ja $\beta$ heijastuskulma. Lisäksi tuleva säde, heijastunut säde ja normaali ovat samassa tasossa, ja heijastunut säde on normaalin toisella puolella kuin tuleva. Säteen ja pinnan välinen kulma on $90^\circ - \alpha$, eikä sitä käytetä tulokulmana.

<svg data-fig="heijastuslaki" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva: tuleva säde osuu seinän pintaan kohdassa O, ja heijastunut säde lähtee siitä. Kohdasta O on piirretty katkoviivalla pinnan normaali eli pintaa vastaan kohtisuora suora. Tulokulma alfa on tulevan säteen ja normaalin välinen kulma ja heijastuskulma beeta heijastuneen säteen ja normaalin välinen kulma; molemmat ovat 40 astetta. Harmaalla on merkitty säteen ja pinnan välinen kulma, 90 astetta miinus alfa, jota ei käytetä tulokulmana." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-11-heijastuslaki.webp" x="6.1" y="3.7" width="588.2" height="340.7" preserveAspectRatio="none"/>
  <foreignObject x="246" y="33.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{normaali}$</div></foreignObject>
  <foreignObject x="257" y="157.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\alpha$</div></foreignObject>
  <foreignObject x="323" y="157.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\beta$</div></foreignObject>
  <foreignObject x="88" y="183.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$90^\circ - \alpha$</div></foreignObject>
  <foreignObject x="290" y="293.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$O$</div></foreignObject>
  <foreignObject x="20" y="57.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{tuleva säde}$</div></foreignObject>
  <foreignObject x="385" y="57.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{heijastunut säde}$</div></foreignObject>
  <foreignObject x="510" y="225.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{seinä}$</div></foreignObject>
</svg>

Huygensin periaate selittää, miksi kulmat ovat yhtä suuret. Tasoaallon rintama $AB$ osuu seinään vinosti, joten sen piste $A$ koskettaa seinää ensin. Siitä lähtee alkeisaalto, kun rintaman toinen pää $B$ on vielä matkan päässä. Kun $B$ saapuu seinälle kohtaan $C$, $A$:sta lähtenyt alkeisaalto on edennyt saman matkan, koska nopeus on sama. Heijastunut rintama $CD$ sivuaa alkeisaaltoja. Kolmiot $ABC$ ja $CDA$ ovat yhtenevät: niillä on yhteinen sivu $AC$, yhtä pitkät sivut $BC$ ja $AD$ sekä suora kulma kohdissa $B$ ja $D$. Siksi rintamat muodostavat seinän kanssa yhtä suuret kulmat. Rintaman ja seinän välinen kulma on yhtä suuri kuin säteen ja normaalin välinen kulma, joten $\beta = \alpha$.

<svg data-fig="huygens" viewBox="0 0 600 350" role="img" aria-label="Kaavakuva: Huygensin periaate selittää heijastuslain. Tasoaallon aaltorintama AB osuu vinosti seinään: piste A on jo seinällä, kun piste B on vielä matkan päässä. Kun B etenee säteen suuntaan seinälle kohtaan C, kohdasta A lähtenyt alkeisaalto on ehtinyt yhtä pitkän matkan, ja sen säde on yhtä suuri kuin matka BC. Myös A:n ja C:n puolivälistä on piirretty pienempi alkeisaalto. Heijastunut aaltorintama CD sivuaa alkeisaaltoja. Rintama AB muodostaa seinän kanssa kulman alfa ja rintama CD kulman beeta, ja kulmat ovat yhtä suuret." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-11-huygens.webp" x="1.2" y="1.2" width="597" height="358.2" preserveAspectRatio="none"/>
  <foreignObject x="197.5" y="257" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\alpha$</div></foreignObject>
  <foreignObject x="391.5" y="257" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$\beta$</div></foreignObject>
  <foreignObject x="108" y="263.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$A$</div></foreignObject>
  <foreignObject x="481" y="263.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$C$</div></foreignObject>
  <foreignObject x="347" y="113.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$B$</div></foreignObject>
  <foreignObject x="242" y="113.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$D$</div></foreignObject>
  <foreignObject x="123.5" y="37.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{alkeisaalto}$</div></foreignObject>
</svg>

## Esimerkki
Meren aallot saapuvat suoraa aallonmurtajaa kohti niin, että aaltorintamat muodostavat murtajan seinän kanssa $50^\circ$:n kulman. Mikä on aaltojen tulokulma ja heijastuskulma, ja mikä kulma heijastuneiden aaltojen etenemissuunnan ja murtajan seinän välille jää?

<!-- vaihe -->

**Tunnetut ja kysytty.** Aaltorintaman ja seinän välinen kulma on $\varphi = 50^\circ$.

Kysytään tulokulmaa $\alpha$, heijastuskulmaa $\beta$ ja heijastuneen säteen ja seinän pinnan välistä kulmaa $\gamma$.

<!-- vaihe -->

**Periaate.** Säde on kohtisuorassa aaltorintamaa vastaan ja normaali kohtisuorassa seinää vastaan. Kun kumpaakin suoraa käännetään $90^\circ$, niiden välinen kulma ei muutu, joten säteen ja normaalin välinen kulma on sama kuin rintaman ja seinän välinen kulma. Heijastuslain mukaan heijastuskulma on yhtä suuri kuin tulokulma, kun molemmat mitataan normaalista.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&\alpha = \varphi \\
&\beta = \alpha \\
&\gamma = 90^\circ - \beta
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita: kaikki kulmat ovat asteina.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&\alpha = 50^\circ \\
&\beta = 50^\circ \\
&\gamma = 90^\circ - 50^\circ = 40^\circ
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Tulokulma ja heijastuskulma ovat $50^\circ$, ja heijastuneet aallot etenevät $40^\circ$:n kulmassa murtajan seinään nähden. Kulmat ilmoitetaan kokonaisina asteina kuten lähtötieto $50^\circ$.

<!-- vaihe -->

**Järkevyys.** Jos rintamat olisivat seinän suuntaiset, eli $\varphi = 0^\circ$, aallot tulisivat kohtisuoraan ja palaisivat samaa reittiä, $\alpha = \beta = 0^\circ$. Kun $\varphi$ kasvaa, aallot tulevat yhä loivemmin. Lisäksi $\alpha + \gamma = 90^\circ$, kuten normaalin ja pinnan välisen suoran kulman pitääkin.

## Yleinen virhekäsitys
Yleisin virhe on mitata tulokulma pinnasta eikä normaalista. Jos säde muodostaa seinän kanssa $30^\circ$:n kulman, tulokulma ei ole $30^\circ$ vaan $90^\circ - 30^\circ = 60^\circ$. Piirrä siksi aina ensin normaali osumakohtaan. Toinen virhe on ajatella, että aalto taipuu vain hyvin kapeassa raossa ja leveä rako päästää sen läpi täysin suorana. Diffraktiota on jokaisessa raossa ja jokaisen esteen reunalla, mutta se näkyy selvästi vasta, kun raon leveys on aallonpituuden suuruusluokkaa. Kolmas virhe on luulla, että kiinteä pää vaimentaa pulssin. Jäykästä kiinnityksestä pulssi heijastuu lähes kokonaan, mutta kääntyneenä.

## Tiivistelmä
- Aaltorintama yhdistää samassa vaiheessa olevat kohdat, ja säde näyttää etenemissuunnan kohtisuoraan rintamaa vastaan.
- Heijastuslaki: $\beta = \alpha$, kun tulokulma ja heijastuskulma mitataan pinnan normaalista.
- Köyden kiinteästä päästä pulssi heijastuu kääntyneenä, vapaasta päästä kääntymättä.
- Huygensin periaate: aaltorintaman jokainen piste on alkeisaallon lähde, ja uusi rintama sivuaa alkeisaaltoja. Periaate selittää heijastumisen ja diffraktion.
- Diffraktio eli aallon taipuminen raon tai esteen taakse on voimakasta, kun raon tai esteen leveys on suunnilleen aallonpituuden suuruinen tai pienempi.
