# Kirchhoffin lait ja potentiaali virtapiirissä

> **Miksi** lintu voi istua paljaalla suurjännitejohdolla vahingoittumatta, vaikka johdossa kulkee satojen ampeerien virta?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: suurjännitelinja peltomaiseman yllä kesäpäivänä. Kahden ristikkopylvään välissä riippuu johtimia. Yhdellä johtimella istuu rivissä neljä pikkulintua. Taustalla on metsän reuna ja kumpuileva pelto." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy65h-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#eef5f9"/></linearGradient><radialGradient id="fy65h-sun" cx="0.4" cy="0.4" r="0.7"><stop offset="0" stop-color="#ffc078"/><stop offset="1" stop-color="#e8590c"/></radialGradient><linearGradient id="fy65h-field" gradientUnits="userSpaceOnUse" x1="0" y1="430" x2="0" y2="600"><stop offset="0" stop-color="#f1dfb5"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy65h-sky)"/>
  <circle cx="1020" cy="110" r="80" fill="#ffffff" fill-opacity="0.5"/>
  <path d="M1078,133 L1104,132.5 L1081.5,119.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1059,159 L1081.5,171.5 L1069,149 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1029.5,171.5 L1042.5,194 L1043,168 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M997,168 L997.5,194 L1010.5,171.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M971,149 L958.5,171.5 L981,159 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M958.5,119.5 L936,132.5 L962,133 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M962,87 L936,87.5 L958.5,100.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M981,61 L958.5,48.5 L971,71 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1010.5,48.5 L997.5,26 L997,52 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1043,52 L1042.5,26 L1029.5,48.5 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1069,71 L1081.5,48.5 L1059,61 Z" fill="#ffc078" stroke-linejoin="round"/>
  <path d="M1081.5,100.5 L1104,87.5 L1078,87 Z" fill="#ffc078" stroke-linejoin="round"/>
  <circle cx="1020" cy="110" r="50" fill="url(#fy65h-sun)"/>
  <path d="M210,130 Q208,96 248,100 Q264,64 304,76 Q340,56 360,94 Q396,98 392,130 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M697,84 Q695.5,60 723.5,63 Q735,38 763,46 Q788,32 802,59 Q827,61.5 824.5,84 Z" fill="#ffffff" stroke-linejoin="round"/>
  <path d="M0,400 Q100,372 200,397.5 Q300,343.5 400,403 Q500,357 600,400.5 Q700,380 800,395.5 Q900,376.5 1000,396.5 Q1100,369.5 1200,398 Q1300,337 1400,404.5 V600 H0 Z" fill="#b2f2bb" stroke-linejoin="round"/>
  <path d="M0,402 L15.5,352.5 L31,402 L45,357 L59.5,402 L68,378.5 L76.5,402 L85.5,379 L94,402 L108,357 L122.5,402 L131.5,377 L140.5,402 L151,372.5 L161,402 L170.5,375.5 L180,402 L193,361 L206.5,402 L218,368 L229,402 L243,359 L256.5,402 L271,356.5 L285.5,402 L299,360.5 L312.5,402 L327,355.5 L342,402 L354,366 L365.5,402 L380,356.5 L394.5,402 L405.5,370.5 L416,402 L430.5,355 L445.5,402 L459,361 L472,402 L487.5,353.5 L502.5,402 L515,363.5 L527.5,402 L542.5,355 L557.5,402 L567,374 L577,402 L587,374 L597,402 L609.5,362.5 L622.5,402 L631.5,377.5 L640.5,402 L655,354.5 L670,402 L684.5,357.5 L698.5,402 L713,356.5 L727.5,402 L737.5,372.5 L748,402 L758.5,370 L769.5,402 L782.5,362.5 L795.5,402 L808,363.5 L820.5,402 L832,367 L844,402 L853,376 L862.5,402 L873,372.5 L883,402 L898.5,353 L913.5,402 L929,352.5 L944.5,402 L954,375.5 L963.5,402 L978.5,354.5 L993.5,402 L1003.5,372 L1014,402 L1024.5,372.5 L1034.5,402 L1048.5,358.5 L1062.5,402 L1072.5,373 L1083,402 L1098.5,352.5 L1114,402 L1128,357 L1142.5,402 L1152.5,373.5 L1162,402 L1173.5,369 L1184.5,402 L1199.5,353.5 L1215,402 V432 H0 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <rect x="0" y="430" width="1200" height="170" fill="url(#fy65h-field)"/>
  <path d="M-60,600 L240,430" fill="none" stroke="#d9b26a" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M90,600 L390,430" fill="none" stroke="#d9b26a" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M240,600 L540,430" fill="none" stroke="#d9b26a" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M390,600 L690,430" fill="none" stroke="#d9b26a" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M540,600 L840,430" fill="none" stroke="#d9b26a" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M690,600 L990,430" fill="none" stroke="#d9b26a" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M840,600 L1140,430" fill="none" stroke="#d9b26a" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M990,600 L1290,430" fill="none" stroke="#d9b26a" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M1140,600 L1440,430" fill="none" stroke="#d9b26a" stroke-width="3" stroke-linejoin="round" stroke-opacity="0.6"/>
  <path d="M107.5,470 L142.5,110 H157.5 L192.5,470" fill="none" stroke="#6c757d" stroke-width="3.75" stroke-linejoin="round"/>
  <line x1="107.5" y1="470" x2="185.5" y2="398" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="192.5" y1="470" x2="114.5" y2="398" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="114.5" y1="398" x2="178.5" y2="326" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="185.5" y1="398" x2="121.5" y2="326" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="121.5" y1="326" x2="171.5" y2="254" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="178.5" y1="326" x2="128.5" y2="254" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="128.5" y1="254" x2="164.5" y2="182" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="171.5" y1="254" x2="135.5" y2="182" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="85" y1="182" x2="215" y2="182" stroke="#6c757d" stroke-width="3.75" stroke-linecap="butt"/>
  <line x1="85" y1="182" x2="85" y2="199.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="215" y1="182" x2="215" y2="199.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="107.5" y1="110" x2="192.5" y2="110" stroke="#6c757d" stroke-width="3.75" stroke-linecap="butt"/>
  <line x1="107.5" y1="110" x2="107.5" y2="127.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="192.5" y1="110" x2="192.5" y2="127.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M1037.5,470 L1072.5,110 H1087.5 L1122.5,470" fill="none" stroke="#6c757d" stroke-width="3.75" stroke-linejoin="round"/>
  <line x1="1037.5" y1="470" x2="1115.5" y2="398" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="1122.5" y1="470" x2="1044.5" y2="398" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="1044.5" y1="398" x2="1108.5" y2="326" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="1115.5" y1="398" x2="1051.5" y2="326" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="1051.5" y1="326" x2="1101.5" y2="254" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="1108.5" y1="326" x2="1058.5" y2="254" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="1058.5" y1="254" x2="1094.5" y2="182" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="1101.5" y1="254" x2="1065.5" y2="182" stroke="#6c757d" stroke-width="1.875" stroke-linecap="butt"/>
  <line x1="1015" y1="182" x2="1145" y2="182" stroke="#6c757d" stroke-width="3.75" stroke-linecap="butt"/>
  <line x1="1015" y1="182" x2="1015" y2="199.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="1145" y1="182" x2="1145" y2="199.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="1037.5" y1="110" x2="1122.5" y2="110" stroke="#6c757d" stroke-width="3.75" stroke-linecap="butt"/>
  <line x1="1037.5" y1="110" x2="1037.5" y2="127.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="1122.5" y1="110" x2="1122.5" y2="127.5" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M89,199.5 Q550,269.5 1011,199.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M219,199.5 Q680,269.5 1141,199.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M111.5,127.5 Q572.5,197.5 1033.5,127.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <path d="M196.5,127.5 Q657.5,197.5 1118.5,127.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round"/>
  <line x1="563.5" y1="232.5" x2="563.5" y2="218.5" stroke="#1f2933" stroke-width="2.3" stroke-linecap="butt"/>
  <line x1="575" y1="232.5" x2="575" y2="218.5" stroke="#1f2933" stroke-width="2.3" stroke-linecap="butt"/>
  <path d="M539.5,198 Q542,218.5 569.5,220 Q594.5,218.5 597,193.5 Q592.5,179.5 576.5,182 Q558,182 539.5,198 Z" fill="#6c757d" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M539.5,198 L516.5,207 L521,193.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="599.5" cy="182" r="13.8" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M611,179.5 L622.5,184 L611,186.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="602.5" cy="178.5" r="2.875" fill="#ffffff"/>
  <path d="M555.5,198 Q574,207 590,198" fill="none" stroke="#8a96a3" stroke-width="2.875" stroke-linejoin="round"/>
  <line x1="619" y1="234" x2="619" y2="220" stroke="#1f2933" stroke-width="2.3" stroke-linecap="butt"/>
  <line x1="630.5" y1="234" x2="630.5" y2="220" stroke="#1f2933" stroke-width="2.3" stroke-linecap="butt"/>
  <path d="M595,199.5 Q597,220 624.5,221.5 Q650,220 652.5,195 Q647.5,181 631.5,183.5 Q613,183.5 595,199.5 Z" fill="#6c757d" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M595,199.5 L572,208.5 L576.5,195 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="654.5" cy="183.5" r="13.8" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M666,181 L677.5,185.5 L666,188 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="658" cy="180" r="2.875" fill="#ffffff"/>
  <path d="M611,199.5 Q629.5,208.5 645.5,199.5" fill="none" stroke="#8a96a3" stroke-width="2.875" stroke-linejoin="round"/>
  <line x1="692.5" y1="234.5" x2="692.5" y2="220.5" stroke="#1f2933" stroke-width="2.3" stroke-linecap="butt"/>
  <line x1="704" y1="234.5" x2="704" y2="220.5" stroke="#1f2933" stroke-width="2.3" stroke-linecap="butt"/>
  <path d="M728.5,200 Q726,220.5 698.5,222 Q673,220.5 671,195.5 Q675.5,181.5 691.5,184 Q710,184 728.5,200 Z" fill="#6c757d" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M728.5,200 L751.5,209 L746.5,195.5 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="668.5" cy="184" r="13.8" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M657,181.5 L645.5,186 L657,188.5 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="665" cy="180.5" r="2.875" fill="#ffffff"/>
  <path d="M712,200 Q694,209 677.5,200" fill="none" stroke="#8a96a3" stroke-width="2.875" stroke-linejoin="round"/>
  <line x1="766.5" y1="233" x2="766.5" y2="219.5" stroke="#1f2933" stroke-width="2.3" stroke-linecap="butt"/>
  <line x1="778" y1="233" x2="778" y2="219.5" stroke="#1f2933" stroke-width="2.3" stroke-linecap="butt"/>
  <path d="M742.5,198.5 Q744.5,219.5 772,220.5 Q797.5,219.5 800,194 Q795,180 779,182.5 Q760.5,182.5 742.5,198.5 Z" fill="#6c757d" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M742.5,198.5 L719.5,208 L724,194 Z" fill="#1f2933" stroke-linejoin="round"/>
  <circle cx="802" cy="182.5" r="13.8" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M813.5,180 L825,185 L813.5,187 Z" fill="#e8590c" stroke-linejoin="round"/>
  <circle cx="805.5" cy="179" r="2.875" fill="#ffffff"/>
  <path d="M758.5,198.5 Q777,208 793,198.5" fill="none" stroke="#8a96a3" stroke-width="2.875" stroke-linejoin="round"/>
</svg>

## Ydinajatus

### Virta ei kulu: Kirchhoffin virtalaki
Sähkövirta on varausten liikettä. Varausta ei synny eikä häviä. Sitä ei myöskään kerry johtimiin, kun virrat pysyvät vakioina. Siksi kaikki varaus, joka tulee **haarautumispisteeseen**, myös lähtee siitä. Haarautumispiste on kohta, jossa johdin jakautuu haaroiksi. **Haarautumispisteeseen tulevien virtojen summa on yhtä suuri kuin siitä lähtevien virtojen summa.** Tämä on Kirchhoffin virtalaki. Samasta syystä virta on yhtä suuri vastuksen kummallakin puolella. Vastuksessa sähköenergiaa muuttuu vastuksen sisäenergiaksi. Sisäenergia siirtyy lämpönä ympäristöön. Virta ei kuitenkaan kulu vastuksessa.

Rinnakkaisten haarojen yli on sama jännite (luku *Vastusten sarja- ja rinnankytkennät*). Siksi Ohmin lain mukaan pienemmän resistanssin haaraan kulkee suurempi virta. Kuvassa haaran $30\,\Omega$ virta on kaksinkertainen haaran $60\,\Omega$ virtaan verrattuna. Haarojen virrat $0{,}20\,\text{A}$ ja $0{,}10\,\text{A}$ ovat yhteensä $0{,}30\,\text{A}$. Se on yhtä paljon kuin tuleva virta.

<svg data-fig="junction" viewBox="0 0 600 330" role="img" aria-label="Kaavakuva haarautumispisteestä, ei mittakaavassa. Vasemmalta tulee johdinta pitkin virta I1 = 0,30 A haarautumispisteeseen. Siitä lähtee kaksi haaraa. Ylähaarassa on 30 ohmin vastus ja alahaarassa 60 ohmin vastus. Haarat yhtyvät oikealla uudelleen. Violettien virtanuolten leveys on verrannollinen virtaan. Ylähaarassa on I2 = 0,20 A ja alahaarassa I3 = 0,10 A. Haaroista lähtee yhteensä yhtä paljon virtaa kuin pisteeseen tulee, 0,30 A." style="max-width:100%;font-size:24px">
  <polyline points="24,170 200,170" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="200,170 200,72 520,72 520,268 200,268 200,170" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="520,170 576,170" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="348" y="60" width="64" height="24" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="348" y="256" width="64" height="24" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <circle cx="200" cy="170" r="6" fill="#1f2933"/>
  <circle cx="520" cy="170" r="6" fill="#1f2933"/>
  <foreignObject x="351" y="91.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$30\,\Omega$</div></foreignObject>
  <foreignObject x="351" y="219.5" width="58" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$60\,\Omega$</div></foreignObject>
  <path d="M40,152 L124,152 L124,160 L150,140 L124,120 L124,128 L40,128 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="15" y="93.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#7048e8">$I_1 = 0{,}30\,\text{A}$</div></foreignObject>
  <path d="M230,52 L298,52 L298,60 L320,44 L298,28 L298,36 L230,36 Z" fill="#7048e8" stroke-linejoin="round"/>
  <path d="M230,300 L302,300 L302,307 L320,296 L302,285 L302,292 L230,292 Z" fill="#7048e8" stroke-linejoin="round"/>
  <foreignObject x="334" y="27.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_2 = 0{,}20\,\text{A}$</div></foreignObject>
  <foreignObject x="334" y="283.5" width="170" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#7048e8">$I_3 = 0{,}10\,\text{A}$</div></foreignObject>
  <foreignObject x="216" y="155.5" width="230" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{haarautumispiste}$</div></foreignObject>
</svg>

### Potentiaali: jokaisen kohdan sähköinen taso
Virtapiirin jokaisella kohdalla on **potentiaali** $V$. Potentiaali on kohdan jännite valittuun nollakohtaan nähden. Nollakohdaksi valitaan usein jännitelähteen miinusnapa tai maadoitus. Sen potentiaali on $0\,\text{V}$. Kahden kohdan välinen jännite on niiden potentiaalien erotus. Potentiaalia voi verrata korkeuteen. Korkeus riippuu siitä, mistä sitä mitataan. Kahden kohdan korkeusero ei riipu siitä. Samoin nollakohdan siirtäminen muuttaa kaikkia potentiaaleja yhtä paljon, mutta jännitteet pysyvät ennallaan.

Potentiaali muuttuu vain lähteessä ja vastuksissa. Lähteessä se nousee miinusnavalta plusnavalle lähteen jännitteen verran. Lähde on tässä luvussa ideaalinen. Se tarkoittaa, että lähteen oman resistanssin vaikutus jätetään huomiotta. Vastuksessa potentiaali laskee virran suuntaan jännitteen $U = RI$ verran. Johtimen resistanssi on niin pieni, että sen jännite jätetään huomiotta. Siksi saman johtimen kaikissa kohdissa on sama potentiaali. Kuvan piirissä pisteet $B$ ja $C$ ovat samaa johdinta. Molempien potentiaali on $6{,}0\,\text{V}$.

<svg data-fig="circuit" viewBox="0 0 600 368" role="img" aria-label="Kytkentäkaavio, ei mittakaavassa. Jännitelähde on 9,0 V. Sen plusnavalta tulee ensin vastus R1 = 10 ohmia. Sen jälkeen on kaksi rinnakkaista vastusta, R2 = 30 ohmia ja R3 = 60 ohmia. Ne palaavat lähteen miinusnapaan. Johtimiin on merkitty pisteet A–F ja niiden potentiaalit, kun lähteen miinusnapa on nollakohta: A 9,0 V, B ja C 6,0 V sekä D, E ja F 0 V. Saman johtimen kaikissa kohdissa potentiaali on sama. Se muuttuu vain lähteessä ja vastuksissa." style="max-width:100%;font-size:24px">
  <polyline points="72,177 72,90 470,90 470,280 72,280 72,193" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="330,90 330,280" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="46" y1="177" x2="98" y2="177" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="59" y1="193" x2="85" y2="193" stroke="#1f2933" stroke-width="7" stroke-linecap="butt"/>
  <rect x="164" y="78" width="64" height="24" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="318" y="153" width="24" height="64" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <rect x="458" y="153" width="24" height="64" fill="#ffffff" stroke="#1f2933" stroke-width="3"/>
  <circle cx="330" cy="90" r="6" fill="#1f2933"/>
  <circle cx="330" cy="280" r="6" fill="#1f2933"/>
  <foreignObject x="26" y="152.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$+$</div></foreignObject>
  <foreignObject x="26" y="192.5" width="24" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$-$</div></foreignObject>
  <foreignObject x="100" y="170.5" width="150" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U = 9{,}0\,\text{V}$</div></foreignObject>
  <foreignObject x="126" y="111.5" width="140" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_1 = 10\,\Omega$</div></foreignObject>
  <foreignObject x="352" y="152.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R_2$</div></foreignObject>
  <foreignObject x="352" y="188.5" width="64" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$30\,\Omega$</div></foreignObject>
  <foreignObject x="492" y="152.5" width="40" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$R_3$</div></foreignObject>
  <foreignObject x="492" y="188.5" width="64" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$60\,\Omega$</div></foreignObject>
  <circle cx="112" cy="90" r="5" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="98" y="51.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A$</div></foreignObject>
  <foreignObject x="72" y="19.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$9{,}0\,\text{V}$</div></foreignObject>
  <circle cx="286" cy="90" r="5" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="272" y="51.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$B$</div></foreignObject>
  <foreignObject x="246" y="19.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$6{,}0\,\text{V}$</div></foreignObject>
  <circle cx="470" cy="90" r="5" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="456" y="51.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$C$</div></foreignObject>
  <foreignObject x="430" y="19.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$6{,}0\,\text{V}$</div></foreignObject>
  <circle cx="470" cy="280" r="5" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="456" y="289.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$D$</div></foreignObject>
  <foreignObject x="430" y="321.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$0\,\text{V}$</div></foreignObject>
  <circle cx="330" cy="280" r="5" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="316" y="289.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E$</div></foreignObject>
  <foreignObject x="290" y="321.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$0\,\text{V}$</div></foreignObject>
  <circle cx="112" cy="280" r="5" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="98" y="289.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$F$</div></foreignObject>
  <foreignObject x="72" y="321.5" width="80" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$0\,\text{V}$</div></foreignObject>
</svg>

### Kierros silmukassa: Kirchhoffin jännitelaki
**Silmukka** on virtapiirin suljettu reitti, joka palaa lähtökohtaansa. Kun silmukka kierretään, potentiaali palaa samaan arvoon, josta lähdettiin. Siksi **potentiaalin nousujen ja laskujen summa silmukassa on nolla**. Tämä on Kirchhoffin jännitelaki. Yhden silmukan piirissä lähteen jännite on yhtä suuri kuin vastusten jännitteiden summa. Energian kannalta jännite kertoo, kuinka paljon energiaa yhtä varausyksikköä kohti muuttuu muodosta toiseen (luku *Virtapiiri, sähkövirta ja jännite*). Varaus saa lähteessä energiaa ja luovuttaa saman määrän vastuksissa.

Kuvan piirissä on kaksi silmukkaa. Toinen kulkee vastuksen $R_2$ kautta ja toinen vastuksen $R_3$ kautta. Kummassakin lähteen $9{,}0\,\text{V}$ jakautuu kahteen osaan. Vastuksen $R_1$ jännite on $3{,}0\,\text{V}$ ja haaran jännite on $6{,}0\,\text{V}$. Siksi rinnakkaisten haarojen yli on sama jännite.

### Lintu johdolla
Linnun jalat ovat saman johtimen kahdessa kohdassa. Kohdat ovat vain muutaman senttimetrin päässä toisistaan. Lintu on rinnakkainen haara jalkojen välissä olevalle johtimen pätkälle. Pätkän resistanssi on häviävän pieni. Siksi jalkojen välinen jännite on vain millivoltteja. Ohmin lain mukaan linnun läpi kulkee silloin häviävän pieni virta. Virtalain mukaan lähes koko virta jatkaa johdinta pitkin. Linnun potentiaali maahan nähden on suuri. Vaara syntyisi vasta, jos lintu koskettaisi samalla toista johdinta tai pylvästä, joiden potentiaali on eri. Ihmiselle tilanne ei ole vertailukelpoinen. Suurjännitejohtoa ei saa lähestyä, koska valokaari voi syntyä jo ilman kosketusta.

## Kaava: Kirchhoffin lait
Kirchhoffin virtalaki haarautumispisteelle:
```latex
\sum I_\text{tulevat} = \sum I_\text{lähtevät}
```
missä $I_\text{tulevat}$ ovat haarautumispisteeseen tulevat virrat (A) ja $I_\text{lähtevät}$ siitä lähtevät virrat (A). Kun virta jakautuu kahteen haaraan, $I_1 = I_2 + I_3$.

Kohtien $A$ ja $B$ välinen jännite on potentiaalien erotus:
```latex
U_{AB} = V_A - V_B
```
missä $U_{AB}$ on jännite (V) ja $V_A$ ja $V_B$ ovat kohtien potentiaalit (V) samaan nollakohtaan nähden. Jännite on positiivinen, kun $A$ on korkeammassa potentiaalissa.

Kirchhoffin jännitelaki silmukalle:
```latex
\sum \Delta V = 0
```
missä $\Delta V$ (V) on potentiaalin muutos silmukan kussakin osassa, kun silmukka kierretään kerran. Lähteessä miinusnavalta plusnavalle $\Delta V = +U$. Vastuksessa virran suuntaan $\Delta V = -RI$. Johtimessa $\Delta V = 0$. Yhden silmukan piirissä on kaksi vastusta. Laki antaa silloin $U - R_1 I - R_2 I = 0$ eli $U = R_1 I + R_2 I$.

**Potentiaalikuvaaja** näyttää potentiaalin silmukan eri kohdissa. Kuvaajassa kierretään pisteillä $A$–$F$ merkityn piirin silmukka. Kierros alkaa miinusnavasta $F$, kulkee vastusten $R_1$ ja $R_2$ kautta ja palaa pisteeseen $F$. Lähteen nousu $+9{,}0\,\text{V}$ on yhtä suuri kuin vastusten laskujen $-3{,}0\,\text{V}$ ja $-6{,}0\,\text{V}$ summa. Johtimissa kuvaaja on vaakasuora.

<svg data-fig="potential-graph" viewBox="0 0 600 360" role="img" aria-label="Potentiaalikuvaaja. Pystyakseli on mittakaavassa, vaaka-akseli on kaavamainen. Kuvaajassa on potentiaali V volteissa, kun kierretään kuvan virtapiirin silmukka. Kierros alkaa lähteen miinusnavasta F, kulkee lähteen ja vastusten R1 ja R2 kautta ja palaa pisteeseen F. Lähteessä potentiaali nousee 0 voltista 9,0 volttiin. Johdinta pitkin pisteeseen A se pysyy 9,0 voltissa. Vastuksessa R1 se laskee 3,0 V arvoon 6,0 V pisteessä B. Vastuksessa R2 se laskee 6,0 V nollaan pisteessä E. Pisteestä E pisteeseen F potentiaali pysyy nollassa. Nousujen ja laskujen summa on nolla." style="max-width:100%;font-size:24px">
  <line x1="96" y1="230" x2="500" y2="230" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="170" x2="500" y2="170" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="96" y1="110" x2="500" y2="110" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="95" y1="290" x2="514" y2="290" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M526,290 L513,296 L513,284 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="96" y1="291" x2="96" y2="56" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M96,44 L102,57 L90,57 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="89" y1="230" x2="96" y2="230" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="215.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$3$</div></foreignObject>
  <line x1="89" y1="170" x2="96" y2="170" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="155.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$6$</div></foreignObject>
  <line x1="89" y1="110" x2="96" y2="110" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="64" y="95.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$9$</div></foreignObject>
  <foreignObject x="532" y="275.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\text{kohta}$</div></foreignObject>
  <foreignObject x="86" y="13.5" width="62" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$V\ (\text{V})$</div></foreignObject>
  <rect x="127.5" y="70" width="27" height="220" fill="#eef5f9"/>
  <foreignObject x="119" y="71.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$U$</div></foreignObject>
  <rect x="230.5" y="70" width="45" height="220" fill="#eef5f9"/>
  <foreignObject x="231" y="71.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_1$</div></foreignObject>
  <rect x="365.5" y="70" width="45" height="220" fill="#eef5f9"/>
  <foreignObject x="366" y="71.5" width="44" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_2$</div></foreignObject>
  <line x1="97" y1="230" x2="500" y2="230" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="97" y1="170" x2="500" y2="170" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="97" y1="110" x2="500" y2="110" stroke="#e3dccb" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="64" y="269.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <polyline points="96,290 141,290 141,110 186,110 230.5,110 275.5,170 320.5,170 365.5,170 410,290 455,290 500,290" fill="none" stroke="#1971c2" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="96" y1="290" x2="96" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="82" y="303.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$F$</div></foreignObject>
  <line x1="186" y1="290" x2="186" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="172" y="303.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A$</div></foreignObject>
  <line x1="320.5" y1="290" x2="320.5" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="306.5" y="303.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$B$</div></foreignObject>
  <line x1="455" y1="290" x2="455" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="441" y="303.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$E$</div></foreignObject>
  <line x1="500" y1="290" x2="500" y2="297" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="486" y="303.5" width="28" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$F$</div></foreignObject>
  <circle cx="96" cy="290" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="186" cy="110" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="320.5" cy="170" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="455" cy="290" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="500" cy="290" r="5.5" fill="#1971c2" stroke="#ffffff" stroke-width="2"/>
  <foreignObject x="149" y="185.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$+9{,}0\,\text{V}$</div></foreignObject>
  <foreignObject x="283.5" y="125.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-3{,}0\,\text{V}$</div></foreignObject>
  <foreignObject x="418" y="215.5" width="110" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$-6{,}0\,\text{V}$</div></foreignObject>
</svg>

## Esimerkki
Jännitelähteen jännite on $12\,\text{V}$. Lähteen plusnavasta virta kulkee vastuksen $R_1 = 20\,\Omega$ kautta haarautumispisteeseen $B$. Siitä lähtee kaksi rinnakkaista haaraa: vastus $R_2 = 60\,\Omega$ ja vastus $R_3 = 30\,\Omega$. Haarat palaavat lähteen miinusnapaan, joka on nollakohta. Mikä on pisteen $B$ potentiaali, ja kuinka suuri virta kulkee vastuksen $R_3$ kautta?

<!-- vaihe -->

**Tunnetut ja kysytty.** $U = 12\,\text{V}$, $R_1 = 20\,\Omega$, $R_2 = 60\,\Omega$, $R_3 = 30\,\Omega$ ja miinusnavan potentiaali $0\,\text{V}$. Kysytään pisteen $B$ potentiaalia $V_B$ ja virtaa $I_3$.

<!-- vaihe -->

**Periaate.** Koko virta $I_1$ kulkee lähteen ja vastuksen $R_1$ kautta. Rinnakkaiset vastukset korvataan yhdellä vastuksella $R_{23}$. Silloin Ohmin laki antaa virran $I_1$. Jännitelain mukaan potentiaali laskee plusnavan arvosta $U$ vastuksessa $R_1$ jännitteen $R_1 I_1$ verran. Vastus $R_3$ on pisteen $B$ ja nollakohdan välissä. Siksi sen jännite on $V_B$.

<!-- vaihe -->

**Kaava ratkaistuna.**
```latex
\begin{aligned}
&\frac{1}{R_{23}} = \frac{1}{R_2} + \frac{1}{R_3} \\
&I_1 = \frac{U}{R_1 + R_{23}} \\
&V_B = U - R_1 I_1 \\
&I_3 = \frac{V_B}{R_3}
\end{aligned}
```

<!-- vaihe -->

**Yksikkömuunnokset.** Ei tarvita. Kaikki suureet ovat perusyksiköissä, ja $1\,\text{V} : 1\,\Omega = 1\,\text{A}$.

<!-- vaihe -->

**Sijoitus.**
```latex
\begin{aligned}
&\frac{1}{R_{23}} = \frac{1}{60\,\Omega} + \frac{1}{30\,\Omega} \\
&R_{23} = 20\,\Omega \\
&I_1 = \frac{12\,\text{V}}{20\,\Omega + 20\,\Omega} = 0{,}30\,\text{A} \\
&V_B = 12\,\text{V} - 20\,\Omega \cdot 0{,}30\,\text{A} \\
&\phantom{V_B} = 6{,}0\,\text{V} \\
&I_3 = \frac{6{,}0\,\text{V}}{30\,\Omega} = 0{,}20\,\text{A}
\end{aligned}
```

<!-- vaihe -->

**Tulos.** Pisteen $B$ potentiaali on $6{,}0\,\text{V}$. Vastuksen $R_3$ kautta kulkee virta $0{,}20\,\text{A}$. Tulokset on annettu kahdella merkitsevällä numerolla kuten resistanssit.

<!-- vaihe -->

**Järkevyys.** Vastuksen $R_2$ kautta kulkee $6{,}0\,\text{V} : 60\,\Omega = 0{,}10\,\text{A}$. Haarojen virrat ovat yhteensä $0{,}30\,\text{A}$, kuten virtalaki vaatii. Silmukassa $12\,\text{V} - 6{,}0\,\text{V} - 6{,}0\,\text{V} = 0$, kuten jännitelaki vaatii. Pienemmän resistanssin haaraan kulkee suurempi virta, kuten pitääkin.

## Yleinen virhekäsitys
Moni ajattelee, että vastus kuluttaa virtaa. Silloin virta olisi vastuksen jälkeen pienempi kuin ennen sitä. Vastus muuttaa sähköenergiaa sisäenergiakseen, mutta varauksia ei katoa. Virtamittari näyttää vastuksen kummallakin puolella saman lukeman. Vastuksessa pienenee potentiaali, ei virta.

Toinen yleinen virhe on käyttää haaran virran laskemisessa lähteen jännitettä. Oletetaan, että edellä esimerkissä laskettaisiin $I_3 = 12\,\text{V} : 30\,\Omega = 0{,}40\,\text{A}$. Silloin haaroihin lähtisi yhteensä enemmän virtaa kuin haarautumispisteeseen tulee. Haaran jännite on lähteen jännite miinus sarjaan kytkettyjen vastusten jännitteet. Tässä se on $6{,}0\,\text{V}$. Kolmas virhe on ajatella, että jännite on jonkin yksittäisen kohdan ominaisuus. Jännite on aina kahden kohdan välinen potentiaaliero.

## Tiivistelmä
- Kirchhoffin virtalaki: haarautumispisteeseen tulevien virtojen summa on yhtä suuri kuin siitä lähtevien virtojen summa, koska varaus säilyy. Virta ei kulu vastuksessa.
- Potentiaali $V$ on kohdan jännite nollakohtaan nähden. Jännite on potentiaaliero $U_{AB} = V_A - V_B$. Se ei riipu nollakohdan valinnasta.
- Potentiaali nousee lähteessä miinusnavalta plusnavalle. Vastuksessa se laskee virran suuntaan $RI$:n verran. Johtimessa se pysyy samana.
- Kirchhoffin jännitelaki: silmukan potentiaalin muutosten summa on nolla, $\sum \Delta V = 0$. Siksi lähteen jännite jakautuu silmukan vastuksille, ja rinnakkaisten haarojen yli on sama jännite.
