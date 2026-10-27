# Kaasun tekemä työ ja lämpövoimakone

> **Miksi** lämpövoimalaitos saa polttoaineen energiasta sähköksi vain alle puolet, ja minne loput energiasta menee?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: lauhdevoimalaitos järven rannalla. Voimalinjat vievät sähköä pois, jäähdytystornista nousee suuri höyrypilvi, ja lauhdevesi purkautuu järveen lämpimänä, mikä näkyy oranssina vyöhykkeenä vedessä. Suurin osa polttoaineen energiasta lähtee lämpönä ilmaan ja veteen." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy311h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><linearGradient id="fy311h-lake" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d1f0"/><stop offset="1" stop-color="#2f74b5"/></linearGradient><linearGradient id="fy311h-tower" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#c4ccd4"/></linearGradient><linearGradient id="fy311h-chimney" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#c4ccd4"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="420" fill="url(#fy311h-sky)"/>
  <path d="M0,380 L15,338 L30,380 L40.5,353.5 L51,380 L62.5,350 L73.5,380 L86,348 L98,380 L107,357.5 L116,380 L129,346 L141.5,380 L152,352.5 L163,380 L175,347.5 L187.5,380 L198.5,350.5 L210,380 L221,352 L231.5,380 L245.5,341.5 L259.5,380 L270,353 L280.5,380 L295,340.5 L309,380 L323.5,340 L338,380 L353.5,336.5 L369,380 L380,351 L391,380 L402,352 L412.5,380 L422,357 L431.5,380 L441.5,355 L451.5,380 L465,342.5 L479,380 L488,358 L497,380 L505.5,360 L514,380 L527,344 L540.5,380 L554,342.5 L568,380 L579.5,349 L591.5,380 L604.5,345.5 L617,380 L628.5,350 L640,380 L653,346 L665.5,380 L674.5,357.5 L684,380 L699,337.5 L714,380 L726,349 L737.5,380 L749,351.5 L760,380 L773.5,342 L787.5,380 L798.5,351 L809.5,380 L825,337 L840.5,380 L853,345 L866,380 L879.5,342.5 L893.5,380 L904,351.5 L915,380 L927,349 L938.5,380 L953,340 L967.5,380 L977,356.5 L986.5,380 L1000.5,342 L1014,380 L1028.5,341 L1042.5,380 L1054,349 L1065.5,380 L1080.5,338.5 L1095.5,380 L1110,339 L1125,380 L1139,340.5 L1153.5,380 L1168.5,337.5 L1184,380 L1196,348 L1207.5,380 V420 H0 Z" fill="#c4ccd4" stroke-linejoin="round"/>
  <rect x="0" y="420" width="1200" height="180" fill="url(#fy311h-lake)"/>
  <path d="M0,400 H900 Q860,420 820,440 H0 Z" fill="#c9c2b2" stroke-linejoin="round"/>
  <path d="M120,420 Q160,300 140,190 H300 Q280,300 320,420 Z" fill="url(#fy311h-tower)" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M130,190 Q128,156 168,160 Q184,124 224,136 Q260,116 280,154 Q316,158 312,190 Z" fill="#ffffff" stroke-linejoin="round" stroke="#c9c2b2" stroke-width="2.5"/>
  <path d="M183,136 Q180.5,92 232.5,97 Q253,50 305,66 Q352,40 378,89 Q425,94.5 419.5,136 Z" fill="#ffffff" stroke-linejoin="round" stroke="#c9c2b2" stroke-width="2.5"/>
  <path d="M304,98 Q301,50.5 357,56 Q379.5,5.5 435.5,22.5 Q486,-5.5 514,47.5 Q564.5,53 559,98 Z" fill="#ffffff" stroke-linejoin="round" stroke="#c9c2b2" stroke-width="2.5"/>
  <path d="M481,82 Q479,44.5 523,49 Q540.5,9.5 584.5,22.5 Q624,0.5 646,42.5 Q685.5,47 681,82 Z" fill="#ffffff" stroke-linejoin="round" stroke="#c9c2b2" stroke-width="2.5"/>
  <rect x="360" y="250" width="140" height="170" fill="#e3dccb" stroke="#1f2933" stroke-width="3"/>
  <rect x="500" y="310" width="220" height="110" fill="#c4ccd4" stroke="#1f2933" stroke-width="3"/>
  <rect x="520" y="340" width="26" height="40" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="564" y="340" width="26" height="40" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="608" y="340" width="26" height="40" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="652" y="340" width="26" height="40" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="696" y="340" width="26" height="40" fill="#eef5f9" stroke="#1f2933" stroke-width="2"/>
  <rect x="400" y="120" width="36" height="130" fill="url(#fy311h-chimney)" stroke="#1f2933" stroke-width="3"/>
  <rect x="380" y="290" width="30" height="40" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <rect x="440" y="290" width="30" height="40" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <rect x="690" y="420" width="30" height="24" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <ellipse cx="760" cy="480" rx="150" ry="40" fill="#ffc078" fill-opacity="0.55"/>
  <ellipse cx="740" cy="468" rx="80" ry="22" fill="#e8590c" fill-opacity="0.45"/>
  <path d="M850,420 L880,230 L910,420 M840,270 H920 M850,300 H910" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round"/>
  <path d="M1030,420 L1060,230 L1090,420 M1020,270 H1100 M1030,300 H1090" fill="none" stroke="#1f2933" stroke-width="4" stroke-linejoin="round"/>
  <path d="M720,320 Q800,290 840,270 M840,270 Q960,300 1020,270 M1100,270 Q1150,290 1200,285" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M720,330 Q800,320 850,300 M850,300 Q960,330 1030,300 M1090,300 Q1150,320 1200,315" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
