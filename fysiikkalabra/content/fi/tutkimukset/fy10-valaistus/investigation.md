# Valaistus­voimakkuuden riippuvuus etäisyydestä

> **Tutkimuskysymys:** Miten lampun aiheuttama valaistusvoimakkuus riippuu etäisyydestä lamppuun, ja vastaako riippuvuus teoriasta odotettavaa mallia?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: pimennetyssä huoneessa pöydällä palaa pieni kirkas lamppu telineessään. Samalla korkeudella on valoanturi omassa telineessään, ja sen herkkä pinta on suunnattu lamppua kohti. Pöydän reunalla on mittatikku, joka ulottuu lampun kohdalta anturin ohi. Anturin johto kulkee pöydällä olevaan mittauslaitteeseen, ja vieressä on vihko." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy10vh-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1f2933"/><stop offset="1" stop-color="#6b7480"/></linearGradient><linearGradient id="fy10vh-desk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient><radialGradient id="fy10vh-glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#f1dfb5"/><stop offset="0.55" stop-color="#ffc078" stop-opacity="0.8"/><stop offset="1" stop-color="#ffc078" stop-opacity="0"/></radialGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy10vh-wall)"/>
  <rect x="0" y="440" width="1200" height="160" fill="url(#fy10vh-desk)"/>
  <line x1="0" y1="462" x2="1200" y2="458" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="484" x2="1200" y2="480" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="506" x2="1200" y2="502" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="528" x2="1200" y2="524" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="550" x2="1200" y2="546" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="572" x2="1200" y2="568" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="440" x2="1200" y2="440" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="250" cy="270" r="230" fill="url(#fy10vh-glow)"/>
  <rect x="190" y="426" width="120" height="16" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="243" y="310" width="14" height="118" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="250" cy="266" r="34" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M240.5,284.5 L240.5,266 L245,261 L250,266 L255,261 L259.5,266 L259.5,284.5" fill="none" stroke="#1f2933" stroke-width="1.8" stroke-linejoin="round"/>
  <rect x="233" y="295" width="34" height="18.5" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="720" y="426" width="100" height="16" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="763" y="300" width="14" height="128" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="756" y="234" width="32" height="64" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="750" y="245.5" width="8" height="41" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M788,280 C840,300 820,400 900,410" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="890" y="390" width="150" height="52" rx="6" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="904" y="400" width="90" height="32" rx="3" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <circle cx="1016" cy="416" r="8" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="220" y="470" width="640" height="26" rx="3" fill="#ffe8a3" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="230" y1="470" x2="230" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="240" y1="470" x2="240" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="250" y1="470" x2="250" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="260" y1="470" x2="260" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="270" y1="470" x2="270" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="280" y1="470" x2="280" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="290" y1="470" x2="290" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="300" y1="470" x2="300" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="310" y1="470" x2="310" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320" y1="470" x2="320" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="330" y1="470" x2="330" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="340" y1="470" x2="340" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="350" y1="470" x2="350" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="360" y1="470" x2="360" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="370" y1="470" x2="370" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="470" x2="380" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="390" y1="470" x2="390" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="400" y1="470" x2="400" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="410" y1="470" x2="410" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="470" x2="420" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="470" x2="430" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="440" y1="470" x2="440" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="450" y1="470" x2="450" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="460" y1="470" x2="460" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="470" x2="470" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="470" x2="480" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="490" y1="470" x2="490" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="500" y1="470" x2="500" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="510" y1="470" x2="510" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="520" y1="470" x2="520" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="530" y1="470" x2="530" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="540" y1="470" x2="540" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="550" y1="470" x2="550" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="560" y1="470" x2="560" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="570" y1="470" x2="570" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="580" y1="470" x2="580" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="590" y1="470" x2="590" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="600" y1="470" x2="600" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="610" y1="470" x2="610" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="620" y1="470" x2="620" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="630" y1="470" x2="630" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="640" y1="470" x2="640" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="650" y1="470" x2="650" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="660" y1="470" x2="660" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="670" y1="470" x2="670" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="680" y1="470" x2="680" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="690" y1="470" x2="690" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="700" y1="470" x2="700" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="710" y1="470" x2="710" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="720" y1="470" x2="720" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="730" y1="470" x2="730" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="740" y1="470" x2="740" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="750" y1="470" x2="750" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="760" y1="470" x2="760" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="770" y1="470" x2="770" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="780" y1="470" x2="780" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="790" y1="470" x2="790" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="800" y1="470" x2="800" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="810" y1="470" x2="810" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="820" y1="470" x2="820" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="830" y1="470" x2="830" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="840" y1="470" x2="840" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="850" y1="470" x2="850" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="860" y1="470" x2="860" y2="475" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <g transform="translate(1040,535) rotate(-5)"><rect x="-90" y="-34" width="190" height="66" rx="4" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/><line x1="-74" y1="-18" x2="84" y2="-18" stroke="#6b7480" stroke-width="1.5" stroke-opacity="0.6"/><line x1="-74" y1="-6" x2="84" y2="-6" stroke="#6b7480" stroke-width="1.5" stroke-opacity="0.6"/><line x1="-74" y1="6" x2="84" y2="6" stroke="#6b7480" stroke-width="1.5" stroke-opacity="0.6"/><line x1="-74" y1="18" x2="84" y2="18" stroke="#6b7480" stroke-width="1.5" stroke-opacity="0.6"/><line x1="-74" y1="30" x2="84" y2="30" stroke="#6b7480" stroke-width="1.5" stroke-opacity="0.6"/></g>
