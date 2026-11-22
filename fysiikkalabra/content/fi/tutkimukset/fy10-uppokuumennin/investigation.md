# Uppokuumentimen hyötysuhteen määrittäminen

> **Tutkimuskysymys:** Kuinka suuri osa uppokuumentimeen tuodusta sähköenergiasta lämmittää kalorimetrissä olevaa vettä, ja pysyykö tämä osuus samana koko lämmityksen ajan?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratorion työpöydällä on kalorimetri, joka on piirretty puoliksi auki leikattuna. Sen sisällä on vettä, ja uppokuumentimen kierukka on kokonaan veden alla. Kannen läpi veteen ulottuvat myös lämpömittari ja sekoitin. Kuumennin on kytketty johtimilla virtalähteeseen ja kahteen yleismittariin. Pöydällä on lisäksi vaaka ja vihko." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-uppokuumennin-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

Vedenkeitin, lämminvesivaraaja ja akvaarion lämmitin lämmittävät vettä sähköllä. Tässä tutkimuksessa lämmität vettä uppokuumentimella, mittaat sähköisiä suureita ja veden lämpötilaa ja selvität, kuinka suuri osa sähköenergiasta päätyy veteen. Tulos määritetään kuvaajasta, ei yksittäisestä mittauksesta. Mittaa, piirrä ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** uppokuumentimen hyötysuhde veden lämmittämisessä epävarmuuksineen, määritettynä kuvaajan avulla, sekä se, pysyykö hyötysuhde samana koko mittausalueella.

**Päätät itse:** veden määrän, lämmitysajan ja sen, kuinka usein kirjaat lukemat, mistä suureista piirrät kuvaajan ja miksi, mitkä mittauspisteet otat mukaan sovitukseen perusteluineen sekä tavan, jolla arvioit tuloksen epävarmuuden. Ohjatussa ja osittain ohjatussa työtavassa sivu antaa näihin tukea, itsenäisessä työtavassa perustelet valintasi itse.

::: tuki I
**Itsenäinen työtapa.** Laajennus, eristyksen vaikutuksen tutkiminen, kuuluu työhösi: vertaa lopuksi kahdella järjestelyllä saatuja hyötysuhteita epävarmuuksineen.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Kuinka suuri osa sähköenergiasta arvelet päätyvän veteen? Mihin muualle energiaa voi joutua?
2. Millainen on veden lämpötilan kuvaaja ajan funktiona, kun kuumennin on päällä? Muuttuuko kuvaajan muoto, kun vesi on lämmennyt selvästi huoneenlämpöä lämpimämmäksi?
3. Jos veden massa kaksinkertaistetaan ja kuumentimen teho pysyy samana, mitä tapahtuu lämpötilan nousunopeudelle? Entä hyötysuhteelle?
4. Mikä mittauksessa on todennäköisesti suurin epävarmuuden lähde?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Tutkimuskysymyksestä mitattaviksi suureiksi

Energiaa ei voi lukea suoraan mittarista. Ennen kuin luet eteenpäin, kirjaa:

1. Mitkä suureet mittaamalla saat selville kuumentimeen tuodun sähköenergian? Entä veden saaman lämmön?
2. Miten saat yhdestä lämmityksestä useita mittauspisteitä?
3. Mitä pidät vakiona, ja mitä kirjaat ylös vain kerran?
4. Millaisen kuvaajan piirrät, jotta hyötysuhde saadaan sen kulmakertoimesta?

## Teoriaa lyhyesti

Uppokuumentimessa sähkövirta kulkee vastuslangan läpi, ja sähköenergia muuttuu langan sisäenergiaksi. Kuumasta langasta siirtyy lämpöä ympäröivään veteen, mutta lämpenevät myös kuumennin itse, kalorimetrin astia, lämpömittari ja sekoitin, ja lämpöä siirtyy ympäristöön. Tässä työssä hyödyksi lasketaan vain veden saama lämpö. **Hyötysuhde** kertoo, kuinka suuri osa laitteeseen tuodusta energiasta on hyötyä:

```latex
\eta = \frac{Q}{E}
```