</svg>

## Ydinajatus
Kun kaasu laajenee ja työntää mäntää, se tekee työtä. Kaasu painaa mäntää voimalla $F = pA$, missä $A$ on männän pinta-ala. Jos mäntä liikkuu matkan $s$ ja paine pysyy samana, kaasun tekemä työ on voima kertaa matka, $pAs$. Tulo $As$ on kaasun tilavuuden muutos $\Delta V$, joten kaasun tekemä työ on $W_\text{k} = p\,\Delta V$. ($V$, $p$)-kuvaajassa se on kuvaajan ja $V$-akselin väliin jäävä pinta-ala, samoin kuin työ ($s$, $F$)-kuvaajassa. Kun kaasua puristetaan, ympäristö tekee työtä kaasuun, ja $W_\text{k}$ on negatiivinen. Työtä tekevä kaasu luovuttaa energiaa, joten tällä tunnilla ensimmäinen pääsääntö kirjoitetaan muodossa $\Delta U = Q - W_\text{k}$.

<svg data-fig="piston-work" viewBox="0 0 600 330" role="img" aria-label="Kaasun tekemä työ männälle, periaatekuva. Sylinterin poikkipinta-ala on A. Kaasun paine p työntää mäntää voimalla F = pA, ja mäntä siirtyy matkan Δs oikealle. Kaasun tilavuus kasvaa varjostetun osan verran, ΔV = AΔs. Työ on W_k = FΔs = pAΔs = pΔV. Kuva ei ole mittakaavassa." style="max-width:100%;font-size:24px">
  <defs><pattern id="fy311-dv" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="12" height="12" fill="#ffc078"/><line x1="0" y1="0" x2="0" y2="12" stroke="#e8590c" stroke-width="2"/></pattern></defs>
  <rect x="110" y="70" width="140" height="120" fill="#ffc078" fill-opacity="0.3"/>
  <rect x="250" y="70" width="170" height="120" fill="url(#fy311-dv)"/>
  <line x1="250" y1="70" x2="250" y2="190" stroke="#6b7480" stroke-width="2" stroke-linecap="butt" stroke-dasharray="7 5"/>
  <rect x="104" y="64" width="6" height="132" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="104" y="64" width="458" height="6" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="104" y="190" width="458" height="6" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="413" y="71" width="14" height="118" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="429" y1="130" x2="515" y2="130" stroke="#e8590c" stroke-width="5" stroke-linecap="butt"/>
  <path d="M536,130 L514,140 L514,120 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="449" y="85.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$F = pA$</div></foreignObject>
  <foreignObject x="130.5" y="115.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kaasu},\ p$</div></foreignObject>
  <foreignObject x="318.5" y="115.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$\Delta V$</span></div></foreignObject>
  <line x1="76" y1="130" x2="76" y2="82" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M76,71 L81.5,83 L70.5,83 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="76" y1="130" x2="76" y2="178" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M76,189 L70.5,177 L81.5,177 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="46" y="115.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px"><span style="background:#ffffff;padding:0 5px;border-radius:3px">$A$</span></div></foreignObject>
  <line x1="250" y1="198" x2="250" y2="234" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="198" x2="420" y2="234" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="311" y1="226" x2="262" y2="226" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M251,226 L263,220.5 L263,231.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="359" y1="226" x2="408" y2="226" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M419,226 L407,231.5 L407,220.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="318.5" y="211.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta s$</div></foreignObject>
  <foreignObject x="183.5" y="275.5" width="233" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W_\text{k} = F\,\Delta s = pA\,\Delta s = p\,\Delta V$</div></foreignObject>
