# Planckin vakio LEDien avulla

> **Tutkimuskysymys:** Miten LEDin kynnysjännite riippuu sen lähettämän valon aallonpituudesta, ja kuinka suuri Planckin vakio on tämän perusteella?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: laboratorion työpöydällä on pienjännitelähde, säädettävä liukuvastus ja kaksi yleismittaria, joiden näytöissä ei ole lukemia. Johdot kulkevat kytkentäalustalle, jossa yksi LED loistaa himmeästi. Pöydällä on rasia, jossa on erivärisiä sammuneita LEDejä, sekä LEDien tietolehti ja vihko." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy10plh-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#dfe9ef"/></linearGradient><linearGradient id="fy10plh-desk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy10plh-wall)"/>
  <rect x="0" y="470" width="1200" height="130" fill="url(#fy10plh-desk)"/>
  <line x1="0" y1="492" x2="1200" y2="488" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="514" x2="1200" y2="510" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="536" x2="1200" y2="532" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="558" x2="1200" y2="554" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="580" x2="1200" y2="576" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="470" x2="1200" y2="470" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <rect x="60" y="300" width="220" height="170" rx="10" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="84" y="324" width="120" height="46" rx="4" fill="#2b3a42" stroke="#1f2933" stroke-width="2"/>
  <circle cx="240" cy="347" r="20" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="240" y1="347" x2="252" y2="333" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="110" cy="430" r="9" fill="#1f2933" stroke="#1f2933" stroke-width="2"/>
  <circle cx="230" cy="430" r="9" fill="#e9ecef" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="340" y="400" width="26" height="70" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="574" y="400" width="26" height="70" rx="3" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="366" y="412" width="208" height="46" rx="8" fill="#d9a066" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="372" y1="413" x2="372" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="380" y1="413" x2="380" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="388" y1="413" x2="388" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="396" y1="413" x2="396" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="404" y1="413" x2="404" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="412" y1="413" x2="412" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="420" y1="413" x2="420" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="428" y1="413" x2="428" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="436" y1="413" x2="436" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="444" y1="413" x2="444" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="452" y1="413" x2="452" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="460" y1="413" x2="460" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="468" y1="413" x2="468" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="476" y1="413" x2="476" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="484" y1="413" x2="484" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="492" y1="413" x2="492" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="500" y1="413" x2="500" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="508" y1="413" x2="508" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="516" y1="413" x2="516" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="524" y1="413" x2="524" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="532" y1="413" x2="532" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="540" y1="413" x2="540" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="548" y1="413" x2="548" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="556" y1="413" x2="556" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="564" y1="413" x2="564" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <line x1="572" y1="413" x2="572" y2="457" stroke="#a5653a" stroke-width="2" stroke-linecap="butt"/>
  <rect x="350" y="384" width="240" height="8" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <rect x="468" y="376" width="30" height="36" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="640" y="330" width="120" height="140" rx="10" fill="#f4c542" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="652" y="342" width="96" height="47.5" rx="4" fill="#2b3a42" stroke="#1f2933" stroke-width="2"/>
  <circle cx="700" cy="422.5" r="19.6" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="700" y1="422.5" x2="700" y2="405.5" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="676" cy="458" r="5" fill="#1f2933"/>
  <circle cx="724" cy="458" r="5" fill="#1f2933"/>
  <rect x="800" y="330" width="120" height="140" rx="10" fill="#f4c542" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="812" y="342" width="96" height="47.5" rx="4" fill="#2b3a42" stroke="#1f2933" stroke-width="2"/>
  <circle cx="860" cy="422.5" r="19.6" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="860" y1="422.5" x2="860" y2="405.5" stroke="#ffffff" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="836" cy="458" r="5" fill="#1f2933"/>
  <circle cx="884" cy="458" r="5" fill="#1f2933"/>
  <rect x="960" y="430" width="200" height="40" rx="4" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="972" y="440" width="5" height="5" fill="#c9c2b2"/>
  <rect x="983.5" y="440" width="5" height="5" fill="#c9c2b2"/>
  <rect x="995" y="440" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1006.5" y="440" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1018" y="440" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1029.5" y="440" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1041" y="440" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1052.5" y="440" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1064" y="440" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1075.5" y="440" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1087" y="440" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1098.5" y="440" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1110" y="440" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1121.5" y="440" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1133" y="440" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1144.5" y="440" width="5" height="5" fill="#c9c2b2"/>
  <rect x="972" y="453" width="5" height="5" fill="#c9c2b2"/>
  <rect x="983.5" y="453" width="5" height="5" fill="#c9c2b2"/>
  <rect x="995" y="453" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1006.5" y="453" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1018" y="453" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1029.5" y="453" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1041" y="453" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1052.5" y="453" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1064" y="453" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1075.5" y="453" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1087" y="453" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1098.5" y="453" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1110" y="453" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1121.5" y="453" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1133" y="453" width="5" height="5" fill="#c9c2b2"/>
  <rect x="1144.5" y="453" width="5" height="5" fill="#c9c2b2"/>
  <circle cx="1060" cy="378" r="46" fill="#f2a69c" fill-opacity="0.35"/>
  <circle cx="1060" cy="378" r="30" fill="#f2a69c" fill-opacity="0.45"/>
  <line x1="1054" y1="406" x2="1054" y2="440" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt"/>
  <line x1="1066" y1="406" x2="1066" y2="434" stroke="#8a96a3" stroke-width="3" stroke-linecap="butt"/>
  <rect x="1043" y="398" width="34" height="8" rx="2" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <path d="M1046,398 L1046,370 A14,14 0 0 1 1074,370 L1074,398 Z" fill="#f2a69c" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="1090" y="430" width="40" height="10" rx="4" fill="#d9a066" stroke="#1f2933" stroke-width="2"/>
  <path d="M230,430 C230,520 350,500 353,470" fill="none" stroke="#1f2933" stroke-width="3.5" stroke-linejoin="round"/>
  <path d="M483,376 C483,300 640,290 676,458" fill="none" stroke="#1f2933" stroke-width="3.5" stroke-linejoin="round"/>
  <path d="M724,458 C780,492 1060,492 1110,440" fill="none" stroke="#1f2933" stroke-width="3.5" stroke-linejoin="round"/>
  <path d="M1054,410 C1000,300 840,300 836,458" fill="none" stroke="#6c757d" stroke-width="3.5" stroke-linejoin="round"/>
  <path d="M1066,410 C1080,320 900,320 884,458" fill="none" stroke="#6c757d" stroke-width="3.5" stroke-linejoin="round"/>
  <path d="M110,430 C110,488 1000,488 1040,470" fill="none" stroke="#1f2933" stroke-width="3.5" stroke-linejoin="round"/>
  <rect x="420" y="500" width="230" height="50" rx="6" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="446.5" y1="521.5" x2="446.5" y2="540" stroke="#8a96a3" stroke-width="1.65" stroke-linecap="butt"/>
  <line x1="453.5" y1="521.5" x2="453.5" y2="536.5" stroke="#8a96a3" stroke-width="1.65" stroke-linecap="butt"/>
  <rect x="440.5" y="517" width="18.5" height="4.5" rx="2" fill="#ffc078" stroke="#1f2933" stroke-width="2"/>
  <path d="M442.5,517 L442.5,501.5 A7.5,7.5 0 0 1 457.5,501.5 L457.5,517 Z" fill="#ffc078" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <line x1="488.5" y1="521.5" x2="488.5" y2="540" stroke="#8a96a3" stroke-width="1.65" stroke-linecap="butt"/>
  <line x1="495.5" y1="521.5" x2="495.5" y2="536.5" stroke="#8a96a3" stroke-width="1.65" stroke-linecap="butt"/>
  <rect x="482.5" y="517" width="18.5" height="4.5" rx="2" fill="#b2f2bb" stroke="#1f2933" stroke-width="2"/>
  <path d="M484.5,517 L484.5,501.5 A7.5,7.5 0 0 1 499.5,501.5 L499.5,517 Z" fill="#b2f2bb" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <line x1="530.5" y1="521.5" x2="530.5" y2="540" stroke="#8a96a3" stroke-width="1.65" stroke-linecap="butt"/>
  <line x1="537.5" y1="521.5" x2="537.5" y2="536.5" stroke="#8a96a3" stroke-width="1.65" stroke-linecap="butt"/>
  <rect x="524.5" y="517" width="18.5" height="4.5" rx="2" fill="#d0e6fb" stroke="#1f2933" stroke-width="2"/>
  <path d="M526.5,517 L526.5,501.5 A7.5,7.5 0 0 1 541.5,501.5 L541.5,517 Z" fill="#d0e6fb" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <line x1="572.5" y1="521.5" x2="572.5" y2="540" stroke="#8a96a3" stroke-width="1.65" stroke-linecap="butt"/>
  <line x1="579.5" y1="521.5" x2="579.5" y2="536.5" stroke="#8a96a3" stroke-width="1.65" stroke-linecap="butt"/>
  <rect x="566.5" y="517" width="18.5" height="4.5" rx="2" fill="#ffe066" stroke="#1f2933" stroke-width="2"/>
  <path d="M568.5,517 L568.5,501.5 A7.5,7.5 0 0 1 583.5,501.5 L583.5,517 Z" fill="#ffe066" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <line x1="614.5" y1="521.5" x2="614.5" y2="540" stroke="#8a96a3" stroke-width="1.65" stroke-linecap="butt"/>
  <line x1="621.5" y1="521.5" x2="621.5" y2="536.5" stroke="#8a96a3" stroke-width="1.65" stroke-linecap="butt"/>
  <rect x="608.5" y="517" width="18.5" height="4.5" rx="2" fill="#ffd8a8" stroke="#1f2933" stroke-width="2"/>
  <path d="M610.5,517 L610.5,501.5 A7.5,7.5 0 0 1 625.5,501.5 L625.5,517 Z" fill="#ffd8a8" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <g transform="translate(790,535) rotate(4)"><rect x="-60" y="-40" width="120" height="70" rx="3" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/><line x1="-46" y1="-26" x2="46" y2="-26" stroke="#6b7480" stroke-width="2"/><line x1="-46" y1="-15" x2="28" y2="-15" stroke="#6b7480" stroke-width="2"/><line x1="-46" y1="-4" x2="46" y2="-4" stroke="#6b7480" stroke-width="2"/><line x1="-46" y1="7" x2="28" y2="7" stroke="#6b7480" stroke-width="2"/><line x1="-46" y1="18" x2="46" y2="18" stroke="#6b7480" stroke-width="2"/></g>
  <g transform="translate(130,530) rotate(-6)"><rect x="-80" y="-34" width="200" height="66" rx="4" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/><line x1="-64" y1="-18" x2="104" y2="-18" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/><line x1="-64" y1="-6" x2="104" y2="-6" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/><line x1="-64" y1="6" x2="104" y2="6" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/><line x1="-64" y1="18" x2="104" y2="18" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/><line x1="-64" y1="30" x2="104" y2="30" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/></g>
