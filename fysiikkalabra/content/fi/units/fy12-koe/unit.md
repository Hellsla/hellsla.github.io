# Ylioppilaskoe ja vastaustekniikka

> **Miksi** kaksi vastausta, joissa on sama lopputulos, voi saada aivan eri pisteet?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: koepöytä ylhäältä vinosti nähtynä. Pöydällä on kannettava tietokone, jonka näytöllä on kuvaaja: mittauspisteet ja niihin sovitettu nouseva suora. Tietokoneen vieressä ovat laskin, ruutuvihko, jossa on lyijykynällä piirretty kappale ja nuolia, lyijykynä ja vesipullo. Seinällä on kello. Kuvassa ei ole tekstiä." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy12koe-h-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#e3dccb"/></linearGradient><linearGradient id="fy12koe-h-desk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9b26a"/><stop offset="1" stop-color="#c79a52"/></linearGradient><linearGradient id="fy12koe-h-bottle" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="#f6f1e6"/>
  <rect x="0" y="0" width="1200" height="330" fill="url(#fy12koe-h-wall)"/>
  <rect x="0" y="330" width="1200" height="270" fill="url(#fy12koe-h-desk)"/>
  <line x1="0" y1="330" x2="1200" y2="330" stroke="#a97a35" stroke-width="4" stroke-linecap="butt"/>
  <circle cx="1040" cy="120" r="62" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <circle cx="1040" cy="120" r="52" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <line x1="1040" y1="78" x2="1040" y2="72" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="1061" y1="83.5" x2="1064" y2="78.5" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="1076.5" y1="99" x2="1081.5" y2="96" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="1082" y1="120" x2="1088" y2="120" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="1076.5" y1="141" x2="1081.5" y2="144" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="1061" y1="156.5" x2="1064" y2="161.5" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="1040" y1="162" x2="1040" y2="168" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="1019" y1="156.5" x2="1016" y2="161.5" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="1003.5" y1="141" x2="998.5" y2="144" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="998" y1="120" x2="992" y2="120" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="1003.5" y1="99" x2="998.5" y2="96" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="1019" y1="83.5" x2="1016" y2="78.5" stroke="#6b7480" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="1040" y1="120" x2="1017.5" y2="107" stroke="#1f2933" stroke-width="5" stroke-linecap="round"/>
  <line x1="1040" y1="120" x2="1074.5" y2="100" stroke="#1f2933" stroke-width="3" stroke-linecap="round"/>
  <circle cx="1040" cy="120" r="5" fill="#c92a2a"/>
  <path d="M380,92 L820,92 Q832,92 832,104 L832,372 L368,372 L368,104 Q368,92 380,92 Z" fill="#6c757d" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <rect x="388" y="112" width="424" height="244" rx="4" fill="#ffffff"/>
  <line x1="488.5" y1="330" x2="488.5" y2="140" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="546.5" y1="330" x2="546.5" y2="140" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="605" y1="330" x2="605" y2="140" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="663.5" y1="330" x2="663.5" y2="140" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="721.5" y1="330" x2="721.5" y2="140" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="292" x2="780" y2="292" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="254" x2="780" y2="254" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="216" x2="780" y2="216" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="178" x2="780" y2="178" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="429" y1="330" x2="786" y2="330" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M796,330 L785,335 L785,325 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="430" y1="331" x2="430" y2="134" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M430,124 L435,135 L425,135 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="430" y1="313.5" x2="774.5" y2="149.5" stroke="#1971c2" stroke-width="3.5" stroke-linecap="round"/>
  <circle cx="430" cy="312.5" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="484" cy="289.5" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="537.5" cy="260.5" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="591.5" cy="237" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="645.5" cy="211" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="699" cy="186.5" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="753" cy="159" r="7" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <path d="M330,372 L870,372 L920,420 L280,420 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <line x1="330" y1="381" x2="870" y2="381" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt" stroke-dasharray="18 6"/>
  <line x1="342" y1="393" x2="858" y2="393" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt" stroke-dasharray="18 6"/>
  <line x1="354" y1="405" x2="846" y2="405" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt" stroke-dasharray="18 6"/>
  <rect x="560" y="404" width="80" height="10" rx="3" fill="#8a96a3"/>
  <path d="M70,430 L300,402 L330,560 L96,590 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="73" y1="448" x2="303.5" y2="419.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="76" y1="465.5" x2="306.5" y2="437" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="78.5" y1="483.5" x2="310" y2="454.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="81.5" y1="501" x2="313.5" y2="472" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="84.5" y1="519" x2="316.5" y2="490" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="87.5" y1="536.5" x2="320" y2="507.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="90" y1="554.5" x2="323.5" y2="525" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="93" y1="572" x2="326.5" y2="542.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="99" y1="426.5" x2="125" y2="586" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="127.5" y1="423" x2="154.5" y2="582.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="156" y1="419.5" x2="184" y2="579" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="185" y1="416" x2="213" y2="575" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="214" y1="412.5" x2="242" y2="571" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="242.5" y1="409" x2="271.5" y2="567.5" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="271" y1="405.5" x2="301" y2="564" stroke="#d0e6fb" stroke-width="1.5" stroke-linecap="butt"/>
  <path d="M165,478 L225,470 L232,512 L172,520 Z" fill="none" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="199" y1="495" x2="203.5" y2="536" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M205,548 L197.5,535.5 L209.5,534.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="199" y1="495" x2="193.5" y2="458" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M192,446 L199.5,458 L188,459.5 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <line x1="199" y1="495" x2="256" y2="487.5" stroke="#c92a2a" stroke-width="3.5" stroke-linecap="butt"/>
  <path d="M268,486 L256,493.5 L254.5,482 Z" fill="#c92a2a" stroke-linejoin="round"/>
  <path d="M318,452 L352,410 L362,418 L328,460 Z" fill="#ffc078" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M318,452 L328,460 L312,470 Z" fill="#f1dfb5" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M352,410 L362,418 L368,410 L358,402 Z" fill="#c92a2a" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M930,440 L1060,424 L1082,566 L952,582 Z" fill="#1f2933" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="M948,452 L1046,440 L1052,478 L954,490 Z" fill="#b2f2bb" stroke-linejoin="round"/>
  <rect x="958" y="502" width="17" height="14" rx="3" fill="#c4ccd4"/>
  <rect x="982" y="499" width="17" height="14" rx="3" fill="#c4ccd4"/>
  <rect x="1006" y="496" width="17" height="14" rx="3" fill="#c4ccd4"/>
  <rect x="1030" y="493" width="17" height="14" rx="3" fill="#e8590c"/>
  <rect x="961" y="524" width="17" height="14" rx="3" fill="#c4ccd4"/>
  <rect x="985" y="521" width="17" height="14" rx="3" fill="#c4ccd4"/>
  <rect x="1009" y="518" width="17" height="14" rx="3" fill="#c4ccd4"/>
  <rect x="1033" y="515" width="17" height="14" rx="3" fill="#e8590c"/>
  <rect x="964.5" y="546" width="17" height="14" rx="3" fill="#c4ccd4"/>
  <rect x="988.5" y="543" width="17" height="14" rx="3" fill="#c4ccd4"/>
  <rect x="1012.5" y="540" width="17" height="14" rx="3" fill="#c4ccd4"/>
  <rect x="1036.5" y="537" width="17" height="14" rx="3" fill="#e8590c"/>
  <rect x="1118" y="330" width="46" height="200" rx="12" fill="url(#fy12koe-h-bottle)" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="1126" y="300" width="30" height="32" rx="5" fill="#1971c2" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="1126" y1="380" x2="1156" y2="380" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
