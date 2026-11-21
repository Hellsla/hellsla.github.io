# Aalto kohtaa esteen tai raon

> **Miksi** aallot ylettyvät aallonmurtajan kapeasta aukosta myös sataman nurkkiin? Miksi ne eivät kulje vain suoraan aukon kohdalle?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: satama ylhäältä viistosti katsottuna. Taustalla on avomeri. Siellä aallonharjat kulkevat suorina riveinä kohti satamaa. Kivistä tehdyn aallonmurtajan keskellä on kapea aukko. Aukon kummallakin puolella on pieni majakka. Aukon takana on sataman allas. Altaassa aallonharjat leviävät puoliympyröinä koko altaan leveydelle. Ne ulottuvat myös aallonmurtajan taakse altaan nurkkiin. Nurkissa laiturin veneet keinuvat. Laitureilla on punaisia venevajoja ja kuusia. Kaukana merellä on purjevene." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-11-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Aaltorintama ja säde
Aaltoa on helpointa kuvata ylhäältä katsottuna. **Aaltorintama** on viiva, joka yhdistää aallon samassa vaiheessa olevat kohdat. Samassa vaiheessa olevat kohdat liikkuvat samaan aikaan samalla tavalla. Esimerkiksi yksi aallonharja on aaltorintama. Kahden peräkkäisen harjan välinen etäisyys on aallonpituus $\lambda$ (luku *Aaltojen synty ja eteneminen*). **Säde** on nuoli, joka näyttää aallon etenemissuunnan. Säde on aina kohtisuorassa aaltorintamaa vastaan. Suoran rintaman aalto on tasoaalto. Pistemäisestä lähteestä, kuten veteen pudonneesta kivestä, lähtee ympyräaalto. Sen säteet osoittavat lähteestä poispäin joka suuntaan.

<svg data-fig="rintamat" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva kahdesta aallosta ylhäältä katsottuna. Vasemmalla on tasoaalto. Sen aaltorintamat ovat yhdensuuntaisia suoria. Suorien väli on aallonpituus lambda. Säteet ovat nuolia, jotka ovat kohtisuorassa rintamia vastaan. Oikealla on ympyräaalto, joka lähtee pistemäisestä lähteestä. Sen aaltorintamat ovat samankeskisiä ympyröitä. Säteet lähtevät lähteestä joka suuntaan, ja ne ovat kohtisuorassa rintamia vastaan." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-11-rintamat.webp" x="0" y="0" width="600" height="351.2" preserveAspectRatio="none"/>
  <foreignObject x="90" y="7.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{tasoaalto}$</div></foreignObject>
  <foreignObject x="377.5" y="7.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{ympyräaalto}$</div></foreignObject>
  <foreignObject x="90" y="301.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\lambda$</div></foreignObject>
  <foreignObject x="126" y="301.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{aaltorintama}$</div></foreignObject>
  <foreignObject x="526" y="301.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{säde}$</div></foreignObject>
</svg>

```pysahdy
Kivi putoaa veteen ja synnyttää ympyräaallon. Aaltorintama on ympyrä. Mihin suuntaan säteet osoittavat rintamaan nähden?
---
Säteet osoittavat lähteestä poispäin. Ne ovat joka kohdassa kohtisuorassa rintamaa vastaan, koska säde näyttää aallon etenemissuunnan.
```

### Heijastuminen köyden päästä
Kun aalto saapuu väliaineen rajalle, se heijastuu. Silloin osa aallosta tai koko aalto palaa takaisin. Köydessä tämän näkee yhdestä pulssista. Oletetaan, että köyden pää on kiinni seinässä. Silloin pää ei pääse liikkumaan. Ylöspäin suuntautuva pulssi vetää kiinnitystä ylöspäin. Seinä vetää köyttä yhtä suurella voimalla alaspäin. Siksi **kiinteästä päästä heijastunut pulssi on kääntynyt**: se palaa alaspäin suuntautuvana. Oletetaan sitten, että köyden pää on rengas, joka liukuu kitkatta tankoa pitkin. Silloin pää heilahtaa pulssin mukana ylös, eikä mikään vedä sitä alas. **Vapaasta päästä heijastunut pulssi ei käänny**, vaan palaa samanmerkkisenä.