</svg>

### Lämpövoimakone toistaa liikettään
Lämpövoimakone muuttaa lämpöä jatkuvasti työksi, joten sen on toistettava liikettään. Mäntä on saatava takaisin alas. Jos se painetaan alas samassa paineessa, palautus vie koko kaasun tekemän työn. Palautus vaatii vähemmän työtä, jos kaasu jäähdytetään ensin pienempään paineeseen, mutta silloin kaasu luovuttaa lämpöä kylmempään ympäristöön. Höyryvoimalaitoksessa vesi kiehuu kattilassa, kuuma höyry laajenee turbiinissa ja pyörittää generaattoria, ja turbiinista tuleva höyry tiivistyy jälleen vedeksi lauhduttimessa, jota merivesi jäähdyttää. Työaine kiertää samaa rataa yhä uudelleen, joten kierroksen lopussa sen sisäenergia on sama kuin alussa. Energia säilyy: kuumasta lähteestä tullut lämpö $Q_1$ on yhtä suuri kuin koneen tekemä työ $W$ ja kylmempään ympäristöön luovutettu lämpö $Q_2$ yhteensä.

Kokemus osoittaa, ettei lämpövoimakone voi muuttaa kaikkea saamaansa lämpöä työksi, vaan osa on aina luovutettava kylmempään ympäristöön. Tämä on termodynamiikan toisen pääsäännön sisältö. Mitä suurempi on kuuman lähteen ja kylmän ympäristön lämpötilaero kuuman lähteen lämpötilaan nähden, sitä suuremman osan lämmöstä kone voi muuttaa työksi. Kiertoprosesseja ei tällä kurssilla lasketa; simulaatio näyttää vain, miksi lämpöä $Q_2$ ei voi välttää.

<svg data-fig="heat-engine" viewBox="0 0 600 340" role="img" aria-label="Lämpövoimakoneen energiavirrat nuolina, joiden leveys kuvaa energiavirtaa eli tehoa: kuumasta lähteestä, jonka lämpötila on T_1, tulee koneeseen lämpö Q_1. Kone tekee työn W, joka on 40 prosenttia Q_1:stä, ja luovuttaa loput, lämmön Q_2, kylmään ympäristöön, jonka lämpötila on T_2. Nuolten leveydet ovat mittakaavassa: Q_1 60, W 24 ja Q_2 36 yksikköä, joten Q_1-nuoli on yhtä leveä kuin W- ja Q_2-nuolet yhteensä." style="max-width:100%;font-size:24px">
  <rect x="150" y="12" width="300" height="52" rx="10" fill="#f2a69c" stroke="#c92a2a" stroke-width="2.5"/>
  <foreignObject x="215" y="23.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kuuma lähde}\quad T_1$</div></foreignObject>
  <rect x="150" y="276" width="300" height="52" rx="10" fill="#d0e6fb" stroke="#1971c2" stroke-width="2.5"/>
  <foreignObject x="190" y="287.5" width="220" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kylmä ympäristö}\quad T_2$</div></foreignObject>
  <rect x="225" y="118" width="150" height="98" rx="12" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="271" y="152.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kone}$</div></foreignObject>
  <path d="M270,64 L270,94 L258,94 L300,118 L342,94 L330,94 L330,64 Z" fill="#e8590c" stroke-linejoin="round"/>
  <path d="M282,216 L282,250 L270,250 L300,274 L330,250 L318,250 L318,216 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M375,179 L534,179 L534,190 L560,167 L534,144 L534,155 L375,155 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="354" y="77.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q_1$</div></foreignObject>
  <foreignObject x="342" y="229.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q_2$</div></foreignObject>
  <foreignObject x="460" y="119.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W$</div></foreignObject>
  <foreignObject x="16" y="137.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{nuolen leveys}$</div></foreignObject>
  <foreignObject x="16" y="167.5" width="133" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kuvaa tehoa}$</div></foreignObject>