</svg>

Planckin vakio on yksi luonnon perusvakioista: se kertoo, kuinka suuri energia valon pienimmällä osalla, fotonilla, on. Vakion voi määrittää koulun laboratoriossa tavallisilla LEDeillä ja kahdella yleismittarilla. Tässä tutkimuksessa mittaat usean erivärisen LEDin sähköisiä ominaisuuksia ja päättelet niistä Planckin vakion. Mittaa, piirrä ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** kuinka suuri kynnysjännite on usealla erivärisellä LEDillä, miten se riippuu LEDin valon aallonpituudesta ja kuinka suuri Planckin vakio on tämän perusteella epävarmuuksineen. Vertaa tulosta Planckin vakion tunnettuun arvoon.

**Päätät itse** (osittain ohjattu ja itsenäinen työtapa): kuinka monta LEDiä ja mittauspistettä käytät ja millä jännitealueella mittaat opettajan ilmoittaman virtarajan sisällä, miten määrität kynnysjännitteen, kuvaajan akselit perusteluineen sekä tavan, jolla arvioit tuloksen epävarmuuden. Ohjatussa työtavassa sivu kiinnittää nämä valinnat. Osittain ohjatussa työtavassa sivu antaa vaihtoehdot kynnysjännitteen määrittämiseen ja epävarmuuden arvioimiseen, ja valitset niistä perustellen. Itsenäisessä työtavassa valitset ja perustelet kaiken itse.