</svg>

## Koe ja ajankäyttö {Koe}

### Sähköinen koe
Fysiikan koe tehdään tietokoneella. Vastaus kirjoitetaan tekstinä, kaavat kaavaeditorilla, ja kuvaajan tai piirroksen voi liittää vastaukseen kuvakaappauksena. Kokeen rakenne, tehtävien ja vastausten määrä sekä sallitut apuvälineet ja ohjelmat on kerrottu ylioppilastutkintolautakunnan määräyksissä ja kokeen omissa ohjeissa. Tarkista ne ajantasaisina ennen koetta ja harjoittele kokeen ohjelmilla etukäteen.

### Ajankäyttö ja tehtävien valinta
Lue kokeen ohjeet ensin: niissä sanotaan, mihin tehtäviin vastataan ja kuinka moneen. Selaa sitten kaikki tehtävät ja merkitse, mitkä osaat varmasti. Jos voit valita, valitse tehtävät, joiden ilmiön tunnistat ja joiden kaikkiin osiin pystyt vastaamaan. Jaa aika tehtävien pisteiden suhteen ja jätä loppuun aikaa tarkistukselle. Jos jumiudut, kirjoita se, minkä osaat, ja palaa tehtävään myöhemmin.

## Täydellinen ratkaisu {Ydinajatus}

