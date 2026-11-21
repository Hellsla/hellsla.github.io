# Mekaanisen energian säilyminen ja energiaperiaate

> **Miksi** perinteisen ketjuhissillä toimivan vuoristoradan ensimmäinen mäki on yleensä korkein, jos junalle ei anneta myöhemmin lisää energiaa?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: huvipuiston vuoristorata kesäpäivänä. Vasemmalla nousee radan ensimmäinen ja korkein mäki. Punainen juna on juuri noussut sen huipulle. Sen jälkeen rata laskee syvään laaksoon ja nousee toiselle mäelle. Toinen mäki on selvästi matalampi. Sen jälkeen tulee vielä matalampi kolmas mäki. Radan alla on valkoiset tukipylväät, ja taustalla on kuusimetsää." class="fig-hero" style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-8-hero.webp" x="0" y="0" width="1200" height="600" preserveAspectRatio="none"/>
</svg>

## Ydinajatus

### Mekaaninen energia vaihtaa muotoaan
Luvussa *Liike-energia, potentiaalienergia ja mekaaninen energia* opit, että kappaleen mekaaninen energia on liike-energian ja potentiaalienergian summa, $E_\text{mek} = E_\text{k} + E_\text{p}$. Liike-energia on energiaa, joka kappaleella on, koska se liikkuu. Potentiaalienergia on energiaa, joka kappaleella on, koska se on korkealla.

Vuoristoradan vaunu rullaa laaksoon. Sen korkeus pienenee ja nopeus kasvaa. Silloin potentiaalienergiaa muuttuu liike-energiaksi. Kun vaunu nousee vastakkaista rinnettä, liike-energiaa muuttuu takaisin potentiaalienergiaksi. Jos kitkaa ja ilmanvastusta ei ole, vaunu nousee täsmälleen lähtökorkeudelleen ja pysähtyy siellä hetkeksi. Mekaaninen energia on silloin joka hetki yhtä suuri, vaikka sen muoto vaihtuu. Tätä sanotaan **mekaanisen energian säilymiseksi**.

