# Olomuodon muutokset

> **Miksi** kiehuvan veden lämpötila ei nouse yli 100 °C:n, vaikka liesi on täysillä ja kattilaan siirtyy koko ajan energiaa?

## Ydinajatus
Aine esiintyy kolmessa olomuodossa: kiinteänä, nesteenä ja kaasuna. Mikromallin mukaan kiinteässä aineessa hiukkaset värähtelevät paikoillaan toistensa sitomina, nesteessä ne liikkuvat toistensa ohi mutta pysyvät yhdessä, ja kaasussa ne liikkuvat vapaasti ja törmäilevät vain harvoin. Olomuodon muutoksessa hiukkasten keskinäinen sidos muuttuu: sulamisessa kiinteän aineen järjestys purkautuu, ja höyrystymisessä hiukkaset irtoavat kokonaan toisistaan. Vastakkaiset muutokset ovat jähmettyminen ja tiivistyminen. Jää voi myös sublimoitua suoraan höyryksi, kuten pakkasella kuivuvassa pyykissä.

<svg viewBox="0 0 600 300" role="img" aria-label="Mikromalli, kaavakuva: kiinteässä aineessa hiukkaset ovat säännöllisessä järjestyksessä toisissaan kiinni, nesteessä ne ovat epäjärjestyksessä mutta yhä kosketuksissa, kaasussa ne ovat kaukana toisistaan ja liikkuvat vapaasti. Nuolet: kiinteä sulaa nesteeksi, neste höyrystyy kaasuksi." style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
  <rect x="20" y="90" width="150" height="150" rx="6" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <rect x="225" y="90" width="150" height="150" rx="6" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <rect x="430" y="90" width="150" height="150" rx="6" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <g fill="#a9d1f0" fill-opacity="1" stroke="#2f74b5" stroke-width="2">
    <circle cx="50" cy="120" r="13"/>
    <circle cx="80" cy="120" r="13"/>
    <circle cx="110" cy="120" r="13"/>
    <circle cx="140" cy="120" r="13"/>
    <circle cx="50" cy="150" r="13"/>
    <circle cx="80" cy="150" r="13"/>
    <circle cx="110" cy="150" r="13"/>
    <circle cx="140" cy="150" r="13"/>
    <circle cx="50" cy="180" r="13"/>
    <circle cx="80" cy="180" r="13"/>
    <circle cx="110" cy="180" r="13"/>
    <circle cx="140" cy="180" r="13"/>
    <circle cx="50" cy="210" r="13"/>
    <circle cx="80" cy="210" r="13"/>
    <circle cx="110" cy="210" r="13"/>
    <circle cx="140" cy="210" r="13"/>
    <circle cx="247" cy="226" r="13"/>
    <circle cx="275" cy="224" r="13"/>
    <circle cx="303" cy="227" r="13"/>
    <circle cx="331" cy="224" r="13"/>
    <circle cx="357" cy="226" r="13"/>
    <circle cx="261" cy="200" r="13"/>
    <circle cx="289" cy="199" r="13"/>
    <circle cx="318" cy="202" r="13"/>
    <circle cx="346" cy="198" r="13"/>
    <circle cx="250" cy="174" r="13"/>
    <circle cx="278" cy="172" r="13"/>
    <circle cx="307" cy="176" r="13"/>
    <circle cx="336" cy="172" r="13"/>
    <circle cx="458" cy="118" r="13"/>
    <circle cx="545" cy="128" r="13"/>
    <circle cx="500" cy="172" r="13"/>
    <circle cx="462" cy="218" r="13"/>
    <circle cx="552" cy="212" r="13"/>
  </g>
  <g stroke="#6b7480" stroke-width="2" fill="none">
    <line x1="472" y1="123" x2="494" y2="131"/>
    <line x1="536" y1="140" x2="522" y2="160"/>
    <line x1="496" y1="185" x2="489" y2="207"/>
    <line x1="460" y1="203" x2="456" y2="179"/>
    <line x1="539" y1="220" x2="520" y2="232"/>
  </g>
  <line x1="176" y1="165" x2="208" y2="165" stroke="#e8590c" stroke-width="4"/>
  <polygon points="220,165 206,157 206,173" fill="#e8590c"/>
  <line x1="381" y1="165" x2="413" y2="165" stroke="#e8590c" stroke-width="4"/>
  <polygon points="425,165 411,157 411,173" fill="#e8590c"/>
  <text x="197" y="70" text-anchor="middle" fill="#1f2933">sulaa</text>
  <text x="402" y="70" text-anchor="middle" fill="#1f2933">höyrystyy</text>
  <text x="95" y="280" text-anchor="middle" fill="#1f2933">kiinteä</text>
  <text x="300" y="280" text-anchor="middle" fill="#1f2933">neste</text>
  <text x="505" y="280" text-anchor="middle" fill="#1f2933">kaasu</text>
</svg>