**Hyvästä vastauksesta lukija näkee, miten tulokseen päädyttiin, eikä vain lopputulosta.** Siksi jokaisessa laskussa kirjoitetaan näkyviin samat seitsemän vaihetta, joita tämän kirjan esimerkit ja mallivastaukset käyttävät. Perustelu kertoo, miksi juuri tämä laki pätee juuri tässä tilanteessa: kitkaa ei ole, olomuoto ei muutu, tilavuus pysyy vakiona.

<svg data-fig="steps" viewBox="0 0 600 452" role="img" aria-label="Kaavio: täydellisen ratkaisun seitsemän vaihetta allekkain numeroituina kortteina. 1 Annettu ja kysytty: suureet yksiköineen. 2 Periaate: laki ja miksi se pätee. 3 Kaava ratkaistuna: kysytty symboleilla. 4 Muunnokset: perusyksiköihin. 5 Sijoitus: luvut yksiköineen. 6 Vastaus: yksikkö ja tarkkuus. 7 Järkevyys: arvio tai vertailu. Korttien välissä on nuolet ylhäältä alas." style="max-width:100%;font-size:24px">
  <rect x="16" y="14" width="568" height="50" rx="8" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <circle cx="46" cy="39" r="17" fill="#1f2933"/>
  <foreignObject x="36.5" y="26" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px;color:#ffffff">$1$</div></foreignObject>
  <foreignObject x="76" y="24.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Annettu ja kysytty}$</div></foreignObject>
  <foreignObject x="367" y="26.5" width="205" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px;color:#6b7480">$\text{suureet yksiköineen}$</div></foreignObject>
  <line x1="46" y1="64" x2="46" y2="76" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <rect x="16" y="76" width="568" height="50" rx="8" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <circle cx="46" cy="101" r="17" fill="#1f2933"/>
  <foreignObject x="36.5" y="88" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px;color:#ffffff">$2$</div></foreignObject>
  <foreignObject x="76" y="86.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Periaate}$</div></foreignObject>
  <foreignObject x="367" y="88.5" width="205" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px;color:#6b7480">$\text{laki ja miksi se pätee}$</div></foreignObject>
  <line x1="46" y1="126" x2="46" y2="138" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <rect x="16" y="138" width="568" height="50" rx="8" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <circle cx="46" cy="163" r="17" fill="#1f2933"/>
  <foreignObject x="36.5" y="150" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px;color:#ffffff">$3$</div></foreignObject>
  <foreignObject x="76" y="148.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Kaava ratkaistuna}$</div></foreignObject>
  <foreignObject x="367" y="150.5" width="205" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px;color:#6b7480">$\text{kysytty symboleilla}$</div></foreignObject>
  <line x1="46" y1="188" x2="46" y2="200" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <rect x="16" y="200" width="568" height="50" rx="8" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <circle cx="46" cy="225" r="17" fill="#1f2933"/>
  <foreignObject x="36.5" y="212" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px;color:#ffffff">$4$</div></foreignObject>
  <foreignObject x="76" y="210.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Muunnokset}$</div></foreignObject>
  <foreignObject x="400" y="212.5" width="172" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px;color:#6b7480">$\text{perusyksiköihin}$</div></foreignObject>
  <line x1="46" y1="250" x2="46" y2="262" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <rect x="16" y="262" width="568" height="50" rx="8" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <circle cx="46" cy="287" r="17" fill="#1f2933"/>
  <foreignObject x="36.5" y="274" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px;color:#ffffff">$5$</div></foreignObject>
  <foreignObject x="76" y="272.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Sijoitus}$</div></foreignObject>
  <foreignObject x="389" y="274.5" width="183" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px;color:#6b7480">$\text{luvut yksiköineen}$</div></foreignObject>
  <line x1="46" y1="312" x2="46" y2="324" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <rect x="16" y="324" width="568" height="50" rx="8" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <circle cx="46" cy="349" r="17" fill="#1f2933"/>
  <foreignObject x="36.5" y="336" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px;color:#ffffff">$6$</div></foreignObject>
  <foreignObject x="76" y="334.5" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Vastaus}$</div></foreignObject>
  <foreignObject x="378" y="336.5" width="194" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px;color:#6b7480">$\text{yksikkö ja tarkkuus}$</div></foreignObject>
  <line x1="46" y1="374" x2="46" y2="386" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <rect x="16" y="386" width="568" height="50" rx="8" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <circle cx="46" cy="411" r="17" fill="#1f2933"/>
  <foreignObject x="36.5" y="398" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px;color:#ffffff">$7$</div></foreignObject>
  <foreignObject x="76" y="396.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{Järkevyys}$</div></foreignObject>
  <foreignObject x="389" y="398.5" width="183" height="25" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:21px;color:#6b7480">$\text{arvio tai vertailu}$</div></foreignObject>