</svg>

### Hyötysuhde
Hyötysuhde kertoo, kuinka suuri osa koneeseen tuodusta energiasta saadaan hyödyksi. Suomalainen lauhdevoimalaitos, joka tuottaa vain sähköä, saa polttoaineen energiasta sähköksi noin 40 %, ja ydinvoimalaitos noin 35 %. Loput siirtyvät lauhduttimen kautta mereen. Automoottorin hyötysuhde on noin 30 %, ja loput energiasta poistuu pakokaasujen ja jäähdyttimen mukana. Sähkön ja lämmön yhteistuotannossa lauhduttimesta tuleva lämpö johdetaan kaukolämpöverkkoon kaupungin taloihin, joten polttoaineen energiasta saadaan hyödyksi sähkönä ja lämpönä yhteensä 85–90 %. Tämä vastaa alun kysymykseen: sähköksi saadaan alle puolet, mutta loput eivät katoa, vaan siirtyvät lämpönä ympäristöön tai kaukolämpöverkkoon.

### Jäähdytyskone ja lämpöpumppu
Jäähdytyskone ja lämpöpumppu toimivat päinvastoin kuin lämpövoimakone: ne käyttävät sähköenergiaa ja siirtävät sen avulla lämpöä kylmästä paikasta lämpimään. Jääkaappi siirtää lämpöä kaapin sisältä huoneeseen, ja ilmalämpöpumppu ulkoilmasta sisälle. Sisälle luovutettu lämpö on ulkoa otetun lämmön ja käytetyn sähkön summa, joten pumppu voi lämmittää taloa esimerkiksi kolminkertaisella teholla käyttämäänsä sähkötehoon verrattuna. Tätä lämpötehon ja sähkötehon suhdetta sanotaan lämpökertoimeksi. Pumppu ei luo energiaa, vaan siirtää sitä.

<svg data-fig="heat-pump" viewBox="0 0 600 270" role="img" aria-label="Lämpöpumpun energiavirrat nuolina, joiden leveys kuvaa tehoa: sähköenergia E_s ja ulkoilmasta otettu lämpö Q_ulko tulevat pumppuun, ja pumppu luovuttaa sisälle lämmön Q_sisälle, joka on niiden summa. Nuolten leveydet ovat mittakaavassa: E_s 20, Q_ulko 40 ja Q_sisälle 60 yksikköä, joten sisälle lähtevä nuoli on yhtä leveä kuin kaksi tulevaa nuolta yhteensä ja kolme kertaa niin leveä kuin sähkön nuoli." style="max-width:100%;font-size:24px">
  <rect x="230" y="76" width="130" height="126" rx="12" fill="#eef5f9" stroke="#1f2933" stroke-width="3"/>
  <foreignObject x="253.5" y="124.5" width="83" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{pumppu}$</div></foreignObject>
  <path d="M16,120 L208,120 L208,124 L230,110 L208,96 L208,100 L16,100 Z" fill="#1f2933" stroke-linejoin="round"/>
  <path d="M16,178 L208,178 L208,182 L230,158 L208,134 L208,138 L16,138 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M360,169 L532,169 L532,174 L560,139 L532,104 L532,109 L360,109 Z" fill="#e8590c" stroke-linejoin="round"/>
  <foreignObject x="16" y="59.5" width="99" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{sähkö}\ E_\text{s}$</div></foreignObject>
  <foreignObject x="16" y="191.5" width="183" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{ulkoilman lämpö}$</div></foreignObject>
  <foreignObject x="16" y="223.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$Q_\text{ulko}$</div></foreignObject>
  <foreignObject x="381" y="77.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{lämpö sisälle}$</div></foreignObject>
  <foreignObject x="406" y="177.5" width="108" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$Q_\text{sisälle}$</div></foreignObject>
  <foreignObject x="380" y="237.5" width="208" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\text{leveys kuvaa tehoa}$</div></foreignObject>