<svg data-fig="laakso" viewBox="0 0 600 380" role="img" aria-label="Kaavakuva, ei mittakaavassa: vuoristoradan vaunu kaarevassa laaksossa. Kitkaa ja ilmanvastusta ei ole. Vaunu lähtee levosta vasemmalta korkeudelta h (kohta 1). Se ohittaa puolen korkeuden (kohta 2) ja laakson pohjan (kohta 3). Oikealla se pysähtyy samalle korkeudelle h (kohta 4). Siniset nuolet ovat vaunun nopeus. Nopeus on suurin pohjalla. Alla on kunkin kohdan energiapalkit: vihreä on potentiaalienergia ja sininen on liike-energia. Kohdissa 1 ja 4 on vain potentiaalienergiaa. Kohdassa 3 on vain liike-energiaa. Kohdassa 2 on puolet kumpaakin. Palkkien summa on joka kohdassa yhtä suuri." style="max-width:100%;font-size:24px">
  <rect x="14" y="236" width="572" height="10" fill="#f1dfb5"/>
  <line x1="227.5" y1="225.5" x2="227.5" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="372.5" y1="225.5" x2="372.5" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="203" y1="219.5" x2="203" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="397" y1="219.5" x2="397" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="179.5" y1="209.5" x2="179.5" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="420.5" y1="209.5" x2="420.5" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="158" y1="195.5" x2="158" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="442" y1="195.5" x2="442" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="139.5" y1="178" x2="139.5" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="460.5" y1="178" x2="460.5" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="124" y1="158" x2="124" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="476" y1="158" x2="476" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="112" y1="135.5" x2="112" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="488" y1="135.5" x2="488" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="104" y1="111.5" x2="104" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <line x1="496" y1="111.5" x2="496" y2="236" stroke="#c4ccd4" stroke-width="3" stroke-linecap="butt"/>
  <path d="M103,102 L104,107 L105.5,112 L107,117 L108.5,121.5 L110.5,126.5 L112,131.5 L114.5,136 L116.5,140.5 L119,145 L121.5,149.5 L124.5,154 L127,158 L130,162.5 L133.5,166.5 L136.5,170.5 L140,174 L143.5,178 L147.5,181.5 L151,185 L155,188 L159,191.5 L163.5,194.5 L167.5,197.5 L172,200 L176.5,202.5 L181,205 L185.5,207.5 L190,209.5 L195,211.5 L199.5,213.5 L204.5,215 L209.5,216.5 L214.5,217.5 L219.5,219 L224.5,220 L229.5,220.5 L234.5,221 L239.5,221.5 L245,222 L250,222 L350,222 L355,222 L360.5,221.5 L365.5,221 L370.5,220.5 L375.5,220 L380.5,219 L385.5,217.5 L390.5,216.5 L395.5,215 L400.5,213.5 L405,211.5 L410,209.5 L414.5,207.5 L419,205 L423.5,202.5 L428,200 L432.5,197.5 L436.5,194.5 L441,191.5 L445,188 L449,185 L452.5,181.5 L456.5,178 L460,174 L463.5,170.5 L466.5,166.5 L470,162.5 L473,158 L475.5,154 L478.5,149.5 L481,145 L483.5,140.5 L485.5,136 L488,131.5 L489.5,126.5 L491.5,121.5 L493,117 L494.5,112 L496,107 L497,102" fill="none" stroke="#8a96a3" stroke-width="6" stroke-linejoin="round"/>
  <path d="M103,101 L104,106 L105.5,111 L107,116 L108.5,120.5 L110.5,125.5 L112,130.5 L114.5,135 L116.5,139.5 L119,144 L121.5,148.5 L124.5,153 L127,157 L130,161.5 L133.5,165.5 L136.5,169.5 L140,173 L143.5,177 L147.5,180.5 L151,184 L155,187 L159,190.5 L163.5,193.5 L167.5,196.5 L172,199 L176.5,201.5 L181,204 L185.5,206.5 L190,208.5 L195,210.5 L199.5,212.5 L204.5,214 L209.5,215.5 L214.5,216.5 L219.5,218 L224.5,219 L229.5,219.5 L234.5,220 L239.5,220.5 L245,221 L250,221 L350,221 L355,221 L360.5,220.5 L365.5,220 L370.5,219.5 L375.5,219 L380.5,218 L385.5,216.5 L390.5,215.5 L395.5,214 L400.5,212.5 L405,210.5 L410,208.5 L414.5,206.5 L419,204 L423.5,201.5 L428,199 L432.5,196.5 L436.5,193.5 L441,190.5 L445,187 L449,184 L452.5,180.5 L456.5,177 L460,173 L463.5,169.5 L466.5,165.5 L470,161.5 L473,157 L475.5,153 L478.5,148.5 L481,144 L483.5,139.5 L485.5,135 L488,130.5 L489.5,125.5 L491.5,120.5 L493,116 L494.5,111 L496,106 L497,101" fill="none" stroke="#ffffff" stroke-width="1.5" stroke-linejoin="round"/>
  <line x1="78" y1="122" x2="540" y2="122" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="52" y1="222" x2="52" y2="122" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M52,122 l-6,12 h12 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M52,222 l-6,-12 h12 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="18" y="157.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$h$</div></foreignObject>
  <line x1="40" y1="222" x2="78" y2="222" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <circle cx="108.5" cy="112.5" r="3.12" fill="#1f2933"/>
  <circle cx="114.5" cy="129.5" r="3.12" fill="#1f2933"/>
  <path d="M108,106.5 L118,134.5 L129.5,130.5 L119.5,102 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="127.5" cy="110.5" r="4.16" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="131" cy="120.5" r="4.16" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="134.5" cy="163.5" r="3.12" fill="#1f2933"/>
  <circle cx="146.5" cy="177" r="3.12" fill="#1f2933"/>
  <path d="M131.5,158 L151.5,180 L161,172 L141,149.5 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="151" cy="154.5" r="4.16" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="158" cy="162" r="4.16" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="146" y1="138" x2="166" y2="160.5" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M173.5,168.5 L161.5,163 L169.5,156 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="291" cy="219" r="3.12" fill="#1f2933"/>
  <circle cx="309" cy="219" r="3.12" fill="#1f2933"/>
  <path d="M285,217.5 L315,217.5 L315,205 L285,205 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="295.5" cy="200.5" r="4.16" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="306" cy="200.5" r="4.16" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="300" y1="192" x2="347" y2="192" stroke="#1971c2" stroke-width="3" stroke-linecap="butt"/>
  <path d="M358,192 L346,197.5 L346,186.5 Z" fill="#1971c2" stroke-linejoin="round"/>
  <circle cx="485.5" cy="129.5" r="3.12" fill="#1f2933"/>
  <circle cx="491.5" cy="112.5" r="3.12" fill="#1f2933"/>
  <path d="M482,134.5 L492,106.5 L480.5,102 L470.5,130.5 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="469.5" cy="119" r="4.16" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="473" cy="109" r="4.16" fill="#f1dfb5" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="76.5" y="73.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <foreignObject x="94" y="151.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <foreignObject x="264" y="161.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <foreignObject x="505.5" y="73.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <foreignObject x="392" y="173.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <line x1="70" y1="352" x2="560" y2="352" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="108" y="282" width="20" height="70" fill="#2b8a3e"/>
  <foreignObject x="120" y="249.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <rect x="228" y="317" width="20" height="35" fill="#2b8a3e"/>
  <rect x="252" y="317" width="20" height="35" fill="#1971c2"/>
  <foreignObject x="240" y="249.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <rect x="372" y="282" width="20" height="70" fill="#1971c2"/>
  <foreignObject x="360" y="249.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <rect x="468" y="282" width="20" height="70" fill="#2b8a3e"/>
  <foreignObject x="480" y="249.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <rect x="24" y="290" width="16" height="16" fill="#2b8a3e"/>
  <foreignObject x="46" y="283.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#2b8a3e">$E_\text{p}$</div></foreignObject>
  <rect x="24" y="326" width="16" height="16" fill="#1971c2"/>
  <foreignObject x="46" y="319.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$E_\text{k}$</div></foreignObject>