missä $Q$ on veden saama lämpö ja $E$ kuumentimeen tuotu sähköenergia. Hyötysuhteella ei ole yksikköä, ja se ilmoitetaan usein prosentteina. [[apua:fy2-4|Hyötysuhde]]

**Sähköteho ja sähköenergia.** Sähkölaitteen teho on sen napojen välisen jännitteen $U$ ja laitteen läpi kulkevan sähkövirran $I$ tulo:

```latex
P = UI
```

Jännitteen yksikkö on voltti ($\text{V}$), sähkövirran ampeeri ($\text{A}$) ja tehon watti: $1\,\text{V} \cdot 1\,\text{A} = 1\,\text{W} = 1\,\text{J/s}$. Sähkötehoa käsitellään tarkemmin moduulissa FY6. Teho kertoo, kuinka paljon energiaa siirtyy sekunnissa, joten kun jännite ja sähkövirta pysyvät vakioina, ajassa $t$ kuumentimeen tuotu sähköenergia on

```latex
E = Pt = UIt
```

Jos jännite tai sähkövirta muuttuu mittauksen aikana, energia lasketaan osissa: jokaisella lyhyellä aikavälillä $\Delta t$ tuotu energia $UI\Delta t$ lasketaan sen välin jännitteestä ja virrasta, ja osat lasketaan yhteen. [[apua:fy2-3|Teho ja energia]]

**Veden saama lämpö.** Kun veden lämpötila muuttuu $\Delta T$ verran, vesi saa lämmön

```latex
Q = cm\Delta T
```

missä $c$ on veden ominaislämpökapasiteetti (taulukkokirjasta) ja $m$ veden massa. Yhtälö pätee, kun vesi ei muutu olomuodosta toiseen, joten vettä ei lämmitetä kiehuvaksi. Lämpötilan muutos on sama kelvineinä ja celsiusasteina. [[apua:fy3-6|Aineen lämpeneminen]]

**Mittarien kytkeminen.** Virtamittari kytketään **sarjaan** kuumentimen kanssa, jotta sama sähkövirta kulkee molempien läpi. Jännitemittari kytketään **rinnan** kuumentimen kanssa, sen kahden johtimen väliin, jotta se mittaa juuri kuumentimen jännitteen.

<svg data-fig="setup" viewBox="0 0 600 450" role="img" aria-label="Kaaviokuva. Virtalähteen napa on kytketty virtamittarin kautta uppokuumentimen toiseen johtimeen, ja kuumentimen toinen johdin palaa virtalähteen toiseen napaan. Virtamittari on siis sarjassa kuumentimen kanssa ja mittaa sähkövirran I. Jännitemittari on kytketty kuumentimen kahden johtimen väliin eli rinnan kuumentimen kanssa, ja se mittaa jännitteen U. Kuumentimen kierukka on kokonaan veden alla kalorimetrissä. Kannen läpi veteen ulottuvat myös lämpömittari ja sekoitin." style="max-width:100%;font-size:24px">
  <image href="pics/fy10/fy10-uppokuumennin-setup.webp" x="0" y="0" width="600" height="455" preserveAspectRatio="none"/>
  <foreignObject x="26" y="53" width="112" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\text{virtalähde}$</div></foreignObject>
  <foreignObject x="142" y="33" width="18" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:20px">$-$</div></foreignObject>
  <foreignObject x="142" y="73" width="18" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:20px">$+$</div></foreignObject>
  <foreignObject x="240.5" y="117" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px">$\mathrm{A}$</div></foreignObject>
  <foreignObject x="200" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$I$</div></foreignObject>
  <foreignObject x="290.5" y="177" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px">$\mathrm{V}$</div></foreignObject>
  <foreignObject x="290" y="137.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$U$</div></foreignObject>
  <foreignObject x="444" y="288" width="133" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\text{lämpömittari}$</div></foreignObject>
  <foreignObject x="444" y="243" width="122" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\text{kalorimetri}$</div></foreignObject>
  <foreignObject x="444" y="383" width="143" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px">$\text{uppokuumennin}$</div></foreignObject>
  <foreignObject x="79" y="318" width="91" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:20px">$\text{sekoitin}$</div></foreignObject>
  <foreignObject x="275" y="303" width="50" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\text{vesi}$</div></foreignObject>