</svg>

## Kaava: Kaasun työ ja hyötysuhde
Kun kaasun paine pysyy vakiona, kaasun tekemä työ on
```latex
W_\text{k} = p\,\Delta V
```
missä $W_\text{k}$ on kaasun tekemä työ (J), $p$ kaasun paine (Pa) ja $\Delta V$ kaasun tilavuuden muutos (m³). Työ on positiivinen, kun kaasu laajenee, ja negatiivinen, kun kaasua puristetaan. Kaasun sisäenergian muutos on
```latex
\Delta U = Q - W_\text{k}
```
missä $Q$ on kaasuun siirtynyt lämpö (J). Tämä on luvussa *Sisäenergia, lämpömäärä ja energian säilyminen* esitetty ensimmäinen pääsääntö $\Delta U = Q + W$, jossa $W$ on ympäristön kaasuun tekemä työ: $W = -W_\text{k}$.

Lämpövoimakoneen yhden kierroksen aikana tekemä työ ja hyötysuhde ovat
```latex
W = Q_1 - Q_2
```
```latex
\eta = \frac{W}{Q_1}
```
missä $Q_1$ on kuumasta lähteestä koneeseen siirtynyt lämpö (J), $Q_2$ kylmempään ympäristöön luovutettu lämpö (J), $W$ koneen kierroksen aikana tekemä työ (J) ja $\eta$ hyötysuhde, joka ilmoitetaan usein prosentteina. Hyötysuhde voidaan laskea samalla tavalla tehoista, esimerkiksi sähköteho jaettuna polttoaineteholla.

<svg data-fig="pv-work" viewBox="0 0 600 330" role="img" aria-label="(V, p)-kuvaaja vakiopaineessa laajenevasta kaasusta: paine p pysyy vakiona, kun tilavuus kasvaa arvosta V_1 arvoon V_2, joten kuvaaja on vaakasuora jana, jonka nuoli osoittaa laajenemisen suuntaa. Janan ja V-akselin väliin jäävä varjostettu suorakulmio, jonka leveys on tilavuuden muutos ΔV ja korkeus p, on kaasun tekemä työ W_k = p ΔV. Kaaviokuva." style="max-width:100%;font-size:24px">
  <line x1="203" y1="270" x2="203" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="363" y1="270" x2="363" y2="60" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="112.5" x2="470" y2="112.5" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="270" x2="484" y2="270" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,270 L483,276 L483,264 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="271" x2="96" y2="46" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,34 L102,47 L90,47 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="203" y1="270" x2="203" y2="277" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="186.5" y="279.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$V_1$</div></foreignObject>
  <line x1="363" y1="270" x2="363" y2="277" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="346.5" y="279.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$V_2$</div></foreignObject>
  <line x1="89" y1="112.5" x2="96" y2="112.5" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="98" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$p$</div></foreignObject>
  <foreignObject x="66" y="275.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="255.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$V\ (\text{m}^3)$</div></foreignObject>
  <foreignObject x="86" y="3.5" width="74" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$p\ (\text{Pa})$</div></foreignObject>
  <polygon points="203,270 363,270 363,112.5 203,112.5" fill="#e8590c" fill-opacity="0.35"/>
  <polyline points="203,112.5 363,112.5" fill="none" stroke="#1f2933" stroke-width="4.5" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="203" y1="112.5" x2="203" y2="270" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="363" y1="112.5" x2="363" y2="270" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt" stroke-dasharray="6 5"/>
  <line x1="269" y1="112.5" x2="278" y2="112.5" stroke="#1f2933" stroke-width="4.5" stroke-linecap="butt"/>
  <path d="M297,112.5 L277,121.5 L277,103.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="198" y="72" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kaasu laajenee}$</div></foreignObject>
  <foreignObject x="235.5" y="156" width="95" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$W_\text{k} = p\,\Delta V$</div></foreignObject>
  <line x1="257" y1="228" x2="218" y2="228" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M206,228 L219,222 L219,234 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="309" y1="228" x2="348" y2="228" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M360,228 L347,234 L347,222 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="266.5" y="213.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\Delta V$</div></foreignObject>