</svg>

Kaikki vaunuun vaikuttavat voimat eivät muuta sen energiaa. Paino tekee työtä, kun vaunu laskee tai nousee. Juuri tämä työ muuttaa potentiaalienergiaa liike-energiaksi ja takaisin. Radan tukivoima on kohtisuorassa radan pintaa vastaan. Siksi se on kohtisuorassa myös liikettä vastaan, eikä se tee työtä. Mekaaninen energia säilyy siis silloin, kun vain paino tekee työtä. Radan muoto ei ratkaise sitä. Vaunun nopeus missä tahansa kohdassa riippuu vain siitä, kuinka paljon alemmas vaunu on laskeutunut lähtökohdasta. Nopeus ei riipu radan muodosta eikä vaunun massasta.

```pysahdy
Kaksi vaunua lähtee levosta saman mäen huipulta kitkattomalle radalle. Toinen vaunu on kaksi kertaa raskaampi. Kumpi on laakson pohjalla nopeampi?
---
Ne ovat yhtä nopeita. Nopeus riippuu vain siitä, kuinka paljon alemmas vaunu on laskeutunut. Massa tai radan muoto ei vaikuta siihen.
```

### Työ siirtää energiaa
Luvussa *Työ ja energia* opit, että voima tekee työtä, kun kappale liikkuu voiman suuntaan. Nyt tarvitaan myös työn etumerkki. Etumerkki kertoo, onko työ positiivista vai negatiivista.

- Voima tekee positiivista työtä, kun sillä on liikkeen suuntainen komponentti. Silloin voima lisää kappaleen energiaa.
- Liikettä vastustava voima, kuten kitka, tekee negatiivista työtä. Silloin voima vähentää kappaleen energiaa.
- Liikettä vastaan kohtisuora voima, kuten tukivoima, ei tee työtä lainkaan.

