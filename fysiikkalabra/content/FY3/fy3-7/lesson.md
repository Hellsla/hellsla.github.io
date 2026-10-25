# Olomuodon muutokset

> **Miksi** kiehuvan veden lämpötila ei nouse yli 100 °C:n, vaikka liesi on täysillä ja kattilaan siirtyy koko ajan energiaa?

## Ydinajatus
Aine esiintyy kolmessa olomuodossa: kiinteänä, nesteenä ja kaasuna. Mikromallin mukaan kiinteässä aineessa hiukkaset värähtelevät paikoillaan toistensa sitomina, nesteessä ne liikkuvat toistensa ohi mutta pysyvät yhdessä, ja kaasussa ne liikkuvat vapaasti ja törmäilevät vain harvoin. Olomuodon muutoksessa hiukkasten keskinäinen sidos muuttuu: sulamisessa kiinteän aineen järjestys purkautuu, ja höyrystymisessä hiukkaset irtoavat kokonaan toisistaan. Vastakkaiset muutokset ovat jähmettyminen ja tiivistyminen. Jää voi myös sublimoitua suoraan höyryksi, mitä tapahtuu pakkasella kuivuvalle pyykille.

Olomuodon muutos vaatii energiaa, mutta ei nosta lämpötilaa. Kun jäätä lämmitetään, sen lämpötila nousee 0 °C:seen asti. Sitten lämpötila pysyy vakiona, kunnes kaikki jää on sulanut, vaikka energiaa siirtyy koko ajan: energia kuluu hiukkasten sidosten purkamiseen eli hiukkasten välisen vuorovaikutusenergian kasvattamiseen, ei niiden liikkeen kiihdyttämiseen. Samasta syystä kiehuva vesi pysyy 100 °C:ssa, vaikka liesi on täysillä: kaikki siirtyvä energia kuluu veden höyrystämiseen. Mitä suurempi teho, sitä nopeammin vesi kiehuu pois, mutta ei sitä kuumemmaksi. Höyrystyessä sama energia vapautuu, kun höyry tiivistyy, ja siksi 100-asteinen höyry polttaa pahemmin kuin 100-asteinen vesi.

Sulamiseen ja höyrystymiseen tarvittava lämpömäärä on suoraan verrannollinen massaan. Kertoimet ovat aineelle ominaisia: ominaissulamislämpö s kertoo, kuinka paljon energiaa yhden kilogramman sulattaminen vaatii, ja ominaishöyrystymislämpö r, kuinka paljon yhden kilogramman höyrystäminen vaatii. Vedelle s = 334 kJ/kg ja r = 2260 kJ/kg. Höyrystäminen vaatii siis lähes seitsemän kertaa enemmän energiaa kuin sulattaminen ja yli viisi kertaa enemmän kuin veden lämmittäminen 0 °C:sta 100 °C:seen.

Kiehumispiste riippuu paineesta. Faasikaavio esittää, missä olomuodossa aine on kussakin lämpötilassa ja paineessa: sen käyrät ovat sulamis-, kiehumis- ja sublimoitumispisteet eri paineissa. Vuorella, jossa ilmanpaine on pienempi, vesi kiehuu alle 100 °C:ssa, ja painekattilassa paine nostaa kiehumispisteen yli 100 °C:n, jolloin ruoka kypsyy nopeammin.

## Kaava
Massan m sulattamiseen tai höyrystämiseen tarvittava lämpömäärä on
```latex
Q = s m \qquad \text{ja} \qquad Q = r m
```
missä Q on lämpömäärä (J), s aineen ominaissulamislämpö (J/kg), r ominaishöyrystymislämpö (J/kg) ja m sulavan tai höyrystyvän aineen massa (kg). Sama lämpömäärä vapautuu, kun aine jähmettyy tai tiivistyy. Olomuodon muutoksen aikana lämpötila ei muutu, joten kaavassa ei ole ΔT:tä.

Lämpenemiskäyrä näyttää lämpötilan siirretyn energian funktiona. Nousevilla osilla aine lämpenee ja pätee Q = cmΔT, vaakasuorilla osilla aine muuttaa olomuotoaan ja pätee Q = sm tai Q = rm:

<svg viewBox="0 0 600 300" role="img" aria-label="Veden lämpenemiskäyrä: jää lämpenee, sulaa 0 asteessa, vesi lämpenee, kiehuu 100 asteessa, höyry lämpenee; vaakasuorat osat ovat olomuodon muutoksia" style="max-width:100%;font-family:system-ui,sans-serif;font-size:20px">
  <line x1="70" y1="250" x2="580" y2="250" stroke="currentColor" stroke-width="3"/>
  <line x1="70" y1="250" x2="70" y2="30" stroke="currentColor" stroke-width="3"/>
  <polyline points="70,230 100,200 140,200 200,110 480,110 540,70" fill="none" stroke="currentColor" stroke-width="4"/>
  <line x1="70" y1="200" x2="140" y2="200" stroke="currentColor" stroke-width="1" stroke-dasharray="5 5"/>
  <line x1="70" y1="110" x2="200" y2="110" stroke="currentColor" stroke-width="1" stroke-dasharray="5 5"/>
  <text x="62" y="206" text-anchor="end" fill="currentColor">0</text>
  <text x="62" y="116" text-anchor="end" fill="currentColor">100</text>
  <text x="78" y="26" fill="currentColor">T (°C)</text>
  <text x="580" y="282" text-anchor="end" fill="currentColor">Q</text>
  <text x="120" y="190" text-anchor="middle" fill="currentColor">sulaa</text>
  <text x="340" y="100" text-anchor="middle" fill="currentColor">kiehuu, Q = rm</text>
  <text x="170" y="170" text-anchor="start" fill="currentColor">vesi lämpenee</text>
  <text x="75" y="262" text-anchor="start" font-size="17" fill="currentColor">jää</text>
  <text x="500" y="60" text-anchor="start" font-size="17" fill="currentColor">höyry</text>
</svg>

## Esimerkki
Veden ominaishöyrystymislämpö määritetään kokeellisesti. Avoin kalorimetri, jossa on kiehuvaa vettä, on vaa'an päällä, ja vedessä on 1000 W:n uppokuumennin. Viiden minuutin (300 s) aikana vaa'an lukema pienenee 128 g. Mikä on veden ominaishöyrystymislämpö tämän mittauksen mukaan?

Kuumentimen energia siirtyy kokonaan veteen: $Q = Pt = 1000\,\text{W} \cdot 300\,\text{s} = 300\,\text{kJ}$. Koska vesi kiehuu koko ajan, lämpötila ei nouse, ja kaikki energia kuluu höyrystämiseen. Höyrystynyt massa on $m = 0{,}128\,\text{kg}$, joten
```latex
r = \frac{Q}{m} = \frac{300\,\text{kJ}}{0{,}128\,\text{kg}} \approx 2{,}3\,\text{MJ/kg}
```
Tulos 2,34 MJ/kg on hieman taulukkoarvoa 2,26 MJ/kg suurempi, koska osa kuumentimen energiasta siirtyy ilmaan ja astiaan eikä höyrystä vettä. Mittaus on silti tarkka muutaman prosentin sisällä.

## Yleinen virhekäsitys
Moni luulee, että lämmön lisääminen nostaa aina lämpötilaa. Olomuodon muutoksessa lämpötila pysyy vakiona, vaikka energiaa siirtyy paljon: jään sulattaminen vaatii yhtä paljon energiaa kuin saman veden lämmittäminen 0 °C:sta 80 °C:seen. Toinen virhe on pitää 0-asteista jäätä ja 0-asteista vettä samanarvoisina jäähdyttäjinä. Jää viilentää juomaa paljon tehokkaammin, koska se ottaa sulaessaan sulamislämmön ennen kuin alkaa lämmetä. Kolmas virhe on ajatella, että vesi kiehuu aina 100 °C:ssa: kiehumispiste riippuu paineesta.

## Tiivistelmä
- Olomuodot ovat kiinteä, neste ja kaasu. Mikromallissa olomuodon muutos tarkoittaa hiukkasten välisten sidosten purkautumista tai muodostumista.
- Olomuodon muutoksen aikana lämpötila pysyy vakiona. Sulattamiseen tarvitaan $Q = sm$ ja höyrystämiseen $Q = rm$; vedelle s = 334 kJ/kg ja r = 2260 kJ/kg.
- Lämpenemiskäyrässä nousevat osat ovat lämpenemistä ($Q = cm\Delta T$) ja vaakasuorat osat olomuodon muutoksia.
- Kiehumispiste riippuu paineesta; faasikaavio kertoo aineen olomuodon lämpötilan ja paineen mukaan.
- Ominaishöyrystymislämpö voidaan mitata kiehuttamalla vettä uppokuumentimella vaa'an päällä: r = Pt/Δm.