</svg>

Tämän kirjan mallivastauksissa vaiheet on otsikoitu lyhyesti: **Annettu** ja **Kysytty** ovat vaihe 1, **Periaate** vaihe 2, **Kaava** vaihe 3, **Muunnokset** vaihe 4, **Sijoitus** vaihe 5, **Vastaus** vaihe 6 ja **Järkevyys** vaihe 7. Kun näet nämä otsikot ratkaisussa, tunnistat samat seitsemän vaihetta.

### Ratkaise ensin symboleilla
Kun kaava ratkaistaan kysytyn suureen suhteen ennen sijoitusta, lukija näkee, mistä tulos riippuu, ja yksiköt voi tarkistaa. Esimerkiksi tasaisesti kiihtyvässä liikkeessä levosta lähtevän kappaleen kiihtyvyys ratkaistaan näin:

$$
s = \frac{1}{2}at^2 \quad\Rightarrow\quad a = \frac{2s}{t^2}
$$

missä $s$ on kuljettu matka, $t$ aika ja $a$ kiihtyvyys. Kaava pätee vain, kun kiihtyvyys on vakio ja alkunopeus nolla.

### Vastauksen tarkkuus
Välitulokset pidetään pyöristämättöminä, ja vain lopputulos pyöristetään. Lopputuloksessa on yhtä monta merkitsevää numeroa kuin epätarkimmassa lähtöarvossa. Lopputulos ilman yksikköä ei kerro suuretta, joten se ei ole vastaus.

## Tehtäväsanat {Tehtavasanat}

| Sana | Mitä vastaukselta odotetaan |
|---|---|
| laske, määritä | täydellinen ratkaisu seitsemässä vaiheessa |
| selitä | syy-seuraus-ketju fysiikan käsittein: ilmiö, laki, päätelmä |
| perustele | väite ja sen tueksi laki, laskelma tai havainto |
| määritä graafisesti | kuvaaja aineistosta, sovite ja arvo luettuna sovitteesta |
| arvioi | perustellut oletukset, karkea lasku ja sopiva tarkkuus |
| suunnittele | muuttujat, vakioina pidettävät suureet, mittaukset ja virhelähteet |

## Kuvaajat ja kaavat koneella {Kuvaajat}

Kuvaajassa on akseleilla suureet ja yksiköt, kaikki mittauspisteet ja niihin sovitettu suora tai käyrä. Sovite kulkee pisteiden lomitse, eikä pisteitä yhdistetä murtoviivaksi. Kulmakerroin luetaan sovitteelta kahdesta kaukana toisistaan olevasta pisteestä:

$$
k = \frac{\Delta y}{\Delta x}
$$

missä $\Delta y$ ja $\Delta x$ ovat suoran kahden pisteen pysty- ja vaakakoordinaattien erotukset. Kulmakertoimen yksikkö on pystyakselin yksikkö jaettuna vaaka-akselin yksiköllä.