</svg>

::: tuki O OO
Tarkista kirjauksesi tästä. Kun kirjaat jännitteen, sähkövirran ja veden lämpötilan tasaisin väliajoin, saat jokaiselle hetkelle $t$ kaksi energiaa: siihen mennessä tuodun sähköenergian $E = UIt$ ja veden siihen mennessä saaman lämmön $Q = cm(T - T_0)$, missä $T_0$ on veden lämpötila kuumentimen kytkemishetkellä. Yksi lämmitys antaa siis monta mittauspistettä.

**Malli 1: lämpö sähköenergian funktiona.** Jos hyötysuhde pysyy vakiona, $Q = \eta E$. Silloin kuvaaja, jossa pystyakselilla on $Q$ ja vaaka-akselilla $E$, on origon kautta kulkeva suora, ja sen kulmakerroin on hyötysuhde $\eta$. Kulmakerroin on yksikötön, koska kummankin akselin yksikkö on joule.

<svg data-fig="model" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja: veden saama lämpö Q sähköenergian E funktiona mallin mukaan, kun hyötysuhde pysyy vakiona. Kuvaaja on origon kautta kulkeva suora. Katkoviivalla on vertailun vuoksi piirretty suora Q yhtä kuin E, jolla kaikki sähköenergia päätyisi veteen. Mallisuoralle on merkitty kahden pisteen väliset muutokset delta E ja delta Q, ja kulmakerroin eta on delta Q jaettuna delta E:llä. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="291" x2="90" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,24 L96,37 L84,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="60" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$E$</div></foreignObject>
  <foreignObject x="104" y="15.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$Q$</span></div></foreignObject>
  <polyline points="90,290 455,59.5" fill="none" stroke="#c9c2b2" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="8 6"/>
  <foreignObject x="372" y="42.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$Q = E$</div></foreignObject>
  <polyline points="90,290 455,124" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="242" y1="221" x2="413" y2="221" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="413" y1="221" x2="413" y2="143" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="311" y="226.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\Delta E$</div></foreignObject>
  <foreignObject x="423" y="167.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\Delta Q$</div></foreignObject>
  <foreignObject x="160" y="83.5" width="58" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\eta = \dfrac{\Delta Q}{\Delta E}$</div></foreignObject>
</svg>

**Malli 2: lämpötila ajan funktiona.** Jos lisäksi jännite ja sähkövirta pysyvät vakioina, $cm(T - T_0) = \eta UIt$, eli

```latex
T = T_0 + \frac{\eta UI}{cm}\cdot t
```

Lämpötila ajan funktiona on silloin suora, jonka kulmakerroin on $a = \dfrac{\eta UI}{cm}$. Hyötysuhde saadaan kulmakertoimesta: $\eta = \dfrac{cma}{UI}$.

<svg data-fig="heating" viewBox="0 0 600 340" role="img" aria-label="Kuvaaja: veden lämpötila T ajan t funktiona mallin mukaan, kun teho ja hyötysuhde pysyvät vakioina. Kuvaaja on suora, joka alkaa alkulämpötilasta T nolla. Suoralle on merkitty muutokset delta t ja delta T, ja kulmakerroin a on delta T jaettuna delta t:llä. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="290" x2="484" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,290 L483,296 L483,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="291" x2="90" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,24 L96,37 L84,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="502" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t$</div></foreignObject>
  <foreignObject x="104" y="15.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$T$</span></div></foreignObject>
  <polyline points="90,237 455,80.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="45" y="222.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$T_0$</div></foreignObject>
  <line x1="83" y1="237" x2="90" y2="237" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <line x1="223" y1="180" x2="394" y2="180" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="394" y1="180" x2="394" y2="106.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="292" y="185.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\Delta t$</div></foreignObject>
  <foreignObject x="404" y="129" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\Delta T$</div></foreignObject>
  <foreignObject x="152" y="54.5" width="58" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$a = \dfrac{\Delta T}{\Delta t}$</div></foreignObject>
</svg>

