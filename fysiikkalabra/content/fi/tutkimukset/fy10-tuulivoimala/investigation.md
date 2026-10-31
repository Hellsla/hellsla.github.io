# Tuulivoimalan tutkiminen

> **Tutkimuskysymys:** Miten valitsemasi tekijä vaikuttaa tuulivoimalan pienoismallin tuottamaan sähkötehoon?

<svg data-fig="hero" viewBox="0 0 1200 600" role="img" aria-label="Kuvitus: työpöydän vasemmassa reunassa on puhallin, joka puhaltaa kohti tuulivoimalan pienoismallia. Ilmavirtaa kuvaavat katkoviivat kulkevat puhaltimesta roottoriin. Voimalan juurelta lähtevät johdot kulkevat säädettävään vastukseen ja kahteen yleismittariin. Puhaltimen ja voimalan välissä pöydällä on mittanauha, ja pöydällä on myös käsikäyttöinen tuulimittari ja vihko." class="fig-hero" style="max-width:100%;font-size:24px">
  <defs><linearGradient id="fy10th-wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef5f9"/><stop offset="1" stop-color="#dfe9ef"/></linearGradient><linearGradient id="fy10th-desk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e9c98a"/><stop offset="1" stop-color="#d9b26a"/></linearGradient></defs>
  <rect x="0" y="0" width="1200" height="600" fill="url(#fy10th-wall)"/>
  <rect x="0" y="430" width="1200" height="170" fill="url(#fy10th-desk)"/>
  <line x1="0" y1="452" x2="1200" y2="448" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="476" x2="1200" y2="472" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="500" x2="1200" y2="496" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="524" x2="1200" y2="520" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="548" x2="1200" y2="544" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="572" x2="1200" y2="568" stroke="#a97a35" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="0" y1="430" x2="1200" y2="430" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <ellipse cx="150" cy="438" rx="78" ry="14" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="140" y="300" width="20" height="138" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="108" y="190" width="80" height="72" rx="18" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="140" y="255" width="20" height="50" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <ellipse cx="205" cy="225" rx="46" ry="128" fill="#eef5f9" stroke="#1f2933" stroke-width="2.5"/>
  <ellipse cx="205" cy="225" rx="34.5" ry="96" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <ellipse cx="205" cy="225" rx="23" ry="64" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <ellipse cx="205" cy="225" rx="11.5" ry="32" fill="none" stroke="#1f2933" stroke-width="1.5"/>
  <line x1="205" y1="225" x2="251" y2="225" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="205" y1="225" x2="245" y2="289" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="205" y1="225" x2="228" y2="336" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="205" y1="225" x2="205" y2="353" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="205" y1="225" x2="182" y2="336" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="205" y1="225" x2="165" y2="289" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="205" y1="225" x2="159" y2="225" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="205" y1="225" x2="165" y2="161" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="205" y1="225" x2="182" y2="114" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="205" y1="225" x2="205" y2="97" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="205" y1="225" x2="228" y2="114" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <line x1="205" y1="225" x2="245" y2="161" stroke="#1f2933" stroke-width="1.2" stroke-linecap="butt"/>
  <circle cx="205" cy="225" r="12" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <path d="M275,138 C385,126 520,146.6 580,138.5" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-dasharray="14 12" stroke-linecap="round"/>
  <path d="M275,182 C385,176 520,188.8 580,185" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-dasharray="14 12" stroke-linecap="round"/>
  <path d="M275,226 C385,226 520,231.0 580,231" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-dasharray="14 12" stroke-linecap="round"/>
  <path d="M275,270 C385,276 520,273.2 580,277" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-dasharray="14 12" stroke-linecap="round"/>
  <path d="M275,314 C385,326 520,315.4 580,323.5" fill="none" stroke="#6b7480" stroke-width="2.5" stroke-linejoin="round" stroke-dasharray="14 12" stroke-linecap="round"/>
  <rect x="600" y="418" width="110" height="18" rx="4" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M654,418 L659,237 H669 L674,418 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2.5" stroke-linejoin="round"/>
  <rect x="654" y="218" width="62" height="26" rx="10" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <path d="M647.5,225.5 L655.5,199.5 L663,128 L659,125 L648,192.5 L643,221.5 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M644,241 L649.5,270.5 L672,321 L675,315 L656,258 L648,233.5 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M640.5,226.5 L626.5,223 L597,243.5 L598,253.5 L628,242 L641,238.5 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="644" cy="231" r="9" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <path d="M644,221 Q626,231 644,241 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <rect x="860" y="372" width="150" height="58" rx="6" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="872" y="386" width="126" height="18" rx="4" fill="#e8b27a" stroke="#1f2933" stroke-width="2"/>
  <line x1="878" y1="386" x2="878" y2="404" stroke="#a46a2a" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="887" y1="386" x2="887" y2="404" stroke="#a46a2a" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="896" y1="386" x2="896" y2="404" stroke="#a46a2a" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="905" y1="386" x2="905" y2="404" stroke="#a46a2a" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="914" y1="386" x2="914" y2="404" stroke="#a46a2a" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="923" y1="386" x2="923" y2="404" stroke="#a46a2a" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="932" y1="386" x2="932" y2="404" stroke="#a46a2a" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="941" y1="386" x2="941" y2="404" stroke="#a46a2a" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="950" y1="386" x2="950" y2="404" stroke="#a46a2a" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="959" y1="386" x2="959" y2="404" stroke="#a46a2a" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="968" y1="386" x2="968" y2="404" stroke="#a46a2a" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="977" y1="386" x2="977" y2="404" stroke="#a46a2a" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="986" y1="386" x2="986" y2="404" stroke="#a46a2a" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="995" y1="386" x2="995" y2="404" stroke="#a46a2a" stroke-width="1.5" stroke-linecap="butt"/>
  <rect x="912" y="356" width="22" height="28" rx="3" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <line x1="870" y1="366" x2="1000" y2="366" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="868" cy="416" r="5" fill="#1f2933"/>
  <circle cx="1002" cy="366" r="5" fill="#1f2933"/>
  <rect x="740" y="300" width="96" height="130" rx="10" fill="#ffd43b" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="750" y="310" width="76" height="110" rx="6" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="758" y="318" width="60" height="30" rx="3" fill="#b2f2bb" stroke="#1f2933" stroke-width="2"/>
  <circle cx="788" cy="380" r="17" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <line x1="788" y1="380" x2="797" y2="368" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="770" cy="408" r="5" fill="#1f2933"/>
  <circle cx="806" cy="408" r="5" fill="#1f2933"/>
  <rect x="1060" y="300" width="96" height="130" rx="10" fill="#ffd43b" stroke="#1f2933" stroke-width="2.5"/>
  <rect x="1070" y="310" width="76" height="110" rx="6" fill="#6c757d" stroke="#1f2933" stroke-width="2"/>
  <rect x="1078" y="318" width="60" height="30" rx="3" fill="#b2f2bb" stroke="#1f2933" stroke-width="2"/>
  <circle cx="1108" cy="380" r="17" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <line x1="1108" y1="380" x2="1117" y2="368" stroke="#1f2933" stroke-width="3" stroke-linecap="butt"/>
  <circle cx="1090" cy="408" r="5" fill="#1f2933"/>
  <circle cx="1126" cy="408" r="5" fill="#1f2933"/>
  <path d="M700,428 Q712,470 770,408" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M806,408 Q820,470 868,416" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1002,366 Q900,520 708,432" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1090,408 Q1000,480 868,416" fill="none" stroke="#1f2933" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <path d="M1126,408 Q1110,470 1002,366" fill="none" stroke="#6b7480" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>
  <rect x="232" y="470" width="420" height="26" rx="3" fill="#ffe8a3" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="240" y1="470" x2="240" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="250" y1="470" x2="250" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="260" y1="470" x2="260" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="270" y1="470" x2="270" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="280" y1="470" x2="280" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="290" y1="470" x2="290" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="300" y1="470" x2="300" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="310" y1="470" x2="310" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="320" y1="470" x2="320" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="330" y1="470" x2="330" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="340" y1="470" x2="340" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="350" y1="470" x2="350" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="360" y1="470" x2="360" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="370" y1="470" x2="370" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="380" y1="470" x2="380" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="390" y1="470" x2="390" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="400" y1="470" x2="400" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="410" y1="470" x2="410" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="420" y1="470" x2="420" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="430" y1="470" x2="430" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="440" y1="470" x2="440" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="450" y1="470" x2="450" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="460" y1="470" x2="460" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="470" y1="470" x2="470" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="480" y1="470" x2="480" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="490" y1="470" x2="490" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="500" y1="470" x2="500" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="510" y1="470" x2="510" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="520" y1="470" x2="520" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="530" y1="470" x2="530" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="540" y1="470" x2="540" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="550" y1="470" x2="550" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="560" y1="470" x2="560" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="570" y1="470" x2="570" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="580" y1="470" x2="580" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="590" y1="470" x2="590" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="600" y1="470" x2="600" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="610" y1="470" x2="610" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="620" y1="470" x2="620" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="630" y1="470" x2="630" y2="478" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <line x1="640" y1="470" x2="640" y2="484" stroke="#1f2933" stroke-width="1.5" stroke-linecap="butt"/>
  <g transform="translate(450,550) rotate(-12)"><rect x="-14" y="-6" width="96" height="26" rx="10" fill="#6c757d" stroke="#1f2933" stroke-width="2.5"/><circle cx="-34" cy="7" r="30" fill="#c4ccd4" stroke="#1f2933" stroke-width="2.5"/><circle cx="-34" cy="7" r="7" fill="#1f2933"/><line x1="-34" y1="7" x2="-8" y2="7" stroke="#1f2933" stroke-width="1.5"/><line x1="-34" y1="7" x2="-21" y2="29.5" stroke="#1f2933" stroke-width="1.5"/><line x1="-34" y1="7" x2="-47" y2="29.5" stroke="#1f2933" stroke-width="1.5"/><line x1="-34" y1="7" x2="-60" y2="7" stroke="#1f2933" stroke-width="1.5"/><line x1="-34" y1="7" x2="-47" y2="-15.5" stroke="#1f2933" stroke-width="1.5"/><line x1="-34" y1="7" x2="-21" y2="-15.5" stroke="#1f2933" stroke-width="1.5"/></g>
  <g transform="translate(1000,540) rotate(-5)"><rect x="-80" y="-34" width="200" height="66" rx="4" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/><line x1="-64" y1="-18" x2="104" y2="-18" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/><line x1="-64" y1="-6" x2="104" y2="-6" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/><line x1="-64" y1="6" x2="104" y2="6" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/><line x1="-64" y1="18" x2="104" y2="18" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/><line x1="-64" y1="30" x2="104" y2="30" stroke="#1971c2" stroke-width="1.5" stroke-opacity="0.6"/></g>