</svg>

Lukulamppu valaisee kirjan sivun kirkkaasti, kun se on lähellä, mutta huoneen toisella puolella sen valossa on vaikea lukea. Tässä tutkimuksessa selvität mittaamalla, millä tavalla valaistusvoimakkuus pienenee etäisyyden kasvaessa, muodostat tuloksista matemaattisen mallin ja vertaat sitä malliin, jonka voi päätellä valon etenemisestä. Mittaa, piirrä ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** miten valaistusvoimakkuus riippuu etäisyydestä lamppuun, millainen matemaattinen malli kuvaa mittaustuloksia, ja vastaako malli epävarmuuksien rajoissa teoriasta odotettavaa riippuvuutta.

**Päätät itse (osittain ohjattu ja itsenäinen työtapa):** käytettävät etäisyydet ja niiden määrän, sen, mistä kohdista etäisyys mitataan, miten huomioit huoneen muun valaistuksen, miten luet vaihtelevan lukeman, millaisella kuvaajalla tai sovituksella testaat mallia perusteluineen sekä tavan, jolla arvioit tuloksen epävarmuuden. Osittain ohjatussa työtavassa sivu antaa näihin vaihtoehtoja ja tukea, itsenäisessä työtavassa perustelet valintasi itse. Ohjatussa työtavassa et tee näitä valintoja: sivu kiinnittää mittausjärjestelyn ja kuvaajan ja antaa valmiit tavat epävarmuuden arviointiin.

::: tuki I
**Itsenäinen työtapa.** Laajennus, etäisyyden nollakohdan määrittäminen kuvaajasta, kuuluu työhösi: kerro, muuttaako se johtopäätöstäsi mallin sopivuudesta.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Jos etäisyys lamppuun kaksinkertaistuu, mitä arvelet tapahtuvan valaistusvoimakkuudelle? Puolittuuko se, vai muuttuuko se jotenkin muuten?
2. Millainen on kuvaaja, jossa pystyakselilla on valaistusvoimakkuus ja vaaka-akselilla etäisyys? Voiko kuvaajan muodosta suoraan päätellä, millainen riippuvuus on?
3. Miten huoneen muu valaistus vaikuttaa lukemiin lähellä lamppua ja kaukana lampusta?
4. Millä etäisyyksillä arvelet yksinkertaisen mallin toimivan huonoimmin, ja miksi?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Teoriaa lyhyesti

**Valaistusvoimakkuus** $E$ kertoo, kuinka paljon valoa osuu pinnalle pinta-alayksikköä kohti. Sen yksikkö on luksi, $\text{lx}$. Valaistusvoimakkuusanturi mittaa sitä valoa, joka osuu sen herkälle pinnalle.

Pienestä valonlähteestä valo etenee suoraviivaisesti joka suuntaan. Kun valo etenee kauemmas, sama valo leviää yhä suuremmalle alalle, eikä sitä katoa matkalla eikä tule lisää. Tarkastellaan kapeaa, lampusta lähtevää valokeilaa: etäisyydellä $r$ se valaisee pinnan, jonka ala on $A$. Mieti, kuinka suuren alan sama keila valaisee kaksinkertaisella etäisyydellä, kun keilan reunat ovat suoria. Päättele tästä, miten valaistusvoimakkuuden pitäisi riippua etäisyydestä, ja kirjaa malli työselostukseen hypoteesiksi.