Työn yksikkö on sama kuin energian yksikkö, joule.

<svg data-fig="tyo" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva kolmesta tilanteesta. Joka tilanteessa laatikko liikkuu lattialla oikealle. Sininen nuoli on laatikon nopeus. Vasemmalla laatikkoa vedetään liikkeen suuntaan voimalla F. Voima tekee silloin positiivista työtä, W &gt; 0. Keskellä kitkavoima F_μ vaikuttaa lattian pinnasta liikettä vastaan. Se tekee negatiivista työtä, W &lt; 0. Oikealla lattian tukivoima N on kohtisuorassa liikettä vastaan. Se ei tee työtä, W = 0." style="max-width:100%;font-size:24px">
  <image href="pics/fy4/fy4-8-tyo.webp" x="1.2" y="0" width="597" height="338.3" preserveAspectRatio="none"/>
  <foreignObject x="140" y="47.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="157.5" y="139.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}$</div></foreignObject>
  <foreignObject x="77.5" y="247.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W > 0$</div></foreignObject>
  <foreignObject x="10" y="281.5" width="180" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{liikkeen suuntaan}$</div></foreignObject>
  <foreignObject x="340" y="47.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="215.5" y="169.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#c92a2a">$\overline{F}_\mu$</div></foreignObject>
  <foreignObject x="277.5" y="247.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W < 0$</div></foreignObject>
  <foreignObject x="210" y="281.5" width="180" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{liikettä vastaan}$</div></foreignObject>
  <foreignObject x="540" y="47.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
  <foreignObject x="528" y="99.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#c92a2a">$\overline{N}$</div></foreignObject>
  <foreignObject x="477.5" y="247.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W = 0$</div></foreignObject>
  <foreignObject x="410" y="281.5" width="180" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kohtisuoraan}$</div></foreignObject>
</svg>

```pysahdy
Lapsi liukuu pulkalla alas rinnettä. Tekeekö lumen tukivoima työtä? Entä kitka?
---
Tukivoima on kohtisuorassa liikettä vastaan, joten se ei tee työtä. Kitka vastustaa liikettä. Siksi se tekee negatiivista työtä ja vähentää mekaanista energiaa.
```

### Kitka muuttaa mekaanista energiaa sisäenergiaksi
Todellisessa vuoristoradassa pyörien vierimisvastus ja ilmanvastus vastustavat liikettä koko matkan ajan. Ne tekevät negatiivista työtä. Vaunun mekaaninen energia pienenee juuri tämän työn verran. Energia ei katoa. Se muuttuu pyörien, kiskojen ja ilman sisäenergiaksi, jolloin ne lämpenevät hieman. Sisäenergia on aineen hiukkasten energiaa. Kokonaisenergia säilyy aina. Mekaaninen energia säilyy vain, kun kitkaa ja ilmanvastusta ei ole tai ne ovat niin pieniä, että ne voi jättää huomiotta.

Painon eli painovoiman ja kitkan eron muistat luvusta *Liike-energia, potentiaalienergia ja mekaaninen energia*: paino on **konservatiivinen voima**. Uutta on se, mitä tästä seuraa energian laskemiselle. Painon tekemä työ riippuu vain korkeuserosta. Kun kappale palaa samalle korkeudelle, se saa takaisin saman energian, vaikka se olisi kulkenut mitä reittiä tahansa. Siksi painoon liittyy potentiaalienergia. Kitkan ja ilmanvastuksen tekemä negatiivinen työ kasvaa jokaisella kuljetulla metrillä. Siksi se riippuu reitistä. Tällaista voimaa sanotaan **ei-konservatiiviseksi voimaksi**. Sille ei voi määritellä potentiaalienergiaa.

```pysahdy
Auto jarruttaa pysähdyksiin. Mihin sen liike-energia muuttuu?
---
Jarrujen, renkaiden ja tien sisäenergia kasvaa, ja ne lämpenevät. Energia ei katoa.
```