<svg data-fig="koysi" viewBox="0 0 600 380" role="img" aria-label="Kaavakuva, ei mittakaavassa: köyden pulssi heijastuu kahdessa eri tapauksessa. Vasemmalla köyden pää on kiinnitetty seinään. Se on kiinteä pää. Oikealla köyden pää on rengas, joka liukuu kitkatta pystysuoraa tankoa pitkin. Se on vapaa pää. Ylärivi näyttää tilanteen ennen heijastumista: ylöspäin suuntautuva pulssi etenee oikealle kohti köyden päätä. Alarivi näyttää tilanteen heijastumisen jälkeen: pulssi etenee vasemmalle. Kiinteästä päästä heijastunut pulssi on kääntynyt alaspäin. Vapaasta päästä heijastunut pulssi on yhä ylöspäin." style="max-width:100%;font-size:24px">
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
Hollantilainen Christiaan Huygens esitti 1600-luvulla periaatteen. Sen avulla aallon etenemistä voi päätellä piirtämällä. **Huygensin periaatteen** mukaan aaltorintaman jokainen piste on uuden pienen ympyräaallon lähde. Tätä pientä aaltoa sanotaan alkeisaalloksi. Alkeisaallot etenevät samalla nopeudella kuin alkuperäinen aalto. Hetken kuluttua uusi aaltorintama on viiva, joka sivuaa eli juuri koskettaa kaikkia alkeisaaltoja. Tätä viivaa sanotaan alkeisaaltojen sivuajaksi. Avoimessa vedessä alkeisaaltojen sivuaja on taas suora, joten tasoaalto jatkaa suoraan. Joskus osa rintamasta pysähtyy esteeseen tai kimpoaa seinästä. Silloin jäljelle jääneet alkeisaallot kertovat, mihin aalto etenee.

```pysahdy
Aalto etenee nopeudella $0{,}30\,\text{m/s}$. Kuinka suuri on alkeisaallon ympyrän säde $2{,}0\,\text{s}$ kuluttua?
---
Alkeisaalto etenee yhtä nopeasti kuin alkuperäinen aalto. Säde on siis $0{,}30\,\text{m/s} \cdot 2{,}0\,\text{s} = 0{,}60\,\text{m}$. Uusi rintama sivuaa kaikkia näitä ympyröitä.
```

### Diffraktio
Aalto voi kulkea raosta tai esteen ohi. Silloin se taipuu myös esteen taakse, alueelle, jonne suoraan etenevä säde ei osu. Tätä kutsutaan **diffraktioksi** eli taipumiseksi. Huygensin periaate selittää sen. Raon kohdalla olevat rintaman pisteet ovat alkeisaaltojen lähteitä. Reunimmaisten pisteiden alkeisaallot leviävät sivuille. Raon leveyttä merkitään $b$. Jos rako on monta aallonpituutta leveä, rintama jatkaa raon kohdalla lähes suorana. Se kaartuu vain reunoilta. Kun rako on selvästi aallonpituutta kapeampi, eli $b < \lambda$, alkeisaaltoja on raon kohdalla kuin yhdestä pisteestä. Silloin aalto leviää puoliympyränä koko alueelle raon taakse. Aalto leviää paljon jo silloin, kun rako on suunnilleen aallonpituuden levyinen, $b \approx \lambda$.

<svg data-fig="diffraktio" viewBox="0 0 600 360" role="img" aria-label="Kaavakuva, ei mittakaavassa: tasoaalto tulee vasemmalta esteeseen, jossa on rako. Kuva on ylhäältä katsottuna. Vasemmalla rako on noin neljän aallonpituuden levyinen. Raon kohdalla aaltorintamat jatkavat suorina. Vain reunoilla ne kaartuvat hieman varjoon. Raon pisteisiin on piirretty pienet Huygensin alkeisaallot. Oikealla rako on aallonpituutta kapeampi. Raon takana aaltorintamat ovat puoliympyröitä, ja aalto leviää koko alueelle raon taakse." style="max-width:100%;font-size:24px">
  <image href="pics/fy5/fy5-11-diffraktio.webp" x="0" y="0" width="600" height="370" preserveAspectRatio="none"/>
  <foreignObject x="121" y="7.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$b \approx 4\lambda$</div></foreignObject>
  <foreignObject x="427.5" y="7.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$b < \lambda$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy5/ripple-model-single-slit.webp" alt="Laskettu kuva vedestä ylhäältä katsottuna. Vasemmalla on pystysuoria vaaleita ja tummia juovia. Keskellä on este, jossa on kapea rako. Raon oikealla puolella on puoliympyrän muotoisia renkaita."><figcaption>Laskettu mallikuva aaltoaltaasta ylhäältä. Vaaleat juovat ovat aallonharjoja ja tummat aallonpohjia. Suora aalto tulee vasemmalta rakoon. Rako on aallonpituuden levyinen. Raon takana aalto leviää puoliympyröinä joka suuntaan. Oikeasti aalto on raon takana heikompi. Kuvassa se näkyy selvyyden vuoksi yhtä voimakkaana. Esteestä heijastuvaa aaltoa ei ole piirretty.</figcaption></figure>