</svg>

Lämpöpumppu luovuttaa sisälle lämmön, joka on ulkoilmasta otetun lämmön ja pumpun käyttämän sähköenergian summa:
```latex
Q_\text{sisälle} = Q_\text{ulko} + E_\text{s}
```
Lämpökerroin kertoo, kuinka moninkertaisen lämmön pumppu luovuttaa sisälle käyttämäänsä sähköenergiaan verrattuna:
```latex
\varepsilon = \frac{Q_\text{sisälle}}{E_\text{s}}
```
missä $Q_\text{sisälle}$ on sisälle luovutettu lämpö (J), $Q_\text{ulko}$ ulkoilmasta otettu lämpö (J), $E_\text{s}$ pumpun käyttämä sähköenergia (J) ja $\varepsilon$ lämpökerroin. Lämpökerroin voidaan laskea samalla tavalla tehoista.

## Esimerkki
Biovoimalaitoksen kattilaan syötetään puuhakkeen energiaa teholla 500 MW. Kun laitos tuottaa pelkkää sähköä, sähköteho on 190 MW. Talvella sama laitos toimii yhteistuotantovoimalaitoksena: se tuottaa 150 MW sähköä ja 290 MW kaukolämpöä. Mikä on hyötysuhde kummassakin tapauksessa, ja kuinka suuri teho siirtyy ympäristöön hukkalämpönä?

<!-- vaihe -->

**Tunnetut ja kysytty.** Polttoaineteho $P_1 = 500\,\text{MW}$. Pelkkää sähköä tuotettaessa sähköteho $P_\text{s} = 190\,\text{MW}$; yhteistuotannossa $P_\text{s} = 150\,\text{MW}$ ja kaukolämpöteho $P_\text{k} = 290\,\text{MW}$. Kysytään hyötysuhteita $\eta$ ja hukkalämmön tehoa $P_2$ kummassakin tapauksessa.

<!-- vaihe -->

**Periaate.** Hyötysuhde on hyödyksi saatu teho jaettuna syötetyllä teholla; se lasketaan tehoista samoin kuin energioista, koska molemmat ovat energiaa samassa ajassa. Energia säilyy, joten polttoaineteho jakautuu hyödyksi saatuun tehoon ja hukkalämpöön. Hyödyksi tulee pelkässä sähköntuotannossa vain sähkö, yhteistuotannossa sähkö ja kaukolämpö.

<!-- vaihe -->

**Kaava ratkaistuna.** Ratkaistaan kysytyt suureet symboleilla ennen lukuja:
```latex
\begin{aligned}
\eta &= \frac{P_\text{hyöty}}{P_1} \\
P_2 &= P_1 - P_\text{hyöty}
\end{aligned}
```
Pelkälle sähkölle $P_\text{hyöty} = P_\text{s}$ ja yhteistuotannolle $P_\text{hyöty} = P_\text{s} + P_\text{k}$.

<!-- vaihe -->

**Yksikkömuunnokset.** Kaikki tehot on annettu megawatteina, joten muunnoksia ei tarvita: hyötysuhteessa yksikkö supistuu, ja hukkalämpö saadaan megawatteina. Desimaaliluku muutetaan prosenteiksi kertomalla sadalla.

<!-- vaihe -->