Periaate pätee, kun nämä ehdot ovat voimassa:

- Valonlähde on pistemäinen: etäisyys on paljon suurempi kuin lampun valaisevan osan koko.
- Ilma ei juuri absorboi valoa, ja lampun valo pysyy samana koko mittauksen ajan.
- Anturiin osuu vain lampusta suoraan tuleva valo. Seinistä ja pöydästä heijastunut valo ja huoneen muu valaistus eivät kuulu malliin, vaan ne on huomioitava erikseen.
- Anturin herkkä pinta on kohtisuorassa valon tulosuuntaan nähden, ja anturi on aina samassa suunnassa lampusta katsottuna.

Lampun ei tarvitse säteillä yhtä voimakkaasti joka suuntaan: kun mitataan aina samassa suunnassa, samaan keilaan lähtenyt valo leviää kauempana yhtä lailla. Heijastin tai linssi sen sijaan muuttaa valon kulkusuuntia, jolloin valo näyttää tulevan jostain muualta kuin pienestä hehkuvasta osasta. Silloin etäisyys valon näennäiseen lähtökohtaan ei ole se, minkä mittaat, ja malli toimii huonoimmin lähellä lamppua. Siksi tutkimuksessa käytetään lamppua, jossa ei ole heijastinta eikä linssiä.

::: tuki O OO
Tarkista päättelysi tästä.

<svg data-fig="spread" viewBox="0 0 600 380" role="img" aria-label="Kaaviokuva. Pistemäisestä valonlähteestä lähtevä valo kulkee suorina viivoina. Etäisyydellä r se valaisee neliön, jonka pinta-ala on A. Kaksinkertaisella etäisyydellä 2r sama valo leviää neliöön, jonka sivu on kaksinkertainen ja pinta-ala neljä kertaa suurempi, 4A. Suurempi neliö on jaettu neljään A:n kokoiseen osaan." style="max-width:100%;font-size:24px">
  <path d="M458,232 L458,92 L402,148 L402,288 Z" fill="#ffc078" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" fill-opacity="0.45"/>
  <line x1="458" y1="162" x2="402" y2="218" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="260" x2="430" y2="120" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="50" y1="190" x2="458" y2="232" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="50" y1="190" x2="458" y2="92" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="50" y1="190" x2="402" y2="148" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="50" y1="190" x2="402" y2="288" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <path d="M254,211 L254,141 L226,169 L226,239 Z" fill="#ffc078" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round" fill-opacity="0.85"/>
  <circle cx="50" cy="190" r="7" fill="#1f2933"/>
  <foreignObject x="248" y="110.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A$</div></foreignObject>
  <foreignObject x="494" y="85.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$4A$</div></foreignObject>
  <line x1="50" y1="326" x2="240" y2="326" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="50" y1="317" x2="50" y2="335" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="240" y1="317" x2="240" y2="335" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="250" y="311.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$r$</div></foreignObject>
  <line x1="50" y1="360" x2="430" y2="360" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="50" y1="351" x2="50" y2="369" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="430" y1="351" x2="430" y2="369" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="440" y="345.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$2r$</div></foreignObject>
  <line x1="50" y1="202" x2="50" y2="352" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
</svg>

Keilan reunat ovat suoria, joten kaksinkertaisella etäisyydellä valaistun neliön kumpikin sivu on kaksinkertainen ja pinta-ala nelinkertainen, $4A$. Sama valo jakautuu nelinkertaiselle alalle, joten valaistusvoimakkuus on neljäsosa. Yleisesti valaistu ala on verrannollinen etäisyyden neliöön $r^2$, joten valaistusvoimakkuus on kääntäen verrannollinen etäisyyden neliöön:

```latex
E = \frac{I}{r^2}
```

missä $E$ on valaistusvoimakkuus, $r$ etäisyys valonlähteestä ja $I$ lampun **valovoima** tähän suuntaan. Valovoima kertoo, kuinka voimakkaasti lamppu säteilee valoa siihen suuntaan, jossa anturi on. Sen yksikkö on kandela, $\text{cd} = \text{lx}\cdot\text{m}^2$. Tätä riippuvuutta kutsutaan **käänteisen neliön laiksi**. Saman voi sanoa myös näin: tulo $E\cdot r^2$ pysyy vakiona.