<svg data-fig="graph" viewBox="0 0 600 400" role="img" aria-label="Kuvaaja mittakaavassa: kärryn paikka x metreinä ajan t funktiona sekunteina, keksityt esimerkkiarvot. Seitsemän mittauspistettä ajanhetkillä 0–6 s nousee lähes suoraan. Pisteisiin on sovitettu suora, joka kulkee pisteiden lomitse. Kulmakerroin luetaan suoralta kahdesta kaukana toisistaan olevasta pisteestä, (1,0 s; 1,02 m) ja (5,0 s; 3,50 m), katkoviivakolmion avulla: Δt = 4,0 s ja Δx = 2,48 m, joten kulmakerroin on noin 0,62 m/s." style="max-width:100%;font-size:24px">
  <line x1="135.5" y1="350" x2="135.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="191.5" y1="350" x2="191.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="247" y1="350" x2="247" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="303" y1="350" x2="303" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="358.5" y1="350" x2="358.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="414.5" y1="350" x2="414.5" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="350" x2="470" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="292" x2="470" y2="292" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="234" x2="470" y2="234" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="176" x2="470" y2="176" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="118" x2="470" y2="118" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="80" y1="60" x2="470" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="79" y1="350" x2="484" y2="350" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,350 L483,356 L483,344 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="80" y1="351" x2="80" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M80,34 L86,47 L74,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="135.5" y1="350" x2="135.5" y2="357" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="125.5" y="359.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="191.5" y1="350" x2="191.5" y2="357" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="181.5" y="359.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="247" y1="350" x2="247" y2="357" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="237" y="359.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="303" y1="350" x2="303" y2="357" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="293" y="359.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="358.5" y1="350" x2="358.5" y2="357" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="348.5" y="359.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$5$</div></foreignObject>
  <line x1="414.5" y1="350" x2="414.5" y2="357" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="404.5" y="359.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="470" y1="350" x2="470" y2="357" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="460" y="359.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$7$</div></foreignObject>
  <line x1="73" y1="292" x2="80" y2="292" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="48" y="277.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$1$</div></foreignObject>
  <line x1="73" y1="234" x2="80" y2="234" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="48" y="219.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$2$</div></foreignObject>
  <line x1="73" y1="176" x2="80" y2="176" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="48" y="161.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="73" y1="118" x2="80" y2="118" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="48" y="103.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$4$</div></foreignObject>
  <line x1="73" y1="60" x2="80" y2="60" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="48" y="45.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$5$</div></foreignObject>
  <foreignObject x="50" y="355.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="335.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$t\ (\text{s})$</div></foreignObject>
  <foreignObject x="70" y="3.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$x\ (\text{m})$</div></foreignObject>
  <polyline points="80,326.5 447.5,89.5" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="135.5" y1="291" x2="358.5" y2="291" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <line x1="358.5" y1="291" x2="358.5" y2="147" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <circle cx="80" cy="325.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="135.5" cy="293" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="191.5" cy="252.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="247" cy="219.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="303" cy="183" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="358.5" cy="148.5" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="414.5" cy="110" r="6.5" fill="#1f2933" stroke="#ffffff" stroke-width="2"/>
  <circle cx="135.5" cy="291" r="10" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <circle cx="358.5" cy="147" r="10" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <foreignObject x="193" y="298.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#6b7480"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\Delta t = 4{,}0\,\text{s}$</span></div></foreignObject>
  <foreignObject x="370.5" y="226.5" width="120" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\Delta x = 2{,}48\,\text{m}$</span></div></foreignObject>
  <foreignObject x="147" y="74.5" width="145" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#1971c2"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$k = \tfrac{\Delta x}{\Delta t} \approx 0{,}62\,\tfrac{\text{m}}{\text{s}}$</span></div></foreignObject>
</svg>

Jos teet kuvaajan kuvaajaohjelmalla, kuten Graphical Analysisilla, liitä vastaukseen kuvakaappaus, jossa näkyvät akselit, pisteet ja sovitteen yhtälö. Kirjoita lisäksi tekstiin, mikä sovitteen kerroin vastaa mitäkin suuretta ja mitä siitä seuraa. Pelkkä ohjelman tulostama luku ei ole perusteltu vastaus.

## Yleisiä virheitä {Virheet}

- Lopputuloksesta puuttuu yksikkö, tai siinä on liikaa merkitseviä numeroita.
- Välitulokset pyöristetään, ja virhe kertautuu lopputulokseen.
- Kaava kirjoitetaan perustelematta, miksi se pätee tilanteessa.
- Yksikkömuunnos unohtuu: $\text{km/h}$ jää muuttamatta yksikköön $\text{m/s}$ tai celsiusaste kelviniksi.
- Kulmakerroin lasketaan kahdesta vierekkäisestä mittauspisteestä eikä sovitteesta.
- Selitykseksi kirjoitetaan kaava ilman syy-seuraus-ketjua.
- Tulosta ei verrata kokemukseen, jolloin selvä laskuvirhe jää huomaamatta.