Kummankin mallin ehto on, että hyötysuhde pysyy vakiona. Se ei ole itsestään selvää: lämmin vesi luovuttaa ympäristöön sitä enemmän lämpöä, mitä suurempi on sen ja huoneilman lämpötilaero, ja lämmityksen alussa kuumennin ja astia lämpenevät ennen kuin vesi ehtii lämmetä. Mittaus näyttää, pysyvätkö pisteet suoralla koko mittausalueella.
:::

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, mitä mittaat, kuinka usein, mitä pidät vakiona ja kuinka pitkään lämmität.

::: tuki O
**Ohjattu.** Punnitse kalorimetrin sisäastia tyhjänä ja vedellä täytettynä: erotus on veden massa $m$. Veden on peitettävä kuumentimen kierukka kokonaan. Mittaa veden alkulämpötila $T_0$, kytke virta ja käynnistä ajanotto samalla hetkellä. Kirjaa jännite $U$, sähkövirta $I$ ja veden lämpötila $T$ esimerkiksi puolen minuutin välein, ja sekoita vettä koko ajan. Lämmitä, kunnes lämpötila on noussut noin $15\,{}^\circ\text{C}$, ja katkaise sitten virta. Pidä sähkövirta opettajan ilmoittaman rajan alapuolella.
:::

::: tuki OO
**Osittain ohjattu.** Päätä itse, kuinka paljon vettä käytät, kuinka usein kirjaat lukemat ja kuinka pitkään lämmität. Valitse, kumpaa mallia käytät hyötysuhteen määrittämiseen, ja perustele valintasi. Kirjaa päätöksesi perusteluineen.
:::

::: tuki O OO
Mieti ainakin näitä:

- Miksi vettä täytyy sekoittaa koko ajan? Mitä lämpömittari näyttäisi, jos se olisi lähellä kuumenninta ja vesi ei sekoittuisi?
- Mitä tapahtuu lämpöhäviöille, jos lämmität vettä kauan ja paljon? Kannattaako vesi lämmittää mahdollisimman kuumaksi?
- Mitä etua on siitä, että aloitat vedellä, joka on hieman huoneenlämpöä viileämpää, ja lopetat suunnilleen yhtä paljon huoneenlämmön yläpuolella?
- Pysyvätkö jännite ja sähkövirta vakioina? Mallia 2 voi käyttää vain, jos pysyvät; mallissa 1 energian voi laskea osissa.
:::

## Mittaa

Kirjaa alkuperäiset mittaustulokset taulukkoon heti mittauksen aikana. Laskemasi suureet saavat omat sarakkeensa mitattujen oikealle puolelle. Kirjaa myös veden massa, alkulämpötila ja huoneen lämpötila.

::: tuki O
Voit käyttää esimerkiksi tällaista taulukkoa:

| $t\ (\text{s})$ | $U\ (\text{V})$ | $I\ (\text{A})$ | $T\ (^\circ\text{C})$ | $E = UIt\ (\text{J})$ | $Q = cm(T - T_0)\ (\text{J})$ |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

Jos lämpötila-anturi kirjaa lämpötilan itse, kirjaa jännite ja sähkövirta käsin muutaman kerran mittauksen aikana. Jos ne muuttuvat, laske sähköenergia osissa.
:::

Muista mittausepävarmuus: kirjaa, kuinka tarkasti voit lukea lämpötilan, ja selvitä mittarien tarkkuus mittarin ohjeesta tai opettajalta. Jos lasket hyötysuhteen yksittäisestä lukemasta, lämpötilan muutoksen epävarmuuteen vaikuttavat molemmat lukemat, sekä $T$ että $T_0$. Kuvaajan kulmakertoimeen alkulämpötilan virhe ei vaikuta, koska se siirtää kaikkia pisteitä yhtä paljon. [[apua:fy1-3|Mittausepävarmuuden arvioiminen]]

## Käsittele tulokset

Piirrä mittaustuloksista kuvaaja, josta hyötysuhde saadaan kulmakertoimena tai lasketaan kulmakertoimesta. Merkitse akseleille suureet ja yksiköt. Piirrä mittauspisteet, älä yhdistä niitä murtoviivalla, ja sovita pisteisiin suora. [[apua:fy1-4|Suoran sovittaminen ja kulmakertoimen tulkinta]]