</svg>

Tuulivoimala muuntaa liikkuvan ilman energiaa sähköksi. Kuinka paljon sähköä siitä saadaan, riippuu monesta asiasta: tuulesta, lavoista ja siitä, mitä voimalaan on kytketty. Tässä tutkimuksessa valitset yhden tekijän, muutat sitä hallitusti ja selvität mittaamalla, miten se vaikuttaa pienoismallin tuottamaan sähkötehoon. Suunnittele, mittaa ja päättele itse: tämä sivu kertoo, mitä tutkitaan, ja tukee sinua niin paljon kuin valitsemasi työtapa lupaa.

## Tutkimustehtävä

**Selvitettävä:** miten tuulivoimalan pienoismallin sähköteho riippuu yhdestä valitsemastasi tekijästä ja millä tekijän arvoilla teho on suurin mittausalueellasi, ovatko mittaamasi erot suurempia kuin mittausten epävarmuus, ja mistä järjestelmän energiahäviöt aiheutuvat.

Tutkittavaksi tekijäksi voit valita esimerkiksi tuulen nopeuden, lapojen lukumäärän, lapojen kulman, voimalan etäisyyden puhaltimesta tai sähköisen kuormituksen eli kuormitusvastuksen.

**Päätät itse** (molemmissa työtavoissa):