::: tuki I
**Itsenäinen työtapa.** Jos koulussa on hila tai spektrometri, laajennus kuuluu työhösi: mittaa ainakin yhden LEDin aallonpituus itse ja vertaa sitä tietolehden arvoon.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Kun LEDin jännitettä kasvatetaan nollasta alkaen, miten arvelet sen läpi kulkevan sähkövirran muuttuvan? Alkaako LED loistaa heti?
2. Kummalla arvelet olevan suuremman kynnysjännitteen, punaisella vai sinisellä LEDillä?
3. Jos LEDin valon aallonpituus olisi kaksi kertaa niin suuri, mitä arvelet tapahtuvan kynnysjännitteelle?
4. Kuinka lähelle tunnettua arvoa arvelet pääseväsi, ja mikä mittauksessa on todennäköisesti suurin epävarmuuden lähde?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Teoriaa lyhyesti

Tämän työn fysiikkaa käsitellään tarkemmin moduuleissa FY6–FY8, joita ei ole vielä julkaistu Ruukkilabrassa. Tässä on se, mitä tutkimuksessa tarvitset.

**Fotoni.** Valo siirtää energiaa pieninä paloina, fotoneina. Fotonin energia on

```latex
E = hf
```

missä $E$ on fotonin energia, $f$ valon taajuus ja $h$ **Planckin vakio**, jonka yksikkö on $\text{J}\cdot\text{s}$. Valon taajuus ja aallonpituus $\lambda$ liittyvät toisiinsa yhtälöllä $c = f\lambda$, missä $c$ on valon nopeus tyhjiössä. Kun aallonpituus tunnetaan, taajuus on $f = \dfrac{c}{\lambda}$.

**Varaus ja jännite.** Kun varattu hiukkanen siirtyy jännitteen $U$ yli, sen energia muuttuu määrällä $qU$. Elektronin varauksen suuruus on alkeisvaraus $e$, joten elektronin energia muuttuu määrällä $eU$.

**LED.** LED eli hohtodiodi on puolijohdekomponentti, joka johtaa sähkövirtaa hyvin vain yhteen suuntaan, päästösuuntaan. Kun virta kulkee LEDin läpi päästösuuntaan, elektronit menettävät puolijohteessa energiaa, ja energia voi vapautua fotonina. Fotonin energia ja siten valon väri määräytyvät LEDin puolijohdemateriaalista: fotonin energia on suunnilleen yhtä suuri kuin materiaalin energia-aukko eli energiaero, jonka elektroni menettää, ja kynnysjännitteestä laskettu energia $eU_\text{k}$ on vain likiarvo sille. LED alkaa johtaa sähkövirtaa ja lähettää valoa vasta, kun sen jännite on riittävän suuri. Jännitettä, jolla tämä alkaa, kutsutaan tässä työssä **kynnysjännitteeksi** $U_\text{k}$.

**Periaate.** Elektroni voi tuottaa fotonin vain, jos sillä on vähintään fotonin energia. Siksi LED alkaa loistaa suunnilleen silloin, kun yhden elektronin energia $eU_\text{k}$ on yhtä suuri kuin yhden fotonin energia:

```latex
eU_\text{k} \approx hf
```

Yhteys on vain likimääräinen, ja sen ehdot kannattaa pitää mielessä koko työn ajan: LED ei lähetä yhtä ainoaa aallonpituutta vaan kapean aallonpituusalueen, kynnysjännitteen arvo riippuu siitä, miten se määritetään, osa LEDin jännitteestä kuluu sen sisäiseen resistanssiin, ja LEDin lämpeneminen muuttaa sen ominaisuuksia. Vakiot $e = 1{,}602\,176\,634\cdot10^{-19}\ \text{C}$ ja $c = 2{,}997\,924\,58\cdot10^{8}\ \text{m/s}$ ovat tarkkoja määriteltyjä arvoja.

::: tuki O
**Malli kuvaajaksi.** Kun periaatteeseen sijoitetaan $f = \dfrac{c}{\lambda}$ ja ratkaistaan kynnysjännite, saadaan

```latex
U_\text{k} = \frac{hc}{e}\cdot\frac{1}{\lambda}
```

Kynnysjännite on siis mallin mukaan suoraan verrannollinen aallonpituuden käänteislukuun $\dfrac{1}{\lambda}$. Kuvaaja $U_\text{k}$ suureen $\dfrac{1}{\lambda}$ funktiona on suora, jonka kulmakerroin on $k = \dfrac{hc}{e}$. Planckin vakio saadaan kulmakertoimesta:

```latex
h = \frac{ek}{c}
```