Olomuodon muutos vaatii energiaa, mutta ei nosta lämpötilaa. Kun jäätä lämmitetään, sen lämpötila nousee 0 °C:seen asti. Sitten lämpötila pysyy vakiona, kunnes kaikki jää on sulanut, vaikka energiaa siirtyy koko ajan: energia kuluu hiukkasten sidosten purkamiseen eli hiukkasten välisen vuorovaikutusenergian kasvattamiseen, ei niiden liikkeen kiihdyttämiseen. Samasta syystä kiehuva vesi pysyy 100 °C:ssa, vaikka liesi on täysillä: kaikki siirtyvä energia kuluu veden höyrystämiseen. Mitä suurempi teho, sitä nopeammin vesi kiehuu pois, mutta ei sitä kuumemmaksi. Veden höyrystyessä sitoutunut energia vapautuu takaisin, kun höyry tiivistyy, ja siksi 100-asteinen höyry polttaa pahemmin kuin 100-asteinen vesi.

Sulamiseen ja höyrystymiseen tarvittava lämpömäärä on suoraan verrannollinen massaan. Kertoimet ovat aineelle ominaisia: ominaissulamislämpö $s$ kertoo, kuinka paljon energiaa yhden kilogramman sulattaminen vaatii, ja ominaishöyrystymislämpö $r$, kuinka paljon yhden kilogramman höyrystäminen vaatii. Vedelle $s = 334\,\text{kJ/kg}$ ja $r = 2260\,\text{kJ/kg}$. Höyrystäminen vaatii siis lähes seitsemän kertaa enemmän energiaa kuin sulattaminen ja yli viisi kertaa enemmän kuin veden lämmittäminen 0 °C:sta 100 °C:seen.

Kiehumispiste riippuu paineesta. Faasikaavio esittää, missä olomuodossa aine on kussakin lämpötilassa ja paineessa: sen käyrät yhdistävät sulamis-, kiehumis- ja sublimoitumispisteet eri paineissa. Vuorella, jossa ilmanpaine on pienempi, vesi kiehuu alle 100 °C:n lämpötilassa, ja painekattilassa paine nostaa kiehumispisteen yli 100 °C:n, jolloin ruoka kypsyy nopeammin.

## Kaava: Sulamis- ja höyrystymislämpö
Massan $m$ sulattamiseen tai höyrystämiseen tarvittava lämpömäärä on
```latex
Q = s m \qquad \text{ja} \qquad Q = r m
```
missä $Q$ on lämpömäärä (J), $s$ aineen ominaissulamislämpö (J/kg), $r$ ominaishöyrystymislämpö (J/kg) ja $m$ sulavan tai höyrystyvän aineen massa (kg). Sama lämpömäärä vapautuu, kun aine jähmettyy tai tiivistyy. Vakiopaineessa lämpötila ei muutu olomuodon muutoksen aikana, joten kaavassa ei ole lämpötilan muutosta $\Delta T$.

| Vesi | Arvo |
|---|---|
| $s$ | 334 kJ/kg |
| $r$ | 2260 kJ/kg |
| $c$ (jää) | 2100 J/(kg·K) |
| $c$ (vesi) | 4190 J/(kg·K) |
| $c$ (vesihöyry) | 2000 J/(kg·K) |

Taulukossa $c$ on ominaislämpökapasiteetti, joka esiteltiin luvussa ”Aineen lämpeneminen ja jäähtyminen”.

Lämpenemiskäyrä näyttää lämpötilan siirretyn energian funktiona. Nousevilla osilla aine lämpenee ja pätee $Q = cm\Delta T$, vaakasuorilla osilla aine muuttaa olomuotoaan ja pätee $Q = sm$ tai $Q = rm$. Mitä pienempi ominaislämpökapasiteetti, sitä jyrkemmin lämpötila nousee, joten jään ja höyryn osat ovat noin kaksi kertaa jyrkempiä kuin veden osa:

<svg viewBox="0 0 600 300" role="img" aria-label="Veden lämpenemiskäyrä, kaavakuva: jää lämpenee jyrkästi, sulaa 0 asteessa, vesi lämpenee loivemmin, kiehuu 100 asteessa pitkään ja höyry lämpenee jyrkästi; vaakasuorat osat ovat olomuodon muutoksia, joissa Q = sm ja Q = rm" style="max-width:100%;font-family:system-ui,sans-serif;font-size:24px">
  <line x1="70" y1="250" x2="580" y2="250" stroke="#1f2933" stroke-width="3"/>
  <line x1="70" y1="250" x2="70" y2="40" stroke="#1f2933" stroke-width="3"/>
  <polyline points="70,197 80,170 132,170 197,80 548,80 560,44" fill="none" stroke="#c92a2a" stroke-width="4"/>
  <line x1="70" y1="170" x2="132" y2="170" stroke="#6b7480" stroke-width="1" stroke-dasharray="5 5"/>
  <line x1="70" y1="80" x2="197" y2="80" stroke="#6b7480" stroke-width="1" stroke-dasharray="5 5"/>
  <text x="62" y="178" text-anchor="end" fill="#1f2933">0</text>
  <text x="62" y="88" text-anchor="end" fill="#1f2933">100</text>
  <text x="80" y="30" fill="#1f2933">T (°C)</text>
  <foreignObject x="530" y="256" width="50" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$Q$</div></foreignObject>
  <text x="84" y="200" text-anchor="start" fill="#1f2933">sulaa</text>
  <foreignObject x="156" y="180" width="100" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$Q = sm$</div></foreignObject>
  <text x="182" y="152" text-anchor="start" fill="#1f2933">vesi lämpenee</text>
  <text x="284" y="68" text-anchor="start" fill="#1f2933">kiehuu</text>
  <foreignObject x="370" y="42" width="100" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex">$Q = rm$</div></foreignObject>
  <text x="80" y="240" text-anchor="start" fill="#1f2933">jää</text>
  <text x="545" y="36" text-anchor="end" fill="#1f2933">höyry</text>
