# Olomuodon muutokset

> **Miksi** normaalissa ilmanpaineessa kiehuvan veden lämpötila pysyy noin $100\,{}^\circ\text{C}$:ssa, vaikka kattilaan siirtyy koko ajan energiaa?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: keittiön liedellä kattila, jossa vesi kiehuu voimakkaasti. Levy hehkuu punaisena ja siitä siirtyy jatkuvasti energiaa kattilaan, vedessä on kuplia ja siitä nousee höyryä. Veteen upotetun lämpömittarin pylväs pysyy samalla korkeudella." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-7-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus
Aine esiintyy kolmessa olomuodossa: kiinteänä, nesteenä ja kaasuna. Mikromallin mukaan kiinteässä aineessa hiukkaset värähtelevät paikoillaan toistensa sitomina, nesteessä ne liikkuvat toistensa ohi mutta pysyvät yhdessä, ja kaasussa ne liikkuvat vapaasti ja törmäilevät vain harvoin. Olomuodon muutoksessa muuttuvat hiukkasten keskinäiset vuorovaikutukset: sulamisessa kiinteän aineen säännöllinen järjestys purkautuu, ja höyrystymisessä hiukkaset etääntyvät kauas toisistaan. Hiukkaset itse eivät muutu: kun jää sulaa tai vesi kiehuu, vesimolekyylien sisäiset kemialliset sidokset eivät katkea. Vastakkaiset muutokset ovat jähmettyminen ja tiivistyminen. Jää voi myös sublimoitua suoraan höyryksi, kuten pakkasella kuivuvassa pyykissä.

<svg data-fig="micro-model" viewBox="0 0 600 306" role="img" aria-label="Mikromalli, kaavakuva: kiinteässä aineessa hiukkaset ovat säännöllisessä järjestyksessä toisissaan kiinni, nesteessä ne ovat epäjärjestyksessä mutta yhä kosketuksissa, kaasussa ne ovat kaukana toisistaan ja liikkuvat vapaasti. Nuolet: kiinteä sulaa nesteeksi, neste höyrystyy kaasuksi." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-7-micro-model.webp" x="1.2" y="0" width="597" height="317.2" preserveAspectRatio="none"/>
  <foreignObject x="163" y="47.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{sulaa}$</div></foreignObject>
  <foreignObject x="343" y="47.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{höyrystyy}$</div></foreignObject>
  <foreignObject x="47.5" y="259.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kiinteä}$</div></foreignObject>
  <foreignObject x="265" y="259.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{neste}$</div></foreignObject>
  <foreignObject x="470" y="259.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kaasu}$</div></foreignObject>
</svg>

<figure class="unit-photo"><img src="pics/fy3/la-palma-eruption.webp" alt="Yöllinen tulivuorenpurkaus: hehkuva laavasuihku ja rinnettä alas valuvia laavavirtoja punaisen savun alla. Alhaalla näkyy kylän valoja."><figcaption>La Palman tulivuorenpurkaus vuonna 2021. Purkauksessa maan pinnalle virrannut laava jäähtyy ja jähmettyy.</figcaption></figure>

### Mihin energia menee?
Sulaminen ja höyrystyminen vaativat energiaa, mutta eivät nosta lämpötilaa. Kun jäätä lämmitetään, sen lämpötila nousee $0\,{}^\circ\text{C}$:seen asti. Sitten lämpötila pysyy vakiona, kunnes kaikki jää on sulanut, vaikka energiaa siirtyy koko ajan. Sulamisen ja höyrystymisen aikana aineeseen siirtyvä energia muuttaa hiukkasten keskinäisiä vuorovaikutuksia ja kasvattaa niiden välistä vuorovaikutusenergiaa. Puhtaan aineen olomuodon muuttuessa vakiopaineessa lämpötila pysyy vakiona, joten hiukkasten keskimääräinen liike-energia ei kasva.

<figure class="unit-photo"><img src="pics/fy3/melting-ice.webp" alt="Läpikuultavia, osittain sulaneita jääpaloja läheltä kuvattuna."><figcaption>Sulavaa jäätä läheltä kuvattuna. Jään sulaminen vaatii energiaa.</figcaption></figure>

Samasta syystä kiehuva vesi pysyy $100\,{}^\circ\text{C}$:ssa, vaikka liesi on täysillä: siirtyvä energia höyrystää vettä eikä nosta sen lämpötilaa. Höyry vie noin 1700 kertaa enemmän tilaa kuin vesi, joten laajetessaan se työntää ympäröivää ilmaa. Pieni osa höyrystämiseen tarvittavasta energiasta kuluu tähän työhön, ja suurin osa kasvattaa molekyylien välistä vuorovaikutusenergiaa. Mitä suurempi teho, sitä nopeammin vesi kiehuu pois, mutta ei sitä kuumemmaksi. Veden höyrystyessä sitoutunut energia vapautuu takaisin, kun höyry tiivistyy, ja siksi 100-asteinen höyry polttaa pahemmin kuin 100-asteinen vesi.