- tutkittavan tekijän ja sen arvot
- mittausten ja toistojen määrän
- miten pidät muut tekijät vakioina ja miten varmistat sen
- miten luet heiluvat mittarilukemat
- kuvaajan, josta tekijän vaikutus nähdään.

Osittain ohjatussa työtavassa sivu antaa näihin tukea ja neuvoo, miten epävarmuus arvioidaan.

::: tuki I
**Itsenäinen työtapa.** Valitset lisäksi epävarmuuden arviointitavan ja perustelet kaikki valintasi itse.

Laajennus, voimalan hyötysuhteen määrittäminen, kuuluu työhösi, jos käytössäsi on tuulimittari: vertaa tulostasi laajennuksessa kerrottuun ylärajaan.
:::

## Ennusta

Kirjoita ennusteesi vihkoon tai työselostuksen hypoteesiksi ennen kuin luet eteenpäin ja ennen kuin mittaat:

1. Minkä tekijän valitsisit alustavasti? Voit vielä vaihtaa sen suunnitteluvaiheessa. Miten arvelet sähkötehon muuttuvan, kun tekijän arvo kasvaa? Luonnostele ennustamasi kuvaaja.
2. Kasvaako tai pieneneekö teho samaan suuntaan koko mittausalueella, vai voiko sillä olla suurin arvo jollakin tekijän arvolla? Perustele.
3. Vain osa voimalaa pyörittävän tuulen energiasta muuttuu sähköksi. Mihin loput energiasta joutuu?
4. Mitkä asiat voivat muuttua mittauksen aikana huomaamattasi, ja miten ne näkyisivät tuloksissa?

Perustele ennusteesi fysiikan avulla. Palaat siihen johtopäätöksissä.

## Tutkimuskysymyksestä mitattaviksi suureiksi

Tutkimuskysymyksessä on kaksi suuretta: valitsemasi tekijä ja sähköteho. Ennen kuin luet eteenpäin, kirjaa:

1. Mikä on muuttuja, jota muutat, ja miten muutat ja mittaat sen arvoa?
2. Mitä suureita mittaat jokaisella tekijän arvolla, jotta saat sähkötehon selville?
3. Mitkä muut tekijät vaikuttavat sähkötehoon, ja miten pidät ne vakioina?

## Teoriaa lyhyesti

Tuuli pyörittää voimalan roottoria, ja roottorin akseli pyörittää generaattoria, joka muuntaa pyörimisen energian sähköenergiaksi. Generaattoriin kytketty kuorma, tässä kuormitusvastus, muuntaa sähköenergian lämmöksi. Energiaketjun jokaisessa vaiheessa osa energiasta muuttuu muuksi kuin siksi, mitä seuraava vaihe tarvitsee. [[apua:fy4-15|Vesi- ja tuulivoima energian muuntajina]]

**Teho** kertoo, kuinka paljon energiaa muuntuu tai siirtyy aikayksikössä: $P = \dfrac{\Delta E}{\Delta t}$. Voimalan **sähköteho** on energia, jonka generaattori siirtää kuormaan sekunnissa. [[apua:fy2-3|Teho]]

Sähkötehoa ei yleensä lueta suoraan mittarista, vaan se lasketaan kahdesta mitattavasta suureesta. **Sähkövirta** $I$ kertoo, kuinka paljon sähkövarausta kulkee kuorman läpi sekunnissa. Sen yksikkö on ampeeri, $1\ \text{A} = 1\ \text{C/s}$, missä coulomb $\text{C}$ on varauksen yksikkö. **Jännite** $U$ kertoo, kuinka paljon energiaa varaus luovuttaa kuormaan varausyksikköä kohti. Sen yksikkö on voltti, $1\ \text{V} = 1\ \text{J/C}$. Kun jännite ja sähkövirta kerrotaan, saadaan kuormaan sekunnissa siirtyvä energia eli sähköteho:

```latex
P = UI
```

missä $P$ on sähköteho, $U$ kuorman napojen välinen jännite ja $I$ kuorman läpi kulkeva sähkövirta. Yksiköt sopivat yhteen: $\text{V} \cdot \text{A} = \dfrac{\text{J}}{\text{C}} \cdot \dfrac{\text{C}}{\text{s}} = \dfrac{\text{J}}{\text{s}} = \text{W}$. Sähkötehoa ja virtapiirejä käsitellään tarkemmin moduulissa FY6.

Jännitemittari kytketään **rinnan** kuorman kanssa eli kuorman napoihin. Virtamittari kytketään **sarjaan** kuorman kanssa, jolloin sama sähkövirta kulkee mittarin ja kuorman läpi. Kuvassa on yksi tapa kytkeä mittarit. Tarkista opettajalta, tuottaako pienoismallisi generaattori tasa- vai vaihtojännitettä, ja aseta mittarit sen mukaan. Vaihtojännitealueella mittarit näyttävät jännitteen ja sähkövirran tehollisarvot, ja vastuskuormalla niiden tulo $P = UI$ on silloinkin kuormaan siirtyvä keskimääräinen teho.

<svg data-fig="circuit" viewBox="0 0 600 290" role="img" aria-label="Kytkentäkaavio. Vasemmalla on generaattori G. Siitä lähtevässä yläjohtimessa on virtamittari A sarjassa, ja johdin jatkuu oikealle säädettävään kuormitusvastukseen, joka on piirretty suorakulmiona, jonka läpi kulkee vino nuoli. Jännitemittari V on kytketty kuormitusvastuksen rinnalle sen kumpaankin napaan. Alajohdin palaa vastukselta generaattorille. Yläjohtimeen on merkitty sähkövirta I ja jännitemittarin viereen jännite U." style="max-width:100%;font-size:24px">
  <line x1="90" y1="70" x2="90" y2="128" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="90" y1="192" x2="90" y2="250" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="90" y1="70" x2="219" y2="70" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="271" y1="70" x2="390" y2="70" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="390" y1="70" x2="390" y2="120" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="390" y1="200" x2="390" y2="250" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="90" y1="250" x2="390" y2="250" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="90" cy="160" r="32" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="80" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{G}$</div></foreignObject>
  <circle cx="245" cy="70" r="26" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="235" y="55.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{A}$</div></foreignObject>
  <line x1="120" y1="70" x2="166" y2="70" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <path d="M178,70 L165,76 L165,64 Z" fill="#1f2933" stroke-linejoin="round"/>
  <foreignObject x="139" y="31.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$I$</div></foreignObject>
  <rect x="375" y="120" width="30" height="80" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <line x1="356" y1="214" x2="417.5" y2="116" stroke="#1f2933" stroke-width="2" stroke-linecap="butt"/>
  <path d="M424,106 L422,120 L412,114 Z" fill="#1f2933" stroke-linejoin="round"/>
  <line x1="390" y1="96" x2="520" y2="96" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="520" y1="96" x2="520" y2="134" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="520" y1="186" x2="520" y2="226" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <line x1="520" y1="226" x2="390" y2="226" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="390" cy="96" r="5" fill="#1f2933"/>
  <circle cx="390" cy="226" r="5" fill="#1f2933"/>
  <circle cx="520" cy="160" r="26" fill="#ffffff" stroke="#1f2933" stroke-width="2.5"/>
  <foreignObject x="510" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$\text{V}$</div></foreignObject>
  <foreignObject x="554" y="145.5" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$U$</div></foreignObject>
  <foreignObject x="132" y="187.5" width="158" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px;color:#6b7480">$\text{generaattori}$</div></foreignObject>
  <foreignObject x="169" y="125.5" width="195" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-end;height:100%;font-size:24px;color:#6b7480">$\text{kuormitusvastus}$</div></foreignObject>