Sama pätee esteeseen. Ajatellaan estettä, joka on aallonpituutta kapeampi, esimerkiksi laituripaalua. Se ei juuri jätä taakseen varjoa, koska aalto taipuu sen ympäri. Aallonpituutta paljon leveämmän esteen taakse jää suojaisa alue. Diffraktio on siis voimakasta, kun raon tai esteen leveys on aallonpituuden suuruinen tai pienempi. Ääni taipuu ovesta käytävään. Puheäänen aallonpituus on noin metrin luokkaa. Se on suunnilleen yhtä suuri kuin oviaukon leveys.

```pysahdy
Meren aaltojen aallonpituus on $20\,\text{m}$. Laituripaalun leveys on $0{,}50\,\text{m}$. Jääkö paalun taakse selvä tyven alue?
---
Ei jää. Paalu on paljon kapeampi kuin aallonpituus. Aalto taipuu paalun ympäri ja yhtyy sen takana.
```

## Kaava: Heijastuslaki
Aalto osuu tasaiseen pintaan, kuten seinään tai rantamuuriin. Osumakohtaan piirretään pinnan **normaali**. Normaali on suora, joka on kohtisuorassa pintaa vastaan. Kulmat mitataan aina normaalista. Tulokulma on tulevan säteen ja normaalin välinen kulma. Heijastuskulma on heijastuneen säteen ja normaalin välinen kulma. Heijastuslaki on
```latex
\beta = \alpha
```
missä $\alpha$ on tulokulma ja $\beta$ heijastuskulma. Lisäksi tuleva säde, heijastunut säde ja normaali ovat samassa tasossa. Heijastunut säde on normaalin toisella puolella kuin tuleva säde. Säteen ja pinnan välinen kulma on $90^\circ - \alpha$. Sitä ei käytetä tulokulmana.

<svg data-fig="heijastuslaki" viewBox="0 0 600 340" role="img" aria-label="Kaavakuva: tuleva säde osuu seinän pintaan kohdassa O. Heijastunut säde lähtee samasta kohdasta. Kohtaan O on piirretty katkoviivalla pinnan normaali. Normaali on suora, joka on kohtisuorassa pintaa vastaan. Tulokulma alfa on tulevan säteen ja normaalin välinen kulma. Heijastuskulma beeta on heijastuneen säteen ja normaalin välinen kulma. Molemmat kulmat ovat 40 astetta. Harmaalla on merkitty säteen ja pinnan välinen kulma, 90 astetta miinus alfa. Sitä ei käytetä tulokulmana." style="max-width:100%;font-size:24px">
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

Huygensin periaate selittää, miksi kulmat ovat yhtä suuret. Tasoaallon rintama $AB$ osuu seinään vinosti, joten sen piste $A$ koskettaa seinää ensin. Siitä lähtee alkeisaalto, kun rintaman toinen pää $B$ on vielä matkan päässä. Kun $B$ saapuu seinälle kohtaan $C$, $A$:sta lähtenyt alkeisaalto on edennyt saman matkan, koska nopeus on sama. Heijastunut rintama $CD$ sivuaa alkeisaaltoja. Kolmiot $ABC$ ja $CDA$ ovat yhtenevät eli täsmälleen samanmuotoiset ja samankokoiset. Niillä on yhteinen sivu $AC$ ja yhtä pitkät sivut $BC$ ja $AD$. Lisäksi niillä on suora kulma kohdissa $B$ ja $D$. Siksi rintamat muodostavat seinän kanssa yhtä suuret kulmat. Rintaman ja seinän välinen kulma on yhtä suuri kuin säteen ja normaalin välinen kulma, joten $\beta = \alpha$.