```pysahdy
Kattilassa vesi kiehuu. Liesi säädetään suuremmalle teholle. Mitä veden lämpötilalle tapahtuu?
---
Lämpötila ei muutu vaan pysyy noin $100\,{}^\circ\text{C}$:ssa. Suurempi teho höyrystää veden nopeammin.
```

Sulamiseen ja höyrystymiseen tarvittava lämpömäärä on suoraan verrannollinen massaan. Kertoimet ovat aineelle ominaisia: ominaissulamislämpö $s$ kertoo, kuinka paljon energiaa yhden kilogramman sulattaminen vaatii, ja ominaishöyrystymislämpö $r$, kuinka paljon yhden kilogramman höyrystäminen vaatii. Vedelle $s = 334\,\text{kJ/kg}$ ja $r = 2260\,\text{kJ/kg}$. Höyrystäminen vaatii siis lähes seitsemän kertaa enemmän energiaa kuin sulattaminen ja yli viisi kertaa enemmän kuin veden lämmittäminen $0\,{}^\circ\text{C}$:sta $100\,{}^\circ\text{C}$:seen.

```pysahdy
Veden ominaissulamislämpö on $s = 334\,\text{kJ/kg}$. Kuinka paljon energiaa tarvitaan $0{,}50\,\text{kg}$:n jään sulattamiseen?
---
Energia on verrannollinen massaan, joten tarvitaan $0{,}50\,\text{kg} \cdot 334\,\text{kJ/kg} = 167\,\text{kJ}$.
```

Kiehumispiste riippuu paineesta. Faasikaavio esittää, missä olomuodossa aine on kussakin lämpötilassa ja paineessa: sen käyrät yhdistävät sulamis-, kiehumis- ja sublimoitumispisteet eri paineissa. Vuorella, jossa ilmanpaine on pienempi, vesi kiehuu alle $100\,{}^\circ\text{C}$:n lämpötilassa, ja painekattilassa paine nostaa kiehumispisteen yli $100\,{}^\circ\text{C}$:n, jolloin ruoka kypsyy nopeammin.

