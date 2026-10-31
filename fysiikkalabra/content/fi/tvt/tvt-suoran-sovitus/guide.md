Suoran sovittamisessa mittauspisteiden joukkoon piirretään yksi suora, joka kuvaa niitä mahdollisimman hyvin. Sovitus testaa mallia, ja sen kulmakertoimesta määritetään usein tutkittava suure.

## Mihin tarvitset tätä

Suora sovitetaan useimmissa tutkimuksissa, esimerkiksi tutkimuksissa *Jousivakion määrittäminen* ja *Uppokuumentimen hyötysuhteen määrittäminen*. Tutkimuksissa *Leikkiauton nopeus ja lähtökorkeus* ja *Valaistusvoimakkuuden riippuvuus etäisyydestä* mittauksista lasketaan ensin uusi suure, jotta mallin mukainen kuvaaja on suora. Ennen sovitusta tarvitset [[ohje:tvt-kuvaaja|kuvaajan mittauspisteistä]].

## Työvaiheet

1. **Selvitä mallista, millainen suoran pitäisi olla.** Kirjoita tutkimuksen malli suoran yhtälön $y = kx + b$ muotoon ja katso, mitkä suureet tulevat akseleille. Esimerkiksi jousivoiman laki $F = kx$ on origon kautta kulkeva suora, kun pystyakselilla on jousivoima $F$ ja vaaka-akselilla venymä $x$.

2. **Ymmärrä, mitä sovitus tekee.** Mittauspisteet eivät yleensä ole täsmälleen samalla suoralla mittausepävarmuuden vuoksi. Siksi suoraa ei piirretä ensimmäisen ja viimeisen pisteen kautta, vaan pisteiden joukon keskeltä. Graphical Analysis Pro sovittaa suoran **pienimmän neliösumman menetelmällä**: pisteen poikkeama on sen pystysuora etäisyys suorasta, ja ohjelma valitsee suoran, jolla poikkeamien neliöiden summa on pienin.

    <svg data-fig="fit" viewBox="0 0 600 340" role="img" aria-label="Kaaviokuva ilman lukuarvoja: seitsemän mittauspistettä ja niihin sovitettu suora. Jokaisesta pisteestä on pystysuora katkoviiva suoralle; viivan pituus on pisteen poikkeama suorasta. Pisteitä on suoran kummallakin puolella, eikä suora kulje ensimmäisen ja viimeisen pisteen kautta. Pienimmän neliösumman menetelmä valitsee suoran, jolla poikkeamien neliöiden summa on pienin." style="max-width:100%;font-size:24px">
  <line x1="79" y1="290" x2="474" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M486,290 L473,296 L473,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="80" y1="291" x2="80" y2="66" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M80,54 L86,67 L74,67 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="50" y="295.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="492" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x$</div></foreignObject>
  <foreignObject x="70" y="23.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$y$</div></foreignObject>
  <line x1="127.5" y1="233" x2="127.5" y2="244.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="175" y1="247" x2="175" y2="224" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="222.5" y1="191" x2="222.5" y2="203" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="270" y1="198" x2="270" y2="182.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="317.5" y1="138.5" x2="317.5" y2="162" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="365" y1="147.5" x2="365" y2="141" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <line x1="412.5" y1="123" x2="412.5" y2="120.5" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="5 4"/>
  <polyline points="94,259 446,106" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="127.5" cy="233" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="175" cy="247" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="222.5" cy="191" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="270" cy="198" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="317.5" cy="138.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="365" cy="147.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="412.5" cy="123" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="456" y="91.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$y = kx + b$</div></foreignObject>
  <foreignObject x="203.5" y="250" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{poikkeama}$</div></foreignObject>
  <line x1="200.5" y1="252.5" x2="179" y2="235" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
</svg>

3. **Sovita suora ohjelmalla.** Avaa **Graph Tools**, valitse **Apply Curve Fit** ja yhtälöksi **Linear**, eli suora, jossa on vakiotermi. Vaihtoehto **Proportional** on origon kautta kulkeva suora $y = kx$. Jos malli pätee vain osalla mittausalueesta, valitse ensin se väli vetämällä kuvaajan yli: sovitus käyttää vain valittua väliä.

4. **Lue sovituksen tietolaatikko.** Kuvaajan päälle tulevassa laatikossa ovat suoran kertoimet eli kulmakerroin ja vakiotermi ([[ohje:tvt-kulmakerroin|Kulmakertoimen ja vakiotermin tulkinta]]). RMSE kertoo, kuinka kaukana pisteet ovat keskimäärin suorasta pystyakselin yksikössä. Suoran sovituksessa näkyy myös korrelaatiokerroin $r$. Arvo lähellä lukua $1$ tai $-1$ ei yksin todista mallia oikeaksi, koska loivasti kaartuvatkin pisteet voivat antaa sellaisen arvon.

5. **Katso, miten pisteet poikkeavat suorasta.** Jos poikkeamat ovat satunnaisesti suoran kummallakin puolella, suora kuvaa mittauksia hyvin. Jos pisteet kaartuvat järjestelmällisesti, esimerkiksi ovat päissä suoran alapuolella ja keskellä sen yläpuolella, malli ei sovi mittauksiin. Ohjelma sovittaa suoran mihin tahansa pisteisiin, joten tämä on sinun tarkistettava.

6. **Tarkista poikkeava piste.** Selvästi poikkeava mittaustulos tarkistetaan ja mittaus voidaan tarvittaessa toistaa. Tulosta ei poisteta pelkästään siksi, että se poikkeaa muista. Mahdollinen hylkääminen on perusteltava ja kirjattava, esimerkiksi "piste 4 jätettiin pois sovituksesta, koska ajanotto alkoi myöhässä".