<svg data-fig="model" viewBox="0 0 600 330" role="img" aria-label="Kuvaaja: kynnysjännite U k aallonpituuden käänteisluvun yksi per lambda funktiona mallin mukaan. Kuvaaja on origon kautta kulkeva suora, jonka kulmakerroin on h kertaa c jaettuna e:llä. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="280" x2="484" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,280 L483,286 L483,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="281" x2="90" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,24 L96,37 L84,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="60" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="251" width="20" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$\dfrac{1}{\lambda}$</div></foreignObject>
  <foreignObject x="80" y="-6.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U_\text{k}$</div></foreignObject>
  <polyline points="90,280 451,83.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <foreignObject x="127.5" y="76" width="183" height="58" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{kulmakerroin } \dfrac{hc}{e}$</div></foreignObject>
</svg>

Jos kaikkien LEDien kynnysjännitteissä on suunnilleen sama lisäosa, esimerkiksi määritystavasta johtuen, suora siirtyy ylös tai alas eikä kulje origon kautta, mutta kulmakerroin ei muutu. Siksi Planckin vakio kannattaa määrittää kulmakertoimesta eikä yksittäisen LEDin tuloksesta. Eri puolijohdemateriaaleista tehdyillä LEDeillä lisäosa voi kuitenkin olla erisuuruinen, ja silloin se muuttaa myös kulmakerrointa. Mittaamalla selviää, kuinka hyvin malli pätee.
:::

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, mitä muutat, mitä mittaat ja mitä pidät vakiona. Piirrä kytkentäkaavio ja näytä kytkentä opettajalle ennen kuin kytket virran. LEDin kanssa sarjassa on aina oltava vastus, joka rajoittaa sähkövirtaa. Jos säädettävän vastuksen voi säätää nollaan, kytke sen lisäksi sarjaan kiinteä suojavastus, jonka opettaja antaa. Kirjaa myös, mistä saat LEDien aallonpituudet: ne luetaan LEDien tietolehdistä, tai mittaat ne itse spektrometrillä tai hilalla, jos sellainen on käytettävissä (katso laajennus). Älä arvaa aallonpituutta värin perusteella.

::: tuki O
**Ohjattu.** Mittaat jokaisesta LEDistä sarjan, jossa muutat LEDin jännitettä $U$ säätämällä virtalähdettä tai säädettävää vastusta ja luet joka kerta jännitteen $U$ ja sähkövirran $I$. Kynnysjännitteen määrität myöhemmin näistä mittauksista. Käytä kaikkia opettajan antamia erivärisiä LEDejä, joiden aallonpituus tiedetään, mieluiten ainakin neljää. Mittaa jokaisesta LEDistä ainakin kahdeksan pistettä: muutama jännitteillä, joilla virtaa ei juuri kulje, ja ainakin viisi alueelta, jolla virta kasvaa jyrkästi. Vakiona pidät kytkennän, mittarit ja niiden mittausalueet sekä tavan, jolla mittaat.
:::

::: tuki OO
**Osittain ohjattu.** Muuttuja on LEDin väri eli aallonpituus, ja jokaisesta LEDistä mittaat jännitteen ja sähkövirran. Päätä itse, kuinka monta LEDiä ja mittauspistettä käytät ja millä jännitealueella mittaat. Valitse kynnysjännitteen määritystapa kohdassa Käsittele tulokset annetuista vaihtoehdoista. Kirjaa päätöksesi perusteluineen.
:::

::: tuki O OO
Tarkista kytkentäsi tästä:

<svg data-fig="setup" viewBox="0 0 600 400" role="img" aria-label="Kytkentäkaavio. Tasajännitelähteen plusnavasta virta kulkee kiinteän suojavastuksen R s ja säädettävän vastuksen R kautta LEDiin ja siitä virtamittarin kautta takaisin miinusnapaan. LED on kytketty päästösuuntaan. Vastukset rajoittavat virtaa, ja virtamittari on sarjassa LEDin kanssa ja mittaa sähkövirran I. Jännitemittari on kytketty suoraan LEDin napoihin eli rinnan LEDin kanssa, ja se mittaa LEDin jännitteen U." style="max-width:100%;font-size:24px">
  <rect x="30" y="140" width="130" height="110" rx="6" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="65" y="158" width="60" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\text{tasa-}$</div></foreignObject>
  <foreignObject x="49.5" y="184" width="91" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\text{jännite-}$</div></foreignObject>
  <foreignObject x="65" y="210" width="60" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px">$\text{lähde}$</div></foreignObject>
  <circle cx="160" cy="80" r="5" fill="#1f2933"/>
  <circle cx="160" cy="320" r="5" fill="#1f2933"/>
  <line x1="140" y1="140" x2="140" y2="80" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="140" y1="80" x2="160" y2="80" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="140" y1="250" x2="140" y2="320" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="140" y1="320" x2="160" y2="320" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="111" y="91" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:22px">$+$</div></foreignObject>
  <foreignObject x="111" y="283" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:22px">$-$</div></foreignObject>
  <line x1="160" y1="80" x2="191" y2="80" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="259" y1="80" x2="290" y2="80" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="191" y="67" width="68" height="26" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="208.5" y="25.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R_\text{s}$</div></foreignObject>
  <line x1="290" y1="80" x2="321" y2="80" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="389" y1="80" x2="420" y2="80" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <rect x="321" y="67" width="68" height="26" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="315" y1="106" x2="388" y2="58" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M397,52 L390,63 L384,54 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="345" y="19.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$R$</div></foreignObject>
  <foreignObject x="280" y="347.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I$</div></foreignObject>
  <line x1="420" y1="80" x2="420" y2="140" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="420" y1="140" x2="420" y2="182" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="420" y1="218" x2="420" y2="260" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M400,182 L440,182 L420,216 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="398" y1="217" x2="442" y2="217" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <line x1="442" y1="190" x2="458.5" y2="179" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M466,174 L460,183.5 L455,176 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="442" y1="206" x2="458.5" y2="195" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M466,190 L460,199.5 L455,192 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="420" y1="260" x2="420" y2="320" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="160" y1="320" x2="268" y2="320" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="312" y1="320" x2="420" y2="320" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="290" cy="320" r="22" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="280.5" y="307" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px">$\mathrm{A}$</div></foreignObject>
  <circle cx="420" cy="140" r="5" fill="#1f2933"/>
  <circle cx="420" cy="260" r="5" fill="#1f2933"/>
  <line x1="420" y1="140" x2="530" y2="140" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="530" y1="140" x2="530" y2="178" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="530" cy="200" r="22" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="520.5" y="187" width="19" height="26" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px">$\mathrm{V}$</div></foreignObject>
  <line x1="530" y1="222" x2="530" y2="260" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="420" y1="260" x2="530" y2="260" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="562" y="185.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U$</div></foreignObject>
  <foreignObject x="333" y="188" width="39" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:20px;color:#6b7480">$\text{LED}$</div></foreignObject>