Malli pätee vain edellä lueteltujen ehtojen voimassa ollessa. Jos anturiin osuu lisäksi taustavaloa, jonka valaistusvoimakkuus on $E_\text{tausta}$, anturi näyttää summan $\dfrac{I}{r^2} + E_\text{tausta}$.
:::

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, mitä muutat, mitä mittaat ja mitä pidät vakiona. Mieti myös, miten huomioit huoneen muun valaistuksen ja miten pidät lampun ja anturin asennon samana kaikissa mittauksissa.

::: tuki O
**Ohjattu.** Muutat etäisyyttä $r$ lampun valaisevasta osasta anturin herkkään pintaan ja mittaat jokaisella etäisyydellä valaistusvoimakkuuden. Pidät lampun, anturin korkeuden ja asennon sekä huoneen valaistuksen samoina. Pimennä huone niin hyvin kuin pystyt.

<svg data-fig="setup" viewBox="0 0 600 320" role="img" aria-label="Kaaviokuva. Vasemmalla on lamppu telineessään ja oikealla valoanturi telineessään samalla korkeudella. Anturin herkkä pinta on kohtisuorassa lampun ja anturin väliseen suoraan nähden. Etäisyys r mitataan lampun hehkulangasta anturin herkkään pintaan." style="max-width:100%;font-size:24px">
  <rect x="50" y="278" width="100" height="14" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="93" y="198" width="14" height="82" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="430" y="278" width="100" height="14" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="475" y="192" width="14" height="88" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <circle cx="100" cy="160" r="28" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M92,175.5 L92,160 L96,156 L100,160 L104,156 L108,160 L108,175.5" fill="none" stroke="#1f2933" stroke-width="1.8" stroke-linejoin="round"/>
  <rect x="86" y="184" width="28" height="15.5" rx="2" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="468" y="128" width="32" height="64" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="462" y="139.5" width="8" height="41" rx="2" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="100" y1="160" x2="460" y2="160" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="100" y1="128" x2="100" y2="70" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="462" y1="138" x2="462" y2="70" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="4 4"/>
  <line x1="100" y1="80" x2="462" y2="80" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="100" y1="70" x2="100" y2="90" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="462" y1="70" x2="462" y2="90" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="271" y="43.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="58.5" y="291.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{lamppu}$</div></foreignObject>
  <foreignObject x="438.5" y="291.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{anturi}$</div></foreignObject>
  <foreignObject x="176.5" y="174" width="247" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\text{herkkä pinta lamppua kohti}$</div></foreignObject>
</svg>

Aseta lamppu ja anturi samalle korkeudelle niin, että anturin herkkä pinta osoittaa suoraan lamppua kohti. Mittaa etäisyys hehkulangasta tai LED-sirusta anturin herkkään pintaan. Käytä ainakin kahdeksaa etäisyyttä niin, että pienin etäisyys on ainakin kymmenen kertaa lampun valaisevan osan koko ja suurin ainakin neljä kertaa pienin. Tihennä mittauksia lähellä lamppua, koska siellä valaistusvoimakkuus muuttuu nopeimmin.

Mittaa jokaisella etäisyydellä kaksi lukemaa: ensin lamppu päällä ja sitten lamppu sammutettuna. Odota sammuttamisen jälkeen, että lukema asettuu. Jälkimmäinen lukema on taustavalon valaistusvoimakkuus $E_\text{tausta}$ juuri siinä kohdassa. Se poistaa vain huoneen muun valon. Lampun oma valo, joka heijastuu seinistä, pöydästä ja muista pinnoista, jää lukemiin systemaattiseksi virheeksi. Se suurentaa eniten kaukaisia lukemia, joissa lampusta suoraan tuleva valo on heikointa, joten pidä vaaleat pinnat kaukana lampusta ja anturista.
:::

::: tuki OO
**Osittain ohjattu.** Muuttuja on etäisyys lamppuun. Päätä itse, mitä etäisyyksiä käytät ja montako, mistä kohdista lamppua ja anturia mittaat etäisyyden ja miten huomioit taustavalon. Kirjaa päätöksesi perusteluineen.
:::

::: tuki O OO
Mieti ainakin näitä:

- Mistä kohdasta lamppua valo oikeastaan lähtee, ja missä kohdassa anturia on sen herkkä pinta?
- Kuinka lähelle lamppua voit mennä, jotta lamppu on vielä pistemäinen? Kuinka kauas voit mennä, ennen kuin lampun valo hukkuu taustavaloon?
- Miten saat selville, kuinka paljon taustavaloa osuu anturiin? Onko se sama joka kohdassa?
- Mitä tapahtuu, jos anturi on lähellä lamppua mittausalueensa ylärajalla? Jos lukema ei muutu, kun siirrät anturia hieman lähemmäs, anturi ei enää pysty mittaamaan suurempaa valaistusvoimakkuutta.
:::

## Mittaa

Kirjaa alkuperäiset mittaustulokset taulukkoon heti mittauksen aikana. Laskemasi suureet saavat omat sarakkeensa mitattujen oikealle puolelle.

::: tuki O
Voit käyttää esimerkiksi tällaista taulukkoa:

| $r\ (\text{m})$ | $E_\text{kok}\ (\text{lx})$, lamppu päällä | $E_\text{tausta}\ (\text{lx})$, lamppu pois | $E = E_\text{kok} - E_\text{tausta}\ (\text{lx})$ | $\dfrac{1}{r^2}\ \left(\dfrac{1}{\text{m}^2}\right)$ |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

Jos lukema vaihtelee, odota hetki ja kirjaa lukema, jonka ympärillä se vaihtelee, sekä arvio vaihtelun suuruudesta. Pysy itse samassa paikassa joka mittauksessa, ettei varjosi tai vaatteistasi heijastuva valo muuta lukemaa.
:::

Muista mittausepävarmuus: kirjaa, kuinka tarkasti luet etäisyyden ja kuinka paljon valaistusvoimakkuuden lukema vaihtelee. [[apua:fy1-3|Mittausepävarmuuden arvioiminen]]

## Käsittele tulokset

Muodosta mittaustuloksista matemaattinen malli: valitse kuvaaja tai sovitus, josta voit päätellä, noudattavatko tulokset päättelemääsi riippuvuutta. Merkitse akseleille suureet ja yksiköt. Piirrä mittauspisteet, älä yhdistä niitä murtoviivalla. [[apua:fy1-4|Suoran sovittaminen ja kulmakertoimen tulkinta]]

::: tuki O
Piirrä ensin kuvaaja, jossa pystyakselilla on valaistusvoimakkuus $E$ ja vaaka-akselilla etäisyys $r$, ja katso sen muotoa. Piirrä sitten kuvaaja, jossa pystyakselilla on taustavalolla korjattu valaistusvoimakkuus $E$ ja vaaka-akselilla $\dfrac{1}{r^2}$, ja sovita pisteisiin suora.
:::

Vastaa:

1. Miltä näyttää kuvaaja, jossa valaistusvoimakkuus on etäisyyden funktiona? Miksi sen muodosta on vaikea päätellä, onko riippuvuus juuri päättelemäsi kaltainen?
2. Millä kuvaajalla tai sovituksella testasit mallia, ja miksi sen avulla mallin sopivuus näkyy?
3. Noudattavatko pisteet mallia koko mittausalueella? Jos eivät, millä etäisyyksillä ne poikkeavat, ja mihin suuntaan?
4. Mikä on mallisi vakio, mikä on sen yksikkö ja mitä se kertoo lampusta?

::: tuki O OO
**Miksi juuri nämä akselit?** Etäisyyden funktiona valaistusvoimakkuus pienenee kaarevasti, ja monet eri riippuvuudet näyttävät samankaltaisilta kaarilta. Siksi mallia on vaikea testata siitä kuvaajasta. Malli $E = \dfrac{I}{r^2}$ on suoran yhtälö $y = kx$, kun pystyakselille valitaan $E$ ja vaaka-akselille $\dfrac{1}{r^2}$. Jos malli pätee, pisteet ovat origon kautta kulkevalla suoralla, ja kulmakerroin on valovoima $I$. Jos taustavaloa ei ole vähennetty ja se on joka kohdassa yhtä suuri, suora nousee taustavalon verran ylemmäs: kulmakerroin pysyy samana, mutta suora leikkaa pystyakselin kohdassa $E_\text{tausta}$.