::: tuki O
Laske jokaiselle riville sähköenergia $E$ ja veden saama lämpö $Q$. Valitse pystyakselille $Q$ ja vaaka-akselille $E$. Hyötysuhde on sovitetun suoran kulmakerroin.
:::

Kirjoita sovitetun suoran yhtälö ja vastaa:

1. Ovatko pisteet suoralla koko mittausalueella? Jos eivät, poikkeavatko ne alussa, lopussa vai molemmissa, ja mistä se voi johtua?
2. Mikä suure on kulmakerroin, ja mikä on sen yksikkö?
3. Kulkeeko suora origon kautta? Jos ei, mistä vakiotermi voi johtua?
4. Laske $\eta = Q/E$ myös viimeisestä mittauspisteestä ja vertaa sitä kulmakertoimeen. Miksi ne eroavat, ja kumpi on luotettavampi?

::: tuki O OO
Tarkista vastauksesi tästä.

**Kuvaajan alku ja loppu.** Lämmityksen alussa kuumennin, astia ja lämpömittari lämpenevät, ennen kuin vesi ja lämpömittarin lukema ehtivät seurata. Siksi ensimmäiset pisteet voivat jäädä suoran alapuolelle, ja suora voi leikata akselin muualla kuin origossa. Tämä ei muuta suoran osan kulmakerrointa. Astia kuitenkin lämpenee veden mukana koko mittauksen ajan, ja sen saama lämpö pienentää kulmakerrointa ja siis hyötysuhdetta: tässä työssä se lasketaan häviöksi. Lopussa, kun vesi on selvästi huoneilmaa lämpimämpää, häviöt kasvavat ja pisteet voivat kaartua suoran alapuolelle. Sovita suora siihen osaan, jossa pisteet ovat suoralla, ja kerro raportissa, mitkä pisteet jätit pois ja miksi.

**Miksi kuvaaja eikä yksi piste?** Yhdestä mittauspisteestä laskettu $\eta = Q/E$ sisältää lämmityksen alun viiveen ja yksittäisen lukeman virheen, ja viimeisessä pisteessä myös lopun suuremmat häviöt. Kulmakerroin kertoo, kuinka paljon lämpöä vesi saa jokaista lisää tuotua joulea kohden, ja kuvaaja näyttää samalla, onko suhde vakio.
:::

Kuvaajan sovitukseen käytä Graphical Analysis Pro -ohjelmaa. Ruukkilabran ohjeet: [[ohje:tvt-suoran-sovitus|Suoran sovittaminen]], [[ohje:tvt-kulmakerroin|Kulmakertoimen tulkinta]] ja [[ohje:tvt-taulukkolaskenta|Taulukko ja lasketut sarakkeet]].

## Epävarmuus ja luotettavuus

Ilmoita hyötysuhde muodossa $\eta \pm \Delta\eta$ ja perustele, miten arvioit epävarmuuden $\Delta\eta$.

::: tuki O OO
Kulmakertoimen epävarmuuden $\Delta a$ voit arvioida jommallakummalla tavalla:

- **Sovitusohjelman keskivirhe.** Monet ohjelmat ilmoittavat kulmakertoimen keskivirheen. Käytä sitä epävarmuutena $\Delta a$.
- **Jyrkin ja loivin suora.** Piirrä jyrkin ja loivin suora, jotka vielä sopivat pisteisiin niiden epävarmuuksien rajoissa. Määritä niiden kulmakertoimet $a_\text{max}$ ja $a_\text{min}$ ja arvioi epävarmuus vaihteluvälin puolikkaana: $\Delta a = \dfrac{a_\text{max} - a_\text{min}}{2}$.

Sovitus näkee vain pisteiden hajonnan. Jos veden massa, jännite tai sähkövirta on mitattu hieman väärin, kaikki pisteet siirtyvät samassa suhteessa, ja kulmakerroin muuttuu ilman, että pisteet hajoavat. Lisää siksi niiden suhteelliset epävarmuudet kulmakertoimen suhteelliseen epävarmuuteen. Kummassakin mallissa