</svg>

## Esimerkki
Veden ominaishöyrystymislämpö määritetään kokeellisesti. Avoin kalorimetri, jossa on kiehuvaa vettä, on vaa'an päällä, ja vedessä on 1000 W:n uppokuumennin. Viiden minuutin (300 s) aikana vaa'an lukema pienenee 128 g. Mikä on veden ominaishöyrystymislämpö tämän mittauksen mukaan?

<!-- vaihe -->

**Tunnetut ja kysytty.** Teho $P = 1000\,\text{W}$, aika $t = 300\,\text{s}$ ja höyrystynyt massa eli vaa'an lukeman muutos $\Delta m = 128\,\text{g} = 0{,}128\,\text{kg}$. Kysytään ominaishöyrystymislämpöä $r$. Oletetaan, että kuumentimen energia siirtyy kokonaan veteen.

<!-- vaihe -->

**Kaava ratkaistuna.** Vesi kiehuu koko ajan, joten lämpötila ei nouse, ja kaikki kuumentimen energia $Q = Pt$ kuluu höyrystämiseen, $Q = r\,\Delta m$. Siis $Pt = r\,\Delta m$, josta
```latex
r = \frac{Pt}{\Delta m}
```

<!-- vaihe -->

**Sijoitus.** Sijoitetaan arvot yksiköineen:
```latex
\begin{aligned}
&r = \frac{Pt}{\Delta m} \\
&= \frac{1000\,\text{W} \cdot 300\,\text{s}}{0{,}128\,\text{kg}} \\
&= \frac{300\,\text{kJ}}{0{,}128\,\text{kg}} \\
&\approx 2{,}34\,\text{MJ/kg}
\end{aligned}
```

<!-- vaihe -->

**Järkevyys.** Tulos 2,34 MJ/kg on hieman taulukkoarvoa 2,26 MJ/kg suurempi, koska oletus ei pidä täysin paikkaansa. Astia ei enää lämpene, koska vesi on jo kiehumispisteessä, mutta osa kuumentimen energiasta siirtyy astian kautta ympäröivään ilmaan eikä höyrystä vettä. Tulos on silti muutaman prosentin tarkkuudella oikea.

## Yleinen virhekäsitys
Moni luulee, että lämmön lisääminen nostaa aina lämpötilaa. Olomuodon muutoksessa lämpötila pysyy vakiona, vaikka energiaa siirtyy paljon: jään sulattaminen vaatii yhtä paljon energiaa kuin saman veden lämmittäminen 0 °C:sta 80 °C:seen. Toinen virhe on pitää 0-asteista jäätä ja 0-asteista vettä samanarvoisina jäähdyttäjinä. Jää viilentää juomaa paljon tehokkaammin, koska se ottaa sulaessaan paljon energiaa ennen kuin alkaa lämmetä. Kolmas virhe on ajatella, että vesi kiehuu aina 100 °C:ssa: kiehumispiste riippuu paineesta.

## Tiivistelmä
- Olomuodot ovat kiinteä, neste ja kaasu. Mikromallissa olomuodon muutos tarkoittaa hiukkasten välisten sidosten purkautumista tai muodostumista.
- Olomuodon muutoksen aikana lämpötila pysyy vakiona. Sulattamiseen tarvitaan $Q = sm$ ja höyrystämiseen $Q = rm$; vedelle $s = 334\,\text{kJ/kg}$ ja $r = 2260\,\text{kJ/kg}$.
- Lämpenemiskäyrässä nousevat osat ovat lämpenemistä ($Q = cm\Delta T$) ja vaakasuorat osat olomuodon muutoksia.
- Kiehumispiste riippuu paineesta; faasikaavio kertoo aineen olomuodon lämpötilan ja paineen mukaan.
- Ominaishöyrystymislämpö voidaan mitata kiehuttamalla vettä uppokuumentimella vaa'an päällä: $r = Pt/\Delta m$, missä $\Delta m$ on vaa'an lukeman muutos.