<svg data-fig="phase-diagram" viewBox="0 0 600 350" role="img" aria-label="Faasikaavio, kaavakuva: paine p lämpötilan T funktiona. Käyrät erottavat kiinteän, nesteen ja kaasun alueet ja kohtaavat kolmoispisteessä. Kun paine on ilmanpaine, vesi kiehuu 100 asteessa; vuorella paine on pienempi ja kiehumispiste alempi." style="max-width:100%;font-size:24px">
  <line x1="95" y1="296" x2="490" y2="296" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M502,296 L489,302 L489,290 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="297" x2="96" y2="42" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,30 L102,43 L90,43 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="508" y="281.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T$</div></foreignObject>
  <foreignObject x="86" y="-0.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p$</div></foreignObject>
  <polygon points="96,296 100,296 103.5,296 107.5,296 111,295.5 115,295.5 119,295 122.5,295 126.5,294.5 130,294 134,293.5 138,293 141.5,292 145.5,291.5 149,290.5 153,289.5 157,289 160.5,287.5 164.5,286.5 168,285.5 172,284 176,283 179.5,281.5 183.5,280 187,278.5 191,276.5 195,275 198.5,273 202.5,271.5 206,269.5 210,267 198.5,56 96,56" fill="#d0e6fb" fill-opacity="0.7"/>
  <polygon points="210,267 215.5,267 221,266 226.5,265 232,263.5 237.5,262 243,260.5 248.5,258.5 254,256.5 259.5,254.5 265,252 270.5,249.5 276,247 281.5,244 287,241 292.5,238 298,235 303.5,232 309,228.5 314.5,225 320,221.5 325.5,217.5 331,213.5 336.5,210 342,205.5 348,201.5 353.5,197.5 359,193 364.5,188.5 370,184 375.5,179.5 381,174.5 386.5,170 392,165 397.5,160 403,155 408.5,149.5 414,144.5 419.5,139 425,133.5 430.5,128 476,128 476,56 198.5,56 210,267" fill="#a9d1f0" fill-opacity="0.55"/>
  <polygon points="96,296 100,296 103.5,296 107.5,296 111,295.5 115,295.5 119,295 122.5,295 126.5,294.5 130,294 134,293.5 138,293 141.5,292 145.5,291.5 149,290.5 153,289.5 157,289 160.5,287.5 164.5,286.5 168,285.5 172,284 176,283 179.5,281.5 183.5,280 187,278.5 191,276.5 195,275 198.5,273 202.5,271.5 206,269.5 210,267 215.5,267 221,266 226.5,265 232,263.5 237.5,262 243,260.5 248.5,258.5 254,256.5 259.5,254.5 265,252 270.5,249.5 276,247 281.5,244 287,241 292.5,238 298,235 303.5,232 309,228.5 314.5,225 320,221.5 325.5,217.5 331,213.5 336.5,210 342,205.5 348,201.5 353.5,197.5 359,193 364.5,188.5 370,184 375.5,179.5 381,174.5 386.5,170 392,165 397.5,160 403,155 408.5,149.5 414,144.5 419.5,139 425,133.5 430.5,128 476,128 476,296 96,296" fill="#ffc078" fill-opacity="0.5"/>
  <polyline points="96,296 100,296 103.5,296 107.5,296 111,295.5 115,295.5 119,295 122.5,295 126.5,294.5 130,294 134,293.5 138,293 141.5,292 145.5,291.5 149,290.5 153,289.5 157,289 160.5,287.5 164.5,286.5 168,285.5 172,284 176,283 179.5,281.5 183.5,280 187,278.5 191,276.5 195,275 198.5,273 202.5,271.5 206,269.5 210,267" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="210,267 215.5,267 221,266 226.5,265 232,263.5 237.5,262 243,260.5 248.5,258.5 254,256.5 259.5,254.5 265,252 270.5,249.5 276,247 281.5,244 287,241 292.5,238 298,235 303.5,232 309,228.5 314.5,225 320,221.5 325.5,217.5 331,213.5 336.5,210 342,205.5 348,201.5 353.5,197.5 359,193 364.5,188.5 370,184 375.5,179.5 381,174.5 386.5,170 392,165 397.5,160 403,155 408.5,149.5 414,144.5 419.5,139 425,133.5 430.5,128" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="210,267 198.5,56" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="368" y1="185.5" x2="368" y2="296" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="185.5" x2="368" y2="185.5" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="368" cy="185.5" r="6.5" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="382" y="179" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ilmanpaine}$</div></foreignObject>
  <line x1="308.5" y1="229" x2="308.5" y2="296" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="96" y1="229" x2="308.5" y2="229" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="308.5" cy="229" r="6.5" fill="#c92a2a" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="322.5" y="222.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{vuori}$</div></foreignObject>
  <foreignObject x="318" y="305.5" width="100" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$100\,{}^\circ\text{C}$</div></foreignObject>
  <circle cx="210" cy="267" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="210" y1="267" x2="210" y2="296" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="140" y="305.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kolmoispiste}$</div></foreignObject>
  <foreignObject x="98" y="123" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kiinteä}$</div></foreignObject>
  <foreignObject x="281.5" y="70.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{neste}$</div></foreignObject>
  <foreignObject x="380" y="260" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kaasu}$</div></foreignObject>
</svg>

```pysahdy
Miksi ruoka kypsyy painekattilassa nopeammin kuin avoimessa kattilassa?
---
Paine nostaa kiehumispisteen yli $100\,{}^\circ\text{C}$:n, joten vesi on kuumempaa.
```

## Kaava: Sulamis- ja höyrystymislämpö
Massan $m$ sulattamiseen tai höyrystämiseen tarvittava lämpömäärä on
```kaavat
sulamislämpö :: Q = s m
höyrystymislämpö :: Q = r m
```
missä $Q$ on lämpömäärä (J), $s$ aineen ominaissulamislämpö (J/kg), $r$ ominaishöyrystymislämpö (J/kg) ja $m$ sulavan tai höyrystyvän aineen massa (kg). Sama lämpömäärä vapautuu, kun aine jähmettyy tai tiivistyy. Vakiopaineessa lämpötila ei muutu olomuodon muutoksen aikana, joten kaavassa ei ole lämpötilan muutosta $\Delta T$.

| Vesi | Arvo |
|---|---|
| $s$ | $334\,\text{kJ/kg}$ |
| $r$ | $2260\,\text{kJ/kg}$ |
| $c$ (jää) | $2100\,\text{J/(kg}\cdot\text{K)}$ |
| $c$ (vesi) | $4190\,\text{J/(kg}\cdot\text{K)}$ |
| $c$ (vesihöyry) | $2000\,\text{J/(kg}\cdot\text{K)}$ |