### Vastaus alun kysymykseen
Ketjuhissi nostaa junan ensimmäisen mäen huipulle. Sen jälkeen junalla on vain se mekaaninen energia, jonka se sai noston aikana. Mikään ei lisää sitä. Vastusvoimat vähentävät sitä jokaisella metrillä. Jos seuraava mäki olisi yhtä korkea kuin ensimmäinen, juna ei pääsisi sen huipulle. Jokaisen myöhemmän mäen täytyy olla matalampi kuin ensimmäinen. Sen täytyy olla matalampi myös kuin korkeus, jolle jäljellä oleva energia riittäisi. Silloin junalle jää huipulla vielä liike-energiaa.

## Kaava: Mekaniikan energiaperiaate

### Työ ja liike-energia
Kappale liikkuu suoraviivaisesti samaan suuntaan matkan $s$, ja siihen vaikuttaa vakiovoima $\overline{F}$. Voiman tekemä työ on silloin
```kaavat
voiman tekemä työ :: W = F\, s
```
missä $F$ on voiman liikkeen suuntainen komponentti ($\text{N}$) ja $s$ on kuljettu matka ($\text{m}$). Komponentti on negatiivinen, kun se osoittaa liikettä vastaan. Työn yksikkö on $1\,\text{N}\cdot\text{m} = 1\,\text{J}$.

Oletetaan, että kappale liikkuu $x$-akselia pitkin ja siihen vaikuttaa akselin suuntainen vakio kokonaisvoima $\Sigma F_x$. Silloin kappale kiihtyy tasaisesti, ja sen kiihtyvyys on $a = \tfrac{\Sigma F_x}{m}$. Luvussa *Kiihtyvyys ja tasaisesti kiihtyvä liike* opit kaksi asiaa. Tasaisesti kiihtyvässä liikkeessä kiihtyvyys on $a = \tfrac{v_2 - v_1}{t}$. Siirtymä on keskinopeus kertaa aika, $\Delta x = \tfrac{v_1 + v_2}{2}\,t$. Siirtymä kertoo, kuinka paljon ja mihin suuntaan paikka muuttuu. Nopeuksilla $v_1$ ja $v_2$ on tässä etumerkki: negatiivinen nopeus tarkoittaa liikettä akselin negatiiviseen suuntaan. Kun yhtälöt kerrotaan keskenään, aika supistuu pois:
```latex
\begin{aligned}
&a\,\Delta x = \frac{v_2 - v_1}{t} \cdot \frac{v_1 + v_2}{2}\,t \\
&\phantom{a\,\Delta x} = \tfrac12 \left(v_2^2 - v_1^2\right)
\end{aligned}
```
Kerro yhtälö puolittain massalla $m$ ja sijoita $ma = \Sigma F_x$. Saat $\Sigma F_x\, \Delta x = \tfrac{1}{2} m v_2^2 - \tfrac{1}{2} m v_1^2$ eli $\Sigma F_x\, \Delta x = \Delta E_\text{k}$.

Siirtymä $\Delta x$ ja kuljettu matka $s$ ovat eri asioita. Jos kappale liikkuu koko ajan samaan suuntaan, siirtymän suuruus on sama kuin kuljettu matka. Silloin kokonaisvoiman työ on $\Sigma F\, s$. Jos kappale kääntyy takaisin, kuljettu matka on pidempi kuin siirtymä. Esimerkki on ylös heitetty pallo. Silloin vakiovoiman työ lasketaan siirtymästä, $W = F_x\, \Delta x$. Toinen tapa on laskea työ osissa niin, että jokaisessa osassa kappale liikkuu yhteen suuntaan. Kun kitka ja ilmanvastus vastustavat kappaleen liikettä, niiden tekemä työ on negatiivinen. Sen itseisarvo kasvaa kuljetun matkan mukana. Kummassakin tapauksessa kokonaisvoiman tekemä työ on yhtä suuri kuin liike-energian muutos:
```kaavat
työperiaate :: E_{\text{k}0} + W = E_\text{k}
```
missä $E_{\text{k}0}$ on liike-energia alussa ja $E_\text{k}$ on liike-energia lopussa ($\text{J}$). $W$ on kaikkien kappaleeseen vaikuttavien voimien yhdessä tekemä työ ($\text{J}$). Tämä on **työperiaate**. Kokonaistyö on siis liike-energian muutos: $W = \Delta E_\text{k}$. Esimerkki: kärryn massa on $2{,}0\,\text{kg}$. Kokonaisvoima $12\,\text{N}$ kiihdyttää sitä levosta matkan $3{,}0\,\text{m}$. Voima tekee työn $36\,\text{J}$, ja kärryn nopeus on lopussa $6{,}0\,\text{m/s}$.