</svg>

::: tuki OO
Tarkista kirjauksesi tästä. Mittaat jokaisella tekijän arvolla kuorman jännitteen $U$ ja sähkövirran $I$ ja lasket niistä sähkötehon $P = UI$. Kaikki luettelon tekijät vaikuttavat tehoon, joten muuta vain yhtä kerrallaan ja pidä muut samoina:

| Tekijä | Miten muutat ja mittaat sitä | Mitä pidät vakiona |
|---|---|---|
| tuulen nopeus $v$ | puhaltimen nopeusasetus; mittaa $v$ tuulimittarilla voimalan kohdalta | lavat, lapakulma, kuorma, voimalan paikka |
| lapojen lukumäärä | vaihda lapoja, sijoita ne tasaisesti navan ympärille | lapojen muoto ja kulma, tuuli, kuorma, paikka |
| lapakulma | aseta kaikki lavat samaan kulmaan; lue kulma navan asteikosta tai astelevyllä | lapojen määrä, tuuli, kuorma, paikka |
| etäisyys puhaltimesta | mittaa etäisyys puhaltimen ritilästä roottoriin | puhaltimen asetus, lavat, kuorma, voimala puhaltimen keskilinjalla |
| kuormitusvastus $R$ | säädä vastusta; lue arvo vastuksen asteikolta tai laske mittauksistasi $R = \dfrac{U}{I}$ | tuuli, lavat, lapakulma, paikka |

Kuorman resistanssi $R = \dfrac{U}{I}$ kertoo, kuinka suuri jännite tarvitaan kuljettamaan kuorman läpi tietty sähkövirta. Sitä käsitellään moduulissa FY6.
:::

## Suunnittele

Ennen mittaamista päätä ja kirjaa ylös, mitä tekijää muutat, mitkä sen arvot valitset, mitä mittaat ja mitä pidät vakiona. Kokeile järjestelyä ensin: lähteekö roottori pyörimään kaikilla valitsemillasi arvoilla, ja kuinka paljon mittarilukemat heiluvat?

::: tuki OO
**Osittain ohjattu.** Valitse tekijä, jonka arvoa pystyt muuttamaan ainakin viidessä vaiheessa. Lapojen lukumäärässä riittää se, mitä välineistössä on. Päätä itse arvot, toistojen määrä ja lukutapa. Kirjaa päätöksesi perusteluineen.

Mieti ainakin näitä:

- Miten merkitset voimalan ja puhaltimen paikat, jotta ne pysyvät samoina koko mittauksen ajan, ellei juuri etäisyyttä tutkita?
- Kuinka kauan odotat jokaisen muutoksen jälkeen, ennen kuin luet mittarit?
- Lukemat heiluvat, koska puhaltimen ilmavirta on pyörteinen. Luetko useita lukemia ja lasket niistä keskiarvon, vai tallennatko jännitteen ja sähkövirran antureilla?
- Miten luet jännitteen ja sähkövirran samaan aikaan, kun ne ovat eri mittareissa?
:::

::: tuki OO
**Vihjeitä tekijöittäin.**

- **Kuormitusvastus.** Kun generaattorista otetaan sähkövirtaa, generaattori vastustaa roottorin pyörimistä. Käy läpi laaja resistanssialue, myös aivan pienet ja hyvin suuret arvot.
- **Tuulen nopeus.** Puhaltimessa on yleensä vain muutama nopeusasetus. Mittaa tuulen nopeus voimalan paikalta niin, että voimala on siirretty sivuun, koska roottori hidastaa ilmaa edessään. Ilmavirta ei ole tasainen: mittaa useasta kohdasta roottorin alueelta.
- **Etäisyys.** Etäisyyden muuttaminen muuttaa voimalaan osuvaa ilmavirtaa. Jos mittaat lisäksi tuulen nopeuden jokaisella etäisyydellä, voit tarkastella tehoa myös tuulen nopeuden funktiona.
- **Lapojen lukumäärä ja kulma.** Päätä, mistä lapakulma mitataan, esimerkiksi lavan ja roottorin pyörimistason välistä, ja käytä samaa tapaa koko ajan. Pidä roottori tasapainossa: epäsymmetrinen roottori tärisee.
:::