Taulukossa $c$ on ominaislämpökapasiteetti, joka esiteltiin luvussa *Aineen lämpeneminen ja jäähtyminen*.

Lämpenemiskäyrä näyttää lämpötilan siirretyn energian funktiona. Nousevilla osilla aine lämpenee ja pätee $Q = cm\Delta T$, vaakasuorilla osilla aine muuttaa olomuotoaan ja pätee $Q = sm$ tai $Q = rm$. Mitä pienempi ominaislämpökapasiteetti, sitä jyrkemmin lämpötila nousee, joten jään ja höyryn osat ovat noin kaksi kertaa jyrkempiä kuin veden osa:

<svg data-fig="heating-curve" viewBox="0 0 600 350" role="img" aria-label="Veden lämpenemiskäyrä, kaavakuva: lämpötila siirretyn energian Q funktiona. Jää lämpenee jyrkästi, sulaa vaakasuoralla osalla 0 asteessa (Q = sm), vesi lämpenee loivemmin 0:sta 100 asteeseen, kiehuu pitkällä vaakasuoralla osalla 100 asteessa (Q = rm) ja höyry lämpenee jyrkästi. Jään ja höyryn osien jyrkkyys on noin kaksinkertainen veden osaan verrattuna; vaakasuorien osien pituudet eivät ole mittakaavassa." style="max-width:100%;font-size:24px">
  <line x1="96" y1="237" x2="476" y2="237" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="119" x2="476" y2="119" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="296" x2="490" y2="296" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M502,296 L489,302 L489,290 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="297" x2="96" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,34 L102,47 L90,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="89" y1="237" x2="96" y2="237" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="222.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <line x1="89" y1="119" x2="96" y2="119" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="39" y="104.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$100$</div></foreignObject>
  <foreignObject x="508" y="281.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q$</div></foreignObject>
  <foreignObject x="86" y="3.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$T\ (^\circ\text{C})$</div></foreignObject>
  <polyline points="96,272.5 114,237 150,237 270,119 456,119 468,95.5" fill="none" stroke="#c92a2a" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="484" y="79" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\text{höyry}$</div></foreignObject>
  <foreignObject x="99" y="184.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\text{jää}$</span></div></foreignObject>
  <foreignObject x="156" y="242.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{sulaa}\quad Q = sm$</div></foreignObject>
  <foreignObject x="246" y="196.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{vesi}$</div></foreignObject>
  <foreignObject x="290.5" y="81" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kiehuu}\quad Q = rm$</div></foreignObject>
</svg>

## Esimerkki
Veden ominaishöyrystymislämpö määritetään kokeellisesti. Avoin kalorimetri, jossa on kiehuvaa vettä, on vaa'an päällä, ja vedessä on $1000\,\text{W}$:n uppokuumennin. Viiden minuutin ($300\,\text{s}$) aikana vaa'an lukema pienenee $128\,\text{g}$ (keksitty esimerkkiluku, ei oikean mittauksen tulos). Mikä on veden ominaishöyrystymislämpö tämän lukeman mukaan?

<!-- vaihe -->

**Tunnetut ja kysytty.** Teho $P = 1000\,\text{W}$, aika $t = 300\,\text{s}$ ja höyrystynyt massa eli vaa'an lukeman muutos $\Delta m = 128\,\text{g}$.

Vesi on kiehuvaa eli $100\,{}^\circ\text{C}$:ssa.

Kysytään ominaishöyrystymislämpöä $r$.

Oletetaan, että kuumentimen energia siirtyy kokonaan veteen.

<!-- vaihe -->

**Periaate.** Vesi kiehuu koko ajan, joten sen lämpötila ei nouse ja kaikki kuumentimen antama energia $Q = Pt$ kuluu höyrystämiseen. Höyrystymiseen tarvittava lämpömäärä on verrannollinen höyrystyneeseen massaan, $Q = r\,\Delta m$. Energia säilyy, joten nämä kaksi ovat yhtä suuret.

<!-- vaihe -->