## Kertaa tarvittaessa {Kertaa}

- Merkitsevät numerot ja virhelähteet: luvussa [*Mittaaminen ja mittauksen luotettavuus*](fy1-3.html).
- Kuvaajan piirtäminen, sovite ja kulmakerroin: luvussa [*Graafinen esitys ja suoran sovittaminen*](fy1-4.html).
- Kokeen suunnittelu ja raportti: luvussa [*Oma kokeellinen tutkimus: suunnittelu, toteutus ja raportointi*](fy1-8.html).
- Täydellinen ratkaisu esimerkin avulla: luvussa [*Aineen lämpeneminen ja jäähtyminen*](fy3-6.html).

## Esimerkki

Kylpyammeeseen lasketaan $145\,\text{kg}$ vettä, jonka lämpötila nousee lämminvesivaraajassa $10{,}0\,{}^\circ\text{C}$:sta $38{,}0\,{}^\circ\text{C}$:een. Kuinka paljon energiaa veden lämmittäminen vaatii kilowattitunteina? Varaajan ja putkien lämpöhäviöitä ei oteta huomioon.

Esimerkin vaiheet ovat samat kuin mallivastausten otsikot: *Tunnetut ja kysytty* on Annettu ja Kysytty, *Kaava ratkaistuna* on Kaava, *Yksikkömuunnokset* on Muunnokset ja *Tulos* on Vastaus.

<!-- vaihe -->

**Tunnetut ja kysytty.** Veden massa $m = 145\,\text{kg}$, alkulämpötila $T_1 = 10{,}0\,{}^\circ\text{C}$, loppulämpötila $T_2 = 38{,}0\,{}^\circ\text{C}$ ja taulukosta veden ominaislämpökapasiteetti $c = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}}$. Kysytään lämpömäärää $Q$ kilowattitunteina.

<!-- vaihe -->

**Periaate.** Vesi lämpenee eikä sen olomuoto muutu, joten veteen siirtyvä lämpömäärä on $Q = cm\Delta T$. Häviöitä ei oteta huomioon, joten varaajan antama energia on sama kuin veden saama lämpömäärä.

<!-- vaihe -->

**Kaava ratkaistuna.** Kysytty suure on jo yksin vasemmalla puolella:
```latex
Q = cm(T_2 - T_1)
```

<!-- vaihe -->

**Yksikkömuunnokset.** Lämpötilaero on sama kelvineinä ja celsiusasteina: $T_2 - T_1 = 28{,}0\,\text{K}$. Lopuksi joulet muunnetaan kilowattitunneiksi: $1\,\text{kWh} = 1000\,\text{W} \cdot 3600\,\text{s} = 3{,}6 \cdot 10^{6}\,\text{J}$.

<!-- vaihe -->

**Sijoitus.** Sijoitetaan arvot yksiköineen ja muunnetaan tulos:
```latex
\begin{aligned}
&Q = 4190\,\tfrac{\text{J}}{\text{kg}\cdot\text{K}} \cdot 145\,\text{kg} \cdot 28{,}0\,\text{K} \\
&= 17\,011\,400\,\text{J} \\
&= \frac{17\,011\,400\,\text{J}}{3{,}6 \cdot 10^{6}\,\text{J/kWh}} \\
&= 4{,}7254\,\text{kWh}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Lämmittäminen vaatii noin $4{,}73\,\text{kWh}$ energiaa. Kolme merkitsevää numeroa, kuten massassa $145\,\text{kg}$ ja lämpötilaerossa $28{,}0\,\text{K}$.

<!-- vaihe -->

**Järkevyys.** Karkea arvio: $4000 \cdot 150 \cdot 30\,\text{J} \approx 18\,\text{MJ} = 5\,\text{kWh}$, mikä on lähellä tulosta. Yksi täysi kylpy vastaa siis suunnilleen sitä, että $2\,\text{kW}$:n sähkölämmitin olisi päällä yli kaksi tuntia.