<svg data-fig="model" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja: valaistusvoimakkuus E etäisyyden neliön käänteisarvon, yksi per r toiseen, funktiona mallin mukaan. Kun taustavalo on vähennetty, kuvaaja on origon kautta kulkeva suora, jonka kulmakerroin on valovoima I. Kun taustavaloa ei ole vähennetty, kuvaaja on samansuuntainen suora, joka leikkaa pystyakselin taustavalon valaistusvoimakkuuden kohdalla. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="119" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="120" y1="291" x2="120" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M120,24 L126,37 L114,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="90" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="275.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$1/r^2$</div></foreignObject>
  <foreignObject x="110" y="-6.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E$</div></foreignObject>
  <polyline points="120,290 452.5,107.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="120,247 452.5,64.5" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <foreignObject x="29" y="235" width="81" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:20px;color:#6b7480">$E_\text{tausta}$</div></foreignObject>
  <line x1="114" y1="247" x2="120" y2="247" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="141" y="74" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{taustavalo mukana}$</div></foreignObject>
  <foreignObject x="309" y="222.5" width="258" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{taustavalo vähennetty}$</div></foreignObject>
  <foreignObject x="365" y="170" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kulmakerroin } I$</div></foreignObject>
</svg>

**Toinen tapa: potenssisovitus.** Sovita taustavalolla korjattuihin pisteisiin ohjelmalla potenssifunktio $E = A\cdot r^{n}$, jossa $A$ ja $n$ ovat sovituksen vakiot. Malli ennustaa, että eksponentti on $n = -2$. Jos taustavaloa ei ole vähennetty, valaistusvoimakkuus pienenee kaukana hitaammin kuin mallissa, ja eksponentin itseisarvo jää pienemmäksi kuin $2$. Samoin käy, jos mittaamasi etäisyydet ovat kauttaaltaan liian pieniä, esimerkiksi kun etäisyys on mitattu lampun kuvun pinnasta eikä hehkulangasta. Tätä virhettä tutkitaan laajennuksessa.

Kumpikin tapa on hyvä, kun perustelet sen. Suoran kuvaajasta poikkeamat näkyvät helposti silmällä, potenssisovitus taas antaa eksponentin suoraan verrattavaksi teoriaan.
:::

Kuvaajan piirtämiseen ja sovitukseen käytä Graphical Analysis Pro -ohjelmaa. Ruukkilabran ohjeet: [[ohje:tvt-suoran-sovitus|Suoran sovittaminen]], [[ohje:tvt-kulmakerroin|Kulmakertoimen tulkinta]] ja [[ohje:tvt-taulukkolaskenta|Taulukko ja lasketut sarakkeet]].

## Epävarmuus ja luotettavuus

Ilmoita mallisi vakio epävarmuuksineen ja perustele, miten arvioit epävarmuuden. Kerro, vastaako mittaustesi riippuvuus teoriasta odotettavaa riippuvuutta epävarmuuksien rajoissa.

::: tuki O OO
**Pisteiden epävarmuus.** Kun taustavalo vähennetään, erotuksen epävarmuus on lukemien epävarmuuksien summa: $\Delta E = \Delta E_\text{kok} + \Delta E_\text{tausta}$. Kun etäisyys korotetaan toiseen, suhteellinen epävarmuus kaksinkertaistuu: suureen $\dfrac{1}{r^2}$ suhteellinen epävarmuus on $2\cdot\dfrac{\Delta r}{r}$. Lähellä lamppua etäisyyden epävarmuus painaa siis eniten.

**Vakion epävarmuus.** Kulmakertoimen tai eksponentin epävarmuuden voit arvioida jommallakummalla tavalla:

- **Sovitusohjelman keskivirhe.** Monet ohjelmat ilmoittavat sovituksen vakioiden keskivirheet. Käytä niitä epävarmuutena.
- **Jyrkin ja loivin suora.** Piirrä suoran kuvaajaan jyrkin ja loivin suora, jotka vielä sopivat pisteisiin niiden epävarmuuksien rajoissa. Määritä niiden kulmakertoimet $I_\text{max}$ ja $I_\text{min}$ ja arvioi epävarmuus vaihteluvälin puolikkaana: $\Delta I = \dfrac{I_\text{max} - I_\text{min}}{2}$.