</svg>

Mieti ainakin näitä:

- Miksi jännitemittari kytketään suoraan LEDin napoihin eikä virtalähteen napoihin?
- Kumpi LEDin jaloista kytketään plusnapaan päin? Yleensä pidempi jalka on plusnapaan kytkettävä anodi, mutta tarkista asia opettajalta tai tietolehdestä.
- Miten varmistat, että virta pysyy opettajan ilmoittaman rajan alapuolella, vaikka säädät vastusta?
:::

## Mittaa

Kirjaa alkuperäiset mittaustulokset taulukkoon heti mittauksen aikana: jokaiselle LEDille oma mittaussarja, ja lisäksi jokaisen LEDin väri ja aallonpituus sekä tieto siitä, mistä aallonpituus on peräisin. Laskemasi suureet saavat omat sarakkeensa mitattujen oikealle puolelle.

Pidä virta koko ajan opettajan ilmoittaman rajan alapuolella, äläkä katso suoraan kirkkaasti loistavaan LEDiin. UV- ja infrapuna-LEDiin ei katsota koskaan suoraan, ja UV-LEDin kanssa käytetään opettajan antamia silmäsuojaimia.

::: tuki O
Voit käyttää jokaiselle LEDille esimerkiksi tällaista taulukkoa:

| $U\ (\text{V})$ | $I\ (\text{mA})$ |
|---|---|
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |

Kokoa lopuksi kaikkien LEDien tulokset yhteen taulukkoon:

| LED | $\lambda\ (\text{nm})$ | $\dfrac{1}{\lambda}\ \left(\dfrac{1}{\text{m}}\right)$ | $U_\text{k}\ (\text{V})$ |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

Aloita jännitteestä nolla ja kasvata sitä pienin askelin. Kun virta alkaa kasvaa, pienennä askelia. Lopeta sarja, kun virta lähestyy opettajan ilmoittamaa rajaa. Lue mittarit vasta, kun lukemat ovat asettuneet, ja mittaa sarja ripeästi, ettei LED ehdi lämmetä. Katkaise virta aina, kun vaihdat LEDiä.
:::

Muista mittausepävarmuus: kirjaa mittareiden lukematarkkuus ja aallonpituuden epävarmuus, eli tietolehden ilmoittama vaihteluväli tai oma arviosi. [[apua:fy1-3|Mittausepävarmuuden arvioiminen]]

## Käsittele tulokset

Käsittele tulokset kahdessa vaiheessa. Merkitse kaikkien kuvaajien akseleille suureet ja yksiköt, piirrä mittauspisteet, älä yhdistä niitä murtoviivalla, ja sovita suora vain niihin pisteisiin, joihin se mallin mukaan kuuluu. [[apua:fy1-4|Suoran sovittaminen ja kulmakertoimen tulkinta]]

1. Piirrä jokaisen LEDin mittauksista virta–jännite-kuvaaja ja määritä siitä LEDin kynnysjännite. Kirjaa, miten määritit sen, ja perustele, miksi juuri tämä tapa kuvaa jännitettä, jolla LED alkaa lähettää fotoneja.
2. Muunna aallonpituudet metreiksi. Piirrä kaikkien LEDien tuloksista kuvaaja, josta Planckin vakio saadaan kulmakertoimen avulla, ja perustele, miksi valitsit juuri nämä akselit.
3. Millainen riippuvuus pisteistä näkyy? Jos sovitit pisteisiin suoran, kirjoita sen yhtälö ja pohdi, mistä mahdollinen vakiotermi voi johtua.
4. Mikä on kulmakertoimen yksikkö? Laske Planckin vakio kulmakertoimesta ja tarkista, että yksiköksi tulee $\text{J}\cdot\text{s}$.

::: tuki O OO
**Kynnysjännitteen määrittäminen.** LEDin virta–jännite-kuvaaja on mallin mukaan tämän muotoinen:

<svg data-fig="iu" viewBox="0 0 600 330" role="img" aria-label="Kuvaaja: LEDin sähkövirta I jännitteen U funktiona mallin mukaan. Pienillä jännitteillä virta on lähes nolla. Tietyn jännitteen jälkeen virta kasvaa jyrkästi ja lähes suoraviivaisesti. Jyrkän osan suora on jatkettu katkoviivalla vaaka-akselille, ja leikkauskohta on merkitty kynnysjännitteeksi U k. Kuvaajassa ei ole mittauspisteitä." style="max-width:100%;font-size:24px">
  <line x1="89" y1="280" x2="484" y2="280" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M496,280 L483,286 L483,274 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="90" y1="281" x2="90" y2="36" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M90,24 L96,37 L84,37 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="60" y="285.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$0$</div></foreignObject>
  <foreignObject x="502" y="265.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U$</div></foreignObject>
  <foreignObject x="80" y="-6.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$I$</div></foreignObject>
  <polyline points="90,280 92.5,280 95.5,280 98,280 100.5,280 103.5,280 106,280 108.5,280 111.5,280 114,280 116.5,280 119.5,280 122,280 124.5,280 127,280 130,280 132.5,280 135,280 138,280 140.5,280 143,280 146,280 148.5,280 151,280 154,280 156.5,280 159,280 162,280 164.5,280 167,280 170,280 172.5,280 175,280 178,280 180.5,280 183,280 186,280 188.5,280 191,280 193.5,280 196.5,280 199,280 201.5,280 204.5,280 207,280 209.5,280 212.5,280 215,280 217.5,280 220.5,280 223,280 225.5,280 228.5,280 231,280 233.5,280 236.5,280 239,279.5 241.5,279.5 244.5,279.5 247,279.5 249.5,279.5 252.5,279 255,279 257.5,279 260,278.5 263,278.5 265.5,278 268,277.5 271,277 273.5,276.5 276,275.5 279,275 281.5,274 284,272.5 287,271.5 289.5,269.5 292,268 295,266 297.5,263.5 300,261 303,258 305.5,255 308,252 311,248.5 313.5,244.5 316,240.5 319,236.5 321.5,232 324,228 326.5,223.5 329.5,218.5 332,214 334.5,209 337.5,204.5 340,199.5 342.5,194.5 345.5,189.5 348,184.5 350.5,179.5 353.5,174.5 356,169 358.5,164 361.5,159 364,154 366.5,149 369.5,143.5 372,138.5 374.5,133.5 377.5,128.5 380,123 382.5,118 385.5,113 388,107.5 390.5,102.5 393,97.5 396,92.5 398.5,87 401,82 404,77 406.5,71.5 409,66.5" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <polyline points="299,280 417,52" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="7 5"/>
  <line x1="299" y1="272" x2="299" y2="288" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <foreignObject x="282.5" y="289.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$U_\text{k}$</div></foreignObject>
  <foreignObject x="101" y="102.5" width="164" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:20px;color:#6b7480">$\text{jyrkän osan suora}$</div></foreignObject>
  <line x1="268.5" y1="119" x2="363.5" y2="151" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
</svg>

Kynnysjännitteen voi määrittää esimerkiksi näillä tavoilla:

- **Jyrkän osan suora.** Sovita suora virta–jännite-kuvaajan jyrkästi nousevaan, lähes suoraan osaan ja jatka sitä vaaka-akselille. Leikkauskohdan jännite on kynnysjännite. Tapa käyttää monta mittauspistettä, joten yksittäisen lukeman virhe vaikuttaa vähemmän.
- **Valon syttyminen.** Kasvata jännitettä hämärässä huoneessa hitaasti ja kirjaa jännite, jolla LEDistä näkyy ensimmäinen heikko valo. Tapa on nopea, mutta tulos riippuu katsojan silmästä ja huoneen valaistuksesta. Tapa sopii vain näkyvää valoa lähettäville LEDeille: infrapuna-LEDin valoa ei näe lainkaan, eikä UV- tai infrapuna-LEDiin katsota koskaan suoraan.
- **Pieni sovittu virta.** Kirjaa jännite, jolla virta saavuttaa saman pienen arvon jokaisella LEDillä. Tapa on johdonmukainen, mutta tulos riippuu valitusta virrasta.

Käytä samaa tapaa kaikilla LEDeillä.
:::

::: tuki O
Määritä kynnysjännite jyrkän osan suoran avulla. Valitse virta–jännite-kuvaajassa pystyakselille virta $I$ ja vaaka-akselille jännite $U$. Valitse yhteisessä kuvaajassa pystyakselille kynnysjännite $U_\text{k}$ ja vaaka-akselille $\dfrac{1}{\lambda}$.
:::

::: tuki O OO
**Tarkista vastauksesi tästä: miksi juuri nämä akselit?** Kun periaatteeseen $eU_\text{k} \approx hf$ sijoitetaan $f = \dfrac{c}{\lambda}$ ja ratkaistaan kynnysjännite, saadaan

```latex
U_\text{k} = \frac{hc}{e}\cdot\frac{1}{\lambda}
```

Tämä on suoran yhtälö $y = kx$, kun pystyakselille valitaan $U_\text{k}$ ja vaaka-akselille $\dfrac{1}{\lambda}$. Silloin kulmakerroin on $k = \dfrac{hc}{e}$, sen yksikkö on $\text{V}\cdot\text{m}$, ja Planckin vakio on $h = \dfrac{ek}{c}$. Jos vaaka-akselille valittaisiin aallonpituus $\lambda$, pisteet asettuisivat käyrälle eikä suoralle. Toinen hyvä valinta on pystyakselille fotonin energia $eU_\text{k}$ ja vaaka-akselille taajuus $f = \dfrac{c}{\lambda}$: silloin kulmakerroin on suoraan $h$. Aallonpituus muunnetaan metreiksi ennen käänteisluvun laskemista: $1\ \text{nm} = 10^{-9}\ \text{m}$.

Tarkista vielä kuvaajastasi: ovatko pisteet suoralla, ja kulkeeko suora origon kautta? Jos kaikkien LEDien kynnysjännitteissä on sama lisäosa, suora siirtyy ylös tai alas, mutta kulmakerroin ei muutu. Eri materiaaleista tehdyillä LEDeillä lisäosa voi olla erisuuruinen, ja silloin se muuttaa myös kulmakerrointa.
:::

Kuvaajien piirtämiseen ja sovitukseen voit käyttää esimerkiksi Graphical Analysis -ohjelmaa tai taulukkolaskentaa. Ruukkilabran ohjeet: [[ohje:tvt-suoran-sovitus|Suoran sovittaminen]], [[ohje:tvt-kulmakerroin|Kulmakertoimen tulkinta]] ja [[ohje:tvt-taulukkolaskenta|Taulukkolaskenta]].