<svg data-fig="huygens" viewBox="0 0 600 350" role="img" aria-label="Kaavakuva: Huygensin periaate selittää heijastuslain. Tasoaallon aaltorintama AB osuu vinosti seinään. Piste A on jo seinällä, kun piste B on vielä matkan päässä. Piste B etenee säteen suuntaan seinälle kohtaan C. Samassa ajassa kohdasta A lähtenyt alkeisaalto on edennyt yhtä pitkän matkan. Alkeisaallon säde on siis yhtä suuri kuin matka BC. Myös A:n ja C:n puolivälistä on piirretty pienempi alkeisaalto. Heijastunut aaltorintama CD sivuaa eli koskettaa alkeisaaltoja. Rintama AB muodostaa seinän kanssa kulman alfa. Rintama CD muodostaa seinän kanssa kulman beeta. Kulmat ovat yhtä suuret." style="max-width:100%;font-size:24px">
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
Meren aallot saapuvat suoraa aallonmurtajaa kohti. Aaltorintamat muodostavat murtajan seinän kanssa $50^\circ$:n kulman. Mikä on aaltojen tulokulma ja heijastuskulma? Mikä kulma jää heijastuneiden aaltojen etenemissuunnan ja murtajan seinän välille?

<!-- vaihe -->

**Tunnetut ja kysytty.** Aaltorintaman ja seinän välinen kulma on $\varphi = 50^\circ$.

Kysytään tulokulmaa $\alpha$, heijastuskulmaa $\beta$ ja heijastuneen säteen ja seinän pinnan välistä kulmaa $\gamma$.

<!-- vaihe -->

**Periaate.** Säde on kohtisuorassa aaltorintamaa vastaan. Normaali on kohtisuorassa seinää vastaan. Ajatellaan, että kumpaakin suoraa käännetään $90^\circ$. Silloin niiden välinen kulma ei muutu. Siksi säteen ja normaalin välinen kulma on sama kuin rintaman ja seinän välinen kulma. Heijastuslain mukaan heijastuskulma on yhtä suuri kuin tulokulma, kun molemmat mitataan normaalista.

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

**Tulos.** Tulokulma ja heijastuskulma ovat $50^\circ$. Heijastuneet aallot etenevät $40^\circ$:n kulmassa murtajan seinään nähden. Kulmat ilmoitetaan kokonaisina asteina kuten lähtötieto $50^\circ$.

<!-- vaihe -->

**Järkevyys.** Oletetaan, että rintamat ovat seinän suuntaiset, eli $\varphi = 0^\circ$. Silloin aallot tulisivat kohtisuoraan ja palaisivat samaa reittiä, $\alpha = \beta = 0^\circ$. Kun $\varphi$ kasvaa, aallot tulevat yhä loivemmin. Lisäksi $\alpha + \gamma = 90^\circ$, kuten normaalin ja pinnan välisen suoran kulman pitääkin.

## Yleinen virhekäsitys
Yleisin virhe on mitata tulokulma pinnasta eikä normaalista. Säde voi muodostaa seinän kanssa $30^\circ$:n kulman. Silloin tulokulma ei ole $30^\circ$, vaan $90^\circ - 30^\circ = 60^\circ$. Piirrä siksi aina ensin normaali osumakohtaan. Toinen virhe on ajatella, että aalto taipuu vain hyvin kapeassa raossa. Sen mukaan leveä rako päästää aallon läpi täysin suorana. Diffraktiota on jokaisessa raossa ja jokaisen esteen reunalla. Se näkyy selvästi vasta, kun raon leveys on suunnilleen aallonpituuden suuruinen. Kolmas virhe on luulla, että kiinteä pää vaimentaa pulssin. Jäykästä kiinnityksestä pulssi heijastuu lähes kokonaan, mutta kääntyneenä.

## Tiivistelmä
- Aaltorintama yhdistää samassa vaiheessa olevat kohdat. Säde näyttää etenemissuunnan kohtisuoraan rintamaa vastaan.
- Heijastuslaki: $\beta = \alpha$, kun tulokulma ja heijastuskulma mitataan pinnan normaalista.
- Köyden kiinteästä päästä pulssi heijastuu kääntyneenä, vapaasta päästä kääntymättä.
- Huygensin periaate: aaltorintaman jokainen piste on alkeisaallon lähde, ja uusi rintama sivuaa alkeisaaltoja. Periaate selittää heijastumisen ja diffraktion.
- Diffraktio eli aallon taipuminen raon tai esteen taakse on voimakasta, kun raon tai esteen leveys on suunnilleen aallonpituuden suuruinen tai pienempi.