## Mittaa

Kirjaa alkuperäiset mittarilukemat taulukkoon heti mittauksen aikana. Laskemasi teho saa oman sarakkeensa mitattujen oikealle puolelle. Kirjaa myös vakioina pitämiesi tekijöiden arvot, esimerkiksi etäisyys ja puhaltimen asetus.

::: tuki OO
Voit käyttää esimerkiksi tällaista taulukkoa. Kirjaa jokainen toisto omalle rivilleen ja laske kunkin tekijän arvon tehoista keskiarvo $\bar{P}$ erilliseen taulukkoon, jossa on tekijän arvo, $\bar{P}$ ja sen epävarmuus $\Delta P$.

| tekijän arvo (yksikkö) | toisto | $U\ (\text{V})$ | $I\ (\text{A})$ | $P = UI\ (\text{W})$ |
|---|---|---|---|---|
| | 1. | | | |
| | 2. | | | |
| | 3. | | | |

Lue jännite ja sähkövirta mahdollisimman samaan aikaan, esimerkiksi niin, että kaksi ryhmäläistä lukee kumpikin oman mittarinsa sovitusta merkistä. Jos lukemat heiluvat, kirjaa myös heilahtelun pienin ja suurin arvo: heilahtelu on tässä työssä usein suurempi kuin mittarin lukematarkkuus.
:::

Muista mittausepävarmuus: kirjaa, kuinka tarkasti luet mittarit ja kuinka paljon lukemat vaihtelevat. [[apua:fy1-3|Mittausepävarmuus ja toistomittaukset]]

## Käsittele tulokset

Laske sähköteho jokaisella tekijän arvolla. Piirrä mittaustuloksista kuvaaja, josta näkyy, miten sähköteho riippuu tutkimastasi tekijästä. Merkitse akseleille suureet ja yksiköt. Piirrä mittauspisteet, älä yhdistä niitä murtoviivalla. Sovita pisteisiin suora tai käyrä vain, jos sille on fysikaaliset perusteet. [[apua:fy1-4|Kuvaajan laatiminen ja tulkinta]]

::: tuki OO
Valitse pystyakselille sähköteho $\bar{P}$ ja vaaka-akselille tutkimasi tekijä. Merkitse jokaiseen pisteeseen pystysuora virhejana, jonka pituus kumpaankin suuntaan on tehon epävarmuus $\Delta P$: silloin näet suoraan, ovatko pisteiden väliset erot epävarmuutta suurempia. Lapojen lukumäärällä on vain kokonaislukuarvoja, joten sen kuvaajassa pisteiden välille ei piirretä käyrää. Jos tutkit tuulen nopeutta, voit kokeilla, ovatko pisteet suoralla, kun vaaka-akselille valitaan $v^3$ (katso laajennus). Pisteiden pitäisi osua suoralle vain, jos hyötysuhde ei muutu tuulen nopeuden mukana.
:::

Vastaa:

1. Miten sähköteho muuttuu, kun tekijän arvo kasvaa? Onko teholla suurin arvo mittausalueellasi?
2. Millä tekijän arvoilla voimala toimii parhaiten, ja kuinka tarkasti voit sanoa sen kuvaajasta?
3. Ovatko pisteiden väliset erot suurempia kuin tehon epävarmuus?

Laskuihin ja kuvaajaan käytä Graphical Analysis Pro -ohjelmaa. Ruukkilabran ohjeet: [[ohje:tvt-kuvaaja|Mittauspisteiden kuvaaja]] ja [[ohje:tvt-taulukkolaskenta|Taulukko ja lasketut sarakkeet]].

## Epävarmuus ja luotettavuus

Arvioi tehon epävarmuus $\Delta P$ jokaisessa mittauspisteessä, vähintään parhaassa pisteessä ja sen naapuripisteissä, jotta voit verrata pisteiden välisiä eroja epävarmuuteen. Ilmoita sähköteho epävarmuuksineen ainakin sillä tekijän arvolla, jolla voimala toimi parhaiten, muodossa $P = (P \pm \Delta P)\ \text{W}$, ja perustele, miten arvioit epävarmuuden.

::: tuki OO
Tehon epävarmuuden voit arvioida näin:

- **Jännitteen ja sähkövirran epävarmuus.** Käytä epävarmuutena $\Delta U$ ja $\Delta I$ suurempaa seuraavista: mittarin lukematarkkuus tai heilahtelun vaihteluvälin puolikas.
- **Tulon epävarmuus.** Kun suureet kerrotaan, niiden suhteelliset epävarmuudet lasketaan yhteen: $\dfrac{\Delta P}{P} = \dfrac{\Delta U}{U} + \dfrac{\Delta I}{I}$.
- **Toistot.** Jos teit toistoja, arvioi keskiarvon epävarmuus myös toistojen vaihteluvälin puolikkaana, $\Delta P = \dfrac{P_\text{max} - P_\text{min}}{2}$, ja käytä suurempaa näistä kahdesta arviosta.

Pyöristä $\Delta P$ yhteen merkitsevään numeroon ja $P$ samaan desimaaliin.
:::

Pohdi sitten luotettavuutta konkreettisesti: mitkä tekijät saattoivat muuttua, vaikka yritit pitää ne vakioina? Olivatko virheet satunnaisia vai systemaattisia, ja mihin suuntaan systemaattiset virheet olisivat muuttaneet tulosta? Miten parantaisit mittausta?

## Johtopäätökset

Vastaa tutkimuskysymykseen mittaustesi perusteella. Miten valitsemasi tekijä vaikutti sähkötehoon, ja millä käyttöalueella voimala toimi parhaiten? Mistä järjestelmän energiahäviöt aiheutuvat? Viittaa kuvaajaan, esimerkiksi "kuvaajasta 1 nähdään, että …". Vertaa tulosta ennusteeseesi: mikä osui oikeaan ja mikä ei?

## Raportoi

Kirjoita työstä työselostus FY10:n työselostuspohjalla ja käy läpi sen kaikki osat. Kuvaajien ja tulosten esittämisessä auttaa ohje [[ohje:tvt-tyoselostus|Kuvaajat ja tulokset työselostukseen]]. Tässä tutkimuksessa erityisen tärkeitä ovat nämä:

- **Tutkimuskysymys ja hypoteesi:** valitsemasi tekijä ja ennusteesi perusteluineen.
- **Koejärjestely ja menetelmä:** mitä muutit, mitä mittasit ja mitä pidit vakiona, miten varmistit sen, sekä kytkentäkaavio.
- **Mittaustulokset:** alkuperäiset jännitteen ja sähkövirran lukemat omissa sarakkeissaan ja teho niiden oikealla puolella.
- **Tulos:** kuvaaja, teho epävarmuuksineen oikein pyöristettynä ja voimalan paras käyttöalue.
- **Luotettavuus:** energiahäviöt ja ne tekijät, jotka vaikuttivat mittaustulosten luotettavuuteen.

## Laajennus: tuulivoimalan hyötysuhde

Kuinka suuri osa tuulen tehosta muuttuu sähköksi? Roottorin läpi virtaavan tuulen teho on

```latex
P_\text{tuuli} = \tfrac{1}{2}\rho A v^3
```

missä $\rho$ on ilman tiheys (huoneilmassa noin $1{,}2\ \text{kg/m}^3$; tiheys riippuu lämpötilasta ja ilmanpaineesta), $A = \pi r^2$ roottorin pyyhkäisemä pinta-ala, $r$ roottorin säde eli etäisyys navan keskeltä lavan kärkeen ja $v$ tuulen nopeus. Malli olettaa, että tuuli puhaltaa kohtisuoraan roottoria kohti ja sen nopeus on sama koko pinta-alalla. Nopeus $v$ on tuulen nopeus ennen kuin roottori hidastaa ilmaa. [[apua:fy4-15|Tuulivoimalan teho]]