**Kaava ratkaistuna.** Kuumentimen luovuttama lämpömäärä $Q_\text{kuum}$ on yhtä suuri kuin höyrystymiseen kuluva lämpömäärä $Q_\text{h}$. Kirjoitetaan se auki ja ratkaistaan $r$:
```latex
\begin{aligned}
&Q_\text{kuum} = Q_\text{h} \\[6pt]
&Pt = r\,\Delta m \\
&r = \frac{Pt}{\Delta m}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Vaa'an lukeman muutos muunnetaan kilogrammoiksi: $128\,\text{g} = 0{,}128\,\text{kg}$. Teho ja aika ovat jo perusyksiköissä, ja $1\,\text{W} \cdot 1\,\text{s} = 1\,\text{J}$. Lopuksi tulos muunnetaan megajouleiksi: $1\,\text{MJ} = 10^6\,\text{J}$.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan arvot yksiköineen:
```latex
\begin{aligned}
&r = \frac{Pt}{\Delta m} \\
&= \frac{1000\,\text{W} \cdot 300\,\text{s}}{0{,}128\,\text{kg}} \\
&= \frac{300\,000\,\text{J}}{0{,}128\,\text{kg}} \\
&= 2\,343\,750\,\tfrac{\text{J}}{\text{kg}}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Ominaishöyrystymislämpö on $2{,}34\,\tfrac{\text{MJ}}{\text{kg}}$. Tulos ilmoitetaan kolmella merkitsevällä numerolla, koska massan lukema $128\,\text{g}$ on annettu kolmella numerolla ja se rajoittaa tarkkuutta eniten.

<!-- vaihe -->

**Järkevyys.** Tulos $2{,}34\,\tfrac{\text{MJ}}{\text{kg}}$ on hieman taulukkoarvoa $2{,}26\,\tfrac{\text{MJ}}{\text{kg}}$ suurempi, noin $3{,}7\,\%$. Se on odotettu suunta: osa kuumentimen energiasta siirtyy astian kautta ympäröivään ilmaan eikä höyrystä vettä, joten oletus "kaikki energia veteen" antaa liian suuren $r$:n. Taulukkoarvolla höyrystyisi $\Delta m = \dfrac{Q}{r} = \dfrac{Pt}{r} = \dfrac{300\,\text{kJ}}{2260\,\tfrac{\text{kJ}}{\text{kg}}} = 0{,}133\,\text{kg}$ eli $133\,\text{g}$, vain $5\,\text{g}$ enemmän kuin mitattu, joten tulos on muutaman prosentin tarkkuudella oikea.

## Yleinen virhekäsitys
Moni luulee, että lämmön lisääminen nostaa aina lämpötilaa. Puhtaan aineen olomuodon muutoksessa vakiopaineessa lämpötila pysyy vakiona, vaikka energiaa siirtyy paljon: jään sulattaminen vaatii yhtä paljon energiaa kuin saman veden lämmittäminen $0\,{}^\circ\text{C}$:sta $80\,{}^\circ\text{C}$:seen. Toinen virhe on pitää 0-asteista jäätä ja 0-asteista vettä samanarvoisina jäähdyttäjinä. Jää viilentää juomaa paljon tehokkaammin, koska se ottaa sulaessaan paljon energiaa ennen kuin alkaa lämmetä. Kolmas virhe on ajatella, että vesi kiehuu aina $100\,{}^\circ\text{C}$:ssa: kiehumispiste riippuu paineesta.

## Tiivistelmä
- Olomuodot ovat kiinteä, neste ja kaasu. Mikromallissa olomuodon muutos muuttaa hiukkasten keskinäisiä vuorovaikutuksia: sulaessa ja höyrystyessä hiukkasten välinen vuorovaikutusenergia kasvaa, mutta molekyylien sisäiset kemialliset sidokset eivät katkea.
- Kun paine pysyy vakiona, puhtaan aineen lämpötila pysyy vakiona olomuodon muutoksen aikana. Sulattamiseen tarvitaan $Q = sm$ ja höyrystämiseen $Q = rm$; vedelle $s = 334\,\text{kJ/kg}$ ja $r = 2260\,\text{kJ/kg}$.
- Lämpenemiskäyrässä nousevat osat ovat lämpenemistä ($Q = cm\Delta T$) ja vaakasuorat osat olomuodon muutoksia.
- Kiehumispiste riippuu paineesta; faasikaavio kertoo aineen olomuodon lämpötilan ja paineen mukaan.
- Ominaishöyrystymislämpö voidaan mitata kiehuttamalla vettä uppokuumentimella vaa'an päällä: $r = Pt/\Delta m$, missä $\Delta m$ on vaa'an lukeman muutos.

<svg data-fig="scene" viewBox="0 0 600 360" role="img" aria-label="Kuvitus: järvi jäätyy alkutalvella. Rannan puolella on jo ohut jääkansi, ulompana vesi on vielä sulana, ja rannalla on ensilumi." style="max-width:100%;font-size:24px">
  <image href="pics/fy3/fy3-7-scene.webp" x="0" y="0" width="600" height="360" preserveAspectRatio="none"/>
</svg>