**Sijoitus.** Pelkälle sähkölle ja yhteistuotannolle erikseen:
```latex
\begin{aligned}
\eta_1 &= \frac{P_\text{s}}{P_1} \\
&= \frac{190\,\text{MW}}{500\,\text{MW}} \\
&= 0{,}380 \\
P_{2,1} &= P_1 - P_\text{s} \\
&= 500\,\text{MW} - 190\,\text{MW} \\
&= 310\,\text{MW} \\[6pt]
\eta_2 &= \frac{P_\text{s} + P_\text{k}}{P_1} \\
&= \frac{150\,\text{MW} + 290\,\text{MW}}{500\,\text{MW}} \\
&= 0{,}880 \\
P_{2,2} &= P_1 - (P_\text{s} + P_\text{k}) \\
&= 500\,\text{MW} - 440\,\text{MW} \\
&= 60\,\text{MW}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Pelkällä sähköntuotannolla hyötysuhde on $\eta_1 = 0{,}380 = 38{,}0\,\%$ ja hukkalämpöä siirtyy mereen lauhduttimen kautta $310\,\text{MW}$. Yhteistuotannossa hyötysuhde on $\eta_2 = 0{,}880 = 88{,}0\,\%$ ja hukkalämpöä on vain $60\,\text{MW}$. Tehot on annettu täysinä megawatteina, joten erotukset $310\,\text{MW}$ ja $60\,\text{MW}$ tunnetaan megawatin tarkkuudella. Hyötysuhteet ovat osamääriä, joten niissä on yhtä monta numeroa kuin epätarkimmassa tehossa: $190\,\text{MW}$, $150\,\text{MW}$, $290\,\text{MW}$ ja $500\,\text{MW}$ ovat kaikki kolmen numeron arvoja, joten hyötysuhteet annetaan kolmella numerolla.

<!-- vaihe -->

**Järkevyys.** Kumpikin hyötysuhde jää alle 100 %:n, kuten pitääkin, ja energia säilyy: $190\,\text{MW} + 310\,\text{MW} = 500\,\text{MW}$ ja $150\,\text{MW} + 290\,\text{MW} + 60\,\text{MW} = 500\,\text{MW}$. Sähköä saadaan yhteistuotannossa vähemmän, koska höyry lauhdutetaan korkeammassa lämpötilassa, jotta sen lämpö kelpaa kaukolämmöksi. Polttoaineen energia käytetään silti paljon paremmin hyödyksi.

## Yleinen virhekäsitys
Moni ajattelee, että parempi tekniikka voisi tehdä lämpövoimakoneesta lähes täydellisen, niin että kaikki lämpö muuttuisi työksi. Kitkan ja muiden häviöiden vähentäminen auttaa, mutta osa lämmöstä on aina luovutettava kylmempään ympäristöön, joten hyötysuhde jää selvästi alle 100 %:n. Simulaation kitkaton mäntä näyttää syyn: jotta mäntä saadaan alas pienemmällä työllä kuin se nousi, kaasua on jäähdytettävä, ja jäähdytyksessä lämpöä siirtyy kylmään veteen.

Toinen virhe on pitää lämpöpumppua ikiliikkujana, koska se luovuttaa enemmän lämpöä kuin käyttää sähköä. Ylimääräinen lämpö tulee ulkoilmasta, eikä energiaa synny tyhjästä. Kolmas virhe on ajatella, että paineistettu kaasu tekee työtä jo sillä, että sen paine on suuri. Työtä tehdään vain, kun tilavuus muuttuu ja mäntä liikkuu.

## Tiivistelmä
- Vakiopaineessa laajeneva kaasu tekee työn $W_\text{k} = p\,\Delta V$, joka on ($V$, $p$)-kuvaajan alle jäävä pinta-ala. Sisäenergia muuttuu $\Delta U = Q - W_\text{k}$.
- Mäntäkone voi toistaa työnsä vain, jos kaasu jäähdytetään ennen kuin mäntä palautetaan; silloin lämpöä siirtyy kylmempään.
- Lämpövoimakone ottaa lämpöä $Q_1$ kuumasta lähteestä, tekee työn $W$ ja luovuttaa lämmön $Q_2$ kylmempään ympäristöön: $W = Q_1 - Q_2$.
- Hyötysuhde on $\eta = W/Q_1$. Lämpövoimakone ei voi muuttaa kaikkea lämpöä työksi.
- Lauhdevoimalaitoksen hyötysuhde on noin 40 %, mutta sähkön ja lämmön yhteistuotannossa kokonaishyötysuhde on 85–90 %.
- Jäähdytyskone ja lämpöpumppu siirtävät työn avulla lämpöä kylmästä lämpimään. Ne eivät luo energiaa.