<svg data-fig="swept" viewBox="0 0 600 340" role="img" aria-label="Kaaviokuva. Vasemmalla roottori edestä: kolmen lavan kärjet piirtävät pyöriessään katkoviivalla merkityn ympyrän. Ympyrän säde r on etäisyys navan keskeltä lavan kärkeen, ja ympyrän pinta-ala on roottorin pyyhkäisemä pinta-ala A, joka on pii kertaa r toiseen. Oikealla sama roottori sivulta: kolme sinistä nopeusnuolta v osoittaa vasemmalta kohti roottoria, kohtisuoraan roottorin tasoa vastaan." style="max-width:100%;font-size:24px">
  <circle cx="165" cy="160" r="118" fill="#eef5f9" stroke="#6b7480" stroke-width="2" stroke-dasharray="7 6"/>
  <path d="M171,152 L180,118.5 L172,42 L162,42 L160.5,118.5 L159,152 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M169,169 L193.5,193.5 L264,225 L268.5,216.5 L203,177 L175,159 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M155,159 L121.5,167.5 L59.5,213 L64.5,221.5 L131.5,184.5 L161,169 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="165" cy="160" r="9" fill="#c4ccd4" stroke="#1f2933" stroke-width="2"/>
  <line x1="165" y1="160" x2="267" y2="101" stroke="#1f2933" stroke-width="2.5" stroke-linecap="butt"/>
  <circle cx="267" cy="101" r="4" fill="#1f2933"/>
  <foreignObject x="230" y="118" width="20" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:flex-start;height:100%;font-size:24px">$r$</div></foreignObject>
  <foreignObject x="130" y="295.5" width="70" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px">$A = \pi r^2$</div></foreignObject>
  <rect x="476" y="42" width="8" height="236" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <rect x="482" y="148" width="56" height="24" rx="8" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>
  <path d="M478,150 Q460,160 478,170 Z" fill="#c4ccd4" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <path d="M502,172 L498,318 H518 L514,172 Z" fill="#ffffff" stroke="#1f2933" stroke-width="2" stroke-linejoin="round"/>
  <line x1="330" y1="80" x2="439" y2="80" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M454,80 L438,87 L438,73 Z" fill="#1971c2" stroke-linejoin="round"/>
  <line x1="330" y1="160" x2="439" y2="160" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M454,160 L438,167 L438,153 Z" fill="#1971c2" stroke-linejoin="round"/>
  <line x1="330" y1="240" x2="439" y2="240" stroke="#1971c2" stroke-width="4" stroke-linecap="butt"/>
  <path d="M454,240 L438,247 L438,233 Z" fill="#1971c2" stroke-linejoin="round"/>
  <foreignObject x="363.5" y="41.5" width="33" height="29" overflow="visible"><div xmlns="http://www.w3.org/1999/xhtml" class="fig-tex" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:24px;color:#1971c2">$\overline{v}$</div></foreignObject>
</svg>

Voimalan **hyötysuhde** on sen antaman sähkötehon $P$ ja tuulen tehon suhde: [[apua:fy2-4|Hyötysuhde]]

```latex
\eta = \frac{P}{P_\text{tuuli}}
```

Edes ihanteellinen roottori ei voi muuttaa käyttökelpoiseksi kuin noin $59\ \%$ läpi virtaavan tuulen tehosta, koska ilman on päästävä virtaamaan pois roottorin takaa. Tätä ylärajaa kutsutaan Betzin rajaksi. Todellisessa voimalassa osa energiasta menetetään lisäksi kitkaan ja generaattorissa, joten hyötysuhde jää rajan alle.

Määritä voimalan hyötysuhde epävarmuuksineen ainakin sillä tekijän arvolla, jolla voimala toimi parhaiten, ja selvitä, minkä suureen epävarmuus vaikuttaa tulokseen eniten. Onko tuloksesi uskottava, kun vertaat sitä Betzin rajaan? Miten tuulen epätasaisuus voi vaikuttaa tulokseen?

::: tuki OO
**Vihjeitä.** Mittaa tuulen nopeus useasta kohdasta tasaisesti roottorin alueelta voimala sivuun siirrettynä. Koska tuulen teho on verrannollinen nopeuden kuutioon, laske keskiarvo luvuista $v^3$, älä korota nopeuksien keskiarvoa kolmanteen potenssiin. Hyötysuhteen suhteellinen epävarmuus on suhteellisten epävarmuuksien summa, ja potenssi kertoo, kuinka monta kertaa suure lasketaan mukaan:

```latex
\begin{aligned}
\frac{\Delta \eta}{\eta} &= \frac{\Delta P}{P} + \frac{\Delta \rho}{\rho} \\
&\quad + 2\cdot\frac{\Delta r}{r} + 3\cdot\frac{\Delta v}{v}
\end{aligned}
```

Koska käytit nopeuksien kuutioiden keskiarvoa, $v$ tarkoittaa tässä lukua $\sqrt[3]{\overline{v^3}}$, missä $\overline{v^3}$ on lukujen $v^3$ keskiarvo. Voit myös arvioida kuutioiden keskiarvon suhteellisen epävarmuuden suoraan ja käyttää sitä termin $3\cdot\dfrac{\Delta v}{v}$ paikalla. Ilman tiheyden epävarmuuden $\Delta\rho$ voit arvioida huoneen lämpötilasta ja ilmanpaineesta: katso tiheys taulukkokirjasta tai laske se näistä, ja arvioi, kuinka paljon se muuttuu, kun lämpötila ja paine vaihtelevat mittaustesi epävarmuuden verran.
:::

## Arvioi omaa työtäsi

Arvioi työtäsi työselostuspohjan muistilistalla ja vastaa lisäksi:

- Muutitko vain yhtä tekijää kerrallaan? Miten sen voi todeta mittauspöytäkirjastasi?
- Pystyisikö toinen ryhmä toistamaan mittauksesi kuvauksesi perusteella?
- Perustuuko johtopäätöksesi kuvaajaan ja mittaustuloksiin vai siihen, mitä odotit?
- Mitä tekisit toisin, jos aloittaisit alusta?