### Energiaperiaate
Kokonaistyö jaetaan kahteen osaan. Toinen osa on painon tekemä työ $W_G$. Toinen osa on kaikkien muiden voimien tekemä työ. Muita voimia ovat esimerkiksi kitka, ilmanvastus, vetävä köysi ja työntävä käsi. Kun kappale laskeutuu korkeuden $h$, paino tekee työn $mgh$. Potentiaalienergia pienenee saman verran, joten $W_G = -\Delta E_\text{p}$. Kun painon työ kirjoitetaan näin potentiaalienergian muutoksena, työperiaatteen työksi $W$ jää vain muiden voimien kuin painon tekemä työ. Saat **mekaniikan energiaperiaatteen**:
```kaavat
mekaniikan energiaperiaate :: E_{\text{p}0} + E_{\text{k}0} + W = E_\text{p} + E_\text{k}
```
missä indeksi $0$ tarkoittaa alkutilannetta. Suure ilman indeksiä tarkoittaa lopputilannetta. Lisäksi $E_\text{k} = \tfrac{1}{2} mv^2$ on liike-energia ja $E_\text{p} = mgh$ on potentiaalienergia korkeudella $h$ valitusta nollatasosta. Suure $W$ on muiden voimien kuin painon tekemä työ ($\text{J}$). Sanoin: mekaanisen energian muutos on yhtä suuri kuin muiden voimien kuin painon tekemä työ, $\Delta E_\text{mek} = W$. Nollatason saa valita vapaasti, esimerkiksi tilanteen alimpaan kohtaan, koska vain korkeuden muutos vaikuttaa tulokseen.

<svg data-fig="palkit" viewBox="0 0 600 360" role="img" aria-label="Energiapalkit, kaavakuva mittakaavassa. Alussa kappaleella on vain potentiaalienergiaa E_p0. Liike-energia E_k0 on nolla. Kitka tekee negatiivisen työn W. Sen palkki osoittaa nollatasosta alaspäin. Lopussa kappaleella on vain liike-energiaa E_k. Potentiaalienergia E_p on nolla. Katkoviiva näyttää alun mekaanisen energian korkeuden. Loppuenergia on alkuenergiaa pienempi juuri kitkan työn verran." style="max-width:100%;font-size:24px">
  <foreignObject x="78.5" y="11.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{alussa}$</div></foreignObject>
  <foreignObject x="432.5" y="11.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lopussa}$</div></foreignObject>
  <line x1="30" y1="232" x2="570" y2="232" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <rect x="140" y="72" width="40" height="160" fill="#2b8a3e"/>
  <rect x="280" y="232" width="40" height="64" fill="#e8590c"/>
  <rect x="420" y="136" width="40" height="96" fill="#1971c2"/>
  <foreignObject x="220" y="135.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="360" y="135.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$=$</div></foreignObject>
  <line x1="180" y1="72" x2="540" y2="72" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <path d="M470,72 h8 V136 h-8" fill="none" stroke="#e8590c" stroke-width="2.5" stroke-linejoin="round"/>
  <foreignObject x="486" y="89.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#e8590c">$|W|$</div></foreignObject>
  <foreignObject x="57.5" y="317.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$E_{\text{k}0}$</div></foreignObject>
  <foreignObject x="137.5" y="317.5" width="45" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$E_{\text{p}0}$</div></foreignObject>
  <foreignObject x="290" y="317.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#e8590c">$W$</div></foreignObject>
  <foreignObject x="423.5" y="317.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$E_\text{k}$</div></foreignObject>
  <foreignObject x="503.5" y="317.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#2b8a3e">$E_\text{p}$</div></foreignObject>
  <foreignObject x="70" y="199.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$0$</div></foreignObject>
  <foreignObject x="510" y="199.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480">$0$</div></foreignObject>