```latex
\frac{\Delta \eta}{\eta} \approx \frac{\Delta a}{a} + \frac{\Delta m}{m} + \frac{\Delta U}{U} + \frac{\Delta I}{I}
```

missä $a$ on käyttämäsi kuvaajan kulmakerroin (mallissa 1 $a = \eta$). Alkulämpötilan $T_0$ virhe siirtää kaikkia pisteitä yhtä paljon, joten se ei muuta kulmakerrointa.

Pyöristä $\Delta\eta$ yhteen merkitsevään numeroon ja $\eta$ samaan desimaaliin.
:::

Pohdi sitten luotettavuutta konkreettisesti: mitkä olivat suurimmat epävarmuuden lähteet, olivatko ne satunnaisia vai systemaattisia, ja mihin suuntaan ne olisivat muuttaneet tulosta? Mitä hyötysuhteesi kertoo juuri tästä järjestelystä, ja mitä se ei kerro kuumentimesta yleensä? Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Pysyikö hyötysuhde samana koko lämmityksen ajan? Perustele, miksi kulmakertoimesta saatu hyötysuhde on luotettavampi kuin yksittäisestä mittauspisteestä laskettu. Viittaa kuvaajaan, esimerkiksi "kuvaajasta 1 nähdään, että …". Mihin veteen päätymätön energia joutui? Vertaa tulosta ennusteeseesi: mikä osui oikeaan ja mikä ei?

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla ja käy läpi sen kaikki osat. Kuvaajien ja tulosten esittämisessä auttaa ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tausta ja teoria:** miten sähköenergia ja veden saama lämpö lasketaan ja miksi valitsemasi kuvaajan kulmakertoimesta saadaan hyötysuhde.
- **Koejärjestely ja menetelmä:** kytkentäkaavio, jossa näkyy, miten mittarit on kytketty, sekä työturvallisuus.
- **Mittaustulokset:** alkuperäiset lukemat omissa sarakkeissaan ja johdetut suureet niiden oikealla puolella, sekä veden massa, alkulämpötila ja huoneen lämpötila.
- **Tulosten käsittely ja tulos:** kuvaaja, sovitettu suora, mahdollisesti pois jätetyt pisteet perusteluineen $\eta \pm \Delta\eta$ oikein pyöristettynä sekä perustelu sille, miksi tulos määritettiin kulmakertoimesta eikä yksittäisestä pisteestä.
- **Luotettavuus:** konkreettiset epävarmuuden lähteet ja niiden vaikutuksen suunta.

## Laajennus: eristyksen vaikutus

Kalorimetrin tehtävä on vähentää lämmön siirtymistä ympäristöön. Tutki, kuinka paljon sillä on merkitystä: toista mittaus järjestelyllä, joka eristää huonommin, esimerkiksi ilman kantta tai tavallisessa lasisessa dekantterilasissa, ja määritä hyötysuhde samalla tavalla.

Vertaa kahdella järjestelyllä saatuja hyötysuhteita epävarmuuksineen: mahtuvatko ne toistensa epävarmuusväleihin? Päällekkäiset välit tarkoittavat, että tulokset ovat sopusoinnussa, eivät sitä, että ne on todistettu samoiksi. Näkyykö ero myös siinä, missä kohdassa pisteet alkavat kaartua suoralta?

::: tuki O OO
**Vihjeitä.** Muuta vain yhtä asiaa kerrallaan: käytä samaa veden massaa, samaa alkulämpötilaa ja samaa kuumenninta ja pidä sähkövirta samana. Muuten et tiedä, mistä mahdollinen ero johtuu.
:::

Muista turvallisuus myös laajennuksessa: kierukan on oltava koko ajan veden alla, ja lasiastia kuumenee.

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi kuvaajaan ja mittaustuloksiin vai siihen, mitä odotit?
- Mitä tekisit toisin, jos aloittaisit alusta?

**Sovella:** Vedenkeittimen tyyppikilvessä ilmoitetaan sen teho. Mitä sinun pitäisi tietää tai mitata, jotta voisit arvioida keittimen hyötysuhteen, ja miksi tulos olisi vain arvio? Pohdi tätä ajatuksen tasolla: kodin sähkölaitteiden sähköisiä suureita ei mitata itse.