## Epävarmuus ja luotettavuus

Ilmoita Planckin vakio muodossa $h = (h \pm \Delta h)\ \text{J}\cdot\text{s}$ ja perustele, miten arvioit epävarmuuden $\Delta h$.

::: tuki O OO
Koska $e$ ja $c$ ovat tarkkoja arvoja, Planckin vakion suhteellinen epävarmuus on sama kuin kulmakertoimen: $\dfrac{\Delta h}{h} = \dfrac{\Delta k}{k}$. Kulmakertoimen epävarmuuden voit arvioida jommallakummalla tavalla:

- **Sovitusohjelman keskivirhe.** Monet ohjelmat ilmoittavat kulmakertoimen keskivirheen. Käytä sitä epävarmuutena $\Delta k$.
- **Jyrkin ja loivin suora.** Piirrä jyrkin ja loivin suora, jotka vielä sopivat pisteisiin niiden epävarmuuksien rajoissa. Määritä niiden kulmakertoimet $k_\text{max}$ ja $k_\text{min}$ ja arvioi epävarmuus vaihteluvälin puolikkaana: $\Delta k = \dfrac{k_\text{max} - k_\text{min}}{2}$.

Pisteiden epävarmuudet saat näin. Kynnysjännitteen epävarmuuden voit arvioida sovittamalla jyrkkään osaan jyrkimmän ja loivimman sopivan suoran ja katsomalla, kuinka paljon niiden leikkauskohdat eroavat. Suureen $\dfrac{1}{\lambda}$ suhteellinen epävarmuus on sama kuin aallonpituuden: $\dfrac{\Delta(1/\lambda)}{1/\lambda} = \dfrac{\Delta\lambda}{\lambda}$.

Pyöristä $\Delta h$ yhteen merkitsevään numeroon ja $h$ samaan tarkkuuteen.
:::

::: tuki O
Ohjatussa työtavassa käytä kulmakertoimen epävarmuutena jyrkimmän ja loivimman suoran menetelmää.
:::

Vertaa tulosta Planckin vakion tunnettuun arvoon $h = 6{,}626\,070\,15\cdot10^{-34}\ \text{J}\cdot\text{s}$. Laske, kuinka monta prosenttia tuloksesi poikkeaa siitä, ja tarkista, mahtuuko tunnettu arvo epävarmuusvälisi sisään.

Pohdi sitten luotettavuutta konkreettisesti: mitkä tekijät aiheuttivat mittausepävarmuutta, olivatko ne satunnaisia vai systemaattisia, ja mihin suuntaan systemaattiset virheet olisivat muuttaneet tulosta? Jos tunnettu arvo jää epävarmuusvälisi ulkopuolelle, ero ei selity pelkillä lukematarkkuuksilla: mieti, mitkä Teoriaa lyhyesti -kohdan mallin ehdoista eivät ehkä täyttyneet. Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Viittaa kuvaajiin, esimerkiksi "kuvaajasta 2 nähdään, että …". Vastaa lisäksi:

- Millä perusteella LEDin kynnysjännite voidaan määrittää, ja olisiko toinen määritystapa voinut muuttaa tulosta?
- Kuinka hyvin LEDin lähettämän fotonin energiaa voidaan arvioida kynnysjännitteen avulla? Laske jokaiselle LEDille fotonin energia $\dfrac{hc}{\lambda}$ Planckin vakion tunnetulla arvolla ja vertaa sitä energiaan $eU_\text{k}$.
- Onko ero tuloksesi ja tunnetun arvon välillä mittausepävarmuuden rajoissa, vai viittaako se mallin likimääräisyyteen?

Vertaa tulosta ennusteeseesi: mikä osui oikeaan ja mikä ei?

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla (kuvaajista ja tuloksista ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]) ja käy läpi sen kaikki osat. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tausta ja teoria:** fotonin energia, periaate $eU_\text{k} \approx hf$ ehtoineen ja perustelu kuvaajan akseleille.
- **Koejärjestely ja menetelmä:** kytkentäkaavio, mistä LEDien aallonpituudet ovat peräisin ja miten määritit kynnysjännitteen.
- **Mittaustulokset:** jokaisen LEDin mittaussarja omana taulukkonaan ja yhteenvetotaulukko, jossa johdetut suureet ovat mitattujen oikealla puolella.
- **Tulos:** $h = (h \pm \Delta h)\ \text{J}\cdot\text{s}$ oikein pyöristettynä ja poikkeama tunnetusta arvosta.
- **Luotettavuus:** konkreettiset epävarmuuden lähteet, niiden vaikutuksen suunta ja mallin rajat.

## Laajennus: aallonpituudet itse hilalla

Tietolehden aallonpituuden sijasta voit mitata LEDin aallonpituuden itse. Spektrometri näyttää valon aallonpituusjakauman suoraan, jos koulussa on sellainen. Hilassa on tiheässä hyvin kapeita rakoja, ja se taivuttaa eri aallonpituuksia eri suuntiin. Lähin sivukuva eli ensimmäisen kertaluvun kuva syntyy kulmaan $\theta$, jolle pätee

```latex
d\sin\theta = \lambda
```

missä $d$ on hilan kahden vierekkäisen raon välimatka eli hilavakio ja $\lambda$ valon aallonpituus. Jos hilaan on merkitty rakojen määrä millimetrillä $N$, hilavakio on $d = \dfrac{1\ \text{mm}}{N}$. Hilaa ja valon diffraktiota käsitellään tarkemmin moduulissa FY7.