</svg>

Kappale liikkuu paikallaan olevaa alustaa tai ilmaa vasten. Silloin kitka ja ilmanvastus vastustavat liikettä ja tekevät negatiivista työtä. Ne pienentävät mekaanista energiaa. (Liikkuva alusta tai tuuli voi tehdä myös positiivista työtä. Esimerkiksi kuljetinhihna kantaa laatikkoa.) Vetävä köysi tai moottori voi tehdä positiivista työtä ja kasvattaa mekaanista energiaa. Näin tekee ketjuhissi, joka nostaa junaa. Jos muut voimat eivät tee työtä, $W = 0$. Silloin energiaperiaatteesta tulee **mekaanisen energian säilymislaki**:
```kaavat
mekaanisen energian säilymislaki :: E_{\text{p}0} + E_{\text{k}0} = E_\text{p} + E_\text{k}
```
Kappale lähtee levosta korkeudelta $h$ ja laskeutuu nollatasolle. Säilymislaista $mgh = \tfrac{1}{2} mv^2$ saadaan $v = \sqrt{2gh}$. Massa supistuu pois, joten nopeus ei riipu massasta.

## Esimerkki
Lapsi laskee pulkalla mäen alas. Lapsen ja pulkan yhteinen massa on $32\,\text{kg}$. Pulkka lähtee levosta mäen huipulta. Huippu on $5{,}0\,\text{m}$ korkeammalla kuin mäen juuri. Mäen juurella pulkan nopeudeksi mitataan $7{,}6\,\text{m/s}$. Kuinka suuren työn kitka ja ilmanvastus tekevät yhteensä pulkkaan laskun aikana?

<!-- vaihe -->

**Tunnetut ja kysytty.** $m = 32\,\text{kg}$, korkeusero $h = 5{,}0\,\text{m}$, alkunopeus $v_1 = 0$, loppunopeus $v_2 = 7{,}6\,\text{m/s}$ ja $g = 9{,}81\,\text{m/s}^2$.

Kysytään kitkan ja ilmanvastuksen yhdessä tekemää työtä $W$.

<!-- vaihe -->

**Periaate.** Pulkkaan vaikuttavat paino, lumen tukivoima, kitka ja ilmanvastus. Tukivoima on kohtisuorassa liikettä vastaan, joten se ei tee työtä. Painon työ otetaan huomioon potentiaalienergian muutoksena. Kitka ja ilmanvastus ovat muita voimia kuin paino, joten käytetään energiaperiaatetta. Nollataso valitaan mäen juurelle.

<!-- vaihe -->

**Kaava ratkaistuna.** Alussa $E_{\text{k}0} = 0$ ja $E_{\text{p}0} = mgh$. Lopussa $E_\text{k} = \tfrac{1}{2} mv_2^2$ ja $E_\text{p} = 0$:
```latex
\begin{aligned}
&mgh + W = \tfrac{1}{2} m v_2^2 \\
&W = \tfrac{1}{2} m v_2^2 - mgh
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Niitä ei tarvita. Kaikki suureet ovat SI-yksiköissä, ja $1\,\text{kg}\cdot\tfrac{\text{m}^2}{\text{s}^2} = 1\,\text{J}$.

<!-- vaihe -->

**Sijoitus.** Lasketaan ensin loppuhetken liike-energia ja alun potentiaalienergia. Sitten lasketaan niiden erotus:
```latex
\begin{aligned}
&\tfrac{1}{2} m v_2^2 \\
&= \tfrac12 \cdot 32\,\text{kg} \cdot \left(7{,}6\,\tfrac{\text{m}}{\text{s}}\right)^2 \\
&= 924{,}16\,\text{J} \\[6pt]
&mgh \\
&= 32\,\text{kg} \cdot 9{,}81\,\tfrac{\text{m}}{\text{s}^2} \cdot 5{,}0\,\text{m} \\
&= 1569{,}6\,\text{J} \\[6pt]
&W \\
&= 924{,}16\,\text{J} - 1569{,}6\,\text{J} \\
&= -645{,}44\,\text{J}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Kitka ja ilmanvastus tekevät yhteensä työn $W \approx -6{,}5 \cdot 10^2\,\text{J}$. Tulos ilmoitetaan kahdella merkitsevällä numerolla, koska korkeus $5{,}0\,\text{m}$ ja nopeus $7{,}6\,\text{m/s}$ on annettu kahdella numerolla. Työ on negatiivinen, koska kitka ja ilmanvastus vastustavat liikettä. Noin $650\,\text{J}$ mekaanista energiaa muuttui lumen, jalasten ja ilman sisäenergiaksi.