7. **Päätä, kulkeeko suora origon kautta.** Vaikka malli olisi muotoa $y = kx$, sovita ensin suora, jossa on vakiotermi, eli valitse yhtälö **Linear**. Jos vakiotermi on epävarmuuksien rajoissa nolla, mittaukset ovat sopusoinnussa origon kautta kulkevan mallin kanssa. Jos se poikkeaa selvästi nollasta, selvitä syy. Valitse yhtälö **Proportional** vain, kun siihen on fysikaalinen syy, ja kerro siitä raportissa.

8. **Muuta kaareva riippuvuus suoraksi.** Jos mallin mukainen kuvaaja ei ole suora, laske mittauksista uusi suure, jonka avulla siitä tulee suora. Tätä kutsutaan linearisoinniksi. Tee uudesta suureesta laskettu sarake ([[ohje:tvt-taulukkolaskenta|Taulukko ja lasketut sarakkeet]]), valitse se akselille ja sovita suora. Ohjelma osaa sovittaa myös käyriä, mutta suorasta näet silmällä, sopiiko malli, ja kulmakertoimen merkitys on selvä. Esimerkkejä tutkimuksista:

    - heiluri, $T = 2\pi\sqrt{\tfrac{l}{g}}$: jaksonajan neliö $T^2$ pituuden $l$ funktiona
    - leikkiauto, $v^2 = 2g \cdot h$: nopeuden neliö $v^2$ korkeuden $h$ funktiona
    - valaistus, $E = \tfrac{I}{r^2}$: valaistusvoimakkuus $E$ suureen $\tfrac{1}{r^2}$ funktiona
    - jäähtyminen: $\ln(T - T_\text{huone})$ ajan $t$ funktiona, kun $T$ on veden lämpötila

    <svg data-fig="linearise" viewBox="0 0 600 330" role="img" aria-label="Kaksi kaaviokuvaa ilman lukuarvoja. Vasemmalla nopeus v korkeuden h funktiona: pisteet kaartuvat, ja niihin piirretty suora kulkee päissä pisteiden yläpuolella ja keskellä alapuolella. Oikealla samoista mittauksista laskettu nopeuden neliö v toiseen korkeuden h funktiona: pisteet ovat suoralla, joka kulkee origon kautta." style="max-width:100%;font-size:24px">
  <line x1="79" y1="250" x2="234" y2="250" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M246,250 L233,256 L233,244 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="80" y1="251" x2="80" y2="66" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M80,54 L86,67 L74,67 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="252" y="235.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$h\ (\text{m})$</div></foreignObject>
  <foreignObject x="70" y="23.5" width="87" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v\ (\text{m/s})$</div></foreignObject>
  <polyline points="86.5,208 217.5,90.5" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="7 5"/>
  <circle cx="85.5" cy="220.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="90.5" cy="208" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="101.5" cy="191" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="120" cy="169" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="146.5" cy="145.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="180" cy="122" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="213.5" cy="102" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="369" y1="250" x2="504" y2="250" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M516,250 L503,256 L503,244 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="370" y1="251" x2="370" y2="66" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M370,54 L376,67 L364,67 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="522" y="235.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$h\ (\text{m})$</div></foreignObject>
  <foreignObject x="360" y="23.5" width="124" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$v^2\ (\text{m}^2/\text{s}^2)$</div></foreignObject>
  <polyline points="370,250 490,95" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="374.5" cy="244" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="379" cy="238" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="388.5" cy="226.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="404.5" cy="205.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="427" cy="176" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="455.5" cy="139" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="484.5" cy="102" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <line x1="337" y1="40" x2="337" y2="270" stroke="#c9c2b2" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <foreignObject x="46" y="281.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{pisteet kaartuvat}$</div></foreignObject>
  <foreignObject x="352.5" y="281.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$\text{pisteet suoralla}$</div></foreignObject>
</svg>

## Tavallisimmat virheet

- **Suora on piirretty ensimmäisen ja viimeisen pisteen kautta.** Huomaat sen, kun lähes kaikki muut pisteet ovat suoran samalla puolella. Käytä ohjelman sovitusta.
- **Pisteet on yhdistetty viivalla.** Kuvaaja näyttää sahalaidalta, eikä viiva ole malli. Valitse näyttötavaksi **Points** ([[ohje:tvt-kuvaaja|Mittauspisteiden kuvaaja]]) ja sovita suora.
- **Suora on pakotettu origon kautta ilman syytä.** Valittuna on **Proportional**, ja pisteet ovat toisessa päässä suoran yläpuolella ja toisessa alapuolella. Valitse yhtälö **Linear** ja tulkitse vakiotermi.
- **Kaartuviin pisteisiin on sovitettu suora.** Poikkeamat muodostavat kaaren eivätkä ole satunnaisia, vaikka $r$ olisi lähellä lukua $1$. Tarkista malli ja linearisoi.
- **Poikkeava piste on poistettu kertomatta.** Lukija ei voi arvioida tulosta. Kirjaa jokainen pois jätetty piste ja syy siihen.
- **Suoraa jatketaan mitatun alueen ulkopuolelle perustelematta.** Mittaukset osoittavat mallin päteväksi vain mitatulla alueella. Kerro, kuinka kauas jatkoit suoraa ja miksi malli pätee siellä.

## Tarkista ennen kuin jatkat

- Suora on sovitettu ohjelmalla oikealle välille, ei ensimmäisen ja viimeisen pisteen kautta.
- Poikkeamat ovat satunnaisia eivätkä muodosta kaarta.
- Jokainen pois jätetty piste on kirjattu perusteluineen.
- Tiedät, kuuluuko malliin vakiotermi, ja olet valinnut sovituksen sen mukaan.