<svg data-fig="grating" viewBox="0 0 600 360" role="img" aria-label="Kaaviokuva ylhäältä. Vasemmalla on kapea rako, jonka takana on LED, ja raon kohdalla poikittainen mitta-asteikko. Oikealla etäisyydellä L asteikosta on hila ja sen takana silmä. Valo kulkee raosta suoraan hilaan. Silmä näkee raon värillisen kuvan asteikolla etäisyydellä x raosta, suunnassa, joka poikkeaa kulman theta verran raon suunnasta." style="max-width:100%;font-size:24px">
  <rect x="104" y="40" width="12" height="280" fill="#ffe8a3" stroke="#1f2933" stroke-width="2"/>
  <line x1="116" y1="52" x2="126" y2="52" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="116" y1="72" x2="122" y2="72" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="116" y1="92" x2="122" y2="92" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="116" y1="112" x2="122" y2="112" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="116" y1="132" x2="122" y2="132" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="116" y1="152" x2="126" y2="152" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="116" y1="172" x2="122" y2="172" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="116" y1="192" x2="122" y2="192" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="116" y1="212" x2="122" y2="212" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="116" y1="232" x2="122" y2="232" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="116" y1="252" x2="126" y2="252" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="116" y1="272" x2="122" y2="272" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="116" y1="292" x2="122" y2="292" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="116" y1="312" x2="122" y2="312" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="102" y="245" width="16" height="10" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="48" y="234" width="34" height="32" rx="6" fill="#f2a69c" stroke="#1f2933" stroke-width="2"/>
  <foreignObject x="4" y="239" width="36" height="22" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:18px;color:#6b7480">$\text{LED}$</div></foreignObject>
  <line x1="470" y1="160" x2="470" y2="300" stroke="#1f2933" stroke-width="4" stroke-linecap="butt"/>
  <line x1="466" y1="166" x2="474" y2="166" stroke="#ffffff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="466" y1="179" x2="474" y2="179" stroke="#ffffff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="466" y1="192" x2="474" y2="192" stroke="#ffffff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="466" y1="205" x2="474" y2="205" stroke="#ffffff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="466" y1="218" x2="474" y2="218" stroke="#ffffff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="466" y1="231" x2="474" y2="231" stroke="#ffffff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="466" y1="244" x2="474" y2="244" stroke="#ffffff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="466" y1="257" x2="474" y2="257" stroke="#ffffff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="466" y1="270" x2="474" y2="270" stroke="#ffffff" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="466" y1="283" x2="474" y2="283" stroke="#ffffff" stroke-width="1.5" stroke-linecap="butt"/>
  <foreignObject x="480" y="134" width="50" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:20px;color:#6b7480">$\text{hila}$</div></foreignObject>
  <path d="M500,236 Q526,220 552,250 Q526,280 500,264" fill="#ffffff" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="516" cy="250" r="8" fill="#1f2933"/>
  <foreignObject x="510" y="282" width="60" height="24" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:#6b7480">$\text{silmä}$</div></foreignObject>
  <line x1="118" y1="250" x2="455" y2="250" stroke="#2b8a3e" stroke-width="3" stroke-linecap="butt"/>
  <path d="M468,250 L454,256.5 L454,243.5 Z" fill="#2b8a3e" stroke-linejoin="round"/>
  <line x1="470" y1="250" x2="118" y2="100" stroke="#2b8a3e" stroke-width="2" stroke-linecap="butt" stroke-dasharray="8 6"/>
  <circle cx="110" cy="100" r="7" fill="#b2f2bb" stroke="#2b8a3e" stroke-width="2"/>
  <path d="M400,250 A70,70 0 0 1 405.5,222.5" fill="none" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <foreignObject x="366" y="213.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$\theta$</div></foreignObject>
  <line x1="110" y1="320" x2="470" y2="320" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="110" y1="310" x2="110" y2="330" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="470" y1="310" x2="470" y2="330" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="280" y="327.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$L$</div></foreignObject>
  <line x1="82" y1="100" x2="82" y2="250" stroke="#6b7480" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="72" y1="100" x2="92" y2="100" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <line x1="72" y1="250" x2="92" y2="250" stroke="#6b7480" stroke-width="2" stroke-linecap="butt"/>
  <foreignObject x="48" y="160.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px">$x$</div></foreignObject>
</svg>

Kun katsot raon takana loistavaa LEDiä hilan läpi, näet raon sivulla värillisen kuvan. Mittaa etäisyys $L$ asteikosta hilaan ja kuvan etäisyys $x$ raosta asteikolla. Silloin $\tan\theta = \dfrac{x}{L}$, josta saat kulman $\theta$ ja edelleen aallonpituuden. Vertaa mittaamaasi aallonpituutta tietolehden arvoon epävarmuuksineen: ovatko ne sopusoinnussa? Päällekkäiset epävarmuusvälit tarkoittavat, että tulokset ovat sopusoinnussa, eivät sitä, että ne on todistettu samoiksi. Miten aallonpituuden epävarmuus vaikuttaa Planckin vakion epävarmuuteen?

Katso hilan läpi vain sellaista näkyvää valoa lähettävää LEDiä, jonka opettaja on hyväksynyt tähän, ja pidä virta niin pienenä, että LED loistaa himmeästi. UV- ja infrapuna-LEDejä ei katsota hilan läpi.

::: tuki O OO
**Vihjeitä.** Pimennä huone ja pidä hila kohtisuorassa raosta tulevaan valoon nähden. Mittaa kuva raon molemmilta puolilta ja käytä etäisyyksien keskiarvoa: silloin hilan pieni vinous kumoutuu. Mitä suurempi $L$, sitä pienempi on etäisyyksien lukemisen suhteellinen epävarmuus, kunhan kuva vielä erottuu. LED lähettää kapean aallonpituusalueen, joten kuva on hieman leveä: lue sen keskikohta.
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi kuvaajiin ja mittaustuloksiin vai siihen, mitä odotit?
- Mitä tekisit toisin, jos aloittaisit alusta?