<!-- vaihe -->

**Järkevyys.** Ilman kitkaa ja ilmanvastusta pulkan nopeus olisi mäen juurella $\sqrt{2gh} \approx 9{,}9\,\text{m/s}$. Mitattu $7{,}6\,\text{m/s}$ on pienempi, kuten pitääkin. Mekaanista energiaa muuttui sisäenergiaksi noin $41\,\%$ alun potentiaalienergiasta. Oletetaan, että rinne on $24\,\text{m}$ pitkä. Silloin keskimääräinen vastusvoima on $645\,\text{J} : 24\,\text{m} \approx 27\,\text{N}$. Se on alle kymmenesosa painosta $314\,\text{N}$, mikä on uskottava liukuvalle pulkalle.

## Yleinen virhekäsitys
Moni ajattelee, että raskaampi kappale on mäen alla nopeampi. Oletetaan, että kitkan ja ilmanvastuksen voi jättää huomiotta. Silloin massa supistuu säilymislaista pois: täysi ja tyhjä vaunu ovat laakson pohjalla yhtä nopeita. Raskaammalla vaunulla on pohjalla enemmän liike-energiaa. Sillä oli kuitenkin alussa myös enemmän potentiaalienergiaa.

Toinen virhe on sanoa, että kitka hävittää energiaa. Kitka pienentää mekaanista energiaa. Yhtä suuri määrä energiaa siirtyy kuitenkin sisäenergiaksi, ja kokonaisenergia säilyy. Kolmas virhe on laskea kitkan työ korkeuserosta. Kitkan työ on kitkavoima kertaa kuljettu matka pitkin rataa. Oletetaan, että vastusvoima on yhtä suuri. Silloin pitkällä loivalla radalla muuttuu sisäenergiaksi enemmän mekaanista energiaa kuin lyhyellä jyrkällä radalla, vaikka korkeusero olisi sama.

## Tiivistelmä
- Mekaaninen energia $E_\text{mek} = E_\text{k} + E_\text{p}$ säilyy, kun vain paino tekee työtä. Silloin kitkan ja ilmanvastuksen voi jättää huomiotta, eikä mikään vedä tai työnnä kappaletta. Tukivoima ei tee työtä, koska se on kohtisuorassa liikettä vastaan.
- Voima tekee työtä liikkeen suuntaisella komponentillaan, $W = F s$, kun kappale liikkuu yhteen suuntaan. Työ on positiivista liikkeen suuntaan ja negatiivista liikettä vastaan.
- Kokonaisvoiman tekemä työ on yhtä suuri kuin liike-energian muutos, $W = \Delta E_\text{k}$.
- Energiaperiaate: mekaanisen energian muutos on muiden voimien kuin painon tekemä työ, $\Delta E_\text{mek} = W$. Kitka ja ilmanvastus muuttavat mekaanista energiaa sisäenergiaksi, ja kokonaisenergia säilyy.
- Paino on konservatiivinen voima, koska sen työ riippuu vain korkeuserosta. Kitka ja ilmanvastus ovat ei-konservatiivisia voimia, koska niiden työ kasvaa kuljetun matkan mukana.