Pyöristä epävarmuus yhteen merkitsevään numeroon ja tulos samaan desimaaliin. Potenssisovituksessa tarkista, osuuko $-2$ välille $n \pm \Delta n$. Suoran kuvaajassa tarkista, osuuko origo jyrkimmän ja loivimman suoran väliin. Jos osuu, tulokset ovat sopusoinnussa mallin kanssa, mutta se ei todista mallia oikeaksi.
:::

Pohdi sitten luotettavuutta konkreettisesti: olivatko suurimmat epävarmuuden lähteet satunnaisia vai systemaattisia, ja mihin suuntaan systemaattiset virheet olisivat muuttaneet tulosta? Mieti ainakin taustavaloa, heijastuksia, anturin asentoa ja sitä, mistä kohdista etäisyys mitattiin. Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Millainen matemaattinen malli kuvaa tuloksia, ja vastaako se teoriasta päättelemääsi riippuvuutta koko mittausalueella? Perustele, miksi valitsemastasi kuvaajasta tai sovituksesta voi päätellä mallin sopivuuden. Viittaa kuvaajaan, esimerkiksi "kuvaajasta 2 nähdään, että …". Vertaa tulosta ennusteeseesi: mikä osui oikeaan ja mikä ei?

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla ja käy läpi sen kaikki osat. Kuvaajien ja tulosten esittämisessä auttaa ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tausta ja teoria:** periaate, josta malli päätellään, malli hypoteesina ja ehdot, joilla se pätee.
- **Koejärjestely ja menetelmä:** kuva järjestelystä, mistä kohdista etäisyys mitattiin, miten taustavalo huomioitiin ja miten asento pidettiin samana.
- **Mittaustulokset:** alkuperäiset lukemat omissa sarakkeissaan, myös taustavalo, ja lasketut suureet niiden oikealla puolella.
- **Tulosten käsittely ja graafinen analyysi:** millä kuvaajalla tai sovituksella mallia testattiin ja miksi.
- **Luotettavuus:** konkreettiset epävarmuuden lähteet ja niiden vaikutuksen suunta.

## Laajennus: missä valo syntyy?

Etäisyyden mittaaminen on hankalaa, koska hehkulanka on lasikuvun sisällä ja anturin herkkä osa voi olla suojakuoren takana. Mittaamasi etäisyys $r$ voi siis poiketa todellisesta etäisyydestä vakiomäärän $d$ verran, niin että todellinen etäisyys on $r + d$.

Muuta malliasi niin, että siinä on mukana $d$. Määritä sitten $d$ epävarmuuksineen itse valitsemastasi kuvaajasta tai sovituksesta, ja perustele valintasi. Onko $d$ sopusoinnussa sen kanssa, mihin arvioit valon syntykohdan ja anturin herkän pinnan? Jos korjaat etäisyydet, sopivatko tulokset paremmin päälinjan malliin?

::: tuki O OO
**Malli, jossa on mukana $d$.** Kun etäisyys $r$ korvataan todellisella etäisyydellä $r + d$, malli on muotoa

```latex
E = \frac{I}{(r + d)^2}
```

missä $I$ on lampun valovoima. Kun yhtälön molemmilta puolilta otetaan neliöjuuri ja käänteisluku, saadaan

```latex
\frac{1}{\sqrt{E}} = \frac{1}{\sqrt{I}}\cdot r + \frac{d}{\sqrt{I}}
```

joten suure $\dfrac{1}{\sqrt{E}}$ on mitatun etäisyyden $r$ funktiona suora. Jos $d = 0$, suora kulkee origon kautta. Muuten suora leikkaa vaaka-akselin kohdassa $r = -d$.

**Vihjeitä.** Jos sovitat suoran $\dfrac{1}{\sqrt{E}} = a\cdot r + b$, niin $a = \dfrac{1}{\sqrt{I}}$ ja $b = \dfrac{d}{\sqrt{I}}$, joten $d = \dfrac{b}{a}$. Vähennä taustavalo ennen neliöjuuren ottamista. Kaukana lampusta valaistusvoimakkuus on pieni, joten taustavalon ja heijastusten epävarmuus tekee suureesta $\dfrac{1}{\sqrt{E}}$ siellä hyvin epävarman. Etäisyyden virhe taas vaikuttaa eniten lähellä lamppua, joten lähimmät pisteet kertovat eniten luvusta $d$.
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi kuvaajaan ja mittaustuloksiin vai siihen, mitä odotit?
- Mitä tekisit toisin, jos aloittaisit alusta?
